## Gravity Waves

### Overview of a gravity wave drag parameterization

The orographic gravity wave drag scheme represents the upward momentum flux of the gravity waves induced by sub-grid scale topography and calculates the horizontal wind deceleration associated with its convergence (McFarlane, 1987). The main input data are eastward wind ($u$), northward wind ($v$), and temperature ($T$), and the output data are the tendency of eastward wind and northward wind, $\partial u/\partial t, \partial v/\partial t$.

The outline of the calculation procedure is as follows.

1. The momentum flux at the ground surface is calculated from the variance of sub-grid scale orography, the horizontal wind speed at the lowest level, and the static stability.

2. The upward propagation of gravity waves is considered. If the momentum flux exceeds its critical value, which is determined by the critical Froude number, then wave breaking occurs and the momentum is limited by the critical value.

3. The tendency of horizontal wind is obtained by calculating the vertical convergence of momentum flux in each layer.

### Relationship between local Froude number and momentum flux

Considering the vertical flux of horizontal momentum due to orographic gravity waves, the difference between the flux ($\tau$) and the local Froude number ($F_L = NH/U$) at a certain altitude is

$$
   F_L = \left(
            \frac{\tau N}{E_f \rho U^3}
           \right)^{1/2} \; , \tag{p-grav.589}
$$

This relationship holds for the following cases where $N = g/\theta \partial \theta/\partial z$ is the Brant-Väisälä frequency, $\rho$ is the density of the atmosphere, $U$ is the wind speed, and $E_f$ is the proportional constant corresponding to the horizontal scale of the rippling of the surface. From now on,

$$
  \tau = \frac{E_f F_L^2 \rho U^3}{N} \tag{p-grav.590}
$$

The local Froude number ($F_L$) cannot exceed the critical Froude number ($F_{c}$). If the local Froude number calculated from ([589](p-grav.589)) exceeds the critical Froude number $F_{c}$, the gravity wave becomes supersaturated and the flux decreases to the momentum flux corresponding to the critical Froude number.

### Momentum fluxes at the surface.

The magnitude of the vertical flux of horizontal momentum due to gravity waves excited at the earth's surface, $\tau_{1/2}$, is calculated by substituting the local Froude number $(F_L)_{1/2} = N_1 h/U_1$ into ([590](p-grav.590)),

$$
  \tau_{1/2} = E_f h^2 \rho_1 N_1 U_1 \; ,
$$

where $U_1 = |{\mathbf v}_1| = (u_1^2 + v_1^2)^{1/2}$ is the surface wind speed, $N_1, \rho_1$ are estimated to be the stability and density of the atmosphere near the earth's surface, respectively. $h$ is an indicator of the change in the sub-grid orography and is assumed to be equal to the standard deviation of the surface height ($Z_{SD}$).

Here, when the local Froude number ($(F_L)_{1/2} = N_1 Z_{SD}/U_1$) exceeds the critical Froude number ($F_c$), the momentum flux is suppressed to the value obtained by substituting ([590](p-grav.590)) for $F_c$. In other words,

$$
  \tau_{1/2} = \min \left(
                   E_f Z_{SD}^{2} \rho_1 N_1 U_1, \;
                  \frac{E_f F_c^{2} \rho_1 U_1^3}{N_1}
               \right)
$$

### Momentum fluxes in the upper levels.

Suppose that the momentum flux $\tau_{k-1/2}$ is computed at level $k-1/2$. When no saturation occurs, $\tau_{k+1/2}$ is equal to $\tau_{k-1/2}$. If the momentum flux ($\tau_{k-1/2}$) exceeds the momentum flux calculated from the critical Froude number at the $k+1/2$ level, wave breaking occurs in the $k$ layer and the momentum flux decreases to the critical flux.

$$
  \tau_{k+1/2} = \min \left(
               \tau_{k-1/2}, \;
               \frac{E_f F_c^2 \rho_{k+1/2} U_{k+1/2}^3}{N_{k+1/2}}
                      \right),
$$

Note that $U_{k+1/2}$ is the magnitude of the horizontal wind speed projected on to the direction of the lowest level of the horizontal wind,

$$
  U_{k+1/2} = \frac{{\mathbf v}_{k+1/2}
                      \cdot {\mathbf v}_{1}}
                   {|{\mathbf v}_{1}|       }
$$

### The magnitude of the time variation of horizontal wind due to momentum convergence.

The tendency of the projected component of the horizontal wind, $U_{k}$, is ,

$$
  \frac{\partial U}{\partial t}
        = - \frac{1}{\rho} \frac{\partial \tau}{\partial z}
        = g  \frac{\partial \tau}{\partial p}.
$$

That is

$$
  \frac{\partial U_{k}}{\partial t}
        =  g  \frac{\tau_{k+1/2} - \tau{k-1/2}}{\Delta p}.
$$

Using this, tendency for the eastward and northward winds are calculated as follows

$$
  \frac{\partial u_{k}}{\partial t}  =
           \frac{\partial U_{k}}{\partial t} \frac{u_{1}}{U_{1}} \\
  \frac{\partial v_{k}}{\partial t}  =
           \frac{\partial U_{k}}{\partial t} \frac{v_{1}}{U_{1}}
$$

### Other Notes.

1. it is assumed that no gravity waves are excited at the ground surface when the wind speed is small ($U_{1} \le v_{min}$) or when the undulations at the surface are small ($Z_{SD} \le (Z_{SD})_{min}$).
