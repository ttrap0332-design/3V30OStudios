using UnityEngine;

/// <summary>
/// SpiralMovement - Implements spiral motion patterns using polar coordinate transformations
/// Part of the EV0LVerse Codex System
/// 
/// This script generates spiral trajectories through:
/// - Polar to Cartesian coordinate conversion (r, θ) → (x, y, z)
/// - Incremental angular velocity updates over time
/// - Configurable radial growth/decay for spiral expansion
/// - ES0IL Core integration for resource-based motion scaling
/// - Dragonfly Motor Class compatibility for flight patterns
/// </summary>
public class SpiralMovement : MonoBehaviour
{
    [Header("Spiral Parameters")]
    [Tooltip("Angular velocity in degrees per second")]
    [SerializeField] private float angularVelocity = 45f;
    
    [Tooltip("Rate of radial growth/decay per second")]
    [SerializeField] private float radiusGrowthRate = 0.5f;
    
    [Tooltip("Initial radius of the spiral")]
    [SerializeField] private float initialRadius = 1f;
    
    [Tooltip("Maximum radius before reset or reversal")]
    [SerializeField] private float maxRadius = 10f;
    
    [Tooltip("Minimum radius (for inward spirals)")]
    [SerializeField] private float minRadius = 0.1f;
    
    [Tooltip("Phase offset in degrees for spiral start position")]
    [SerializeField] private float phaseOffset = 0f;
    
    [Tooltip("Spiral tightness factor (affects the spiral's density)")]
    [SerializeField] private float spiralTightness = 1f;
    
    [Tooltip("Direction of spiral rotation: 1 = counterclockwise, -1 = clockwise")]
    [SerializeField] private int rotationDirection = 1;
    
    [Tooltip("Enable vertical (Y-axis) movement for 3D spirals")]
    [SerializeField] private bool enable3DSpiral = false;
    
    [Tooltip("Vertical movement speed (only if 3D spiral enabled)")]
    [SerializeField] private float verticalSpeed = 0.5f;
    
    [Header("EV0LVerse Integration")]
    [Tooltip("Link to ES0IL Core for resource-based scaling")]
    [SerializeField] private bool linkToES0ILCore = false;
    
    [Tooltip("Dragonfly Motor Class mode for flight patterns")]
    [SerializeField] private bool dragonflyMotorMode = false;
    
    [Tooltip("Hellraiser Loop trigger threshold (engine load percentage)")]
    [SerializeField] [Range(0f, 1f)] private float hellraiserThreshold = 0.75f;
    
    [Header("Debug Visualization")]
    [Tooltip("Draw spiral trajectory in Scene view")]
    [SerializeField] private bool drawGizmos = true;
    
    [Tooltip("Number of gizmo points to draw")]
    [SerializeField] private int gizmoResolution = 100;
    
    [Tooltip("Color of the spiral gizmo")]
    [SerializeField] private Color gizmoColor = Color.cyan;
    
    // Internal state
    private float currentAngle = 0f;
    private float currentRadius;
    private Vector3 centerPosition;
    private float engineLoad = 0f; // Simulated engine load for Hellraiser Loop
    private bool isHellraiserActive = false;
    
    // ES0IL Core simulation
    private float resourcePressure = 1f;
    
    // Constants for simulation
    private const float ENGINE_LOAD_FREQUENCY = 0.1f;
    private const float EMITTER_CLEANUP_TIME = 2f;
    private const float BASE_PRESSURE = 1f;
    private const float PRESSURE_AMPLITUDE = 0.5f;
    private const float PRESSURE_FREQUENCY = 0.5f;
    
    void Start()
    {
        // Initialize spiral parameters
        currentRadius = initialRadius;
        centerPosition = transform.position;
        currentAngle = phaseOffset;
        
        // Log initialization for MetaBlueprint tracking
        Debug.Log($"[SpiralMovement] Initialized at {centerPosition} with radius {initialRadius}");
    }
    
    void Update()
    {
        // Update engine load simulation (cycles between 0 and 1)
        engineLoad = Mathf.PingPong(Time.time * ENGINE_LOAD_FREQUENCY, 1f);
        
        // Check Hellraiser Loop threshold
        isHellraiserActive = engineLoad >= hellraiserThreshold;
        
        // Apply ES0IL Core resource pressure if linked
        if (linkToES0ILCore)
        {
            resourcePressure = SimulateES0ILResourcePressure();
        }
        
        // Calculate spiral motion
        UpdateSpiralPosition();
        
        // Apply Dragonfly Motor adjustments if enabled
        if (dragonflyMotorMode)
        {
            ApplyDragonflyMotorPattern();
        }
    }
    
    /// <summary>
    /// Core spiral position calculation using polar coordinates
    /// Converts (r, θ) to Cartesian (x, y, z)
    /// </summary>
    private void UpdateSpiralPosition()
    {
        // Update angle based on angular velocity and rotation direction
        float angleIncrement = angularVelocity * rotationDirection * Time.deltaTime;
        currentAngle += angleIncrement;
        
        // Apply spiral tightness factor
        float effectiveAngle = currentAngle * spiralTightness;
        
        // Update radius with growth/decay
        float radiusChange = radiusGrowthRate * Time.deltaTime;
        
        // Apply resource pressure scaling if ES0IL Core is linked
        if (linkToES0ILCore)
        {
            radiusChange *= resourcePressure;
        }
        
        // Apply Hellraiser Loop intensity boost
        if (isHellraiserActive)
        {
            radiusChange *= (1f + engineLoad);
        }
        
        currentRadius += radiusChange;
        
        // Clamp radius within bounds
        if (currentRadius >= maxRadius)
        {
            currentRadius = maxRadius;
            radiusGrowthRate *= -1; // Reverse direction
        }
        else if (currentRadius <= minRadius)
        {
            currentRadius = minRadius;
            radiusGrowthRate *= -1; // Reverse direction
        }
        
        // Polar to Cartesian conversion
        float angleRad = effectiveAngle * Mathf.Deg2Rad;
        float x = currentRadius * Mathf.Cos(angleRad);
        float z = currentRadius * Mathf.Sin(angleRad);
        float y = 0f;
        
        // Add vertical component for 3D spirals
        if (enable3DSpiral)
        {
            y = verticalSpeed * Time.time;
        }
        
        // Update transform position
        transform.position = centerPosition + new Vector3(x, y, z);
    }
    
    /// <summary>
    /// Simulates ES0IL Core resource extraction pressure
    /// Returns a multiplier based on environmental factors
    /// </summary>
    private float SimulateES0ILResourcePressure()
    {
        // Simulate resource pressure with sine wave (oscillates between 0.5 and 1.5)
        float pressure = BASE_PRESSURE + PRESSURE_AMPLITUDE * Mathf.Sin(Time.time * PRESSURE_FREQUENCY);
        return pressure;
    }
    
    /// <summary>
    /// Applies Dragonfly Motor Class flight pattern adjustments
    /// Adds angular momentum and hover behavior
    /// </summary>
    private void ApplyDragonflyMotorPattern()
    {
        // Add slight wobble for realistic flight
        float wobbleX = Mathf.Sin(Time.time * 2f) * 0.1f;
        float wobbleZ = Mathf.Cos(Time.time * 2.5f) * 0.1f;
        
        Vector3 wobble = new Vector3(wobbleX, 0f, wobbleZ);
        transform.position += wobble * Time.deltaTime;
        
        // Angular momentum visualization (rotation)
        float rotationSpeed = angularVelocity * 0.5f;
        transform.Rotate(Vector3.up, rotationSpeed * Time.deltaTime);
    }
    
    /// <summary>
    /// Triggers particle emission for Hellraiser Loop integration
    /// Called when energy surplus events occur
    /// </summary>
    public void TriggerHellraiserEmission()
    {
        if (!isHellraiserActive) return;
        
        Debug.Log($"[Hellraiser Loop] Energy surplus event triggered at load {engineLoad:F2}");
        
        // Emit spiral particles (would integrate with particle system)
        // This is a placeholder for the actual particle system integration
        GameObject emitter = new GameObject("SpiralEmitter");
        emitter.transform.position = transform.position;
        
        // Add visual effect here
        // ParticleSystem ps = emitter.AddComponent<ParticleSystem>();
        // Configure particle system to emit spiral patterns
        
        Destroy(emitter, EMITTER_CLEANUP_TIME); // Cleanup after configured time
    }
    
    /// <summary>
    /// Resets spiral to initial parameters
    /// </summary>
    public void ResetSpiral()
    {
        currentAngle = phaseOffset;
        currentRadius = initialRadius;
        transform.position = centerPosition;
        Debug.Log("[SpiralMovement] Spiral reset to initial state");
    }
    
    /// <summary>
    /// Returns current spiral state for MetaBlueprint analysis
    /// </summary>
    public SpiralState GetSpiralState()
    {
        return new SpiralState
        {
            angle = currentAngle,
            radius = currentRadius,
            engineLoad = engineLoad,
            isHellraiserActive = isHellraiserActive,
            resourcePressure = resourcePressure
        };
    }
    
    /// <summary>
    /// Draws spiral trajectory gizmos in Scene view for debugging
    /// </summary>
    private void OnDrawGizmos()
    {
        if (!drawGizmos) return;
        
        Vector3 center = Application.isPlaying ? centerPosition : transform.position;
        Gizmos.color = gizmoColor;
        
        Vector3 previousPoint = center;
        float testRadius = initialRadius;
        float testAngle = phaseOffset;
        
        for (int i = 0; i <= gizmoResolution; i++)
        {
            float t = (float)i / gizmoResolution;
            testAngle = t * 360f * spiralTightness;
            testRadius = Mathf.Lerp(initialRadius, maxRadius, t);
            
            float angleRad = testAngle * Mathf.Deg2Rad;
            float x = testRadius * Mathf.Cos(angleRad);
            float z = testRadius * Mathf.Sin(angleRad);
            float y = enable3DSpiral ? t * verticalSpeed * 10f : 0f;
            
            Vector3 point = center + new Vector3(x, y, z);
            
            if (i > 0)
            {
                Gizmos.DrawLine(previousPoint, point);
            }
            
            previousPoint = point;
        }
        
        // Draw center point
        Gizmos.color = Color.red;
        Gizmos.DrawSphere(center, 0.1f);
    }
}

/// <summary>
/// Data structure for spiral state tracking
/// Used in MetaBlueprint analysis and calibration
/// </summary>
[System.Serializable]
public struct SpiralState
{
    public float angle;
    public float radius;
    public float engineLoad;
    public bool isHellraiserActive;
    public float resourcePressure;
}
