## Features and structure of the model

### Basic Features of the Model.

The CCSR/NIES AGCM is a physical description of the global three-dimensional atmosphere,
It is a numerical model for computing the time evolution of a system as an initial value problem.

The data to be inputted are as follows.

 - Initial data for each forecast variable (horizontal wind speed, temperature, surface pressure, specific humidity, cloud liquid water content, and surface volume)

 - Boundary condition data (surface elevation, surface condition, sea surface temperature, etc.)

 - Various parameters of the model (atmospheric components, physical process parameters, etc.)

On the other hand, the output looks like the following.

 - Data for each forecast parameter and diagnostic parameter, for each time or time average

 - Initial data to be used for continuous execution (restart data)

 - Progress and various diagnostic messages

Here, the predictor variable is the differential equation of time evolution, which is integrated in time by
The data is obtained as a time series,
A diagnostic variable is defined as a set of predictor variables, boundary conditions and parameters
It is a quantity calculated by some method that does not include time integration.

To be more specific ,
The model is basically a solution to the following equation (the prediction equation).

     EQ=00004.    --- (1)
     EQ=00004.     --- (2)
     EQ=00004.     --- (3)
     EQ=00004.     --- (4)
     EQ=00004.     --- (5)
     EQ=00004.     --- (6)

Where, TERM00000, TERM00000 is,
Easterly wind, north-south wind, temperature, surface pressure, specific humidity, etc., respectively
It is a forecast variable with a two- or three-dimensional distribution, such as
The right-hand side is the term that gives rise to the time variation of each of those forecast variables.
This time-varying term TERM00001,TERM00001 is ,
It is calculated based on the predictor variables TERM00002 and TERM00002,
The terms such as advection due to atmospheric motion represented by TERM00003 and TERM00004 (the term of TERM00005 in the above formula), and
The term "cloud and radiation" can be broadly divided into two categories: the term by each process, such as cloud and radiation, and the term by each process (the term in the appendix TERM00006).
The former is called the dynamic process and the latter is called the physical process.

The main part of the time-varying term of a mechanical process is the advection term,
The accurate estimation of the spatial differentiation is important in its calculation.
In CCSR/NIES AGCM, the calculation of the horizontal differential term
We use spherical harmonic function expansion.
The physical processes, on the other hand, are energy conversions due to the phase change of water and radiation absorption and injection,
The effects of small-scale atmospheric motion linked to them,
The effects of various processes on the surface of the earth, including the effects of ,
Expressing with parameters in a simple model
(parameterization) is important.

The time integration of the predictive equation is ,
(1) etc.
This is done by approximating the left-hand side by a difference. For example,

     EQ=00000.     --- (7)

By making ,

     EQ=00001.    --- (8)

That would be.
Here, TERM00007 is a function of the forecast variables TERM00008, TERM00008, etc,
Depending on which time forecast variables are used in that calculation to evaluate TERM00009,
There are various possible time difference schemes.
In the CCSR/NIES AGCM ,
Euler method that uses the values from TERM00010 as they are,
The leap frog method using the values from TERM00011,
The implicit method using (approximate) values in TERM00012 is used together.

In the CCSR/NIES AGCM
The time integration of the predictors is done separately for mechanical and physical processes.
First, the mechanics term is basically a leap frog,

     EQ=00002.     --- (9)

However, some terms are treated as implicit. but some terms are treated as implicit.
In the physical process ,
Based on the results of integrating the mechanics terms,
Using a combination of the Euler and implicit methods,

     EQ=00003.     --- (10)

I'm looking for.
Here, TERM00013 in (8) is
Note that it has been replaced by TERM00014.

### Model Execution Flow.

The flow of model execution in brief is as follows.
\is the name of the relevant subroutine.

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

The predictor variables are as follows.
Parentheses are the coordinate system and TERM00015 and TERM00015 are the coordinates, respectively,
Longitude, latitude, dimensionless pressure TERM00016, indicating vertical depth.
\The entries in the list are in units.

 - TAB00000:0.0
 east-west wind speed

 - TAB00000:0.1
     TERM00017 (TERM00018,TERM00018)

 - TAB00000:0.2
     \The "m/score

 - TAB00000:1.0
 north-south wind speed

 - TAB00000:1.1
     TERM00019 (TERM00020,TERM00020)

 - TAB00000:1.2
     \The "m/score

 - TAB00000:2.0
 atmospheric temperature

 - TAB00000:2.1
     TERM00021 (TERM00022,TERM00022)

 - TAB00000:2.2
     \K.L.A.[K.R.I.E.D.]

 - TAB00000:3.0
 surface pressure

 - TAB00000:3.1
     TERM00023 (TERM00024,TERM00024)

 - TAB00000:3.2
     The "hPa\\

 - TAB00000:4.0
 specific humidity

 - TAB00000:4.1
     TERM00025 (TERM00026,TERM00026)

 - TAB00000:4.2
     [kg/kg\\]

 - TAB00000:5.0
 Cloud water mixing ratio

 - TAB00000:5.1
     TERM00027 (TERM00028,TERM00028)

 - TAB00000:5.2
     [kg/kg\\]

 - TAB00000:6.0
 underground temperature

 - TAB00000:6.1
     TERM00029 (TERM00030,TERM00030)

 - TAB00000:6.2
     \K.L.A.[K.R.I.E.D.]

 - TAB00000:7.0
 subterranean moisture

 - TAB00000:7.1
     TERM00031 (TERM00032,TERM00032)

 - TAB00000:7.2
     \The "m/m\

 - TAB00000: 8.0
 amount of snowfall

 - TAB00000:8.1
     TERM00033 (TERM00034,TERM00034)

 - TAB00000:8.2


 - TAB00000:9.0
 sea-ice thickness

 - TAB00000:9.1
     TERM00036 (TERM00037,TERM00037)

 - TAB00000:9.2
     \\0.25\\0.25\0.25\0.25\0.25\0.25\0.25\0.25\0.25\0.25\0.25\0.00}.

However, the sea ice thickness is usually only a predictor in the mixed-layer coupled model.
In addition, the ground temperature is also higher in the oceans not covered by sea ice
Normally, it is not a predictor variable.
Also, in the CCSR/NIES AGCM, TERM00038 and TERM00039 are not independent variables,
In fact, TERM00040 is the forecast variable.

Of these,
The surface and subsurface related quantities TERM00041,TERM00041 are
At the same time it only stores the amount of one step, but,
The atmospheric quantities TERM00042,TERM00042 are,
You need to memorize the amount for two steps at a time.
This means that in the time integration of the dynamics of atmospheric quantities
This is because the leap forg method is used.

The atmospheric quantities TERM00043 and TERM00043 are ,
The main routine is a variable administered by the main routine AGCM5\.
On the other hand, the surface and subsurface quantities of TERM00044 and TERM00044
It doesn't appear in the main routine,
It is managed by the subroutine `MODULE:[PHYSCS]`, which is a subroutine for physical processes.

### The flow of time evolution of variables

We briefly summarize the flow of the model, focusing on the time evolution of the predictor variables.

1. read the initial value `MODULE:[RDSTRT,PRSTRT]`

 Initially, the quantities TERM00045 and TERM00045 related to the atmosphere are essentially
 Two sets of quantities in     TERM00046 and TERM00047 must be prepared.
 This can be prepared if you are starting from the output results of the previous model, but the
 It is not possible to prepare for a departure from normal observations and climate values.
 In that case, we start from the same value as the value of the two time steps,
 Launch the calculation using the fine TERM00048 (see below for details).

 The initial values for the atmospheric quantities TERM00049 and TERM00049 are read from ,
 This is done with `MODULE:[RDSTRT]`, called by the main routine.
 On the other hand, the initial values of the surface and underground quantities TERM00050 and TERM00050 are read from
 Conducted by `MODULE:[PRSTRT]`, called by     `MODULE:[PHYSCS]`.

2. start the time step `MODULE:[TIMSTP]`

 Forecast variables at time TERM00051 (and partly in TERM00052)
     TERM00053,TERM00053
 shall be complete.

     TERM00054 is essentially an externally given parameter,
 At regular intervals, the stability of the calculation is evaluated,
 If there is a risk of calculation instability
 reduce the size of the     TERM00055 `MODULE:[TIMSTP]`.

Set the output of the predictor variable `MODULE:[AHSTIN]`

 In the atmospheric forecast variables, the output is usually
 The value of time TERM00056 at this stage
     TERM00057,TERM00057
 It is.
 The actual output is performed by the later `MODULE:[HISTOU]`
 The timing, which is sent to the buffer here, is

4. mechanical processes `MODULE:[DYNMCS]`

 Solving for the time variation of the predicted variables due to dynamical processes.
     TERM00058,TERM00058
 Based on ,
 Value of the forecast variable in TERM00059 considering only mechanical processes
     TERM00060,TERM00060
 Ask for .

     1. convert to vorticity and divergence `MODULE:[UV2VDG, VIRTMD, HGRAD]`

 Atmospheric forecast parameters of TERM00061,TERM00061
 In order to estimate the change term due to mechanical processes, we first need to estimate
 Convert         TERM00062,TERM00062 to the grid values of vorticity and divergence TERM00063,TERM00063.
 This is because the equations of mechanics are written in terms of vorticity and divergence.
 This transformation involves a spatial derivative,
 This can be done precisely by using the spherical harmonic function expansion
         `MODULE:[UV2VDG]`.

 Furthermore, calculate the pseudotemperature TERM00064, and then set `MODULE:[VIRTMD]`,
 I still use the spherical harmonic function expansion.
 Calculates the horizontal differential of surface pressure TERM00065 `MODULE:[HGRAD]`.

     2. calculation of the time-varying term by advection `MODULE:[GRDDYN]`

 Using the values in TERM00067 of         TERM00066 and TERM00066,
 Due to horizontal and vertical advection,
 Compute some of the time-varying terms for each atmospheric variable.
 First, from the continuity equation, vertical velocity TERM00068 and
 To find the time variation term of         TERM00069 diagnostically,
 Using it, calculate the vertical advection term for TERM00070 and TERM00070.
 Furthermore, the horizontal advection fluxes of TERM00071 and TERM00071 are calculated.

     3. convert to a spectrum `MODULE:[GD2WD, TENG2W]`

 Value of grid points in TERM00072 for atmospheric forecast parameters
 From         TERM00073,TERM00073,
 Values in Spectral Space in Spherical Harmonic Function Expansion
         (However, the vorticity is changed to divergence)
         TERM00074,TERM00074
 (but, TERM00075) `MODULE:[GD2WD]`.

 In addition, the vertical advection of TERM00076 and TERM00076
 Expand the time-varying term into a spectrum.
 Also, by using the derivative in spectral space,
 Convergence of the horizontal advection flux is calculated,
 MODULE:[TENG2W]` to add to the spectral representation of the time change term.

 This allows the TERM00077,TERM00077
 Most terms in the time-varying term are obtained as spectral values.
 However, among the time-varying terms in TERM00078 and TERM00078,
 The term that depends linearly on horizontal divergence TERM00079 is
 To do time integration by the         semi-implicit method,
 It is not included in the time-varying term at this point.

     4. time integration `MODULE:[TINTGR]`

 Among the time-varying terms in         TERM00080 and TERM00080 ,
 We have added a linearly dependent term (the gravitational wave term) to the horizontally diverging TERM00081
 Treat in the         semi-implicit method,
 In addition, the horizontal diffusion of TERM00082,TERM00082
         By implicitly incorporating the
 Perform time integration of the mechanical process part.
 This allows for the
 Spectral representation of forecast values
         TERM00084,TERM00084
 is required.

     5. conversion to grid values `MODULE:[GENGD]`

 From the forecast variables in the spectral representation ,
         TERM00085,TERM00085,
 of TERM00086 considering only mechanical processes
 Grid point values for forecast values
         TERM00087,TERM00087
 .

     6. diffusion correction `MODULE:[CORDIF, CORFRC]`

 Horizontal diffusion is applied on the surface of TERM00088 and so on,
 In large areas of mountain slopes, water vapor is transported uphill,
 Causing problems such as bringing false precipitation at the top of the mountain.
 To mitigate that, etc. such that the diffusion of the TERM00089 surface is close to
 Insert corrections for TERM00090 and TERM00090 `MODULE:[CORDIF]`.

 Also, heat from friction is added to TERM00091 `MODULE:[CORFRC]`

     7. mass conservation correction `MODULE:[MASFIX]`

 Saving of the global integral values of         TERM00092 and TERM00093 is satisfied,
 and make corrections so that there will be no negative values in TERM00094.
 In addition, the correction is made so that the mass of the dry air is constant.

 When I left     DYNMCS ,
 The value of the forecast parameter in     TERM00095 has been discarded,
 Overwritten by the value of the forecast variable in     TERM00096.
 The area containing the     TERM00097 forecast variable is ,
 Only the mechanics process is considered.
 The value of the forecast parameter in     TERM00098 is entered.

5. physical process `MODULE:[PHYSCS]`

 Value of the predicted variables in TERM00099 considering only mechanical processes
     TERM00100,TERM00100
 and by adding a time-varying term from physical processes to
 The value of the forecast parameter in     TERM00101
     TERM00102,TERM00102
 Ask for .

     Calculation of the basic diagnostic variables `MODULE:[PSETUP]`

 The basic
 Find the diagnostic variables.

     2. cumulus convection, large-scale condensation `MODULE:[CUMLUS, LSCOND]`

 To find the time-varying terms of TERM00103 and TERM00103 due to cumulus convection, and `MODULE:[CUMLUS]`
 Perform time integration with `MODULE:[GDINTG]` just for that term.
 In addition, the time-varying terms of TERM00104 and TERM00104 due to large-scale condensation are found, and `MODULE:[LSCOND]`,
 Perform time integration with `MODULE:[GDINTG]` just for that term.
 Precipitation due to cumulus convection and large scale condensation TERM00105,TERM00105,
 Cloud cover (TERM00106, TERM00106, etc.) is required.
 This makes TERM00107 and TERM00107
 Adjusted value for convective condensation process
         TERM00108,TERM00108
 That would be.

     3. set the surface boundary condition `MODULE:[GNDSFC, GNDALB]`

 Set up the surface conditions with given data.
 The ground state index, sea surface temperature, etc. are set to `MODULE:[GNDSFC]`.
 Also, the surface albedo is set to be other than sea level `MODULE:[GNDALB]`.
         (The calculation of sea-surface albedo has been incorporated into the radiative flux calculation routine.)

     4. calculation of the radiation flux `MODULE:[RADCON, RADFLX]`

 Set the atmospheric data for radiation flux calculation `MODULE:[RADCON]`.
 Normally, ozone is read from a file.
 Cloud water and cloud cover are obtained by convection and large-scale condensation,
 We can also give it to you from the outside here.
 Using these and TERM00109 and TERM00109
 Shortwave and longwave radiation flux TERM00110, and
 Calculates the differential coefficient of surface temperature for         implicit calculation `MODULE:[RADFLX]`.

     5. calculation of the vertical diffuse flux `MODULE:[VDFFLX, VFTND1]`

         TERM00111,TERM00111
 with ,
 Fluxes in TERM00112 and TERM00112 by vertical diffusion and
 Calculate the differential coefficient for         implicit calculation `MODULE:[VDFFLX]`.
 In addition, the implicit solution is computed midway through the LU decomposition, `MODULE:[VFTND1]`.

     6. calculation of surface processes and time integration of underground variables `MODULE:[SURFCE]`

 Calculate the fluxes of TERM00113 and TERM00113 between the earth's surface and atmosphere,
 Considering the conduction of heat in the ground, the energy balance at the surface is
 Solve with an         implicit solution.
 This allows the surface temperature (TERM00114) to be diagnostically determined and
 Value of the ground temperature in the TERM00115
         TERM00116
 is required.
 In addition, the rate of change of the predicted variables for the first layer of the atmosphere
 Find         TERM00117,TERM00117.

 Snow accumulation and snowmelt processes are taken into account,
 The value of the snowpack in TERM00118 is determined by TERM00119,
 Taking into account the movement of water in the ground
 Ground moisture TERM00120 is required.

 In the case of the oceanic mixed layer model, the
 Ocean temperature and sea ice thickness
 The value in         TERM00121 is found by time integration.

     7. evaluation of time variation due to radial and vertical diffusion `MODULE:[VFTND2, RADTND, FLXCOR]`

 Combined radiative flux and vertical diffusion
 The rate of change of each forecast variable of the atmosphere over time.
 Seek         TERM00122,TERM00122 `MODULE:[VFTND2]`.
 In addition, isolate the contribution from the radiation from `MODULE:[RADTND]`.
 This is not directly used in the model, but ,
 For the convenience of the data output.

 Because we use the implicit method in these calculations,
 due to changes in surface temperature and atmospheric forecast variables.
 We are taking into account changes in flux.
 We'll account for that and the fluxes that break even.
 Calculate with         `MODULE:[FLXCOR]`.
 This is also for the convenience of data output.

     8. evaluation of gravitational wave resistance `MODULE:[GRAVTY]`

 Calculating the change in atmospheric momentum due to gravitational waves originating from the terrain,
 Time Dependence of TERM00123 and TERM00123 by Vertical Diffusion
 Add to         TERM00124,TERM00124.

     9. evaluation of the atmospheric pressure change term

 Considering the changes in pressure due to precipitation and evaporation,
 Find the atmospheric pressure change term TERM00125.

     10. time integration of physical processes `MODULE:[GDINTG]`

 due to radiation, vertical diffusion, surface processes, gravitational wave resistance, etc.
 The rate of change of each forecast variable of the atmosphere over time.
 Using         TERM00126,TERM00126,
 Find the value of         TERM00127 by time integration.

     11. drying convection adjustment `MODULE:[DADJST]`

 If the calculated TERM00128 and TERM00128 are unstable for dry convection
 Drying convection adjustment.

 By the above procedure,
 Value of the forecast parameters in     TERM00129
     TERM00130,TERM00130
 is required.

6. time filter `MODULE:[TFILT]`

 In order to prevent the     leap frog from causing a calculation mode,
 Apply a time filter.
     TERM00131,TERM00131
 The results of the smoothing operation using the data at the three times of
 Operate on each variable by replacing it with     TERM00132.
     (Actually, at the `MODULE:[TFILT]` stage, the
 Since the information on     TERM00133 has been erased,
 This operation is a two-step process.
 The first stage of operation is done in the mechanical process.)