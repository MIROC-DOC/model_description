## Gravitational wave resistance

**NOTE: the descriptions in this section are outdated.**

### Gravitational Wave Resistance Scheme Overview

The gravitational wave resistance scheme represents the upward momentum flux of the gravitational waves induced by sub-grid scale topography and calculates the horizontal wind deceleration associated with its convergence. The main input data are east-west wind ($u$), north-south wind ($v$), and temperature ($T$), and the output data are the rates of temporal variation of east-west wind and north-south wind, $\partial u/\partial t, \partial v/\partial t$.

The outline of the calculation procedure is as follows.

The momentum flux at the ground surface is calculated from the dispersion of surface height, the horizontal wind speed at the lowest level, and the stratification stability.

We consider the upward propagation of gravitational waves with momentum fluxes. If the momentum flux exceeds the critical fluid number, the momentum flux is determined by the critical fluid number, then breaking waves occur and the flux becomes the critical value of the momentum flux.

3. compute the time evolution of the horizontal wind as the momentum flux converges in each layer.

### Relationship between local fluid number and momentum flux

Considering the vertical flux of horizontal momentum due to surface-derived gravitational waves, the difference between the flux ($\tau$) and the local fluid number ($F_L = NH/U$) at a certain altitude is

$$
   F_L = \left(
            \frac{\tau N}{E_f \rho U^3}
           \right)^{1/2} \; ,
$$

This relationship holds for the following cases where $N = g/\theta \partial \theta/\partial z$ is the Brant-Visala frequency, $\rho$ is the density of the atmosphere, $U$ is the wind speed, and $E_f$ is the proportional constant corresponding to the horizontal scale of the rippling at the surface. From now on,

$$
  \tau = \frac{E_f F_L^2 \rho U^3}{N}
$$

The local fluid number ($F_L$) cannot exceed the critical fluid number ($F_{c}$) at a certain value. If the local fluid number calculated from (589) exceeds the critical fluid number $F_{c}$, the gravitational wave becomes supersaturated and the flux decreases to the momentum flux corresponding to the critical fluid number.

### Momentum fluxes at the surface.

The magnitude of the vertical flux of horizontal momentum due to gravitational waves excited at the earth's surface, $\tau_{1/2}$, is calculated by substituting the local fluid number $(F_L)_{1/2} = N_1 h/U_1$ into (590),

$$
  \tau_{1/2} = E_f h^2 \rho_1 N_1 U_1 \; ,
$$

where $U_1 = |{\mathbf v}_1| = (u_1^2 + v_1^2)^{1/2}$ is the surface wind speed, $N_1, \rho_1$ are estimated to be the stability and density of the atmosphere near the earth's surface, respectively. where $U_1 = |{\mathbf v}_1| = (u_1^2 + v_1^2)^{1/2}$ is the surface wind speed, and $N_1, \rho_1$ are the stability and density of the atmosphere near the earth's surface, respectively. $h$ is an indicator of the change in the surface height of the sub-grid and is assumed to be equal to the standard deviation of the surface height ($Z_{SD}$).

Here, when the local fluid number ($(F_L)_{1/2} = N_1 Z_{SD}/U_1$) exceeds the critical fluid number ($F_c$), the momentum flux is suppressed to the value obtained by substituting (590) for $F_c$. In other words,

$$
  \tau_{1/2} = \min \left(
                   E_f Z_{SD}^{2} \rho_1 N_1 U_1, \;
                  \frac{E_f F_c^{2} \rho_1 U_1^3}{N_1}
               \right)
$$

### Momentum fluxes in the upper levels.

Suppose that the momentum flux $\tau_{k-1/2}$ is required for level $k-1/2$. When no saturation occurs, $\tau_{k+1/2}$ is equal to $\tau_{k-1/2}$. If the momentum flux ($\tau_{k-1/2}$) exceeds the momentum flux calculated from the critical fluid number at the $k+1/2$ level, wave breaking occurs in the $k$ layer and the momentum flux decreases to the critical flux.

$$
  \tau_{k+1/2} = \min \left(
               \tau_{k-1/2}, \;
               \frac{E_f F_c^2 \rho_{k+1/2} U_{k+1/2}^3}{N_{k+1/2}}
                      \right),
$$

Note that $U_{k+1/2}$ is the magnitude of the projective component of the wind speed vectors for each layer relative to the direction of the lowest level of the horizontal wind,

$$
  U_{k+1/2} = \frac{{\mathbf v}_{k+1/2}
                      \cdot {\mathbf v}_{1}}
                   {|{\mathbf v}_{1}|       }
$$

### The magnitude of the time variation of horizontal wind due to momentum convergence.

The temporal rate of change of the projective component of the horizontal wind, $U_{k}$, is ,

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

Using this, the temporal rates of change for the east-west and north-south winds are calculated as follows

$$
  \frac{\partial u_{k}}{\partial t}  =
           \frac{\partial U_{k}}{\partial t} \frac{u_{1}}{U_{1}} \\
  \frac{\partial v_{k}}{\partial t}  =
           \frac{\partial U_{k}}{\partial t} \frac{v_{1}}{U_{1}}
$$

### Other Notes.

1. it is assumed that no gravitational waves are excited at the ground surface when the wind speed is small ($U_{1} \le v_{min}$) and when the undulations at the surface are small ($Z_{SD} \le (Z_{SD})_{min}$).
