using UnityEngine;

/// <summary>
/// Dragonfly Motor Class - Flight Pattern and Angular Momentum System
/// Implements hover dynamics and flight behavior for EV0LVerse entities
/// Part of the EV0LVerse Codex integration system
/// </summary>
public class DragonflyMotor : MonoBehaviour
{
    [Header("Flight Parameters")]
    [Tooltip("Base hover height above ground")]
    [SerializeField] private float hoverHeight = 2.0f;
    
    [Tooltip("Hover stabilization strength")]
    [SerializeField] private float hoverForce = 10f;
    
    [Tooltip("Flight wobble frequency (Hz)")]
    [SerializeField] private float wobbleFrequency = 2.0f;
    
    [Tooltip("Wobble amplitude")]
    [SerializeField] private float wobbleAmplitude = 0.1f;
    
    [Header("Angular Momentum")]
    [Tooltip("Base rotation speed")]
    [SerializeField] private float rotationSpeed = 45f;
    
    [Tooltip("Angular momentum damping")]
    [SerializeField] private float angularDamping = 0.95f;
    
    [Header("Flight Mode")]
    [SerializeField] private FlightMode currentMode = FlightMode.Hover;
    
    // Internal state
    private Vector3 targetPosition;
    private float currentAngularMomentum = 0f;
    private Rigidbody rb;
    
    public enum FlightMode
    {
        Hover,      // Stationary hovering
        Patrol,     // Slow movement
        Combat,     // Evasive maneuvers
        Cruise      // Efficient travel
    }
    
    void Start()
    {
        rb = GetComponent<Rigidbody>();
        
        // Configure rigidbody for flight
        if (rb != null)
        {
            rb.useGravity = false;
            rb.drag = 0.5f;
            rb.angularDrag = angularDamping;
        }
        
        targetPosition = transform.position;
    }
    
    void FixedUpdate()
    {
        ApplyHoverForce();
        ApplyWobble();
        ApplyAngularMomentum();
    }
    
    /// <summary>
    /// Apply hover stabilization force
    /// </summary>
    private void ApplyHoverForce()
    {
        if (rb == null) return;
        
        // Raycast to find ground
        RaycastHit hit;
        if (Physics.Raycast(transform.position, Vector3.down, out hit, 100f))
        {
            float currentHeight = hit.distance;
            float heightError = hoverHeight - currentHeight;
            
            // Apply proportional force to maintain hover height
            Vector3 hoverCorrection = Vector3.up * (heightError * hoverForce);
            rb.AddForce(hoverCorrection);
        }
    }
    
    /// <summary>
    /// Apply realistic flight wobble for stability
    /// </summary>
    private void ApplyWobble()
    {
        // Calculate wobble based on mode
        float modeFrequency = wobbleFrequency;
        float modeAmplitude = wobbleAmplitude;
        
        switch (currentMode)
        {
            case FlightMode.Hover:
                modeFrequency = 2.0f;
                modeAmplitude = 0.1f;
                break;
            case FlightMode.Patrol:
                modeFrequency = 1.5f;
                modeAmplitude = 0.15f;
                break;
            case FlightMode.Combat:
                modeFrequency = 3.0f;
                modeAmplitude = 0.2f;
                break;
            case FlightMode.Cruise:
                modeFrequency = 1.0f;
                modeAmplitude = 0.08f;
                break;
        }
        
        // Generate wobble pattern
        float wobbleX = Mathf.Sin(Time.time * modeFrequency) * modeAmplitude;
        float wobbleZ = Mathf.Cos(Time.time * modeFrequency * 1.2f) * modeAmplitude;
        
        Vector3 wobbleOffset = new Vector3(wobbleX, 0f, wobbleZ);
        
        if (rb != null)
        {
            rb.AddForce(wobbleOffset, ForceMode.VelocityChange);
        }
        else
        {
            transform.position += wobbleOffset * Time.fixedDeltaTime;
        }
    }
    
    /// <summary>
    /// Apply angular momentum for rotation
    /// </summary>
    private void ApplyAngularMomentum()
    {
        // Calculate rotation speed based on mode
        float modeRotationSpeed = rotationSpeed;
        
        switch (currentMode)
        {
            case FlightMode.Hover:
                modeRotationSpeed = 0.5f * rotationSpeed;
                break;
            case FlightMode.Patrol:
                modeRotationSpeed = 1.0f * rotationSpeed;
                break;
            case FlightMode.Combat:
                modeRotationSpeed = 2.0f * rotationSpeed;
                break;
            case FlightMode.Cruise:
                modeRotationSpeed = 0.75f * rotationSpeed;
                break;
        }
        
        // Update angular momentum with damping
        currentAngularMomentum = currentAngularMomentum * angularDamping + 
                                modeRotationSpeed * Time.fixedDeltaTime;
        
        // Apply rotation
        transform.Rotate(Vector3.up, currentAngularMomentum * Time.fixedDeltaTime);
    }
    
    /// <summary>
    /// Change flight mode
    /// </summary>
    public void SetFlightMode(FlightMode newMode)
    {
        currentMode = newMode;
        Debug.Log($"[Dragonfly Motor] Flight mode changed to: {newMode}");
    }
    
    /// <summary>
    /// Get current angular momentum value
    /// </summary>
    public float GetAngularMomentum()
    {
        return currentAngularMomentum;
    }
    
    /// <summary>
    /// Add impulse angular momentum (for evasive maneuvers)
    /// </summary>
    public void AddAngularImpulse(float impulse)
    {
        currentAngularMomentum += impulse;
        Debug.Log($"[Dragonfly Motor] Angular impulse: {impulse:F2}°/s");
    }
}
