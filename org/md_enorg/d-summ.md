## Summary of the mechanics part

Here, we duplicate the previous description,
Enumerate the calculations performed in the Mechanical Process Department.

### Summary of Calculations for the Mechanics Portion

The mechanical processes are calculated in the following order.

1. converting horizontal wind into vorticity and divergence `MODULE:[UV2VDG(dvect)]`

2. calculation of pseudotemperature `MODULE:[VIRTMD(dvtmp)]`

3. calculation of the barometric gradient term `MODULE:[HGRAD(dvect)]`

4. diagnostic calculation of vertical flow `MODULE:[GRDDYN/PSDOT(dgdyn)]`

5. time change term due to advection `MODULE:[GRDDYN(dgdyn)]`

6. convert the predictive variable to a spectrum `MODULE:[GD2WD(dg2wd)]`

7. convert the time-varying term into a spectrum `MODULE:[TENG2W(dg2wd)]`

8. time integration of spectral values `MODULE:[TINTGR(dintg)]`

9. convert the predictive variables to grid values `MODULE:[GENGD(dgeng)]`

10. pseudo etc. TERM00000 plane spreading correction `MODULE:[CORDIF(ddifc)]`

11. consideration of frictional heat by diffusion `MODULE:[CORFRC(ddifc)]`

12. correction for conservation of mass `MODULE:[MASFIX(dmfix)]`

13. (physical process) `MODULE:[PHYSCS(padmn)]`

14. (time filter) `MODULE:[TFILT(aadvn)]`

### Conversion of Horizontal Wind to Vorticity and Divergence

Grid point values for horizontal wind TERM00001,TERM00001
from the grid values of vorticity and divergence TERM00002 and TERM00002.
First, the spectra of vorticity and divergence
Ask for TERM00003,TERM00003,

     EQ=00033.
     EQ=00033.

     EQ=00034.
     EQ=00034.

I'll take that further,

     EQ=00000.

and so on.

### Calculating a Provisional Temperature

Provisional Temperature TERM00005 is ,

     EQ=00035.

However, it is TERM00006,
TERM00007 is a gas constant for water vapor
(461 TERM00008TERM00009)
TERM00010 is a gas constant of air
(287.04 TERM00011TERM00012)
It is.

### Calculating the Barometric gradient term

The barometric gradient term TERM00013 is ,
First, we need to get the TERM00014

     EQ=00001.

to a spectral representation and then ,

     EQ=00002.

     EQ=00003.

### Diagnostic calculations of vertical flow.

Barometric pressure change term, and lead DC,

     EQ=00004.

     EQ=00005.

and its non-gravity components.

     EQ=00006.

     EQ=00007.

### Time change term due to advection.

Momentum advection term:

     EQ=00036.
     EQ=00036.

     EQ=00037.
     EQ=00037.

     EQ=00008.

Temperature advection term:

     EQ=00009.

     EQ=00010.

     EQ=00038.
     EQ=00038.
     EQ=00038.
     EQ=00038.
     EQ=00038.
     EQ=00038.

Water vapor advection term:

     EQ=00011.

     EQ=00012.

     EQ=00013.

### Conversion of Predictive Variables into Spectra

(1) and
(2).

TERM00024,TERM00024
Spectral representation of vorticity and divergence
Convert to TERM00025,TERM00025.
Furthermore,
Temperature TERM00026, Specific Humidity TERM00027,
TERM00028.

     EQ=00014.

to a spectral representation.

### Conversion of time-varying terms to spectra

Time Variation Term of Vorticity

     EQ=00039.
     EQ=00039.
     EQ=00039.

The non-gravity wave component of the time-varying term of the divergence

     EQ=00040.
     EQ=00040.
     EQ=00040.
     EQ=00040.

The non-gravity wave component of the time-varying term of temperature

     EQ=00041.
     EQ=00041.
     EQ=00041.

Time-varying term of water vapor

     EQ=00042.
     EQ=00042.
     EQ=00042.

### Spectral value time integration

Equations in matrix form

     EQ=00043.
     EQ=00043.
     EQ=00043.
     EQ=00043.

by using LU decomposition to solve for
Ask for TERM00038,

     EQ=00015.

     EQ=00016.

due to
TERM00044,
TERM00045
and calculate the value of the spectrum in TERM00046.

     EQ=00044.
     EQ=00044.
     EQ=00044.
     EQ=00044.
     EQ=00044.

### Conversion of Predictive Variables to Grid Values

Spectral values of vorticity and divergence from TERM00047 and TERM00047
Find the horizontal wind speed grid values TERM00048 and TERM00048.

     EQ=00017.

     EQ=00018.

Furthermore,

     EQ=00019.

TERM00052 and TERM00052 are obtained by such methods as

     EQ=00045.

to calculate.

### Pseudo etc. TERM00053 Surface Diffusion Correction

Horizontal diffusion is applied on the TERM00054 surface and so on,
In large areas of mountain slopes, water vapor is transported uphill,
Causing problems such as bringing false precipitation at the top of the mountain.
To mitigate that, etc. TERM00055 close to the diffusion of the surface
Insert corrections for TERM00056 and TERM00056.

     EQ=00046.
     EQ=00046.
     EQ=00046.

So,

     EQ=00020.

And so on.
TERM00057 has been replaced by the spectral value of TERM00058, TERM00059
The spectral representation of the diffusion coefficient multiplied by
It is used to convert to a grid value.

### Consideration of frictional heat from diffusion

Frictional heat from diffusion is ,

     EQ=00021.

It is estimated that .
Therefore,

     EQ=00022.

### Correction for conservation of mass

The spectral method is not used,
The global integration of the TERM00060 is preserved except for rounding errors,
The conservation of the mass, i.e. the global integration of TERM00061, is not guaranteed.
Also, with the expiration of the spectral wavenumber, the
Negative values of the grid points of water vapor are sometimes observed.
For these reasons ,
Let the mass of dry air and water vapor, the mass of cloud water be preserved,
In addition, corrections are made to remove areas with negative water vapor content.

First, at the beginning of the mechanics calculation, `MODULE:[FIXMAS]`,
Calculate the global integral of each component of water vapor and cloud water, TERM00062 and TERM00062.

     EQ=00047.
     EQ=00047.

Also, in the first step of the calculation
Calculate and memorize the dry mass TERM00063.

     EQ=00048.

At the end of the dynamics calculation, `MODULE:[MASFIX]`,
The following procedure is used to make the correction.

First, we discuss the grid points with negative water vapor content,
 The water vapor is distributed from the grid points directly below,
 Remove the negative water vapor.
 If this is     TERM00064,

         EQ=00049.
         EQ=00049.

 However, this should only be done if it is TERM00065.

Next, set the value to zero for the grid points not removed by the above procedure.

3. calculate the global integration value TERM00066,
 Make sure this is consistent with TERM00067,
 Multiply the global water vapor content by a certain percentage.

         EQ=00023.

4. perform dry air mass correction.
 Similarly, calculate the TERM00068,

         EQ=00024.

### Horizontal Diffusion and Rayleigh Friction

The coefficients of horizontal diffusion can be expressed spectrally,

     EQ=00025.

     EQ=00026.

     EQ=00027.

The TERM00069 is the Rayleigh coefficient of friction.
The Rayleigh coefficient of friction is

     EQ=00028.

given in profiles like
However,

     EQ=00029.

Approximate to .
Standard value is, TERM00070,
TERM00071 (TERM00072 : top level of the model),
TERM00073 m,
TERM00074 m.

### Time Filter.

To remove the computation mode in leap frog
Apply the time filter of Asselin (1972) at every step.

     EQ=00030.

and TERM00075.
The TERM00076 used in the next step of the mechanical process is
Using this TERM00077.
For a TERM00078, the standard value of 0.05 should be used.

In fact.
First, in the `MODULE:[GENGD]` conversion of the predictor to a grid of values, the following variables are used,

     EQ=00031.

and when the physical process is done
After fixing the value of TERM00079, you can use `MODULE:[TFILT]` to determine the value of TERM00079,

     EQ=00032.

.