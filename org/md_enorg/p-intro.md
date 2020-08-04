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
Calculate TERM00000, TERM00000 and do time integration.
In addition, in order to evaluate the atmospheric and surface fluxes
Using the surface sub-model.
In the surface sub-model,
Ground Temperature TERM00001, Ground Moisture TERM00002, Snowpack TERM00003, etc.
It is used as a predictor variable.

### Fundamental Equations.

Equation of motion of the atmosphere in the TERM00004 coordinate system, thermodynamic equation,
Consider the equation for a sequence of substances such as water vapor.
The vertical fluxes of momentum, heat, water vapor, etc. are considered,
Find the time variation due to its convergence.
All vertical fluxes are positive upward.

1. equation of motion

         EQ=00000.

         EQ=00001.

     TERM00005,TERM00005: East-West, North-South Wind;
     TERM00006,TERM00006: Their vertical flux.

2. thermodynamic equation

         EQ=00002.

     TERM00007: Temperature ;
     TERM00008: Constant Pressure Specific Heat;
     TERM00009: Hot Position;
     TERM00010: Vertical Sensible Heat Flux;
     TERM00011: Vertical Radiation Flux.

 If we write TERM00012, then this is

         EQ=00003.

 As far as vertical 1D processes are concerned,
 Instead of the     TERM00013, consider the TERM00014.
 For the sake of simplicity, unless there is a risk of confusion,
 Write     TERM00015 as TERM00016.

3. water vapor continuity formula

         EQ=00004.

     TERM00017: Specific Humidity;
     TERM00018: Vertical Steam Flux.

     ### Fundamental Equations in the Ground

 Considered in terms of TERM00019 coordinates with the downward direction positive.
 After all, all vertical fluxes are positive upward.

4. thermal formula

         EQ=00005.

     TERM00020: Ground Temperature; TERM00021: Constant Pressure Specific Heat;
     TERM00022: Vertical Heat Flux;
     TERM00023; Heating term (due to phase change, etc.).

5. formula for ground moisture

         EQ=00006.

     TERM00024: Ground Moisture;
     TERM00025: Lead Water Flux;
     TERM00026; Sources of water (spills, etc.).

6. energy balance equation

 At the surface, an energy balance is established.

         EQ=00007.

     TERM00027: Latent Heat of Evaporation;
     TERM00028: Surface energy balance (due to phase change, etc.).

7. surface water balance

         EQ=00008.

     TERM00029: Precipitation;
     TERM00030: Surface Runoff.

8. the snow balance

         EQ=00009.

     TERM00031: Snow cover(kg/TERM00032);
     TERM00033: Snowfall;
     TERM00034: Sublimation;
     TERM00035: Snowmelt.

### Time integration of physical processes.

Classifying physical processes in terms of the time integration of predictor variables,
The order of execution can be divided into the following three categories.

1. cumulus convection and large-scale condensation

2. radiation, vertical diffusion, ground boundary layer and surface processes

3. gravitational wave resistance, mass regulation, dry convection regulation

Cumulus convection and large-scale condensation,

     EQ=00010.

     EQ=00011.

by the usual Euler difference.
Large-scale condensation schemes include ,
Note that the updated values are passed on by the cumulus convection scheme.
In practice, the output of the heating rate and so on are used in the routines for cumulus convection and large-scale condensation,
Time integration is done by the immediately following `MODULE:[GDINTG]`.

Radiation in the following groups, vertical diffusion, ground boundary layer and surface processes
calculations are essentially all of these updated values
( TERM00036, TERM00036, etc. )
This is done by using
However, in order to calculate some of the terms as implicit, the
Calculate all of these terms together and calculate the heating rate, etc,
Finally, we do time integration.
In other words, symbolically,

     EQ=00012.

That would be.

As for gravitational wave resistance, mass regulation and dry convection regulation,
It is similar to cumulus convection and large-scale condensation.

     EQ=00013.

### Various physical quantities.

A simple calculation from the predictive variables can be used to find
Definitions of various physical quantities.
Some of these are ,
Calculated with `MODULE:[PSETUP]`.

1. temporary temperature

 Provisional Temperature TERM00037 is ,

         EQ=00014.

2. air density

 The atmospheric density, TERM00038, is calculated as follows

         EQ=00015.

3. high degree

 The high degree TERM00039 is a mechanical process
 The same method is used to calculate the geopotential.

         EQ=00016.

         EQ=00017.

         EQ=00018.

4. layer boundary temperature

 The temperature of the boundary of the layer is determined by the temperature of the TERM00040, i.e., the temperature of the boundary relative to the TERM00041
 Do a linear interpolation and calculate.

         EQ=00019.

5. saturated specific humidity

 Saturation Specific Humidity TERM00042,TERM00042
 is approximated using the saturation vapor pressure TERM00043,

         EQ=00020.

 Here, it is TERM00044,

         EQ=00021.

 Therefore, if the latent heat of evaporation (TERM00045) and the gas constant (TERM00046) of the water vapor are held constant, then the number of vapor particles will be reduced,

         EQ=00022.

     TERM00047 is a \\blank\blank\blank\blank\.com.

     (22) From ,

         EQ=00023.

 Here, if the temperature is lower than the freezing point 273.15 K
 Use the sublimation latent heat TERM00049 as the latent heat TERM00048.

6. dry static energy, wet static energy

 Dry static energy TERM00050 is

         EQ=00024.

 Wet Static Energy TERM00051 is

         EQ=00025.

 . defined by .