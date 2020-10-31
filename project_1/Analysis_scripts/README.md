# Description of code

To run scripts, open a new terminal in the analys file:

``` python3 run.py name/of/directory/with/simulation/output```

Use ```output.py``` to change what scripts are being run. 


These scrips will analyse the output files ```tout.dat```, ```orbit.dat``` and ```sf.dat```.

```tout.dat``` contains the 6D phase space information and other parameters for each particle in the simulations (depending on file it might not contain DM output but the scripts will take care of that)

note:
iwas outputs: 

     = 0: DM

     = 1: disc stars
     
     = 2: gas
     
     = 3: old stars (1G)
     
     = 4: new stars (2G)
     


```orbit.dat``` gives all the masses of all the componenets surounding iwas = 4 in a radius of $R_{1G}*1.5$ (i.e. for the fiducial model with r = 20, that means within a radius of 30 pc)



```sf.dat``` gives the star formation rate at each time step
