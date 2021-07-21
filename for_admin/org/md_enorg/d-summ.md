## Summary of the mechanics part

In this section, we enumerate the calculations performed in the Mechanical Engineering Department, although they overlap with the previous descriptions.

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

10. pseudo etc. TERM00356 surface diffusion correction `MODULE:[CORDIF(ddifc)]`

11. consideration of frictional heat by diffusion `MODULE:[CORFRC(ddifc)]`

12. correction for conservation of mass `MODULE:[MASFIX(dmfix)]`

13. (physical process) `MODULE:[PHYSCS(padmn)]`

14. (time filter) `MODULE:[TFILT(aadvn)]`

### Conversion of Horizontal Wind to Vorticity and Divergence

Obtain grid values of vorticity and divergence from the grid values of TERM00357 and TERM00357 for horizontal wind. First, we obtain the spectra of vorticity and divergence from TERM00359 and TERM00359,

     EQ=00140.
     EQ=00140.

     EQ=00141.
     EQ=00141.

I'll take that further,

     EQ=00107.

and so on.

### Calculating a Provisional Temperature

Provisional Temperature TERM00361 is ,

     EQ=00142.

However, it is TERM00362 and TERM00363 is the gas constant for water vapor (461 TERM00364TERM00365) and TERM00366 is the gas constant for air (287.04 TERM00367TERM00368).

### Calculating the Barometric gradient term

The barometric gradient term TERM00369 is first used to define the TERM00370

     EQ=00108.

to a spectral representation and then ,

     EQ=00109.

     EQ=00110.

### Diagnostic calculations of vertical flow.

Barometric pressure change term, and lead DC,

     EQ=00111.

     EQ=00112.

and its non-gravity components.

     EQ=00113.

     EQ=00114.

### Time change term due to advection.

Momentum advection term:

     EQ=00143.
     EQ=00143.

     EQ=00144.
     EQ=00144.

     EQ=00115.

Temperature advection term:

     EQ=00116.

     EQ=00117.

     EQ=00145.
     EQ=00145.
     EQ=00145.
     EQ=00145.
     EQ=00145.
     EQ=00145.

Water vapor advection term:

     EQ=00118.

     EQ=00119.

     EQ=00120.

### Conversion of Predictive Variables into Spectra

(122) and (123).

Convert TERM00380 and TERM00380 to a spectral representation of vorticity and divergence TERM00381 and TERM00381. Furthermore, converting the temperature TERM00382, specific humidity TERM00383, and TERM00384 to

     EQ=00121.

to a spectral representation.

### Conversion of time-varying terms to spectra

Time Variation Term of Vorticity

     EQ=00146.
     EQ=00146.
     EQ=00146.

The non-gravity wave component of the time-varying term of the divergence

     EQ=00147.
     EQ=00147.
     EQ=00147.
     EQ=00147.

The non-gravity wave component of the time-varying term of temperature

     EQ=00148.
     EQ=00148.
     EQ=00148.

Time-varying term of water vapor

     EQ=00149.
     EQ=00149.
     EQ=00149.

### Spectral value time integration

Equations in matrix form

     EQ=00150.
     EQ=00150.
     EQ=00150.
     EQ=00150.

Using LU decomposition, TERM00394 is obtained by solving for

     EQ=00122.

     EQ=00123.

Calculate the value of the spectrum in TERM00400, TERM00401 and then calculate the value of the spectrum in TERM00402 using

     EQ=00151.
     EQ=00151.
     EQ=00151.
     EQ=00151.
     EQ=00151.

### Conversion of Predictive Variables to Grid Values

Obtain grid values of horizontal wind speed from the spectral values of vorticity and divergence (TERM00403 and TERM00403) TERM00404 and TERM00404.

     EQ=00124.

     EQ=00125.

Furthermore,

     EQ=00126.

TERM00408, TERM00408, and so on,

     EQ=00152.

to calculate.

### Pseudo etc. TERM00409 Surface Diffusion Correction

The horizontal diffusion is applied on the surface of TERM00410, but it can cause problems in large slopes, such as transporting water vapor uphill and causing false precipitation at the top of a mountain. To mitigate this problem, corrections have been made for TERM00412 and TERM00412 to make the diffusion closer to that of the TERM00411 surface, e.g., for TERM00412.

     EQ=00153.
     EQ=00153.
     EQ=00153.

So,

     EQ=00127.

and so on. In TERM00413, the spectral value of TERM00414 is converted to a grid by multiplying the spectral value of TERM00415 by the spectral representation of the diffusion coefficient.

### Consideration of frictional heat from diffusion.

Frictional heat from diffusion is ,

     EQ=00128.

It is estimated that Therefore,

     EQ=00129.

### Correction for conservation of mass

In the spectral method, the global integral of TERM00416 is preserved with rounding errors removed, but the preservation of the mass, i.e. the global integral of TERM00417 is not guaranteed. Moreover, a wavenumber break in the spectra sometimes results in negative values of the water vapor grid points. For this reason, we perform a correction to preserve the masses of dry air, water vapor, and cloud water, and to remove the regions with negative water vapor content.

At the beginning of the dynamics calculations, the global integrals of `MODULE:[FIXMAS]`, water vapor, and cloud water are calculated for TERM00418 and TERM00418.

     EQ=00154.
     EQ=00154.

In the first step of the calculation, the dry mass TERM00419 is calculated and stored.

     EQ=00155.

At the end of the calculation, `MODULE:[MASFIX]`, the following procedure is followed.

First, negative water vapor is removed by dividing the water vapor from the grid points immediately below the grid points. Suppose that TERM00420 is used,

         EQ=00156.
         EQ=00156.

 However, this should only be done if it is TERM00421.

Next, set the value to zero for the grid points not removed by the above procedure.

3. calculate the global integral value of TERM00422 and multiply the global water vapor content by a fixed percentage so that it is the same as that of TERM00423.

         EQ=00130.

4. correct for dry air mass Likewise calculate TERM00424,

         EQ=00131.

### Horizontal Diffusion and Rayleigh Friction

The coefficients of horizontal diffusion can be expressed spectrally,

     EQ=00132.

     EQ=00133.

     EQ=00134.

TERM00425 is the Rayleigh coefficient of friction. The Rayleigh coefficient of friction is

     EQ=00135.

However, the profile is given in the same way as However,

     EQ=00136.

The results are approximate to those of TERM00426 and TERM00427. The standard values are TERM00426, TERM00427 (TERM00428: top level of the model), TERM00429 m, and TERM00430 m.

### Time Filter.

Apply the time filter of Asselin (1972) to remove computational modes in leap frog at every step.

     EQ=00137.

and TERM00431 are obtained. This TERM00433 is used as the TERM00432 for the next step of the mechanical process. As a rule, 0.05 is used for TERM00434.

In fact, the first step is to convert the predictor to a grid value at the `MODULE:[GENGD]`,

     EQ=00138.

and after the physical process is finished and the value of TERM00435 is fixed, the `MODULE:[TFILT]` can be used to determine

     EQ=00139.

.