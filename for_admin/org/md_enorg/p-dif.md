## Vertical Diffusion.

### Vertical Diffusion Scheme Overview.

The vertical diffusion scheme evaluates the vertical flux of physical quantities due to sub-grid scale turbulent diffusion. The main input data are wind speed, TERM00826, TERM00826, air temperature, TERM00827, specific humidity, TERM00828, and cloud water, TERM00829, and the output data are the vertical fluxes of momentum, heat, water vapor, and cloud water, as well as the derivative values for obtaining the implicit solution.

The vertical diffusion coefficients are estimated using the level 2 parameterization of the Mellor and Yamada (1974, 1982) turbulent flow closure model.

The outline of the calculation procedure is as follows.

Calculate the Richardson number as the stability of the atmosphere.

2. calculate the diffusion coefficient from Richardson number `MODULE:[VDFCOF]`.

3. calculate the flux and its derivative from the diffusion coefficient.

### Basic Formula for Flux Calculations

The vertical diffuse flux in the atmosphere is evaluated by using the diffusion coefficient TERM00830 as follows

     EQ=00305.

     EQ=00306.

     EQ=00307.

     EQ=00308.

### Richardson Number.

The bulk Richardson number (TERM00831), which is the benchmark for atmospheric stratification stability, is

     EQ=00309.

defined by Here, TERM00832 represents TERM00833. Also, TERM00834 is defined by the hydrostatic pressure equation,

     EQ=00310.

Flux Ricahrdson number TERM00835 is ,

     EQ=00311.

However,

     EQ=00325.
     EQ=00325.
     EQ=00325.
     EQ=00325.
     EQ=00325.
     EQ=00325.

     EQ=00312.

     EQ=00313.

The relationship between TERM00836 and TERM00837 is illustrated in the figure[#p-dif:rib-rif]](#p-dif:rib-rif).

### Diffusion Coefficient.

The diffusion coefficients are given for each layer boundary (TERM00838 level) as follows.

     EQ=00326.
     EQ=00326.

Here, TERM00841 and TERM00841 are

     EQ=00314.

     EQ=00315.

with ,

     EQ=00327.
     EQ=00327.

TERM00842 is a mixing distance, according to Blakadar (1962),

     EQ=00316.

Take the following. TERM00843 is the Kárman constant. The current standard value is TERM00844 m.



### Calculating Flux.

Using the above, we calculate the fluxes and flux derivatives.

     EQ=00317.

     EQ=00318.

     EQ=00319.

     EQ=00320.

     EQ=00321.

     EQ=00322.

     EQ=00323.

     EQ=00324.

### Minimum Diffusion Coefficient.

In the very stable case, the above estimate gives zero as the diffusion coefficient. If this value is used as it is, various adverse effects on the behavior of the model are observed. The current standard value is TERM00848 0.15 TERM00849/s, which is common to all fluxes.

### Other Notes.

We call shallow cumulus convection `MODULE:[SHLCOF]`, which is a dummy by default.