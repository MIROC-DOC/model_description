# Introduction
## Characteristics of MIROC6 AGCM

Atmospheric GCM part of MIROC is based on CCSR/NIES  AGCM 5.6 that is a three dimensional global general circulation model developed by the Center for Climate System Research (CCSR), University of Tokyo and the National Institute for Environmental Studies (NIES). The features of the model are summarized below.

- **System of equations**: Hydrostatic primitive equations
- **Area**: Global 3D
- **Prognostic variables**: Horizontal wind speed, temperature, surface pressure,  specific humidity, cloud water
- **Horizontal discretization**: Spectral transformation (Bourke, 1988) method
- **Vertical discretization**: Hybrid $\sigma - p$ coordinate, based on Arakawa and Konor (1996)
- **Resolution for default**: T85 (150 km), 81 levels up to 0.004 hPa
- **Time integration**: Essentially the leap frog scheme, with a time filter (Williams, 2009)
- **Cumulus**: An entrainment plume model with multiple cloud types (Chikira and Sugiyama, 2010)
- **Shallow convection**: A mass-flux-based single-plume model based on Park and Bretherton (2009)
- **Large scale condensation & Cloud microphysics**: A prognostic large scale condensation scheme (Watanabe et al., 2009) and the implementation of a bulk mirco-physical scheme (Wilson and Ballard, 1999)
- **Radiation**: k-distribution scheme (Sekiguchi and Nakajima, 2008) with a hexagonal solid column as ice particle habit and extended mode radius of cloud particles
- **Turbulence**: The Mellor-Yamada-Nakanishi-Niino scheme (Nakanishi 2001; Nakanishi and Niino 2004)'s level 2.5 closure scheme
- **Surface flux**: Bulk coefficients (Louis, 1979; Louis et al., 1982) with convection effects at sea surface (Miller et al., 1992)
- **Gravity wave drag**: An orographic gravity wave parameterization (McFarlane, 1987) with a non-orographic gravity wave parameterization (Hines, 1997; Watanabe et al., 2011)
