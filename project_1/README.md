# Code used during Project 1: Multiple Stellar Populations and Internal Kinematics

File descriptions:
- Analysis scripts
The simulation outputs three files of interest; tout.dat, orbit.dat and sf.dat.

tout.dat contains all information on the particles at a specific time step. It generally takes the form:
![tout.dat](./tout.dat_description.png?raw=true "tout.dat")
where letters from A to J contain information about the mass resolution and softening length of the particles and K to M are changed depending on which version of the simulation is being used. 

orbit.dat contains only the x, y, z and mass of all the components and sf.dat contains information about star formation.

This file takes the information in these tables, scales them into physical units, and converts them to python arrays and performs some basic analysis.

- Jupyter notebooks
These notebooks take the information from the python arrays output from the analysis scripts and then does a much deaper analysis.

- Scaling relations
This file compiles the outputs from the jupyter notebooks in order to create scaling realtions for the models used
