import numpy as np
import pandas as pd
import scale
from plots import plot_total_orbit
from plots import plot_orbit_gc
from plots import plot_gc_pos
from plots import plot_gc_pos_2D
from plots import full_orbit
import outputs



def scale_center(array):
    array[:,0] *= scale.to_pc #  x
    array[:,1] *= scale.to_pc #  y
    array[:,2] *= scale.to_pc #  z

    array[ :, 3] *= scale.v   #  vx
    array[ :, 4] *= scale.v   #  vy
    array[ :, 5] *= scale.v   #  vz

    return array

def scale_time(array):
    array[:,0] *= scale.t  / 1e6 # time - Myr
    array[:,3] *= scale.m        # dwarf galaxy
    array[:,4] *= scale.m        # gas
    array[:,5] *= scale.m        # new stars
    array[:,6] *= scale.m        # GC

    array[:,7] *= scale.m           # total AGB output
    array[:,8] *= scale.m           # AGB output from globular cluster 

    return array


def to_numpy(timeEv, agb, dwarf, gc):
    
    timeEv = np.asarray(timeEv, dtype = np.float32)
    agb = np.asarray(agb, dtype = np.float32)
    dwarf = np.asarray(dwarf, dtype = np.float32)
    gc = np.asarray(gc, dtype = np.float32)

    timeEv = np.hstack((timeEv, agb))
    del agb

    timeEv = scale_time(timeEv)
    dwarf = scale_center(dwarf)
    gc = scale_center(gc)

    time_col_header = ['time', 'ncount', 'dark_matter', 'dwarf', 'gas', 'new_stars', 'GC', 'total_AGB', 'GC_AGB']
    gc_col_header = ['x', 'y', 'z', 'vx', 'vy', 'vz']
    dwarf_col_header = ['x', 'y', 'z', 'vx', 'vy', 'vz']

    timeEv = pd.DataFrame(timeEv, columns = time_col_header)
    dwarf = pd.DataFrame(dwarf, columns = dwarf_col_header)
    gc = pd.DataFrame(gc, columns = gc_col_header)

    timeEv.loc[:,'total_gc'] = timeEv['GC'] + timeEv['new_stars'] + timeEv['GC_AGB']

    return timeEv, dwarf, gc

def get_gc_wrt_dwarf(gc, dwarf):

    centered_dwarf_x = dwarf['x'] - gc['x']
    centered_dwarf_y = dwarf['y'] - gc['y']
    centered_dwarf_z = dwarf['z'] - gc['z']
    
    plot_gc_pos(centered_dwarf_x, centered_dwarf_y, centered_dwarf_z)

def make_dot_arr(x, y, time):
    x_dot = []
    y_dot = []
    time_check = []

    index = 1
    interval = 10
    for i in range(0,len(time)):
        if time[i] < index * interval:
            continue
        else:
            #print(index * interval)
            x_dot.append(x[i])
            y_dot.append(y[i])
            time_check.append(time[i])
            index +=1

    
    time_check = np.asarray(time_check)
    return x_dot, y_dot, time_check


def orbit_array_import():
    timeEv = []
    agb = []
    gc = []
    dwarf = []

    linecount = 0

    with open('orbit.dat', 'r') as orbit:

        for line in orbit:

            row = line.split()

            # row with time step
            if linecount == 0:
                timeEv.append(row)
                linecount+=1
            
            
            # AGB ejecta
            elif linecount == 1:
                agb.append(row)
                linecount+=1
                

            # dwarf center - reset line counter
            elif linecount == 2:
                dwarf.append(row)
                linecount +=1
                
            
            # GC center
            elif linecount == 3:
                gc.append(row)
                linecount =0

            else:
                print("WARNING: incorrect line indexing!")

    timeEv, dwarf, gc = to_numpy(timeEv, agb, dwarf, gc)
    return timeEv, dwarf, gc

def init_plots(gc,  x_dot, y_dot, time):
    
    gas_init = np.load('gas_init.npy')
    new_r = np.load('new_crop_rad.npy')
    
    

    # Load in the indexed arrays
    ns_1_index = np.load('ns_1_index.npy')
    ns_2_index = np.load('ns_2_index.npy')

    # Restrict id=1 stars within 20 pc
    ns_index_20 = []
    for i in range(0, ns_1_index.size):
        if new_r[i] < 20:
            #print('added')
            ns_index_20.append(ns_1_index[i])
    
    ns_index_20 = np.asarray(ns_index_20)

    # Allow any id=2 stars to be in the sample
    

    # Dont worry with the if conditions because if it breaks, 
    # it will break in tout and not get to orbit.

    # Apply indexing to the rows we want
    new_1_gas = gas_init[ns_index_20,:]
    new_2_gas = gas_init[ns_2_index,:]

    col_header = ['x', 'y', 'z', 'vx', 'vy', 'vz', 'iwas', 'id', 'mass']
    gas_init = pd.DataFrame(gas_init, columns=col_header)
    new_1_gas = pd.DataFrame(new_1_gas, columns=col_header)
    new_2_gas = pd.DataFrame(new_2_gas, columns=col_header)

    # The scatter plot with the 3 different componants
    #full_orbit(gc['x'], gc['y'],  x_dot, y_dot, time, gas_init, new_1_gas[:,0], new_1_gas[:,1],new_2_gas[:,0], new_2_gas[:,1])
    full_orbit(gc['x'], gc['y'],  x_dot, y_dot, time, gas_init, new_1_gas, new_2_gas)
    

                
def run_orbit():

    timeEv, dwarf, gc = orbit_array_import()

    x_dot, y_dot, time = make_dot_arr(np.asarray(gc['x']), np.asarray(gc['y']), np.asarray(timeEv['time']))
    plot_gc_pos_2D(gc['x'], gc['y'],  x_dot, y_dot, time,dwarf['x'][0],dwarf['y'][0])
    if outputs.init_timestep == True:
        init_plots(gc, x_dot, y_dot, time)

    get_gc_wrt_dwarf(gc, dwarf)
    plot_gc_pos(gc['x'], gc['y'], gc['z'])
    #plot_total_orbit(timeEv) # Runs the version with all the lines
    plot_orbit_gc(timeEv)
    start_rad = np.sqrt(gc['x'][0]**2+ gc['y'][0]**2+gc['z'][0]**2)
    print('AGB fraction:')
    print(timeEv.GC_AGB.iloc[-1]/timeEv.gas.iloc[-1])

    print('Starting radii: ', start_rad)







