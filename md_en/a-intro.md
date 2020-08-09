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

$$
  \frac{\partial{u}}{\partial {t}}  =  \left( {\mathcal F}_x \right)_D + \left( {\mathcal F}_x \right)_P 
   \\
  \frac{\partial{v}}{\partial {t}}  =  \left( {\mathcal F}_y \right)_D + \left( {\mathcal F}_y \right)_P \\
  \frac{\partial{T}}{\partial {t}}  =  \left( Q \right)_D + \left( Q \right)_P \\
  \frac{\partial{p_S}}{\partial {t}}  =  \left( M \right)_D + \left( M \right)_P \\
  \frac{\partial{q}}{\partial {t}}  =  \left( S \right)_D + \left( S \right)_P \\
  \frac{\partial{T_g}}{\partial {t}}  =  \left( Q_g \right)_D + \left( Q_g \right)_P 
$$







Here, $u,v,T,p_S,q,T_g$ are two-dimensional and three-dimensional forecast variables such as wind, north-south wind, temperature, surface pressure, specific humidity, and surface state amount, respectively, and the right-hand side is a term that causes time variation of each forecast variable. The terms ${\mathcal F}_x,{\mathcal F}_y,Q,S,Q_g$ are calculated based on the forecast variables $u,v,T,p_S,q,T_g$, but the terms $u$ and $v$, such as advection due to the motion of the atmosphere (the terms of the terminal terminal number 5 in the above equation), and the terms $D$, such as cloud and radiation, are not included in the time-varying variables. There are two main types of terms, one for each process in the process of The former is called the mechanical process, and the latter is called the physical process.

The advection term is the main part of the time-varying term in mechanical processes, and the accurate estimation of the spatial derivative is important in its calculation. The CCSR/NIES AGCM utilizes the spherical harmonic expansion to calculate the horizontal differential term. On the other hand, it is important for physical processes to be represented in a simple model with parameters (parameterization), such as energy conversions due to the phase change of water, radiative absorption and emission, the effects of small-scale atmospheric motions, and the effects of various processes on the ground surface.

The time integration of the forecasting equation is done by approximating the left-hand side of (1) etc. by the difference. For example,

$$
  \frac{\partial{q}}{\partial {t}} \rightarrow \frac{q^{t+\Delta t} - q^{t}}{\Delta t}
$$


By making ,

$$
  q^{t+\Delta t} = q^{t} 
       + \Delta t \left[ \left( S \right)_D + \left( S \right)_P  \right]
$$


where $S$ is a function of the forecast variables $u,v,T,p_S,q$. Although $S$ is a function of the forecast variables $u,v,T,p_S,q$, and so on, there are various time difference schemes that can be used in this calculation depending on the time of day the forecast variables are used to evaluate $S$. The CCSR/NIES AGCM uses the Euler method, which uses the value of the $t$ as it is, the leap frog method, which uses the value of the $t+\Delta t/2$, and the implicit method, which uses the (approximate) value of the $t+\Delta t$.

In the CCSR/NIES AGCM, the time integration of the predictors is done separately for the mechanical and physical processes. The first term of the dynamics is basically a leap frog,

$$
  \tilde{q}^{t+\Delta t} = q^{t-\Delta t} + 2 \Delta t \left( S \right)_D^{t}
$$


However, some terms are treated as implicit. with the exception of some terms which are treated as implicit. In the physical process, based on the results of integrating the mechanical terms, the Euler and implicit methods are used together,

$$
  q^{t+\Delta t} = \tilde{q}^{t+\Delta t} + 2 \Delta t \left( S \right)_P
$$


in (8). Note that $\Delta t$ in (8) is replaced by $2 \Delta t$.

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

The predictive variables are as follows. The values in parentheses are the coordinate system, and $\lambda,\varphi,\sigma, z$ indicate the longitude, latitude, dimensionless pressure, $\sigma$, and vertical depth, respectively. \The values in the square brackets are in units of the index.

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

However, the sea ice thickness is usually only a predictor in the mixed-layer coupled model. Also, subsurface temperature is not usually a predictor when the ocean is not covered by sea ice. In the CCSR/NIES AGCM, $q$ and $l$ are not independent variables; in fact, $q+l$ is the forecast variable.

Of these quantities, the quantities for the surface and the subsurface, $T_g, W_g, W_y, h_I$, store only one step at a time, while the quantities for the atmosphere, $u, v, T, p_S, q, l$, need to store two steps at a time. This is due to the fact that the leap forg method is used in the time integration of the dynamic process of the quantities related to the atmosphere.

The quantities of the atmosphere, $u, v, T, p_S, q, l$, are variables managed by the main routine, `Administration of the Atmosphere'[AGCM5\a]`. On the other hand, the quantities relating to the earth's surface and ground, $T_g, W_g, W_y, h_I$, do not appear in the main routine, but are managed by the subroutine `MODULE:[PHYSCS]` of the physical process.

### The flow of time evolution of variables

We briefly summarize the flow of the model, focusing on the time evolution of the predictor variables.

1. read the initial value `MODULE:[RDSTRT,PRSTRT]`

 Initially, the quantities $u, v, T, p_S, q, l$ for the atmosphere must be prepared as two sets of quantities in $t$ and $t-\Delta t$. These quantities can be prepared when starting from the output of previous models, but cannot be prepared when starting from ordinary observations or climatic values. In that case, we will start from the same value of the two time steps and start up the calculation using the fine $\Delta t$ (see below for details).

 Initial values of the atmospheric quantities $u, v, T, p_S, q, l$ are read by the `MODULE:[RDSTRT]`, which is called by the main routine. On the other hand, the initial values for the quantities of $T_g, W_g, W_y, h_I$ for the earth's surface and ground are read by `MODULE:[PRSTRT]`, which is called by `MODULE:[PHYSCS]`.

2. start the time step `MODULE:[TIMSTP]`

 Forecast variables at time $t$ (and partly in $t-\Delta t$)
     $u^{t}, u^{t-\Delta t}, v^{t}, v^{t-\Delta t},
T^{t}, T^{t-\Delta t}, p_S^{t}, p_S^{t-\Delta t},
q^{t}, q^{t-\Delta t}, l^{t}, l^{t-\Delta t},
T_g^{t}, W_g^{t}, W_y^{t}$
 shall be complete.

     Although $\Delta t$ is basically an externally given parameter, the stability of the calculation is evaluated at regular intervals and $\Delta t$ should be reduced if the calculation is likely to be unstable.

Set the output of the predictor variable `MODULE:[AHSTIN]`

 In the atmospheric forecast variables, what is usually output is the value of time $t$ at this stage, $u^{t}, v^{t}, T^{t}, p_S^{t}, q^{t}, l^{t}$, and $u^{t}, v^{t}, T^{t}, p_S^{t}, q^{t}, l^{t}$. The actual output is done at the later timing of `MODULE:[HISTOU]`, but it is sent to the buffer at this point.

4. mechanical processes `MODULE:[DYNMCS]`

 Solving for the time variation of the predicted variables due to dynamical processes.
     $u^{t}, u^{t-\Delta t}, v^{t}, v^{t-\Delta t},
T^{t}, T^{t-\Delta t}, p_S^{t}, p_S^{t-\Delta t},
q^{t}, q^{t-\Delta t}, l^{t}, l^{t-\Delta t}$
 The value of the predicted variable in $t+\Delta t$, considering only mechanical processes, based on
     $\hat{u}^{t+\Delta t}, \hat{v}^{t+\Delta t}, 
\hat{T}^{t+\Delta t}, \hat{p_S}^{t+\Delta t}, 
\hat{q}^{t+\Delta t}, \hat{l}^{t+\Delta t}$
 Ask for .

     1. convert to vorticity and divergence `MODULE:[UV2VDG, VIRTMD, HGRAD]`

 In order to estimate the change terms of the atmospheric predictors $u, v, T, p_S, q, l$ due to mechanical processes, $u^{t}, v^{t}$ are first converted to grid values of vorticity and divergence, $\zeta^{t},D^{t}$. This is because the dynamics equations are written in terms of vorticity and divergence. Although this transformation involves a spatial derivative, it can be performed precisely by using the spherical harmonic expansion `MODULE:[UV2VDG]`.

 Furthermore, we calculate the pseudotemperature $T_v^{t}$ and the horizontal differential of surface pressure $\nabla \ln p_S$ using `MODULE:[VIRTMD]`, also using the spherical harmonic expansion function, and `MODULE:[HGRAD]`.

     2. calculation of the time-varying term by advection `MODULE:[GRDDYN]`

 Using the values in         $u, v, T, p_S, q, l$ at $t$, a part of the time-varying terms for each atmospheric variable is calculated by using the values in $u, v, T, p_S, q, l$ for horizontal and vertical advection. First, the time-varying terms of vertical velocity $\dot{\sigma}$ and $p_S$ are diagnostically obtained from successive equations, and then the vertical advection terms of $u, v, T, q, l$ are calculated using the time-varying terms. Furthermore, calculate the horizontal advection fluxes in $u, v, T, q, l$.

     3. convert to a spectrum `MODULE:[GD2WD, TENG2W]`

 Value of grid points in $t-\Delta t$ for atmospheric forecast variables from $u^{t}, v^{t}, T^{t}, p_S^{t}, q^{t}, l^{t}$ in the spectral space of spherical harmonic function expansion (but converted to vorticity divergence)
         $\tilde{\zeta}^{t}, \tilde{D}^{t}, \tilde{T}^{t}, 
\tilde{\pi}^{t}, \tilde{q}^{t}, \tilde{l}^{t}$
 (but, $\pi \equiv \ln p_S$) `MODULE:[GD2WD]`.

 In addition, the time-varying terms of $u, v, T, p_S, q, l$ are expanded into spectra. We also calculate the convergence of the horizontal advection fluxes by using the derivative in spectral space and add them to the spectral representation of the time-varying term `MODULE:[TENG2W]`.

 With this, most of the time-varying terms in $\zeta, D, T, \pi, q, l$ can be obtained as spectral values. However, among the time-varying terms in $\zeta, D, T, \pi$, those that depend on the horizontally diverging $D$ are not included in the time-varying term at this point because the time integration is performed by the semi-implicit method.

     4. time integration `MODULE:[TINTGR]`

 Among the time-varying terms in         $\zeta, D, T, \pi$, a term that depends linearly on the horizontal divergence $D$ (the gravitational wave term) is treated by the semi-implicit method, and furthermore, by implicitly incorporating the horizontal diffusion of $\zeta, D, T, q, l$, the mechanical process part of Time integration is performed. This allows for a spectral representation of the predicted value of $t+\Delta t$ considering only the mechanical processes
         $\tilde{\zeta}^{t+\Delta t}, \tilde{D}^{t+\Delta t}, 
\tilde{T}^{t+\Delta t}, \tilde{\pi}^{t+\Delta t}, 
\tilde{q}^{t+\Delta t}, \tilde{l}^{t+\Delta t}$
 is required.

     5. conversion to grid values `MODULE:[GENGD]`

 Grid values for the forecast values of $u, v, T, p_S, q, l$, and $t+\Delta t$ considering only mechanical processes from a spectral representation of the forecast variables
         $\hat{u}^{t+\Delta t}, \hat{v}^{t+\Delta t}, 
\hat{T}^{t+\Delta t}, \hat{p_S}^{t+\Delta t}, 
\hat{q}^{t+\Delta t}, \hat{l}^{t+\Delta t}$
 .

     6. diffusion correction `MODULE:[CORDIF, CORFRC]`

 Horizontal diffusion is applied in the plane of $\sigma$, but in large slopes, it causes problems such as upward transport of water vapor and false precipitation at the tops of mountains. To mitigate this problem, a correction has been added for $T,q,l$ to be close to the diffusion of $p$ surface, such as `MODULE:[CORDIF]`.

 Also, heat from friction is added to $\hat{T}$ `MODULE:[CORFRC]`

     7. mass conservation correction `MODULE:[MASFIX]`

 Corrections are made so that the global integral values of         $q$ and $l$ are preserved and the negative value of $q$ is eliminated. Furthermore, corrections are made so that the mass of dry air remains constant.

 After exiting     DYNMCS, the value of the forecaster variable in $t-\Delta t$ is discarded and is overwritten by the value of the forecaster variable in $t$. The area of the forecaster variable in $t$ is replaced by the value of the forecaster variable in $t+\Delta t$ which only takes into account the mechanical processes.

5. physical process `MODULE:[PHYSCS]`

 Value of the predicted variables in $t+\Delta t$ considering only mechanical processes
     $\hat{u}^{t+\Delta t}, \hat{v}^{t+\Delta t}, 
\hat{T}^{t+\Delta t}, \hat{p_S}^{t+\Delta t}, 
\hat{q}^{t+\Delta t}, \hat{l}^{t+\Delta t}$
 and by adding a time-varying term from physical processes to the value of the predicted variable in $t+\Delta t$
     $u^{t+\Delta t}, v^{t+\Delta t}, 
T^{t+\Delta t}, p_S^{t+\Delta t}, 
q^{t+\Delta t}, l^{t+\Delta t}$
 Ask for .

     Calculation of the basic diagnostic variables `MODULE:[PSETUP]`

 Find the basic diagnostic variables such as pseudotemperature, barometric pressure at each level, and altitude.

     2. cumulus convection, large-scale condensation `MODULE:[CUMLUS, LSCOND]`

 Calculates the time-varying terms of $T, q, l$ due to cumulus convection and integrates them with `MODULE:[CUMLUS]` and the time integration with `MODULE:[GDINTG]` using the term alone. Also, the time-varying terms of $T, q, l$ due to large-scale condensation are found and integrated by `MODULE:[LSCOND]`, and the time integration is performed with `MODULE:[GDINTG]` using only the term `MODULE:[GDINTG]`. Precipitation due to cumulus convection and large-scale condensation ($P_c, P_l$), cloud cover ($C_c, C_l$), and so on can be obtained. This gives the values of $T, q, l$ adjusted for convective condensation processes ($\hat{T}^{t+\Delta t,a}, 
\hat{q}^{t+\Delta t,a}, \hat{l}^{t+\Delta t,a}$).

     3. set the surface boundary condition `MODULE:[GNDSFC, GNDALB]`

 The state of the earth surface is set according to a given data. The ground state index, the sea surface temperature, and so on are set `MODULE:[GNDSFC]`. The surface albedo is set according to the data given by `MODULE:[GNDALB]`. (The calculation of the sea-surface albedo is incorporated into the routine for calculating the radiation flux.)

     4. calculation of the radiation flux `MODULE:[RADCON, RADFLX]`

 Set the atmospheric composition data for radiation flux calculation `MODULE:[RADCON]`. Usually, ozone is read from a file. The cloud water and cloud masses are obtained from the cumulus convection and large-scale condensation methods, but they can also be given here externally. Using these two files and $\hat{T}^{t+\Delta t,a}, \hat{q}^{t+\Delta t,a}$, the differential coefficients for the surface temperature used in $F_R$ and the implicit calculation are calculated with the $F_R$ and `MODULE:[RADFLX]`.

     5. calculation of the vertical diffuse flux `MODULE:[VDFFLX, VFTND1]`

 Using         $\hat{u}^{t+\Delta t}, \hat{v}^{t+\Delta t}, 
\hat{T}^{t+\Delta t,a}, \hat{q}^{t+\Delta t,a}, \hat{l}^{t+\Delta t,a}$, the fluxes of $u, v, T, q, l$ by the vertical diffusion process and the differential coefficient for implicit calculation are calculated using `MODULE:[VDFFLX]`. Furthermore, computes the implicit solution using the LU decomposition up to the middle of the process `MODULE:[VFTND1]`.

     6. calculation of surface processes and time integration of underground variables `MODULE:[SURFCE]`

 The fluxes of $u, v, T, q $ between the surface and the atmosphere are calculated, and the energy balance at the ground surface is solved by using an implicit solution considering the conduction of heat in the ground. This results in obtaining the surface temperature ($T_s$) and the value of the ground temperature ($T_g^{t+\Delta t}$) from the surface temperature ($t+\Delta t$) diagnostically. Furthermore, the time rate of change of the predicted variables of the atmosphere in the first layer, $F_{x,1}, F_{y,1}, Q_1, S_1$, can be obtained.

 Considering the snow accumulation and snowmelt process, the value of snow accumulation ($t+\Delta t$) is determined and the ground moisture ($W_g^{t+\Delta t}$) is determined by considering the movement of water in the ground.

 When an oceanic mixed-layer model is used, the values of ocean temperature and sea ice thickness can be obtained by time integration in $t+\Delta t$.

     7. evaluation of time variation due to radial and vertical diffusion `MODULE:[VFTND2, RADTND, FLXCOR]`

 Rate of change of each forecast variable for the combined radiative flux and vertical diffusion
 Calculates         ${\mathcal F}_x, {\mathcal F}_y, Q, S$ `MODULE:[VFTND2]`. Furthermore, the contribution of radiation is separated from the model by `MODULE:[RADTND]`. This is not used directly in the model, but is done for the sake of outputting the data.

 Since we use the implicit method, we take into account the changes in fluxes due to changes in surface temperature and atmospheric variables. The fluxes are calculated by `MODULE:[FLXCOR]` to take the change in the surface temperature and atmospheric variables into account. This is also for the convenience of the data output.

     8. evaluation of gravitational wave resistance `MODULE:[GRAVTY]`

 The change in atmospheric momentum due to geological origin is calculated and added to the rates of change of $u, v$ due to vertical diffusion of the atmosphere (${\mathcal F}_x, {\mathcal F}_y$).

     9. evaluation of the atmospheric pressure change term

 Considering the change in atmospheric pressure due to precipitation and evaporation, the atmospheric pressure change term $M$ is obtained.

     10. time integration of physical processes `MODULE:[GDINTG]`

 Using the rates of change of atmospheric variables such as radiation, vertical diffusion, surface processes, and gravitational wave resistance calculated above, the values in $t+\Delta t$ are integrated in time using ${\mathcal F}_x, {\mathcal F}_y, Q, M, S$.

     11. drying convection adjustment `MODULE:[DADJST]`

 If the calculated values of $T, q, l$ are unstable with respect to dry convection, dry convection adjustment is applied.

 By the above procedure, the value of the forecast variable in $t+\Delta t$
     $u^{t+\Delta t}, v^{t+\Delta t}, 
T^{t+\Delta t}, p_S^{t+\Delta t}, 
q^{t+\Delta t}, l^{t+\Delta t}$
 is required.

6. time filter `MODULE:[TFILT]`

 A time filter is applied to suppress the occurrence of calculation modes by     leap frog. With the time data of $u^{t-\Delta t}, u^{t}, u^{t+\Delta t}$, and TERM00131, smoothing operations are applied to each variable to convert them to $u^{t}$. (Actually, since the information on $u^{t-\Delta t}$ is deleted at `MODULE:[TFILT]` stage, this operation is performed in two steps. The first operation is performed in the mechanical process.)
