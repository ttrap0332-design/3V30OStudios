using UnityEngine;

/// <summary>
/// ES0IL Core - Environmental Semantic Organic Intelligence Layer
/// Placeholder implementation for resource extraction and environmental pressure simulation
/// Part of the EV0LVerse Codex integration system
/// </summary>
public class ES0ILCore : MonoBehaviour
{
    [Header("Resource Parameters")]
    [Tooltip("Base resource extraction rate")]
    [SerializeField] private float baseExtractionRate = 1.0f;
    
    [Tooltip("Environmental pressure multiplier (0.5 - 1.5)")]
    [SerializeField] private float environmentalPressure = 1.0f;
    
    [Tooltip("Resource regeneration rate")]
    [SerializeField] private float regenerationRate = 0.1f;
    
    [Header("Resource State")]
    [SerializeField] private float currentResources = 100f;
    [SerializeField] private float maxResources = 200f;
    
    // Singleton instance
    private static ES0ILCore instance;
    public static ES0ILCore Instance => instance;
    
    void Awake()
    {
        // Singleton pattern
        if (instance == null)
        {
            instance = this;
            DontDestroyOnLoad(gameObject);
        }
        else
        {
            Destroy(gameObject);
        }
    }
    
    void Update()
    {
        // Simulate environmental pressure oscillation
        environmentalPressure = 1.0f + 0.5f * Mathf.Sin(Time.time * 0.5f);
        
        // Regenerate resources over time
        currentResources += regenerationRate * Time.deltaTime;
        currentResources = Mathf.Clamp(currentResources, 0, maxResources);
    }
    
    /// <summary>
    /// Get current resource pressure for binding to spiral systems
    /// </summary>
    public float GetResourcePressure()
    {
        return environmentalPressure;
    }
    
    /// <summary>
    /// Extract resources from the environment
    /// Returns amount extracted (may be less than requested)
    /// </summary>
    public float ExtractResources(float amount)
    {
        float extracted = Mathf.Min(amount, currentResources);
        currentResources -= extracted;
        
        Debug.Log($"[ES0IL Core] Extracted {extracted:F2} resources. " +
                 $"Remaining: {currentResources:F2}/{maxResources:F2}");
        
        return extracted;
    }
    
    /// <summary>
    /// Check if sufficient resources are available
    /// </summary>
    public bool HasSufficientResources(float amount)
    {
        return currentResources >= amount;
    }
    
    /// <summary>
    /// Get current resource level as percentage
    /// </summary>
    public float GetResourceLevel()
    {
        return currentResources / maxResources;
    }
}
