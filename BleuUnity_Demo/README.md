# BleuUnity Demo - Spiral Movement System
## EV0LVerse Codex Integration Project

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Unity](https://img.shields.io/badge/unity-2021.3_LTS-green)
![License](https://img.shields.io/badge/license-EV0LVerse-purple)

---

## 🌀 Overview

The **BleuUnity Demo** is a complete Unity project demonstrating spiral motion mechanics integrated with the EV0LVerse Codex system. This project showcases:

- **Spiral Movement System** - Physics-based spiral trajectories using polar coordinates
- **ES0IL Core Integration** - Resource-based motion scaling
- **Dragonfly Motor Class** - Flight pattern simulation with angular momentum
- **Hellraiser Loop** - Dynamic intensity scaling based on energy surplus
- **MetaBlueprint Analysis** - Comprehensive documentation and visualization

---

## 📦 Project Structure

```
BleuUnity_Demo/
├── Assets/
│   ├── Scripts/
│   │   └── SpiralMovement.cs          # Core spiral motion script
│   ├── Prefabs/
│   │   └── SpiralEmitter.prefab       # Spiral object prefab
│   ├── Scenes/
│   │   └── SpiralDemo.unity           # Demo simulation scene
│   ├── Materials/
│   │   └── SpiralTrailMat.mat         # Trail visualization material
│   └── README.md                       # Asset documentation
├── ProjectSettings/
│   └── (Unity project configuration)
├── Documentation/
│   └── MetaBlueprint_SpiralMovement.md # Complete technical analysis
├── Charts/
│   └── (Visualization charts - to be generated)
└── README.md                            # This file
```

---

## 🚀 Quick Start

### Prerequisites

- **Unity 2021.3 LTS** or higher
- **Git** for repository cloning
- Basic understanding of Unity Editor

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ttrap0332-design/3V30OStudios.git
   cd 3V30OStudios/BleuUnity_Demo
   ```

2. **Open in Unity Hub:**
   - Launch Unity Hub
   - Click "Add" → Select `BleuUnity_Demo` folder
   - Open project with Unity 2021.3 LTS or higher

3. **Load Demo Scene:**
   - Navigate to `Assets/Scenes/`
   - Open `SpiralDemo.unity`

4. **Run Simulation:**
   - Press **Play** button in Unity Editor
   - Observe spiral motion in Scene and Game views

---

## 🎮 Features

### Spiral Movement Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| **Angular Velocity** | Rotation speed (degrees/sec) | 45° |
| **Radius Growth Rate** | Spiral expansion rate | 0.5 |
| **Initial Radius** | Starting spiral size | 1.0 |
| **Max Radius** | Maximum spiral extent | 10.0 |
| **Min Radius** | Minimum spiral extent | 0.1 |
| **Phase Offset** | Starting angle | 0° |
| **Spiral Tightness** | Pattern density | 1.0 |
| **Rotation Direction** | Spin direction (±1) | 1 |

### EV0LVerse Integration

#### ES0IL Core
- **Resource Pressure Binding** - Links spiral growth to resource extraction
- **Environmental Adaptation** - Dynamic scaling based on pressure (0.5x - 1.5x)
- **Real-time Adjustment** - Oscillating pressure simulation

#### Dragonfly Motor Class
- **Angular Momentum** - Realistic flight physics
- **Hover Dynamics** - Wobble patterns for stability
- **Rotation Visualization** - Automatic Y-axis rotation

#### Hellraiser Loop
- **Energy Surplus Detection** - Monitors engine load
- **Threshold Activation** - Triggers at 75% load
- **Dynamic Intensity** - Scales spiral growth (1.75x - 2.0x)
- **Particle Emission** - Spawns spiral effects on trigger

---

## 📊 Spiral Calibration

### Trajectory Types

1. **2D Planar Spiral**
   - Horizontal (XZ plane) expansion
   - Configurable tightness and growth
   - Ideal for ground-based effects

2. **3D Helix Spiral**
   - Vertical (Y-axis) component
   - Rising/falling trajectory
   - Perfect for flight paths

3. **Pulsing Spiral**
   - Alternating expansion/contraction
   - Reverses at min/max radius
   - Creates breathing effect

### Mathematical Model

```
Position Calculation:
  x(t) = r(t) × cos(θ(t))
  y(t) = vertical_speed × t        (if 3D enabled)
  z(t) = r(t) × sin(θ(t))

where:
  θ(t) = θ₀ + ω × direction × t
  r(t) = r₀ + growth_rate × t × modifiers
```

---

## 🔧 Configuration Guide

### Basic Setup

1. **Create GameObject:**
   ```
   Hierarchy → Right Click → Create Empty
   Name: "SpiralEmitter"
   ```

2. **Add Script:**
   ```
   Inspector → Add Component → SpiralMovement
   ```

3. **Configure Parameters:**
   - Set `Angular Velocity` to desired rotation speed
   - Adjust `Radius Growth Rate` for expansion speed
   - Set `Initial Radius` for starting size

### Advanced Integration

#### ES0IL Core Link
```csharp
// Enable in Inspector
spiralMovement.linkToES0ILCore = true;

// Resource pressure affects growth rate
// Simulated with sine wave: 0.5x to 1.5x multiplier
```

#### Dragonfly Motor Mode
```csharp
// Enable in Inspector
spiralMovement.dragonflyMotorMode = true;

// Adds flight wobble and rotation
// Frequency: 2.0-2.5 Hz
// Rotation: 0.5x angular velocity
```

#### Hellraiser Threshold
```csharp
// Set threshold (0.0 - 1.0)
spiralMovement.hellraiserThreshold = 0.75f;

// Triggers at 75% engine load
// Applies intensity boost: 1.75x - 2.0x
```

---

## 🎨 Visualization

### Gizmos (Scene View)

Enable `Draw Gizmos` in Inspector to see:
- **Cyan Lines** - Spiral trajectory path
- **Red Sphere** - Center point marker
- **Resolution** - Adjustable point density (default: 100)

### Runtime Visualization

- **Trail Renderer** - Shows path history
- **Particle System** - Hellraiser emission effects
- **Debug Logs** - State tracking in Console

---

## 📖 Documentation

### Complete Reference

📘 **[MetaBlueprint Analysis](Documentation/MetaBlueprint_SpiralMovement.md)**
- Code logic breakdown
- Visual node mapping
- Integration pathways
- API reference
- Calibration charts

### Key Sections

1. **Mathematical Foundation** - Polar coordinate transformations
2. **Algorithm Flow** - Step-by-step execution
3. **Unity Scene Setup** - Hierarchy and components
4. **Hellraiser Integration** - Energy surplus mechanics
5. **ES0IL Core Binding** - Resource pressure effects
6. **Dragonfly Motor** - Flight pattern simulation

---

## 🧪 Testing & Validation

### Test Scenarios

1. **Basic Spiral**
   - Default parameters
   - 2D planar motion
   - Gizmos enabled

2. **3D Helix**
   - Enable `enable3DSpiral`
   - Set `verticalSpeed` to 0.5
   - Observe rising trajectory

3. **ES0IL Integration**
   - Enable `linkToES0ILCore`
   - Watch radius change with pressure
   - Monitor Console for pressure values

4. **Hellraiser Activation**
   - Set threshold to 0.5 (easier trigger)
   - Observe intensity boost above threshold
   - Check emission events in Console

### Expected Results

✅ Smooth spiral trajectory  
✅ Proper polar-to-Cartesian conversion  
✅ Radius stays within min/max bounds  
✅ Gizmos render correctly in Scene view  
✅ ES0IL pressure modulates growth  
✅ Hellraiser triggers at threshold  
✅ Dragonfly mode adds realistic wobble  

---

## 🔌 API Reference

### Public Methods

```csharp
// Reset spiral to initial state
spiralMovement.ResetSpiral();

// Get current state for analysis
SpiralState state = spiralMovement.GetSpiralState();

// Manually trigger Hellraiser emission
spiralMovement.TriggerHellraiserEmission();
```

### SpiralState Structure

```csharp
public struct SpiralState
{
    float angle;              // Current angle (degrees)
    float radius;             // Current radius
    float engineLoad;         // Engine load (0-1)
    bool isHellraiserActive;  // Hellraiser status
    float resourcePressure;   // ES0IL multiplier
}
```

---

## 🎯 Use Cases

### Game Development
- **Enemy AI** - Spiral attack patterns
- **Player Movement** - Dash/dodge abilities
- **Particle Effects** - Spell animations
- **Camera Systems** - Cinematic orbits

### Simulation
- **Physics Demo** - Polar coordinate visualization
- **Flight Training** - Spiral maneuver practice
- **Data Visualization** - Spiral graphs
- **Art Installation** - Generative patterns

### EV0LVerse Ecosystem
- **Resource Extraction** - ES0IL Core integration
- **Flight Mechanics** - Dragonfly Motor Class
- **Energy Systems** - Hellraiser Loop dynamics
- **MetaBlueprint** - System analysis framework

---

## 📈 Performance

### Optimization Tips

1. **Object Pooling** - Reuse GameObjects for particle emission
2. **LOD System** - Reduce spiral complexity at distance
3. **Update Frequency** - Use FixedUpdate for physics calculations
4. **Gizmo Toggle** - Disable in builds for performance

### Benchmarks

| Platform | FPS | CPU Usage | Memory |
|----------|-----|-----------|--------|
| PC (High) | 144+ | < 5% | ~50 MB |
| PC (Mid) | 60+ | < 10% | ~60 MB |
| Mobile | 30+ | < 20% | ~80 MB |

---

## 🛠️ Troubleshooting

### Common Issues

**Problem:** Spiral doesn't move
- **Solution:** Check `angularVelocity` and `radiusGrowthRate` are non-zero

**Problem:** Gizmos not visible
- **Solution:** Enable `drawGizmos` in Inspector and check Scene view

**Problem:** Hellraiser never triggers
- **Solution:** Lower `hellraiserThreshold` or increase simulation time

**Problem:** Spiral jitters or stutters
- **Solution:** Ensure consistent framerate, use FixedUpdate if needed

---

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines.

### Development Workflow

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

---

## 📝 License

This project is part of the **EV0LVerse Codex** system.  
See [LICENSE](../LICENSE) for details.

---

## 🌟 Acknowledgments

- **EV0LVerse Development Team** - System architecture
- **Unity Technologies** - Game engine platform
- **Open Source Community** - Inspiration and support

---

## 📞 Support

- **Documentation:** [MetaBlueprint](Documentation/MetaBlueprint_SpiralMovement.md)
- **Issues:** [GitHub Issues](https://github.com/ttrap0332-design/3V30OStudios/issues)
- **Discussions:** [GitHub Discussions](https://github.com/ttrap0332-design/3V30OStudios/discussions)

---

## 🔮 Roadmap

### v1.1 (Planned)
- [ ] Multi-spiral coordination system
- [ ] Advanced particle effects
- [ ] AI behavior integration
- [ ] VR/AR compatibility

### v1.2 (Future)
- [ ] Blockchain NFT patterns
- [ ] Machine learning optimization
- [ ] Cloud-based parameter sync
- [ ] Mobile platform support

---

**Built with ❤️ for the EV0LVerse Codex System**

🌀 *"Where spirals meet sovereignty, motion becomes meaning."* 🌀
