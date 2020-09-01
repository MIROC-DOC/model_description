# Model Overview.

## Characteristics of CCSR/NIES AGCM

AGCM5.4 is a three-dimensional global general circulation model developed by the Center for Climate System Research (CCSR) of the University of Tokyo and the National Institute for Environmental Studies (NIES). The features of the model are described below.

| Header0 | Header1 |
| ------- | ------- |
| system of equations | hydrostatic primitive equation system |
| area | Global 3D |
| predictive variable | Horizontal wind speed, Temperature, Surface pressure, Specific humidity, Cloud water content, Land surface temperature, Soil moisture |
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
| gravitational wave resistance | Scheme based on     McFarlane (1987) |
| option | North-south vertical and east-west vertical two-dimensional models. Vertical 1D model. |
|  | Marine Mixed-Layer Coupling Model |
