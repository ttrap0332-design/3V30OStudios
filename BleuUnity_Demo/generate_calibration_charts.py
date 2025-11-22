#!/usr/bin/env python3
"""
Spiral Movement Calibration Chart Generator
Generates trajectory plots and calibration charts for SpiralMovement.cs analysis
Part of the EV0LVerse Codex MetaBlueprint system
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import os

# Configuration
OUTPUT_DIR = "Charts"
DPI = 150
FIGSIZE = (10, 8)

# Spiral parameters (matching SpiralMovement.cs defaults)
ANGULAR_VELOCITY = 45  # degrees per second
RADIUS_GROWTH_RATE = 0.5  # units per second
INITIAL_RADIUS = 1.0
MAX_RADIUS = 10.0
MIN_RADIUS = 0.1
SPIRAL_TIGHTNESS = 1.0
SIMULATION_TIME = 30.0  # seconds


def polar_to_cartesian(radius, angle_deg):
    """Convert polar coordinates to Cartesian"""
    angle_rad = np.radians(angle_deg)
    x = radius * np.cos(angle_rad)
    y = radius * np.sin(angle_rad)
    return x, y


def generate_spiral_trajectory(duration=SIMULATION_TIME):
    """Generate spiral trajectory points over time"""
    dt = 0.1  # time step
    time_points = np.arange(0, duration, dt)
    
    angles = []
    radii = []
    x_coords = []
    y_coords = []
    z_coords = []
    
    current_angle = 0
    current_radius = INITIAL_RADIUS
    radius_direction = 1  # 1 for growing, -1 for shrinking
    
    for t in time_points:
        # Update angle
        current_angle += ANGULAR_VELOCITY * dt
        
        # Update radius with growth/decay
        current_radius += RADIUS_GROWTH_RATE * radius_direction * dt
        
        # Reverse direction at boundaries
        if current_radius >= MAX_RADIUS:
            current_radius = MAX_RADIUS
            radius_direction = -1
        elif current_radius <= MIN_RADIUS:
            current_radius = MIN_RADIUS
            radius_direction = 1
        
        # Convert to Cartesian
        x, y = polar_to_cartesian(current_radius, current_angle * SPIRAL_TIGHTNESS)
        
        # Store values
        angles.append(current_angle)
        radii.append(current_radius)
        x_coords.append(x)
        y_coords.append(y)
        z_coords.append(t * 0.5)  # Vertical component for 3D spiral
    
    return {
        'time': time_points,
        'angles': np.array(angles),
        'radii': np.array(radii),
        'x': np.array(x_coords),
        'y': np.array(y_coords),
        'z': np.array(z_coords)
    }


def plot_2d_trajectory(data):
    """Generate 2D spiral trajectory plot (X vs Y)"""
    fig, ax = plt.subplots(figsize=FIGSIZE)
    
    # Plot spiral path with color gradient representing time
    scatter = ax.scatter(data['x'], data['y'], c=data['time'], 
                        cmap='viridis', s=10, alpha=0.6)
    
    # Add center point
    ax.plot(0, 0, 'ro', markersize=10, label='Center', zorder=5)
    
    # Add radius circles for reference
    for r in [INITIAL_RADIUS, MAX_RADIUS / 2, MAX_RADIUS]:
        circle = Circle((0, 0), r, fill=False, color='gray', 
                       linestyle='--', alpha=0.3)
        ax.add_patch(circle)
    
    # Styling
    ax.set_xlabel('X Position (units)', fontsize=12)
    ax.set_ylabel('Y Position (units)', fontsize=12)
    ax.set_title('Spiral Trajectory - 2D Projection (X vs Y)', 
                fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.set_aspect('equal')
    ax.legend(fontsize=10)
    
    # Add colorbar for time
    cbar = plt.colorbar(scatter, ax=ax)
    cbar.set_label('Time (seconds)', fontsize=10)
    
    plt.tight_layout()
    output_path = os.path.join(OUTPUT_DIR, 'trajectory_2d_plot.png')
    plt.savefig(output_path, dpi=DPI, bbox_inches='tight')
    print(f"✅ Saved: {output_path}")
    plt.close()


def plot_radial_distance(data):
    """Generate radial distance over time plot"""
    fig, ax = plt.subplots(figsize=FIGSIZE)
    
    # Plot radius over time
    ax.plot(data['time'], data['radii'], 'b-', linewidth=2, label='Radius')
    
    # Add reference lines
    ax.axhline(y=MAX_RADIUS, color='r', linestyle='--', 
              alpha=0.5, label=f'Max Radius ({MAX_RADIUS})')
    ax.axhline(y=MIN_RADIUS, color='g', linestyle='--', 
              alpha=0.5, label=f'Min Radius ({MIN_RADIUS})')
    ax.axhline(y=INITIAL_RADIUS, color='orange', linestyle=':', 
              alpha=0.5, label=f'Initial Radius ({INITIAL_RADIUS})')
    
    # Styling
    ax.set_xlabel('Time (seconds)', fontsize=12)
    ax.set_ylabel('Radius (units)', fontsize=12)
    ax.set_title('Radial Distance Over Time', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=10)
    
    plt.tight_layout()
    output_path = os.path.join(OUTPUT_DIR, 'radial_distance_plot.png')
    plt.savefig(output_path, dpi=DPI, bbox_inches='tight')
    print(f"✅ Saved: {output_path}")
    plt.close()


def plot_3d_trajectory(data):
    """Generate 3D helix spiral plot"""
    fig = plt.figure(figsize=FIGSIZE)
    ax = fig.add_subplot(111, projection='3d')
    
    # Plot 3D spiral
    scatter = ax.scatter(data['x'], data['y'], data['z'], 
                        c=data['time'], cmap='plasma', s=10, alpha=0.6)
    
    # Add center line
    ax.plot([0, 0], [0, 0], [data['z'].min(), data['z'].max()], 
           'r--', linewidth=2, alpha=0.5, label='Center Axis')
    
    # Styling
    ax.set_xlabel('X Position', fontsize=10)
    ax.set_ylabel('Y Position', fontsize=10)
    ax.set_zlabel('Z Position (Height)', fontsize=10)
    ax.set_title('3D Helix Spiral Trajectory', fontsize=14, fontweight='bold')
    ax.legend(fontsize=9)
    
    # Add colorbar
    cbar = plt.colorbar(scatter, ax=ax, pad=0.1, shrink=0.8)
    cbar.set_label('Time (seconds)', fontsize=9)
    
    plt.tight_layout()
    output_path = os.path.join(OUTPUT_DIR, 'trajectory_3d_plot.png')
    plt.savefig(output_path, dpi=DPI, bbox_inches='tight')
    print(f"✅ Saved: {output_path}")
    plt.close()


def plot_angular_velocity(data):
    """Generate angular velocity profile"""
    fig, ax = plt.subplots(figsize=FIGSIZE)
    
    # Plot angle over time
    ax.plot(data['time'], data['angles'], 'purple', linewidth=2, 
           label='Angle (degrees)')
    
    # Styling
    ax.set_xlabel('Time (seconds)', fontsize=12)
    ax.set_ylabel('Angle (degrees)', fontsize=12)
    ax.set_title('Angular Velocity Profile', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=10)
    
    # Add angular velocity annotation
    avg_angular_vel = (data['angles'][-1] - data['angles'][0]) / data['time'][-1]
    ax.text(0.02, 0.98, f'Avg Angular Velocity: {avg_angular_vel:.1f}°/s',
           transform=ax.transAxes, fontsize=10,
           verticalalignment='top', bbox=dict(boxstyle='round', 
           facecolor='wheat', alpha=0.5))
    
    plt.tight_layout()
    output_path = os.path.join(OUTPUT_DIR, 'angular_velocity_plot.png')
    plt.savefig(output_path, dpi=DPI, bbox_inches='tight')
    print(f"✅ Saved: {output_path}")
    plt.close()


def plot_engine_load(data):
    """Generate engine load and Hellraiser activation plot"""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=FIGSIZE, sharex=True)
    
    # Simulate engine load with ping-pong pattern
    engine_load = 0.5 + 0.5 * np.sin(data['time'] * 0.5)
    hellraiser_threshold = 0.75
    
    # Plot 1: Engine Load
    ax1.plot(data['time'], engine_load, 'b-', linewidth=2, label='Engine Load')
    ax1.axhline(y=hellraiser_threshold, color='r', linestyle='--', 
               linewidth=2, label=f'Hellraiser Threshold ({hellraiser_threshold})')
    
    # Highlight active regions
    active_regions = engine_load >= hellraiser_threshold
    ax1.fill_between(data['time'], 0, 1, where=active_regions, 
                     alpha=0.2, color='red', label='Hellraiser Active')
    
    ax1.set_ylabel('Engine Load', fontsize=12)
    ax1.set_title('Engine Load and Hellraiser Activation', 
                 fontsize=14, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    ax1.legend(fontsize=9, loc='upper right')
    ax1.set_ylim([0, 1.05])
    
    # Plot 2: Intensity Multiplier
    intensity_multiplier = np.where(active_regions, 1 + engine_load, 1.0)
    ax2.plot(data['time'], intensity_multiplier, 'g-', linewidth=2, 
            label='Intensity Multiplier')
    ax2.axhline(y=1.0, color='gray', linestyle=':', alpha=0.5)
    
    ax2.set_xlabel('Time (seconds)', fontsize=12)
    ax2.set_ylabel('Intensity Multiplier', fontsize=12)
    ax2.set_title('Spiral Intensity Boost', fontsize=12, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    ax2.legend(fontsize=9)
    
    plt.tight_layout()
    output_path = os.path.join(OUTPUT_DIR, 'engine_load_plot.png')
    plt.savefig(output_path, dpi=DPI, bbox_inches='tight')
    print(f"✅ Saved: {output_path}")
    plt.close()


def plot_parameter_sensitivity(data):
    """Generate parameter sensitivity analysis"""
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # Test different angular velocities
    ax = axes[0, 0]
    for vel in [30, 45, 60, 90]:
        angles = np.arange(0, 360 * 3, 1)
        radii = INITIAL_RADIUS + (angles / (vel * 10))
        x, y = polar_to_cartesian(radii, angles)
        ax.plot(x, y, label=f'{vel}°/s', alpha=0.7, linewidth=1.5)
    ax.set_title('Angular Velocity Sensitivity', fontweight='bold')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    ax.set_aspect('equal')
    
    # Test different growth rates
    ax = axes[0, 1]
    for rate in [0.2, 0.5, 0.8, 1.2]:
        angles = np.arange(0, 360 * 3, 1)
        radii = INITIAL_RADIUS + (angles / 360) * rate * 10
        x, y = polar_to_cartesian(radii, angles)
        ax.plot(x, y, label=f'{rate} u/s', alpha=0.7, linewidth=1.5)
    ax.set_title('Growth Rate Sensitivity', fontweight='bold')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    ax.set_aspect('equal')
    
    # Test different tightness factors
    ax = axes[1, 0]
    for tight in [0.5, 1.0, 1.5, 2.0]:
        angles = np.arange(0, 360 * 3, 1)
        radii = INITIAL_RADIUS + (angles / 360) * 5
        x, y = polar_to_cartesian(radii, angles * tight)
        ax.plot(x, y, label=f'Tightness {tight}', alpha=0.7, linewidth=1.5)
    ax.set_title('Spiral Tightness Sensitivity', fontweight='bold')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    ax.set_aspect('equal')
    
    # Test direction comparison
    ax = axes[1, 1]
    angles = np.arange(0, 360 * 3, 1)
    radii = INITIAL_RADIUS + (angles / 360) * 5
    x1, y1 = polar_to_cartesian(radii, angles)
    x2, y2 = polar_to_cartesian(radii, -angles)
    ax.plot(x1, y1, label='Counterclockwise', alpha=0.7, linewidth=2)
    ax.plot(x2, y2, label='Clockwise', alpha=0.7, linewidth=2)
    ax.set_title('Rotation Direction', fontweight='bold')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    ax.set_aspect('equal')
    
    plt.suptitle('Parameter Sensitivity Analysis', 
                fontsize=16, fontweight='bold', y=0.995)
    plt.tight_layout()
    
    output_path = os.path.join(OUTPUT_DIR, 'parameter_sensitivity_plot.png')
    plt.savefig(output_path, dpi=DPI, bbox_inches='tight')
    print(f"✅ Saved: {output_path}")
    plt.close()


def main():
    """Main execution function"""
    print("🌀 Spiral Movement Calibration Chart Generator")
    print("=" * 60)
    
    # Create output directory
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print(f"📁 Output directory: {OUTPUT_DIR}/")
    print()
    
    # Generate spiral trajectory data
    print("🔄 Generating spiral trajectory data...")
    data = generate_spiral_trajectory()
    print(f"✅ Generated {len(data['time'])} data points")
    print()
    
    # Generate all plots
    print("📊 Generating calibration charts...")
    plot_2d_trajectory(data)
    plot_radial_distance(data)
    plot_3d_trajectory(data)
    plot_angular_velocity(data)
    plot_engine_load(data)
    plot_parameter_sensitivity(data)
    
    print()
    print("=" * 60)
    print("✅ All calibration charts generated successfully!")
    print(f"📂 Charts saved in: {OUTPUT_DIR}/")
    print()
    print("Generated files:")
    for filename in os.listdir(OUTPUT_DIR):
        if filename.endswith('.png'):
            print(f"  - {filename}")


if __name__ == "__main__":
    main()
