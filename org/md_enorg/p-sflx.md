## Surface Flux.

### Overview of the Surface Flux Scheme

The surface flux scheme is ,
due to turbulent transport in the ground boundary layer.
Assessing the flux of physical quantities between atmospheric surfaces.
The main input data are wind speed TERM00000, TERM00000, and temperature TERM00001, Specific humidity is the TERM00002,
The output data are the vertical fluxes of momentum, heat, water vapor and
It is the differential value for obtaining an implicit solution.

Bulk coefficients are obtained according to Louis(1979), Louis <span>*et al.*& lt;/span>(1982).
However, we take into account the difference between the momentum and heat roughness in the correction.

The outline of the calculation procedure is as follows.

1. as the stability of the atmosphere.
     Richardson numbers.

2. calculate the bulk coefficient from Richardson number `MODULE:[PSFCL]`.

3. calculate the flux and its derivative from the bulk coefficient.

4. if necessary, using the required flux
 After taking into account the roughness effect of sea level, the effect of free convection, and wind speed correction,
 Do the math again.

### Basic Formula for Flux Calculations

Surface Flux TERM00003 and TERM00003 are
Using the bulk coefficients TERM00004 and TERM00004
It is expressed as follows.

> EQ=00000.

> EQ=00001.

> EQ=00002.

> EQ=00003.

However, the TERM00005 is the amount of possible evaporation.
The calculation of actual evaporation is a combination of "surface processes" and
We will discuss this in the section "Solving Diffusion-Based Budget Equations for Atmospheric Surface Systems".

### Richardson Number.

The standard of stability between atmospheric surfaces,
Bulk Richardson number TERM00006 is

> EQ=00004.

Here,

> EQ=00005.

is a correction factor and is approximated from the uncorrected bulk Richardson number, while
Here, the calculation method is abbreviated.

### Bulk factor.

The bulk coefficients TERM00007 and TERM00007 are
Louis(1979), Louis <span>*et al.*</span span>(1982).
However, we take into account the difference between the momentum and heat roughness in the correction.
i.e., the roughness to momentum, heat, and water vapor.
TERM00008 and TERM00008 respectively
In general, it is TERM00009 and TERM00009, but heat and water vapor are also
Bulk factor for flux from the height of the TERM00010
First find the TERM00011 and TERM00012 and then correct them.

> EQ=00006.

> EQ=00007.

> EQ=00008.

> EQ=00009.

> EQ=00010.

The TERM00013 and TERM00013 are
The bulk coefficient (for fluxes from TERM00014) at neutral,

> EQ=00011.

Correction Factor TERM00015 is ,

> EQ=00012.

but the method of calculation is abbreviated.
The coefficient is TERM00016,TERM00016.

The dependence of the bulk coefficients on TERM00017 is illustrated in Fig,
Figure [p-sflx:cm\]] (#p-sflx:cm), Figure [p-sflx:ch [\\\\]](#p-sflx:ch), Figure [p-sflx:ch](#p-sflx:ch).

### Calculating Flux.

This will calculate the flux.

> EQ=00013.

> EQ=00014.

> EQ=00015.

> EQ=00016.

The differential term is as follows

> EQ=00017.

> EQ=00018.

> EQ=00019.

> EQ=00020.

> EQ=00021.

Here, it's important to note,
TERM00019 is a quantity that is not required at this time.
Epidermal temperature is ,
Conditions for surface heat balance

> EQ=00022.

Determined to meet.
At this point, for TERM00020, we use the one from the previous time step for evaluation.
The true flux value that meets the surface balance is ,
It is determined by solving this equation in conjunction with surface processes.
In that sense, I have added TERM00021 to the flux above.

### handling at sea level.

At sea level, we follow Miller et al. (1992) and consider the following two effects.

 - Free convection is preeminent when the wind speed is low

 - The roughness of the sea surface varies with the wind speed.

The effect of free convection is calculated using the buoyancy flux TERM00022,

> EQ=00023.

When I was in TERM00023,

> EQ=00024.

> EQ=00025.

to be considered by making TERM00024 corresponds to the thickness scale of the mixing layer.
The current standard value is TERM00025 m.

The roughness variation of the sea surface is represented by the friction velocity TERM00026

> EQ=00026.

with ,

> EQ=00027.
> EQ=00027.
> EQ=00027.

Evaluate as follows. TERM00027 TERM00028 TERM00029 is
It is the kinematic viscosity of the atmosphere,
The standard values for the other coefficients are
TERM00030,TERM00030,
TERM00031,TERM00031,
TERM00032,TERM00032.

For the above calculations, TERM00033 and TERM00033 are required,
Perform successive approximation calculations.

### Wind Speed Correction

In general, the roughness of the ground surface is greater on large surfaces than on small surfaces.
The downward transport of momentum is so efficient that the wind just above it is weak,
The difference in wind speed cancels out the difference in roughness in TERM00034.

In the model, the wind speed passed to the surface flux calculation is
It is a value calculated by time integration of the mechanical processes,
The values are smoothed by spectral expansion.
This is the reason why the surface of the ground with widely different roughnesses, such as sea level and land level, is
In an area that is mixed on a small scale ,
I can't describe this compensation effect well.
Therefore, once the momentum flux is calculated and
The wind speed in the lowest layer of the atmosphere is corrected for by it, and then
Recalculate the momentum, heat, and water fluxes again.

### Minimum wind speed.

Consider the effects of small-scale exercise,
Surface wind speed in the calculation of surface flux
Set the minimum value of TERM00035.
The current standard values are the same for all fluxes and
It is 3 m/s.
