import scale
import sys
import numpy as np
import plots
import outputs


# put values into physical quantities
def scale_arrays(array):

    if array.size == 0:
        return array # Make sure things can be multiplied

    array[:,0] = np.multiply(array[:,0], scale.to_pc)  # all x
    array[:,1] = np.multiply(array[:,1], scale.to_pc)  # all y
    array[:,2] = np.multiply(array[:,2], scale.to_pc)  # all z

    array[:,3] = np.multiply(array[:,3], scale.v)  # all vx
    array[:,4] = np.multiply(array[:,4], scale.v)  # all vy
    array[:,5] = np.multiply(array[:,5], scale.v)  # all vz

    array[:,6] = array[:,6].astype(int) # cast to integer

    array[:,8] = np.multiply(array[:,8], scale.m)  # all mass
    return array


# If we didn't get as many timesteps as we thought - cancel everything
def check_timestep(recovered_timestep, data):
    if outputs.timestep != recovered_timestep:
        print('WARNING: incorrect number of time stamps')

        np.save('gas', data[-1][1])
        np.save('new', data[-1][2])
        np.save('old', data[-1][3])

        sys.exit()

# Initialise arrays by setting them to []
def init_arr():
    return [], [], [], []

# Converting arrays to numpy
def convert_2_np(gal, gas, new, old):
    return np.asarray(gal), np.asarray(gas), np.asarray(new), np.asarray(old)

# Generate the time step to append to the 'mega array'
def gen_ts(gal, gas, new, old):
    ts = []

    gal, gas, new, old = convert_2_np(gal, gas, new, old)

    # Apply scaling
    gal = scale_arrays(gal)
    gas = scale_arrays(gas) 
    new = scale_arrays(new)
    old = scale_arrays(old) 
    
    # Append arrays
    ts.append(gal)
    ts.append(gas)
    ts.append(new)
    ts.append(old)

    return ts

# read in the file into a 3D array
def tout_array_import():

    #an array for each time step
    timeStepArray = []

    gal, gas, new, old = init_arr()
    
    data = []

    first_loop = True
    counter_start = False

    # The number of columns we want to import
    col_num = 9

    
    ns_1_index = []
    ns_2_index = []
    counter = 0

    with open('tout.dat', 'r') as tout:

        for line in tout:

            row = np.fromstring(line, sep=' ')

            if row.size == 2: # New time step

                if first_loop == True: # If it's the first loop
                    first_loop = False
                    timeStepArray.append(row[1]* scale.t)
                    continue

                # Store values
                timeStepArray.append(row[1] * scale.t)

                print('appending timestep')
                counter_start = True
                ns_1_index = []
                ns_2_index = []
                counter = 0
                data.append(gen_ts(gal, gas, new, old))
                
                # Clear arrays
                gal, gas, new, old = init_arr()

            if row.size <= 5:
                continue # Skip the lines with 5 rows

            row = row[0:col_num] # Take first 9 vars

            #counter = 0 # Just in case NS is the first thing in the list 
            # Unliekly - but will show up as 2 0's at the start
            
            
            if row[6] == 1: # Dwarf
                gal.append(row)
            elif row[6] == 2: # Gas
                gas.append(row)
                if counter_start == True:
                    counter+=1
            elif row[6] == 3: # New stars
                new.append(row)
                if row[7] == 1 and counter_start == True:
                    ns_1_index.append(counter)
                    counter+=1
                elif row[7] == 2 and counter_start == True:
                    ns_2_index.append(counter)
                    counter+=1
            elif row[6] ==4: # Old stars
                
                if counter_start == True: # not sure whether this should be here??
                    counter_start = False # Will restart counter when it goes back to gas and not restart array indexing
                    # Stop from incrementing 
                
                old.append(row)
            elif row[6] ==0: # DM
                continue # dont care about DM
            else:
                print("WARNING: unknown iwas argument")
                sys.exit()
            #print(counter)
            #if counter_start == True:
            #    counter+=1
            
    print('appending final timestep')
    
    data.append(gen_ts(gal, gas, new, old)) # now a 4D array

    # Clear arrays
    gal, gas, new, old = init_arr()
    
    
    ns_1_index = np.asarray(ns_1_index)
    ns_2_index = np.asarray(ns_2_index)
   
    np.save('ns_1_index', ns_1_index)
    np.save('ns_2_index', ns_2_index)

    return data, timeStepArray

def run_tout():

    data, timeStepArray = tout_array_import() # Import data
    
    outputs.timestep = len(timeStepArray) # Assign value

    #check_timestep(recovered_timestep, data) # Error checking

    if outputs.spacial_plots == True: # Make the spatial plot
        plots.plot_tout_4(data, timeStepArray)
    
    if outputs.export_last_timestep == True:
        np.save('gal', data[-1][0])
        np.save('gas', data[-1][1])
        np.save('gas_init', data[0][1])
        np.save('gal_init', data[0][0])
        np.save('new', data[-1][2])
        np.save('old', data[-1][3])

    if outputs.export_all_timestep == True:
        for i in range(outputs.timestep):
            np.save('gal'+str(i), data[i][0])
            np.save('gas'+str(i), data[i][1])
            np.save('new'+str(i), data[i][2])
            np.save('old'+str(i), data[i][3])
    
    print('finished tout import')
    print(timeStepArray)
    # Return the final time step
    return data[outputs.timestep-1]
