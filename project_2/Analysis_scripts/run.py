# Custom files
import outputs

import tout



import sys
import os
import numpy as np


path = sys.argv[1]
os.chdir(path)
print('Accessing directory: ', os.getcwd())

def reconstruct_timestep():
    final_timestep = []
    final_timestep.append(np.load('gal.npy'))
    final_timestep.append(np.load('gas.npy'))
    final_timestep.append(np.load('new.npy'))
    final_timestep.append(np.load('old.npy'))
    return final_timestep

def main():
    # Imports everything and makes spatial plot if nececcary
    # Final time step should be a 3D array containing gal, gas, new & old
    if outputs.run_tout == True:

        file_exists = os.path.exists('timestep.npy')
        print('file exists? ',file_exists)

        if outputs.run_from_file == False or file_exists == False:            
            tout.run_tout()
            
        else: # Used for debugging & testing
            print('running from file')
            reconstruct_timestep()
            

    



if __name__ == "__main__":
    main()
