import matplotlib.pyplot as plt 
import numpy as np 
from scipy.interpolate import interp1d # Importing interpolation function 
from numpy import trapz # Importing trapezodial integration 

with open("nasa_solar_irridiance_data_08_08_2024_realistic_conditions.csv") as file:
    read = file.readlines() # Read each line of the file

# Data Arrangment 
# YEAR,MO,DY,HR,ALLSKY_SFC_SW_DWN
time = [] # In hours 

gih_values = [] # Solar Irradiance Data: Units w/m^2 

for line in read: # Grabbing the index and item associated with the read object 
    clean_data = line.strip().split(',') # Seperate the items in an array by the commas and remove the \n 
    if len(clean_data) >= 5: # Check the length of the array passed in 
        time.append(float(clean_data[3])) # Appending the time 
        gih_values.append(float(clean_data[4])) # Appending the gih values to the array 

def calculate_avg(data): # The average value is nice to have but does not amount to having the area under the curve from an integral
    # Iterating over the array values and taking the average
    if not data: 
        return 0 # Prevent's division by zero 
    total = 0 # Initializing total 
    average = 0 #Initializing average 
    for value in data:
        total += value # Summing the values 
        average = total /len(data)
    return average


# Solar Panel Simulation 

MAX_POWER = 9.34 # Each solar panel has a maximum power rating of 9.34 watts 

NUMBER_OF_PANNELS = 6 # Maximum Number of Panels I can fit on my 4ft^2 surface area, pannels are assumed to be laying just flat. 

MAX_POWER_PANNELS = MAX_POWER * NUMBER_OF_PANNELS # The total maximum wattage of the 6 pannels 

SURFACE_AREA_PANNELS = 0.3666 # Units meter squared 

EFFICENCY = 0.195 # twenty percent efficency 

# # Integrating the total Energy over a 0-24 hour interval
# ENERGY = trapz(gih_values, time) * 3600 # getting J/m^2 (Scalar)

time_hours = np.array(time)
irradiance = np.array(gih_values)

p_in = SURFACE_AREA_PANNELS * irradiance * EFFICENCY # Energy: Units J Power

# Integrate p_in over a period of 24 hours to gather the total energy harvested over this cycle 
harvested_solar_energy = trapz(p_in, time_hours) # Returns the total amount of harvested solar energy in watt-hours


print(f"Amount gained from 24-hour solar harvest:{harvested_solar_energy: .4f} Wh")


# Battery Simulation 

E_MAX = 57.72 # Maximum Watt-hours so it's full charge E(0)


P_OUT = 76.17  # Unit  W

E = np.zeros_like(time_hours) # Intializing an array filled with zeros that is the same shape and size as time_hours

E[0] = E_MAX # Initial Condition (fully charged Battery, before it stars discharging due to moving or hotel load)

def calculate_state_of_charge():

    # Calculating the dt's from each point  
    dt = np.diff(time_hours, prepend=time_hours[0]) # Unit: Hours
    for i in range(1, len(time_hours)): # Loop starting from one so we can find the difference between a previous and next time step
        delta_Energy = (p_in[i-1] - P_OUT) * dt[i] # Calulating the difference in energy at every time step
        E[i] = E[i-1] + delta_Energy # Delta Energy could be negative or positive 

        # Bounding the Energy Function 
        if E[i] > E_MAX:
            E[i] = E_MAX
        elif E[i] < 0:
            E[i] = 0
    SoC = (E/E_MAX) * 100
    return SoC



def battery_status() -> None:
    batter_empty_indices = np.where(E == 0)[0] 
    if batter_empty_indices.size > 0:
        time_to_empty = time_hours[batter_empty_indices[0]]
        print(f"Battery depleted after: {time_to_empty: .4f} hours")
    else:
        print("Battery never fully depleted")

SoC = calculate_state_of_charge()

battery_status()

# Plotting the battery 
plt.figure(figsize=(10,10))
plt.plot(time_hours, SoC, marker = 'x')
plt.xlabel("Time (hours)")
plt.ylabel("Battery State of Charge (%)")
plt.title("Battery SoC over Time")
plt.grid(True)
plt.show()

# PLotting the power into the syytem
# plt.plot(time_hours, p_in, label='Input Power (W)')
# plt.xlabel("Time (hours)")
# plt.ylabel("Power (W)")
# plt.title("Instantaneous Power Input from Solar Panel")
# plt.grid(True)
# plt.legend()
# plt.show()


