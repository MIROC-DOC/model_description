## Features and structure of the model

**NOTE: the descriptions in this section are outdated.**

### Basic Features of the Model.

The MIROC6 AGCM is a numerical model for describing the global three-dimensional atmosphere based on physical laws and calculating the time evolution of the system as an initial value problem or a boundary value problem.

The data to be inputted are as follows.

- Initial data for each prognostic variable (horizontal wind speed, temperature, surface pressure, specific humidity, cloud liquid water content, etc.)

- Boundary condition data (surface elevation, surface condition, sea surface temperature, etc.)

- Various parameters of the model (atmospheric components, physical process parameters, etc.)

On the other hand, the output is the following.

- Data for each prognostic parameter and diagnostic parameter, for each time or time average

- Initial data to be used for continuous execution (restart data)

- Progress and various diagnostic messages

The prognostic variable is the data obtained as a time series by integrating the differential equation of time evolution, and the diagnostic variable is the quantity calculated from the prognostic variable, the boundary conditions and the parameters by some method that does not include time integration.

More specifically, the model basically solves the following equations (prognostic equations).

$$
  \frac{\partial{u}}{\partial {t}}  =  \left( {\mathcal F}_x \right)_D + \left( {\mathcal F}_x \right)_P.
   \\
  \frac{\partial{v}}{\partial {t}}  =  \left( {\mathcal F}_y \right)_D + \left( {\mathcal F}_y \right)_P. \\
  \frac{\partial{T}}{\partial {t}}  =  \left( Q \right)_D + \left( Q \right)_P. \\
  \frac{\partial{p_S}}{\partial {t}}  =  \left( M \right)_D + \left( M \right)_P. \\
  \frac{\partial{q}}{\partial {t}}  =  \left( S \right)_D + \left( S \right)_P. \\
  \frac{\partial{T_g}}{\partial {t}}  =  \left( Q_g \right)_D + \left( Q_g \right)_P.
$$

Here, $u,v,T,p_S,q,T_g$ are two-dimensional and three-dimensional prognostic variables such as eastward wind, northward wind, temperature, surface pressure, specific humidity, and surface state amount, respectively, and the right-hand side is a term that causes time variation of each prognostic variable. The terms ${\mathcal F}_x,{\mathcal F}_y,Q,S,Q_g$ are calculated based on the prognostic variables $u,v,T,p_S,q,T_g$, are divided into two main categories: the terms $u$ and $v$, such as advection due to the motion of the atmosphere (the terms with index $D$ in the above equation), and the terms such as cloud and radiation (the terms with index $P$ in the above equation). There are two main types of terms. The former is called the dynamical process, and the latter is called the physical process.

The advection term is the main part of the time-varying term in dynamical processes, and the accurate estimation of the spatial derivative is important in its calculation. The MIROC6 AGCM utilizes the spherical harmonic expansion to calculate the horizontal differential term. On the other hand, it is important for physical processes to be represented in a simple model with parameters (parameterization), such as energy conversions due to the phase change of water, radiative absorption and emission, the effects of small-scale atmospheric motions, and the effects of various processes on the ground surface.

The time integration of the prognostic equation is done by approximating the left-hand side of (1) etc. by the difference. For example,

$$
  \frac{\partial{q}}{\partial {t}} \rightarrow \frac{q^{t+\Delta t} - q^{t}}{\Delta t}
$$


By making ,

$$
  q^{t+\Delta t} = q^{t}
       + \Delta t \left[ \left( S \right)_D + \left( S \right)_P  \right]
$$


where $S$ is a function of the prognostic variables $u,v,T,p_S,q$. Although $S$ is a function of the prognostic variables $u,v,T,p_S,q$, and so on, there are various time difference schemes that can be used in this calculation depending on the time of day the prognostic variables are used to evaluate $S$. The MIROC6 AGCM uses the Euler method, which uses the value of the $t$ as it is, the leap frog method, which uses the value of the $t+\Delta t/2$, and the implicit method, which uses the (approximate) value of the $t+\Delta t$.

In the MIROC6 AGCM, the time integration of the prognostic variables is done separately for the dynamical and physical processes. The dynamical processes basically use a leap frog,

$$
  \tilde{q}^{t+\Delta t} = q^{t-\Delta t} + 2 \Delta t \left( S \right)_D^{t}
$$

However, some terms are treated as implicit. In the physical process, based on the results of integrating the dynamical terms, the Euler and implicit methods are used together,

$$
  q^{t+\Delta t} = \tilde{q}^{t+\Delta t} + 2 \Delta t \left( S \right)_P
$$


in (8). Note that $\Delta t$ in (8) is replaced by $2 \Delta t$.

### Model Execution Flow.

The flow of the model execution is briefly shown below. The entries in the index are the names of the corresponding subroutine.

1. set the parameters of an experiment, coordinates, etc. `SUBROUTINE:[PCONST,ASETCO,SETPAR,SETTSTRT,SETTEND]`

2. read the initial values of the prognostic variables `SUBROUTINE:[RDSTRT]`

3. start the time step `SUBROUTINE:[TIMSTP]`

4. perform time integration by mechanical processes `SUBROUTINE:[DYNMCS]`

5. perform time integration by physical processes `SUBROUTINE:[PHYSCS]`

6. advance the time `MODULE:[TFILT]`

7. Output the data if necessary `MODULE:[HISTOU]`

8. Output the restart data if necessary `SUBROUTINE:[WRRSTR]`

9. Return to 3

### Prognostic variables

The prognostic variables are as follows. The values in parentheses are the coordinate system, and $\lambda,\varphi,\sigma, z$ indicate the longitude, latitude, dimensionless pressure, $\sigma$, and vertical depth, respectively. The values in the square brackets are in units of the index.

| Element | Symbol | Unit |
| ------- | ------- | ------- |
| eastward wind speed | $u$ ($\lambda,\varphi,\sigma$) | $\mathrm{[m/s]}$|
| northward wind speed | $v$ ($\lambda,\varphi,\sigma$) | $\mathrm{[m/s]}$|
| atmospheric temperature | $T$ ($\lambda,\varphi,\sigma$) | $\mathrm{[K]}$ |
| surface pressure | $p_S$ ($\lambda,\varphi$) |  $\mathrm{[hPa]}$ |
| specific humidity | $q$ ($\lambda,\varphi,\sigma$) |  $\mathrm{[kg/kg]}$ |
| cloud water specific humidity | $l$ ($\lambda,\varphi,\sigma$) |  $\mathrm{[kg/kg]}$ |
| cloud ice specific humidity | $q_i$ ($\lambda,\varphi,\sigma$) |  $\mathrm{[kg/kg]}$ |
| total water PDF variance | $V$ ($\lambda,\varphi,\sigma$) |  $\mathrm{ND}$ |
| total water PDF skewness | $S$ ($\lambda,\varphi,\sigma$) |  $\mathrm{ND}$ |
| variance of liquid potential temperature | $TSQ$ ($\lambda,\varphi,\sigma$) |  $\mathrm{K^2}$ |
| covariance of liquid potential temperature and total water | $COV$ ($\lambda,\varphi,\sigma$) |  $\mathrm{K}$ |
| variance of total water | $QSQ$ ($\lambda,\varphi,\sigma$) |  $\mathrm{ND}$ |
| tracers | | |

Of these quantities, the quantities for turbulence process, $TSQ, COV, QSQ$, store only one step at a time, while the quantities for the atmosphere, $u, v, T, p_S, q, l, q_i, V, S$, need to store two steps at a time. This is due to the fact that the leap frog method is used in the time integration of the dynamic process of the quantities related to the atmosphere.

The quantities of the atmosphere, $u, v, T, p_S, q, l$, are variables managed by the main routine, `Administration of the Atmosphere'[AGCM5\a]`. On the other hand, the quantities relating to the earth's surface and ground, $q_i, V, S, TSQ, COV, QSQ$, do not appear in the main routine, but are managed by the subroutine `MODULE:[PHYSCS]` of the physical process.

Tracers include mass concentrations of aerosol species,

### The flow of time evolution of variables

This subsection is to be written.
