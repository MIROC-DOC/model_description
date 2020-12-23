# pcldphys: Cloud Microphysics
## Overview of Cloud Microphysics

The stratiform cloud microphysics in MIROC6 are basically the same as those used in MIROC5 (Watanabe et al. 2010). MIROC5 implemented a physically based bulk microphysical scheme.

The previous version of the scheme in MIROC3.2 diagnoses the fraction of liquid-phase condensate to total condensate simply as a function of the local temperature. The explicit treatment of ice cloud processes allows more flexible representation of the cloud liquid/ice partitioning in MIROC5/6 (Watanabe et al. 2010; Cesana et al. 2015).

The MIROC6 cloud microphysics treat two prognostic variables: ice water mixing ratio $q_i$ and cloud water mixing ratio $q_c$. Ice number concentration $N_i$ is diagnosed as a function of $q_i$ and air temperature $T \mathrm{~K}$. Cloud number concentration $N_c$ is explicitlly predicted by the online aerosol module implemented. Rain water mixing ratio $q_r$ is treated as a diagnostic variable: $q_r$ falls out to surface within the time step.

The scheme utilize a “dry” mixing ratio ($\mathrm{~kg} \mathrm{~kg}^{-1}$) to define the amount of water condensate. For example, $q_c$ is the mass of cloud water per mass of dry air in the layer. The dry air density $\rho \mathrm{~kg} \mathrm{~m}^{-3}$ is calculated as $\rho =P/(R_{air}T)$, where $P$ is the pressure in Pa, and the gas constant of air $R =287.04 \mathrm{~J} \mathrm{~kg}^{-1} \mathrm{~K}^{-1}$. A mass is obtained by multiplying the mixing ratio by the density. (e.g., the mass of ice $m_i = \rho q_i $)
A number concentraion is in units $\mathrm{~m}^{-3}$. Hereafter, unless stated otherwise, the cloud variables $q_c, q_i,N_c, \text{and } N_i$represent grid-averaged values; prime variables represent mean in-cloud quantities (e.g., such that $q_c = C q_c^{'}$, where $C$ is cloud fraction).
The sub-grid scale cloud variability within the cloudy area is not considered.

The cold rain parameterization following Wilson and Ballard (1999) predicts $q_i$ using physically based tendency terms, which represent homogeneous nucleation, heterogeneous nucleation, deposition and sublimation between vapor and ice, riming (cloud liquid water collection by ice), and ice melting. The warm rain processes produce rain as the sum of autoconversion and accretion.

Specific formulations of each process are described in the following "Microphysical Processes" subsection.
## Microphysical Processes

The calculation is done from the top layer down.
### Ice Properties

The formulation of the ice conversion terms requires parametrization of the mass, fall speed and particle size distributions of ice. These are described first and then subsequently used to derive the conversion terms.

The ice particle size distribution is parametrized as

$$
N_{i}(D)=N_{i0} \exp (-0.1222 (T-T_{0})) \exp \left(-\Lambda_{i} D\right)
\tag{WB99.A1}
$$
where $D$ is the equivolume diameter of the particle in $\mathrm{m}$, $N_{i0}=2.0 \times 10^{6} \mathrm{~m}^{-4}$, $T$ is the temperature in Kelvin, and $T_{0}= 273.15$.  $\Lambda_{i}$ represents the slope of the exponential distribution. The temperature function $\exp (-0.1222 (T-T_0))$ represents the fact that ice particles tend to be smaller at lower temperatures, and is an implicit way of parametrizing aggregation.

The mass of an ice particle is parametrized as a function of D
$$
m_{\mathrm{i}}(D)=a D^{b}
\tag{WB99.A2}
$$

where $a=0.069 \mathrm{~kg} \mathrm{~m}^{-2} \text {and } b=2.0$.

The fall-speed of an ice particle at an air density of $1\mathrm{~kg} \mathrm{~m}^{-3} $ is

$$
v_{\text {i}}(D)=c D^{d}
\tag{WB99.A3}
$$

where $c=25.2 m^{0.473} \mathrm{~s}^{-1}$ and $d=0.527 .$

At low air densities a particle will fall faster than at high air densities. Considering such ventilation effect, the fall-speed of a particle at arbitrary air density $\rho$, $v(\rho)$ is

$$
v(\rho)=\left(\rho_{0} / \rho\right)^{0.4} \nu\left(\rho_{0}\right)
\tag{WB99.A6}
$$

The combination of the distribution, mass and velocity relationships yield a fall-speed ice water content relationship.

### Ice Fall Flux

For a given ice content and temperature, $\Lambda_{\text {i}}$ can be calculated by integrating (A.2) across the particle size distribution (A.1). This gives the result that, for a given temperature, $\Lambda_{\text {i}}$ is proportional to the inverse cube root of the ice water content.

$$
\Lambda_{\text {i}} = \left(\frac{2aN_{i0}\exp (-0.1222 (T-T_{0}))}{m_i}\right)^{\frac{1}{3}}
$$

GPICEWGT ( IJSDIM,KMAX,0:KMAX ) !! ice flux weight to level k
VICELMT ( IJSDIM,KMAX,KMAX ) !! fall through limit
STYABV  !! ice flux fraction which stays above , times GAMF(1)
GOTHR ( IJSDIM, KMAX, KMAX )  !! ice fraction which goes through

The ice flux fraction from the layer k which stays above the level kk, $\text{STYABV}|_{k,kk}$ is


fraction of ice flux from level 'k' to 'kk'

Finally, the fraction of ice flux from level 'k' to the level 'kk' in the time-step, $\text{iceweight}|_{k,kk}$, is given as follows.

### Evaporation of Rain and Snow

The evaporation rate of rain $E_{r}\mathrm{~kg} \mathrm{~kg}^{-1} \mathrm{~m}^{-2} \mathrm{~s}^{-1}$ is expressed as
$$
E_{r}=k_{E}\left(q^{w}-q_v\right) \frac{F_r}{V_{Tr}}
$$
where $F_r$ denotes the net accumulation of rain water at the layer, $V_{Tr}$ the terminal velocity, and $k_E$ the evaporation factor ($V_{Tr} = 5\mathrm{~m} \mathrm{~s}^{-1}$and $k_E = 0.5$). $q_w$ correcponds to the saturation water vapor mixing ratio at the wet-bulb temperature. The evaporation occurs only when $q^{w}-q_v>0$.

Similary to this, the evaporation rate of snow $E_{s}\mathrm{~kg} \mathrm{~kg}^{-1} \mathrm{~m}^{-2} \mathrm{~s}^{-1}$ is expressed as
$$
E_{s}=k_{E}\left(q^{w}-q_v\right) \frac{F_s}{V_{Tr}}
$$
where $F_s$ denotes sedimentation of cloud ice above the layer. $V_{Ts} = 5\mathrm{~m}$.

### Ice Fall Out

### Ice Fall In

### Homogeneous nucleation

This term simply converts all liquid water to ice if the temperature is less than a given threshold of $233.15 \mathrm{~K}$.

### Heterogeneous nucleation

Heterogeneous freezing of cloud droplets takes place through contact and immersion freezing on ice cucleating particles (INPs), which are parameterized according to Lohmann and Diehl (2006) and Diehl et al. (2006).
Soil dust and black carbon can act as INPs.
Ratios of activated INPs to the total number concentration of soil dust and black carbon for the contact freezing and the immersion/condensation freezing are based on Fig. 1 in Lohmann and Diehl (2006)
With the number of INPs ($N_{nuc}$) calculated in SPRINTARS, the rate of heterogeneous freezing is diagnosed as follows.

$$
\frac{\partial q_i}{\partial t}=  \max \{N_{nuc} W_{nuc0}, q_c\}
$$
The weight of nucleated drop, $W_{nuc0}$, is set to $1.0\times10^{-12}$.
### Deposition-sublimation

A single ice particle grows or disappear by vapour diffusion according to the following equation:

$$
\frac{\partial m_i(D)}{\partial t}=\left\{4 \pi C\left(S_{\mathrm{i}}-1\right) F\right\} /\left[\left\{L_{\mathrm{s}} /(R_{v} T)-1\right\} L_{\mathrm{s}} /\left(k_{\mathrm{a}} T\right)+R_v T /\left(X P_{\text {sati }}\right)\right]
$$

where $\frac{\partial m_i(D)}{\partial t}$ is the rate of change of mass of the particle; $(S_i - 1)$ is the supersaturation of the atmosphere with respect to ice; $R_v$ is the gas constant for water vapour; $k_a$ is the thermal conductivity of air at temperature $T, X$ is the diffusivity of water vapour; $P_{\text {sati}}$ is the saturated vapour pressure over ice; $L_{\mathrm{s}}$ is the latent heat of sublimation of ice; $C$ is a capacitance term and $F$ is a ventilation coefficient. $C$ is assumed to appropriate to spheres, so is equal to $D / 2 . F$ is given by Pruppacher and Klett (1978) as $F=0.65+0.44 S c^{1 / 3} R e^{1 / 2}$ where $S c$ is the Schmidt number, equal to $0.6,$ and $R e$ is the Reynolds number, $v(D) \rho D / \mu,$ where $v(D)$ is the fall-speed of the particle and $\mu$ is the dynamic viscosity of air.

Integrating the distribution of ice, $\frac{\partial q_i}{\partial t}$ is obtained as
$$
\frac{\partial q_i}{\partial t}=\int \frac{\partial m_i(D)}{\partial t}N(D)dD
$$

The ice grows or disappears depending on the sign of $(S_i - 1)$.

1. $(S_i - 1)>0$

The ice grows (deposition). If $q_c$ exists, $q_c$ is evaporated as fast as the deposition process (Wegener–Bergeron–Findeisen process). the saturation vapor pressure over water and the lower saturation vapor pressure over ice. The basis of this theory is the fact that the equilibrium vapor pressure of water vapor with respect to ice is less than that with respect to liquid water at the same subfreezing temperature. Thus, within an admixture of these particles, the ice crystals would gain mass by vapor deposition at the expense of the liquid drops that would lose mass by evaporation.

1. $(S_i - 1)<0$

The ice disappears (sublimation)
### Cloud water collection by ice (riming)
The Rate at which single ice particle collects supercooled liquid water is given by the equation

Lomann 2004
In the model, riming (the ice crystals settling through a population of supercooled cloud droplets, freezing them upon collision) is based on the geometric sweep-out integrated over all ice sizes:
$$
\frac{\partial q_{i}}{\partial t}=\frac{\pi E_{\mathrm{SW}} n_{0 S} a q_{c} \Gamma(3+b)}{4 \lambda_{S}^{(3+b)}}\left(\frac{\rho_{0}}{\rho}\right)^{0.5}
$$
where $n_{0 S}=3 \times 10^{6} \mathrm{~m}^{-4}$ is the intercept parameter, $\lambda_{S}$ is the slope of the exponential Marshall-Palmer snow crystal size distribution, $a=4.84, b=0.25, \rho$ is the air density, and $\rho_{0}=1.3 \mathrm{~kg} \mathrm{~m}^{-3}$ is the reference density.
The collection efficiency $E_{\mathrm{sw}}$ is highly dependent on the cloud droplet and snow crystal size (Pruppacher and Klett 1997 ). The size-dependent collection efficiency for aggregates is introduced as obtained from laboratory results by Lew et al. (1986) (simulation ESWagg)

$$
E_{\mathrm{SW}}^{\mathrm{agg}}=0.939 \mathrm{St}^{2.657}
$$

The Stokes number (St) is given by
$$
\mathrm{St}=\frac{2\left(V_{t}-\boldsymbol{v}_{t}\right) \boldsymbol{v}_{t}}{D g}
$$
$V_{t}$ is the snow crystal terminal velocity, and $D$ is the maximum dimension of the snow crystal.
$v_{t}$ is the cloud droplet terminal velocity; $g$ is the acceleration due to gravity.
### Ice melt


since this term is essentially a diffusion term, although of heat instead of moisture, its form is very similar to that of the deposition and evaporation of ice term. The rate of change of ice mass of a melting particle is given by:
$$
\mathrm{d} m / \mathrm{d} t=-4 \pi C F\left\{k_{\mathrm{a}} / L_{\mathrm{m}}\left(T_{\mathrm{w}}-T_{0}\right)\right\}
$$
where $L_{\mathrm{m}}$ is the latent heat of melting of ice, $T_{\mathrm{w}}$ is the wet-bulb temperature of the air and $T_{0}$ is the freezing point of ice. The capacitance term, $C,$ is considered to be that for spherical particles. Hence $C=D / 2 .$ The ventilation factor, $F,$ is considered to be

The rate of change of ice mass of a melting particle is given by

$T_{\mathrm{w}}$ is the wet-bulb temperature of the air and $T_{0}$ is the freezing point of ice. The wet-bulb temperature is calculated using a numerical approximation containing the saturation deficit and the air

### Warm rain cloud microphysics


A Spectral Radiation-Transport Model for Aerosol Species (SPRINTARS; Takemura et al. 2000, 2002, 2005, 2009) coupled with MIROC6 explicitly predicts the number concentrations for aerosol species.
The nucleation of cloud droplets is based on the parameterization by Abdul-Razzak and Ghan [2000].

The autoconversion term following Berry (1967) is a function of $q_c$ and $N_c$ to take into account aerosol-cloud interaction.
Rain water $q_r$ is treated as a diagnostic variables.
$q_r$ falls out to surface within the time step.

autoconversion
Berry scheme
b1 = 0.035, b2 =0.12, b3 = 1.d-12


accretion

### total precipitation

### melt/freeze

## Future Challenges



