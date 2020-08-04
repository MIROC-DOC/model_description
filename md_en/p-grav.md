## Gravitational wave resistance

### Gravitational Wave Resistance Scheme Overview

The gravitational wave resistance scheme is,
Excited by sub-grid scale terrain
The upward momentum flux of the gravitational wave is represented,
The horizontal wind deceleration associated with its convergence is calculated.
The main input data are: east-west wind $u$, north-south wind $v$, and temperature $T$,
The output data is the time rate of change for the east-west and north-south winds,
$\partial u/\partial t, \partial v/\partial t$, is.

The outline of the calculation procedure is as follows.

1. the momentum flux at the ground surface.
 Dispersion of surface altitude,
 The horizontal wind speed at the lowest level, stratification stability, etc.

2. consider the upward propagation of gravitational waves with momentum fluxes.
 Momentum fluxes are determined from the critical fluid number
 If the critical flux is exceeded,
 Suppose a breaking wave occurs and the flux is at its critical value.

3. according to the convergence of the momentum flux at each layer.
 Calculate the time variation of the horizontal wind.

### Relationship between local fluid number and momentum flux

The gravitational waves of surface origin
Given the vertical flux of horizontal momentum,
Flux at a certain altitude $\tau$ and
Local Fluid Number $F_L = NH/U$ and ,

$$
   F_L = \left(
            \frac{\tau N}{E_f \rho U^3}
           \right)^{1/2} \; ,
$$


The relationship between the two is valid.
Here, $N = g/\theta \partial \theta/\partial z$ is
Brandt Vaisala Frequency,
$\rho$ is the density of the atmosphere,
$U$ corresponds to the wind speed and $E_f$ corresponds to the horizontal scale of the ripples on the ground surface
It is a proportional constant .
Now..,

$$
  \tau = \frac{E_f F_L^2 \rho U^3}{N}
$$


Local Fluid Number $F_L$ is ,
Assume that a certain value, the critical fluid number $F_{c}$, cannot be exceeded.
Calculated from (1)
If the local fluid number exceeds the critical fluid number $F_{c}$
The gravitational waves are supersaturated,
Up to the momentum flux corresponding to the critical fluid number
Flux decreases.

### Momentum fluxes at the surface.

due to gravitational waves excited at the earth's surface.
The magnitude of the vertical flux of horizontal momentum $\tau_{1/2}$ is ,
except for the local fluid number at the surface
$(F_L)_{1/2} = N_1 h/U_1$.
(2) by substituting (2) for ,

$$
  \tau_{1/2} = E_f h^2 \rho_1 N_1 U_1 \; ,
$$


It is estimated that .
Here,
The $U_1 = |{\mathbf v}_1| = (u_1^2 + v_1^2)^{1/2}$ has a surface wind speed of ,
$N_1, \rho_1$ are the two most common types of data in the atmosphere near the earth's surface.
It is stability and density.
$h$ is an indicator of the sub-grid surface elevation change,
Assume that the standard deviation of the surface elevation is equal to $Z_{SD}$.

Here, the local fluid number at the surface
If $(F_L)_{1/2} = N_1 Z_{SD}/U_1$ is the critical fluid number
When you exceed the $F_c$,
The momentum flux is calculated by substituting $F_c$ into (2) and
Let's say it can be contained.
Namely,

$$
  \tau_{1/2} = \min \left(
                   E_f Z_{SD}^{2} \rho_1 N_1 U_1, \; 
                  \frac{E_f F_c^{2} \rho_1 U_1^3}{N_1}
               \right)
$$


### Momentum fluxes in the upper levels.

The momentum flux at level $k-1/2$ is
Suppose we are required to.
$\tau_{k+1/2}$, when no saturation occurs
Equal to $\tau_{k-1/2}$.
This momentum flux, $\tau_{k-1/2}$, is ,
Momentum fluxes calculated from the critical fluid number at the $k+1/2$ level
In the case of a wave breaking event that exceeds
The momentum flux decreases to the flux corresponding to the criticality.

$$
  \tau_{k+1/2} = \min \left( 
               \tau_{k-1/2}, \;
               \frac{E_f F_c^2 \rho_{k+1/2} U_{k+1/2}^3}{N_{k+1/2}}
                      \right),
$$


However, the $U_{k+1/2}$,
. of the wind velocity vector at each layer,
It is the magnitude of the projective component of the lowest level with respect to the direction of the horizontal wind,

$$
  U_{k+1/2} = \frac{{\mathbf v}_{k+1/2} 
                      \cdot {\mathbf v}_{1}}
                   {|{\mathbf v}_{1}|       }
$$


### The magnitude of the time variation of horizontal wind due to momentum convergence.

The temporal rate of change of the projective component of the horizontal wind, $U_{k}$, is

$$
  \frac{\partial U}{\partial t} 
        = - \frac{1}{\rho} \frac{\partial \tau}{\partial z}
        = g  \frac{\partial \tau}{\partial p}
$$


as determined by i.e. ,

$$
  \frac{\partial U_{k}}{\partial t} 
        =  g  \frac{\tau_{k+1/2} - \tau{k-1/2}}{\Delta p}.
$$


With this ,
The rate of change of the east-west and north-south winds over time is calculated as follows.

$$
  \frac{\partial u_{k}}{\partial t}  = 
           \frac{\partial U_{k}}{\partial t} \frac{u_{1}}{U_{1}} \\
  \frac{\partial v_{k}}{\partial t}  = 
           \frac{\partial U_{k}}{\partial t} \frac{v_{1}}{U_{1}}
$$



### Other Notes.

1. when the wind speed at the lowest level is small ($U_{1} \le v_{min}$) and
 In the case of small undulations in the earth's surface ($Z_{SD} \le (Z_{SD})_{min}$),
 Assuming no gravitational waves are excited at the earth's surface.
