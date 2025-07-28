import numpy as np 
import matplotlib.pyplot as plt

# GHI Unit is W/m^2
# Arrangement of the Data
# Year, Month, Day, Hour, Minute, GHI


# Open and read file (usuing with open takes care of closing the file, best practices)
with open('solar_ghi_data.csv', 'r') as file:
    read = file.readlines()

ghi_values = [] # Storing my GHI values, unit w/m^2
hours = [] # Storing hours 

# Extract GHI and Hour
for line in read:
    parts = line.strip().split(',')  # Split line by commas
    if len(parts) >= 6:
        hours.append(parts[3])                 # Hour
        ghi_values.append(float(parts[5]))     # GHI (converted to float)

# Plot
plt.figure(figsize=(10, 5))
plt.plot(hours, ghi_values, marker='o')
plt.xlabel("Hour of Day")
plt.ylabel("GHI (W/m²)")
plt.title("Global Horizontal Irradiance vs Hour")
plt.grid(True)
plt.show()




