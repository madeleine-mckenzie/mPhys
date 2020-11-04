# JuPyter scripts for the second part of the project

## File description:

### 2_phase_2x3_plots
Makes the 6 panel time step plots

### 2_phase_new_disc

It was noticed that ram pressure impacts the gas component and it isnt centred on this disc and new stars. Therefore the analysis is re-performed for these components with different density cut off chrietera. It also outputs the 2x1 plot for the new and disc star components used in the paper.
Also, I use this file to calculate the metallicity scaling relations.

### 2_phase_animation
Just like the animation file in the previous project, it makes a gif of the galaxy's evolution. 

### 2_phase_import3
The most important file!!
This includes the clump finding algorithm. The code is (hopefully) well commented and plots have been left in to explain how the alogirthm works. Note this file may take a while to load on github

### metallicity_plots
Creating the large metallicity plots of the eight largest clumps. Need to know the directories of the largest clumps for it to work. Run after you ahve run 2_phase_import.
