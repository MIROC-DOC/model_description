## Summary of the mechanics part

Here, we duplicate the previous description,
Enumerate the calculations performed in the mechanical part.

### Summary of calculations in the mechanics part.

The mechanical processes are calculated in the following order.

1. the transformation of horizontal wind into vorticity and divergence `MODULE:[UV2VDG(dvect)]`

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
from the grid point values of vorticity and divergence TERM00002 and TERM00002.
First, the spectra of vorticity and divergence
Ask for TERM00003,TERM00003,

> EQ=00033.  
> <span id="d-summ:uv-zeta" label="d-summ:uv-zeta" label="d-summ:uv-zeta"> </span>
> EQ=00033.

> EQ=00034.  
> <span id="d-summ:uv-D" label="d-summ:uv-D" label="d-summ:uv-D">\[d-summ:uv-D\\[d-summ:uv-D\]</span>.
> EQ=00034.

And more,

> EQ=00000.

and so on.

### Calculating Pseudotemperature

Provisional Temperature TERM00004 is ,

> EQ=00035.

However, it is TERM00005,
TERM00006 is a gas constant for water vapor
(461 TERM00007TERM00008)
TERM00009 is a gas constant of air
(287.04 TERM00010TERM00011)
.

### Calculating the Barometric gradient term

The barometric gradient term TERM00012 is ,
First, we need to get the TERM00013

> EQ=00001.

to a spectral representation and then ,

> EQ=00002.

> EQ=00003.

### Diagnostic calculations of vertical flow.

Barometric pressure change term, and lead DC,

> EQ=00004.

> EQ=00005.

and its non-gravity component.

> EQ=00006.

> EQ=00007.

### The time-varying term due to advection.

Momentum advection term:

> EQ=00036.  
> EQ=00036.

> EQ=00037.  
> EQ=00037.

> EQ=00008.

Temperature Advection Term:

> EQ=00009.

> EQ=00010.

> EQ=00038.  
> EQ=00038.  
> EQ=00038.  
> EQ=00038.  
> EQ=00038.  
> EQ=00038.

Water Vapor Advection Term:

> EQ=00011.

> EQ=00012.

> EQ=00013.

### Conversion of Predictive Variables to Spectra.


([\\\d\[d-summ:uv-D\]](#d-summ:uv-D)) to

TERM00014,TERM00014.
Spectral representation of vorticity and divergence
Convert to TERM00015,TERM00015.
Furthermore ,
Temperature TERM00016, Specific Humidity TERM00017,
TERM00018.

> EQ=00014.

to a spectral representation.

### Conversion of time-varying terms to spectra.

Time Variation Term of Vorticity

> EQ=00039.  
> EQ=00039.  
> EQ=00039.

The non-gravity wave component of the time-varying term of the divergence

> EQ=00040.  
> EQ=00040.  
> EQ=00040.  
> EQ=00040.

The non-gravitational component of the time-varying term of temperature

> EQ=00041.  
> EQ=00041.  
> EQ=00041.

Time-varying terms for water vapor

> EQ=00042.  
> EQ=00042.  
> EQ=00042.

### Spectral Value Time Integration

Equations in matrix form

> EQ=00043.  
> EQ=00043.  
> EQ=00043.  
> EQ=00043.

By using LU decomposition to solve for
Ask for TERM00019,

> EQ=00015.

> EQ=00016.

by.
TERM00020,
TERM00021
and calculate the value of the spectrum in TERM00022 by finding

> EQ=00044.  
> EQ=00044.  
> EQ=00044.  
> EQ=00044.  
> EQ=00044.

### Conversion of Prediction Variables to Grid Values

Spectral values of vorticity and divergence from TERM00023 and TERM00023
Find the grid values for the horizontal wind speed TERM00024,TERM00024.

> EQ=00017.

> EQ=00018.

Furthermore ,

> EQ=00019.

TERM00025,TERM00025 are obtained by such methods as

> EQ=00045.

Calculate the .

### Pseudo etc. TERM00026 Surface Diffusion Correction

Horizontal diffusion is applied on the surface of TERM00027 and so on,
In large areas of mountain slopes, water vapor is transported uphill,
causing problems such as bringing false precipitation at the top of the mountain.
To mitigate it, such as close to the diffusion of the TERM00028 surface
Insert a correction for TERM00029 and TERM00029.

> EQ=00046.  
> EQ=00046.  
> EQ=00046.

so,

> EQ=00020.

And so on.
TERM00030 is equal to the spectral value of TERM00031 in TERM00032
The spectral representation of the diffusion coefficient multiplied by
Converted into a grid value.

### Consideration of frictional heat by diffusion.

Frictional heat from diffusion is ,

> EQ=00021.

It is estimated that
Therefore,

> EQ=00022.

### Correction for conservation of mass.

The spectral method is not used,
The global integration of the TERM00033 is preserved except for rounding errors,
The conservation of the mass, i.e., the global integration of TERM00034, is not guaranteed.
Also, as the spectral wavenumber expires, it is not possible to preserve the global integration of TERM00034,
Negative values of the grid points of water vapor are sometimes observed.
For these reasons,
Let the mass of dry air and water vapor, the mass of cloud water be preserved,
Furthermore, corrections are made to remove the negative water vapor content in the region.

First, at the beginning of the dynamics calculation, `MODULE:[FIXMAS]` is added,
Global integrals of water vapor and cloud water are calculated for TERM00035 and TERM00035.

> EQ=00047.  
> EQ=00047.

In the first step of the calculation, the global integrals of
Calculate and memorize dry mass TERM00036.

> EQ=00048.

At the end of the dynamics calculation, `MODULE:[MASFIX]`,
The correction is performed as follows.

First, for the grid points with negative water vapor content,
    The water vapor is distributed from the grid points directly below,
    Remove negative water vapor.
    If this is TERM00037,

    > EQ=00049.  
    > EQ=00049.

    However, this is only done for TERM00038.

The value is then set to zero for the grid points not removed by the above procedure.

3. calculate the global integration value TERM00039 and
    Make sure this matches the TERM00040,
    Multiply the global water vapor content by a constant percentage.

    > EQ=00023.

4. correcting the dry air mass.
    Similarly, calculate TERM00041 and

    > EQ=00024.

### Horizontal Diffusion and Rayleigh Friction

The coefficients of horizontal diffusion can be expressed spectrally,

> EQ=00025.

> EQ=00026.

> EQ=00027.

The TERM00042 is the Rayleigh coefficient of friction.
The Rayleigh coefficient of friction is

> EQ=00028.

The profile is given as
However,

> EQ=00029.

It is approximated as follows.
Standard values are, TERM00043,
TERM00044 (TERM00045 : the top level of the model),
TERM00046 m,
TERM00047 m. .

### Time Filter.

To remove the computation mode in leap frog
Applying Asselin's (1972) time filter at every step.

> EQ=00030.

and TERM00048 are obtained.
TERM00049, which is used in the next step of the mechanical process, is
Use this TERM00050.
For a TERM00051 it is standard to use 0.05.

In practice, you should use
First, in the `MODULE:[GENGD]` conversion of the predictor to a grid of values, the following variables are used,

> EQ=00031.

and when the physical process is complete, the
After determining the value of TERM00052, you can use `MODULE:[TFILT]` to determine the value of the TERM00052,

> EQ=00032.
