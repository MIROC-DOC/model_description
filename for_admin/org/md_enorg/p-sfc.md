## Surface Processes.

### Overview of Surface Processes.

Surface processes provide boundary conditions at the lower edge of the atmosphere through the exchange of momentum, heat, and water fluxes between the atmosphere and the surface. The surface process evaluates the thermal inertia of the earth's surface, water accumulation, snow accumulation, sea ice accumulation, etc. by using original forecast variables such as temperature (TERM00900), moisture (TERM00901), and snow cover (TERM00902). The main input data are the diffusion of geophysical quantities between the atmosphere and the earth's surface, as well as radiation and precipitation fluxes. The output data consist of surface temperature (TERM00903) and various boundary condition parameters such as albedo and roughness.

Surface processes are classified as follows.

1. geothermal diffusion processes - Determining the geothermal structure

2. geological and hydrological processes - Determining the structure of underground water, runoff, etc.

3. snow accumulation process - snow accumulation, snowmelt, etc., expression of snow-related processes

4. oceanic mixed layer processes - determining ocean temperature and sea ice thickness (optional)

We briefly list the characteristics of the CCSR/NIES AGCM surface processes:

Evaluate the thermal conductivity and water diffusion (optional) of multiple layers in the ground.

2. assessing the surface heat balance using the surface temperature.

3. diffusional conduction of heat and water is solved by the implicit method.

Snow is not treated as a separate layer, but is evaluated together with the first surface layer.

5. assessing oceanic mixed layers and sea ice in multiple layers (optional)

We follow the flow of the calculations and give a brief description of the scheme. \The entries in the square brackets are the names of the corresponding subroutines and the ones in parentheses are the file names. The entries enclosed in parentheses refer to the description in other sections.

1. (Evaluate surface fluxes `MODULE:[SFCFLX(psfcm)]`)
 The heat, water (evaporation), and momentum fluxes between the atmosphere and the earth's surface are estimated using the bulk formula. However, the evaporation efficiency (TERM00904) is set to 1.

2. evaluate the surface roughness `MODULE:[GNDZ0(pgsfc)]`
 Basically, it is given from the outside, depending on the file and surface type, but it can be changed depending on the amount of snowfall and other factors.

3. assessing the heat flux and heat capacity within the ground surface . `MODULE:[LNDFLX(pglnd), SEAFLX(pgsea), SNWFLX(pgsnw)]`
 The heat capacity of the land and sea layers is estimated, and the heat fluxes at the boundary of each layer are estimated from the heat conduction equation. When snowfall is present, the heat capacity and fluxes are changed.

4. evaluate the water flux and capacity of the land surface `MODULE:[LNDWFX(pglnd)]`
 Estimate the capacity of water in each layer of land and the water flux at the boundary of each layer from the water diffusion equation

5. evaluate the evaporation efficiency `MODULE:[GNDBET(pgsfc)]`
 For the land surface, the calculation depends on soil moisture and stomatal resistance.

6. implicit solution of geo-thermal conduction up to the middle `MODULE:[GNDHT1(pggnd)]`
 We evaluate the temperature change due to heat conduction in the ground. However, since the evaluation is done implicitly including the change in surface temperature, we only perform the first stage of the evaluation here.

7. solving the surface heat balance `MODULE:[SLVSFC(pgslv)]`
 Solves the equation for the heat balance at the earth's surface and obtains the temporal variation of temperature at the earth's surface and temperature and specific humidity in the first layer of the atmosphere. These equations are used to correct the heat/water (evaporation) fluxes between the atmosphere and the ground surface and the heat conduction fluxes at the ground surface. When there is snow or ice cover and the surface temperature exceeds the freezing point, the surface temperature is used as the freezing point, and the residual flux is evaluated as the flux used for snow melting.

8. implicit solution for geothermal conduction `MODULE:[GNDHT2(pggnd)]`
 Since the change in surface temperature was obtained, it is used to solve for the change in underground temperature due to heat conduction.

9. evaluate snow reduction by snow sublimation `MODULE:[SNWSUB(pgsnw)]`
 For snow accumulation conditions, the evaporation (sublimation) flux reduces the snow accumulation by the calculated flux.

10. assessing the increase in snow cover due to snowfall `MODULE:[SNWFLP(pgsnw)]`
 It discriminates between snowfall and rainfall and increases the snowpack when it falls.

11. assessing snowfall reduction due to snowmelt `MODULE:[SNWMLP(pgsnw)]`
 When the surface temperature or the first layer temperature is above the freezing point during snow accumulation, snowmelt is assumed to occur and the snow accumulation is reduced by keeping the temperature below the freezing point.

12. implicit solution for groundwater diffusion `MODULE:[GNDWTR(pggnd)]`
 Solving changes in subsurface moisture due to subsurface water fluxes.

13. evaluate precipitation interception by snowpack `MODULE:[SNWROF(pgsnw)]`
 When there is snowfall, the infiltration of precipitation into the soil is prevented and rainfall and snowmelt water (part of it) become runoff.

14. assessing surface runoff `MODULE:[LNDROF(pglnd)]`
 Calculation of surface runoff of rainfall and snowmelt. Three evaluation methods can be selected: the bucket model, the new bucket model, and runoff evaluation using infiltration capacity.

15. evaluate the freezing process `MODULE:[LNDFRZ(pglnd)]`
 Calculates the temperature change due to the freezing and thawing of the ground moisture and the resulting latent heat release. However, this routine is optional and is usually skipped.

16. assessing the growth of sea ice `MODULE:[SEAICE(pgsea)]`
 With the oceanic mixed layer option, the increase or decrease in the thickness of the sea ice due to heat transfer is calculated.

17. evaluate the melting of sea ice surface `MODULE:[SEAMLT(pgsea)]`
 If the surface temperature or the first layer temperature of the sea ice is above the freezing point, melting is assumed to occur and the temperature is kept below the freezing point to reduce the thickness of the sea ice.

18. nudge the ocean temperature `MODULE:[SEANDG(pgsea)]`
 With the oceanic mixed layer option, nudging can be added to the sea surface temperature to bring it closer to a given temperature.

19. evaluate the wind speed on the ground `MODULE:[SLVWND(pggnd)]`
 Solving for changes in wind speed in the first layer of the atmosphere.

Some of the above routines are further subdivided into subroutines for the evaluation of land, sea and snow surfaces as follows

1. setting the boundary conditions `MODULE:[GNDSFC(pgbnd)]`

     1. read the surface conditions `MODULE:[GETIDX(pgbnd)]`

     2. read the sea level condition `MODULE:[GETSEA(pgbnd)]`

     3. set the condition of sea level `MODULE:[SEATMP(pgsea)]`

2. evaluate the surface albedo `MODULE:[GNDALB(pgsfc)]`

     1. load the albedo `MODULE:[GETALB(pgbnd)]`

     2. change the land surface albedo `MODULE:[LNDALB(pglnd)]`

     3. change the sea-surface albedo `MODULE:[SEAALB(pgsea)]`

     4. change the snow albedo `MODULE:[SNWALB(pgsnw)]`

3. evaluate the surface roughness `MODULE:[GNDZ0(pgsfc)]`

     1. read the roughness `MODULE:[GETZ0(pgbnd)]`

     2. change the land surface roughness `MODULE:[LNDZ0(pglnd)]`

     3. change the sea surface roughness `MODULE:[SEAZ0(pgsea)]`

     4. change the snow surface roughness `MODULE:[SNWZ0(pgsnw)]`

4. evaluate the surface wetness `MODULE:[GNDBET(pgsfc)]`

     1. read the degree of wetness `MODULE:[GETBET(pgbnd)]`

     2. change the surface wetness `MODULE:[LNDBET(pglnd)]`

     3. change the degree of sea surface wetness `MODULE:[SEABET(pgsea)]`

     4. change the snow surface wetness `MODULE:[SNWBET(pgsnw)]`

### classification of the ground surface.

The ground surface is classified according to the externally given conditions as follows, according to the surface type TERM00905.

 - TAB00003:0.0
     m

 - TAB00003:0.1
 requirement

 - TAB00003:1.0
     \-I can't even begin to tell you what to do.

 - TAB00003:1.1
 mixed-layered ocean

 - TAB00003:2.0
     \-I can't tell you how many times I've been in a row.

 - TAB00003:2.1
 Sea Ice (given from outside)

 - TAB00003:3.0
     0

 - TAB00003:3.1
 Sea level (providing temperature from outside)

 - TAB00003:4.0
     1

 - TAB00003:4.1
 land ice

 - TAB00003:5.0
     TERM00906 2

 - TAB00003:5.1
 land surface

In addition, depending on the internally variable ice conditions, we have the following surface conditions (TERM00907).

 - TAB00004:0.0
     n

 - TAB00004:0.1
 state

 - TAB00004:1.0
     0

 - TAB00004:1.1
 Sea surface without ice

 - TAB00004:2.0
     1

 - TAB00004:2.1
 Sea Ice and Land Ice

 - TAB00004:3.0
     TERM00908 2

 - TAB00004:3.1
 land surface

These are defined in `MODULE:[GNDSFC(pgsfc)]`.

### Surface Heat Balance.

The conditions of the surface heat balance are ,

     EQ=00356.

in TERM00909 and TERM00909. TERM00909 and TERM00909 use atmospheric and subsurface predicted variables and the atmospheric and subsurface predicted variables prior to the evaluation of surface processes, but this balance is generally not satisfied in TERM00910, which was used at that time.

There are several ways to solve this problem.

1. how to consider only TERM00911 as an unknown

2. how to consider TERM00912 and TERM00912 as unknowns

The latter method is used in the CCSR/NIES AGCM. It is necessary to combine all the variables in all layers of the atmosphere and ground to solve the problem. The details will be described in the section "Solving the diffuse balance equation for atmospheric and ground systems".

There are two ways to evaluate the evaporation term TERM00913 and TERM00913.

1. as TERM00914, multiply TERM00915 (possible evaporation rate) obtained by solving (439) by TERM00916.

Solve (439) directly using TERM00917.

The temperature used in the calculation of TERM00918 is different between the former and the latter. In the former case, the temperature in the case of TERM00919 is used, while in the latter case the actual temperature is used.

In the CCSR/NIES AGCM, the former method is used as the standard method. When TERM00920 resulting from the solution of (439) on a snow or ice surface exceeds the freezing point, or TERM00921 on a sea surface divides the freezing temperature of seawater (in the case of the oceanic mixed layer model), the temperature of TERM00922 is fixed to the freezing point and each flux is calculated by fixing the temperature of TERM00922 to the freezing point, and the residuals of the equation in (439) ( energy residuals) will be used to freeze and thaw the snow and ice.

### Set the discrete coordinate system `MODULE:[SETGLV,SETWLV,SETSLV]`

The subsurface is discretized in the TERM00923 coordinate system. Land temperature is defined by the TERM00924 layer, water content by the TERM00925 layer, and ocean temperature by the TERM00926 layer. TERM00927 increases from the upper to the lower levels. The flux is defined by the layer boundary TERM00928 and TERM00928.

In addition, a layer with a thickness of zero is considered in TERM00929 and the skin temperature is defined as TERM00930. For convenience, it is represented by TERM00931 and set to TERM00932.

### Calculating land heat flux and heat capacity `MODULE:[LNDFLX]`

The evaluation of physical properties such as heat and moisture fluxes in the ground and wetness is carried out separately according to whether the ground surface is sea or land surface, and in the case of land surface, whether or not there is snow cover. In the following, we firstly describe the evaluation method for the case of land surface without snow. The differences in the evaluation methods for the cases of sea and snow surfaces will be described later.

The heat capacity of the land surface is ,

     EQ=00357.

where TERM00933 is the volume specific heat.

The land heat flux is treated as a constant heat transfer coefficient (which may depend on the TERM00934).

     EQ=00358.

     EQ=00359.

### Calculating the water flux on land `MODULE:[LNDWFX]`

The capacity of water in each layer TERM00935 is ,

     EQ=00360.

However, in practice, it is not possible to store this much water. The maximum storage capacity, i.e., the saturation capacity, is defined as the saturation water content of TERM00936,

     EQ=00361.

The basic formula for the groundwater flux can be written as follows.

     EQ=00362.

Here, TERM00937 represents the effect of gravity.

There are two ways to evaluate the groundwater flux on land.

1. fixed diffusion coefficient method

2. moisture content dependent diffusion coefficient method `MODULE:[HYDFLX]`

In the method of fixed diffusion coefficients, it is simply expressed as follows. TERM00938 is the diffusion coefficient and TERM00939 is the density of liquid water. Here, the gravitational potential term TERM00940 in (445) is neglected.

     EQ=00363.

     EQ=00364.

On the other hand, in the method with the moisture content-dependent diffusion coefficients, the hydraulic potential is obtained as follows.

     EQ=00365.

     EQ=00419.
     EQ=00419.

where TERM00941 is the saturated hydraulic conductivity, TERM00942 is the saturation degree, and TERM00943 is the pressure potential, which is given as follows

     EQ=00366.

     EQ=00367.

TERM00944, TERM00945, and TERM00946 are constants and may depend on the ground surface types TERM00947 and TERM00948.

### Calculating land surface spill`MODULE:[LNDROF]`

The following three methods can be used to evaluate runoff.

1. bucket model

2. new bucket model

3. surface runoff with consideration of infiltration capacity

In the bucket model ,

     EQ=00368.

and this is

     EQ=00369.

with the outflow as TERM00949,

     EQ=00420.
     EQ=00420.

The other two are Otherwise ,

     EQ=00421.
     EQ=00421.

The new bucket model (Kondo, 1993) is a model for estimating the average groundwater infiltration rate for spatially non-uniform surface soil types and depths. The model was originally developed to estimate the daily average runoff, but it was modified to use the model at each time step. In the new bucket model, precipitation infiltration and post-runoff soil moisture are estimated as follows.

     EQ=00370.

Here, TERM00950 is a time constant (standard value of 3600s). The runoff rate (TERM00951) is calculated from the surface water balance

     EQ=00422.
     EQ=00422.

It is estimated that However,

     EQ=00371.

The evaluation of surface runoff (TERM00952) considering infiltration capacity is given by TERM00953 for infiltration capacity, TERM00954 for stratiform rainfall intensity, and TERM00955 for convective rainfall intensity, as follows

     EQ=00372.

The amount of precipitation input percolating to the ground surface is modified as follows.

     EQ=00423.
     EQ=00423.

In the case above equation (463), the exponential distribution of the precipitation intensity probability of convective rainfall is assumed in the rainfall intensity probability TERM00956, which is derived from the following equation

     EQ=00373.

     EQ=00374.

However, the effective infiltration capacity is set to TERM00957 based on the assumption that stratiform rainfall infiltration is uniform. The value of TERM00958 is a constant (typically 0.6) for the fraction of convective rainfall area in the total grid area.

When considering multi-layered soil water transfer, we can also consider the drainage from each layer in proportion to the permeability coefficient.

### Evaluating Albedo on land `MODULE:[LNDALB]`

The evaluation of albedo is basically based on a constant value given by an external source. There are two ways to give them.

1. give a distribution in a file

2. specify a value for each surface type TERM00959

For each wavelength band, two components are given in the visible and near-infrared regions (the same values are used in the standard).

It is also possible to take into account the effects of surface wetness and the zenith angle of solar radiation as follows (not taken into account in the standard).

     EQ=00375.

     EQ=00376.

Here, the wetness factor (TERM00960) and the zenith angle factor (TERM00961) are constants.

### Evaluating roughness on land surface`MODULE:[LNDZ0]`

The evaluation of roughness is basically based on a constant value given by an external source. The two methods of evaluation are as follows.

1. give a distribution in a file

2. specify a value for each ground surface type TERM00962

The roughness TERM00963 for heat and the roughness TERM00964 for water vapor should be a constant multiple of the roughness TERM00965 for momentum if not given. (TERM00966 by default)

### Evaluating surface wetness on land`MODULE:[LNDBET]`

On the land surface, TERM00967 has a constant value of 1. For the non-ice surface, there are several evaluation methods that can be used for the non-ice surface as follows.

1. using an externally given constant value. As a way of giving ,

     1. give a distribution in a file

     2. specify a value for each ground surface type TERM00968

 There are two possibilities.

2. soil moisture Calculated as a function of TERM00969.

 Define the saturation degree TERM00970 and give it as a function.

     Function type 1. 1 if critical saturation exceeds TERM00971, below that depends on a linearity.

             EQ=00377.

     2. that depend nonlinearly on function type 2. TERM00972.

             EQ=00378.

In the following, we describe the different treatment of the sea surface from that of the land surface.

### Calculating heat flux and heat capacity at sea level `MODULE:[SEAFLX]`

At sea level, the heat capacity varies depending on the presence of sea ice. Using the volume specific heat of seawater (TERM00974) and the volume specific heat of sea ice (TERM00975), TERM00976 is used as the thickness of sea ice,

     EQ=00379.

Even at sea level, the thermal conductivity is kept constant (depending on TERM00977).

     EQ=00380.

     EQ=00381.

However, in the area where sea ice exists, the temperature between sea ice and seawater is set to TERM00978 (TERM00979 271.15K), and the thermal conductivity is set to the value of the sea ice.

     EQ=00382.

Heat fluxes in the oceans outside the sea ice area are only meaningful when using an oceanic mixed layer model.

### Evaluating surface wetness at sea level `MODULE:[SEABET]`

The surface moisture content (TERM00980) used to evaluate evaporation is a constant value of 1 for the sea surface and sea ice.

### albedo and roughness at sea level

The albedo at the sea surface not covered by sea ice is calculated in the radiation routine for each wavelength range as a function of the optical thickness of the atmosphere and the solar incidence angle in `MODULE:[SSRFC]` .

The roughness of the sea surface not covered by the ocean is calculated as a function of the momentum flux in the surface flux routine `MODULE:[SEAZ0F]` .

The albedo and roughness of the sea surface covered with sea ice are given as constant values. `MODULE:[SEAALB, SEAZ0]`. The current standard values are albedo 0.7 and roughness 1 TERM00981 m.

In the following, we describe the different treatment of the snow surface from that of the land surface.

### Snow Heat Flux Correction `MODULE:[SNWFLX]`

The snow is treated as the same thermal layer as the first layer of the ground surface. In other words, the heat capacity and thermal diffusivity of the first layer are modified by the presence of snow.

The heat capacity can be simply summed, where TERM00982 is the specific heat per mass of snow and TERM00983 is the mass per unit area of snow,

     EQ=00383.

However, TERM00984 is the heat capacity for the case without snow.

The heat flux is defined as the hypothetical temperature at the snow-soil interface of TERM00985,

     EQ=00384.

However, if TERM00986 is the snow depth and TERM00987 is the snow density, then the value of TERM00988 is obtained. Removing TERM00989 from the above equation results in

     EQ=00424.
     EQ=00424.

However, TERM00990 is the flux for the case without snow. Therefore, if this has already been calculated, the fluxes for the case with snow can be obtained by taking the harmonic mean of that and the fluxes for snow only. The temperature differential coefficients TERM00991 and TERM00992 can also be obtained by taking the harmonic mean of the temperature differential coefficients.

If there is more than a certain amount of snow cover, the temperature of TERM00993 should be regarded as the temperature of snow cover rather than the temperature of the soil. To account for such a case, in the above equation, TERM00995 is actually used instead of TERM00994, and not only TERM00996 but also TERM00997 is treated as being affected by snow cover.

     EQ=00385.

     EQ=00386.

### Calculating snow sublimation `MODULE:[SNWSUB]`

Decrease the snowpack by the amount of sublimation flux.

     EQ=00387.

When the snow accumulation is fully sublimated, the shortage of water flux is evaporated from the soil. In this case, the surface energy balance is calculated on the assumption that all the surface moisture fluxes have sublimated, and it is necessary to correct the soil temperature.

     EQ=00388.

### Calculating snowfall `MODULE:[SNWFLP]`

When precipitation arrives at the ground surface, it is judged whether it is solid (snow) or liquid (rain).

Atmosphere First Layer Wet Bulb Temperature TERM00998

     EQ=00389.

If the freezing point (TERM00999) is lower than the freezing point (TERM01000), the temperature is regarded as snow, and if it is higher than the freezing point (TERM01001), the temperature is regarded as rain. The purpose of using the wet-ball temperature is to incorporate the effect of the temperature of precipitation reaching the earth's surface depending on the evaporation rate of precipitation during its fall.

In the case of snowfall, the snowpack is increased by the amount of snowfall.

     EQ=00390.

TERM01002 is a snowfall flux.

### Snowmelt calculation `MODULE:[SNWMLP]`

If the surface energy balance (TERM01003) is positive and/or the temperature of the first layer of soil (including snow) is higher than the freezing point at a snow location, the amount of snowmelt is calculated and the latent heat of melting is corrected for the soil temperature.

Assuming that the soil temperature before the correction is set to TERM01004, the amount of snow melt (TERM01005) and the soil temperature (TERM01006) when snow melt is assumed to be equal to the amount of energy balance removed is

In TERM01007,

     EQ=00391.

     EQ=00392.

When using TERM01008 ,

     EQ=00393.

     EQ=00394.

In the case of TERM01009, it is assumed that the temperature of the snow part other than the melting snow does not change due to the energy balance. TERM01010 is the latent heat of melting, TERM01011 is the freezing point, and TERM01012 is the specific heat of ice.

The actual snowmelt and soil temperature are based on the current amount of snow melt and the case where the TERM01013 melts completely,

     EQ=00395.

     EQ=00396.

### Calculating Snow Surface Runoff`MODULE:[SNWROF]`

If there is a snow accumulation (TERM01014), prior to calculating the snow runoff, the snow runoff (TERM01015) is evaluated as follows and excluded from the surface moisture input. Also, snowmelt water (TERM01016) is added to the surface moisture input at this point.

     EQ=00397.

     EQ=00425.
     EQ=00425.
     EQ=00425.

Here, TERM01017 is the surface infiltration rate due to snow cover. The standard value of the critical snowpack (TERM01018) for infiltration is 200 kg/TERM01019.

### Evaluating albedo on snow-covered surfaces`MODULE:[SNWALB]`

If snow TERM01020 is present, the snow cover ratio is considered to be proportional to the square root of the snowpack, and the albedo approaches the snow value TERM01021 in proportion to the square root of the snowpack (the critical value TERM01022 is 200kg/TERM01023 in standard).

     EQ=00398.

In addition, the effect of snow albedo reduction during melting and wet snow cover is taken into account as follows.

     EQ=00399.

where TERM01024 is the surface temperature. The standard values for dry snow albedo (TERM01025) and wet snow albedo (TERM01026) are 0.7 and 0.5, respectively. The critical temperatures (TERM01027 and TERM01028) are 258.15 and 273.15, respectively.

Furthermore, we can take into account the effect of the zenith angle dependence of solar radiation as in the absence of snow (not taken into account in the standard).

### Evaluating Surface Roughness on Snow Covered Surfaces`MODULE:[SNWZ0]`

When the snow cover is TERM01029, the ratio of snow cover is considered to be proportional to the square root of the snowpack, and the surface roughness approaches the snow roughness in proportion to the square root of the snowpack (the critical value of TERM01030 is 200kg/TERM01031 in standard).

     EQ=00400.

The standard values for snow roughness are 10 TERM01032, 10 TERM01033, and 10 TERM01034 for momentum, temperature, and water vapor, respectively.

### Evaluating Surface Wetness on Snow Covered Surfaces`MODULE:[SNWBET]`

In the case of snow cover (TERM01035), the snow cover ratio is considered to be proportional to the square root of the snow cover, and the surface wetness approaches snow wetness 1 in proportion to the square root of the snow cover (the critical value of TERM01036 is 200kg/TERM01037 in standard).

     EQ=00401.

In the following section, we describe the optional surface processes.

### Calculating the freezing process `MODULE:[LNDFRZ]`

To use this option, the number of vertical layers in terms of temperature and moisture must be equal to the level of each layer.

After calculating the ground temperature by thermal diffusion,

 - If the ground temperature is lower than the freezing point and liquid moisture is present, the freezing of moisture will be

 - If the ground temperature is higher than the freezing point and solid moisture is present, the water will melt.

Calculate.

Assuming that the freezing rate of the TERM01038 layer is TERM01039, the freezing moisture TERM01040 is

     EQ=00402.

However, a negative value of TERM01041 represents the water to be melted. TERM01042 is the value of TERM01043 when freezing/thawing occurs until the soil temperature reaches the freezing point, and is given by

     EQ=00403.

TERM01044 has an ice point of 273.16K.

The change in soil temperature due to the latent heat of the soil moisture phase change is given by

     EQ=00404.

### oceanic mixed layer model `MODULE:[SEAFRZ]`

In the mixed layer model, the temporal variation of ocean temperature and sea ice thickness is calculated by solving the heat budget of the ocean.

Although a multi-layered model is also possible, we will take a single-layer model of thickness (TERM01045) as an example here. The predictor variables are temperature (TERM01046) and sea ice thickness (TERM01047).

First, the heat capacity of the oceans and surface fluxes are determined by `MODULE:[SEAFLX]` The heat capacity of the oceans is defined as the specific heat of water (TERM01048), the specific heat of ice (TERM01049), and the density of water and ice (TERM01050),

         EQ=00405.

 In the absence of sea ice, the heat transfer flux is

         EQ=00406.

 On the other hand, if there is sea ice,

         EQ=00407.

 where TERM01051 is the freezing temperature of sea ice at 271.35 K. where TERM01051 is the freezing temperature of sea ice at 271.35K.

     The heat flux in the TERM01052 is usually zero, but it can be provided by an external source. This is used for flux correction considering ocean heat transport.

Using this heat flux and heat capacity, we can determine the change in temperature (TERM01054) as well as the land surface.

3. the melting of the sea ice surface is treated in the same way as snow. `MODULE:[SEAFLX]`

 First, let's get the melting value (TERM01055)
 When the     TERM01056 ,

         EQ=00408.

 When the     TERM01057 ,

         EQ=00409.

 In the case of full melting, however, the value is set to TERM01058 and the heat is corrected for the difference.

         EQ=00410.

 Varying the thickness of the ice,

         EQ=00411.

 Then, vary the heat capacity correspondingly.

         EQ=00412.

The next step is to consider the growth process from the bottom of the sea ice.

     1. when there is no sea ice (TERM01059)

 When         TERM01060 ,

             EQ=00413.

 When the         TERM01061 ,

             EQ=00414.

 If this is positive, the sea ice is produced. If this value is positive, sea ice is produced. Note that TERM01062 becomes positive when TERM01063 becomes less than or equal to TERM01064 K.

             EQ=00426.
             EQ=00426.
             EQ=00426.

     2. when the sea ice already exists (TERM01065)

 Heat fluxes from the seawater beneath the sea ice to the bottom of the sea ice.

             EQ=00415.

 Estimated by The difference between TERM01066 and the heat flux from the ocean upward to TERM01067 is used for the growth or melting of sea ice.

             EQ=00416.

 So..,

             EQ=00427.
             EQ=00427.
             EQ=00427.

5. you can externally give the reference temperature TERM01068 and apply nudging to it.

         EQ=00417.

 This is a heat flux

         EQ=00418.

 The equivalent of giving a .

 To perform     flux correction, you can perform nudging by giving an appropriate TERM01069, memorize TERM01070, and give it as TERM01071.