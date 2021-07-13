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

We compute the time-varying terms TERM00436 and TERM00436 for the forecast variables from these processes, and perform time integration. In order to evaluate the atmospheric and surface fluxes, the ground surface sub-model is used. The ground surface sub-model uses such predictors as the ground temperature (TERM00437), ground moisture (TERM00438), and snow cover (TERM00439) as predictor variables.

### Fundamental Equations.

Considering the equation of motion of the atmosphere in TERM00440 coordinate system, thermodynamic equations, and equations for continuity of materials such as water vapor etc. Considering the vertical fluxes of momentum, heat, water vapor, etc., the time variation of the fluxes is determined by their convergence. All the vertical fluxes are assumed to be positive for the upward direction.

1. equation of motion

         EQ=00157.

         EQ=00158.

     TERM00441,TERM00441: East-West, North-South Wind; TERM00442,TERM00442: Their Vertical Flux.

2. thermodynamic equation

         EQ=00159.

     TERM00443: Temperature; TERM00444: Constant Pressure Specific Heat; TERM00445: Temperature Level; TERM00446: Vertical Sensible Heat Flux; TERM00447: Vertical Radiation Flux.

 Here, with TERM00448, this is,

         EQ=00160.

 As far as one-dimensional vertical processes are concerned, instead of TERM00449, we can consider TERM00450. For simplicity, unless there is a risk of confusion, TERM00451 should be written as TERM00452 below.

3. water vapor continuity formula

         EQ=00161.

     TERM00453: Specific Humidity; TERM00454: Vertical Water Vapor Flux.

     ### Fundamental Equations in the Ground

 Consider the TERM00455 coordinates with the downward direction positive. As expected, the vertical fluxes are all positive in the upward direction.

4. thermal formula

         EQ=00162.

     TERM00456: Ground Temperature; TERM00457: Constant Pressure Specific Heat; TERM00458: Vertical Heat Flux; TERM00459; Heating Term (due to phase change etc.).

5. formula for ground moisture

         EQ=00163.

     TERM00460: Ground moisture; TERM00461: Vertical water flux; TERM00462; Water sources (e.g., runoff).

6. energy balance equation

 At the surface, an energy balance is established.

         EQ=00164.

     TERM00463: Latent heat of evaporation; TERM00464: Surface energy balance (associated with phase change, etc.).

7. surface water balance

         EQ=00165.

     TERM00465: Precipitation; TERM00466: Surface Runoff.

8. the snow balance

         EQ=00166.

     TERM00467: Snow cover (kg/TERM00468); TERM00469: Snowfall; TERM00470: Sublimation; TERM00471: Snowmelt.

### Time integration of physical processes.

In terms of time integration of predictors, we can classify the physical processes in the following three orders of execution.

1. cumulus convection and large-scale condensation

2. radiation, vertical diffusion, ground boundary layer and surface processes

3. gravitational wave resistance, mass regulation, dry convection regulation

Cumulus convection and large-scale condensation,

     EQ=00167.

     EQ=00168.

where the values are updated by the usual Euler difference Note that the large-scale condensation scheme is updated by the cumulus convection scheme. In practice, the routines of cumulus convection and large-scale condensation output the heating rates and so on, and the time integration is performed immediately afterwards by `MODULE:[GDINTG]`.

The calculations of the radiative, vertical diffusion, ground boundary layer and surface processes in the following groups are basically performed with these updated values (TERM00472, TERM00472, etc.). However, in order to calculate some of the terms as implicit, we calculate the heating rates and so on for all of these terms together, and then perform time integration at the end. In other words, if we write symbolically

     EQ=00169.

That would be.

The gravitational wave resistance, mass modulation, and dry convection modulation are the same as those for cumulus convection and large-scale condensation.

     EQ=00170.

### Various physical quantities.

Here are definitions of various geophysical quantities that can be computed simply from the predictors. Some of them are calculated with `MODULE:[PSETUP]`.

1. temporary temperature

 Provisional Temperature TERM00473 is ,

         EQ=00171.

2. air density

 The atmospheric density TERM00474 is calculated as follows

         EQ=00172.

3. high degree

 The altitude TERM00475 is evaluated in the same way as the calculation of the geopotential for mechanical processes.

         EQ=00173.

         EQ=00174.

         EQ=00175.

4. layer boundary temperature

 The temperature at the boundary of the layer is calculated by performing a linear interpolation on TERM00476, i.e., TERM00477.

         EQ=00176.

5. saturated specific humidity

 The saturated specific humidity TERM00478 and TERM00478 are approximated using the saturated vapor pressure TERM00479,

         EQ=00177.

 Here, it is TERM00480,

         EQ=00178.

 Therefore, if the latent heat of evaporation (TERM00481) and the gas constant of water vapor (TERM00482) are held constant, the number of vaporized materials will be reduced,

         EQ=00179.

     .....

     (199) from ,

         EQ=00180.

 Here, if the temperature is lower than the freezing point 273.15K, the sublimation latent heat TERM00485 is used as the latent heat TERM00484.

6. dry static energy, wet static energy

 Dry static energy TERM00486 is

         EQ=00181.

 Wet Static Energy TERM00487 is

         EQ=00182.

 . defined by .