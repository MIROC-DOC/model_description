# Model Overview.

## Characteristics of CCSR/NIES AGCM

AGCM5.4 was developed in collaboration with the Center for Climate System Research (CCSR) at the University of Tokyo.
Prepared in collaboration with the National Institute for Environmental Studies (NIES) ,
A global three-dimensional general circulation model of the atmosphere.
The characteristics of the model are listed below.

| Header0 | Header1 |
| ------- | ------- |
| system of equations | hydrostatic primitive equation system |
| area | Global 3D |
| predictive variable | Horizontal wind speed, temperature, surface pressure, specific humidity, cloud cover, |
| horizontal discretization | spectral transformation technique |
| vertical discretization | σ-system (Arakawa and Suarez, 1983) |
| emission | 2-stream DOM/adding method |
|  | (Based on Nakajima and Tanaka, 1986) |
| large-scale cloud process | Scheme with total water mixing ratio as a forecast variable |
|  | (Based on Le Treut and Li, 1991) |
| cumulus convection | Simplified Arakawa-Schubert scheme |
| vertical diffusion | Mellor and Yamada(1974) level2 |
| Surface flux | Louis(1979) Bulk type |
|  | (Considering the convection effects of stomatal resistance, Miller et al. 1992) |
| surface thermal process | multi-layered heat conduction |
| Surface Hydrological Processes | bucket model |
|  | (or, New Bucket Model, Multilayer Water Transport) |
| gravitational wave resistance | Scheme     based on McFarlane (1987) |
| option | North-south vertical and east-west vertical two-dimensional models. |
|  | Marine Mixed-Layer Coupling Model |

