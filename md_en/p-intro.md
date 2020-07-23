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

The time-varying terms of the forecast variables due to these processes
Calculate $F_x, F_y, Q, M, S$, $F_x, F_y, Q, M, S$ and do time integration.
In addition, in order to evaluate the atmospheric and surface fluxes
Using the surface sub-model.
In the surface sub-model,
Ground Temperature $T_g$, Ground Moisture $W_g$, Snowpack $W_y$, etc.
It is used as a predictor variable.

### Fundamental Equations.

Equation of motion of the atmosphere in the $\sigma$ coordinate system, thermodynamic equation,
Consider the equation for a sequence of substances such as water vapor.
The vertical fluxes of momentum, heat, water vapor, etc. are considered,
Find the time variation due to its convergence.
All vertical fluxes are positive upward.

1. equation of motion

$$
  \rho \frac{du}{dt} = \frac{\partial Fu}{\partial \sigma}
$$

     > <span id="u-eq.orig" label="u-eq.orig" label="u-eq.orig">\\centric</span>

$$
  \rho \frac{dv}{dt} = \frac{\partial Fv}{\partial \sigma}
$$


     $u, v$: East-West, North-South Wind;
     $Fu, Fv$: Their vertical flux.

2. thermodynamic equation

$$
  \rho \frac{dc_p T}{dt} = \frac{T}{\theta} \frac{\partial F{\theta}}{\partial \sigma} 
                     + \frac{\partial F{R}}{\partial \sigma} 
$$


     $T$: Temperature ;
     $c_p$: Constant Pressure Specific Heat;
     $\theta=T(p/p_0)^{-R/c_p}=T(p/p_0)^{-\kappa}$: Hot Position;
     $F\theta$: Vertical Sensible Heat Flux;
     $FR$: Vertical Radiation Flux.

 If we write $\theta'=T(p/p_s)^{-\kappa}=T\sigma^{-\kappa}$, then this is

$$
  \rho \frac{dc_p T}{dt} = \sigma^\kappa \frac{\partial F{\theta'}}{\partial \sigma} 
                     + \frac{\partial F{R}}{\partial \sigma} 
$$


 As far as vertical 1D processes are concerned,
 Instead of the     $\theta$, consider the $\theta'$.
 For the sake of simplicity, unless there is a risk of confusion,
 Write     $\theta'$ as $\theta$.

3. water vapor continuity formula

$$
  \rho \frac{dq}{dt} = \frac{\partial Fq}{\partial \sigma} 
$$


     $q$: Specific Humidity;
     $F{q}$: Vertical Steam Flux.

     ### Fundamental Equations in the Ground

 Considered in terms of $z$ coordinates with the downward direction positive.
 After all, all vertical fluxes are positive upward.

4. thermal formula

$$
  \frac{\partial C_g G}{\partial t} = \frac{\partial Fg}{\partial z} + Sg
$$


     $G$: Ground Temperature; $C_g$: Constant Pressure Specific Heat;
     $F{g}$: Vertical Heat Flux;
     $Sg$; Heating term (due to phase change, etc.).

5. formula for ground moisture

$$
  C_w \frac{\partial w}{\partial t} = \frac{\partial Fw}{\partial z} + Sw
$$


     $w$: Ground Moisture;
     $F{w}$: Lead Water Flux;
     $Sw$; Sources of water (spills, etc.).

6. energy balance equation

 At the surface, an energy balance is established.

$$
    F{\theta} + L F{q} + F{R} - F{g} = \Delta s \; \; (\sigma=1, z=0)
$$


     $L$: Latent Heat of Evaporation;
     $\Delta s$: Surface energy balance (due to phase change, etc.).

7. surface water balance

$$
  Pg + Fw - Rg = 0
$$


     $Pg$: Precipitation;
     $Rg$: Surface Runoff.

8. the snow balance

$$
  \frac{\partial Wy}{\partial t} = Py - Fy - My
$$


     $Wy$: Snow cover(kg/m$^2$);
     $Py$: Snowfall;
     $Fy$: Sublimation;
     $My$: Snowmelt.

### Time integration of physical processes.

Classifying physical processes in terms of the time integration of predictor variables,
The order of execution can be divided into the following three categories.

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


by the usual Euler difference.
Large-scale condensation schemes include ,
Note that the updated values are passed on by the cumulus convection scheme.
In practice, the output of the heating rate and so on are used in the routines for cumulus convection and large-scale condensation,
Time integration is done by the immediately following `MODULE:[GDINTG]`.

Radiation in the following groups, vertical diffusion, ground boundary layer and surface processes
calculations are essentially all of these updated values
( $\hat{T}^{t+\Delta t,(1)}, \hat{q}^{t+\Delta t,(2)}$, $\hat{T}^{t+\Delta t,(1)}, \hat{q}^{t+\Delta t,(2)}$, etc. )
This is done by using
However, in order to calculate some of the terms as implicit, the
Calculate all of these terms together and calculate the heating rate, etc,
Finally, we do time integration.
In other words, symbolically,

$$
  \hat{T}^{t+\Delta t,(3)} = \hat{T}^{t+\Delta t,(2)} 
              + 2 \Delta t Q_{RAD,DIF,SFC}
               (\hat{T}^{t+\Delta t,(2)},\hat{T}^{t+\Delta t,(3)})
$$


That would be.

As for gravitational wave resistance, mass regulation and dry convection regulation,
It is similar to cumulus convection and large-scale condensation.

$$
  \hat{T}^{t+\Delta t,(4)} = \hat{T}^{t+\Delta t,(3)} 
              +  2 \Delta t Q_{ADJ}(\hat{T}^{t+\Delta t,(3)})
$$


### Various physical quantities.

A simple calculation from the predictive variables can be used to find
Definitions of various physical quantities.
Some of these are ,
Calculated with `MODULE:[PSETUP]`.

1. temporary temperature

 Provisional Temperature $T_v$ is ,

$$
  T_v = T ( 1 + \epsilon_v q - l )
$$


2. air density

 The atmospheric density, $\rho$, is calculated as follows

$$
  \rho = \frac{p}{RT_v}
$$


3. high degree

 The high degree $z$ is a mechanical process
 The same method is used to calculate the geopotential.

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

 The temperature of the boundary of the layer is determined by the temperature of the $\ln p$, i.e., the temperature of the boundary relative to the $\ln \sigma$
 Perform a linear interpolation and calculate.

$$
  T_{k-1/2} = \frac{\ln \sigma_{k-1} - \ln \sigma_{k-1/2}}
                   {\ln \sigma_{k-1} - \ln \sigma_k      } T_k
            + \frac{\ln \sigma_{k-1/2} - \ln \sigma_k}
                   {\ln \sigma_{k-1} - \ln \sigma_k      } T_{k-1}
$$


5. saturated specific humidity

 Saturation Specific Humidity $q^*(T,p)$
 is approximated using the saturation vapor pressure $e^*(T)$,

$$
q^*(T,p) = \frac{\epsilon e^*(T)}{p} .
$$


 Here, it is $\epsilon=0.622$,

$$
\frac{1}{e^*_v} \frac{\partial e^*_v}{\partial T} = \frac{L}{R_v T^2}
$$

     > <span id="e-sat" label="e-sat">\\blade[e-sat]< /span>

 Therefore, if the latent heat of evaporation ($L$) and the gas constant ($R_v$) of the water vapor are held constant, then the number of vapor particles will be reduced,

$$
  e^*(T) = e^*(T=273{K}) 
                      \exp \left[ \frac{L}{R_v} 
                            \left( \frac{1}{273} - \frac{1}{T} \right)
                       \right] ,
$$


     $e^*(T=273{K}) = 611$ is a \\blank\blank\blank\blank\.com.

     (From [\\\[e-sat\]] (#e-sat)),

$$
\frac{\partial q^*}{\partial T} = \frac{L}{R_v T^2} q^*(T,p) .
$$


 Here, if the temperature is lower than the freezing point 273.15 K
 Use the sublimation latent heat $L+L_M$ as the latent heat $L$.

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

