# Physical Processes.

## Overview of Physical Processes.

As a physical process, we can consider the following

 - cumulus convection process

 - large-scale condensation process

 - radiation process

 - vertical diffusion process

 - surface flux

 - Surface and underground processes

 - gravitational wave resistance

We compute the time-varying terms $F_x, F_y, Q, M, S$ for the forecast variables from these processes, and perform time integration. In order to evaluate the atmospheric and surface fluxes, the ground surface sub-model is used. The ground surface sub-model uses such predictors as the ground temperature ($T_g$), ground moisture ($W_g$), and snow cover ($W_y$) as predictor variables.

### Fundamental Equations.

Considering the equation of motion of the atmosphere in $\sigma$ coordinate system, thermodynamic equations, and equations for continuity of materials such as water vapor etc. Considering the vertical fluxes of momentum, heat, water vapor, etc., the time variation of the fluxes is determined by their convergence. All the vertical fluxes are assumed to be positive for the upward direction.

1. equation of motion

$$
  \rho \frac{d {u}}{d {t}} = \frac{\partial{Fu}}{\partial {\sigma}}
$$


$$
  \rho \frac{d {v}}{d {t}} = \frac{\partial{Fv}}{\partial {\sigma}}
$$


     $u, v$: East-West, North-South Wind; $Fu, Fv$: Their Vertical Flux.

2. thermodynamic equation

$$
  \rho \frac{d {c_p T}}{d {t}} = \frac{T}{\theta} \frac{\partial{F{\theta}}}{\partial {\sigma}} 
                     + \frac{\partial{F{R}}}{\partial {\sigma}} 
$$


     $T$: Temperature; $c_p$: Constant Pressure Specific Heat; $\theta=T(p/p_0)^{-R/c_p}=T(p/p_0)^{-\kappa}$: Temperature Level; $F\theta$: Vertical Sensible Heat Flux; $FR$: Vertical Radiation Flux.

 Here, with $\theta'=T(p/p_s)^{-\kappa}=T\sigma^{-\kappa}$, this is,

$$
  \rho \frac{d {c_p T}}{d {t}} = \sigma^\kappa \frac{\partial{F{\theta'}}}{\partial {\sigma}} 
                     + \frac{\partial{F{R}}}{\partial {\sigma}} 
$$


 As far as one-dimensional vertical processes are concerned, instead of $\theta$, we can consider $\theta'$. For simplicity, unless there is a risk of confusion, $\theta'$ should be written as $\theta$ below.

3. water vapor continuity formula

$$
  \rho \frac{d {q}}{d {t}} = \frac{\partial{Fq}}{\partial {\sigma}} 
$$


     $q$: Specific Humidity; $F{q}$: Vertical Water Vapor Flux.

     ### Fundamental Equations in the Ground

 Consider the $z$ coordinates with the downward direction positive. As expected, the vertical fluxes are all positive in the upward direction.

4. thermal formula

$$
  \frac{\partial{C_g G}}{\partial {t}} = \frac{\partial{Fg}}{\partial {z}} + Sg
$$


     $G$: Ground Temperature; $C_g$: Constant Pressure Specific Heat; $F{g}$: Vertical Heat Flux; $Sg$; Heating Term (due to phase change etc.).

5. formula for ground moisture

$$
  C_w \frac{\partial{w}}{\partial {t}} = \frac{\partial{Fw}}{\partial {z}} + Sw
$$


     $w$: Ground moisture; $F{w}$: Vertical water flux; $Sw$; Water sources (e.g., runoff).

6. energy balance equation

 At the surface, an energy balance is established.

$$
    F{\theta} + L F{q} + F{R} - F{g} = \Delta s \; \; (\sigma=1, z=0)
$$


     $L$: Latent heat of evaporation; $\Delta s$: Surface energy balance (associated with phase change, etc.).

7. surface water balance

$$
  Pg + Fw - Rg = 0
$$


     $Pg$: Precipitation; $Rg$: Surface Runoff.

8. the snow balance

$$
  \frac{\partial{Wy}}{\partial {t}} = Py - Fy - My
$$


     $Wy$: Snow cover (kg/m$^2$); $Py$: Snowfall; $Fy$: Sublimation; $My$: Snowmelt.

### Time integration of physical processes.

In terms of time integration of predictors, we can classify the physical processes in the following three orders of execution.

1. cumulus convection and large-scale condensation

2. radiation, vertical diffusion, ground boundary layer and surface processes

3. gravitational wave resistance, mass regulation, dry convection regulation

Cumulus convection and large-scale condensation,

$$
  \hat{T}^{t+\Delta t,(1)} = \hat{T}^{t+\Delta t} 
                         +  2 \Delta t Q_{CUM}(\hat{T}^{t+\Delta t})
$$


$$
  \hat{T}^{t+\Delta t,(2)} = \hat{T}^{t+\Delta t,(1)} 
                         +  2 \Delta t Q_{LSC}(\hat{T}^{t+\Delta t,(1)})
$$


where the values are updated by the usual Euler difference Note that the large-scale condensation scheme is updated by the cumulus convection scheme. In practice, the routines of cumulus convection and large-scale condensation output the heating rates and so on, and the time integration is performed immediately afterwards by `MODULE:[GDINTG]`.

The calculations of the radiative, vertical diffusion, ground boundary layer and surface processes in the following groups are basically performed with these updated values ($\hat{T}^{t+\Delta t,(1)}, \hat{q}^{t+\Delta t,(2)}$, etc.). However, in order to calculate some of the terms as implicit, we calculate the heating rates and so on for all of these terms together, and then perform time integration at the end. In other words, if we write symbolically

$$
  \hat{T}^{t+\Delta t,(3)} = \hat{T}^{t+\Delta t,(2)} 
              + 2 \Delta t Q_{RAD,DIF,SFC}
               (\hat{T}^{t+\Delta t,(2)},\hat{T}^{t+\Delta t,(3)})
$$


That would be.

The gravitational wave resistance, mass modulation, and dry convection modulation are the same as those for cumulus convection and large-scale condensation.

$$
  \hat{T}^{t+\Delta t,(4)} = \hat{T}^{t+\Delta t,(3)} 
              +  2 \Delta t Q_{ADJ}(\hat{T}^{t+\Delta t,(3)})
$$


### Various physical quantities.

Here are definitions of various geophysical quantities that can be computed simply from the predictors. Some of them are calculated with `MODULE:[PSETUP]`.

1. temporary temperature

 Provisional Temperature $T_v$ is ,

$$
  T_v = T ( 1 + \epsilon_v q - l )
$$


2. air density

 The atmospheric density $\rho$ is calculated as follows

$$
  \rho = \frac{p}{RT_v}
$$


3. high degree

 The altitude $z$ is evaluated in the same way as the calculation of the geopotential for mechanical processes.

$$
  z = \frac{\Phi}{g} 
$$


$$
 \Phi_{1}  =  \Phi_{s} + C_{p} ( \sigma_{1}^{-\kappa} - 1  ) T_{v,1}
$$


$$
 \Phi_k - \Phi_{k-1} 
   =  C_{p}
   \left[ \left( \frac{ \sigma_{k-1/2} }{ \sigma_k } \right)^{\kappa}
          - 1 \right] T_{v,k} 
       + C_{p}
   \left[ 1- 
         \left( \frac{ \sigma_{k-1/2} }{ \sigma_{k-1} } \right)^{\kappa}
              \right] T_{v,k-1}
$$


4. layer boundary temperature

 The temperature at the boundary of the layer is calculated by performing a linear interpolation on $\ln p$, i.e., $\ln \sigma$.

$$
  T_{k-1/2} = \frac{\ln \sigma_{k-1} - \ln \sigma_{k-1/2}}
                   {\ln \sigma_{k-1} - \ln \sigma_k      } T_k
            + \frac{\ln \sigma_{k-1/2} - \ln \sigma_k}
                   {\ln \sigma_{k-1} - \ln \sigma_k      } T_{k-1}
$$


5. saturated specific humidity

 The saturated specific humidity $q^*(T,p)$ are approximated using the saturated vapor pressure $e^*(T)$,

$$
q^*(T,p) = \frac{\epsilon e^*(T)}{p} .
$$


 Here, it is $\epsilon=0.622$,

$$
\frac{1}{e^*_v} \frac{\partial{e^*_v}}{\partial {T}} = \frac{L}{R_v T^2}
$$


 Therefore, if the latent heat of evaporation ($L$) and the gas constant of water vapor ($R_v$) are held constant, the number of vaporized materials will be reduced,

$$
  e^*(T) = e^*(T=273{K}) 
                      \exp \left[ \frac{L}{R_v} 
                            \left( \frac{1}{273} - \frac{1}{T} \right)
                       \right] ,
$$


     .....

     (199) from ,

$$
\frac{\partial{q^*}}{\partial {T}} = \frac{L}{R_v T^2} q^*(T,p) .
$$


 Here, if the temperature is lower than the freezing point 273.15K, the sublimation latent heat $L+L_M$ is used as the latent heat $L$.

6. dry static energy, wet static energy

 Dry static energy $s$ is

$$
  s = C_p T + g z \; ,
$$


 Wet Static Energy $h$ is

$$
  h = C_p T + g z + L q \; ,
$$


 . defined by .
