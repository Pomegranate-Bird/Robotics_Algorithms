import numpy as np 
import matplotlib.pyplot as plt
from scipy.integrate import cumtrapz

# Given data
time = np.array([0, 30, 60, 90, 120, 150, 180, 210,240, 270, 300, 330, 360, 390, 420, 450, 480, 510, 540, 570, 600])
voltages = np.array([12.38, 12.34, 12.30, 12.23, 12.17, 12.08, 12.00, 11.91, 11.81, 11.70, 11.58, 11.45, 11.27, 11.12, 11.02, 10.94, 10.87, 10.80, 10.73, 10.63 , 10.51])
approximate_amps = 6  # Constant current

# Calculate power (P = V * I)
power = voltages * approximate_amps

# Calculate cumulative energy using trapezoidal integration
cumulative_energy = np.zeros_like(time)  # Initialize with zeros
cumulative_energy[1:] = cumtrapz(power, time)  # Fill cumulative energy from index 1 onwards

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(time, cumulative_energy, marker='o', linestyle='-', color='b')
plt.xlabel("Time (Seconds)", fontsize=12)
plt.ylabel("Energy (Joules)", fontsize=12)
plt.title("Cumulative Energy vs. Time: Robot Discharge", fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)

# Annotate the final energy value
final_energy = cumulative_energy[-1]
plt.annotate(f'Total Energy: {final_energy:.2f} J', 
             xy=(time[-1], final_energy),
             xytext=(time[-1]-150, final_energy-1000),
             arrowprops=dict(arrowstyle='->'))

plt.tight_layout()
plt.show()