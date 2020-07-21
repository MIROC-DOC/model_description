## Radiant Flux.

### Summary of Radiation Flux Calculations

The CCSR/NIES AGCM radiation calculation scheme is ,
Discrete Ordinate Method and
It was created based on the k-Distribution Method.
by gases and clouds/aerosols
Considering the absorption, emission, and scattering processes of solar and terrestrial radiation,
Calculate the value of the radiation flux at each level.
The main input data are temperature $T$, specific humidity $q$, and cloud cover $l$, cloud cover is in $C$,
The output data are upward and downward radiation fluxes, $F^-, F^+$,
and the differential coefficient of upward radiation flux with respect to surface temperature
This is a $dF^-/dT_g$.

The calculation is done for several wavelengths.
Each wavelength range is based on the k-distribution method,
It is further divided into several sub-channels.
As for gaseous absorption,
H$_2$O, CO$_2$, O$_3$, N$_2$O, Band Absorption of the CH$_4$ and ,
Continuous absorption of H$_2$O, O$_2$, O$_3$
and CFC absorption is incorporated.
As for the scattering, we can use Rayleigh scattering of gases and
Scattering by cloud and aerosol particles is incorporated.

The outline of the calculation procedure is as follows (subroutine names in parentheses).

1. calculate the Planck function from atmospheric temperature `MODULE:[PLANKS]`.

2. in each subchannel,
 Calculates the optical thickness due to gas absorption `MODULE:[PTFIT]`.

3. by continuous absorption and CFC absorption
 calculate the optical thickness `MODULE:[CNTCFC]`.

4. of Rayleigh scattering and particle scattering
 Calculates the optical thickness and scattering moment `MODULE:[SCATMM]`.

5. from the optical thickness and solar zenith angle of the scattering,
 Seeking sea-level albedo `MODULE:[SSRFC]`.

6. for each sub-channel,
 Expand the Planck function by optical thickness `MODULE:[PLKEXP]`.

7. for each sub-channel,
 Calculates the transmission coefficient, reflection coefficient, and source function for each layer `MODULE:[TWST]`

8. by adding method, the
 calculate the radiation flux `MODULE:[ADDING]`

To account for the partial coverage of clouds,
The transmission coefficients, reflection coefficients and source functions for each layer are
Calculated separately for cloud cover and cloud-free conditions,
Multiply the cloud cover by the weight of the cloud cover and take the average.
We also consider the cloud cover of the cumulus clouds.
In addition, we also perform several additions and calculate the clear-sky radiation flux.

### Wavelengths and Subchannels.

The basics of radiative flux calculations are ,
Beer-Lambert's Law

$$
  F^\lambda(z) = F^\lambda(0) exp (-k^\lambda z)
$$


. where $F^\lambda$ is the radiant flux density at the wavelength of $\lambda$.
$k^\lambda$ is the absorption coefficient.
In order to calculate the radiative fluxes related to the heating rate, we need to calculate the
An integration operation with respect to the wavelength is required.

$$
  F(z) = \int F^\lambda(z) d \lambda 
 = \int F^\lambda(0) exp (-k^\lambda z) d \lambda
$$

> <span id="p-rad:beer" label="p-rad: > beer">beer[p-rad:beer\]</span>.

However, the absorption and emission of radiation by gas molecules is not
Due to the complicated wavelength dependence of the absorption line structure of the molecule,
It is not easy to evaluate this integration precisely.
The method designed to make the relatively precise calculation easier is
It is a k-distribution method.
Within a certain wavelength range, the absorption coefficient of $k$
Consider the density function $F(k)$ for $\lambda$,
([p-rad:beer\]](#p-rad:beer))

$$
 \int F^\lambda(0) exp (-k^\lambda z) d \lambda 
 \simeq \int \bar{F}^k(0) exp (-k z) F(k) dk
$$


which is approximated by where $bar{F}^k(0)$ is
In the $z=0$, the absorption coefficient in this wavelength range has a value of $k$
It is a flux averaged over a wavelength.
This expression shows that $\bar{F}_k, F(k)$ are the same as the $k$
If you have a relatively smooth function,

$$
 \int F^\lambda(0) exp (-k^\lambda z) d \lambda 
 \simeq \sum \bar{F}^i(0) exp (-k^i z) F^i
$$

> <span id="p-rad:beer-kd" label="p-rad: beer-kd">\\blazer[p-rad:beer-kd\]</span>

with the addition of a finite number of exponential terms (subchannels), as
It is possible to calculate relatively precisely.
This method is furthermore ,
It has the advantage that it is easy to consider absorption and scattering at the same time.

In the CCSR/NIES AGCM ,
By changing the radiation parameter data, the
Calculations can be performed at various wavelengths.
Not currently used as a standard,
The wavelength range is divided into 18 parts.
In addition, each wavelength range is divided into one to six sub-channels (corresponding to the $i$ in the above formula),
There will be 37 channels in total.
The wavelength range is the wavenumber (cm$^{-1}$)
50, 250, 400, 550, 770, 990, 1100, 1400, 2000,
2500, 4000, 14500, 31500, 33000, 34500, 36000, 43,000, 46,000, 50000
Divided by.

### Calculating the Planck function `MODULE:[PLANKS]`

The Planck function $\overline{B}^w(T)$ integrated in each wavelength range is,
Evaluate by the following formula.

$$
  \overline{B}^w(T) 
   = \lambda^{-2} T \exp \left\{ \sum_{n=0}{4} B^w_n (\bar{\lambda}^w T)^{-n}
                         \right\}
$$


$\bar{\lambda}^w$ is the average wavelength of the wavelength range,
$B^w_n$ is a parameter defined by function fitting.
This is the atmospheric temperature of each layer, $T_l$, and the boundary atmospheric temperature of each layer, $T_{l+1/2}$
and surface temperature $T_g$.

In the following, the index $w$ is basically abbreviated for the wavelength range.

### Calculating the optical thickness by gas absorption `MODULE:[PTFIT]`

The optical thickness of the gas absorption is determined by using the index $m$ as the type of molecule,
It looks like the following.

$$
  \tau^g = \sum_{m=1}{N_m} k^{(m)} C^{(m)}
$$


where $k^{(m)}$ is the absorption coefficient of the molecule $m$, and each subchannel has a Different.

$$
 k^{(m)} = \exp\left\{ \sum_{i=0}{N_i} \sum_{j=0}{N_j} A^{(m)}_{ij}
                   (\ln p)^{i} (T-T_{STD})^{j}
               \right\}
$$


as a function of temperature $T$(K) and atmospheric pressure $p$(hPa) in the form Given.
$C^{(m)}$ is the amount of gas in the layer represented by mol cm$^{-2}$,
Volume Mixing Ratio $r$ (in ppmv) to ,

$$
  C = 1\times 10^{-5} \frac{p}{R_u T} \Delta z \cdot r
$$


And it can be calculated that .
However, $R_u$ is the gas constant per mole (8.31 J mol$_{-1}$ K$^{-1}$) and ,
The unit of air layer thickness $\Delta z$ is in km.
The volume mixing ratio $r$ at ppmv is
Mass Mixture Ratio $q$ to ,

$$
  r = 10^6 R^{(m)}/R^{(air)} q = 10^6 M^{(air)}/M^{(m)}
$$


This can be converted by .
$R^{(m)},R^{(air)}$ are
Gas constant per target molecule and atmospheric mass, respectively,
$M^{(m)},M^{(air)}$ is
It is the average molecular weight of the target molecule and the atmosphere, respectively.

This calculation is done for each sub-channel and each layer.

### Optical Thickness by Continuous Absorption and CFC Absorption `MODULE:[CNTCFC]`

The optical thickness of the H$_2$O continuous absorption $\tau^{H_2O}$ is ,
Think of it as a dimer,
Basically, it is evaluated in proportion to the square of the volume mixing ratio of water vapor.

$$
\tau^{H_2O} = ( A^{H_2O} + f(T) \hat{A}^{H_2O} ) (r^{H_2O})^2 \rho \Delta z
$$


The $f(T)$ for the $\hat{A}$ section is ,
The temperature dependence of the absorption of the dimer.
Furthermore, in the wavelength range where normal gas absorption is ignored, the
Incorporate a contribution proportional to the square of the volume mixing ratio of water vapor.

The continuous absorption of O$_2$ is assumed to be constant in the mixing ratio,

$$
\tau^{O_2} = A^{O_2} \rho \Delta z
$$


.

Continuous absorption of O$_3$ is achieved by using the mixing ratio $r^{O_3}$ and incorporating the temperature dependence .

$$
\tau^{O_3} = \sum_{n=0}{2} A^{O_3}_n r^{O_3} \frac{T}{T_{STD}}^n \rho \Delta z
$$


Absorption of CFCs is considered for $N_m$ types of CFCs,

$$
\tau^{CFC} = \sum_{m=1}{N_m} A^{CFC}_m r^{(m)} \rho \Delta z
$$


The sum of these optical thicknesses is $\tau^{CON}$.

$$
 \tau^{CON} =  \tau^{H_2O} + \tau^{O_2} + \tau^{O_3} + \tau^{CFC} 
$$


This calculation is performed for each wavelength range and each layer.

### Scattering optical thickness and scattering moments `MODULE:[SCATMM]`

The optical thicknesses of Rayleigh scattering and particle dissipation (including scattering and absorption) are

$$
\tau^{s} 
 = \left( e^R + \sum_{p=1}{N_p} e^{(p)}_m r^{(p)}\right) \rho \Delta z
$$


where $e^R$ is the dissipation coefficient of Rayleigh scattering,
The $e^{(p)}$ is the dissipation factor of the particle $p$,
$r^{(p)}$ converted to standard conditions
It is the volume mixing ratio of the particle $p$.

Here, the mass mixing ratio of cloud water from $l$
The conversion of cloud grains to standard state-conversion volume mixing ratios (ppmv) is as follows.

$$
  r = 10^6 \frac{p_{STD}}{R T_{STD}}/\rho_w
$$


However, $\rho_w$ is the density of cloud particles.

On the other hand, the scattering-induced part of the optical thickness, $\tau_s^s$, is

$$
\tau_s^{s} 
 = \left( s^R + \sum_{p=1}{N_p} s^{(p)}_m r^{(p)}\right) \rho \Delta z
$$


where $s^R$ is the scattering coefficient of Rayleigh scattering,
$s^{(p)}$ is the scattering coefficient for the particle $p$.

Also, the standardized scattering moments
$g$ (asymmetry factor) and $f$ (forward scattering factor) were not

$$
g = \frac{1}{\tau_s} \left[
    \left( g^R + \sum_{p=1}{N_p} g^{(p)}_m r^{(p)}\right) \rho \Delta z
    \right]
$$


$$
f = \frac{1}{\tau_s} \left[ 
    \left( f^R + \sum_{p=1}{N_p} f^{(p)}_m r^{(p)}\right) \rho \Delta z
    \right]
$$


Here, $g^R, f^R$ are the scattering moments of Rayleigh scattering,
$g^{(p)}, f^{(p)}$ is the scattering moment of the particle $p$.

This calculation is performed for each wavelength range and each layer.

### Albedo at Sea Level `MODULE:[SSRFC]`

Albedo $\alpha_s$ at sea level is the vertical addition of the optical thickness of the scattering
Using $<\tau^{s}>$ and the solar incidence angle factor $\mu_0$,

$$
  \alpha_s = \exp\left\{ \sum_{i,j} C_{ij} {\mathcal T}^j {\mu_0}^j \right\}
$$


expressed as follows.
However,

$$
 {\mathcal T} = ( 4 <\tau^{s}>/\mu )^{-1}
$$


It is.

This calculation is done for each wavelength.

### Total Optical Thickness.

Gaseous band absorption, continuous absorption, Rayleigh scattering, particle scattering and absorption
All things considered, the optical thickness is ,

$$
  \tau = \tau^g + \tau^{CON} + \tau^{s}
$$


where $\tau^g$ is different for each subchannel. Here, since $\tau^g$ is different for each subchannel,
The calculation is done for each sub-channel and each layer.

### Planck function expansion `MODULE:[PLKEXP]`

In each layer, the Planck function $B$ is

$$
  B(\tau') = b_0 + b_1 \tau' + b_2 \left(\tau'\right)^2
$$


and obtain the expansion coefficients $b_0, b_1, b,2$.
Here, as $B(0)$
$B$ at the top of each layer (bordering the top layer),
As $B(\tau)$, $B$ at the bottom edge of each layer (the boundary with the layer below),
As $B(\tau/2)$, use the $B$ at the representative level of each layer.

$$
  b_0  =  B(0)  \\
  b_1  =  ( 4B(\tau/2) - B(\tau) - 3B(0) )/\tau  \\
  b_2  =  2 ( B(\tau) + B(0) - 2B(\tau/2) )/\tau^2  
$$




This calculation is done for each sub-channel and each layer.

### Transmission and reflection coefficients of each layer, the source function `MODULE:[TWST]`

So far obtained, optical thickness $\tau$, optical thickness of scattering $\tau^s$,
Scattering Moments $g, f$, Expansion Coefficient for Planck Function $b_0, b_1, b_2$,
Using the solar incidence angle factor $\mu_0$,
Assuming a uniform layer, and using the two-stream approximation
Transmission Coefficient $R$, Reflection Coefficient $T$, Downward Radiation Source Function $\epsilon^+$,
Find the upward radiation source function $\epsilon^-$.

The single-scattering albedo $\omega$ is,

$$
  \omega = \tau_s^s/\tau
$$


The contribution from the forward scattering factor $f$ is
Corrected Optical Thickness $\tau^*$,
The single-scattering albedo $\omega^*$, asymmetric factor $g^*$ is,

$$
  \tau^*  =  \frac{\tau}{1-\omega f} \\
  \omega^*  =  \frac{(1-f)\omega}{1-\omega f}   \\
  g^*  =  \frac{g-f}{1-f}  
$$




From now on, as a phase function of the normalized scattering,

$$
  \hat{P}^\pm    =  \omega^* {W^-}^2 \left( 1 \pm 3g^* \mu \right)/2 \\
  \hat{S}_s^\pm  =  \omega^* W^-     \left( 1 \pm 3g^* \mu \mu_0 \right)/2
$$



However, $\mu$ is a two-stream directional cosine, and

$$
  \mu \equiv \left\{ \begin{array}{ll}
                   1/\sqrt{3} \; \; \;  可視・近赤外域 \\
                   1/1.66     \; \; \;  赤外域
                    \end{array}
             \right.
$$


$$
  W^- \equiv \mu^{-1/2}
$$


Furthermore,

$$
  X  =  \mu^{-1} - (\hat{P}^+ - \hat{P}^- ) \\
  Y  =  \mu^{-1} - (\hat{P}^+ + \hat{P}^- ) \\
  \hat{\sigma}_s^{\pm}  =  \hat{S}_s^+ \pm \hat{S}_s^- \\
  \lambda  =  \sqrt{XY}
$$





the reflectance $R$ and transmission $T$ become

$$
 \frac{A^+{\tau^*}}{A^-{\tau^*}}
   =  \frac{X (1+e^{-\lambda\tau^*}) - \lambda (1-e^{-\lambda\tau^*})}
             {X (1+e^{-\lambda\tau^*}) + \lambda (1-e^{-\lambda\tau^*})} \\
 \frac{B^+{\tau^*}}{B^-{\tau^*}}
   =  \frac{X (1-e^{-\lambda\tau^*}) - \lambda (1+e^{-\lambda\tau^*})}
             {X (1-e^{-\lambda\tau^*}) + \lambda (1+e^{-\lambda\tau^*})}
$$



$$
  R  =   \frac{1}{2} \left(  \frac{A^+{\tau^*}}{A^-{\tau^*}} 
                             + \frac{B^+{\tau^*}}{B^-{\tau^*}} \right) \\
  T  =   \frac{1}{2} \left(  \frac{A^+{\tau^*}}{A^-{\tau^*}} 
                             - \frac{B^+{\tau^*}}{B^-{\tau^*}} \right)
$$



Next, we first find the source function from which the Planck function is derived.

$$
  \hat{b}_n = 2 \pi (1-\omega^*) W^- b_n \; \; \; n=0,1,2 
$$


The expansion coefficients of the radiant function can be found from

$$
  D_2^\pm  =  \frac{\hat{b}_2}{Y} \\
  D_1^\pm  =  \frac{\hat{b}_1}{Y} \mp  \frac{2 \hat{b}_2}{XY} \\
  D_0^\pm  =  \frac{\hat{b}_0}{Y} + \frac{2 \hat{b}_2}{XY^2} 
                \mp  \frac{\hat{b}_1}{XY} \\
$$





$$
  D^\pm(0)       =  D_0^pm \\
  D^\pm(\tau^*)  =  D_0^pm + D_1^pm \tau^* + D_2^pm {\tau^*}^2
$$



The source function $\hat{\epsilon}_A^\pm$, which is derived from the Planck function, is

$$
  \hat{\epsilon}_A^-  =  D^-(0) - R D^+(0) - T D^-(\tau^*) \\
  \hat{\epsilon}_A^+  =  D^+(0) - T D^+(0) - R D^-(\tau^*)
$$



On the other hand, the source function of the solar-induced radiation is

$$
  Q\gamma = \frac{X\hat{\sigma}_s^+ + \mu_0^{-1} \hat{\sigma}_s^-}
                 {\lambda^2 - \mu_0^{-2} }
$$


than ,

$$
  V_s^\pm = \frac{1}{2} \left[
             Q\gamma \pm \left( \frac{Q\gamma}{\mu X} 
                                + \frac{\hat{\sigma}_s^-}{X} \right)
                        \right]
$$


we obtain the following by using

$$
  \hat{\epsilon}_S^-  =  V_s^- - R V_s^+ - T V_s^- e^{-\tau^*/\mu_0} \\
  \hat{\epsilon}_S^+  =  V_s^+ - T V_s^+ - R V_s^- e^{-\tau^*/\mu_0}
$$



This calculation is done for each sub-channel and each layer.

### Combinations of source functions for each layer.

The Planck function origin and solar-induced origin
The combined source function is

$$
  \epsilon^\pm  = 
  \epsilon_A^\pm + \hat{\epsilon}_S^\pm e^{-<\tau^*>/\mu_0} F_0 \\
$$


However, the $<\tau^*>$ is not a good match for the upper atmosphere. However, $<\tau^*>$ has a value of
to the top of the layer we're considering now.
It is the total optical thickness of the $\tau^*$,
It is the incident flux in the wavelength range under consideration in $F_0$.
In other words, $e^{-<\tau^*>/\mu_0} F_0$ is
It is the incident flux at the top of the layer under consideration.
This calculation is actually ,

$$
  e^{-<\tau^*>/\mu_0} = \Pi' e^{-\tau^*/\mu_0}
$$


The procedure is as follows. $\Pi'$ will be taken from the uppermost layer of the atmosphere by
Represents the product up to one layer above the layer we're considering now.

This calculation is done for each sub-channel and each layer.

### Radiation flux at each layer boundary `MODULE:[ADDING]`

Transmission Coefficient of Each Layer $R_l$, Reflection Coefficient $T_l$, Radiation Source Function $\epsilon^\pm_l$
is required in all layers of $l$,
The radiation fluxes at each layer boundary can be obtained by using the adding method.
This means that the two layers of $R,T,\epsilon$ are known,
The $R,T,\epsilon$ of the whole combined layer of the two layers can be easily calculated by
It is an exploitation of what is required .
In a homogeneous layer, the reflectance of the incident light from above, the transmission coefficient and the
It is the same as the reflectance and transmittance of the incident light from below,
Because it is different in heterogeneous layers composed of multiple layers,
The reflectance, transmittance and transmittance of the incident light from above ($R^+, T^+$, $R^+, T^+$)
Distinguish between the reflectance and the transmittance of the incident light from below ($R^-, T^-$) and the reflectance of the incident light from below ($R^-, T^-$).
Now, in layer 1 above and layer 2 below, these
If $R^\pm_1, T\pm_1, \epsilon^\pm_1,
 R^\pm_2, T\pm_2, \epsilon^\pm_2$ are known,
Value in the composite layer
$R^\pm_{1,2}, T\pm_{1,2}, \epsilon^\pm_{1,2}$ is
It looks like the following.

$$
  R^+_{1,2}  =  R^+_1 + T^-_1 ( 1- R^+_2 R^-_1 )^{-1} R^+_2 T^+_1 \\
  R^-_{1,2}  =  R^-_2 + T^+_2 ( 1- R^+_1 R^-_2 )^{-1} R^-_1 T^-_2 \\
  T^+_{1,2}  =  T^+_2 ( 1- R^+_1 R^-_2 )^{-1} T^+_1 \\
  T^-_{1,2}  =  T^-_1 ( 1- R^+_1 R^-_2 )^{-1} T^-_2 \\
  \epsilon^+_{1,2}  =  \epsilon^+_2 
    + T^+_2 ( 1- R^+_2 R^-_1 )^{-1} ( R^-_1 \epsilon^-_2 + \epsilon^+_1 ) \\
  \epsilon^-_{1,2}  =  \epsilon^-_1 
    + T^-_1 ( 1- R^+_2 R^-_1 )^{-1} ( R^+_2 \epsilon^+_1 + \epsilon^-_2 ) 
$$







Let's say there are layers 1, 2, ...$N$ from the top.
However, the surface is considered to be a single layer and is the $N$ layer.
Reflectance and radiance of the layers from the $n$ to the $N$ are considered as a single layer source function
Given the $R^+_{n,N}, \epsilon^-_{n,N}$, $R^+_{n,N}, \epsilon^-_{n,N}$ ,

$$
  R^+_{n,N}  =  R^+_n 
      + T^-_n ( 1- R^+_{n+1,N} R^-_n )^{-1} R^+_{n+1,N} T^+_n \\
  \epsilon^-_{n,N}  =  \epsilon^-_n
    + T^-_n ( 1- R^+_{n,N} R^-_n )^{-1} 
      ( R^+_{n,N} \epsilon^+_n + \epsilon^-_{n,N} ) 
$$



This is the value at the surface

$$
  R^+_{N,N}  =   R^+_N = 2 {W^+}^2 \alpha_s \\
  \epsilon^-_{N,N}  =   \epsilon^-_N 
    = W^+ \left( 2 \alpha_s \mu_0 e^{-<\tau^*>/\mu_0} F_0 
                 + 2 \pi (1-\alpha_s) B_N 
          \right)
$$



It can be solved by $n=N-1, \ldots 1$ in sequence, starting from
However,

$$
  W^+ \equiv \mu^{1/2}
$$


In the next section, we consider the reflectance and source function of the layers from the first to the $n$ as a single layer
Given the $R^-_{1,n}, \epsilon^+_{1,n}$, $R^-_{1,n}, \epsilon^+_{1,n}$ ,

$$
  R^-_{1,n}  =  R^-_n 
      + T^+_n ( 1- R^+_{1,n-1} R^-_n )^{-1} R^-_{1,n-1} T^-_n \\
  \epsilon^+_{1,n}  =  \epsilon^+_n
    + T^+_n ( 1- R^+_{1,n-1} R^-_n )^{-1} 
      ( R^-_{1,n-1} \epsilon^-_n + \epsilon^+_{1,n-1} ) 
$$



and this is also $R^-_{1,1} = R^-_1, \epsilon^+_{1,1} = \epsilon^+_1$
It can be solved by $n=2, \ldots N$, starting from

With these ,
Downward flux at the boundary between layers $n$ and $n+1$ $u^+_{n,n+1}$
and upward flux $u^-_{n,n+1}$ is ,
$1\sim n$ The combination of layers and
$n+1\sim N$ Reduced to a matter between two layers of combined layers,

$$
 u^+_{n+1/2} = (1-R^-_{1,n} R^+_{n+1,N})^{-1}
    (\epsilon^+_{1,n} + R^-_{1,n} \epsilon^-_{n+1,N} ) \\
 u^-_{n+1/2} = R^+_{n+1,N}  u^+_{n,n+1} + \epsilon^-_{n+1,N}
$$



It can be written as.
However, the flux at the top of the atmosphere is not

$$
 u^+_{1/2}  =  0 \\
 u^-_{1/2}  =  \epsilon^-_{1,N}
$$



Finally, since this flux is scaled ,
We rescaled and added direct solar incidence to the
Find the radiation flux.

$$
  F^+_{n+1/2}  =  \frac{W^+}{\bar{W}} u^+_{n+1/2} 
                + \mu_0 e^{-<\tau^*>_{1,n}/\mu_0} F_0 \\\\
  F^-_{n+1/2}  =  \frac{W^+}{\bar{W}} u^-_{n+1/2} \\
$$





This calculation is done for each sub-channel.

### Add in the flux.

If the radiation flux $F^\pm_c$ is found for each subchannel in each layer, the
It corresponds to a wavelength representative of the subchannel
By applying a weight ($w_c$) and adding them together,
The wavelength-integrated flux is found.

$$
  \bar{F}^\pm = \sum_c w_c F^\pm
$$


In practice, the short wavelength range (solar region),
Divided into long wavelengths (earth's radiation region) and added together.
In addition, a part of the short wavelength region (shorter than the wavelength of $0.7\mu$)
The downward flux at the surface is obtained as PAR (photosynthetically active radiation).

### The temperature derivative of the flux

To solve for surface temperature by implicit,
Differential term of upward flux with respect to surface temperature
Calculating $dF^-/dT_g$.
Therefore, the value for temperatures 1K higher than $T_g$
We also obtained $\overline{B}^w(T_g+1)$ and used it to
Redo the flux calculation using the addition method,
The difference from the original value is set to $dF^-/dT_g$.
This is a meaningful value only in the long-wavelength region (Earth's radiation region).

### Handling of cloud cover

In the CCSR/NIES AGCM ,
Considering the horizontal coverage of clouds in a single grid.
There are two types of clouds

1. stratus cloud. Diagnosed by the large scale condensation scheme `MODULE:[LSCOND]`.
 For each layer ($n$), the lattice-averaged cloud water content of $l^l_n$ and
 The horizontal coverage factor (cloud cover) $C^l_n$ is defined.

2. cumulus clouds. Diagnosed by the cumulus convection scheme `MODULE:[CUMLUS]`.
 For each layer ($n$) the lattice-averaged cloud water content $l^c_n$ is defined, but
 Horizontal coverage (cloud cover) $C^c$ shall be constant in the vertical direction.

In these treatments, we assume that the stratocumulus clouds overlap randomly in a vertical direction,
Assuming that the cumulus cloud always occupies the same area in the upper and lower layers
(Assume that the cloud cover is 0 or 1 if it is confined to that region).
To do so, we perform the following calculations.

1. optical thickness of Rayleigh and particle scattering/absorption, etc.
     $\tau^s, \tau_s^s, g, f$,

     1. when cloud water of the $l^l_n/C^l_n$ exists (stratocumulus)

     2. when there are no clouds at all

     3. when cloud water in the cloud cover of $l^c_n/C^c$ is present (cumulus clouds)

 Calculate for.

2. reflection and transmission coefficients for each layer,
 The radiant source function (Planck function origin, insolation origin) is
 Calculate for each of the three cases above.
 The values for no clouds.
     $R^\circ$, in the case of stratus clouds $R^l$, in the case of cumulus clouds
     $R^c$ and so on.

3. reflection and transmission coefficients for each layer,
 The source function is averaged with the weight of the cloud cover of the stratocumulus, $C^l$.
 The averages are expressed by adding the $\bar{}$,

$$
        \bar{R}  =  ( 1 - C^l ) R^\circ + C^l R^l \\
        \bar{T}  =  ( 1 - C^l ) T^\circ + C^l T^l \\
        \bar{\epsilon}  =  
            ( 1 - C^l ) \epsilon_A^\circ + C^l \epsilon_A^l \\        
           +  
            \left[ ( 1 - C^l ) \epsilon_S^\circ + C^l \epsilon_S^l \right] 
            e^{-\overline{<\tau^*>}/\mu_0} F_0 
$$





 However, the However ,

$$
        e^{-\overline{<\tau^*>}/\mu_0} 
        = \Pi' \left[ ( 1 - C^l ) e^{-\tau^{*\circ}/\mu_0} 
                       + C_l e^{-\tau^{*l}/\mu_0} \right]
$$


 It is.
 Also,

$$
        \epsilon^\circ  =  \epsilon_A^\circ +
                             \epsilon_S^\circ 
                              e^{-<\tau^{*\circ}>/\mu_0} F_0 \\
        \epsilon^c      =  \epsilon_A^c +
                             \epsilon_S^c 
                              e^{-<\tau^{*c}>/\mu_0} F_0        
$$



 Seek also.

4. when the characteristic values of the average (e.g., $\bar{R}$) are used,
 When using a characteristic value without clouds (e.g., $R^\circ$),
 When the characteristic values of cumulus clouds (e.g., $R^c$) are used,
 fluxes by adding, respectively.
     Find $\bar{F}, F^\circ, F^c$.

5. the final flux we seek is

$$
        F = ( 1 - C^c ) \bar{F} + C^c F^c
$$


     ($F^\circ$ is used to estimate cloud radiative forcing
 I'm doing the math.)

### Incidence flux and angle of incidence `MODULE:[SHTINS]`

Incident Flux $F_0$ is ,
Solar constant, $F_{00}$,
The distance between the sun and the earth,
The ratio of the ratio to the time average is $r_s$.

$$
F_0 = F_00 r_s^-2 
$$


Here, $r_s$ asks for the following.

$$
  M \equiv 2 \pi ( d - d_0 ) 
$$


As ,

$$
  r_s = a_0 - a_1 \cos M - a_2 \cos 2M - a_3 \cos 3M
$$


Note that $d$ is the time in days since the beginning of the year.

The angle of incidence is obtained as follows.
Solar angle position $\omega_s$

$$
  \omega_s = M + b_1 \sin M + b_2 \sin 2M + b_3 \sin 3M
$$


As the solar declination $\delta_s$ is

$$
  \sin \delta_s = \sin \epsilon \sin ( \omega_s - \omega_0 ) 
$$


Then the angle of incidence factor $\mu = \cos \zeta$ (where $\zeta$ is the zenith angle) is

$$
\mu = \cos \zeta = \cos \varphi \cos \delta_s \cos h
                 + \sin \varphi \sin \delta_s
$$


$\varphi$ is a latitude,
$h$ is the time angle (local time minus $\pi$).

Assuming that the eccentricity of the Earth's orbit is $e$ (Katayama, 1974 ),

$$
   a_0  =   1 + e^2 \\
   a_1  =   e - 3/8 e^3 - 5/32 e^5 \\
   a_2  =   1/2 e^2 - 1/3e^4 \\
   a_3  =   3/8 e^3 - 135/64^5 \\
   b_1  =  2e - 1/4 e^3 + 5/96 e^5 \\
   b_2  =  5/4 e^2 - 11/24 e^4 \\
   b_3  =  13/12 e^3 - 645/940 e^5 \\
$$









It is also possible to give average annual insolation.
In this case, the annual mean incidence and the annual mean angle of incidence are
It approximates to be as follows.

$$
\overline{F} = F_{00}/\pi
$$


$$
\overline{\mu} \simeq 0.410 + 0.590 \cos^2 \varphi .
$$


### Other Notes.

The calculation of the radiation is usually not done at every step.
 To do so, we have to save the radiation flux,
 If the time is not used for radiation calculation, it is used.
 As for the shortwave radiation,
 Percentage of time (time that is $\mu_0>0$) between next calculation time and daylight hours $f$ and
 Using the solar incidence angle factor ($\bar{\mu_0}$) averaged over the daylight hours
 Seeking Flux $\bar{F}$,

$$
        F =  f \frac{\mu_0}{\bar{\mu_0}} \bar{F}
$$


 .

2. cloud water depends on the temperature,
 Treated as water and ice cloud particles.
 Percentage treated as ice clouds $f_I$ is ,

$$
        f_I = \frac{ T_0 - T }{ T_0 - T_1 }
$$


     (but with a maximum value of 1 and a minimum value of 0). Also,
     $T_0 = 273.15{K}, T_1 = 258.15{K}$.