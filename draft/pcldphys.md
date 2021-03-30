## Cloud Microphysics

The `SUBROUTINE:[CLDPHYS]` is written in the `pcldphys.F` file.

### Overview of Cloud Microphysics

Cloud microphysics control the conversion from water condensate to precipitate. The condensate parameterization closely links to the lifetime of and radiative properties of the clouds.

The stratiform (non-convective) cloud microphysics in MIROC6 (Tatebe et al. 2019) are basically the same as those used in MIROC5 (Watanabe et al. 2010). MIROC5 implemented a physically based bulk microphysical scheme. The previous version of the scheme in MIROC3.2 diagnoses the fraction of liquid-phase condensate to total condensate simply as a function of the local temperature. In contrast, the explicit treatment of ice cloud processes allows flexible representation of the cloud liquid/ice partitioning in MIROC5 and MIROC6 (Watanabe et al. 2010; Cesana et al. 2015).

The MIROC6 cloud microphysics scheme uses four quantities to describe water in the atmosphere: vapour; liquid-phase cloud droplets; raindrops; and frozen water. Only one quantity, which we will refer to as ‘ice’, is used to describe all frozen water in large-scale clouds, including aggregated snow, pristine ice crystals and rimed particles. Physically based transfer terms link the four water quantities. The scheme treats two prognostic condansate variables: ice water mixing ratio $q_i$ and cloud water mixing ratio $q_c$. Water vapor mixing ratio $q_v$ affects the rate of microphysical processes and $q_v$ itself is also modified via microphysical processes. Ice number concentration $N_i$ is diagnosed as a function of $q_i$ and air temperature $T$ in $\mathrm{~K}$. Cloud number concentration $N_c$ is predicted by the online aerosol module implemented. Rain water mixing ratio $q_r$ is treated as a diagnostic variable: $q_r$ falls out to the surface within the time step. Cloud fraction is predicted as described in the section 'pmlsc: Large Scale Condensation'.

The cold rain parameterization following Wilson and Ballard (1999) predicts $q_i$ using physically based tendency terms, which represent homogeneous nucleation, heterogeneous nucleation, deposition/sublimation between vapor and ice, riming (cloud liquid water collection by falling ice), and ice melting. The warm rain processes produce rain as the sum of autoconversion and accretion processes. Specific formulations of each process are described in the following "Microphysical Processes" subsection.

The scheme utilizes a “dry” mixing ratio ($\mathrm{~kg} \mathrm{~kg}^{-1}$) to define the amount of water condensate. For example, $q_c$ is the mass of cloud water per mass of dry air in the layer. The dry air density $\rho \mathrm{~kg} \mathrm{~m}^{-3}$ is calculated as $\rho =P/(R_{air}T)$, where $P$ is the pressure in Pa, and the gas constant of air $R_{air} =287.04 \mathrm{~J} \mathrm{~kg}^{-1} \mathrm{~K}^{-1}$. A condensate mass is obtained by multiplying the mixing ratio by the air density. (e.g., the mass of ice $m_i = \rho q_i$). A number concentraion is in units $\mathrm{~m}^{-3}$.

Hereafter, unless stated otherwise, the cloud variables $q_c, q_i,N_c, \text{and } N_i$represent grid-averaged values; prime variables represent mean in-cloud quantities (e.g., such that $q_c = C q_c^{'}$, where $C$ is cloud fraction). Note that $q_v{'} \neq q_v$. $q_v{'}$ for ice clouds is determined as described in pmlsc section. The sub-grid scale variability of water content within the cloudy area is not considered at present.

### Microphysical Processes

The time evolution of $q_i$ by microphysical processes is written in symbolic form as follows.

$$
\begin{split}
\left(\frac{\partial q_i}{\partial t}\right)_{\text {micro}}
&=\left(\frac{\partial q_i}{\partial t}\right)_{\text {esnw}}
+\left(\frac{\partial q_i}{\partial t}\right)_{\text {fallin}}
+\left(\frac{\partial q_i}{\partial t}\right)_{\text {fallout}}
+\left(\frac{\partial q_i}{\partial t}\right)_{\text {hom}}\\
&+\left(\frac{\partial q_i}{\partial t}\right)_{\text {het}}
+\left(\frac{\partial q_i}{\partial t}\right)_{\text {dep}}
+\left(\frac{\partial q_i}{\partial t}\right)_{\text {rim}}
+\left(\frac{\partial q_i}{\partial t}\right)_{\text {mlt}}
\end{split}
$$

, where t is time. The terms of the right hand side denote evaporation of snow (sunscript esnw), ice fall in from above layers (subscript fallin), ice fall out to below layers (subscript fallout), homogeneous nucleation (subscript hom), heterogeneous nucleation (subscript het), deposition/sublimation (subscript dep), riming (subscript rim), and melting (subscript mlt). Similarly, the time evolution of $q_c$ by microphysical processes is

$$
\left(\frac{\partial q_c}{\partial t}\right)_{\text {micro}}
=\left(\frac{\partial q_c}{\partial t}\right)_{\text {hom}}
+\left(\frac{\partial q_c}{\partial t}\right)_{\text {het}}
+\left(\frac{\partial q_c}{\partial t}\right)_{\text {rim}}
+\left(\frac{\partial q_c}{\partial t}\right)_{\text {evap}}
+\left(\frac{\partial q_c}{\partial t}\right)_{\text {auto}}
+\left(\frac{\partial q_c}{\partial t}\right)_{\text {accr}}
$$

, where the terms on the right hand side are homogeneous nucleation, heterogeneous nucleation, riming, evaporation (subscript evap), autoconversion (subscript auto), and accretion (subscript accr). The formulations of these processes are detailed in the following subsections.

The conversion terms of all processes are calculated at every layer downward from the top layer (k=kmax) to the bottom layer of the column (k=1). k is the vertical level increasing with height, i.e., k+1 is the next vertical level above k.

The changes in the temperature of a layer is treated consistent with the phase-change of water.

$$
\left(\frac{\partial T}{\partial t}\right)_{phase~change}=\left(\frac{\partial T}{\partial t}\right)_{vapor \leftrightarrow liquid}+\left(\frac{\partial T}{\partial t}\right)_{vapor \leftrightarrow solid}+\left(\frac{\partial T}{\partial t}\right)_{liquid \leftrightarrow solid}
$$

with

$$
\left(\frac{\partial T}{\partial t}\right)_{vapor \leftrightarrow liquid}
=\frac{L_{v}}{c_{p}}\left(
\left(\frac{\partial q_c}{\partial t}\right)_{evap}
+\left(\frac{\partial q_r}{\partial t}\right)_{erain}
\right)
$$

$$
\left(\frac{\partial T}{\partial t}\right)_{vapor \leftrightarrow solid}
=\frac{L_{s}}{c_{p}}\left(
\left(\frac{\partial q_i}{\partial t}\right)_{esnw}
+\left(\frac{\partial q_i}{\partial t}\right)_{dep}
\right)
$$

$$
\left(\frac{\partial T}{\partial t}\right)_{liquid \leftrightarrow solid}
=\frac{L_{f}}{c_{p}}\left(
\left(\frac{\partial q_i}{\partial t}\right)_{hom}
+\left(\frac{\partial q_i}{\partial t}\right)_{het}
+\left(\frac{\partial q_i}{\partial t}\right)_{rim}
+\left(\frac{\partial q_i}{\partial t}\right)_{mlt}
\right),
$$

where $L_v, L_s,$ and $L_f$ is the latent heat of vaporization, sublimation, and fusion, respectively. $C_p$ is the specific heat of moist air at constant pressure.

#### Ice Properties

The formulation of the ice conversion terms requires parametrization of the mass, fall speed and particle size distributions of ice. These are described first and then subsequently used to derive the conversion terms.

The ice particle size distribution is parametrized as

$$
N_{i}(D)=N_{i0} \exp (-0.1222 (T-T_{0})) \exp \left(-\Lambda_{i} D\right),
\tag{WB99.A1}
$$

where $D$ is the equivolume diameter of the particle in $\mathrm{m}$, $N_{i0}=2.0 \times 10^{6} \mathrm{~m}^{-4}$, $T$ is the temperature in $\mathrm{K}$, and $T_{0}= 273.15$ $\mathrm{K}$.  $\Lambda_{i}$ represents the slope of the exponential distribution. The temperature function $\exp (-0.1222 (T-T_0))$ represents the fact that ice particles tend to be smaller at lower temperatures, and is an implicit way of parametrizing aggregation.

The mass of an ice particle is parametrized as a function of D

$$
m_{\mathrm{i}}(D)=a D^{b}
\tag{WB99.A2}
$$

where $a=0.069 \mathrm{~kg} \mathrm{~m}^{-2} \text {and } b=2.0$.

The fall-speed of an ice particle at an air density of $\rho_{0} = 1\mathrm{~kg} \mathrm{~m}^{-3}$ is

$$
v_{\text {i}}(D,\rho_0)=c D^{d}
\tag{WB99.A3}
$$

where $c=25.2 m^{0.473} \mathrm{~s}^{-1}$ and $d=0.527 .$

At low air densities a particle will fall faster than at high air densities. Considering such ventilation effect, the fall-speed of a particle at arbitrary air density $\rho$ is

$$
v_{\text {i}}(D,\rho)=\left(\rho_{0} / \rho\right)^{0.4} v_{\text {i}}\left(D,\rho_{0}\right)
\tag{WB99.A6}
$$

The combination of the size distribution, mass and velocity relationships yields a fall-speed and ice water content relationship.

For a given ice content and temperature, $\Lambda_{\text {i}}$ can be calculated by integrating (A.2) across the particle size distribution (A.1). This gives the result that, for a given temperature, $\Lambda_{\text {i}}$ is proportional to the inverse cube root of the ice water content.

$$
\Lambda_{\text {i}} = \left(\frac{2aN_{i0}\exp (-0.1222 (T-T_{0}))}{m_i}\right)^{\frac{1}{3}}
$$

#### Evaporation of Rain and Snow

The evaporation rate of rain $\left(\frac{\partial q_r}{\partial t}\right)_{\text {erain}}$ is expressed as

$$
\left(\frac{\partial q_r}{\partial t}\right)_{\text {erain}}
=\frac{1}{\rho \Delta z}k_{E}\left(q^{w}-q_v\right) \frac{F_r}{V_{Tr}}
$$

, where $F_r$ denotes the net accumulation of rain water at the layer in $\mathrm{kg} \mathrm{~m}^{-2} \mathrm{~s}^{-1}$, $V_{Tr}$ the terminal velocity, and $k_E$ the evaporation factor ($V_{Tr} = 5\mathrm{~m} \mathrm{~s}^{-1}$and $k_E = 0.5$). $q^w$ correcponds to the saturation water vapor mixing ratio at the wet-bulb temperature. The evaporation occurs only when $q^{w}-q_v>0$.

Similary to this, the evaporation rate of falling ice $\left(\frac{\partial q_i}{\partial t}\right)_{\text {esnw}}$ is expressed as

$$
\left(\frac{\partial q_i}{\partial t}\right)_{\text {esnw}}
=k_{E}\left(q^{w}-q_v\right) \frac{F_i}{V_{Tr}}
$$

where $F_i$ denotes sedimentation of cloud ice from above layers. $V_{Ts}$ is set to $5\mathrm{~m} \mathrm{~s}^{-1}$.

#### Ice Fall

The total ice flux from the layer 'k' is
$$
F_i|_k = \int^\infty_0 N_{\mathrm{i}}(D) m_{\mathrm{i}}(D) v_{\text {i}}(D)dD.
$$

The fraction of ice flux from level the 'k' to the below level 'kk' $(1<=\text{kk}<\text{k})$ $\text{iceweight}|_{k,kk}$, is given as

$$
\frac{\int^{f(\text{zm(k)}-\text{zm(kk)})}_0 N_{\mathrm{i}}(D) m_{\mathrm{i}}(D) v_{\text {i}}(D)dD-
\int^{f(\text{zm(k)}-\text{zm(kk+1)})}_0 N_{\mathrm{i}}(D) m_{\mathrm{i}}(D) v_{\text {i}}(D)dD}
{\int^\infty_0 N_{\mathrm{i}}(D) m_{\mathrm{i}}(D) v_{\text {i}}(D)dD},
$$

where zm(k) is the middle of the height of the layer k, and f(dz) is the ice size which falls the distance dz in a single time step.

The net ice fall out from the layer is

$$
\left(\frac{\partial q_i}{\partial t}\right)_{\text {fallout}}
=-\frac{\Delta t}{\rho \Delta z}F_i
$$.

The net ice fall in to the layer 'k' is

$$
\left(\frac{\partial q_i}{\partial t}\right)_{\text {fallin}}
=\frac{\Delta t}{\rho \Delta z} \sum^{l=kmax}_{l=k+1}F_i|_{k=l} \times \text{iceweight}|_{l,k}
$$

#### Homogeneous nucleation

This term simply converts all liquid cloud water to ice if the temperature is less than a given threshold of $233.15 \mathrm{~K}$.

$$
\left(\frac{\partial q_i}{\partial t}\right)_{\text {hom}}
=-\left(\frac{\partial q_c}{\partial t}\right)_{\text {hom}}
=  \frac{q_c}{\Delta t}
$$

#### Heterogeneous nucleation

A Spectral Radiation-Transport Model for Aerosol Species (SPRINTARS; Takemura et al. 2000, 2002, 2005, 2009) coupled with MIROC6 explicitly predicts the masses and number concentrations for aerosol species. Heterogeneous freezing of cloud droplets takes place through contact and immersion freezing on ice cucleating particles (INPs), which are parameterized according to Lohmann and Diehl (2006) and Diehl et al. (2006). Soil dust and black carbon are assumed to act as INPs. Ratios of activated INPs to the total number concentration of soil dust and black carbon for the contact freezing and the immersion/condensation freezing are based on Fig. 1 in Lohmann and Diehl (2006). Using the number of INPs ($N_{nuc}$) predicted in SPRINTARS, the rate of heterogeneous freezing is diagnosed as follows.

$$
\left(\frac{\partial q_i}{\partial t}\right)_{\text {het}}
=-\left(\frac{\partial q_c}{\partial t}\right)_{\text {het}}
=  \max \{N_{nuc} W_{nuc0}, \frac{q_c}{\Delta t}\}
$$

The weight of nucleated drop, $W_{nuc0}$, is set to $1.0\times10^{-12}$.

#### Deposition/Sublimation

A single ice particle grows or disappears by water vapor diffusion according to the following equation:

$$
\frac{\partial m_i(D)}{\partial t}=\left\{4 \pi C\left(S_{\mathrm{i}}-1\right) F\right\} /\left[\left\{L_{\mathrm{s}} /(R_{v} T)-1\right\} L_{\mathrm{s}} /\left(k_{\mathrm{a}} T\right)+R_v T /\left(X P_{\text {sati }}\right)\right]
$$

where $\frac{\partial m_i(D)}{\partial t}$ is the rate of change of the particle mass; $(S_i - 1)$ is the supersaturation of the atmosphere with respect to ice; $R_v$ is the gas constant for water vapour; $k_a$ is the thermal conductivity of air at temperature $T, X$ is the diffusivity of water vapour; $P_{\text {sati}}$ is the saturated vapour pressure over ice; $L_{\mathrm{s}}$ is the latent heat of sublimation of ice; $C$ is a capacitance term and $F$ is a ventilation coefficient. $C$ is assumed to appropriate to spheres, so is equal to $D/2$ . $F$ is given by Pruppacher and Klett (1997) as $F=0.65+0.44 S c^{1 / 3} R e^{1 / 2}$, where $S c$ is the Schmidt number, equal to $0.6,$ and $R e$ is the Reynolds number, $v(D) \rho D / \mu,$ where $\mu$ is the dynamic viscosity of air.

Integrating ice size distribution, $\left(\frac{\partial q_i}{\partial t}\right)_{\text {dep}}$ is obtained as

$$
\left(\frac{\partial q_i}{\partial t}\right)_{\text {dep}}
= \frac{1}{\rho}\int \frac{\partial m_i(D)}{\partial t}N(D)dD
$$

The ice grows or disappears depending on the sign of $(S_i - 1)$.

1. $(S_i - 1)>0$

The ice grows (deposition). If $q_c$ exists in the same grid, $q_c$ is evaporated as fast as the deposition process (Wegener–Bergeron–Findeisen process).

$$
\left(\frac{\partial q_c}{\partial t}\right)_{\text {evap}}
=-\left(\frac{\partial q_i}{\partial t}\right)_{\text {dep}}
$$

The basis of this theory is the fact that the saturation vapor pressure of water vapor with respect to ice is less than that with respect to liquid water at the same temperature. Thus, within a mixture of these particles, the ice would gain mass by vapor deposition at the expense of the liquid drops that would lose mass by evaporation.

2. $(S_i - 1)<0$

The ice disappears (sublimation).

#### Cloud water collection by ice (riming)

Riming process (the ice crystals settling through a population of supercooled cloud droplets, freezing them upon collision) is based on the geometric sweep-out integrated over all ice sizes (Lohmann 2004):

$$
\left(\frac{\partial q_i}{\partial t}\right)_{\text {rim}}
=-\left(\frac{\partial q_c}{\partial t}\right)_{\text {rim}}
=\frac{\pi E_{\mathrm{SW}} n_{0S} a q_{c} \Gamma(3+b)}{4 \lambda_{S}^{(3+b)}}\left(\frac{\rho_{0}}{\rho}\right)^{0.5}
$$

where $n_{0 S}=3 \times 10^{6} \mathrm{~m}^{-4}$ is the intercept parameter, $\lambda_{S}$ is the slope of the exponential Marshall-Palmer ice crystal size distribution, $a=4.84, b=0.25$, and $\rho_{0}=1.3 \mathrm{~kg} \mathrm{~m}^{-3}$ is the reference density. $\Gamma$ is the gamma fanction. The collection efficiency $E_{\mathrm{sw}}$ is highly dependent on the cloud droplet and snow crystal size (Pruppacher and Klett 1997). The size-dependent collection efficiency for aggregates is introduced as obtained from laboratory results by Lew et al. (1986) (simulation ESWagg).

$$
E_{\mathrm{SW}}^{\mathrm{agg}}=0.939 \mathrm{St}^{2.657}
$$

The Stokes number (St) is given by
$$
\mathrm{St}=\frac{2\left(V_{t}-{v}_{t}\right) {v}_{t}}{D g}
$$

$V_{t}$ is the snow crystal terminal velocity, and $D$ is the maximum dimension of the snow crystal. $v_{t}$ is the cloud droplet terminal velocity. $g$ is the acceleration due to gravity.

#### Ice melt

Since this term is essentially a diffusion term, although of heat instead of moisture, its form is very similar to that of the deposition and evaporation of ice term. The rate of change of ice mass of a melting particle is given by:

$$
\left(\frac{\partial q_r}{\partial t}\right)_{\text {mlt}}
=-\left(\frac{\partial q_i}{\partial t}\right)_{\text {mlt}}
=4 \pi C F\left\{k_{\mathrm{a}} / L_{\mathrm{m}}\left(T^{\mathrm{w}}-T_{0}\right)\right\}
$$

,where $L_{\mathrm{m}}$ is the latent heat of melting of ice, $T^{\mathrm{w}}$ is the wet-bulb temperature of the air and $T_{0}=273.15\mathrm{K}$ is the freezing point of ice. Ice melt occurs when $T^{\mathrm{w}}-T_{0}>0$. The capacitance term, $C,$ is considered to be that for spherical particles. Hence $C=D / 2 .$ The ventilation factor, $F$ is considered to be the same as in the deposition/sublimation process.

#### Warm rain cloud microphysics

We assume $N_c$ is the number of aerosols activated as droplets. The nucleation of cloud droplets is predicted in the aerosol module SPRINTARS (Takemura et al. 2000; 2002; 2005; 2009) based on the parameterization by Abdul-Razzak and Ghan (2000), which depends on the aerosol particle number concentrations, size distributions and chemical properties of of each aerosol species, and the updraft velocity.

The autoconversion term following Berry (1968) is a function of $q_c$ and $N_c$.

$$
\left(\frac{\partial q_r}{\partial t}\right)_{\text {auto}}
=-\left(\frac{\partial q_c}{\partial t}\right)_{\text {auto}}
=\frac{1}{\rho}
\frac{b_1 \times m_{c}'^{2}}{b_2+b_3 \frac{N_{c}}{m_{c}'}}
$$


The parameters are set as $b_1 = 0.035$, $b_2 =0.12$, $b_3 = 1.0\times10^{-12}$. The effect of aerosol-cloud interaction on cloud lifetime is taken into account by the dependency on $N_c$.

The accretion term is given as

$$
\left(\frac{\partial q_r}{\partial t}\right)_{\text {auto}}
=-\left(\frac{\partial q_c}{\partial t}\right)_{\text {auto}}
=\frac{1}{\rho}q_c q_r
$$

Rain water $q_r$ into the layer is from above the layer. $q_r$ is treated as a diagnostic variables: $q_r$ falls out to surface within the time step.

#### Total precipitation

The total amount of precipitation at a certain pressure level, $p,$ is obtained by integrating the relevant processes from the top of the model $(p=0)$ to the respective pressure level. The fluxes of rain and ice $\mathrm{kgm}^{-2} \mathrm{~s}^{-1}$ are then expressed as

$$
P_{\text {rain}}(p) =\frac{1}{g} \int_{0}^{p}\left(
\left(\frac{\partial q_r}{\partial t}\right)_{\text {auto}}
+\left(\frac{\partial q_r}{\partial t}\right)_{\text {accr}}
+\left(\frac{\partial q_r}{\partial t}\right)_{\text {mlt}}
-\left(\frac{\partial q_r}{\partial t}\right)_{\text {revap}}
\right) d p
$$

$$
P_{\text {ice}}(p)
=\frac{1}{g} \int_{0}^{p}\left(
\left(\frac{\partial q_i}{\partial t}\right)_{\text {fallin}}
-\left(\frac{\partial q_i}{\partial t}\right)_{\text {fallout}}
+\left(\frac{\partial q_i}{\partial t}\right)_{\text {rim}}
-\left(\frac{\partial q_r}{\partial t}\right)_{\text {mlt}}
-\left(\frac{\partial q_r}{\partial t}\right)_{\text {esnw}}
\right) d p
$$
