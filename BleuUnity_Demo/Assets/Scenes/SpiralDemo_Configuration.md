# Unity Scene Configuration Guide
## SpiralDemo.unity Setup Instructions

---

## Scene Hierarchy

### 1. Main Camera
```
GameObject: Main Camera
├── Transform
│   ├── Position: (0, 10, -10)
│   ├── Rotation: (45, 0, 0)
│   └── Scale: (1, 1, 1)
└── Camera Component
    ├── Clear Flags: Skybox
    ├── Field of View: 60
    ├── Clipping Planes: Near 0.3, Far 1000
    └── Tag: MainCamera
```

**Optional:** Add `CameraFollow.cs` script to track spiral object dynamically.

---

### 2. Directional Light
```
GameObject: Directional Light
├── Transform
│   ├── Position: (0, 10, 0)
│   ├── Rotation: (50, -30, 0)
│   └── Scale: (1, 1, 1)
└── Light Component
    ├── Type: Directional
    ├── Color: White (FFFFFF)
    ├── Intensity: 1.0
    ├── Shadow Type: Soft Shadows
    └── Shadow Resolution: High
```

---

### 3. SpiralEmitter (Main Object)
```
GameObject: SpiralEmitter
├── Transform
│   ├── Position: (0, 0, 0)
│   ├── Rotation: (0, 0, 0)
│   └── Scale: (1, 1, 1)
├── SpiralMovement.cs
│   ├── Angular Velocity: 45
│   ├── Radius Growth Rate: 0.5
│   ├── Initial Radius: 2.0
│   ├── Max Radius: 8.0
│   ├── Min Radius: 0.1
│   ├── Phase Offset: 0
│   ├── Spiral Tightness: 1.0
│   ├── Rotation Direction: 1
│   ├── Enable 3D Spiral: false
│   ├── Vertical Speed: 0.5
│   ├── Link to ES0IL Core: false
│   ├── Dragonfly Motor Mode: false
│   ├── Hellraiser Threshold: 0.75
│   ├── Draw Gizmos: true
│   ├── Gizmo Resolution: 100
│   └── Gizmo Color: Cyan
├── Mesh Filter (Sphere)
├── Mesh Renderer
│   └── Material: SpiralTrailMat
└── Trail Renderer (Optional)
    ├── Time: 2.0
    ├── Width: 0.1
    ├── Color Gradient: Cyan to Transparent
    └── Material: TrailMaterial
```

---

### 4. GridFloor
```
GameObject: GridFloor
├── Transform
│   ├── Position: (0, -0.1, 0)
│   ├── Rotation: (0, 0, 0)
│   └── Scale: (10, 1, 10)
├── Mesh Filter (Plane)
└── Mesh Renderer
    └── Material: GridMaterial (with grid texture)
```

---

### 5. ES0IL Core Manager (Optional)
```
GameObject: ES0IL_Core_Manager
├── Transform
│   ├── Position: (0, 0, 0)
│   ├── Rotation: (0, 0, 0)
│   └── Scale: (1, 1, 1)
└── ES0ILCore.cs
    ├── Base Extraction Rate: 1.0
    ├── Environmental Pressure: 1.0
    ├── Regeneration Rate: 0.1
    ├── Current Resources: 100
    └── Max Resources: 200
```

---

### 6. Particle System (Hellraiser Loop)
```
GameObject: HellraiserParticles
├── Transform
│   ├── Position: (0, 0, 0)
│   ├── Rotation: (0, 0, 0)
│   └── Scale: (1, 1, 1)
└── Particle System
    ├── Duration: 1.0
    ├── Looping: false
    ├── Start Lifetime: 1.0 - 2.0
    ├── Start Speed: 2.0 - 5.0
    ├── Start Size: 0.1 - 0.3
    ├── Start Color: Cyan with alpha gradient
    ├── Shape: Cone
    │   ├── Angle: 30
    │   ├── Radius: 0.5
    │   └── Emit from: Base
    ├── Emission: Bursts (20-50 particles)
    └── Color over Lifetime: Cyan → White → Transparent
```

---

## Material Setup

### SpiralTrailMat.mat
```
Material: SpiralTrailMat
├── Shader: Standard
├── Rendering Mode: Transparent
├── Albedo: Cyan (00FFFF)
├── Metallic: 0.0
├── Smoothness: 0.5
├── Emission: Enabled
│   ├── Color: Cyan (00FFFF)
│   └── Intensity: 0.5
└── Transparency: 0.8
```

### GridMaterial.mat
```
Material: GridMaterial
├── Shader: Standard
├── Rendering Mode: Opaque
├── Albedo: Dark Gray (333333)
├── Metallic: 0.2
├── Smoothness: 0.3
└── Tiling: (10, 10)
```

---

## Scene Settings

### Lighting
```
Window → Rendering → Lighting Settings
├── Skybox Material: Default Skybox
├── Sun Source: Directional Light
├── Environment Lighting
│   ├── Source: Skybox
│   ├── Intensity Multiplier: 1.0
│   └── Ambient Mode: Skybox
├── Environment Reflections
│   ├── Source: Skybox
│   └── Resolution: 128
└── Fog
    ├── Enabled: false
    └── Mode: Exponential
```

### Physics Settings
```
Edit → Project Settings → Physics
├── Gravity: (0, -9.81, 0)
├── Default Solver Iterations: 6
├── Default Solver Velocity Iterations: 1
├── Bounce Threshold: 2.0
└── Auto Simulation: true
```

---

## Camera Follow Script (Optional)

Create `CameraFollow.cs`:

```csharp
using UnityEngine;

public class CameraFollow : MonoBehaviour
{
    [SerializeField] private Transform target;
    [SerializeField] private Vector3 offset = new Vector3(0, 10, -10);
    [SerializeField] private float smoothSpeed = 0.125f;
    [SerializeField] private bool lookAtTarget = true;
    
    void LateUpdate()
    {
        if (target == null) return;
        
        Vector3 desiredPosition = target.position + offset;
        Vector3 smoothedPosition = Vector3.Lerp(transform.position, 
                                                desiredPosition, 
                                                smoothSpeed);
        transform.position = smoothedPosition;
        
        if (lookAtTarget)
        {
            transform.LookAt(target);
        }
    }
}
```

Attach to Main Camera and assign SpiralEmitter as target.

---

## Testing Checklist

### Visual Verification
- [ ] Spiral object visible in Scene and Game views
- [ ] Gizmos draw spiral path correctly in Scene view
- [ ] Trail Renderer shows motion path
- [ ] Grid floor provides visual reference
- [ ] Lighting illuminates scene properly

### Functional Testing
- [ ] Spiral motion follows expected trajectory
- [ ] Radius expands and contracts properly
- [ ] Rotation occurs in correct direction
- [ ] 3D spiral mode creates vertical helix
- [ ] ES0IL Core pressure modulates growth
- [ ] Dragonfly Motor adds wobble
- [ ] Hellraiser triggers at threshold
- [ ] Parameter changes affect motion

### Performance Check
- [ ] FPS remains above 60 (desktop)
- [ ] No memory leaks over time
- [ ] Particle systems perform efficiently
- [ ] Gizmos can be disabled in builds

---

## Keyboard Controls (Optional)

Add input handling script:

```csharp
void Update()
{
    // Reset spiral
    if (Input.GetKeyDown(KeyCode.R))
    {
        GetComponent<SpiralMovement>().ResetSpiral();
    }
    
    // Toggle 3D mode
    if (Input.GetKeyDown(KeyCode.T))
    {
        // Toggle enable3DSpiral parameter
    }
    
    // Trigger Hellraiser
    if (Input.GetKeyDown(KeyCode.H))
    {
        GetComponent<SpiralMovement>().TriggerHellraiserEmission();
    }
}
```

---

## Export Settings

### Build Configuration
```
File → Build Settings
├── Platform: PC, Mac & Linux Standalone
├── Target Platform: Windows
├── Architecture: x86_64
├── Development Build: Checked (for testing)
└── Scenes to Build:
    └── Scenes/SpiralDemo.unity
```

### Quality Settings
```
Edit → Project Settings → Quality
├── Quality Level: High
├── V Sync Count: Every V Blank
├── Texture Quality: Full Res
├── Anisotropic Textures: Per Texture
└── Shadows: Soft Shadows
```

---

## Troubleshooting

### Issue: Spiral doesn't move
**Solution:** Verify `angularVelocity` and `radiusGrowthRate` are non-zero

### Issue: Gizmos not visible
**Solution:** Check `drawGizmos` is enabled and Scene view has Gizmos button toggled on

### Issue: Camera doesn't follow
**Solution:** Ensure CameraFollow script target is assigned to SpiralEmitter

### Issue: Trail Renderer not showing
**Solution:** Check Trail Renderer is enabled and material is assigned

### Issue: Poor performance
**Solution:** Reduce gizmo resolution, disable unnecessary particle systems, or lower quality settings

---

**Scene Configuration Version:** 1.0  
**Last Updated:** 2025-11-21  
**Compatible Unity Versions:** 2021.3 LTS+
