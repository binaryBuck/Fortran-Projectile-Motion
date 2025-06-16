! --------------------------------------------------------------------
! Given 
!   (Time) the total time from launch to measurement
!   (U) the launch velocity
!   (Angle) the initial angle of launch (in degree)
!   (g) the acceleration due to gravity
! this program computes the position (x and y coordinates)
! and the velocity (magnitude and direction) of a projectile.
! --------------------------------------------------------------------

PROGRAM ProjectileSim
   IMPLICIT NONE

   ! NOTE: In Fortran, REAL indicates a float data type. 
   REAL, PARAMETER :: g  = 9.8
   REAL, PARAMETER :: PI = 3.1415926
   REAL            :: Angle             ! Launch angle in degrees
   REAL            :: Time              ! Input time of flight
   REAL            :: Theta             ! Direction of velocity (degrees)
   REAL            :: U                 ! Launch velocity (m/s)
   REAL            :: V                 ! Resultant velocity
   REAL            :: Vx, Vy            ! Velocity components
   REAL            :: X, Y              ! Displacements
   REAL            :: TotalFlightTime   ! Calculated total flight time
   REAL            :: AngleRad          ! Launch angle in radians
   INTEGER         :: i                 ! Loop counter

   READ(*,*)  Time, U, Angle

   ! Convert angle to radians once for calculations
   AngleRad = Angle * PI / 180.0

   ! Calculate total flight time assuming launch and landing heights are equal
   TotalFlightTime = 2.0 * U * SIN(AngleRad) / g

   DO i = 1, 5

      ! Check if input time exceeds total flight time
      IF (Time > TotalFlightTime) THEN
         WRITE(*,*) '*** WARNING: Input time exceeds total flight time ***'
         WRITE(*,*) 'Input time:', Time, 's'
         WRITE(*,*) 'Total flight time:', TotalFlightTime, 's'
         WRITE(*,*) 'Results correspond to input time, which is after landing.'
      END IF

      ! Compute position and velocity at input time
      X  = U * COS(AngleRad) * Time
      Y  = U * SIN(AngleRad) * Time - 0.5 * g * Time**2
      Vx = U * COS(AngleRad)
      Vy = U * SIN(AngleRad) - g * Time
      V  = SQRT(Vx**2 + Vy**2)
      Theta = ATAN2(Vy, Vx) * 180.0 / PI  ! Use ATAN2 for full angle range

      ! Output results
      WRITE(*,*) '--- Simulation #', i, ' ---'
      WRITE(*,*) 'Launch velocity (U): ', U
      WRITE(*,*) 'Time (input): ', Time
      WRITE(*,*) 'Horizontal displacement : ', X
      WRITE(*,*) 'Vertical displacement   : ', Y
      WRITE(*,*) 'Resultant velocity      : ', V
      WRITE(*,*) 'Direction (in degrees)  : ', Theta
      WRITE(*,*)

      ! Double velocity for next iteration
      U = U * 2.0

      ! Recalculate total flight time for new velocity
      TotalFlightTime = 2.0 * U * SIN(AngleRad) / g
   END DO

END PROGRAM ProjectileSim