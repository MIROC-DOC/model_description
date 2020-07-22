## Radiant Flux.

### Summary of Radiation Flux Calculations

The CCSR/NIES AGCM radiation calculation scheme is ,
Discrete Ordinate Method and
It was created based on the k-Distribution Method.
by gases and clouds/aerosols
Considering the absorption, emission, and scattering processes of solar and terrestrial radiation,
Calculate the value of the radiation flux at each level.
The main input data are temperature TERM00000, specific humidity TERM00001, cloud cover TERM00002, and cloud cover TERM00003,
The output data are upward and downward radiation fluxes, TERM00004 and TERM00004,
and the differential coefficient of upward radiation flux with respect to surface temperature
This is a TERM00005.

The calculation is done for several wavelengths.
Each wavelength range is based on the k-distribution method,
It is further divided into several sub-channels.
As for gaseous absorption,
Band Absorption in TERM00006, TERM00007, TERM00008, TERM00009, TERM00010 and ,
Continuous absorption of TERM00011, TERM00012, TERM00013
and CFC absorption is incorporated.
As for the scattering, we can use Rayleigh scattering of gases and
Scattering by cloud and aerosol particles is incorporated.

The outline of the calculation procedure is as follows (subroutine names in parentheses).

1. calculate the Planck function from atmospheric temperature `MODULE:[PLANKS]`.

2. in each subchannel,
 Calculates the optical thickness due to gas absorption `MODULE:[PTFIT]`.

3. by continuous absorption and CFC absorption
 calculate the optical thickness `MODULE:[CNTCFC]`.

4. of Rayleigh scattering and particle scattering
 Calculates the optical thickness and scattering moment `MODULE:[SCATMM]`.

5. from the optical thickness and solar zenith angle of the scattering,
 Seeking sea-level albedo `MODULE:[SSRFC]`.

6. for each sub-channel,
 Expand the Planck function by optical thickness `MODULE:[PLKEXP]`.

7. for each sub-channel,
 Calculates the transmission coefficient, reflection coefficient, and source function for each layer `MODULE:[TWST]`

8. by adding method, the
 calculate the radiation flux `MODULE:[ADDING]`

To account for the partial coverage of clouds,
The transmission coefficients, reflection coefficients and source functions for each layer are
Calculated separately for cloud cover and cloud-free conditions,
Multiply the cloud cover by the weight of the cloud cover and take the average.
We also consider the cloud cover of the cumulus clouds.
In addition, we also perform several additions and calculate the clear-sky radiation flux.

### Wavelengths and Subchannels.

The basics of radiative flux calculations are ,
Beer-Lambert's Law

> EQ=00000.

. where TERM00014 is the radiant flux density at the wavelength of TERM00015.
TERM00016 is the absorption coefficient.
In order to calculate the radiative fluxes related to the heating rate, we need to calculate the
An integration operation with respect to the wavelength is required.

> EQ=00001.
> <span id="p-rad:beer" label="p-rad:beer" label="p-rad:beer">\blazer[p-rad:beer]</span>

However, the absorption and emission of radiation by gas molecules is not
Due to the complicated wavelength dependence of the absorption line structure of the molecule,
It is not easy to evaluate this integration precisely.
The method designed to make the relatively precise calculation easier is
It is a k-distribution method.
Within a certain wavelength range, the absorption coefficient of TERM00017
Consider the density function TERM00019 for TERM00018,
([p-rad:beer\]](#p-rad:beer))

> EQ=00002.

which is approximated by where TERM00020 is
In the TERM00021, the absorption coefficient in this wavelength range has a value of TERM00022
It is a flux averaged over a wavelength.
This expression shows that TERM00023 and TERM00023 are the same as the TERM00024
If you have a relatively smooth function,

> EQ=00003.
> <span id="p-rad:beer-kd" label="p-rad:beer-kd" label="p-rad:beer-kd"> </span>

with the addition of a finite number of exponential terms (subchannels), such that
It is possible to calculate relatively precisely.
This method is furthermore ,
It has the advantage that it is easy to consider absorption and scattering at the same time.

In the CCSR/NIES AGCM ,
By changing the radiation parameter data, the
Calculations can be performed at various wavelengths.
Not currently used as a standard,
The wavelength range is divided into 18 parts.
In addition, each wavelength range is divided into one to six sub-channels (corresponding to the TERM00025 in the above formula),
There will be 37 channels in total.
The wavelength range is a wavenumber (TERM00026)
50, 250, 400, 550, 770, 990, 1100, 1400, 2000,
2500, 4000, 14500, 31500, 33000, 34500, 36000, 43000, 46000, 50000
Divided by.

### Calculating the Planck function `MODULE:[PLANKS]`

The Planck function TERM00027 integrated in each wavelength range is,
Evaluate by the following formula.

> EQ=00004.

TERM00028 is the average wavelength of the wavelength range,
TERM00029 is a parameter defined by function fitting.
This is the atmospheric temperature of each layer, TERM00030, and the boundary atmospheric temperature of each layer, TERM00031
and surface temperature TERM00032.

In the following, the index TERM00033 is basically abbreviated for the wavelength range.

### Calculating the optical thickness by gas absorption `MODULE:[PTFIT]`

The optical thickness of the gas absorption is determined by using the index TERM00034 as the type of molecule,
It looks like the following.

> EQ=00005.

where TERM00035 is the absorption coefficient of the molecule TERM00036, which is different for each subchannel.

> EQ=00006.

as a function of temperature TERM00037(K) and atmospheric pressure TERM00038(hPa).
TERM00039 is the amount of gas in the layer represented by mol TERM00040,
Volume Mixing Ratio TERM00041 (in ppmv) to ,

> EQ=00007.

And it can be calculated that .
Note that TERM00042 is the gas constant per mole (8.31 J TERM00043 TERM00044),
The unit of air layer thickness TERM00045 is in km.
The volume mixing ratio TERM00046 at ppmv is
Mass Mixture Ratio TERM00047 to ,

> EQ=00008.

This can be converted by .
TERM00048 and TERM00048 are
Gas constant per target molecule and atmospheric mass, respectively,
TERM00049,TERM00049 is
It is the average molecular weight of the target molecule and the atmosphere, respectively.

This calculation is done for each sub-channel and each layer.

### Optical Thickness by Continuous Absorption and CFC Absorption `MODULE:[CNTCFC]`

The optical thickness of the TERM00050 continuous absorption TERM00051 is ,
Think of it as a dimer,
Basically, it is evaluated in proportion to the square of the volume mixing ratio of water vapor.

> EQ=00009.

The TERM00053 for the TERM00052 section is ,
The temperature dependence of the absorption of the dimer.
Furthermore, in the wavelength range where normal gas absorption is ignored, the
Incorporate a contribution proportional to the square of the volume mixing ratio of water vapor.

The continuous absorption of TERM00054 is assumed to be constant in the mixing ratio,

> EQ=00010.

.

The continuous absorption of TERM00055 is based on the mixing ratio TERM00056 and incorporates a temperature dependence,

> EQ=00011.

Absorption of CFCs is considered for TERM00057 types of CFCs,

> EQ=00012.

The sum of these optical thicknesses is TERM00058.

> EQ=00013.

This calculation is performed for each wavelength range and each layer.

### Scattering optical thickness and scattering moments `MODULE:[SCATMM]`

The optical thicknesses of Rayleigh scattering and particle dissipation (including scattering and absorption) are

> EQ=00014.

where TERM00059 is the dissipation coefficient of Rayleigh scattering,
The TERM00060 is the dissipation factor of the particle TERM00061,
TERM00062 converted to standard conditions
It is the volume mixing ratio of the particle TERM00063.

Here, the mass mixing ratio of cloud water from TERM00064
The conversion of cloud grains to standard state-conversion volume mixing ratios (ppmv) is as follows.

> EQ=00015.

However, TERM00065 is the density of cloud particles.

On the other hand, the scattering-induced part of the optical thickness, TERM00066, is

> EQ=00016.

where TERM00067 is the scattering coefficient of Rayleigh scattering,
TERM00068 is the scattering coefficient for the particle TERM00069.

Also, the standardized scattering moments
TERM00070 (asymmetry factor) and TERM00071 (forward scattering factor) were not

> EQ=00017.

> EQ=00018.

Here, TERM00072 and TERM00072 are the scattering moments of Rayleigh scattering,
TERM00073,TERM00073 is the scattering moment of the particle TERM00074.

This calculation is performed for each wavelength range and each layer.

### Albedo at Sea Level `MODULE:[SSRFC]`

Albedo TERM00075 at sea level is the vertical addition of the optical thickness of the scattering
Using TERM00076 and the solar incidence angle factor TERM00077,

> EQ=00019.

expressed as follows.
However,

> EQ=00020.

It is.

This calculation is done for each wavelength.

### Total Optical Thickness.

Gaseous band absorption, continuous absorption, Rayleigh scattering, particle scattering and absorption
All things considered, the optical thickness is ,

> EQ=00021.

where TERM00078 is different for each subchannel. Here, since TERM00078 is different for each subchannel,
The calculation is done for each sub-channel and each layer.

### Planck function expansion `MODULE:[PLKEXP]`

In each layer, the Planck function TERM00079 is

> EQ=00022.

and obtain the expansion coefficients TERM00080 and TERM00080.
Here, as TERM00081
TERM00082 at the top of each layer (bordering the top layer),
As TERM00083, TERM00084 at the bottom edge of each layer (the boundary with the layer below),
As TERM00085, use the TERM00086 at the representative level of each layer.

> EQ=00045.
> EQ=00045.
> EQ=00045.

This calculation is done for each sub-channel and each layer.

### Transmission and reflection coefficients of each layer, the source function `MODULE:[TWST]`

So far obtained, optical thickness TERM00087, optical thickness of scattering TERM00088,
Scattering Moments TERM00089,TERM00089, Expansion Coefficient for Planck Function TERM00090,TERM00090,
Using the solar incidence angle factor TERM00091,
Assuming a uniform layer, and using the two-stream approximation
Transmission Coefficient TERM00092, Reflection Coefficient TERM00093, Downward Radiation Source Function TERM00094,
Find the upward radiation source function TERM00095.

The single-scattering albedo TERM00096 is,

> EQ=00023.

The contribution from the forward scattering factor TERM00097 is
Corrected Optical Thickness TERM00098,
The single-scattering albedo TERM00099, asymmetric factor TERM00100 is,

> EQ=00046.
> EQ=00046.
> EQ=00046.

From now on, as a phase function of the normalized scattering,

> EQ=00047.
> EQ=00047.

However, TERM00101 is a two-stream directional cosine, and

> EQ=00024.

> EQ=00025.

Furthermore,

> EQ=00048.
> EQ=00048.
> EQ=00048.
> EQ=00048.

the reflectance TERM00102 and transmission TERM00103 become

> EQ=00049.
> EQ=00049.

> EQ=00050.
> EQ=00050.

Next, we first find the source function from which the Planck function is derived.

> EQ=00026.

The expansion coefficients of the radiant function can be found from

> EQ=00051.
> EQ=00051.
> EQ=00051.
> EQ=00051.

> EQ=00052.
> EQ=00052.

The source function TERM00104, which is derived from the Planck function, is

> EQ=00053.
> EQ=00053.

On the other hand, the source function of the solar-induced radiation is

> EQ=00027.

than ,

> EQ=00028.

we obtain the following by using

> EQ=00054.
> EQ=00054.

This calculation is done for each sub-channel and each layer.

### Combinations of source functions for each layer.

The Planck function origin and solar-induced origin
The combined source function is

> EQ=00029.

However, the TERM00105 is not a good match for the upper atmosphere. However, TERM00105 has a value of
to the top of the layer we're considering now.
It is the total optical thickness of the TERM00106,
It is the incident flux in the wavelength range under consideration in TERM00107.
In other words, TERM00108 is
It is the incident flux at the top of the layer under consideration.
This calculation is actually ,

> EQ=00030.

The procedure is as follows. TERM00109 will be taken from the uppermost layer of the atmosphere by
Represents the product up to one layer above the layer we're considering now.

This calculation is done for each sub-channel and each layer.

### Radiation flux at each layer boundary `MODULE:[ADDING]`

Transmission coefficient of each layer TERM00110, Reflection coefficient TERM00111, Radiation source function TERM00112
is required in all layers of TERM00113,
The radiation fluxes at each layer boundary can be obtained by using the adding method.
This means that the two layers of TERM00114 and TERM00114 are known,
The TERM00115 and TERM00115 of the whole combined layer of the two layers can be easily calculated by
It is an exploitation of what is required .
In a homogeneous layer, the reflectance of the incident light from above, the transmission coefficient and the
It is the same as the reflectance and transmittance of the incident light from below,
Because it is different in heterogeneous layers composed of multiple layers,
The reflectance, transmittance and transmittance of the incident light from above (TERM00116, TERM00116)
Distinguish between the reflectance and the transmittance of the incident light from below (TERM00117) and the reflectance of the incident light from below (TERM00117).
Now, in layer 1 above and layer 2 below, these
If TERM00118 and TERM00118 are known,
Value in the composite layer
TERM00119,TERM00119 is
It looks like the following.

> EQ=00055.
> EQ=00055.
> EQ=00055.
> EQ=00055.
> EQ=00055.
> EQ=00055.

Let's say there are layers 1, 2, ...TERM00120 from the top.
However, the surface is considered to be a single layer and is the TERM00121 layer.
Reflectance and source function of the layers from the TERM00122 to the TERM00123 layer as a single layer
Given the TERM00124, TERM00124 ,

> EQ=00056.
> EQ=00056.

This is the value at the surface

> EQ=00057.
> EQ=00057.

It can be solved by TERM00125 and TERM00125 in sequence, starting from
However,

> EQ=00031.

In the next section, we consider the reflectance and source function of the layers from the first to the TERM00126 as a single layer
Given the TERM00127, TERM00127 ,

> EQ=00058.
> EQ=00058.

and this is also TERM00128,TERM00128
It can be solved by TERM00129 and TERM00129, starting from

With these ,
Downward flux at the boundary between layers TERM00130 and TERM00131 TERM00132
and upward flux TERM00133 is ,
TERM00134 The combination of layers and
TERM00135 Reduced to a matter between two layers of combined layers,

> EQ=00059.
> EQ=00059.

It can be written as.
However, the flux at the top of the atmosphere is not

> EQ=00060.
> EQ=00060.

Finally, since this flux is scaled ,
We rescaled and added direct solar incidence to the
Find the radiation flux.

> EQ=00061.
> EQ=00061.
> EQ=00061.
> EQ=00061.

This calculation is done for each sub-channel.

### Add in the flux.

If the radiation flux TERM00136 is found for each subchannel in each layer, the
It corresponds to a wavelength representative of the subchannel
By applying a weight (TERM00137) and adding them together,
The wavelength-integrated flux is found.

> EQ=00032.

In practice, the short wavelength range (solar region),
Divided into long wavelengths (earth's radiation region) and added together.
In addition, a part of the short wavelength region (shorter than the wavelength of TERM00138)
The downward flux at the surface is obtained as PAR (photosynthetically active radiation).

### The temperature derivative of the flux

To solve for surface temperature by implicit,
Differential term of upward flux with respect to surface temperature
Calculating TERM00139.
Therefore, the value for temperatures 1K higher than TERM00140
We also obtained TERM00141 and used it to
Redo the flux calculation using the addition method,
The difference from the original value is set to TERM00142.
This is a meaningful value only in the long-wavelength region (Earth's radiation region).

### Handling of cloud cover

In the CCSR/NIES AGCM ,
Considering the horizontal coverage of clouds in a single grid.
There are two types of clouds

1. stratus cloud. Diagnosed by the large scale condensation scheme `MODULE:[LSCOND]`.
 For each layer (TERM00143), the lattice-averaged cloud water content of TERM00144 and
 The horizontal coverage factor (cloud cover) TERM00145 is defined.

2. cumulus clouds. Diagnosed by the cumulus convection scheme `MODULE:[CUMLUS]`.
 For each layer (TERM00146) the lattice-averaged cloud water content TERM00147 is defined, but
 Horizontal coverage (cloud cover) TERM00148 shall be constant in the vertical direction.

In these treatments, we assume that the stratocumulus clouds overlap randomly in a vertical direction,
Assuming that the cumulus cloud always occupies the same area in the upper and lower layers
(Assume that the cloud cover is 0 or 1 if it is confined to that region).
To do so, we perform the following calculations.

1. optical thickness of Rayleigh and particle scattering/absorption, etc.
     TERM00149,TERM00149,

     1. when cloud water of the TERM00150 exists (stratocumulus)

     2. when there are no clouds at all

     3. when cloud water in the cloud cover of TERM00151 is present (cumulus clouds)

 Calculate for.

2. reflection and transmission coefficients for each layer,
 The radiant source function (Planck function origin, insolation origin) is
 Calculate for each of the three cases above.
 The values for no clouds.
     TERM00152, in the case of stratus clouds TERM00153, in the case of cumulus clouds
     TERM00154 and so on.

3. reflection and transmission coefficients for each layer,
 The source function is averaged with the weight of the cloud cover of the stratocumulus, TERM00155.
 The averages are represented by TERM00156,

     > EQ=00062.
     > EQ=00062.
     > EQ=00062.
     > EQ=00062.

 However, the However ,

     > EQ=00033.

 It is.
 Also,

     > EQ=00063.
     > EQ=00063.

 Seek also.

4. when the characteristic values of the average (e.g., TERM00157) are used,
 When using a characteristic value without clouds (e.g., TERM00158),
 When the characteristic values of cumulus clouds (e.g., TERM00159) are used,
 fluxes by adding, respectively.
 Find     TERM00160,TERM00160.

5. the final flux we seek is

     > EQ=00034.

     (TERM00161 is used to estimate cloud radiative forcing
 I'm doing the math.)

### Incidence flux and angle of incidence `MODULE:[SHTINS]`

Incident Flux TERM00162 is ,
Solar constant, TERM00163,
The distance between the sun and the earth,
The ratio of the ratio to the time average is TERM00164.

> EQ=00035.

Here, TERM00165 asks for the following.

> EQ=00036.

As ,

> EQ=00037.

Note that TERM00166 is the time in days since the beginning of the year.

The angle of incidence is obtained as follows.
Solar angle position TERM00167

> EQ=00038.

As the solar declination TERM00168 is

> EQ=00039.

Then the angle of incidence factor TERM00169 (where TERM00170 is the zenith angle) is

> EQ=00040.

TERM00171 is a latitude,
TERM00172 is the time angle (local time minus TERM00173).

Assuming that the eccentricity of the Earth's orbit is TERM00174 (Katayama, 1974),

> EQ=00064.
> EQ=00064.
> EQ=00064.
> EQ=00064.
> EQ=00064.
> EQ=00064.
> EQ=00064.
> EQ=00064.

It is also possible to give average annual insolation.
In this case, the annual mean incidence and the annual mean angle of incidence are
It approximates to be as follows.

> EQ=00041.

> EQ=00042.

### Other Notes.

The calculation of the radiation is usually not done at every step.
 To do so, we have to save the radiation flux,
 If the time is not used for radiation calculation, it is used.
 As for the shortwave radiation,
 Percentage of time (time that is TERM00175) between next calculation time (TERM00176) and
 Using the solar incidence angle factor (TERM00177) averaged over the daylight hours
 Seeking Flux TERM00178,

     > EQ=00043.

 .

2. cloud water depends on the temperature,
 Treated as water and ice cloud particles.
 Percentage treated as ice clouds TERM00179 is ,

     > EQ=00044.

     (but with a maximum value of 1 and a minimum value of 0). Also,
     TERM00180,TERM00180.
