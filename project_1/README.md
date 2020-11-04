# Code used during Project 1: Multiple Stellar Populations and Internal Kinematics

## File descriptions:
### Analysis scripts
The simulation outputs three files of interest; tout.dat, orbit.dat and sf.dat. This file takes the information in these tables, scales them into physical units, and converts them to python arrays and performs some basic analysis.

#### tout.dat 
Contains all information on the particles at a specific time step. It generally takes the form:
![tout.dat](./tout.dat_description.png?raw=true "tout.dat")
where letters from A to J contain information about the mass resolution and softening length of the particles and K to M are changed depending on which version of the simulation is being used. 

#### orbit.dat 
Contains only the x, y, z and mass of all the components 

#### sf.dat 
Contains information about star formation.


### Jupyter notebooks
These notebooks take the information from the python arrays output from the analysis scripts and then does a much deaper analysis.
The outputs saved on github should contain the information from the fiducial model.
There are two versions of our model: one that contains information on whether a 2G star is an ex-situ (formed outside the cluster and accreted) or in-situ (formed within the 1G) and another version which contains the helium ubundances of the 2G stars.
Different cells are executed depending on the model.

### Scaling relations
This file compiles the outputs from the jupyter notebooks in order to create scaling realtions for the models used
