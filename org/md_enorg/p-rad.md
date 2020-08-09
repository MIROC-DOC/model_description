## Radiant Flux.

### Summary of Radiation Flux Calculations

The CCSR/NIES AGCM radiation calculation scheme is based on the Discrete Ordinate Method and the k-Distribution Method. Considering the absorption, emission, and scattering processes of solar and terrestrial radiation due to gases, clouds, and aerosols, the values of radiation flux at each level are calculated. The main input data are air temperature (TERM00645), specific humidity (TERM00646), cloud water content (TERM00647), and cloud cover (TERM00648), and the output data are upward and downward radiation fluxes, TERM00649, TERM00649, and the derivative of upward radiation fluxes on the surface temperature The coefficient is TERM00650.

The computation is divided into several spectral regions. Each wavelength range is further divided into several subchannels based on the k-distribution method. For gas absorption, we adopt the band absorption of TERM00651, TERM00652, TERM00653, TERM00654, TERM00655, and the continuous absorption of TERM00656, TERM00657, TERM00658, and CFC. As for scattering, the Rayleigh scattering of gases and scattering by cloud and aerosol particles are adopted.

The outline of the calculation procedure is as follows (subroutine names in parentheses).

1. calculate the Planck function from atmospheric temperature `MODULE:[PLANKS]`.

Calculates the optical thickness due to gas absorption in each subchannel `MODULE:[PTFIT]`.

3. calculate the optical thickness by continuous absorption and CFC absorption `MODULE:[CNTCFC]`.

4. calculate the optical thickness and scattering moments for Rayleigh scattering and particle scattering `MODULE:[SCATMM]`.

From the optical thickness and solar zenith angle of the scattering, we obtain the albedo of the sea surface `MODULE:[SSRFC]`.

6. for each subchannel, expand the Planck function by optical thickness `MODULE:[PLKEXP]`.

7. for each subchannel, calculate the transmission coefficient, reflection coefficient, and source function for each layer `MODULE:[TWST]`

8. calculate the radiative flux at the boundary of each layer by the adding method `MODULE:[ADDING]`

In order to take into account the partial cloud coverage, the transmission coefficients, reflection coefficients, and source functions are calculated separately for the cloud-covered and cloud-free cases, and averaged by multiplying the cloud cover weights. The cloud cover case and the cloud cover case are computed separately, and the cloud cover weight is multiplied by the weight of the cloud cover. We also calculate the clear sky radiation flux by adding several times.

### Wavelengths and Subchannels.

The basis of the radiative flux calculation is the Beer-Lambert's law

     EQ=00240.

. TERM00659 is the radiant flux density at the wavelength TERM00660. TERM00661 is the absorption coefficient. In order to calculate the heating rate of the radiation flux, an integral operation for wavelengths is necessary.

     EQ=00241.

However, it is not easy to evaluate the integration of the absorption and emission of gas molecules in a precise manner because of the complicated wavelength dependence of the absorption line structure of the molecules. The k-distribution method has been developed for the purpose. Considering the density function TERM00664 for the absorption coefficient TERM00663 in the absorption coefficient TERM00662 in a certain wavelength range, (277) is calculated by

     EQ=00242.

which is approximated by where TERM00665 is the flux averaged over a wavelength of TERM00666 with an absorption coefficient of TERM00667 in this wavelength range. This equation works well if TERM00668 and TERM00668 are relatively smooth functions of TERM00669,

     EQ=00243.

We can compute relatively precisely the summation of a finite number of exponential terms (subchannels), as shown in This method has the additional advantage that it is easy to take into account absorption and scattering at the same time.

The CCSR/NIES AGCM can be run at various wavelengths by changing the radiation parameter data. In the current standard AGCM, the wavelength region is divided into 18 spectral divisions. Each wavelength region is divided into one to six subchannels (corresponding to the TERM00670 in the above equation), and the total number of subchannels is 37. The wavelength range is divided into 50, 250, 400, 400, 550, 770, 990, 1100, 1400, 2000, 2500, 4000, 14500, 31500, 33000, 34500, 36000, 43000, 46000, and 50000 in wavenumber (TERM00671).

### Calculating the Planck function `MODULE:[PLANKS]`

The Planck function TERM00672 integrated in each wavelength range is evaluated by the following equation.

     EQ=00244.

TERM00673 is the average wavelength in the wavelength range, and TERM00674 is a parameter determined by function fitting. It is calculated for the atmospheric temperature (TERM00675) of each layer, the atmospheric temperature (TERM00676) of the boundary of each layer, and the surface temperature (TERM00677) of the ground surface.

In the following, the term TERM00678 for the wavelength range is basically omitted.

### Calculating the optical thickness by gas absorption `MODULE:[PTFIT]`

The optical thickness of the gas absorption is given by the index TERM00679 as follows

     EQ=00245.

where TERM00680 is the absorption coefficient of the molecule TERM00681, which is different for each subchannel.

     EQ=00246.

as a function of temperature TERM00682(K) and atmospheric pressure TERM00683(hPa). TERM00684 is the quantity of gas in the layer represented by mol TERM00685 and is given by the volume mixing ratio TERM00686 (in ppmv),

     EQ=00247.

This can be calculated as follows. Note that TERM00687 is the gas constant per mole (8.31 J TERM00688 TERM00689) and the thickness of the gas layer (TERM00690) is measured in km. The volumetric mixing ratio (TERM00691) in ppmv can be calculated from the mass mixing ratio (TERM00692),

     EQ=00248.

which can be converted by TERM00693 and TERM00693 are the gas constants per mass of the target molecule and atmosphere, respectively, and TERM00694 and TERM00694 are the average molecular weights of the target molecule and atmosphere, respectively.

This calculation is done for each sub-channel and each layer.

### Optical Thickness by Continuous Absorption and CFC Absorption `MODULE:[CNTCFC]`

The optical thickness of the optical thickness of TERM00695 by continuous absorption in TERM00696 is considered to be due to the dimer and is basically evaluated in proportion to the square of the volume mixing ratio of the water vapor.

     EQ=00249.

TERM00698 in TERM00697 expresses the temperature dependence of absorption of the dimer. In addition, a contribution proportional to the square of the volume mixing ratio of water vapor is incorporated in the wavelength range where normal gas absorption is ignored.

The continuous absorption of TERM00699 is assumed to be constant in the mixing ratio,

     EQ=00250.

.

Continuous absorption of TERM00700 is achieved by using the mixing ratio TERM00701 and incorporating the temperature dependence,

     EQ=00251.

Absorption of CFCs is considered for TERM00702 types of CFCs,

     EQ=00252.

The sum of these optical thicknesses is TERM00703.

     EQ=00253.

This calculation is performed for each wavelength range and each layer.

### Scattering optical thickness and scattering moments `MODULE:[SCATMM]`

The optical thicknesses of Rayleigh scattering and particle dissipation (including scattering and absorption) are

     EQ=00254.

where TERM00704 is the dissipation coefficient of Rayleigh scattering, TERM00705 is the dissipation coefficient of the particle TERM00706, and TERM00707 is the volume mixing ratio of the particle TERM00708 converted to the standard state.

The conversion from the mass mixing ratio of cloud water (TERM00709) to the standard state-change volume mixing ratio of cloud particles (ppmv) is as follows

     EQ=00255.

However, TERM00710 is the density of cloud particles.

On the other hand, the scattering-induced part of the optical thickness, TERM00711, is

     EQ=00256.

where TERM00712 is the scattering coefficient for Rayleigh scattering and TERM00713 is the scattering coefficient for the particle TERM00714.

The normalized scattering moments TERM00715 (asymmetric factor) and TERM00716 (forward scattering factor) are not the same as those of the

     EQ=00257.

     EQ=00258.

where TERM00717 and TERM00717 are the scattering moments of Rayleigh scattering, and TERM00718 and TERM00718 are the scattering moments of the particles TERM00719.

This calculation is performed for each wavelength range and each layer.

### Albedo at Sea Level `MODULE:[SSRFC]`

Albedo TERM00720 at sea level is obtained by adding the optical thickness of the scattered signal vertically to TERM00721 and using the solar incidence angle factor TERM00722,

     EQ=00259.

However, it is expressed as However,

     EQ=00260.

It is.

This calculation is done for each wavelength.

### Total Optical Thickness.

The optical thickness, taking into account all gas band absorption, continuous absorption, Rayleigh scattering, and particle scattering and absorption, is about

     EQ=00261.

where TERM00723 is different for each subchannel and each layer is calculated separately. Here, since TERM00723 is different for each subchannel, the calculation is performed for each subchannel and each layer.

### Planck function expansion `MODULE:[PLKEXP]`

In each layer, the Planck function TERM00724 is

     EQ=00262.

and obtain the expansion coefficients TERM00725 and TERM00725. Here, TERM00727 at the upper end of each layer (the boundary with the upper layer) is used as TERM00726, TERM00729 at the lower end of each layer (the boundary with the lower layer) is used as TERM00728, and TERM00731 at the representative level of each layer is used as TERM00730.

     EQ=00285.
     EQ=00285.
     EQ=00285.

This calculation is done for each sub-channel and each layer.

### Transmission and reflection coefficients of each layer, the source function `MODULE:[TWST]`

Using the obtained optical thickness TERM00732, the scattering optical thickness TERM00733, the scattering moments TERM00734 and TERM00734, the expansion coefficients of the Planck function TERM00735 and TERM00735, and the solar incidence angle factor TERM00736, we obtain a uniform layer of Assuming that the transmission coefficient (TERM00737), the reflection coefficient (TERM00738), the downward radiation source function (TERM00739), and the upward radiation source function (TERM00740) are obtained by the two-stream approximation.

The single-scattering albedo TERM00741 is a ,

     EQ=00263.

The optical thickness corrected for contributions from the forward scattering factor TERM00742 TERM00743, the single-scattering albedo TERM00744, and the asymmetry factor TERM00745 are all in the same order,

     EQ=00286.
     EQ=00286.
     EQ=00286.

From now on, as a phase function of the normalized scattering,

     EQ=00287.
     EQ=00287.

However, TERM00746 is a two-stream directional cosine,

     EQ=00264.

     EQ=00265.

Furthermore,

     EQ=00288.
     EQ=00288.
     EQ=00288.
     EQ=00288.

the reflection coefficient (TERM00747) and the transmission coefficient (TERM00748) are

     EQ=00289.
     EQ=00289.

     EQ=00290.
     EQ=00290.

Next, we first find the source function from which the Planck function is derived.

     EQ=00266.

The expansion coefficients of the radiant function can be found from

     EQ=00291.
     EQ=00291.
     EQ=00291.
     EQ=00291.

     EQ=00292.
     EQ=00292.

The source function TERM00749, which is derived from the Planck function, is

     EQ=00293.
     EQ=00293.

On the other hand, the source function of the solar-induced radiation is

     EQ=00267.

than ,

     EQ=00268.

we obtain the following by using

     EQ=00294.
     EQ=00294.

This calculation is done for each sub-channel and each layer.

### Combinations of source functions for each layer.

The source functions of both Planck's and solar-induced origins are

     EQ=00269.

This value is the total optical thickness of TERM00750 from the top of the atmosphere to the top of the layer under consideration, where TERM00752 is the incident flux in the wavelength range under consideration. Note that the TERM00750 is the total optical thickness of the TERM00751 from the top of the atmosphere to the top of the layer under consideration, and the TERM00752 is the incident flux in the considered wavelength range. That is, TERM00753 is the incident flux at the top of the layer under consideration. This calculation does not actually work in practice,

     EQ=00270.

We do as follows. TERM00754 is the product of the topmost layer of the atmosphere to the layer above the one we are considering.

This calculation is done for each sub-channel and each layer.

### Radiation flux at each layer boundary `MODULE:[ADDING]`

Once the transmission coefficient (TERM00755), reflection coefficient (TERM00756), and source function (TERM00757) of each layer are obtained for all layers (TERM00758), the radiation flux at the boundary of each layer can be calculated using the adding method. This is based on the fact that, if the TERM00759 and TERM00759 of the two layers are known, the total TERM00760 and TERM00760 of the combined layer can be obtained by a simple calculation. In the homogeneous layer, the reflectance and transmittance of the upper incident layer are the same as that of the lower incident layer, and the transmittance and reflectance of the lower incident layer are the same as those in the homogeneous layer, but in the heterogeneous layer composed of multiple layers, the reflectance and transmittance of the upper incident layer (TERM00761 and TERM00761) and the reflectance and transmittance of the lower incident layer (TERM00761 and TERM00761) are different, so that we can obtain Distinguish between TERM00762 and TERM00762. Now, if these values of TERM00763 and TERM00763 are known in the upper layer1 and the lower layer2, the combined layer values of TERM00764 and TERM00764 are as follows.

     EQ=00295.
     EQ=00295.
     EQ=00295.
     EQ=00295.
     EQ=00295.
     EQ=00295.

It is assumed that there are layers 1, 2, ...and TERM00765 from the top. However, the surface is considered to be a single layer, and the TERM00766 is assumed to be the first TERM00766 layer. Considering the reflection coefficient and the radiation source functions (TERM00769 and TERM00769) of the TERM00767 to TERM00768 layers as a single layer, we assume that the surface of the Earth is a single layer and is defined as the TERM00766 layer,

     EQ=00296.
     EQ=00296.

This is the value at the surface

     EQ=00297.
     EQ=00297.

and can be solved by TERM00770 and TERM00770 in sequence, starting from However,

     EQ=00271.

Next, considering the reflectance and the emissivity functions (TERM00772 and TERM00772) for the layers from the first to the TERM00771st layer as a single layer, we find that

     EQ=00298.
     EQ=00298.

and this can also be solved by TERM00774 and TERM00774 starting from TERM00773 and TERM00773.

Using these, the downward flux TERM00777 and the upward flux TERM00778 at the boundary between layers TERM00775 and TERM00776 are reduced to a problem between the two layers, the combined layer TERM00779 and the combined layer TERM00780,

     EQ=00299.
     EQ=00299.

which can be written as However, the flux at the upper end of the atmosphere can be written as

     EQ=00300.
     EQ=00300.

Finally, since this flux is scaled, we rescale it and add direct solar incidence to obtain the radiative flux.

     EQ=00301.
     EQ=00301.
     EQ=00301.
     EQ=00301.

This calculation is done for each sub-channel.

### Add in the flux.

Once the radiation flux (TERM00781) for each subchannel of each layer is obtained, the wavelength-integrated flux is obtained by multiplying the flux by the weight (TERM00782) corresponding to the wavelength of the representative subchannel and adding them together.

     EQ=00272.

In practice, we add the fluxes in the short wavelength region (solar region) and the long wavelength region (terrestrial radiation region) to each other. In addition, we obtain PAR (photosynthetically active radiation) as the downward flux at the earth's surface in a part of the short wavelength region (shorter than the wavelength of TERM00783).

### The temperature derivative of the flux

In order to solve the surface temperature by implicitly, we calculate the differential term TERM00784 of the upward-flowing flux to the surface temperature. For this purpose, we also obtain the value of TERM00786, which is 1K higher than that of TERM00785, and recalculate the flux by the addition method using that value, and obtain the difference from the original value as TERM00787. This value is meaningful only in the long wavelength region (earth's radiation region).

### Handling of cloud cover

The CCSR/NIES AGCM considers the horizontal coverage of clouds in a grid. The two types of clouds are as follows.

1. stratus cloud. The large-scale condensation scheme `MODULE:[LSCOND]` is used to diagnose these clouds. For each layer (TERM00788) the grid-averaged cloud water content (TERM00789) and the horizontal coverage (cloud cover) (TERM00790) are defined for each layer (TERM00788).

2. cumulus clouds. Diagnosed with the cumulus convection scheme `MODULE:[CUMLUS]`. For each layer (TERM00791) the grid-averaged cloud cover (TERM00792) is defined, but the horizontal coverage (cloud cover) TERM00793 is assumed to be constant in the vertical direction.

In these treatments, it is assumed that the stratocumulus clouds randomly overlap vertically, and that the cumulus clouds always occupy the same area in the upper and lower layers (and that the cloud cover is assumed to be zero or one if it is restricted to that area). For this purpose, the calculation is performed as follows.

1. optical thickness of Rayleigh and particle scattering/absorption etc. TERM00794,TERM00794,

     1. the presence of clouds and water in the cloud cover of TERM00795 (stratocumulus)

     2. when there are no clouds at all

     3. when cloud water of TERM00796 is present (cumulus clouds)

 Calculate for.

We calculate the reflection coefficient, transmission coefficient, and radiation function (origin of Planck's function and origin of solar radiation) for each layer for the three cases above. The value for the case without clouds is set to TERM00797, the case with stratus clouds is set to TERM00798, the case with cumulus clouds is set to TERM00799, and so on.

3. the reflection coefficient, transmission coefficient, and radiative function of each layer are averaged with the weight of the cloud cover of the stratocumulus (TERM00800). Expressing the averaged values with the TERM00801

         EQ=00302.
         EQ=00302.
         EQ=00302.
         EQ=00302.

 However, the However ,

         EQ=00273.

 It is. Also ,

         EQ=00303.
         EQ=00303.

 Seek also.

Fluxes TERM00805 and TERM00805 are calculated for the cases with the characteristic values of average (e.g., TERM00802), without clouds (e.g., TERM00803), and cumulus (e.g., TERM00804) by using the ading method, respectively.

5. the final flux we seek is

         EQ=00274.

     (TERM00806 is calculated to estimate cloud radiative forcing.)

### Incidence flux and angle of incidence `MODULE:[SHTINS]`

The incident flux TERM00807 is defined as the ratio of the solar constant (TERM00808) and the distance between the sun and the earth to the time-averaged value (TERM00809).

     EQ=00275.

Here, TERM00810 asks the following.

     EQ=00276.

As ,

     EQ=00277.

Note that TERM00811 is expressed in days from the beginning of the year.

The angle of incidence is obtained as follows. Find the angular position of the sun, TERM00812, as

     EQ=00278.

As the solar declination TERM00813 is

     EQ=00279.

Then the angle of incidence factor TERM00814 (TERM00815 is the zenith angle) is

     EQ=00280.

TERM00816 is the latitude and TERM00817 is the time angle (local time minus TERM00818).

Assuming that the eccentricity of the Earth's orbit is TERM00819 (Katayama, 1974),

     EQ=00304.
     EQ=00304.
     EQ=00304.
     EQ=00304.
     EQ=00304.
     EQ=00304.
     EQ=00304.
     EQ=00304.

It is also possible to give the annual mean solar radiation. In this case, the mean annual incidence and the mean annual angle of incidence are approximately as follows

     EQ=00281.

     EQ=00282.

### Other Notes.

The calculation of the radiation is usually not done at every step. For this reason, we save the radiation flux and use it for the time when the radiation calculation is not performed. For the short-wave radiation, the flux (TERM00823) is calculated by using the ratio of the time of daylight between the next calculation time and the time of the next calculation (TERM00820) as a percentage of the time of daylight (the time of TERM00820) and the solar incidence angle factor (TERM00822) averaged over the daylight period,

         EQ=00283.

 .

Cloud water is treated as water and ice clouds depending on the temperature. The fraction treated as ice clouds TERM00824 is

         EQ=00284.

     (but with a maximum value of 1 and a minimum value of 0). Let TERM00825 and TERM00825 be set to TERM00825.