## Surface Processes.

### Overview of Surface Processes.

The surface processes are the processes of momentum, heat, and water between the atmosphere and the earth's surface
Giving boundary conditions at the lower end of the atmosphere through flux exchange.
Surface processes are described in the Ground Temperature TERM00000, Ground Moisture TERM00001,
Handle your own forecast variables, such as snow cover TERM00002,
Thermal inertia of the ground surface, water accumulation, snow accumulation,
Evaluate the accumulation of sea ice and other factors.
The main input data are the diffusion of geophysical quantities between the atmosphere and the surface
and the fluxes due to radiation and precipitation.
The output data are the surface temperature (TERM00003) and
Various boundary condition parameters such as albedo and roughness.

Surface processes are classified as follows.

1. geothermal diffusion processes - Determining the geothermal temperature structure

2. geological and hydrological processes - Determining the structure of underground water, runoff, etc.

3. snow accumulation process - snow accumulation, snowmelt, etc., expression of snow-related processes

4. oceanic mixed layer processes - determining ocean temperature and sea ice thickness (optional)

We briefly list the characteristics of the CCSR/NIES AGCM surface processes:

Evaluate the thermal conductivity and water diffusion (optional) of multiple layers in the ground.

2. assessing the surface heat balance using the surface temperature.

3. diffusional conduction of heat and water is solved by the implicit method.

Snow is not treated as a separate layer, but is evaluated together with the first surface layer.

5. assessing oceanic mixed layers and sea ice in multiple layers (optional)

The scheme is outlined in detail along the calculation flow.
\where the part in the square brackets is the name of the corresponding subroutine and the part in ( ) is the file name.
The entries enclosed in parentheses refer to the descriptions in other sections.

1. (Evaluate surface fluxes `MODULE:[SFCFLX(psfcm)]`)
 The heat, water (evaporation), and momentum fluxes between the atmosphere and the surface are
 Estimate in bulk.
 However, the evaporation efficiency (TERM00004) is set to 1.

2. evaluate the surface roughness `MODULE:[GNDZ0(pgsfc)]`
 Basically, it depends on the file and the surface type.
 I can get it from the outside,
 Change according to snowfall and other factors.

3. evaluate the heat flux and heat capacity within the ground surface .
     `MODULE:[LNDFLX(pglnd), SEAFLX(pgsea), SNWFLX(pgsnw)]`
 Estimate the heat capacity of each layer of land and sea,
 The heat flux at each layer boundary is estimated from the heat transfer equation.
 If there is snowfall, change the heat capacity and flux.

4. evaluate the water flux and capacity of the land surface `MODULE:[LNDWFX(pglnd)]`
 Estimate the capacity of each layer of water on land,
 Estimate the water flux at each layer boundary from the water diffusion equation

5. evaluate the evaporation efficiency `MODULE:[GNDBET(pgsfc)]`
 For the land surface, the calculation depends on soil moisture and stomatal resistance.

6. implicit solution of geo-thermal conduction up to the middle `MODULE:[GNDHT1(pggnd)]`
 Evaluate the temperature change due to heat conduction in the ground.
 However, taking into account the surface temperature changes
 Since it is done     implicitly, only the first step is done here.

7. solving the surface heat balance `MODULE:[SLVSFC(pgslv)]`
 Solving the equation for the heat balance between the surface temperature and
 Time variation of temperature and specific humidity in the first layer of the atmosphere.
 Using this, the heat/water (evaporation) flux between the atmosphere and the ground surface
 and compensate for the heat transfer flux at the surface.
 If there is snow or ice and the surface temperature is above the freezing point,
 With the surface temperature as the freezing point,
 Evaluate the residual flux as the flux used for snowmelt.

8. implicit solution for geothermal conduction `MODULE:[GNDHT2(pggnd)]`
 Since the change in surface temperature was obtained, we used it to determine
 Solving for changes in ground temperature due to heat conduction in the ground.

9. evaluate snow reduction by snow sublimation `MODULE:[SNWSUB(pgsnw)]`
 For snow cover conditions, the calculated evaporation (sublimation) fluxes allow
 Decrease the snowpack.

10. assessing the increase in snow cover due to snowfall `MODULE:[SNWFLP(pgsnw)]`
 It discriminates between snowfall and rainfall and increases the snowpack when it falls.

11. assessing snowfall reduction due to snowmelt `MODULE:[SNWMLP(pgsnw)]`
 If the surface temperature or first layer temperature exceeds the freezing point during snowfall ,
 If the snow melts, it will keep the temperature below the freezing point,
 Decrease the snowpack.

12. implicit solution for groundwater diffusion `MODULE:[GNDWTR(pggnd)]`
 Solving changes in subsurface moisture due to subsurface water fluxes.

13. evaluate precipitation interception by snowpack `MODULE:[SNWROF(pgsnw)]`
 Snowfall prevents precipitation infiltration into the soil,
 Rainfall and snowmelt water (part of it) will be runoff.

14. assessing surface runoff `MODULE:[LNDROF(pglnd)]`
 Calculating surface runoff of rainfall and snowmelt water.
 Bucket Model, New Bucket Model,
 There are 3 evaluation methods to choose from, including runoff evaluation using permeability.

15. evaluate the freezing process `MODULE:[LNDFRZ(pglnd)]`
 Freezing and thawing of groundwater and
 Calculate the temperature change due to the latent heat release associated with it.
 However, this routine is optional,
 Usually skipped.

16. assessing the growth of sea ice `MODULE:[SEAICE(pgsea)]`
 If you specify the marine mixed layer option ,
 Calculate the increase or decrease in the thickness of the sea ice due to heat conduction.

17. evaluate the melting of sea ice surface `MODULE:[SEAMLT(pgsea)]`
 If the surface temperature or first layer temperature of the sea ice exceeds the freezing point,
 The temperature is kept below the freezing point,
 Decrease the thickness of the sea ice.

18. nudge the ocean temperature `MODULE:[SEANDG(pgsea)]`
 With the oceanic mixed layer option, the given
 Nudging to get closer to the temperature.
 It can be added to the temperature of the sea surface.

19. evaluate the wind speed on the ground `MODULE:[SLVWND(pggnd)]`
 Solving for changes in wind speed in the first layer of the atmosphere.

Also, some of the routines mentioned above are
In addition, the following subroutines for the evaluation of land, sea and snow surfaces are used
There's a split.

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

The ground surface is a condition given by the outside world,
According to the surface type TERM00005, they are classified as follows.

 - TAB00000:0.0
     m

 - TAB00000:0.1
 requirement

 - TAB00000:1.0
     \-I can't even begin to tell you what to do.

 - TAB00000:1.1
 mixed-layered ocean

 - TAB00000:2.0
     \-I can't tell you how many times I've been in a row.

 - TAB00000:2.1
 Sea Ice (given from outside)

 - TAB00000:3.0
     0

 - TAB00000:3.1
 Sea level (providing temperature from outside)

 - TAB00000:4.0
     1

 - TAB00000:4.1
 land ice

 - TAB00000:5.0
     TERM00006 2

 - TAB00000:5.1
 land surface

Furthermore, depending on the possible internal changes in the ice conditions,
Take the following ground surface conditions TERM00007.

 - TAB00001:0.0
     n

 - TAB00001:0.1
 state

 - TAB00001:1.0
     0

 - TAB00001:1.1
 Sea surface without ice

 - TAB00001:2.0
     1

 - TAB00001:2.1
 Sea Ice and Land Ice

 - TAB00001:3.0
     TERM00008 2

 - TAB00001:3.1
 land surface

These are defined in `MODULE:[GNDSFC(pgsfc)]`.

### Surface Heat Balance.

The conditions of the surface heat balance are ,

> EQ=00000.
> <span id="p-sfc:sfc-balance" label="p-sfc:sfc-balance" label="p-sfc:sfc-balance">\blazer[p-sfc:sfc-balance]</span>.

It is.
TERM00009, TERM00009 is ,
Atmospheric and subsurface forecast variables before evaluating surface processes and ,
The evaluation is performed using the
In the TERM00010 used at that time, this balance is generally not met.

There are several ways to solve this problem.

1. how to consider only TERM00011 as an unknown

2. how to consider TERM00012 and TERM00012 as unknown numbers

The CCSR/NIES AGCM uses the latter method.
In doing so, it is necessary to combine and solve for all the variables of the atmospheric and ground layers.
The details are described in the section "Solving the Diffusion-Based Budget Equations for Atmospheric Surface Systems".

There are two ways to evaluate the evaporation terms TERM00013 and TERM00013.

1. as a TERM00014
 Solved for     ([\\p-sfc:sfc-balance\](#p-sfc:sfc-balance)) TERM00015
     (possible evaporation amount) multiplied by TERM00016.

2. using TERM00017.
     ([p-sfc:sfc-balance\]](#p-sfc:sfc-balance)) directly solve.

The temperatures used in the calculations in TERM00018 are different between the former and the latter.
In the former case, the temperature in the case of TERM00019,
In the latter case, the actual temperature is used.

The CCSR/NIES AGCM uses the former method as standard.
The result of solving (with a [\blind\blind\blind\blind\blind\blade}(#p-sfc:sfc-balance)](#p-sfc:sfc-balance) on a snow or ice surface
If the TERM00020 exceeds the freezing point,
Or, when TERM00021 divides the freezing temperature of seawater at the sea surface (in the case of oceanic mixed-layer model)
by fixing the temperature of the TERM00022 at the freezing point and calculating each flux,
([p-sfc:sfc-balance\]](#p-sfc:sfc-balance)) and the residuals (energy residuals) of the formula
Suppose it is used for freezing and thawing snow and ice.

### Set the discrete coordinate system `MODULE:[SETGLV,SETWLV,SETSLV]`

The ground is discretized with the TERM00023 coordinate system.
Land temperature is layer TERM00024, water content is layer TERM00025,
Ocean temperature is defined in layer TERM00026.
The TERM00027 increases from the top to the bottom.
The flux is defined by the layer boundary TERM00028,TERM00028.

Also, consider a layer of zero thickness on the TERM00029,
Define skin temperature TERM00030.
For convenience, it is represented by TERM00031 and TERM00032.

### Calculating land heat flux and heat capacity `MODULE:[LNDFLX]`

Physical quantities, such as heat and moisture fluxes in the ground, and wetness
The evaluation of surface characteristics is based on whether the surface is sea or land, and in the case of land surface
This is done separately if there is snowfall or not.
In the following, we will first evaluate the evaluation method for the land surface case without snow.
We shall describe in brief. We will describe the difference between the case of sea level and snow surface in detail later.

The heat capacity of the land surface is ,

> EQ=00001.

where TERM00033 is the volume specific heat.

The land heat flux is treated as a constant heat transfer coefficient (which may depend on TERM00034).

> EQ=00002.

> EQ=00003.

### Calculating the water flux on land `MODULE:[LNDWFX]`

The capacity of water in each layer TERM00035 is ,

> EQ=00004.

However, in practice, it is not possible to store this much water.
The maximum storage capacity, i.e., the saturation capacity, is defined as the saturation water content of TERM00036,

> EQ=00005.

The basic formula for the groundwater flux can be written as follows.

> EQ=00006.
> <span id="basic-Fw" label="basic-Fw">\\[basic-Fw]</span>

Here, TERM00037 represents the effect of gravity.

There are two ways to evaluate the groundwater flux on land.

1. fixed diffusion coefficient method

2. moisture content dependent diffusion coefficient method `MODULE:[HYDFLX]`

In the method of fixed diffusion coefficients, we simply express it as follows.
TERM00038 is the diffusion coefficient and TERM00039 is the density of liquid water.
where the gravitational potential term TERM00040 in ([basic-Fw\]](#basic-Fw)) is
Ignore it.

> EQ=00007.

> EQ=00008.

On the other hand, the method with the moisture content dependent diffusion coefficient is not applicable,
Using the hydraulic potential, we obtain the following.

> EQ=00009.

> EQ=00063.
> EQ=00063.

where TERM00041 is the saturated hydraulic conductivity, TERM00042 is the saturation degree, and TERM00043 is the pressure potential,
It is given as follows.

> EQ=00010.

> EQ=00011.

TERM00044, TERM00045, and TERM00046 are constants and may depend on the ground surface types TERM00047 and TERM00048.

### Calculating land surface spill`MODULE:[LNDROF]`

The following three methods can be used to evaluate runoff.

1. bucket model

2. new bucket model

3. surface runoff with consideration of infiltration capacity

In the bucket model ,

> EQ=00012.

and this is

> EQ=00013.

with the outflow as TERM00049,

> EQ=00064.
> EQ=00064.

.
Other than that ,

> EQ=00065.
> EQ=00065.

The new bucket model (Kondo, 1993) is based on the idea that surface soil types and depths are spatially
It is a model for estimating the average groundwater infiltration rate for non-uniform cases.
It was originally developed to estimate the daily average outflow of ,
Here, we changed it to be used at each time step.
In the new bucket model, precipitation infiltration and post-runoff soil moisture are estimated as follows.

> EQ=00014.

Here, TERM00050 is a time constant (standard value 3600s).
In this case, the runoff volume (TERM00051) is calculated from the surface water balance

> EQ=00066.
> EQ=00066.

It is estimated that .
However,

> EQ=00015.

The evaluation of the surface runoff TERM00052 considering soil infiltration capacity is based on the evaluation of the infiltration capacity of the TERM00053,
Assuming that the intensity of stratiform rainfall is TERM00054 and that of convective rainfall is TERM00055,
Given below.

> EQ=00016.
> <span id="inf-exs" label="inf-exs">\blazer[inf-exs]</span>

The amount of precipitation input percolating to the ground surface is modified as follows.

> EQ=00067.
> EQ=00067.

On the formula ([index[inf-exs]](#inf-exs)), convective rainfall intensity probability TERM00056
It is derived from the following equation, which assumes an exponential distribution.

> EQ=00017.

> EQ=00018.

However, assuming that stratocumulus rainfall is uniformly infiltrating, the effective infiltration capacity of
TERM00057.
TERM00058 is the percentage of convective rainfall area in the total grid area,
It is a constant (0.6 by default).

When considering multi-layered soil moisture transfer,
We can also consider the drainage from each layer proportional to the permeability coefficient.

### Evaluating Albedo on land `MODULE:[LNDALB]`

The evaluation of albedo is basically based on a constant value given by an external source.
There are two ways to give it.

1. give a distribution in a file

2. specify a value for each surface type TERM00059

For each wavelength band, we can give two components in the visible and near-infrared
(The same values are used in the standard).

We can also consider the effects of surface wetness and solar radiation zenith angle as follows
(Not considered in the standard).

> EQ=00019.

> EQ=00020.

Here, the wetness factor (TERM00060) and the zenith angle factor (TERM00061) are constants.

### Evaluating roughness on land surface`MODULE:[LNDZ0]`

The evaluation of roughness is basically based on a constant value given by an external source.
There are two ways to give it.

1. give a distribution in a file

2. specify a value for each surface type TERM00062

The roughness TERM00063 for heat and the roughness TERM00064 for water vapor are
If not given, the roughness to momentum is a constant multiple of TERM00065.
(TERM00066 by default)

### Evaluating surface wetness on land`MODULE:[LNDBET]`

On land ice, TERM00067 has a constant value of 1.
For non-icy land surfaces, we can use several evaluation methods as follows.

1. using an externally given constant value. As a way of giving ,

     1. give a distribution in a file

     2. specify a value for each surface type TERM00068

 There are two possibilities.

2. soil moisture calculated as a function of TERM00069.

 Define the saturation degree TERM00070,
 We give it as a function.

     Function type 1.
 The critical saturation is 1 if it exceeds the critical saturation value of TERM00071, and is linearly dependent below it.

         > EQ=00021.

     2. that depend nonlinearly on function type 2. TERM00072.

         > EQ=00022.

In the following, we describe the different treatment of the sea surface from that of the land surface.

### Calculating heat flux and heat capacity at sea level `MODULE:[SEAFLX]`

At the sea surface, the heat capacity varies depending on the presence of sea ice.
Volumetric Specific Heat of Seawater TERM00074 and
Using the volume specific heat of sea ice with TERM00075, TERM00076 is used as the thickness of the sea ice,

> EQ=00023.

Even at sea level, the thermal conductivity is kept constant (depending on TERM00077).

> EQ=00024.

> EQ=00025.

However, in areas where there is sea ice,
The temperature of the boundary between sea ice and seawater is set to TERM00078 (TERM00079 271.15K),
Let the thermal conductivity be the value of the sea ice.

> EQ=00026.

Heat fluxes in the oceans outside the sea ice area are significant because
This is only the case with the oceanic mixed layer model.

### Evaluating surface wetness at sea level `MODULE:[SEABET]`

The surface moisture content of the TERM00080 used to evaluate evaporation is ,
The constant value of 1 for the sea surface and sea ice.

### albedo and roughness at sea level

The albedo at the sea surface, which is not covered by sea ice, is in the radiation routine,
Calculated at each wavelength as a function of atmospheric optical thickness and solar incidence angle
`MODULE:[SSRFC]` .

The roughness of the ocean surface that is not covered by the ocean is determined in the surface flux routine,
Calculated as a function of momentum flux
`MODULE:[SEAZ0F]` .

The albedo and roughness of the sea surface covered with sea ice are
Give a constant value.
`MODULE:[SEAALB, SEAZ0]`.
The current standard value is 0.7, albedo,
The roughness is 1 TERM00081 m.

In the following, we describe the different treatment of the snow surface from that of the land surface.

### Snow Heat Flux Correction `MODULE:[SNWFLX]`

The snow is treated thermally as the same layer as the first layer of the ground surface.
That is, the heat capacity and thermal diffusivity of the first layer are
The shape will be changed by the presence of snow.

The heat capacity is expressed as a simple sum of
Let TERM00082 be the specific heat per mass of snow and TERM00083 be the mass per unit area of snow,

> EQ=00027.

However, TERM00084 is the heat capacity in the absence of snow.

The heat flux is defined as the hypothetical temperature at the snow-soil interface, which is set to TERM00085,

> EQ=00028.

However, the depth of the snow cover in TERM00086 is
Let TERM00087 be the density of snow, and TERM00088 be the density of snow.
Eliminating TERM00089 from the equation above,

> EQ=00068.
> EQ=00068.

However, the TERM00090 is the flux when there is no snow.
Therefore, if this has already been calculated,
By taking the harmonic mean of that and the snow only flux,
Fluxes are required in the presence of snow.
Also, the temperature differential coefficient of the fluxes TERM00091 and TERM00092
is similarly obtained by the harmonic mean of the temperature differential coefficients.

If there is more than a certain amount of snowfall ,
The temperature TERM00093 should be regarded as the temperature of the snowpack rather than the temperature of the soil.
To account for such cases, in fact, the
In the above formula, instead of TERM00094, TERM00095 is used,
Furthermore, not only TERM00096, but also TERM00097 is changed by snow
Handling.

> EQ=00029.

> EQ=00030.

### Calculating snow sublimation `MODULE:[SNWSUB]`

Decrease the snowpack by the amount of sublimation flux.

> EQ=00031.

When the snowfall is fully sublimated, the missing water flux is evaporated from the soil.
The energy balance of the earth's surface is assumed to be the same as if the surface moisture flux were all sublimated
We need to correct for the soil temperature because it has been calculated.

> EQ=00032.

### Calculating snowfall `MODULE:[SNWFLP]`

When precipitation arrives at the ground surface, it is judged whether it is solid (snow) or liquid (rain).

Atmosphere First Layer Wet Bulb Temperature TERM00098

> EQ=00033.

If the freezing point (TERM00099) is lower than the freezing point (TERM00100), it is assumed to be snow, and if it is higher than the freezing point (TERM00101), it is assumed to be rain.
The reason why the wet-ball temperature is used is that the temperature of precipitation reaching the surface is
This is to incorporate effects that depend on the likelihood of evaporation during the fall of precipitation.

In the case of snowfall, the snowpack is increased by the amount of snowfall.

> EQ=00034.

TERM00102 is a snowfall flux.

### Snowmelt calculation `MODULE:[SNWMLP]`

If the surface energy balance (TERM00103) is positive, as a result of the calculation of the surface energy balance
and/or Soil first layer in areas with snow cover (including snowpack)
When the temperature of the soil is higher than the freezing point, the amount of snowmelt is calculated and the latent heat of melting is calculated.
Make corrections.

If the soil temperature before correction is set to TERM00104,
If the snowmelt occurred to the extent that it would resolve the energy balance
Snowmelt TERM00105 and soil temperature TERM00106 are ,

When the TERM00107 ,

> EQ=00035.

> EQ=00036.

When the TERM00108 ,

> EQ=00037.

> EQ=00038.

In the case of TERM00109, the temperature of the part of the snow that melts in the energy balance except for the snow is
I'm assuming it doesn't change.
TERM00110 is the latent heat of melting, TERM00111 is the freezing point, and TERM00112 is the specific heat of ice.

The actual snowmelt and soil temperature are based on the current amount of snow and soil temperature in the case of full melting of the TERM00113,

> EQ=00039.

> EQ=00040.

### Calculating Snow Surface Runoff`MODULE:[SNWROF]`

If there is a snow TERM00114, prior to calculating the land surface runoff
The runoff due to snow accumulation was evaluated as follows,
Exclude moisture from the surface input.
Snowmelt water (TERM00116) is added to the surface water input here.

> EQ=00041.

> EQ=00069.
> EQ=00069.
> EQ=00069.

where TERM00117 is the surface infiltration rate due to snow cover.
The standard value of critical snowpack for infiltration, TERM00118, is 200 kg/TERM00119.

### Evaluating albedo on snow-covered surfaces`MODULE:[SNWALB]`

If you have a snow TERM00120 ,
The ratio of snow cover is considered to be proportional to the square root of the snowpack,
Albedo approaches the snow value TERM00121 in proportion to the square root of the snowpack
(The critical value of TERM00122 is 200 kg/TERM00123 in standard).

> EQ=00042.

Also, when melting occurs and the snowpack is wet, the snow albedo
The smaller effect is considered as follows.

> EQ=00043.

where TERM00124 is the surface temperature.
Dry Snow Albedo TERM00125, Wet Snow Albedo TERM00126
The standard values for
The critical temperatures (TERM00127 and TERM00128) are 258.15 and 273.15, respectively.

Furthermore, as in the absence of snow, we can take into account the effect of the zenith angle dependence of solar radiation
(Not considered in the standard).

### Evaluating Surface Roughness on Snow Covered Surfaces`MODULE:[SNWZ0]`

If you have a snow TERM00129 ,
The ratio of snow cover is considered to be proportional to the square root of the snowpack,
Surface roughness approaches snow roughness in proportion to the square root of the snowpack.
(The critical value, TERM00130, is 200 kg/TERM00131 in standard).

> EQ=00044.

The standard values for snow roughness are for momentum, temperature and water vapor, respectively.
10 TERM00132, 10 TERM00133, 10 TERM00134.

### Evaluating Surface Wetness on Snow Covered Surfaces`MODULE:[SNWBET]`

If you have a snow TERM00135 ,
The ratio of snow cover is considered to be proportional to the square root of the snowpack,
Surface wetness approaches snow wetness 1 in proportion to the square root of the snowpack
(The critical value of TERM00136 is 200 kg/TERM00137 in standard).

> EQ=00045.

In the following section, we describe the optional surface processes.

### Calculating the freezing process `MODULE:[LNDFRZ]`

To use this option, you must use the
The number of vertical layers in the ground and the level of each layer must be equal.

After calculating the ground temperature by thermal diffusion,

 - If the ground temperature is lower than the freezing point and liquid moisture is present, the freezing of moisture will be

 - If the ground temperature is higher than the freezing point and solid moisture is present, the water will melt.

Calculate.

Assuming that the ice content of the TERM00138 layer is TERM00139, the freezing water (TERM00140) is

> EQ=00046.

where the negative TERM00141 represents the water to be melted.
The TERM00142 will freeze/thaw until the soil temperature reaches the freezing point.
This is the value of TERM00143 if it were to occur, given by

> EQ=00047.

TERM00144 has an ice point of 273.16K.

The change in soil temperature due to the latent heat of the soil moisture phase change is given by

> EQ=00048.

### oceanic mixed layer model `MODULE:[SEAFRZ]`

In the oceanic mixed layer model ,
By solving for the heat balance of the oceans, the temperature of the oceans and
Determine the time variation of sea ice thickness.

Multi-layered models are possible, but,
Here we will take a single layer model of thickness TERM00145 as an example.
The predictor variables are temperature (TERM00146) and sea ice thickness (TERM00147).

First, determine the heat capacity and surface flux of the ocean.
     `MODULE:[SEAFLX]`
 The heat capacity of the oceans is ,
 The specific heat of water TERM00148, the specific heat of ice TERM00149, and the density of water and ice as TERM00150,

     > EQ=00049.

 In the absence of sea ice, the heat transfer flux is

     > EQ=00050.

 On the other hand, if there is sea ice,

     > EQ=00051.

 where TERM00151 is the freezing temperature of sea ice at 271.35 K. where TERM00151 is the freezing temperature of sea ice at 271.35 K.

 Heat flux in the     TERM00152 is usually zero while the TERM00153 is usually zero,
 It can be given from the outside.
 It is used in the case of flux correction considering oceanic heat transport.

2. using this heat flux and heat capacity
 As with the land surface, determine the change in temperature (TERM00154).

The melting of the sea ice surface is treated in the same way as snow.
     `MODULE:[SEAFLX]`

 First, I'll set the melting value, TERM00155, to
 When the     TERM00156 ,

     > EQ=00052.

 When the     TERM00157 ,

     > EQ=00053.

 Estimate in ,
 However, if it has melted completely, set the value to TERM00158 and compensate for the heat.

     > EQ=00054.

 Varying the thickness of the ice,

     > EQ=00055.

 Then, vary the heat capacity correspondingly.

     > EQ=00056.

The next step is to consider the growth process from the bottom of the sea ice.

     1. when there is no sea ice (TERM00159)

 When the         TERM00160 ,

         > EQ=00057.

 When the         TERM00161 ,

         > EQ=00058.

 Estimate in .
 When it is positive, sea ice is produced.
 Here, TERM00162 is TERM00163 is TERM00164 K or less
 Note that it is positive when the

         > EQ=00070.
         > EQ=00070.
         > EQ=00070.

     2. when the sea ice is already present (TERM00165)

 Heat fluxes from the seawater beneath the sea ice to the bottom of the sea ice.

         > EQ=00059.

 Estimate in .
 The difference between         TERM00166 and the heat flux from the ocean to the top of TERM00167
 Used for the growth or melting of sea ice.

         > EQ=00060.

 So..,

         > EQ=00071.
         > EQ=00071.
         > EQ=00071.

5. give an external reference temperature of TERM00168
 You can nudging it.

     > EQ=00061.

 This is a heat flux

     > EQ=00062.

 The equivalent of giving a .

 To do     flux correction,
 Provide the appropriate TERM00169 and perform nudging,
 Remember the     TERM00170,
 You can give it to me as TERM00171.
