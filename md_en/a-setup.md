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

 - TAB00000:0.0 
 earth radius

 - TAB00000:0.1 
     $a$

 - TAB00000:0.2 
     m

 - TAB00000:0.3 
     6.37 $\times 10^6$

 - TAB00000:1.0 
 acceleration of gravity

 - TAB00000:1.1 
     $g$

 - TAB00000:1.2 
     ms$^-2$

 - TAB00000:1.3 
     9.8

 - TAB00000:2.0 
 atmospheric pressure specific heat

 - TAB00000:2.1 
     $C_p$

 - TAB00000:2.2 
     J kg$^{-1}$ K$^{-1}$

 - TAB00000:2.3 
     1004.6

 - TAB00000:3.0 
 Atmospheric gas constant

 - TAB00000:3.1 
     $R$

 - TAB00000:3.2 
     J kg$^{-1}$ K$^{-1}$

 - TAB00000:3.3 
     287.04

 - TAB00000:4.0 
 Latent heat of water evaporation

 - TAB00000:4.1 
     $L$

 - TAB00000:4.2 
     J kg$^{-1}$

 - TAB00000:4.3 
     2.5 $\times 10^6$

 - TAB00000:5.0 
 Water vapor constant pressure specific heat

 - TAB00000:5.1 
     $C_v$

 - TAB00000:5.2 
     J kg$^{-1}$ K$^{-1}$

 - TAB00000:5.3 
     1810\bsp.

 - TAB00000:6.0 
 Gas constant of water

 - TAB00000:6.1 
     $R_v$

 - TAB00000:6.2 
     J kg$^{-1}$ K$^{-1}$

 - TAB00000:6.3 
     461\.

 - TAB00000:7.0 
 Density of liquid water

 - TAB00000:7.1 
     $d_{H_2O}$

 - TAB00000:7.2 
     J kg$^{-1}$ K$^{-1}$

 - TAB00000:7.3 
     1000.

 - TAB00000: 8.0 
     0 in $^{\circ}$.
 saturation vapor

 - TAB00000:8.1 
     $e^*$(273K)

 - TAB00000:8.2 
     Pa.

 - TAB00000:8.3 
     611

 - TAB00000:9.0 
     Stefan Bolzman
 constant

 - TAB00000:9.1 
     $\sigma_{SB}$

 - TAB00000:9.2 
     W m$^{-2}$ K$^{-4}$

 - TAB00000:9.3 
     5.67
     $\times 10^{-8}$

 - TAB00000:10.0 
     Kárman Constant

 - TAB00000:10.1 
     $k$

 - TAB00000:10.2

 - TAB00000:10.3 
     0.4

 - TAB00000:11.0 
 Latent heat of ice melting

 - TAB00000:11.1 
     $L_M$

 - TAB00000:11.2 
     J kg$^{-1}$

 - TAB00000:11.3 
     3.4 $\times 10^5$

 - TAB00000:12.0 
 Water Freezing Point

 - TAB00000:12.1 
     $T_M$

 - TAB00000:12.2 
     K

 - TAB00000:12.3 
     273.15

 - TAB00000:13.0 
 Constant pressure specific heat of water

 - TAB00000:13.1 
     $C_w$

 - TAB00000:13.2 
     J kg$^{-1}$

 - TAB00000:13.3 
     4,200\.

 - TAB00000:14.0 
 The freezing point of seawater

 - TAB00000:14.1 
     $T_I$

 - TAB00000:14.2 
     K

 - TAB00000:14.3 
     271.35

 - TAB00000:15.0 
 Specific heat ratio of ice at constant pressure

 - TAB00000:15.1 
     $C_I  = C_w - L_M/T_M$

 - TAB00000:15.2

 - TAB00000:15.3 
     2397\.

 - TAB00000:16.0 
 water vapor molecular weight ratio

 - TAB00000:16.1 
     $\epsilon  = R/R_v$

 - TAB00000:16.2

 - TAB00000:16.3 
     0.622

 - TAB00000:17.0 
 coefficient of provisional temperature

 - TAB00000:17.1 
     $\epsilon_v = \epsilon^{-1} - 1$

 - TAB00000:17.2

 - TAB00000:17.3 
     0.606

 - TAB00000:18.0 
 Ratio of specific heat to gas constant

 - TAB00000:18.1 
     $\kappa = R/C_p$

 - TAB00000:18.2

 - TAB00000:18.3 
     0.286

