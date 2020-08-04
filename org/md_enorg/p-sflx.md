## Surface Flux.

### Overview of the Surface Flux Scheme

The surface flux scheme is ,
due to turbulent transport in the ground boundary layer.
Assessing the flux of physical quantities between atmospheric surfaces.
The main input data are wind speed TERM00000, TERM00000, temperature TERM00001, and specific humidity TERM00002,
The output data are the vertical fluxes of momentum, heat, water vapor and
It is the differential value for obtaining an implicit solution.

Bulk coefficients are obtained according to Louis(1979), Louis <span>*et al.*</span>(1982).
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

     EQ=00000.

     EQ=00001.

     EQ=00002.

     EQ=00003.

However, the TERM00009 is the possible evaporation rate.
The calculation of actual evaporation is a combination of "surface processes" and
We will discuss this in the section "Solving Diffusion-Based Budget Equations for Atmospheric Surface Systems".

### Richardson Number.

The standard of stability between atmospheric surfaces,
Bulk Richardson Number TERM00010 is

     EQ=00004.

Here,

     EQ=00005.

is a correction factor and is approximated from the uncorrected bulk Richardson number, while
Here, the calculation method is abbreviated.

### Bulk factor.

The bulk coefficients TERM00011,TERM00011 are
Louis(1979), Louis <span>*et al.*</span>(1982).
However, we take into account the difference between the momentum and heat roughness in the correction.
i.e., the roughness to momentum, heat, and water vapor.
TERM00012 and TERM00012 respectively
In general, the TERM00013 and TERM00013 are used, but heat and water vapor are also
Bulk factor for flux from the height of the TERM00014
Find first the TERM00015 and TERM00016 and then correct them.

     EQ=00006.

     EQ=00007.

     EQ=00008.

     EQ=00009.

     EQ=00010.

TERM00017 and TERM00017 are
The bulk factor (for fluxes from TERM00018) at neutral,

     EQ=00011.

Correction Factor TERM00019 is ,

     EQ=00012.

but the method of calculation is abbreviated.
The coefficients are TERM00020 and TERM00020.

The dependence of the bulk coefficient on the TERM00021 is illustrated in Fig,
Figure [p-sflx:cm\] (#p-sflx:cm), Figure [p-sflx:ch\] (#p-sflx:ch).

### Calculating Flux.

This will calculate the flux.

     EQ=00013.

     EQ=00014.

     EQ=00015.

     EQ=00016.

The differential term is as follows

     EQ=00017.

     EQ=00018.

     EQ=00019.

     EQ=00020.

     EQ=00021.

Here, it's important to note,
TERM00032 is a quantity that is not required at this time.
Epidermal temperature is ,
Conditions for surface heat balance

     EQ=00022.

Determined to meet.
At this point, for TERM00033, we use the one from the previous time step to evaluate.
The true flux value that meets the surface balance is ,
It is determined by solving this equation in conjunction with surface processes.
In that sense, I have added TERM00034 to the flux above.

### handling at sea level.

At sea level, we follow Miller et al. (1992) and consider the following two effects.

 - Free convection is preeminent when the wind speed is low

 - The roughness of the sea surface varies with the wind speed.

The effect of free convection is calculated using the buoyancy flux TERM00035,

     EQ=00023.

During the TERM00036,

     EQ=00024.

     EQ=00025.

to be considered by making TERM00038 corresponds to the thickness scale of the mixed layer.
The current standard value is TERM00039 m.

The roughness variation of the sea surface is represented by the friction velocity (TERM00040)

     EQ=00026.

with ,

     EQ=00027.
     EQ=00027.
     EQ=00027.

Evaluate as follows. TERM00041 TERM00042 TERM00043 is
It is the kinematic viscosity of the atmosphere,
The standard values for the other coefficients are
TERM00044,TERM00044,
TERM00045,TERM00045,
TERM00046,TERM00046.

For the above calculations, TERM00047 and TERM00047 are required,
Perform successive approximation calculations.

### Wind Speed Correction

In general, the roughness of the ground surface is greater on large surfaces than on small surfaces.
The downward transport of momentum is so efficient that the wind just above it is weak,
The difference in wind speed cancels out the difference in roughness in TERM00048.

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
Set the minimum value of TERM00049.
The current standard values are the same for all fluxes and
It is 3 m/s.