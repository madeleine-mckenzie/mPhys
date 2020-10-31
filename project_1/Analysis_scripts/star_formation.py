import scale
import numpy as np
from plots import star_formation_plots
from plots import star_formation_rate_plots

def sfr(ism, gas, time):
    # New arrays 
    ism_rate = []
    gas_rate = []

    ism_rate.append(ism[0])
    gas_rate.append(gas[0])
    for i in range(1, time.shape[0]):
        
        # As specified in Kenji's notes
        ism_rate.append((ism[i]-ism[i-1])/(time[i]-time[i-1]))
        gas_rate.append((gas[i]-gas[i-1])/(time[i]-time[i-1]))

    # Comvert these to numpy
    ism_rate = np.asarray(ism_rate, dtype = np.float32)
    gas_rate = np.asarray(gas_rate, dtype = np.float32)


    return ism_rate, gas_rate

def check_arr_len(time, ism):
    while time.shape[0] > ism.shape[0]:
        time = np.delete(time, -1)
    return time
    


def sf_array_import():

    row_skip = False
    time = []
    ism = []
    gas = []

    #Read in the file line by line
    with open('sf.dat', 'r') as file:

        for line in file:

            row = line.split()

            # If less than 5 words - hit a new time stamp
            if len(row) == 1:
                time.append(row[0])
                row_skip = True
                continue
                
            #importing relelvent quantities
            if len(row) == 3 and row_skip == False:
                ism.append(row[0])
                gas.append(row[1])
                #ignore row[2]
                continue
            
            # This row is not important to our analysis
            if row_skip == True:
                row_skip = False
                continue
            
    # Convert to numpy arrays
    time = np.asarray(time, dtype = np.float32)
    ism = np.asarray(ism, dtype = np.float32)
    gas = np.asarray(gas, dtype = np.float32)

    # Scale arrays by relevent quanitities
    time *= scale.t
    ism *= scale.m
    gas *= scale.m  

    return ism, gas, time

def run_sf():
    ism, gas, time = sf_array_import()
    time = check_arr_len(time, ism)

    ism_rate, gas_rate = sfr(ism, gas, time)

    star_formation_plots(ism, gas, time)

    star_formation_rate_plots(ism_rate, gas_rate, time)



    



