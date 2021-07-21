## Surface Flux.

### Overview of the Surface Flux Scheme

The surface flux scheme evaluates the physical quantity fluxes between the atmospheric surfaces due to turbulent transport in the boundary layer. The main input data are wind speed (TERM00850), temperature (TERM00850), temperature (TERM00851), and specific humidity (TERM00852), and the output data are the vertical fluxes of momentum, heat, and water vapor as well as the differential values for obtaining implicit solutions.

The bulk coefficients are obtained according to Louis(1979) and Louis <span>*et al.*</span>(1982), except for the correction for the difference in roughness between momentum and heat. However, corrections are made to take into account the difference between momentum and heat roughness.

The outline of the calculation procedure is as follows.

Calculate the Richardson number as the stability of the atmosphere.

2. calculate the bulk coefficient from Richardson number `MODULE:[PSFCL]`.

3. calculate the flux and its derivative from the bulk coefficient.

If necessary, the calculated fluxes are re-calculated after taking into account the roughness effect, the free flow effect, and the wind speed correction.

### Basic Formula for Flux Calculations

Surface fluxes (TERM00853 and TERM00853) are expressed using the bulk coefficients (TERM00854 and TERM00854) as follows

     EQ=00328.

     EQ=00329.

     EQ=00330.

     EQ=00331.

Note that TERM00859 is the possible evaporation rate. The calculation of actual evaporation is described in the sections "Surface processes" and "Solution of diffuse-type balance equations for atmospheric surface systems".

### Richardson Number.

The bulk Richardson number (TERM00860), which is used as a benchmark for the stability between the atmospheric surfaces, is

     EQ=00332.

Here,

     EQ=00333.

is a correction factor, which is approximated from the uncorrected bulk Richardson number, but we abbreviate the calculation here.

### Bulk factor.

The bulk coefficients of TERM00861 and TERM00861 are calculated according to Louis (1979) and Louis <span>*et al.*</span> (1982). However, corrections are made to take into account the difference between momentum and heat roughness. If the roughnesses for momentum, heat, and water vapor are set to TERM00862 and TERM00862, respectively, the results are generally TERM00863 and TERM00863, but the bulk coefficients for heat and water vapor for the fluxes from the height of TERM00864 are also set to TERM00865, TERM 00866 first, and then corrected.

     EQ=00334.

     EQ=00335.

     EQ=00336.

     EQ=00337.

     EQ=00338.

TERM00867,TERM00867 is the bulk coefficient (for fluxes from TERM00868) at neutral,

     EQ=00339.

Correction Factor TERM00869 is ,

     EQ=00340.

but the method of calculation is omitted. The coefficients are TERM00870 and TERM00870.

The dependence of the bulk coefficient on the TERM00871 is illustrated in Figure [\brachio[p-sflx:cm\]] (#p-sflx:cm) and Figure [\brachio[p-sflx:ch\c\]] (#p-sflx:ch).

### Calculating Flux.

This will calculate the flux.

     EQ=00341.

     EQ=00342.

     EQ=00343.

     EQ=00344.

The differential term is as follows

     EQ=00345.

     EQ=00346.

     EQ=00347.

     EQ=00348.

     EQ=00349.

Here, it is important to note that TERM00882 is a quantity that is not required at this point in time. The surface temperature is the condition of the surface heat balance

     EQ=00350.

is determined to satisfy. At this point, TERM00883 evaluates the fluxes in the previous time step. The true value of the flux that satisfies the surface balance is determined by solving this equation in conjunction with surface processes. In this sense, we have marked the above fluxes with TERM00884.

### handling at sea level.

At sea level, we follow Miller et al. (1992) and consider the following two effects.

 - Free convection is preeminent when the wind speed is low

 - The roughness of the sea surface varies with the wind speed.

The effect of free convective motion is estimated by calculating the buoyancy flux TERM00885,

     EQ=00351.

When it was TERM00886,

     EQ=00352.

     EQ=00353.

The TERM00888 corresponds to the mixed layer thickness scale. TERM00888 corresponds to the thickness scale of the mixing layer. The current standard value is TERM00889 m.

The roughness variation of the sea surface is determined by the friction velocity (TERM00890)

     EQ=00354.

with ,

     EQ=00355.
     EQ=00355.
     EQ=00355.

The evaluation is performed as follows. TERM00891 TERM00892 TERM00893 is the kinematic viscosity coefficient of the atmosphere and the other standard values of the coefficients are TERM00894, TERM00894, TERM00895, TERM00895, TERM00896 and TERM00896.

In the above calculations, we perform successive approximation calculations because TERM00897 and TERM00897 are required.

### Wind Speed Correction

In general, the downward transport of momentum is more efficient on a large rough surface than on a small rough surface, which results in a weaker wind over the surface, and the difference in wind speed can cancel out the difference in TERM00898 due to the difference in roughness.

In the model, the wind speed passed to the surface flux calculation is the value calculated by the time integration of the dynamic process and smoothed by the spectral expansion. Therefore, this compensation effect cannot be well represented in a region where the land and sea surfaces with widely different roughnesses coexist at small scales, for example, where the sea surface and the land surface. The momentum fluxes are calculated once, and then the wind speed in the lowermost layer of the atmosphere is corrected by the fluxes and the momentum, heat and water fluxes are recalculated once again.

### Minimum wind speed.

The minimum value of the surface wind speed (TERM00899) for calculating the surface fluxes is set to take into account the effects of small-scale motions. The current standard value is 3m/s, which is common to all fluxes.