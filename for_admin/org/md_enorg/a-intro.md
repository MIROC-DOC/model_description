## Features and structure of the model

### Basic Features of the Model.

The CCSR/NIES AGCM is a numerical model for describing the global three-dimensional atmosphere based on physical laws and calculating the time evolution of the system as an initial value problem.

The data to be inputted are as follows.

 - Initial data for each forecast variable (horizontal wind speed, temperature, surface pressure, specific humidity, cloud liquid water content, and surface volume)

 - Boundary condition data (surface elevation, surface condition, sea surface temperature, etc.)

 - Various parameters of the model (atmospheric components, physical process parameters, etc.)

On the other hand, the output looks like the following.

 - Data for each forecast parameter and diagnostic parameter, for each time or time average

 - Initial data to be used for continuous execution (restart data)

 - Progress and various diagnostic messages

The predictor is the data obtained as a time series by integrating the differential equation of time evolution, and the diagnostic variable is the quantity calculated from the predictor, the boundary conditions and the parameters by some method that does not include time integration.

More specifically, the model basically finds the solution to the following equations (forecast equations).

     EQ=00004.
     EQ=00004.
     EQ=00004.
     EQ=00004.
     EQ=00004.
     EQ=00004.

Here, TERM00000 and TERM00000 are two-dimensional and three-dimensional forecast variables such as wind, north-south wind, temperature, surface pressure, specific humidity, and surface state amount, respectively, and the right-hand side is a term that causes time variation of each forecast variable. The terms TERM00001 and TERM00001 are calculated based on the forecast variables TERM00002 and TERM00002, but the terms TERM00003 and TERM00004, such as advection due to the motion of the atmosphere (the terms of the terminal terminal number 5 in the above equation), and the terms TERM00005, such as cloud and radiation, are not included in the time-varying variables. There are two main types of terms, one for each process in the process of The former is called the mechanical process, and the latter is called the physical process.

The advection term is the main part of the time-varying term in mechanical processes, and the accurate estimation of the spatial derivative is important in its calculation. The CCSR/NIES AGCM utilizes the spherical harmonic expansion to calculate the horizontal differential term. On the other hand, it is important for physical processes to be represented in a simple model with parameters (parameterization), such as energy conversions due to the phase change of water, radiative absorption and emission, the effects of small-scale atmospheric motions, and the effects of various processes on the ground surface.

The time integration of the forecasting equation is done by approximating the left-hand side of (1) etc. by the difference. For example,

     EQ=00000.

By making ,

     EQ=00001.

where TERM00007 is a function of the forecast variables TERM00008 and TERM00008. Although TERM00007 is a function of the forecast variables TERM00008, TERM00008, and so on, there are various time difference schemes that can be used in this calculation depending on the time of day the forecast variables are used to evaluate TERM00009. The CCSR/NIES AGCM uses the Euler method, which uses the value of the TERM00010 as it is, the leap frog method, which uses the value of the TERM00011, and the implicit method, which uses the (approximate) value of the TERM00012.

In the CCSR/NIES AGCM, the time integration of the predictors is done separately for the mechanical and physical processes. The first term of the dynamics is basically a leap frog,

     EQ=00002.

However, some terms are treated as implicit. with the exception of some terms which are treated as implicit. In the physical process, based on the results of integrating the mechanical terms, the Euler and implicit methods are used together,

     EQ=00003.

in (8). Note that TERM00013 in (8) is replaced by TERM00014.

### Model Execution Flow.

The flow of the model execution is briefly shown below. The entries in the index [[\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.066}.} are the names of the corresponding subroutine.

1. set the parameters of an experiment, coordinates, etc. `MODULE:[SETPAR,PCONST,SETCOR,SETZS]`

2. read the initial values of the predictor variable `MODULE:[RDSTRT]`

3. start the time step `MODULE:[TIMSTP]`

4. perform time integration by mechanical processes `MODULE:[DYNMCS]`

5. perform time integration by physical processes `MODULE:[PHYSCS]`

6. advance the time `MODULE:[STPTIM, TFILT]`

Output the data if necessary `MODULE:[HISTOU]`

Output the restart data if necessary `MODULE:[WRRSTR]`

9. 3\. Back to

### Predictive variables.

The predictive variables are as follows. The values in parentheses are the coordinate system, and TERM00015 and TERM00015 indicate the longitude, latitude, dimensionless pressure, TERM00016, and vertical depth, respectively. \The values in the square brackets are in units of the index.

 - TAB00001:0.0
 east-west wind speed

 - TAB00001:0.1
     TERM00017 (TERM00018,TERM00018)

 - TAB00001:0.2
     \The "m/score

 - TAB00001:1.0
 north-south wind speed

 - TAB00001:1.1
     TERM00019 (TERM00020,TERM00020)

 - TAB00001:1.2
     \The "m/score

 - TAB00001:2.0
 atmospheric temperature

 - TAB00001:2.1
     TERM00021 (TERM00022,TERM00022)

 - TAB00001:2.2
     \K.L.A.[K.R.I.E.D.]

 - TAB00001:3.0
 surface pressure

 - TAB00001:3.1
     TERM00023 (TERM00024,TERM00024)

 - TAB00001:3.2
     The "hPa\\

 - TAB00001:4.0
 specific humidity

 - TAB00001:4.1
     TERM00025 (TERM00026,TERM00026)

 - TAB00001:4.2
     [kg/kg\\]

 - TAB00001:5.0
 Cloud water mixing ratio

 - TAB00001:5.1
     TERM00027 (TERM00028,TERM00028)

 - TAB00001:5.2
     [kg/kg\\]

 - TAB00001:6.0
 underground temperature

 - TAB00001:6.1
     TERM00029 (TERM00030,TERM00030)

 - TAB00001:6.2
     \K.L.A.[K.R.I.E.D.]

 - TAB00001:7.0
 subterranean moisture

 - TAB00001:7.1
     TERM00031 (TERM00032,TERM00032)

 - TAB00001:7.2
     \The "m/m\

 - TAB00001:8.0
 amount of snowfall

 - TAB00001:8.1
     TERM00033 (TERM00034,TERM00034)

 - TAB00001:8.2


 - TAB00001:9.0
 sea-ice thickness

 - TAB00001:9.1
     TERM00036 (TERM00037,TERM00037)

 - TAB00001:9.2
     \\0.25\\0.25\0.25\0.25\0.25\0.25\0.25\0.25\0.25\0.25\0.25\0.00}.

However, the sea ice thickness is usually only a predictor in the mixed-layer coupled model. Also, subsurface temperature is not usually a predictor when the ocean is not covered by sea ice. In the CCSR/NIES AGCM, TERM00038 and TERM00039 are not independent variables; in fact, TERM00040 is the forecast variable.

Of these quantities, the quantities for the surface and the subsurface, TERM00041 and TERM00041, store only one step at a time, while the quantities for the atmosphere, TERM00042 and TERM00042, need to store two steps at a time. This is due to the fact that the leap forg method is used in the time integration of the dynamic process of the quantities related to the atmosphere.

The quantities of the atmosphere, TERM00043 and TERM00043, are variables managed by the main routine, `Administration of the Atmosphere'[AGCM5\a]`. On the other hand, the quantities relating to the earth's surface and ground, TERM00044 and TERM00044, do not appear in the main routine, but are managed by the subroutine `MODULE:[PHYSCS]` of the physical process.

### The flow of time evolution of variables

We briefly summarize the flow of the model, focusing on the time evolution of the predictor variables.

1. read the initial value `MODULE:[RDSTRT,PRSTRT]`

 Initially, the quantities TERM00045 and TERM00045 for the atmosphere must be prepared as two sets of quantities in TERM00046 and TERM00047. These quantities can be prepared when starting from the output of previous models, but cannot be prepared when starting from ordinary observations or climatic values. In that case, we will start from the same value of the two time steps and start up the calculation using the fine TERM00048 (see below for details).

 Initial values of the atmospheric quantities TERM00049 and TERM00049 are read by the `MODULE:[RDSTRT]`, which is called by the main routine. On the other hand, the initial values for the quantities of TERM00050 and TERM00050 for the earth's surface and ground are read by `MODULE:[PRSTRT]`, which is called by `MODULE:[PHYSCS]`.

2. start the time step `MODULE:[TIMSTP]`

 Forecast variables at time TERM00051 (and partly in TERM00052)
     TERM00053,TERM00053
 shall be complete.

     Although TERM00054 is basically an externally given parameter, the stability of the calculation is evaluated at regular intervals and TERM00055 should be reduced if the calculation is likely to be unstable.

Set the output of the predictor variable `MODULE:[AHSTIN]`

 In the atmospheric forecast variables, what is usually output is the value of time TERM00056 at this stage, TERM00057, and TERM00057. The actual output is done at the later timing of `MODULE:[HISTOU]`, but it is sent to the buffer at this point.

4. mechanical processes `MODULE:[DYNMCS]`

 Solving for the time variation of the predicted variables due to dynamical processes.
     TERM00058,TERM00058
 The value of the predicted variable in TERM00059, considering only mechanical processes, based on
     TERM00060,TERM00060
 Ask for .

     1. convert to vorticity and divergence `MODULE:[UV2VDG, VIRTMD, HGRAD]`

 In order to estimate the change terms of the atmospheric predictors TERM00061 and TERM00061 due to mechanical processes, TERM00062 and TERM00062 are first converted to grid values of vorticity and divergence, TERM00063 and TERM00063. This is because the dynamics equations are written in terms of vorticity and divergence. Although this transformation involves a spatial derivative, it can be performed precisely by using the spherical harmonic expansion `MODULE:[UV2VDG]`.

 Furthermore, we calculate the pseudotemperature TERM00064 and the horizontal differential of surface pressure TERM00065 using `MODULE:[VIRTMD]`, also using the spherical harmonic expansion function, and `MODULE:[HGRAD]`.

     2. calculation of the time-varying term by advection `MODULE:[GRDDYN]`

 Using the values in         TERM00066 and TERM00066 at TERM00067, a part of the time-varying terms for each atmospheric variable is calculated by using the values in TERM00066 and TERM00066 for horizontal and vertical advection. First, the time-varying terms of vertical velocity TERM00068 and TERM00069 are diagnostically obtained from successive equations, and then the vertical advection terms of TERM00070 and TERM00070 are calculated using the time-varying terms. Furthermore, calculate the horizontal advection fluxes in TERM00071 and TERM00071.

     3. convert to a spectrum `MODULE:[GD2WD, TENG2W]`

 Value of grid points in TERM00072 for atmospheric forecast variables from TERM00073 and TERM00073 in the spectral space of spherical harmonic function expansion (but converted to vorticity divergence)
         TERM00074,TERM00074
 (but, TERM00075) `MODULE:[GD2WD]`.

 In addition, the time-varying terms of TERM00076 and TERM00076 are expanded into spectra. We also calculate the convergence of the horizontal advection fluxes by using the derivative in spectral space and add them to the spectral representation of the time-varying term `MODULE:[TENG2W]`.

 With this, most of the time-varying terms in TERM00077 and TERM00077 can be obtained as spectral values. However, among the time-varying terms in TERM00078 and TERM00078, those that depend on the horizontally diverging TERM00079 are not included in the time-varying term at this point because the time integration is performed by the semi-implicit method.

     4. time integration `MODULE:[TINTGR]`

 Among the time-varying terms in         TERM00080 and TERM00080, a term that depends linearly on the horizontal divergence TERM00081 (the gravitational wave term) is treated by the semi-implicit method, and furthermore, by implicitly incorporating the horizontal diffusion of TERM00082 and TERM00082, the mechanical process part of Time integration is performed. This allows for a spectral representation of the predicted value of TERM00083 considering only the mechanical processes
         TERM00084,TERM00084
 is required.

     5. conversion to grid values `MODULE:[GENGD]`

 Grid values for the forecast values of TERM00085, TERM00085, and TERM00086 considering only mechanical processes from a spectral representation of the forecast variables
         TERM00087,TERM00087
 .

     6. diffusion correction `MODULE:[CORDIF, CORFRC]`

 Horizontal diffusion is applied in the plane of TERM00088, but in large slopes, it causes problems such as upward transport of water vapor and false precipitation at the tops of mountains. To mitigate this problem, a correction has been added for TERM00090 and TERM00090 to be close to the diffusion of TERM00089 surface, such as `MODULE:[CORDIF]`.

 Also, heat from friction is added to TERM00091 `MODULE:[CORFRC]`

     7. mass conservation correction `MODULE:[MASFIX]`

 Corrections are made so that the global integral values of         TERM00092 and TERM00093 are preserved and the negative value of TERM00094 is eliminated. Furthermore, corrections are made so that the mass of dry air remains constant.

 After exiting     DYNMCS, the value of the forecaster variable in TERM00095 is discarded and is overwritten by the value of the forecaster variable in TERM00096. The area of the forecaster variable in TERM00097 is replaced by the value of the forecaster variable in TERM00098 which only takes into account the mechanical processes.

5. physical process `MODULE:[PHYSCS]`

 Value of the predicted variables in TERM00099 considering only mechanical processes
     TERM00100,TERM00100
 and by adding a time-varying term from physical processes to the value of the predicted variable in TERM00101
     TERM00102,TERM00102
 Ask for .

     Calculation of the basic diagnostic variables `MODULE:[PSETUP]`

 Find the basic diagnostic variables such as pseudotemperature, barometric pressure at each level, and altitude.

     2. cumulus convection, large-scale condensation `MODULE:[CUMLUS, LSCOND]`

 Calculates the time-varying terms of TERM00103 and TERM00103 due to cumulus convection and integrates them with `MODULE:[CUMLUS]` and the time integration with `MODULE:[GDINTG]` using the term alone. Also, the time-varying terms of TERM00104 and TERM00104 due to large-scale condensation are found and integrated by `MODULE:[LSCOND]`, and the time integration is performed with `MODULE:[GDINTG]` using only the term `MODULE:[GDINTG]`. Precipitation due to cumulus convection and large-scale condensation (TERM00105,TERM00105), cloud cover (TERM00106,TERM00106), and so on can be obtained. This gives the values of TERM00107 and TERM00107 adjusted for convective condensation processes (TERM00108 and TERM00108).

     3. set the surface boundary condition `MODULE:[GNDSFC, GNDALB]`

 The state of the earth surface is set according to a given data. The ground state index, the sea surface temperature, and so on are set `MODULE:[GNDSFC]`. The surface albedo is set according to the data given by `MODULE:[GNDALB]`. (The calculation of the sea-surface albedo is incorporated into the routine for calculating the radiation flux.)

     4. calculation of the radiation flux `MODULE:[RADCON, RADFLX]`

 Set the atmospheric composition data for radiation flux calculation `MODULE:[RADCON]`. Usually, ozone is read from a file. The cloud water and cloud masses are obtained from the cumulus convection and large-scale condensation methods, but they can also be given here externally. Using these two files and TERM00109 and TERM00109, the differential coefficients for the surface temperature used in TERM00110 and the implicit calculation are calculated with the TERM00110 and `MODULE:[RADFLX]`.

     5. calculation of the vertical diffuse flux `MODULE:[VDFFLX, VFTND1]`

 Using         TERM00111 and TERM00111, the fluxes of TERM00112 and TERM00112 by the vertical diffusion process and the differential coefficient for implicit calculation are calculated using `MODULE:[VDFFLX]`. Furthermore, computes the implicit solution using the LU decomposition up to the middle of the process `MODULE:[VFTND1]`.

     6. calculation of surface processes and time integration of underground variables `MODULE:[SURFCE]`

 The fluxes of TERM00113 and TERM00113 between the surface and the atmosphere are calculated, and the energy balance at the ground surface is solved by using an implicit solution considering the conduction of heat in the ground. This results in obtaining the surface temperature (TERM00114) and the value of the ground temperature (TERM00116) from the surface temperature (TERM00115) diagnostically. Furthermore, the time rate of change of the predicted variables of the atmosphere in the first layer, TERM00117 and TERM00117, can be obtained.

 Considering the snow accumulation and snowmelt process, the value of snow accumulation (TERM00118) is determined and the ground moisture (TERM00120) is determined by considering the movement of water in the ground.

 When an oceanic mixed-layer model is used, the values of ocean temperature and sea ice thickness can be obtained by time integration in TERM00121.

     7. evaluation of time variation due to radial and vertical diffusion `MODULE:[VFTND2, RADTND, FLXCOR]`

 Rate of change of each forecast variable for the combined radiative flux and vertical diffusion
 Calculates         TERM00122 and TERM00122 `MODULE:[VFTND2]`. Furthermore, the contribution of radiation is separated from the model by `MODULE:[RADTND]`. This is not used directly in the model, but is done for the sake of outputting the data.

 Since we use the implicit method, we take into account the changes in fluxes due to changes in surface temperature and atmospheric variables. The fluxes are calculated by `MODULE:[FLXCOR]` to take the change in the surface temperature and atmospheric variables into account. This is also for the convenience of the data output.

     8. evaluation of gravitational wave resistance `MODULE:[GRAVTY]`

 The change in atmospheric momentum due to geological origin is calculated and added to the rates of change of TERM00123 and TERM00123 due to vertical diffusion of the atmosphere (TERM00124 and TERM00124).

     9. evaluation of the atmospheric pressure change term

 Considering the change in atmospheric pressure due to precipitation and evaporation, the atmospheric pressure change term TERM00125 is obtained.

     10. time integration of physical processes `MODULE:[GDINTG]`

 Using the rates of change of atmospheric variables such as radiation, vertical diffusion, surface processes, and gravitational wave resistance calculated above, the values in TERM00127 are integrated in time using TERM00126 and TERM00126.

     11. drying convection adjustment `MODULE:[DADJST]`

 If the calculated values of TERM00128 and TERM00128 are unstable with respect to dry convection, dry convection adjustment is applied.

 By the above procedure, the value of the forecast variable in TERM00129
     TERM00130,TERM00130
 is required.

6. time filter `MODULE:[TFILT]`

 A time filter is applied to suppress the occurrence of calculation modes by     leap frog. With the time data of TERM00131, TERM00131, and TERM00131, smoothing operations are applied to each variable to convert them to TERM00132. (Actually, since the information on TERM00133 is deleted at `MODULE:[TFILT]` stage, this operation is performed in two steps. The first operation is performed in the mechanical process.)