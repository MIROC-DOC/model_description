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

$$
  \frac{\partial{u}}{\partial {t}}  =  \left( {\mathcal F}_x \right)_D + \left( {\mathcal F}_x \right)_P 
   \\
  \frac{\partial{v}}{\partial {t}}  =  \left( {\mathcal F}_y \right)_D + \left( {\mathcal F}_y \right)_P \\
  \frac{\partial{T}}{\partial {t}}  =  \left( Q \right)_D + \left( Q \right)_P \\
  \frac{\partial{p_S}}{\partial {t}}  =  \left( M \right)_D + \left( M \right)_P \\
  \frac{\partial{q}}{\partial {t}}  =  \left( S \right)_D + \left( S \right)_P \\
  \frac{\partial{T_g}}{\partial {t}}  =  \left( Q_g \right)_D + \left( Q_g \right)_P 
$$







Where, $u,v,T,p_S,q,T_g$ is,
Easterly wind, north-south wind, temperature, surface pressure, specific humidity, etc., respectively
It is a forecast variable with a two- or three-dimensional distribution, such as
The right-hand side is the term that gives rise to the time variation of each of those forecast variables.
This time-varying term ${\mathcal F}_x,{\mathcal F}_y,Q,S,Q_g$ is ,
It is calculated based on the predictor variables $u,v,T,p_S,q,T_g$,
The terms such as advection due to atmospheric motion represented by $u$ and $v$ (the term of $D$ in the above formula), and
The term "cloud and radiation" can be broadly divided into two categories: the term by each process, such as cloud and radiation, and the term by each process (the term in the appendix $P$).
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

$$
  \frac{\partial{q}}{\partial {t}} \rightarrow \frac{q^{t+\Delta t} - q^{t}}{\Delta t}
$$


By making ,

$$
  q^{t+\Delta t} = q^{t} 
       + \Delta t \left[ \left( S \right)_D + \left( S \right)_P  \right]
$$


That would be.
Here, $S$ is a function of the forecast variables $u,v,T,p_S,q$, etc,
Depending on which time forecast variables are used in that calculation to evaluate $S$,
There are various possible time difference schemes.
In the CCSR/NIES AGCM ,
Euler method that uses the values from $t$ as they are,
The leap frog method using the values from $t+\Delta t/2$,
The implicit method using (approximate) values in $t+\Delta t$ is used together.

In the CCSR/NIES AGCM
The time integration of the predictors is done separately for mechanical and physical processes.
First, the mechanics term is basically a leap frog,

$$
  \tilde{q}^{t+\Delta t} = q^{t-\Delta t} + 2 \Delta t \left( S \right)_D^{t}
$$


However, some terms are treated as implicit. but some terms are treated as implicit.
In the physical process ,
Based on the results of integrating the mechanics terms,
Using a combination of the Euler and implicit methods,

$$
  q^{t+\Delta t} = \tilde{q}^{t+\Delta t} + 2 \Delta t \left( S \right)_P
$$


I'm looking for.
Here, $\Delta t$ in (8) is
Note that it has been replaced by $2 \Delta t$.

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
Parentheses are the coordinate system and $\lambda,\varphi,\sigma, z$ are the coordinates, respectively,
Longitude, latitude, dimensionless pressure $\sigma$, indicating vertical depth.
\The entries in the list are in units.

| Header0 | Header1 | Header2 |
| ------- | ------- | ------- |
| east-west wind speed | $u$ ($\lambda,\varphi,\sigma$) | \The "m/score |
| north-south wind speed | $v$ ($\lambda,\varphi,\sigma$) | \The "m/score |
| atmospheric temperature | $T$ ($\lambda,\varphi,\sigma$) | \K.L.A.[K.R.I.E.D.] |
| surface pressure | $p_S$ ($\lambda,\varphi$) | The "hPa\\ |
| specific humidity | $q$ ($\lambda,\varphi,\sigma$) | [kg/kg\\] |
| Cloud water mixing ratio | $l$ ($\lambda,\varphi,\sigma$) | [kg/kg\\] |
| underground temperature | $T_g$ ($\lambda,\varphi,z$) | \K.L.A.[K.R.I.E.D.] |
| subterranean moisture | $W_g$ ($\lambda,\varphi,z$) | \The "m/m\ |
| amount of snowfall | $W_y$ ($\lambda,\varphi$) |  |
| sea-ice thickness | $h_I$ ($\lambda,\varphi$) | \\0.25\\0.25\0.25\0.25\0.25\0.25\0.25\0.25\0.25\0.25\0.25\0.00}. |

However, the sea ice thickness is usually only a predictor in the mixed-layer coupled model.
In addition, the ground temperature is also higher in the oceans not covered by sea ice
Normally, it is not a predictor variable.
Also, in the CCSR/NIES AGCM, $q$ and $l$ are not independent variables,
In fact, $q+l$ is the forecast variable.

Of these,
The surface and subsurface related quantities $T_g, W_g, W_y, h_I$ are
At the same time it only stores the amount of one step, but,
The atmospheric quantities $u, v, T, p_S, q, l$ are,
You need to memorize the amount for two steps at a time.
This means that in the time integration of the dynamics of atmospheric quantities
This is because the leap forg method is used.

The atmospheric quantities $u, v, T, p_S, q, l$ are ,
The main routine is a variable administered by the main routine AGCM5\.
On the other hand, the surface and subsurface quantities of $T_g, W_g, W_y, h_I$
It doesn't appear in the main routine,
It is managed by the subroutine `MODULE:[PHYSCS]`, which is a subroutine for physical processes.

### The flow of time evolution of variables

We briefly summarize the flow of the model, focusing on the time evolution of the predictor variables.

1. read the initial value `MODULE:[RDSTRT,PRSTRT]`

 Initially, the quantities $u, v, T, p_S, q, l$ related to the atmosphere are essentially
 Two sets of quantities in     $t$ and $t-\Delta t$ must be prepared.
 This can be prepared if you are starting from the output results of the previous model, but the
 It is not possible to prepare for a departure from normal observations and climate values.
 In that case, we start from the same value as the value of the two time steps,
 Launch the calculation using the fine $\Delta t$ (see below for details).

 The initial values for the atmospheric quantities $u, v, T, p_S, q, l$ are read from ,
 This is done with `MODULE:[RDSTRT]`, called by the main routine.
 On the other hand, the initial values of the surface and underground quantities $T_g, W_g, W_y, h_I$ are read from
 Conducted by `MODULE:[PRSTRT]`, called by     `MODULE:[PHYSCS]`.

2. start the time step `MODULE:[TIMSTP]`

 Forecast variables at time $t$ (and partly in $t-\Delta t$)
     $u^{t}, u^{t-\Delta t}, v^{t}, v^{t-\Delta t},
T^{t}, T^{t-\Delta t}, p_S^{t}, p_S^{t-\Delta t},
q^{t}, q^{t-\Delta t}, l^{t}, l^{t-\Delta t},
T_g^{t}, W_g^{t}, W_y^{t}$
 shall be complete.

     $\Delta t$ is essentially an externally given parameter,
 At regular intervals, the stability of the calculation is evaluated,
 If there is a risk of calculation instability
 reduce the size of the     $\Delta t$ `MODULE:[TIMSTP]`.

Set the output of the predictor variable `MODULE:[AHSTIN]`

 In the atmospheric forecast variables, the output is usually
 The value of time $t$ at this stage
     $u^{t}, v^{t}, T^{t}, p_S^{t}, q^{t}, l^{t}$
 It is.
 The actual output is performed by the later `MODULE:[HISTOU]`
 The timing, which is sent to the buffer here, is

4. mechanical processes `MODULE:[DYNMCS]`

 Solving for the time variation of the predicted variables due to dynamical processes.
     $u^{t}, u^{t-\Delta t}, v^{t}, v^{t-\Delta t},
T^{t}, T^{t-\Delta t}, p_S^{t}, p_S^{t-\Delta t},
q^{t}, q^{t-\Delta t}, l^{t}, l^{t-\Delta t}$
 Based on ,
 Value of the forecast variable in $t+\Delta t$ considering only mechanical processes
     $\hat{u}^{t+\Delta t}, \hat{v}^{t+\Delta t}, 
\hat{T}^{t+\Delta t}, \hat{p_S}^{t+\Delta t}, 
\hat{q}^{t+\Delta t}, \hat{l}^{t+\Delta t}$
 Ask for .

     1. convert to vorticity and divergence `MODULE:[UV2VDG, VIRTMD, HGRAD]`

 Atmospheric forecast parameters of $u, v, T, p_S, q, l$
 In order to estimate the change term due to mechanical processes, we first need to estimate
 Convert         $u^{t}, v^{t}$ to the grid values of vorticity and divergence $\zeta^{t},D^{t}$.
 This is because the equations of mechanics are written in terms of vorticity and divergence.
 This transformation involves a spatial derivative,
 This can be done precisely by using the spherical harmonic function expansion
         `MODULE:[UV2VDG]`.

 Furthermore, calculate the pseudotemperature $T_v^{t}$, and then set `MODULE:[VIRTMD]`,
 I still use the spherical harmonic function expansion.
 Calculates the horizontal differential of surface pressure $\nabla \ln p_S$ `MODULE:[HGRAD]`.

     2. calculation of the time-varying term by advection `MODULE:[GRDDYN]`

 Using the values in $t$ of         $u, v, T, p_S, q, l$,
 Due to horizontal and vertical advection,
 Compute some of the time-varying terms for each atmospheric variable.
 First, from the continuity equation, vertical velocity $\dot{\sigma}$ and
 To find the time variation term of         $p_S$ diagnostically,
 Using it, calculate the vertical advection term for $u, v, T, q, l$.
 Furthermore, the horizontal advection fluxes of $u, v, T, q, l$ are calculated.

     3. convert to a spectrum `MODULE:[GD2WD, TENG2W]`

 Value of grid points in $t-\Delta t$ for atmospheric forecast parameters
 From         $u^{t}, v^{t}, T^{t}, p_S^{t}, q^{t}, l^{t}$,
 Values in Spectral Space in Spherical Harmonic Function Expansion
         (However, the vorticity is changed to divergence)
         $\tilde{\zeta}^{t}, \tilde{D}^{t}, \tilde{T}^{t}, 
\tilde{\pi}^{t}, \tilde{q}^{t}, \tilde{l}^{t}$
 (but, $\pi \equiv \ln p_S$) `MODULE:[GD2WD]`.

 In addition, the vertical advection of $u, v, T, p_S, q, l$
 Expand the time-varying term into a spectrum.
 Also, by using the derivative in spectral space,
 Convergence of the horizontal advection flux is calculated,
 MODULE:[TENG2W]` to add to the spectral representation of the time change term.

 This allows the $\zeta, D, T, \pi, q, l$
 Most terms in the time-varying term are obtained as spectral values.
 However, among the time-varying terms in $\zeta, D, T, \pi$,
 The term that depends linearly on horizontal divergence $D$ is
 To do time integration by the         semi-implicit method,
 It is not included in the time-varying term at this point.

     4. time integration `MODULE:[TINTGR]`

 Among the time-varying terms in         $\zeta, D, T, \pi$ ,
 We have added a linearly dependent term (the gravitational wave term) to the horizontally diverging $D$
 Treat in the         semi-implicit method,
 In addition, the horizontal diffusion of $\zeta, D, T, q, l$
         By implicitly incorporating the
 Perform time integration of the mechanical process part.
 This allows for the
 Spectral representation of forecast values
         $\tilde{\zeta}^{t+\Delta t}, \tilde{D}^{t+\Delta t}, 
\tilde{T}^{t+\Delta t}, \tilde{\pi}^{t+\Delta t}, 
\tilde{q}^{t+\Delta t}, \tilde{l}^{t+\Delta t}$
 is required.

     5. conversion to grid values `MODULE:[GENGD]`

 From the forecast variables in the spectral representation ,
         $u, v, T, p_S, q, l$,
 of $t+\Delta t$ considering only mechanical processes
 Grid point values for forecast values
         $\hat{u}^{t+\Delta t}, \hat{v}^{t+\Delta t}, 
\hat{T}^{t+\Delta t}, \hat{p_S}^{t+\Delta t}, 
\hat{q}^{t+\Delta t}, \hat{l}^{t+\Delta t}$
 .

     6. diffusion correction `MODULE:[CORDIF, CORFRC]`

 Horizontal diffusion is applied on the surface of $\sigma$ and so on,
 In large areas of mountain slopes, water vapor is transported uphill,
 Causing problems such as bringing false precipitation at the top of the mountain.
 To mitigate that, etc. such that the diffusion of the $p$ surface is close to
 Insert corrections for $T,q,l$ `MODULE:[CORDIF]`.

 Also, heat from friction is added to $\hat{T}$ `MODULE:[CORFRC]`

     7. mass conservation correction `MODULE:[MASFIX]`

 Saving of the global integral values of         $q$ and $l$ is satisfied,
 and make corrections so that there will be no negative values in $q$.
 In addition, the correction is made so that the mass of the dry air is constant.

 When I left     DYNMCS ,
 The value of the forecast parameter in     $t-\Delta t$ has been discarded,
 Overwritten by the value of the forecast variable in     $t$.
 The area containing the     $t$ forecast variable is ,
 Only the mechanics process is considered.
 The value of the forecast parameter in     $t+\Delta t$ is entered.

5. physical process `MODULE:[PHYSCS]`

 Value of the predicted variables in $t+\Delta t$ considering only mechanical processes
     $\hat{u}^{t+\Delta t}, \hat{v}^{t+\Delta t}, 
\hat{T}^{t+\Delta t}, \hat{p_S}^{t+\Delta t}, 
\hat{q}^{t+\Delta t}, \hat{l}^{t+\Delta t}$
 and by adding a time-varying term from physical processes to
 The value of the forecast parameter in     $t+\Delta t$
     $u^{t+\Delta t}, v^{t+\Delta t}, 
T^{t+\Delta t}, p_S^{t+\Delta t}, 
q^{t+\Delta t}, l^{t+\Delta t}$
 Ask for .

     Calculation of the basic diagnostic variables `MODULE:[PSETUP]`

 The basic
 Find the diagnostic variables.

     2. cumulus convection, large-scale condensation `MODULE:[CUMLUS, LSCOND]`

 To find the time-varying terms of $T, q, l$ due to cumulus convection, and `MODULE:[CUMLUS]`
 Perform time integration with `MODULE:[GDINTG]` just for that term.
 In addition, the time-varying terms of $T, q, l$ due to large-scale condensation are found, and `MODULE:[LSCOND]`,
 Perform time integration with `MODULE:[GDINTG]` just for that term.
 Precipitation due to cumulus convection and large scale condensation $P_c, P_l$,
 Cloud cover ($C_c, C_l$, etc.) is required.
 This makes $T, q, l$
 Adjusted value for convective condensation process
         $\hat{T}^{t+\Delta t,a}, 
\hat{q}^{t+\Delta t,a}, \hat{l}^{t+\Delta t,a}$
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
 Using these and $\hat{T}^{t+\Delta t,a}, \hat{q}^{t+\Delta t,a}$
 Shortwave and longwave radiation flux $F_R$, and
 Calculates the differential coefficient of surface temperature for         implicit calculation `MODULE:[RADFLX]`.

     5. calculation of the vertical diffuse flux `MODULE:[VDFFLX, VFTND1]`

         $\hat{u}^{t+\Delta t}, \hat{v}^{t+\Delta t}, 
\hat{T}^{t+\Delta t,a}, \hat{q}^{t+\Delta t,a}, \hat{l}^{t+\Delta t,a}$
 with ,
 Fluxes in $u, v, T, q, l$ by vertical diffusion and
 Calculate the differential coefficient for         implicit calculation `MODULE:[VDFFLX]`.
 In addition, the implicit solution is computed midway through the LU decomposition, `MODULE:[VFTND1]`.

     6. calculation of surface processes and time integration of underground variables `MODULE:[SURFCE]`

 Calculate the fluxes of $u, v, T, q $ between the earth's surface and atmosphere,
 Considering the conduction of heat in the ground, the energy balance at the surface is
 Solve with an         implicit solution.
 This allows the surface temperature ($T_s$) to be diagnostically determined and
 Value of the ground temperature in the $t+\Delta t$
         $T_g^{t+\Delta t}$
 is required.
 In addition, the rate of change of the predicted variables for the first layer of the atmosphere
 Find         $F_{x,1}, F_{y,1}, Q_1, S_1$.

 Snow accumulation and snowmelt processes are taken into account,
 The value of the snowpack in $t+\Delta t$ is determined by $W_y^{t+\Delta t}$,
 Taking into account the movement of water in the ground
 Ground moisture $W_g^{t+\Delta t}$ is required.

 In the case of the oceanic mixed layer model, the
 Ocean temperature and sea ice thickness
 The value in         $t+\Delta t$ is found by time integration.

     7. evaluation of time variation due to radial and vertical diffusion `MODULE:[VFTND2, RADTND, FLXCOR]`

 Combined radiative flux and vertical diffusion
 The rate of change of each forecast variable of the atmosphere over time.
 Seek         ${\mathcal F}_x, {\mathcal F}_y, Q, S$ `MODULE:[VFTND2]`.
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
 Time Dependence of $u, v$ by Vertical Diffusion
 Add to         ${\mathcal F}_x, {\mathcal F}_y$.

     9. evaluation of the atmospheric pressure change term

 Considering the changes in pressure due to precipitation and evaporation,
 Find the atmospheric pressure change term $M$.

     10. time integration of physical processes `MODULE:[GDINTG]`

 due to radiation, vertical diffusion, surface processes, gravitational wave resistance, etc.
 The rate of change of each forecast variable of the atmosphere over time.
 Using         ${\mathcal F}_x, {\mathcal F}_y, Q, M, S$,
 Find the value of         $t+\Delta t$ by time integration.

     11. drying convection adjustment `MODULE:[DADJST]`

 If the calculated $T, q, l$ are unstable for dry convection
 Drying convection adjustment.

 By the above procedure,
 Value of the forecast parameters in     $t+\Delta t$
     $u^{t+\Delta t}, v^{t+\Delta t}, 
T^{t+\Delta t}, p_S^{t+\Delta t}, 
q^{t+\Delta t}, l^{t+\Delta t}$
 is required.

6. time filter `MODULE:[TFILT]`

 In order to prevent the     leap frog from causing a calculation mode,
 Apply a time filter.
     $u^{t-\Delta t}, u^{t}, u^{t+\Delta t}$
 The results of the smoothing operation using the data at the three times of
 Operate on each variable by replacing it with     $u^{t}$.
     (Actually, at the `MODULE:[TFILT]` stage, the
 Since the information on     $u^{t-\Delta t}$ has been erased,
 This operation is a two-step process.
 The first stage of operation is done in the mechanical process.)
