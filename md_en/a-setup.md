## Basic Settings.

Here we present the basic setup of the model.

### Coordinate System.

The coordinate system is basically,
Longitude $\lambda$, Latitude $\varphi$, Normalized Pressure $\sigma = p/p_S$
($p_S(\lambda,\varphi)$ are surface pressure.)
and treat each as orthogonal.
However, $z$ is used as the vertical coordinates.

Longitude is discretized at equal intervals `MODULE:[ASETL]`.

$$
  \lambda_i = 2 \pi \frac{i-1}{I}  \;\;\; i = 1, \ldots I-1
$$


Latitude is the Gauss latitude $\varphi_j$ described in Mechanics, and `MODULE:[ ASETL]`,
Gauss-Legendre derived from the integral formula.
This takes $\mu = \sin \varphi$ as its argument
J The zero point of the next Legendre polynomial `MODULE:[GAUSS]`.

If J is large, we can approximate

$$
  \varphi_j =  \pi ( \frac{1}{2}- \frac{j-1/2}{J} ) \;\;\; j = 1, \ldots J-1
$$


Normally, the grid spacing of longitude and latitude is taken as $J = I/2$ almost equally.
This is based on the triangular truncation of the spectral method.

Normalized atmospheric pressure ($\sigma$) is designed to give a good representation of the vertical structure of the atmosphere,
suitably discretized at unequal intervals `MODULE:[ASETS]`.
As we will discuss later in Mechanics, the value of the layer boundaries
Define the $\sigma_{k-1/2}$ in $k = 1 \ldots K+1$ and then ,

$$
 \sigma_k = \left\{ \frac{1}{1+\kappa}
                     \left( \frac{  \sigma^{\kappa +1}_{k-1/2}
                                  - \sigma^{\kappa +1}_{k+1/2}      }
                                  { \sigma_{k-1/2} - \sigma_{k+1/2} }
                     \right)
              \right\}^{1/\kappa}
$$


Find the $\sigma$ representing the layer by
Figure [a-setup:level\]] (#a-setup:level), with the standard Indicates the level of the 20 layers used.

Each forecast variable is all, $(\lambda_i, \varphi_j, \sigma_k)$
or defined on the grid of $(\lambda_i, \varphi_j, z_l)$.
(The underground level, $z_l$, is discussed in the Physical Processes section.)

In the time direction, they are discretized at equally spaced $\Delta t$,
The time integration of the forecasting equation is performed.
However, if the stability of the time integration may be compromised
$\Delta t$ can change.

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
|  | $e^*$(273K) | Pa. | 611 |
| Stefan Bolzman | $\sigma_{SB}$ | W m$^{-2}$ K$^{-4}$ | 5.67 |
| Kárman Constant | $k$ |  | 0.4 |
| Latent heat of ice melting | $L_M$ | J kg$^{-1}$ | 3.4 $\times 10^5$ |
| Water Freezing Point | $T_M$ | K | 273.15 |
| Constant pressure specific heat of water | $C_w$ | J kg$^{-1}$ | 4,200\. |
| The freezing point of seawater | $T_I$ | K | 271.35 |
| Specific heat ratio of ice at constant pressure | $C_I  = C_w - L_M/T_M$ |  | 2397\. |
| water vapor molecular weight ratio | $\epsilon  = R/R_v$ |  | 0.622 |
| coefficient of provisional temperature | $\epsilon_v = \epsilon^{-1} - 1$ |  | 0.606 |
| Ratio of specific heat to gas constant | $\kappa = R/C_p$ |  | 0.286 |


