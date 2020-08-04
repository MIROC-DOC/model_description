## Vertical Diffusion.

### Vertical Diffusion Scheme Overview.

The vertical diffusion scheme,
due to sub-grid scale turbulent diffusion.
Evaluating the vertical flux of physical quantities.
The main input data are wind speed, TERM00000, TERM00000, temperature TERM00001, specific humidity TERM00002, and cloud cover TERM00003,
The output data are the vertical fluxes of momentum, heat, water vapor, cloud water and
It is the differential value for obtaining an implicit solution.

To estimate the vertical diffusion coefficient, the
Mellor and Yamada (1974, 1982).
The turbulent closure model.
Using level 2 parameterization.

The outline of the calculation procedure is as follows.

1. as the stability of the atmosphere.
     Richardson numbers.

2. calculate the diffusion coefficient from Richardson number `MODULE:[VDFCOF]`.

3. calculate the flux and its derivative from the diffusion coefficient.

### Basic Formula for Flux Calculations

The vertical diffuse flux in the atmosphere is ,
Using the diffusion coefficient TERM00004, it is evaluated as follows.

     EQ=00000.

     EQ=00001.

     EQ=00002.

     EQ=00003.

### Richardson Number.

The standard for atmospheric stratospheric stability,
Bulk Richardson number TERM00005 is

     EQ=00004.

. defined by .
Here, TERM00006 represents TERM00007.
The TERM00008 is based on the hydrostatic pressure equation,

     EQ=00005.

The flux Ricahrdson number TERM00009 is ,

     EQ=00006.

However,

     EQ=00020.
     EQ=00020.
     EQ=00020.
     EQ=00020.
     EQ=00020.
     EQ=00020.

     EQ=00007.

     EQ=00008.

The relationship between the TERM00010 and the TERM00011 is illustrated in this figure,
Figure [p-dif:rib-rif\]] (#p-dif:rib-rif).

### Diffusion Coefficient.

The diffusion coefficient is ,
For each layer boundary (TERM00012 level) ,
It is given as follows.

     EQ=00021.
     EQ=00021.

Here, TERM00015 and TERM00015 are,

     EQ=00009.

     EQ=00010.

with ,

     EQ=00022.
     EQ=00022.

TERM00016 is a mixing distance, according to Blakadar (1962),

     EQ=00011.

Take.
TERM00017 is a Kárman constant.
The current standard value is TERM00018 m.

If TERM00019 and TERM00019 are shown as functions of TERM00020,
Figure [p-dif:smsh-rif\]] (#p-dif:smsh-rif).

### Calculating Flux.

Using the above, we calculate the fluxes and flux derivatives.

     EQ=00012.

     EQ=00013.

     EQ=00014.

     EQ=00015.

     EQ=00016.

     EQ=00017.

     EQ=00018.

     EQ=00019.

### Minimum Diffusion Coefficient.

In the very stable case, the above estimate gives zero as the diffusion coefficient.
As it is, the model's behavior can be modified in various ways
Set a suitable minimum value as it will have a negative effect.
The current standard values are the same for all fluxes and
TERM00022 0.15 TERM00023/s

### Other Notes.

I'm calling the shallow cumulus convection `MODULE:[SHLCOF]`,
By default, this is a dummy.