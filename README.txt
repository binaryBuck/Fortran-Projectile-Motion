Written by: Darren Sun

This repository uses Fortran to calculate projectile motion of an object. We assume 
 * Weight(Mass) is a negligible factor, because acceleration due to gravity is constant near Earth’s surface (about 9.8 m/s²) and acts equally on all objects regardless of their mass. 
 * There is negligible air resistance. 
 * The ground is flat and level. 
 * No wind of external forces. 
 * Point mass, the object is treated as a point without rotation, shape, or size effects. 
 * Instantaneous velocity, no acceleration is applied on (u) launch velocity. 
 * Simplified 2-Dimensional X-Y motion. 

There will be 3 inputs prompted from the command line via stdin:
    (Time) the total time from launch to measurement
    (U) the launch velocity
    (Angle) the initial angle of launch (in degree)
    (g) the acceleration due to gravity
And a constant: 
    (g) the acceleration due to gravity 9.8m/s^2

The program runs 5 loops, doubling (U) launch velocity each time. 

Result:
The output of the program will show 5 simulations each time doubling the launch velocity. 
If the total time (Time) input parameter is larger than the total flight time of the projectile returning back to initial launch height, 
then this program shall throw an error and indicate the total flight time to return back to launch height and not cease to run. 
Instead, if the total (Time) from launch to measurement is greater than the total flight time, we continue to calculate and show the 
negative vertical displacement and direction, assuming the projectile continues to fall until (Time). 

Compile and run on MacOS with GNU Fortran (Homebrew GCC 12.2.0) 12.2.0: 

>> gfortran projectilesim.f90 -o projectilesim
>> ./projectilesim
>> INPUT PARAMETERS, EXAMPLE: 15, 2.5, 60
    *** WARNING: Input time exceeds total flight time ***
    Input time:   15.0000000     s
    Total flight time:  0.441849649     s
    Results correspond to input time, which is after landing.
    --- Simulation #           1  ---
    Launch velocity (U):    2.50000000    
    Time (input):    15.0000000    
    Horizontal displacement :    18.7500019    
    Vertical displacement   :   -1070.02405    
    Resultant velocity      :    144.840317    
    Direction (in degrees)  :   -89.5055237    

    *** WARNING: Input time exceeds total flight time ***
    Input time:   15.0000000     s
    Total flight time:  0.883699298     s
    Results correspond to input time, which is after landing.
    --- Simulation #           2  ---
    Launch velocity (U):    5.00000000    
    Time (input):    15.0000000    
    Horizontal displacement :    37.5000038    
    Vertical displacement   :   -1037.54810    
    Resultant velocity      :    142.691772    
    Direction (in degrees)  :   -88.9961090    

    *** WARNING: Input time exceeds total flight time ***
    Input time:   15.0000000     s
    Total flight time:   1.76739860     s
    Results correspond to input time, which is after landing.
    --- Simulation #           3  ---
    Launch velocity (U):    10.0000000    
    Time (input):    15.0000000    
    Horizontal displacement :    75.0000076    
    Vertical displacement   :   -972.596191    
    Resultant velocity      :    138.430084    
    Direction (in degrees)  :   -87.9300690    

    *** WARNING: Input time exceeds total flight time ***
    Input time:   15.0000000     s
    Total flight time:   3.53479719     s
    Results correspond to input time, which is after landing.
    --- Simulation #           4  ---
    Launch velocity (U):    20.0000000    
    Time (input):    15.0000000    
    Horizontal displacement :    150.000015    
    Vertical displacement   :   -842.692383    
    Resultant velocity      :    130.064484    
    Direction (in degrees)  :   -85.5904694    

    *** WARNING: Input time exceeds total flight time ***
    Input time:   15.0000000     s
    Total flight time:   7.06959438     s
    Results correspond to input time, which is after landing.
    --- Simulation #           5  ---
    Launch velocity (U):    40.0000000    
    Time (input):    15.0000000    
    Horizontal displacement :    300.000031    
    Vertical displacement   :   -582.884766    
    Resultant velocity      :    114.125114    
    Direction (in degrees)  :   -79.9070129