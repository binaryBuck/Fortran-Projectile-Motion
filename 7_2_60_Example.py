# This file takes the input 7 Seconds(Time), 2 Meters/Second(U), and 60 Degrees (Angle) input parameters and graphs the trajectory. 
# It is strictly to generate a visual for the example listed in README.txt

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Constants
g = 9.8
PI = 3.1415926

# Initial input values from your Fortran program's input
initial_U = 2.0
initial_angle_deg = 60.0
input_time = 7.0 # This is the specific time from your Fortran input

# Data points from your Fortran program's output at input_time=7s
fortran_output_data = {
    'Simulation': [1, 2, 3, 4, 5],
    'Launch_Velocity_U': [2.0, 4.0, 8.0, 16.0, 32.0],
    'Horizontal_Displacement_at_Input_Time': [7.00000095, 14.0000019, 28.0000038, 56.0000076, 112.000015],
    'Vertical_Displacement_at_Input_Time': [-227.975647, -215.851288, -191.602585, -143.105164, -46.1103210]
}
df_fortran_output = pd.DataFrame(fortran_output_data)

# Convert angle to radians once for calculations
angle_rad = initial_angle_deg * PI / 180.0

# Store data for plotting full trajectories
all_sim_trajectory_data = []

current_U_for_sim = initial_U
for i in range(1, 6): # Loop for 5 simulations
    # Calculate total flight time assuming launch and landing heights are equal
    total_flight_time = (2.0 * current_U_for_sim * np.sin(angle_rad)) / g

    # Generate time points for the trajectory from 0 up to a point slightly beyond total_flight_time
    # or up to the input_time if it's relevant to show the calculated point.
    # We'll take the maximum of total_flight_time and input_time to ensure we cover the Fortran point.
    max_time_for_plot = max(total_flight_time, input_time) * 1.05 # Add 5% buffer
    num_points = 200 # More points for a smoother curve

    time_points = np.linspace(0, max_time_for_plot, num_points)

    # Compute position at each time point for the full trajectory
    X_coords = current_U_for_sim * np.cos(angle_rad) * time_points
    Y_coords = current_U_for_sim * np.sin(angle_rad) * time_points - 0.5 * g * time_points**2

    # Store trajectory data for this simulation
    df_sim_trajectory = pd.DataFrame({
        'Time': time_points,
        'X': X_coords,
        'Y': Y_coords,
        'Simulation': i,
        'Launch_Velocity_U': current_U_for_sim
    })
    all_sim_trajectory_data.append(df_sim_trajectory)

    # Double velocity for next iteration
    current_U_for_sim *= 2.0

# Concatenate all simulation trajectory data into a single DataFrame
full_trajectory_df = pd.concat(all_sim_trajectory_data)

# Create the plot
plt.figure(figsize=(12, 8))

# Plot full trajectories
for sim_num in full_trajectory_df['Simulation'].unique():
    sim_data = full_trajectory_df[full_trajectory_df['Simulation'] == sim_num]
    launch_velocity = sim_data['Launch_Velocity_U'].iloc[0] # Get U for this simulation
    plt.plot(sim_data['X'], sim_data['Y'], linestyle='-', label=f'Trajectory Sim {sim_num} (U={launch_velocity:.1f} m/s)')

# Overlay the specific points from the Fortran output
for index, row in df_fortran_output.iterrows():
    plt.plot(row['Horizontal_Displacement_at_Input_Time'], row['Vertical_Displacement_at_Input_Time'],
             marker='o', markersize=8, color='red',
             label=f'Fortran Output Sim {row["Simulation"]} (t={input_time}s)')

plt.title('Projectile Trajectories and Fortran Output Points (Including Negative Y)')
plt.xlabel('Horizontal Displacement (m)')
plt.ylabel('Vertical Displacement (m)')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5, linestyle='--') # Add a line for Y=0 (ground)
plt.axvline(0, color='black', linewidth=0.5, linestyle='--') # Add a line for X=0 (launch point)
plt.legend(title='Details', bbox_to_anchor=(1.05, 1), loc='upper left') # Place legend outside
plt.tight_layout()
plt.savefig('full_trajectory_with_fortran_points.png')