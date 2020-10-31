import numpy as np


import scale
import sys
import outputs


# put values into physical quantities
def scale_arrays(array):

    if array.size == 0:
        return array # Make sure things can be multiplied

    array[:,0] = np.multiply(array[:,0], scale.r * scale.to_pc)  # all x
    array[:,1] = np.multiply(array[:,1], scale.r * scale.to_pc)  # all y
    array[:,2] = np.multiply(array[:,2], scale.r * scale.to_pc)  # all z

    array[:,3] = np.multiply(array[:,3], scale.v)  # all vx
    array[:,4] = np.multiply(array[:,4], scale.v)  # all vy
    array[:,5] = np.multiply(array[:,5], scale.v)  # all vz

    array[:,6] = array[:,6].astype(int) # cast to integer

    array[:,8] = np.multiply(array[:,8], scale.m)  # all mass

    array[:,12] = np.multiply(array[:,12], scale.t)  # formation epoch

    # Metals
    array[:,14] = np.multiply(array[:,14], scale.m) # H
    array[:,15] = np.multiply(array[:,15], scale.m) # He
    array[:,16] = np.multiply(array[:,16], scale.m) # C
    array[:,17] = np.multiply(array[:,17], scale.m) # N
    array[:,18] = np.multiply(array[:,18], scale.m) # O
    array[:,19] = np.multiply(array[:,19], scale.m) # Fe(56)
    array[:,20] = np.multiply(array[:,20], scale.m) # Mg(24)
    array[:,21] = np.multiply(array[:,21], scale.m) # Ca
    array[:,22] = np.multiply(array[:,22], scale.m) # Si
    array[:,23] = np.multiply(array[:,23], scale.m) # S
    array[:,24] = np.multiply(array[:,24], scale.m) # Ba

    # Dust
    array[:,25] = np.multiply(array[:,25], scale.m) # H
    array[:,26] = np.multiply(array[:,26], scale.m) # He
    array[:,27] = np.multiply(array[:,27], scale.m) # C
    array[:,28] = np.multiply(array[:,28], scale.m) # N
    array[:,29] = np.multiply(array[:,29], scale.m) # O
    array[:,30] = np.multiply(array[:,30], scale.m) # Fe(56)
    array[:,31] = np.multiply(array[:,31], scale.m) # Mg(24)
    array[:,32] = np.multiply(array[:,32], scale.m) # Ca
    array[:,33] = np.multiply(array[:,33], scale.m) # Si
    array[:,34] = np.multiply(array[:,34], scale.m) # S
    array[:,35] = np.multiply(array[:,35], scale.m) # Ba


    return array


# Initialise arrays by setting them to []
def init_arr():
    return [], [], []

# Converting arrays to numpy
def convert_2_np(gal, gas, new):
    return np.asarray(gal), np.asarray(gas), np.asarray(new)

# Generate the time step to append to the 'mega array'
def gen_ts(gal, gas, new):
    ts = []

    gal, gas, new = convert_2_np(gal, gas, new)

    # Apply scaling
    gal = scale_arrays(gal)
    gas = scale_arrays(gas) 
    new = scale_arrays(new)
    
    # Append arrays
    ts.append(gal)
    ts.append(gas)
    ts.append(new)

    return ts

# read in the file into a 3D array
def tout_array_import():

    #an array for each time step
    timeStepArray = []

    gal, gas, new = init_arr()
    
    data = []

    first_loop = True

    # The number of columns we want to import - all the rows!!!!
    # col_num = 12
    prev_row = -1
    particle_id = -1


    with open('tout.dat', 'r') as tout:

        for line in tout:

            row = np.fromstring(line, sep=' ')

            if row.size == 3: # New time step

                if first_loop == True: # If it's the first loop
                    first_loop = False
                    timeStepArray.append(row[2]* scale.t)
                    continue

                # Store values
                timeStepArray.append(row[2] * scale.t)

                print('appending timestep')
                data.append(gen_ts(gal, gas, new))
                
                # Clear arrays
                gal, gas, new = init_arr()

                # reset previous row
                prev_row = -1

                particle_id = -1

            
            # annoying new line for last 2 metals
            elif row.size == 2:

                if prev_row == 1:
                    gal[-1] = np.append(gal[-1], np.append(row, particle_id))
                    
                elif prev_row == 2:
                    gas[-1] = np.append(gas[-1], np.append(row, particle_id))
                elif prev_row == 3:
                    new[-1] = np.append(new[-1], np.append(row, particle_id))

            elif row.size <= 5:
                continue # Skip the lines with 5 rows
            
            
            elif row[6] == 1: # Disc stars
                gal.append(row)
                prev_row = 1

                particle_id += 1 # add 1 to the particle id
            elif row[6] == 2: # Gas
                gas.append(row)
                prev_row = 2
                particle_id += 1
            elif row[6] == 3: # New stars
                new.append(row)
                prev_row = 3
                particle_id += 1
            elif row[6] ==4: # Old stars
                print('found old')
            elif row[6] ==0: # DM
                particle_id += 1
                continue # dont care about DM
            else:
                print("WARNING: unknown iwas argument")
                sys.exit()


            
    print('appending final timestep')
    
    data.append(gen_ts(gal, gas, new)) # now a 4D array

    # Clear arrays
    gal, gas, new = init_arr()

    return data, timeStepArray

def run_tout():

    data, timeStepArray = tout_array_import() # Import data
    
    timestep_no = len(timeStepArray) # Assign value
    np.save('timestep', timeStepArray)
    

    if outputs.export_last_timestep == True:
        np.save('gal', data[-1][0])
        np.save('gas', data[-1][1])
        np.save('gas_init', data[0][1])
        np.save('gal_init', data[0][0])
        np.save('new', data[-1][2])

    if outputs.export_all_timestep == True:
        for i in range(timestep_no):
            np.save('gal'+str(i), data[i][0])
            np.save('gas'+str(i), data[i][1])
            np.save('new'+str(i), data[i][2])
    
    print('finished tout import')
    
    # Return the final time step
    return data[timestep_no-1]
