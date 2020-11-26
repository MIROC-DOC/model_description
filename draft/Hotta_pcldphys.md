pcldphys: Cloud Microphysics

2.1 Overview of Wilson and Ballard scheme

The MIROC cloud microphysics predicts three prognostic variables: ice mass $q_i$, cloud water content $q_c$, and cloud number concentration $N_c$.
Ice number concentration $N_i$ is diagnosed as a function of $q_i$ and air temperature $T$.
The cold rain parameterization following Wilson and Ballard (1999) predicts $q_i$ using physically based tendency terms, which represent homogeneous nucleation, heterogeneous nucleation, deposition and sublimation (between vapor and ice), riming (cloud liquid water collection by ice), and ice melting.

A pectral Radiation-Transport Model for Aerosol Species (SPRINTARS; Takemura et al. 2000, 2002, 2005, 2009) coupled with MIROC explicitly predicts the number concentrations for aerosol species.
The nucleation of cloud droplets is based on the parameterization by Abdul-Razzak and Ghan [2000].
Warm rain is produced as the sum of autoconversion process and accretion process.
The autoconversion term following Berry (1967) is a function of $q_c$ and $N_c$ to take into account aerosol-cloud interaction.
Rain water $q_r$ is treated as a diagnostic variables.
$q_r$ falls out to surface within the time step.

## Microphysical Processes

### Ice Fall Flux

fraction of ice flux from level 'k' to 'kk'

### Evaporation of Rain

### Ice Fall Out

### Ice Fall In

### Homogeneous nucleation

### Heterogeneous nucleation

### Deposition-sublimation

$$
\mathrm{d} m / \mathrm{d} t=\left\{4 \pi C\left(S_{\mathrm{i}}-1\right) F\right\} /\left[\left\{L_{\mathrm{s}} /(R T)-1\right\} L_{\mathrm{s}} /\left(k_{\mathrm{a}} T\right)+R T /\left(X e_{\text {sat ice }}\right)\right]
$$

### Cloud water collection by ice (riming)

### Ice melt

### Warm rain cloud microphysics

### total precipitation

### melt/freeze




