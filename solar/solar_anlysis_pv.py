import matplotlib.pyplot as plt
import numpy as np


dni_values = []
time = []

def open_file(file_name: str) -> None:
    with open(file_name, 'r') as file:
        file_contents = file.readlines()
        file_contents.pop(0) # Eliminating the newline character at the begning of the list
        # print(file_contents)
        # Extracting DNI values from the csv file
        for i in range(len(file_contents)):
            string = file_contents[i]
            string = string.strip().split(',')
            dni_values.append(float(string[5]))
            hour = float(string[3])
            minute = float(string[4])
            time.append(hour + minute/60)
        

def average(array) -> float:
    values = 0 # Intializing values
    count = 0
    for i in range(len(array)):
        values += array[i]
        if(array[i] == 0):
            continue
        else:
            count +=1
    return values/count 

def total_energy(array,array2) -> float:
    # Integrating W/m^2 function to obtain energy
    energy = np.trapz(array, x = array2)
    return energy

def plot_data(args = None) -> None:
    # Plotting the Data
    plt.plot(time, dni_values)
    plt.title("Global Horizontal Irradiance vs Time ")
    plt.xlabel("Time: hours")
    plt.ylabel("DNI Values: w/m^2")
    plt.grid(True)
    plt.show()

def main(args = None) -> None:
    open_file("/home/marvin/robotics/solar/pv_SolarData/pv_GHI_SolarData_Day_August.csv")
    average_dni = average(dni_values)
    energy_in_a_day = total_energy(dni_values, time)
    print(f"Average Solar Irradiance: {average_dni: .2f} w/m^2")
    print(f"Total Energy in a day: {energy_in_a_day: .2f} Joules")
    #plot_data()




if __name__ == "__main__":
    main()

