import numpy as np 
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d # Importing the scipy interpolation for 1D function 


time = np.array([0, 30, 60, 90, 120, 150, 180, 210,240, 270, 300, 330, 360, 390, 420, 450, 480, 510, 540, 570, 600])

voltages = np.array([12.38, 12.34, 12.30, 12.23, 12.17, 12.08, 12.00, 11.91, 11.81, 11.70, 11.58, 11.45, 11.27, 11.12, 11.02, 10.94, 10.87, 10.80, 10.73, 10.63 , 10.51])

xp = []

interpolated_voltage = interp1d(voltages, time, 'linear')


# Approximate Amps
approximate_amps = 6



def voltage_to_power(data):
    power = []
    for voltage_value in data:
        values = voltage_value * approximate_amps # P = V X I
        power.append(values) # Appending the values to the power array 
    return power

power = voltage_to_power(voltages) 

def average_power(power):
    sum = 0
    average_wattage = 0
    for power_values in power:
        sum += power_values
        average_wattage = sum/len(power)
    return average_wattage




total_energy = np.trapz(time, power) # Integrating power vs time to get total Energy 

average_watts = average_power(power)

print(average_watts)
plt.figure(figsize=(10,10))
plt.plot(time, total_energy, marker = 'o')
plt.xlabel("Time: Seconds")
plt.ylabel("Energy: J")
plt.title("Energy vs Time: Robot Discharge")
plt.legend(f"{total_energy}")
plt.show()