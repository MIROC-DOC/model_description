## Radiant Flux.

### Summary of Radiation Flux Calculations

The CCSR/NIES AGCM radiation calculation scheme is based on the Discrete Ordinate Method and the k-Distribution Method. Considering the absorption, emission, and scattering processes of solar and terrestrial radiation due to gases, clouds, and aerosols, the values of radiation flux at each level are calculated. The main input data are air temperature ($T$), specific humidity ($q$), cloud water content ($l$), and cloud cover ($C$), and the output data are upward and downward radiation fluxes, $F^-, F^+$, and the derivative of upward radiation fluxes on the surface temperature The coefficient is $dF^-/dT_g$.

The computation is divided into several spectral regions. Each wavelength range is further divided into several subchannels based on the k-distribution method. For gas absorption, we adopt the band absorption of H$_2$O, CO$_2$, O$_3$, N$_2$O, CH$_4$, and the continuous absorption of H$_2$O, O$_2$, O$_3$, and CFC. As for scattering, the Rayleigh scattering of gases and scattering by cloud and aerosol particles are adopted.

The outline of the calculation procedure is as follows (subroutine names in parentheses).

1. calculate the Planck function from atmospheric temperature `MODULE:[PLANKS]`.

Calculates the optical thickness due to gas absorption in each subchannel `MODULE:[PTFIT]`.

3. calculate the optical thickness by continuous absorption and CFC absorption `MODULE:[CNTCFC]`.

4. calculate the optical thickness and scattering moments for Rayleigh scattering and particle scattering `MODULE:[SCATMM]`.

From the optical thickness and solar zenith angle of the scattering, we obtain the albedo of the sea surface `MODULE:[SSRFC]`.

6. for each subchannel, expand the Planck function by optical thickness `MODULE:[PLKEXP]`.

7. for each subchannel, calculate the transmission coefficient, reflection coefficient, and source function for each layer `MODULE:[TWST]`

8. calculate the radiative flux at the boundary of each layer by the adding method `MODULE:[ADDING]`

In order to take into account the partial cloud coverage, the transmission coefficients, reflection coefficients, and source functions are calculated separately for the cloud-covered and cloud-free cases, and averaged by multiplying the cloud cover weights. The cloud cover case and the cloud cover case are computed separately, and the cloud cover weight is multiplied by the weight of the cloud cover. We also calculate the clear sky radiation flux by adding several times.

### Wavelengths and Subchannels.

The basis of the radiative flux calculation is the Beer-Lambert's law

$$
  F^\lambda(z) = F^\lambda(0) exp (-k^\lambda z)
$$


. $F^\lambda$ is the radiant flux density at the wavelength $\lambda$. $k^\lambda$ is the absorption coefficient. In order to calculate the heating rate of the radiation flux, an integral operation for wavelengths is necessary.

$$
  F(z) = \int F^\lambda(z) d \lambda 
 = \int F^\lambda(0) exp (-k^\lambda z) d \lambda
$$


However, it is not easy to evaluate the integration of the absorption and emission of gas molecules in a precise manner because of the complicated wavelength dependence of the absorption line structure of the molecules. The k-distribution method has been developed for the purpose. Considering the density function $F(k)$ for the absorption coefficient $\lambda$ in the absorption coefficient $k$ in a certain wavelength range, (277) is calculated by

$$
 \int F^\lambda(0) exp (-k^\lambda z) d \lambda 
 \simeq \int \bar{F}^k(0) exp (-k z) F(k) dk
$$


which is approximated by where $bar{F}^k(0)$ is the flux averaged over a wavelength of $z=0$ with an absorption coefficient of $k$ in this wavelength range. This equation works well if $\bar{F}_k, F(k)$ are relatively smooth functions of $k$,

$$
 \int F^\lambda(0) exp (-k^\lambda z) d \lambda 
 \simeq \sum \bar{F}^i(0) exp (-k^i z) F^i
$$


We can compute relatively precisely the summation of a finite number of exponential terms (subchannels), as shown in This method has the additional advantage that it is easy to take into account absorption and scattering at the same time.

The CCSR/NIES AGCM can be run at various wavelengths by changing the radiation parameter data. In the current standard AGCM, the wavelength region is divided into 18 spectral divisions. Each wavelength region is divided into one to six subchannels (corresponding to the $i$ in the above equation), and the total number of subchannels is 37. The wavelength range is divided into 50, 250, 400, 400, 550, 770, 990, 1100, 1400, 2000, 2500, 4000, 14500, 31500, 33000, 34500, 36000, 43000, 46000, and 50000 in wavenumber (cm$^{-1}$).

### Calculating the Planck function `MODULE:[PLANKS]`

The Planck function $\overline{B}^w(T)$ integrated in each wavelength range is evaluated by the following equation.

$$
  \overline{B}^w(T) 
   = \lambda^{-2} T \exp \left\{ \sum_{n=0}{4} B^w_n (\bar{\lambda}^w T)^{-n}
                         \right\}
$$


$\bar{\lambda}^w$ is the average wavelength in the wavelength range, and $B^w_n$ is a parameter determined by function fitting. It is calculated for the atmospheric temperature ($T_l$) of each layer, the atmospheric temperature ($T_{l+1/2}$) of the boundary of each layer, and the surface temperature ($T_g$) of the ground surface.

In the following, the term $w$ for the wavelength range is basically omitted.

### Calculating the optical thickness by gas absorption `MODULE:[PTFIT]`

The optical thickness of the gas absorption is given by the index $m$ as follows

$$
  \tau^g = \sum_{m=1}{N_m} k^{(m)} C^{(m)}
$$


where $k^{(m)}$ is the absorption coefficient of the molecule $m$, which is different for each subchannel.

$$
 k^{(m)} = \exp\left\{ \sum_{i=0}{N_i} \sum_{j=0}{N_j} A^{(m)}_{ij}
                   (\ln p)^{i} (T-T_{STD})^{j}
               \right\}
$$


as a function of temperature $T$(K) and atmospheric pressure $p$(hPa). $C^{(m)}$ is the quantity of gas in the layer represented by mol cm$^{-2}$ and is given by the volume mixing ratio $r$ (in ppmv),

$$
  C = 1\times 10^{-5} \frac{p}{R_u T} \Delta z \cdot r
$$


This can be calculated as follows. Note that $R_u$ is the gas constant per mole (8.31 J mol$_{-1}$ K$^{-1}$) and the thickness of the gas layer ($\Delta z$) is measured in km. The volumetric mixing ratio ($r$) in ppmv can be calculated from the mass mixing ratio ($q$),

$$
  r = 10^6 R^{(m)}/R^{(air)} q = 10^6 M^{(air)}/M^{(m)}
$$


which can be converted by $R^{(m)},R^{(air)}$ are the gas constants per mass of the target molecule and atmosphere, respectively, and $M^{(m)},M^{(air)}$ are the average molecular weights of the target molecule and atmosphere, respectively.

This calculation is done for each sub-channel and each layer.

### Optical Thickness by Continuous Absorption and CFC Absorption `MODULE:[CNTCFC]`

The optical thickness of the optical thickness of H$_2$O by continuous absorption in $\tau^{H_2O}$ is considered to be due to the dimer and is basically evaluated in proportion to the square of the volume mixing ratio of the water vapor.

$$
\tau^{H_2O} = ( A^{H_2O} + f(T) \hat{A}^{H_2O} ) (r^{H_2O})^2 \rho \Delta z
$$


$f(T)$ in $\hat{A}$ expresses the temperature dependence of absorption of the dimer. In addition, a contribution proportional to the square of the volume mixing ratio of water vapor is incorporated in the wavelength range where normal gas absorption is ignored.

The continuous absorption of O$_2$ is assumed to be constant in the mixing ratio,

$$
\tau^{O_2} = A^{O_2} \rho \Delta z
$$


.

Continuous absorption of O$_3$ is achieved by using the mixing ratio $r^{O_3}$ and incorporating the temperature dependence,

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


where $e^R$ is the dissipation coefficient of Rayleigh scattering, $e^{(p)}$ is the dissipation coefficient of the particle $p$, and $r^{(p)}$ is the volume mixing ratio of the particle $p$ converted to the standard state.

The conversion from the mass mixing ratio of cloud water ($l$) to the standard state-change volume mixing ratio of cloud particles (ppmv) is as follows

$$
  r = 10^6 \frac{p_{STD}}{R T_{STD}}/\rho_w
$$


However, $\rho_w$ is the density of cloud particles.

On the other hand, the scattering-induced part of the optical thickness, $\tau_s^s$, is

$$
\tau_s^{s} 
 = \left( s^R + \sum_{p=1}{N_p} s^{(p)}_m r^{(p)}\right) \rho \Delta z
$$


where $s^R$ is the scattering coefficient for Rayleigh scattering and $s^{(p)}$ is the scattering coefficient for the particle $p$.

The normalized scattering moments $g$ (asymmetric factor) and $f$ (forward scattering factor) are not the same as those of the

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


where $g^R, f^R$ are the scattering moments of Rayleigh scattering, and $g^{(p)}, f^{(p)}$ are the scattering moments of the particles $p$.

This calculation is performed for each wavelength range and each layer.

### Albedo at Sea Level `MODULE:[SSRFC]`

Albedo $\alpha_s$ at sea level is obtained by adding the optical thickness of the scattered signal vertically to $<\tau^{s}>$ and using the solar incidence angle factor $\mu_0$,

$$
  \alpha_s = \exp\left\{ \sum_{i,j} C_{ij} {\mathcal T}^j {\mu_0}^j \right\}
$$


However, it is expressed as However,

$$
 {\mathcal T} = ( 4 <\tau^{s}>/\mu )^{-1}
$$


It is.

This calculation is done for each wavelength.

### Total Optical Thickness.

The optical thickness, taking into account all gas band absorption, continuous absorption, Rayleigh scattering, and particle scattering and absorption, is about

$$
  \tau = \tau^g + \tau^{CON} + \tau^{s}
$$


where $\tau^g$ is different for each subchannel and each layer is calculated separately. Here, since $\tau^g$ is different for each subchannel, the calculation is performed for each subchannel and each layer.

### Planck function expansion `MODULE:[PLKEXP]`

In each layer, the Planck function $B$ is

$$
  B(\tau') = b_0 + b_1 \tau' + b_2 \left(\tau'\right)^2
$$


and obtain the expansion coefficients $b_0, b_1, b,2$. Here, $B$ at the upper end of each layer (the boundary with the upper layer) is used as $B(0)$, $B$ at the lower end of each layer (the boundary with the lower layer) is used as $B(\tau)$, and $B$ at the representative level of each layer is used as $B(\tau/2)$.

$$
  b_0  =  B(0)  \\
  b_1  =  ( 4B(\tau/2) - B(\tau) - 3B(0) )/\tau  \\
  b_2  =  2 ( B(\tau) + B(0) - 2B(\tau/2) )/\tau^2  
$$




This calculation is done for each sub-channel and each layer.

### Transmission and reflection coefficients of each layer, the source function `MODULE:[TWST]`

Using the obtained optical thickness $\tau$, the scattering optical thickness $\tau^s$, the scattering moments $g, f$, the expansion coefficients of the Planck function $b_0, b_1, b_2$, and the solar incidence angle factor $\mu_0$, we obtain a uniform layer of Assuming that the transmission coefficient ($R$), the reflection coefficient ($T$), the downward radiation source function ($\epsilon^+$), and the upward radiation source function ($\epsilon^-$) are obtained by the two-stream approximation.

The single-scattering albedo $\omega$ is a ,

$$
  \omega = \tau_s^s/\tau
$$


The optical thickness corrected for contributions from the forward scattering factor $f$ $\tau^*$, the single-scattering albedo $\omega^*$, and the asymmetry factor $g^*$ are all in the same order,

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



However, $\mu$ is a two-stream directional cosine,

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





the reflection coefficient ($R$) and the transmission coefficient ($T$) are

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

The source functions of both Planck's and solar-induced origins are

$$
  \epsilon^\pm  = 
  \epsilon_A^\pm + \hat{\epsilon}_S^\pm e^{-<\tau^*>/\mu_0} F_0 \\
$$


This value is the total optical thickness of $<\tau^*>$ from the top of the atmosphere to the top of the layer under consideration, where $F_0$ is the incident flux in the wavelength range under consideration. Note that the $<\tau^*>$ is the total optical thickness of the $\tau^*$ from the top of the atmosphere to the top of the layer under consideration, and the $F_0$ is the incident flux in the considered wavelength range. That is, $e^{-<\tau^*>/\mu_0} F_0$ is the incident flux at the top of the layer under consideration. This calculation does not actually work in practice,

$$
  e^{-<\tau^*>/\mu_0} = \Pi' e^{-\tau^*/\mu_0}
$$


We do as follows. $\Pi'$ is the product of the topmost layer of the atmosphere to the layer above the one we are considering.

This calculation is done for each sub-channel and each layer.

### Radiation flux at each layer boundary `MODULE:[ADDING]`

Once the transmission coefficient ($R_l$), reflection coefficient ($T_l$), and source function ($\epsilon^\pm_l$) of each layer are obtained for all layers ($l$), the radiation flux at the boundary of each layer can be calculated using the adding method. This is based on the fact that, if the $R,T,\epsilon$ of the two layers are known, the total $R,T,\epsilon$ of the combined layer can be obtained by a simple calculation. In the homogeneous layer, the reflectance and transmittance of the upper incident layer are the same as that of the lower incident layer, and the transmittance and reflectance of the lower incident layer are the same as those in the homogeneous layer, but in the heterogeneous layer composed of multiple layers, the reflectance and transmittance of the upper incident layer ($R^+, T^+$) and the reflectance and transmittance of the lower incident layer ($R^+, T^+$) are different, so that we can obtain Distinguish between $R^-, T^-$. Now, if these values of $R^\pm_1, T\pm_1, \epsilon^\pm_1,
 R^\pm_2, T\pm_2, \epsilon^\pm_2$ are known in the upper layer1 and the lower layer2, the combined layer values of $R^\pm_{1,2}, T\pm_{1,2}, \epsilon^\pm_{1,2}$ are as follows.

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







It is assumed that there are layers 1, 2, ...and $N$ from the top. However, the surface is considered to be a single layer, and the $N$ is assumed to be the first $N$ layer. Considering the reflection coefficient and the radiation source functions ($R^+_{n,N}, \epsilon^-_{n,N}$) of the $n$ to $N$ layers as a single layer, we assume that the surface of the Earth is a single layer and is defined as the $N$ layer,

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



and can be solved by $n=N-1, \ldots 1$ in sequence, starting from However,

$$
  W^+ \equiv \mu^{1/2}
$$


Next, considering the reflectance and the emissivity functions ($R^-_{1,n}, \epsilon^+_{1,n}$) for the layers from the first to the $n$st layer as a single layer, we find that

$$
  R^-_{1,n}  =  R^-_n 
      + T^+_n ( 1- R^+_{1,n-1} R^-_n )^{-1} R^-_{1,n-1} T^-_n \\
  \epsilon^+_{1,n}  =  \epsilon^+_n
    + T^+_n ( 1- R^+_{1,n-1} R^-_n )^{-1} 
      ( R^-_{1,n-1} \epsilon^-_n + \epsilon^+_{1,n-1} ) 
$$



and this can also be solved by $n=2, \ldots N$ starting from $R^-_{1,1} = R^-_1, \epsilon^+_{1,1} = \epsilon^+_1$.

Using these, the downward flux $u^+_{n,n+1}$ and the upward flux $u^-_{n,n+1}$ at the boundary between layers $n$ and $n+1$ are reduced to a problem between the two layers, the combined layer $1\sim n$ and the combined layer $n+1\sim N$,

$$
 u^+_{n+1/2} = (1-R^-_{1,n} R^+_{n+1,N})^{-1}
    (\epsilon^+_{1,n} + R^-_{1,n} \epsilon^-_{n+1,N} ) \\
 u^-_{n+1/2} = R^+_{n+1,N}  u^+_{n,n+1} + \epsilon^-_{n+1,N}
$$



which can be written as However, the flux at the upper end of the atmosphere can be written as

$$
 u^+_{1/2}  =  0 \\
 u^-_{1/2}  =  \epsilon^-_{1,N}
$$



Finally, since this flux is scaled, we rescale it and add direct solar incidence to obtain the radiative flux.

$$
  F^+_{n+1/2}  =  \frac{W^+}{\bar{W}} u^+_{n+1/2} 
                + \mu_0 e^{-<\tau^*>_{1,n}/\mu_0} F_0 \\\\
  F^-_{n+1/2}  =  \frac{W^+}{\bar{W}} u^-_{n+1/2} \\
$$





This calculation is done for each sub-channel.

### Add in the flux.

Once the radiation flux ($F^\pm_c$) for each subchannel of each layer is obtained, the wavelength-integrated flux is obtained by multiplying the flux by the weight ($w_c$) corresponding to the wavelength of the representative subchannel and adding them together.

$$
  \bar{F}^\pm = \sum_c w_c F^\pm
$$


In practice, we add the fluxes in the short wavelength region (solar region) and the long wavelength region (terrestrial radiation region) to each other. In addition, we obtain PAR (photosynthetically active radiation) as the downward flux at the earth's surface in a part of the short wavelength region (shorter than the wavelength of $0.7\mu$).

### The temperature derivative of the flux

In order to solve the surface temperature by implicitly, we calculate the differential term $dF^-/dT_g$ of the upward-flowing flux to the surface temperature. For this purpose, we also obtain the value of $\overline{B}^w(T_g+1)$, which is 1K higher than that of $T_g$, and recalculate the flux by the addition method using that value, and obtain the difference from the original value as $dF^-/dT_g$. This value is meaningful only in the long wavelength region (earth's radiation region).

### Handling of cloud cover

The CCSR/NIES AGCM considers the horizontal coverage of clouds in a grid. The two types of clouds are as follows.

1. stratus cloud. The large-scale condensation scheme `MODULE:[LSCOND]` is used to diagnose these clouds. For each layer ($n$) the grid-averaged cloud water content ($l^l_n$) and the horizontal coverage (cloud cover) ($C^l_n$) are defined for each layer ($n$).

2. cumulus clouds. Diagnosed with the cumulus convection scheme `MODULE:[CUMLUS]`. For each layer ($n$) the grid-averaged cloud cover ($l^c_n$) is defined, but the horizontal coverage (cloud cover) $C^c$ is assumed to be constant in the vertical direction.

In these treatments, it is assumed that the stratocumulus clouds randomly overlap vertically, and that the cumulus clouds always occupy the same area in the upper and lower layers (and that the cloud cover is assumed to be zero or one if it is restricted to that area). For this purpose, the calculation is performed as follows.

1. optical thickness of Rayleigh and particle scattering/absorption etc. $\tau^s, \tau_s^s, g, f$,

     1. the presence of clouds and water in the cloud cover of $l^l_n/C^l_n$ (stratocumulus)

     2. when there are no clouds at all

     3. when cloud water of $l^c_n/C^c$ is present (cumulus clouds)

 Calculate for.

We calculate the reflection coefficient, transmission coefficient, and radiation function (origin of Planck's function and origin of solar radiation) for each layer for the three cases above. The value for the case without clouds is set to $R^\circ$, the case with stratus clouds is set to $R^l$, the case with cumulus clouds is set to $R^c$, and so on.

3. the reflection coefficient, transmission coefficient, and radiative function of each layer are averaged with the weight of the cloud cover of the stratocumulus ($C^l$). Expressing the averaged values with the $\bar{}$

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


 It is. Also ,

$$
        \epsilon^\circ  =  \epsilon_A^\circ +
                             \epsilon_S^\circ 
                              e^{-<\tau^{*\circ}>/\mu_0} F_0 \\
        \epsilon^c      =  \epsilon_A^c +
                             \epsilon_S^c 
                              e^{-<\tau^{*c}>/\mu_0} F_0        
$$



 Seek also.

Fluxes $\bar{F}, F^\circ, F^c$ are calculated for the cases with the characteristic values of average (e.g., $\bar{R}$), without clouds (e.g., $R^\circ$), and cumulus (e.g., $R^c$) by using the ading method, respectively.

5. the final flux we seek is

$$
        F = ( 1 - C^c ) \bar{F} + C^c F^c
$$


     ($F^\circ$ is calculated to estimate cloud radiative forcing.)

### Incidence flux and angle of incidence `MODULE:[SHTINS]`

The incident flux $F_0$ is defined as the ratio of the solar constant ($F_{00}$) and the distance between the sun and the earth to the time-averaged value ($r_s$).

$$
F_0 = F_00 r_s^-2 
$$


Here, $r_s$ asks the following.

$$
  M \equiv 2 \pi ( d - d_0 ) 
$$


As ,

$$
  r_s = a_0 - a_1 \cos M - a_2 \cos 2M - a_3 \cos 3M
$$


Note that $d$ is expressed in days from the beginning of the year.

The angle of incidence is obtained as follows. Find the angular position of the sun, $\omega_s$, as

$$
  \omega_s = M + b_1 \sin M + b_2 \sin 2M + b_3 \sin 3M
$$


As the solar declination $\delta_s$ is

$$
  \sin \delta_s = \sin \epsilon \sin ( \omega_s - \omega_0 ) 
$$


Then the angle of incidence factor $\mu = \cos \zeta$ ($\zeta$ is the zenith angle) is

$$
\mu = \cos \zeta = \cos \varphi \cos \delta_s \cos h
                 + \sin \varphi \sin \delta_s
$$


$\varphi$ is the latitude and $h$ is the time angle (local time minus $\pi$).

Assuming that the eccentricity of the Earth's orbit is $e$ (Katayama, 1974),

$$
   a_0  =   1 + e^2 \\
   a_1  =   e - 3/8 e^3 - 5/32 e^5 \\
   a_2  =   1/2 e^2 - 1/3e^4 \\
   a_3  =   3/8 e^3 - 135/64^5 \\
   b_1  =  2e - 1/4 e^3 + 5/96 e^5 \\
   b_2  =  5/4 e^2 - 11/24 e^4 \\
   b_3  =  13/12 e^3 - 645/940 e^5 \\
$$









It is also possible to give the annual mean solar radiation. In this case, the mean annual incidence and the mean annual angle of incidence are approximately as follows

$$
\overline{F} = F_{00}/\pi
$$


$$
\overline{\mu} \simeq 0.410 + 0.590 \cos^2 \varphi .
$$


### Other Notes.

The calculation of the radiation is usually not done at every step. For this reason, we save the radiation flux and use it for the time when the radiation calculation is not performed. For the short-wave radiation, the flux ($\bar{F}$) is calculated by using the ratio of the time of daylight between the next calculation time and the time of the next calculation ($\mu_0>0$) as a percentage of the time of daylight (the time of $\mu_0>0$) and the solar incidence angle factor ($\bar{\mu_0}$) averaged over the daylight period,

$$
        F =  f \frac{\mu_0}{\bar{\mu_0}} \bar{F}
$$


 .

Cloud water is treated as water and ice clouds depending on the temperature. The fraction treated as ice clouds $f_I$ is

$$
        f_I = \frac{ T_0 - T }{ T_0 - T_1 }
$$


     (but with a maximum value of 1 and a minimum value of 0). Let $T_0 = 273.15{K}, T_1 = 258.15{K}$ be set to $T_0 = 273.15{K}, T_1 = 258.15{K}$.
