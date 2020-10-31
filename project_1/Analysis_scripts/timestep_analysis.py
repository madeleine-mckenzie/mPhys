import numpy as np
import pandas as pd
from array_manager import to_pandas_ts4
from plots import los_curve
from plots import binned_rotation
from plots import position_3d
from plots import plot_mass_ratio_new_2
from plots import plot_mass_ratio_new
from plots import plot_mass_ratio
from plots import final_ts_plot_all
from plots import final_ts_plot_scale
from plots import basic_rot_plot
from plots import rot_theta_plot
from plots import rot_theta__overlay_plot
from plots import xyz_vel_plot
from plots import cumulative_hist
from plots import init_state
from plots import init_basic
from plots import basic_ns_scatter
from plots import original_loc
from plots import init_metal_grad
from plots import interp_1G_2G
from plots import final_GC
from plots import init_metal_grad_kde
from make_summary import get_values
from make_summary import get_para
import outputs
import os

def get_iwas(array):
    iwas_arr = [array['x'][0], array['y'][0], array['z'][0]]
    return iwas_arr

def std_bounds(array, std_val):
    # std_val 1 means keep everything within 1 standard deviation
    x_mean = array['x'].mean()
    x_std = array['x'].std()
    x_upper = x_mean + std_val*x_std
    x_lower = x_mean - std_val*x_std

    y_mean = array['y'].mean()
    y_std = array['y'].std()
    y_upper = y_mean + std_val*y_std
    y_lower = y_mean - std_val*y_std

    z_mean = array['z'].mean()
    z_std = array['z'].std()
    z_upper = z_mean + std_val*z_std
    z_lower = z_mean - std_val*z_std

    bounds = [x_upper, x_lower, y_upper, y_lower, z_upper, z_lower]

    return bounds

def array_crop(array, bounds):
    return array.loc[(array['x'] < bounds[0])&(array['x'] > bounds[1])
                &(array['y'] < bounds[2])&(array['y'] > bounds[3])
                &(array['z'] < bounds[4])&(array['z'] > bounds[5])]

def get_mean_pos(array):
    means = [array['x'].mean(), array['y'].mean(), array['z'].mean()]
    return means

def scale_arrays_pos(array, scaler):
    # Doing it this way stops the terminal warnings
    array = array.assign(x_scale = array['x'] - scaler[0])
    array = array.assign(y_scale = array['y'] - scaler[1])
    array = array.assign(z_scale = array['z'] - scaler[2])
    array = array.assign(r = (array['x_scale']**2 + array['y_scale']**2 + array['z_scale']**2)**0.5)
    return array

def get_mean_vel(array):
    means = [array['vx'].mean(), array['vy'].mean(), array['vz'].mean()]
    return means

def scale_arrays_vel(array, scaler):
    '''
    array.loc[:, 'vx_scale'] = array['vx'] - scaler[0]
    array.loc[:, 'vy_scale'] = array['vy'] - scaler[1]
    array.loc[:, 'vz_scale'] = array['vz'] - scaler[2]
    array.loc[:, 'v'] = (array['vx_scale']**2 + array['vy_scale']**2 + array['vz_scale']**2)**0.5
    '''
    array = array.assign(vx_scale = array['vx'] - scaler[0])
    array = array.assign(vy_scale = array['vy'] - scaler[1])
    array = array.assign(vz_scale = array['vz'] - scaler[2])
    array = array.assign(v = (array['vx_scale']**2 + array['vy_scale']**2 + array['vz_scale']**2)**0.5)
    return array

def binning_loop(array, binsize, pc_range, start):

    x_vy = []    # empty list to append average vy values to
    x_vz = []
    y_vx = []

    while start < pc_range:
        upper = start + binsize
        x_band = array.loc[ (array['x_scale'] > start) & (array['x_scale'] < upper) ]
        y_band = array.loc[ (array['y_scale'] > start) & (array['y_scale'] < upper) ]
        #print(x_band)
        x_vy.append(x_band['vy'].mean())
        x_vz.append(x_band['vz'].mean())
        y_vx.append(y_band['vx'].mean())
        start = upper

    rot_arr = [x_vy, x_vz, y_vx]

    return rot_arr

def binning_los(old_array, new_array):

    binsize = 4   # how many data points to output
    pc_range = 40 # total range - i.e. -20 pc : 20 pc
    start = -40   # starting point: i.e. -20pc

    old_rot_arr = binning_loop(old_array, binsize, pc_range, start)
    new_rot_arr = binning_loop(new_array, binsize, pc_range, start)

    x_pos = []    # empty list to append x values to

    # Create the x arr
    while start < pc_range:
        upper = start + binsize
        x_pos.append((start + upper)/2)
        start = upper
    
    binned_rotation(x_pos, old_rot_arr, new_rot_arr)

    del old_rot_arr, new_rot_arr

def scale_all(gal, gas, new, old, pos_scale, vel_scale):
    gal = scale_arrays_pos(gal, pos_scale)
    gas = scale_arrays_pos(gas, pos_scale)
    new = scale_arrays_pos(new, pos_scale)
    old = scale_arrays_pos(old, pos_scale)

    gal = scale_arrays_vel(gal, vel_scale)
    gas = scale_arrays_vel(gas, vel_scale)
    new = scale_arrays_vel(new, vel_scale)
    old = scale_arrays_vel(old, vel_scale)

    return gal, gas, new, old
 
def mass_ratio(old, new):

    binsize = 1   # how many data points to output
    pc_range = 30 # total range - i.e. -20 pc : 20 pc

    start = 0   # starting point: i.e. -20pc
    pop_ratio = []    # empty list to append average vy values to
    x_pos = []    # empty list to append x values to
    old_mass_arr = []
    new_mass_arr = []

    f_enr_std = []

    while start < pc_range:

        upper = start + binsize
        old_temp = old.loc[(old['r']> start)&(old['r'] < upper)]['mass']
        new_temp = new.loc[(new['r']> start)&(new['r'] < upper)]['mass']
        old_mass = old_temp.sum()
        new_mass = new_temp.sum()
        #old_var = old_temp.var()
        #new_var = new_temp.var()

        #var = old_var*new_var + old_mass

        #f_enr_std.append((old_std**2 + new_std**2)**0.5)

        pop_ratio.append(new_mass/(new_mass+old_mass))
        x_pos.append((start + upper)/2)
        old_mass_arr.append(old_mass)
        new_mass_arr.append(new_mass)
        start = upper
    #plot_mass_ratio_new(old.loc[old['r']< pc_range], new.loc[new['r']< pc_range], x_pos, pop_ratio)
    #plot_mass_ratio_new(old, new, x_pos, pop_ratio)
    x_pos = np.asarray(x_pos)
    pop_ratio = np.asarray(pop_ratio)
    #f_enr_std = np.asarray(f_enr_std)
    plot_mass_ratio(x_pos, pop_ratio)  

def get_theta(arr):
    angles = np.arctan2(arr['y_scale'],arr['x_scale'])
    angles = (2*np.pi + angles) * (angles < 0) + angles*(angles > 0)
    arr = arr.assign(theta = angles)

    #arr[arr['theta'] < 0] += 2*np.pi
    '''
    for i, row in arr.iterrows():

        ifor_val = something

        if <condition>:

            ifor_val = something_else

      df.at[i,'ifor'] = ifor_val
    '''

    return arr

def get_angles_arr():
    # because its gross and ugly and I want to hide my hard coding shame
    return [0, 0.39269908169872414, 0.7853981633974483, 1.1780972450961724, 1.5707963267948966, 1.9634954084936207, 2.356194490192345, 2.748893571891069, 3.141592653589793, 3.5342917352885173, 3.9269908169872414, 4.319689898685965, 4.71238898038469, 5.105088062083414, 5.497787143782138, 5.890486225480862, 6.283185307179586]

def polar_split(arr_ns, arr_gc):
    arr_ns = get_theta(arr_ns)
    arr_gc = get_theta(arr_gc)
   


    # Hard code in array bounds - not going to change at any point (always 16 slices)
    angles_arr = get_angles_arr()

    gc_vy = []    # empty list to append average vy values to
    gc_vz = []
    gc_vx = []

    gc_vy_std = []    # empty list to append average vy values to
    gc_vz_std = []
    gc_vx_std = []

    ns_vy = []
    ns_vz = []
    ns_vx = []

    ns_vy_std = []
    ns_vz_std = []
    ns_vx_std = []
    
    for i in range(1, 17): # For indexing the angles array
        temp_ns = arr_ns.loc[ (arr_ns['theta'] < angles_arr[i]) & (arr_ns['theta'] > angles_arr[i-1]) ]
        temp_gc = arr_gc.loc[ (arr_gc['theta'] < angles_arr[i]) & (arr_gc['theta'] > angles_arr[i-1]) ]

        gc_vy.append(temp_gc['vy_scale'].mean())
        gc_vz.append(temp_gc['vz_scale'].mean())
        gc_vx.append(temp_gc['vx_scale'].mean())

        ns_vy.append(temp_ns['vy_scale'].mean())
        ns_vz.append(temp_ns['vz_scale'].mean())
        ns_vx.append(temp_ns['vx_scale'].mean())


        gc_vy_std.append(temp_gc['vy_scale'].std())
        gc_vz_std.append(temp_gc['vz_scale'].std())
        gc_vx_std.append(temp_gc['vx_scale'].std())

        ns_vy_std.append(temp_ns['vy_scale'].std())
        ns_vz_std.append(temp_ns['vz_scale'].std())
        ns_vx_std.append(temp_ns['vx_scale'].std())

    v_av_vals = pd.DataFrame({'gc_vy':gc_vy, 'gc_vz':gc_vz, 'gc_vx':gc_vx, 'ns_vy':ns_vy, 'ns_vz':ns_vz, 'ns_vx':ns_vx, 'gc_vy_std':gc_vy_std, 'gc_vz_std':gc_vz_std, 'gc_vx_std':gc_vx_std, 'ns_vy_std':ns_vy_std, 'ns_vz_std':ns_vz_std, 'ns_vx_std':ns_vx_std})
    
    return v_av_vals

def get_cartesian_points(rad_val):
    angles_arr = get_angles_arr()
    angles_arr = np.delete(angles_arr, 0) # delete the 0 at the beginning
    mid_angle = 2* np.pi/32

    mid_angle_arr = angles_arr - mid_angle

    x_rad = rad_val * np.cos(mid_angle_arr)
    y_rad = rad_val * np.sin(mid_angle_arr)

    return x_rad, y_rad

def polar_plotter(arr_ns, arr_gc):
    # Returns the median velosities of the polar vals
    v_av_vals = polar_split(arr_ns, arr_gc)
    
    x_rad, y_rad = get_cartesian_points(5)
    
    basic_rot_plot(x_rad, y_rad, v_av_vals, arr_gc)
    # Make angle array for the mid points
    angle_arr_2 = []
    for i in range(0,32):
        angle_arr_2.append(np.degrees((2*np.pi/16*i)+(2*np.pi/32)))

    angle_arr_2 = np.asarray(angle_arr_2)
    v_av_vals_2 = pd.concat([v_av_vals, v_av_vals])

    rot_theta_plot(angle_arr_2, v_av_vals_2)
    rot_theta__overlay_plot(angle_arr_2, v_av_vals_2)

def init_ts_stats(gas, new_1_20, new_1, new_2):
    if new_1_20.size == 0 or new_2.size ==0:
        print('0 value encountered - skipping printout')
        outputs.init_timestep = False
        return False
    else:
        print('#### Initial timestep stats ####')
        print('Number of gas particles: ', gas)
        print('Number of ID = 1 stars: ', new_1.size)
        print('Max index of ID = 1 stars: ', np.max(new_1))
        print('Number of ID = 1 in 20pc stars: ', new_1_20.size)
        print('Max index of ID = 1 in 20pc stars:: ', np.max(new_1_20))
        print('Number of ID = 2 stars: ', new_2.size)
        print('Max index of ID = 2 stars: ', np.max(new_2))
        print('################################')
        return True


def init_metal_cals(gas, id1, id2):
    #gas_r = np.sqrt(gas[:,0]**2 + gas[:,1]**2, gas[:,2]**2)

    id1_r = np.sqrt(id1[:,0]**2 + id1[:,1]**2, id1[:,2]**2)
    id2_r = np.sqrt(id2[:,0]**2 + id2[:,1]**2, id2[:,2]**2)
    total_GC = np.concatenate((id1_r, id2_r), axis = None)

    #plot as a histogram
    init_metal_grad(total_GC,id1_r,id2_r)
    init_metal_grad_kde(total_GC,id1_r,id2_r)



def init_plots(new):
    gal_init = np.load('gal_init.npy')
    gas_init = np.load('gas_init.npy')

    # Find the limit on what index we can get up to
    init_gas_len = np.shape(gas_init)[0]

    # Load in the indexed arrays
    ns_1_index = np.load('ns_1_index.npy')
    ns_2_index = np.load('ns_2_index.npy')

    # Restrict id=1 stars within 20 pc
    ns_index_20 = []
    for i in range(0, ns_1_index.size):
        if new.r[i] < 20:
            ns_index_20.append(ns_1_index[i])
    
    ns_index_20 = np.asarray(ns_index_20)

    # Allow any id=2 stars to be in the sample
    

    if outputs.print_init_state == True:
        can_plot = init_ts_stats(init_gas_len, ns_index_20, ns_1_index, ns_2_index)


    # To stop error that array was too long
    # Check using debug option if this needs to be done for both arrays
    #ns_index_20 = ns_index_20[ns_index_20[:]<init_gas_len]
    #ns_2_index = ns_2_index[ns_2_index[:]<init_gas_len]

    # ^^ Let program crash if the index is bigger

    if can_plot == True:
        # Apply indexing to the rows we want
        new_1_gas = gas_init[ns_index_20,:]
        new_2_gas = gas_init[ns_2_index,:]
        # The scatter plot with the 3 different componants
        original_loc(gas_init[:,0],gas_init[:,1], new_1_gas[:,0], new_1_gas[:,1],new_2_gas[:,0], new_2_gas[:,1])
        init_metal_cals(gas_init, new_1_gas, new_2_gas)
    

    # The 2x1 plot with the red crosses
    init_state(gal_init, gas_init, 4000, 2000)



def run_analysis(data):
    gal, gas, new, old = to_pandas_ts4(data)

    # Get the values of iwas from the original old array
    iwas4_arr = get_iwas(old)
    #iwas4_arr[0] += -1.4
    #iwas4_arr[1] += 0.2
    #iwas4_arr[2] += 0.2
    print(iwas4_arr)


    # crop outlier stars not needed for further analysis
    # (up the std from 1 to > 3 to have minimal scaling)
    
    bounds = std_bounds(old, outputs.bounds_std) # Get std bounds
    
    gal_crop = array_crop(gal, bounds)
    gas_crop = array_crop(gas, bounds)
    old_crop = array_crop(old, bounds)
    new_disk = new.loc[new.id == 1] # From the ISM
    new_crop_GC = new.loc[new.id ==2] # From the GC

    new_crop = new # To keep naming scheme
    #new_crop = array_crop(new, bounds) # To add the cropping back in
    

    basic_ns_scatter(new_crop_GC.x, new_crop_GC.y,new_disk.x, new_disk.y )
    
    # Testing version: no bounds 
    '''
    gal_crop = gal
    gas_crop = gas
    new_crop = new.loc[new['id'] ==2]
    old_crop = old
    '''

    print('cropped arrays')

    # Could change this to get_mean(gas_crop) if you wanted
    # to scale by the mean instead
    mean_vel_arr = get_mean_vel(old_crop)
    

    if outputs.iwas_centering == True:
        #gal_crop, gas_crop, new_crop, old_crop = scale_all(new_disk, gas_crop,new_crop, old_crop, iwas4_arr, mean_vel_arr)
        gal_crop, gas_crop, new_crop, old_crop = scale_all(gal_crop, gas_crop,new_crop, old_crop, iwas4_arr, mean_vel_arr)
    else:
        mean_pos_arr = get_mean_pos(old_crop)
        gal_crop, gas_crop, new_crop, old_crop = scale_all(gal_crop, gas_crop,new_crop, old_crop, mean_pos_arr, mean_vel_arr)

    print('scaled arrays')
    

    # -------- Plotting
    
    if outputs.los_plots == True:
        los_curve(old_crop, new_crop, 80) # Bin size of 80

    if outputs.binned_los_plots == True:
        binning_los(old_crop, new_crop)
    
    if outputs.position_3d_plot == True:
        position_3d(new_crop, iwas4_arr)

    if outputs.mass_ratio_plot == True:
        mass_ratio(old_crop, new_crop)

    if outputs.final_ts_plots == True:
        final_ts_plot_all(gal, gas, new_crop, old, 2000, 1000, iwas4_arr[0]+1000, iwas4_arr[1]+1000)
        final_ts_plot_scale(gal_crop, gas_crop, new_crop, old_crop, 60, 30)
        final_GC(new_crop, old_crop, 60, 30)
        #final_GC(new_crop, old_crop, 100, 50)

        
    
    # Do you want to load in the initial data?
    if outputs.init_timestep == True:
        init_plots(new_crop)

    if os.path.exists('new_crop.npy') == False:
        np.save('new_crop_rad', new_crop.r)

    # -------- Start summery portion 
    #  Note: the new star values being printed to the csv are of the total NS mass - both 1 & 2
    #        discrepancies within this mass and the mass of orbit is that this is cut to 20 and 
    #        orbit has 1.5*R (i.e. for a 20pc GC, cutoff of 30 pc)

    p_5 = get_values(gas_crop, new_crop.loc[new_crop['id']==2], old_crop, 5)
    p_20 = get_values(gas_crop, new_crop, old_crop, 20)
    #p_20 = get_values(gas_crop, new_crop.loc[new_crop['id']==2], old_crop, 20)
    get_para(p_5, p_20)

    # ----- Crop these arrays sepatately - all further anaysis will use the smaller dataset
    analysis_rad = 20

    gal_crop = gal_crop.loc[gal_crop['r']<analysis_rad]
    gas_crop = gas_crop.loc[gas_crop['r']<analysis_rad]
    #new_crop = new_crop.loc[(new_crop['id'] ==2) & (new_crop['r']< 20)] this is the one i was using previously
    new_crop = new_crop.loc[new_crop['r']<analysis_rad]
    old_crop = old_crop.loc[old_crop['r']<analysis_rad]

    #---- The following plots will use the smaller < 20 dataset
    print('Gal mass in to: ', gal_crop.mass.sum())

    if outputs.xyz_vel_plotter == True:
        xyz_vel_plot(new_crop.x_scale, new_crop.y_scale, new_crop.z_scale, new_crop.vx_scale, new_crop.vy_scale, new_crop.vz_scale)

    if outputs.polar_plot == True:
        polar_plotter(new_crop, old_crop)
        

    if outputs.cumulative_hist_plot == True:
        cumulative_hist(old_crop.r, new_crop.r)
    
    #interp_1G_2G(new_crop, old_crop, 30, 30)

    # The sum of only the stars formed within the GC

    new_crop_captured_1 = new_crop.loc[(new_crop['id'] ==1)].mass.sum()
    new_crop_captured_2 = new_crop.loc[(new_crop['id'] ==2)].mass.sum()
    new_crop_captured_3 = new_crop.loc[(new_crop['id'] ==3)].mass.sum()
    new_crop_captured_4 = new_crop.loc[(new_crop['id'] ==4)].mass.sum()
    new_crop_captured_5 = new_crop.loc[(new_crop['id'] ==5)].mass.sum()
    new_crop_captured = new_crop_captured_1+new_crop_captured_2+new_crop_captured_3+new_crop_captured_4+new_crop_captured_5
    # The ratio of stars formed within the GC to total new stars within the GC
    print('AGB mass: ', new_crop_captured)
    print('ISM mass: ', new_crop.mass.sum()-new_crop_captured)
    print('GC to captured stars ratio: ', new_crop_captured/new_crop.mass.sum())
    
