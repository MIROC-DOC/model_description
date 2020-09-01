## Basic Settings.

Here we present the basic setup of the model.

### Coordinate System.

The coordinate system is basically based on the longitude $\lambda$, latitude $\varphi$, and normalized atmospheric pressure $\sigma = p/p_S$ ($p_S(\lambda,\varphi)$ being surface atmospheric pressure), which are treated as orthogonal to each other. However, the vertical coordinates of the underground coordinate system ($z$) are used.

Longitude is discretized at equal intervals `MODULE:[ASETL]`.

$$
  \lambda_i = 2 \pi \frac{i-1}{I}  \;\;\; i = 1, \ldots I-1
$$


The latitude is the Gauss latitude $\varphi_j$ described in Mechanics, and it is derived from `MODULE:[ASETL]`, the Gauss-Legendre integral formula. This is the zero point of the Legendre polynomial of order J with $\mu = \sin \varphi$ as the argument, `MODULE:[GAUSS]`.

If J is large, we can approximate

$$
  \varphi_j =  \pi ( \frac{1}{2}- \frac{j-1/2}{J} ) \;\;\; j = 1, \ldots J-1
$$


Usually, the grid spacing of longitude and latitude is taken to be approximately equal to $J = I/2$. This is based on the triangular truncation of the spectral method.

The normalized atmospheric pressure $\sigma$ is discretized appropriately at unequal intervals so as to better represent the vertical structure of the atmosphere `MODULE:[ASETS]`. As described later in Mechanics, the value of the layer boundaries ($\sigma_{k-1/2}$) is defined in $k = 1 \ldots K+1$, and then

$$
 \sigma_k = \left\{ \frac{1}{1+\kappa}
                     \left( \frac{  \sigma^{\kappa +1}_{k-1/2}
                                  - \sigma^{\kappa +1}_{k+1/2}      }
                                  { \sigma_{k-1/2} - \sigma_{k+1/2} }
                     \right)
              \right\}^{1/\kappa}
$$


to find the $\sigma$ that represents the layers by Figure [a-setup:level\]] (#a-setup:level) shows the standard 20 levels of layers used.

Each predictor is entirely defined on a grid of $(\lambda_i, \varphi_j, \sigma_k)$ or $(\lambda_i, \varphi_j, z_l)$. (The underground level, $z_l$, is described in the section on physical processes.)

In the time direction, the predictive equations are discretized at evenly spaced $\Delta t$ and time integration is performed. However, if the stability of the time integration may be impaired, the $\Delta t$ may change.

### Physical Constants.

The basic physical constants are shown below `MODULE:[APCON]`.

| Header0 | Header1 | Header2 | Header3 |
| ------- | ------- | ------- | ------- |
| earth radius | $a$ | m | 6.37 $\times 10^6$ |
| acceleration of gravity | $g$ | ms$^-2$ | 9.8 |
| atmospheric pressure specific heat | $C_p$ | J kg$^{-1}$ K$^{-1}$ | 1004.6 |
| Atmospheric gas constant | $R$ | J kg$^{-1}$ K$^{-1}$ | 287.04 |
| Latent heat of water evaporation | $L$ | J kg$^{-1}$ | 2.5 $\times 10^6$ |
| Water vapor constant pressure specific heat | $C_v$ | J kg$^{-1}$ K$^{-1}$ | 1810\bsp. |
| Gas constant of water | $R_v$ | J kg$^{-1}$ K$^{-1}$ | 461\. |
| Density of liquid water | $d_{H_2O}$ | J kg$^{-1}$ K$^{-1}$ | 1000. |
| 0 Saturated vapor at 0 $^{\circ}$ | $e^*$(273K) | Pa. | 611 |
| Stefan Bolzman Constant | $\sigma_{SB}$ | W m$^{-2}$ K$^{-4}$ | 5.67 $\times 10^{-8}$ |
| Kárman Constant | $k$ |  | 0.4 |
| Latent heat of ice melting | $L_M$ | J kg$^{-1}$ | 3.4 $\times 10^5$ |
| Water Freezing Point | $T_M$ | K | 273.15 |
| Constant pressure specific heat of water | $C_w$ | J kg$^{-1}$ | 4,200\. |
| The freezing point of seawater | $T_I$ | K | 271.35 |
| Specific heat ratio of ice at constant pressure | $C_I  = C_w - L_M/T_M$ |  | 2397\. |
| water vapor molecular weight ratio | $\epsilon  = R/R_v$ |  | 0.622 |
| coefficient of provisional temperature | $\epsilon_v = \epsilon^{-1} - 1$ |  | 0.606 |
| Ratio of specific heat to gas constant | $\kappa = R/C_p$ |  | 0.286 |
