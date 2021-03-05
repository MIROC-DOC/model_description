## Summary of the dynamical core

In this section, we enumerate the calculations performed in the dynamical core, although they overlap with the previous descriptions.

### Conversion of Horizontal Wind to Vorticity and Divergence `[G2Wpush, G2Wtrans, G2Wshift, W2Gpush, W2Gtrans, W2Gshift (xdsphe.F)]`

Obtain grid point values of vorticity and divergence from the grid point values of $u_{ij}, v_{ij}$ for horizontal wind. First, we obtain the vorticity and divergence in spectral space,  $\zeta_n^m, D_n^m$,

$$
\zeta_n^m  =  \frac{1}{I} \sum_{i=1}^{I} \sum_{j=1}^{J}  
                  \mathrm{i}m v_{ij} \cos\varphi_j {Y_n^{m*}}_{ij}
                \frac{w_j}{a(1-\mu_j^{2})}
           +    \frac{1}{I} \sum_{i=1}^{I} \sum_{j=1}^{J}  
                     u_{ij} \cos\varphi_j (1-\mu_j^2)
                  \frac{\partial }{\partial \mu} {Y_n^{m*}}_{ij}
                 \frac{w_j}{a(1-\mu_j^{2})} \; ,
$$

$$
    D_n^m  =  \frac{1}{I} \sum_{i=1}^{I} \sum_{j=1}^{J}  
                  \mathrm{i}m u_{ij} \cos\varphi_j {Y_n^{m*}}_{ij}
                \frac{w_j}{a(1-\mu_j^{2})}
           -    \frac{1}{I} \sum_{i=1}^{I} \sum_{j=1}^{J}  
                  v_{ij} \cos\varphi_j  (1-\mu_j^2)
                  \frac{\partial }{\partial \mu} {Y_n^{m*}}_{ij}
                 \frac{w_j}{a(1-\mu_j^{2})} ; .
$$


The grid point value is calculated by

$$
  \zeta_{ij}
   =  {\mathcal R}{\mathbf{e}} \sum_{m=-N}^{N} \sum_{n=|m|}^{N}
      \zeta_n^m  {Y_n^m}_{ij} \; ,
$$


and so on.

### Calculating a virtual temperature `[VIRTMD (dvtmp.F)]`

virtual Temperature $T_v$ is ,

$$
  T_v = T ( 1 + \epsilon_v q - l ) \; ,
$$


However, it is $\epsilon_v = R_v/R - 1$ and $R_v$ is the gas constant for water vapor (461 Jkg$^{-1}$K$^{-1}$) and $R$ is the gas constant for air (287.04 Jkg$^{-1}$K$^{-1}$).

### Calculating the pressure gradient term `[PSDOT (dgdyn.F)]`

The pressure gradient term $\nabla \pi = \frac{1}{p_S} \nabla p_S$ is first used to define the $\pi_n^m$

$$
  \pi_n^m  =  \frac{1}{I} \sum_{i=1}^{I} \sum_{j=1}^{J}  
               (\ln {p_S})_{ij} {Y_n^{m *}}_{ij}  w_j \; ,
$$

to a spectral representation and then ,

$$
   \frac{1}{a \cos \varphi}
   \left( \frac{\partial \pi}{\partial \lambda} \right)_{ij}
     =
   \frac{1}{a \cos \varphi}
        {\mathcal R}{\mathbf{e}} \sum_{m=-N}^{N} \sum_{n=|m|}^{N}
       \mathrm{i}m \tilde{X}_n^m {Y_n^m}_{ij}  \; ,
$$


$$
   \frac{1}{a}
   \left( \frac{\partial \pi}{\partial \varphi} \right)_{ij}
     =  
   \frac{1}{a \cos \varphi}
       {\mathcal R}{\mathbf{e}} \sum_{m=-N}^{N} \sum_{n=|m|}^{N}
       \pi_n^m
       ( 1-\mu^{2} ) \frac{\partial }{\partial \mu} {Y_n^m}_{ij}  \; .
$$


### Diagnosis of vertical flow. `[PSDOT (dgdyn.F)]`

Pressure change term, and lead DC,

$$
  \frac{\partial \pi}{\partial t}
   = - \sum_{k=1}^{K} \left\{ D_k \Delta\sigma_k + ({\mathbf{v}}_k \cdot \nabla \pi)\Delta B_k \right\}
$$

$$
  \frac{(m\dot{\eta})_{k-1/2}}{p_s}
   = - B_{k-1/2} \frac{\partial \pi}{\partial t}
    - \sum_{l=k}^{K}\left\{ D_l \Delta\sigma_l + ({\mathbf{v}}_l \cdot \nabla \pi)\Delta B_l \right\}
$$


and its non-gravity components.

$$
  \left( \frac{\partial \pi}{\partial t} \right)^{NG}
   =   - \sum_{k=1}^{K} {\mathbf{v}}_{k} \cdot \nabla \pi  
       \Delta B_{k}
$$

$$
  \frac{(m\dot{\eta})^{NG}_{k-1/2}}{p_s}
   = - B_{k-1/2} \left( \frac{\partial \pi}{\partial t} \right)^{NG}
    - \sum_{l=k}^{K} {\mathbf{v}}_{l} \cdot \nabla \pi
       \Delta B_{l}
$$

### Tendency terms due to advection  `[GRTADV, GRUADV (dgdyn.F)]`

Momentum advection term:

$$
  (A_u)_k
    =  ( \zeta_k + f ) v_k 
             - \left[ \frac{(m\dot{\eta})_{k-1/2}}{p_s} \frac{u_{k-1} - u_k}{\Delta\sigma_{k-1}+\Delta\sigma_k}
               + \frac{(m\dot{\eta})_{k+1/2}}{p_s} \frac{u_k   - u_{k+1}}{\Delta\sigma_{k}+\Delta\sigma_{k+1}} \right]
$$
$$
           - \frac{1}{a\cos\varphi} \frac{\partial \pi}{\partial \lambda}(C_p T_{v,k}\hat{\kappa}-R\bar{T})
             + {\mathcal F}_x
$$

$$
  (A_v)_k
    =  - ( \zeta_k + f ) u_k 
             - \left[ \frac{(m\dot{\eta})_{k-1/2}}{p_s} \frac{v_{k-1} - v_k}{\Delta\sigma_{k-1}+\Delta\sigma_k}
               + \frac{(m\dot{\eta})_{k+1/2}}{p_s} \frac{v_k   - v_{k+1}}{\Delta\sigma_{k}+\Delta\sigma_{k+1}} \right]
$$
$$
           - \frac{1}{a} \frac{\partial \pi}{\partial \varphi}(C_p T_{v,k}\hat{\kappa}-R\bar{T})
             + {\mathcal F}_y
$$

Temperature advection term:

$$
 (u T')_k  = u_k (T_k - \bar{T} )
$$

$$
 (v T')_k  = v_k (T_k - \bar{T} )
$$

$$
   H_k =  T_k' D_k 
          - \left[ \frac{(m\dot{\eta})_{k-1/2}}{p_s} \frac{\hat{T}_{k-1/2} - T_k}{\Delta \sigma_l}
               + \frac{(m\dot{\eta})_{k+1/2}}{p_s} \frac{T_k - \hat{T}_{k+1/2}}{\Delta \sigma_l} \right]
$$
$$
        + \hat{\kappa}_k {\mathbf{v}}_k \cdot \nabla \pi T_{v,k} 
$$
$$
        - \alpha_k \sum_{l=k}^{K} 
                           (D_l \Delta \sigma_l + ({\mathbf{v}}_l \cdot \nabla \pi)\Delta B_l)
                            \frac{T_{v,k}}{\Delta \sigma_k} 
$$
$$
        - \beta_k \sum_{l=k+1}^{K} 
                           (D_l \Delta \sigma_l + ({\mathbf{v}}_l \cdot \nabla \pi)\Delta B_l)
                            \frac{T_{v,k}}{\Delta \sigma_k}
$$

Water vapor advection term:

$$
 (u q)_k  = u_k q_k
$$

$$
 (v q)_k  = v_k q_k
$$

$$
R_k  =  q_k D_k 
       - \frac{1}{2} 
             \left[   \frac{(m\dot{\eta})_{k-1/2}}{p_s} \frac{q_{k-1} - q_k}{\Delta\sigma_k}
               + \frac{(m\dot{\eta})_{k+1/2}}{p_s} \frac{q_k   - q_{k+1}}{\Delta\sigma_k} \right]
$$

### Transformation of prognostic variables to spectral space `[G2Wpush, G2Wtrans, G2Wshift (xdsphe.F)]`

(122) and (123).

Transform $u_{ij}^{t-\Delta t}, v_{ij}^{t-\Delta t}$ to a spectral representation of vorticity and divergence $\zeta_n^m, D_n^m$. Furthermore, transforming the temperature $T^{t-\Delta t}$, specific humidity $q^{t-\Delta t}$, and $\pi = \ln p_S^{t-\Delta t}$ to

$$
  X_n^m  =  \frac{1}{I} \sum_{i=1}^{I} \sum_{j=1}^{J}  
               X_{ij} {Y_n^{m *}}_{ij}  w_j \; ,
$$


to a spectral representation.

### Transformation of tendency terms to spectral space `[G2Wpush, G2Wtrans, G2Wshift (xdsphe.F)]`

Tendency Term of Vorticity


$$
  \frac{\partial{\zeta_n^m}}{\partial {t}}
    =  \frac{1}{I} \sum_{i=1}^{I} \sum_{j=1}^{J}  
    \mathrm{i}m (A_v)_{ij} \cos \varphi_j
    {Y_n^{m *}}_{ij}
    \frac{w_j}{a(1-\mu_j^{2})}
\\
  +\frac{1}{I} \sum_{i=1}^{I} \sum_{j=1}^{J}  
    (A_u)_{ij} \cos \varphi_j
    (1-\mu_j^2)
    \frac{\partial }{\partial \mu} {Y_n^{m *}}_{ij}
    \frac{w_j}{a(1-\mu_j^{2})}
$$



The non-gravity wave component of the tendency term of the divergence

$$
  \left( \frac{\partial{D_n^m}}{\partial {t}} \right)^{NG}
   =  \frac{1}{I} \sum_{i=1}^{I} \sum_{j=1}^{J}  
          \mathrm{i}m (A_u)_{ij} \cos \varphi_j
          {Y_n^{m *}}_{ij}
         \frac{w_j}{a(1-\mu_j^{2})}
          \\
   -\frac{1}{I} \sum_{i=1}^{I} \sum_{j=1}^{J}  
          (A_v)_{ij} \cos \varphi_j
          (1-\mu_j^2)
          \frac{\partial }{\partial \mu} {Y_n^{m *}}_{ij}
          \frac{w_j}{a(1-\mu_j^{2})}
          \\
   -\frac{n(n+1)}{a^{2}}
         \frac{1}{I} \sum_{i=1}^{I} \sum_{j=1}^{J}  
          \hat{E}_{ij}  {Y_n^{m *}}_{ij} w_j
          \\
$$





The non-gravity wave component of the tendency term of temperature

$$
  \left( \frac{\partial{T_n^m}}{\partial {t}} \right)^{NG}
   =  - \frac{1}{I} \sum_{i=1}^{I} \sum_{j=1}^{J}  
          \mathrm{i}m (u T')_{ij} \cos \varphi_j
          {Y_n^{m *}}_{ij}
         \frac{w_j}{a(1-\mu_j^{2})}
          \\
     + \frac{1}{I} \sum_{i=1}^{I} \sum_{j=1}^{J}  
          (v T')_{ij} \cos \varphi_j
          (1-\mu_j^2)
          \frac{\partial }{\partial \mu} {Y_n^{m *}}_{ij}
          \frac{w_j}{a(1-\mu_j^{2})}
          \\
     + \frac{1}{I} \sum_{i=1}^{I} \sum_{j=1}^{J}  
          \hat{H}_{ij}
          {Y_n^{m *}}_{ij} w_j
$$




Tendency term of water vapor

$$
  \frac{\partial{q_n^m}}{\partial {t}}
   =  - \frac{1}{I} \sum_{i=1}^{I} \sum_{j=1}^{J}  
          \mathrm{i}m (uq)_{ij} \cos \varphi_j
          {Y_n^{m *}}_{ij}
         \frac{w_j}{a(1-\mu_j^{2})}
          \\
     + \frac{1}{I} \sum_{i=1}^{I} \sum_{j=1}^{J}  
          (vq)_{ij} \cos \varphi_j
          (1-\mu_j^2)
          \frac{\partial }{\partial \mu} {Y_n^{m *}}_{ij}
          \frac{w_j}{a(1-\mu_j^{2})}
          \\
     + \frac{1}{I} \sum_{i=1}^{I} \sum_{j=1}^{J}  
          R_{ij}
          {Y_n^{m *}}_{ij} w_j
$$




### Time integration in spectral space `[TINTGR (dintg.F)]`

Equations in matrix form

$$
      \left\{ ( 1+2\Delta t {\mathcal D}_H )( 1+2\Delta t {\mathcal D}_M )
           \underline{I}  
      - ( \Delta t )^{2}  ( \underline{W} \ \underline{h}
           + (1+2\Delta t {\mathcal D}_M)
             {\mathbf{G}} {\mathbf{C}}^{T} ) \nabla^{2}_{\sigma}
  \right\}
      \overline{ {\mathbf{D}} }^{t}
       \\
  = ( 1+2\Delta t {\mathcal D}_H )( 1-\Delta t {\mathcal D}_M )
       {\mathbf{D}}^{t-\Delta t}
  +\Delta t
         \left( \frac{\partial {\mathbf{D}}}{\partial t} \right)_{NG}  
  \\
  -\Delta t \nabla^{2}_{\sigma}     
                   \left\{  ( 1+2\Delta t {\mathcal D}_H ) {\mathbf{\Phi}}_{S}
                          + \underline{W}
                            \left[ ( 1-2\Delta t {\mathcal D}_H )
                                    {\mathbf{T}}^{t-\Delta t}
                                  + \Delta t
                                      \left( \frac{\partial {\mathbf{T}}}
                                                  {\partial t}     
                                      \right)_{NG} \right]
                   \right.
  \\
                 \left.  \hspace*{20mm}
                          + ( 1+2\Delta t {\mathcal D}_H ) {\mathbf{G}}
                            \left[ \pi^{t-\Delta t}
                                  + \Delta t
                                     \left( \frac{\partial \pi}
                                                 {\partial t}
                                     \right)_{NG}  \right]
                   \right\} .
$$





Using LU decomposition, $\bar{D}$ is obtained by solving for

$$
  \frac{\partial {\mathbf{T}}}{\partial t}
      =   \left( \frac{\partial {\mathbf{T}}}
                        {\partial t}       \right)_{NG}  
         - \underline{h} {\mathbf{D}}
$$


$$
  \frac{\partial \pi}{\partial t}
      =   \left( \frac{\partial \pi}
                        {\partial t}       \right)_{NG}  
         - {\mathbf{C}} \cdot {\mathbf{D}}
$$


Calculate the value of the spectrum in $\partial {\mathbf{T}}/\partial t$, $\partial \pi/\partial t$ and then calculate the value of the spectrum in $t+\Delta t$ using

$$
  \zeta^{t+\Delta t}  =  \left( \zeta^{t-\Delta t}
                                +   2 \Delta t \frac{\partial{\zeta}}{\partial {t}} \right)
                          ( 1 + 2 \Delta t {\mathcal D}_M )^{-1} \\
  D^{t+\Delta t}  =  2 \bar{D} - D^{t-\Delta t}\\
  T^{t+\Delta t}  =  \left( T^{t-\Delta t}
                                +  2 \Delta t  \frac{\partial{T}}{\partial {t}} \right)
                          ( 1 + 2 \Delta t {\mathcal D}_H )^{-1} \\
  q^{t+\Delta t}  =  \left( q^{t-\Delta t}
                                +  2 \Delta t \frac{\partial{q}}{\partial {t}} \right)
                          ( 1 + 2 \Delta t {\mathcal D}_E )^{-1} \\
\pi^{t+\Delta t}  =  \pi^{t-\Delta t}
                                +  2 \Delta t \frac{\partial{\pi}}{\partial {t}}
$$






### Transformation of prognostic variables to grid point Values `[W2Gpush, W2Gtrans, W2Gshift (xdsphe.F)]`

Obtain grid values of horizontal wind speed from the spectral values of vorticity and divergence ($\zeta_n^m, D_n^m$) $u_{ij}, v_{ij}$.

$$
  u_{ij}
  =  \frac{1}{\cos \varphi_j}
     {\mathcal R}{\mathbf{e}} \sum_{m=-N}^{N}
                       \sum_{\stackrel{n=|m|}{n \neq 0}}^{N}
    \left\{
             \frac{a}{n(n+1)} \zeta_n^m
            (1-\mu^{2}) \frac{\partial{}}{\partial {\mu}} {Y_n^m}_{ij}
          -  \frac{\mathrm{i}m a}{n(n+1)} D_n^m {Y_n^m}_{ij}
    \right\}
$$


$$
  v_{ij}
  =  \frac{1}{\cos \varphi_j}
     {\mathcal R}{\mathbf{e}} \sum_{m=-N}^{N}
                       \sum_{\stackrel{n=|m|}{n \neq 0}}^{N}
    \left\{
          -  \frac{\mathrm{i}m a}{n(n+1)} \zeta_n^m  {Y_n^m}_{ij}
          -  \frac{a}{n(n+1)} \tilde{D}_n^m
            (1-\mu^{2}) \frac{\partial{}}{\partial {\mu}} {Y_n^m}_{ij}
    \right\}
$$


Furthermore,

$$
  T_{ij}
   =  {\mathcal R}{\mathbf{e}} \sum_{m=-N}^{N} \sum_{n=|m|}^{N}
      T_n^m  {Y_n^m}_{ij} \; ,
$$


$T_{ij}, \pi_{ij}, q_{ij}$, and so on,

$$
  {p_S}_{ij} = \exp \pi_{ij}
$$


to calculate.

### Diffusion Correction along pressure level `[CORDIF (ddifc.F)]`

The horizontal diffusion is applied on the surface of $\eta-$plane, but it can cause problems in large slopes, such as transporting water vapor uphill and causing false precipitation at the top of a mountain. To mitigate this problem, corrections have been made for $T,q,l$ to make the diffusion closer to that of the $p$ surface, e.g., for $T,q,l$.

$$
  {\mathcal D}_p (T) = (-1)^{N_D/2} K \nabla^{N_D}_p T  
                \simeq  (-1)^{N_D/2} K \nabla^{N_D}_{\eta} T  
                      - \frac{\partial{\sigma}}{\partial {p}} 
                      (-1)^{N_D/2} K \nabla^{N_D}_{\eta} p
                      \cdot \frac{\partial{T}}{\partial {\sigma}}
$$
$$
                =      (-1)^{N_D/2} K \nabla^{N_D}_{\eta} T  
                    -  (-1)^{N_D/2} K \nabla^{N_D}_{\eta} \pi
                          \cdot \sigma \frac{\partial{T}}{\partial {\sigma}}
$$
$$
                =    {\mathcal D} (T) 
                    -  {\mathcal D} (\pi) 
                       \sigma \frac{\partial{T}}{\partial {\sigma}}
$$

So,

$$
  T_k \leftarrow  T_k 
       -  2 \Delta t
        \sigma_{k} \frac{T_{k+1}-T_{k-1}}{\sigma_{k+1} - \sigma_{k-1}}
        {\mathcal D}(\pi)
$$


and so on. In ${\mathcal D}(\pi)$, the spectral value of $\pi$ is converted to a grid by multiplying the spectral value of $\pi_n^m$ by the spectral representation of the diffusion coefficient.

### Frictional heat associated with diffusion. `[CORDIF (ddifc.F)]`

Frictional heat from diffusion is ,

$$
  Q_{DIF} = - \left( u_{ij} {\mathcal D}(u)_{ij}
                   + v_{ij} {\mathcal D}(v)_{ij} \right)
$$


It is estimated that Therefore,

$$
  T_k \leftarrow  T_k
       -  \frac{2 \Delta t}{C_p}
           \left( u_{ij} {\mathcal D}(u)_{ij}
                 + v_{ij} {\mathcal D}(v)_{ij} \right)
$$

### Horizontal Diffusion and Rayleigh Friction `[DSETDF (dsetd.F)]`

The coefficients of horizontal diffusion can be expressed spectrally,

$$
 {{\mathcal D}_M}_n^m = K_M
                      \left[ \left( \frac{n(n+1)}{a^2} \right)^{N_D/2}
                                - \left( \frac{2}{a^2} \right)^{N_D/2}
                      \right]
                  + K_R
$$


$$
  {{\mathcal D}_H}_n^m = K_M \left( \frac{n(n+1)}{a^2} \right)^{N_D/2}
$$


$$
  {{\mathcal D}_E}_n^m = K_E \left( \frac{n(n+1)}{a^2} \right)^{N_D/2}
$$


$K_R$ is the Rayleigh coefficient of friction. The Rayleigh coefficient of friction is

$$
  K_R = K_R^0 \left[ 1+\tanh \left( \frac{z-z_R}{H_R} \right) \right]
$$


However, the profile is given in the same way as However,

$$
  z = - H \ln \sigma
$$


The results are approximate to those of $K_R^0 = {(30day)}^{-1}$ and $z_R = -H \ln \sigma_{top}$. The standard values are $K_R^0 = {(30day)}^{-1}$, $z_R = -H \ln \sigma_{top}$ ($\sigma_{top}$: top level of the model), $H = 8000$ m, and $H_R = 7000$ m.

### Time Filter `[DADVNC (dadvn.F)]`

To reduce numerical mode associated with leap frog scheme, time filter is applied every time step. MIORC6 used modified Asselin time filter (Williams, 2009), which is updated version of Asselin(1972) used previous version of MIROC. Although Asselin time filter attenuate high frequency physical mode, bringing low accuracy of leap frog scheme, current time filter succeeded in suppressing it.

Modified Asselin filter is expressed as following equation

$$
 \bar{\bar{X}}^t = \bar{X}^t + \nu\alpha[\bar{\bar{X}}^{t-\Delta t} -2 \bar{X}^t + X^{t+\Delta t}]
$$

$$
 \bar{X}^{t+\Delta t} = X^{t+\Delta t} + \nu(1-\alpha)[\bar{\bar{X}}^{t-\Delta t} -2 \bar{X}^t + X^{t+\Delta t}]
$$

where bar indicates time filter. The parameters set to $\nu=0.05$, $\alpha=0.5$. Assuming $\alpha=1$, modified Asselin filter is same as Asselin filter.

In the model, 
$$
 \bar{\bar{X}}^{t*} = (1-\nu\alpha)^{-1}[(1-2\nu\alpha)\bar{X}^t +\nu\alpha \bar{\bar{X}}^{t-\Delta t} ]
$$
is firstly calculated at `MODULE: [DADVNC]` where transformation of prognostic variableto grid point values. And then, $X^{t-\Delta t}-2X^t$ is stored. When the $X^{t+\Delta t}$ is obtained later, time filter conduct at `MODULE [TFILT]`,

$$
 \bar{\bar{X}}^{t} = (1-\nu\alpha)\bar{\bar{X}}^{t*} +\nu\alpha X^{t+\Delta t} 
$$
$$
\bar{X}^{t+\Delta t} = X^{t+\Delta t} + \nu (1-\alpha)[ \bar{\bar{X}}^{t-\Delta t} - 2\bar{X}^{t} + X^{t+\Delta t}]
 $$

### Correction for conservation of mass `[FIXMAS, MASFIX (dmfix.F)]`

In the spectral method, the global integral of $\pi = \ln p_S$ is preserved with rounding errors removed, but the preservation of the mass, i.e. the global integral of $p_S$ is not guaranteed. Moreover, a wavenumber break in the spectra sometimes results in negative values of the water vapor grid points. For this reason, we perform a correction to preserve the masses of dry air, water vapor, and cloud water, and to remove the regions with negative water vapor content.

Before entering dynamical calculations, `[FIXMAS]`, the global integrals of water vapor and cloud water are calculated for $M_q, M_l$.

$$
  M_q^0  =  \sum_{ijk} q p_S  \Delta\lambda_i w_j \Delta\sigma_k  \\
  M_l^0  =  \sum_{ijk} l p_S  \Delta\lambda_i w_j \Delta\sigma_k
$$



In the first step of the calculation, the dry mass $M_d$ is calculated and stored.

$$
  M_d^0 = \sum_{ijk} (1-q-l) p_S \Delta\lambda_i w_j \Delta\sigma_k
$$


After exiting dynamical calculation, `[MASFIX]`, the following procedure is followed.

First, negative water vapor is removed by dividing the water vapor from the grid points immediately below the grid points. Suppose that $q_k < 0 $ is used,

$$
        q_k'      =  0          \\
        q_{k-1}'  =  q_{k-1} + \frac{\Delta p_k}{\Delta p_{k-1}} q_k
$$



 However, this should only be done if it is $q_{k-1}' \ge 0 $.

Next, set the value to zero for the grid points not removed by the above procedure.

3. calculate the global integral value of $M_q$ and multiply the global water vapor content by a fixed percentage so that it is the same as that of $M_q^0$.

$$
        q'' = \frac{M_q^0}{M_q} q'
$$


4. correct for dry air mass Likewise calculate $M_d$,

$$
        p_S'' = \frac{M_d^0}{M_d} p_S
$$


