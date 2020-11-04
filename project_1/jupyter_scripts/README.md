# Jupyter scripts used for all the analysis

I have come to the conclusion that interactive notebooks are the fastest way to analyse these datasets. 
I should have probably turned these into proper scripts but I'm lazy and:
```
if !broken: 
  !fix
```

## File descriptions
- 1_phase_animation
Imports the information from the ```anim.dat``` file and outputs a gif off the simulation. Does not require anything to be imported by the analysis file

- 1_phase_dispersion
Playing around with the gas and disc dispersions trying to figure out whether you can get any stellar captures by the GC

- Centering_script
The most important script here!! This performs all the analysis and creates all the plots. 
The location of the first particle is used as an initial guess for the centre of the cluster. This guess is ok for large scales but calculating radial gradients needs something more precise.

A 3D KDE is used to get the centre of the 1G, this is the purpose of the initial section of the script. After that, most of the code is used for plotting and summarising masses which are used for scaling relations. 

- Fiducial_model is similar to the centring_script but checks things specifically for the fiducial
- Final time step plotting creates the plots for the final time step for the fiducial that's used in the paper
- Kinematics makes the kinematic plots used in the paper

