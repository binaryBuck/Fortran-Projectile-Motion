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
>> INPUT PARAMETERS, EXAMPLE: 7, 2, 60
    *** WARNING: Input time exceeds total flight time ***
    Input time:   7.00000000     s
    Total flight time:  0.353479743     s
    Results correspond to input time, which is after landing.
    --- Simulation #           1  ---
    Launch velocity (U):    2.00000000    
    Time (input):    7.00000000    
    Horizontal displacement :    7.00000095    
    Vertical displacement   :   -227.975647    
    Resultant velocity      :    66.8754272    
    Direction (in degrees)  :   -89.1432190    

    *** WARNING: Input time exceeds total flight time ***
    Input time:   7.00000000     s
    Total flight time:  0.706959486     s
    Results correspond to input time, which is after landing.
    --- Simulation #           2  ---
    Launch velocity (U):    4.00000000    
    Time (input):    7.00000000    
    Horizontal displacement :    14.0000019    
    Vertical displacement   :   -215.851288    
    Resultant velocity      :    65.1665878    
    Direction (in degrees)  :   -88.2412872    

    *** WARNING: Input time exceeds total flight time ***
    Input time:   7.00000000     s
    Total flight time:   1.41391897     s
    Results correspond to input time, which is after landing.
    --- Simulation #           3  ---
    Launch velocity (U):    8.00000000    
    Time (input):    7.00000000    
    Horizontal displacement :    28.0000038    
    Vertical displacement   :   -191.602585    
    Resultant velocity      :    61.8013802    
    Direction (in degrees)  :   -86.2890244    

    *** WARNING: Input time exceeds total flight time ***
    Input time:   7.00000000     s
    Total flight time:   2.82783794     s
    Results correspond to input time, which is after landing.
    --- Simulation #           4  ---
    Launch velocity (U):    16.0000000    
    Time (input):    7.00000000    
    Horizontal displacement :    56.0000076    
    Vertical displacement   :   -143.105164    
    Resultant velocity      :    55.3250465    
    Direction (in degrees)  :   -81.6858902    

    *** WARNING: Input time exceeds total flight time ***
    Input time:   7.00000000     s
    Total flight time:   5.65567589     s
    Results correspond to input time, which is after landing.
    --- Simulation #           5  ---
    Launch velocity (U):    32.0000000    
    Time (input):    7.00000000    
    Horizontal displacement :    112.000015    
    Vertical displacement   :   -46.1103210    
    Resultant velocity      :    43.9062843    
    Direction (in degrees)  :   -68.6285706    