## Summary of the mechanics part

Here, we duplicate the previous description,
Enumerate the calculations performed in the Mechanical Process Department.

### Summary of Calculations for the Mechanics Portion

The mechanical processes are calculated in the following order.

1. converting horizontal wind into vorticity and divergence `MODULE:[UV2VDG(dvect)]`

2. calculation of pseudotemperature `MODULE:[VIRTMD(dvtmp)]`

3. calculation of the barometric gradient term `MODULE:[HGRAD(dvect)]`

4. diagnostic calculation of vertical flow `MODULE:[GRDDYN/PSDOT(dgdyn)]`

5. time change term due to advection `MODULE:[GRDDYN(dgdyn)]`

6. convert the predictive variable to a spectrum `MODULE:[GD2WD(dg2wd)]`

7. convert the time-varying term into a spectrum `MODULE:[TENG2W(dg2wd)]`

8. time integration of spectral values `MODULE:[TINTGR(dintg)]`

9. convert the predictive variables to grid values `MODULE:[GENGD(dgeng)]`

10. pseudo etc. $p$ plane spreading correction `MODULE:[CORDIF(ddifc)]`

11. consideration of frictional heat by diffusion `MODULE:[CORFRC(ddifc)]`

12. correction for conservation of mass `MODULE:[MASFIX(dmfix)]`

13. (physical process) `MODULE:[PHYSCS(padmn)]`

14. (time filter) `MODULE:[TFILT(aadvn)]`

### Conversion of Horizontal Wind to Vorticity and Divergence

Grid point values for horizontal wind $u_{ij}, v_{ij}$
from the grid values of vorticity and divergence $\zeta_{ij}, D_{ij}$.
First, the spectra of vorticity and divergence
Ask for $\zeta_n^m, D_n^m$,

$$
\zeta_n^m  =  \frac{1}{I} \sum_{i=1}^{I} \sum_{j=1}^{J}  
                  im v_{ij} \cos\varphi_j {Y_n^{m*}}_{ij}
                \frac{w_j}{a(1-\mu_j^{2})} 
                 \\
           +    \frac{1}{I} \sum_{i=1}^{I} \sum_{j=1}^{J}  
                     u_{ij} \cos\varphi_j (1-\mu_j^2) 
                  \frac{\partial }{\partial \mu} {Y_n^{m*}}_{ij}
                 \frac{w_j}{a(1-\mu_j^{2})} \; ,
$$

    --- (1)

$$
    D_n^m  =  \frac{1}{I} \sum_{i=1}^{I} \sum_{j=1}^{J}  
                  im u_{ij} \cos\varphi_j {Y_n^{m*}}_{ij}
                \frac{w_j}{a(1-\mu_j^{2})} 
                 \\
           -    \frac{1}{I} \sum_{i=1}^{I} \sum_{j=1}^{J}  
                  v_{ij} \cos\varphi_j  (1-\mu_j^2) 
                  \frac{\partial }{\partial \mu} {Y_n^{m*}}_{ij}
                 \frac{w_j}{a(1-\mu_j^{2})} ; .
$$

    --- (2)

I'll take that further,

$$
  \zeta_{ij} 
   =  {\mathcal R}{TERM00004} \sum_{m=-N}^{N} \sum_{n=|m|}^{N} 
      \zeta_n^m  {Y_n^m}_{ij} \; ,
$$
     --- (3)

and so on.

### Calculating a Provisional Temperature

Provisional Temperature $T_v$ is ,

$$
  T_v = T ( 1 + \epsilon_v q - l ) \; ,
$$
     --- (4)

However, it is $\epsilon_v = R_v/R - 1$,
$R_v$ is a gas constant for water vapor
(461 Jkg$^{-1}$K$^{-1}$)
$R$ is a gas constant of air
(287.04 Jkg$^{-1}$K$^{-1}$)
It is.

### Calculating the Barometric gradient term

The barometric gradient term $\nabla \pi = \frac{1}{p_S} \nabla p_S$ is ,
First, we need to get the $\pi_n^m$

$$
  \pi_n^m  =  \frac{1}{I} \sum_{i=1}^{I} \sum_{j=1}^{J}  
               (\ln {p_S})_{ij} {Y_n^{m *}}_{ij}  w_j \; ,
$$
    --- (5)

to a spectral representation and then ,

$$
   \frac{1}{a \cos \varphi} 
   \left( \frac{\partial \pi}{\partial \lambda} \right)_{ij}
     = 
   \frac{1}{a \cos \varphi} 
        {\mathcal R}{TERM00015} \sum_{m=-N}^{N} \sum_{n=|m|}^{N} 
       im \tilde{X}_n^m {Y_n^m}_{ij}  \; ,
$$
     --- (6)

$$
   \frac{1}{a}
   \left( \frac{\partial \pi}{\partial \varphi} \right)_{ij}
     =  
   \frac{1}{a \cos \varphi} 
       {\mathcal R}{TERM00016} \sum_{m=-N}^{N} \sum_{n=|m|}^{N} 
       \pi_n^m 
       ( 1-\mu^{2} ) \frac{\partial }{\partial \mu} {Y_n^m}_{ij}  \; .
$$
     --- (7)

### Diagnostic calculations of vertical flow.

Barometric pressure change term, and lead DC,

$$
  \frac{\partial \pi}{\partial t}
 = - \sum_{k=1}^{K} ( D_k + {TERM00017}_k \cdot \nabla \pi ) 
       \Delta  \sigma_k
$$
     --- (8)

$$
  \dot{\sigma}_{k-1/2}
 = - \sigma_{k-1/2} \frac{\partial \pi}{\partial t}
   - \sum_{l=k}^{K} ( D_l + {TERM00018}_l \cdot \nabla \pi )          
       \Delta  \sigma_l
$$
     --- (9)

and its non-gravity components.

$$
  \left( \frac{\partial \pi}{\partial t} \right)^{NG}
   =   - \sum_{k=1}^{K} {TERM00019}_{k} \cdot \nabla \pi  
       \Delta  \sigma_{k}  \\
$$
     --- (10)

$$
  \dot{\sigma}^{NG}_{k-1/2}
 = - \sigma_{k-1/2} \left( \frac{\partial \pi}{\partial t} \right)^{NG}
   - \sum_{l=k}^{K} {TERM00020}_{l} \cdot \nabla \pi
       \Delta  \sigma_{l}
$$
     --- (11)

### Time change term due to advection.

Momentum advection term:

$$
  (A_u)_k 
    =  ( \zeta_k + f ) v_k 
             - \frac{1}{2 \Delta \sigma_k} 
             [   \dot{\sigma}_{k-1/2} ( u_{k-1} - u_k   )
               + \dot{\sigma}_{k+1/2} ( u_k   - u_{k+1} ) ]
            \\
           - \frac{C_{p} \hat{\kappa}_k T_{v,k}'}{ a \cos \varphi} 
                  \frac{\partial \pi}{\partial \lambda} 
$$

     --- (12)

$$
  (A_v)_k 
    =  - ( \zeta_k + f ) u_k 
             - \frac{1}{2 \Delta \sigma_k} 
             [   \dot{\sigma}_{k-1/2} ( v_{k-1} - v_k   )
               + \dot{\sigma}_{k+1/2} ( v_k   - v_{k+1} ) ]
            \\
           - \frac{C_{p} \hat{\kappa}_k T_{v,k}'}{a} 
             \frac{\partial \pi}{\partial \varphi} 
$$

     --- (13)

$$
 \hat{E}_k    
  = \frac{1}{2} ( u^2 + v^2 ) 
    +  \sum_{k'=1}^{k} \left[  C_p \alpha_k ( T_v - T )_{k'}
                              + C_p \beta_k ( T_v - T )_{k'-1} \right]
$$
     --- (14)

Temperature advection term:

$$
 (u T')_k  = u_k (T_k - \bar{T} )
$$
     --- (15)

$$
 (v T')_k  = v_k (T_k - \bar{T} )
$$
     --- (16)

$$
 \hat{H}_k  =  T_{k}^{\prime} D_{k}  \\
         - \frac{1}{\Delta \sigma_{k}} 
             [   \dot{\sigma}_{k-1/2} ( \hat{T^{\prime}}_{k-1/2} 
                                         - T^{\prime}_{k}   )
               + \dot{\sigma}_{k+1/2} ( T^{\prime}_{k}  
                                         - \hat{T^{\prime}}_{k+1/2} ) ]
                \\
         - \frac{1}{\Delta \sigma_{k}} 
             [   \dot{\sigma}^{NG}_{k-1/2} ( \hat{\bar{T}}_{k-1/2} 
                                         - \bar{T}_{k}   )
               + \dot{\sigma}^{NG}_{k+1/2} ( \bar{T}_{k}  
                                         - \hat{\bar{T}}_{k+1/2} ) ]
                \\
         + \hat{\kappa}_{k} T_{v,k} {TERM00021}_{k} \cdot \nabla \pi
                \\
         - \frac{\alpha_{k}}{\Delta \sigma_{k} } T_{v,k}
             \sum_{l=k}^{K} {TERM00022}_{l} \cdot \nabla \pi 
               \Delta \sigma_{l}
           - \frac{\beta_{k}}{\Delta \sigma_{k} } T_{v,k}
             \sum_{l=k+1}^{K} {TERM00023}_{l} \cdot \nabla \pi 
               \Delta \sigma_{l}
                \\
         - \frac{\alpha_{k}}{\Delta \sigma_{k} } T'_{v,k}
             \sum_{l=k}^{K} D_l  \Delta \sigma_{l}
           - \frac{\beta_{k}}{\Delta \sigma_{k} } T'_{v,k}
             \sum_{l=k+1}^{K} D_l  \Delta \sigma_{l}
$$





     --- (17)

Water vapor advection term:

$$
 (u q)_k  = u_k q_k
$$
    --- (18)

$$
 (v q)_k  = v_k q_k
$$
    --- (19)

$$
R_k  =  q_k D_k 
       - \frac{1}{2 \Delta \sigma_k} 
             [   \dot{\sigma}_{k-1/2} ( q_{k-1} - q_k   )
               + \dot{\sigma}_{k+1/2} ( q_k   - q_{k+1} ) ]
$$
    --- (20)

### Conversion of Predictive Variables into Spectra

(1) and
(2).

$u_{ij}^{t-\Delta t}, v_{ij}^{t-\Delta t}$
Spectral representation of vorticity and divergence
Convert to $\zeta_n^m, D_n^m$.
Furthermore,
Temperature $T^{t-\Delta t}$, Specific Humidity $q^{t-\Delta t}$,
$\pi = \ln p_S^{t-\Delta t}$.

$$
  X_n^m  =  \frac{1}{I} \sum_{i=1}^{I} \sum_{j=1}^{J}  
               X_{ij} {Y_n^{m *}}_{ij}  w_j \; ,
$$
    --- (21)

to a spectral representation.

### Conversion of time-varying terms to spectra

Time Variation Term of Vorticity

$$
  \frac{\partial{\zeta_n^m}}{\partial {t}} 
   =  \frac{1}{I} \sum_{i=1}^{I} \sum_{j=1}^{J}  
          im (A_v)_{ij} \cos \varphi_j
          {Y_n^{m *}}_{ij}
         \frac{w_j}{a(1-\mu_j^{2})} 
          \\
   +    \frac{1}{I} \sum_{i=1}^{I} \sum_{j=1}^{J}  
          (A_u)_{ij} \cos \varphi_j
          (1-\mu_j^2) 
          \frac{\partial }{\partial \mu} {Y_n^{m *}}_{ij}
          \frac{w_j}{a(1-\mu_j^{2})} 
          \\ 
$$


     --- (22)

The non-gravity wave component of the time-varying term of the divergence

$$
  \left( \frac{\partial{D_n^m}}{\partial {t}} \right)^{NG}
   =  \frac{1}{I} \sum_{i=1}^{I} \sum_{j=1}^{J}  
          im (A_u)_{ij} \cos \varphi_j
          {Y_n^{m *}}_{ij}
         \frac{w_j}{a(1-\mu_j^{2})} 
          \\
   -    \frac{1}{I} \sum_{i=1}^{I} \sum_{j=1}^{J}  
          (A_v)_{ij} \cos \varphi_j
          (1-\mu_j^2) 
          \frac{\partial }{\partial \mu} {Y_n^{m *}}_{ij}
          \frac{w_j}{a(1-\mu_j^{2})} 
          \\
   -   \frac{n(n+1)}{a^{2}} 
         \frac{1}{I} \sum_{i=1}^{I} \sum_{j=1}^{J}  
          \hat{E}_{ij}  {Y_n^{m *}}_{ij} w_j
          \\ 
$$



    --- (23)

The non-gravity wave component of the time-varying term of temperature

$$
  \left( \frac{\partial{T_n^m}}{\partial {t}} \right)^{NG}
   =  - \frac{1}{I} \sum_{i=1}^{I} \sum_{j=1}^{J}  
          im (u T')_{ij} \cos \varphi_j
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


    --- (24)

Time-varying term of water vapor

$$
  \frac{\partial{q_n^m}}{\partial {t}}
   =  - \frac{1}{I} \sum_{i=1}^{I} \sum_{j=1}^{J}  
          im (uq)_{ij} \cos \varphi_j
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


    --- (25)

### Spectral value time integration

Equations in matrix form

$$
      \left\{ ( 1+2\Delta t {\mathcal D}_H )( 1+2\Delta t {\mathcal D}_M )
           \underline{I}  
      - ( \Delta t )^{2}  ( \underline{W} \ \underline{h} 
           + (1+2\Delta t {\mathcal D}_M)
             {TERM00029} {TERM00030}^{T} ) \nabla^{2}_{\sigma}
  \right\}
      \overline{ {TERM00031} }^{t} 
       \\
  = ( 1+2\Delta t {\mathcal D}_H )( 1-\Delta t {\mathcal D}_M ) 
       {TERM00032}^{t-\Delta t}
  + \Delta t 
         \left( \frac{\partial {TERM00033}}{\partial t} \right)_{NG}  
  \\
  -  \Delta t \nabla^{2}_{\sigma}     
                   \left\{  ( 1+2\Delta t {\mathcal D}_H ) {TERM00034}_{S} 
                          + \underline{W} 
                            \left[ ( 1-2\Delta t {\mathcal D}_H ) 
                                    {TERM00035}^{t-\Delta t}
                                  + \Delta t 
                                      \left( \frac{\partial {TERM00036}}
                                                  {\partial t}     
                                      \right)_{NG} \right]
                   \right.
  \\
                 \left.  \hspace*{20mm} 
                          + ( 1+2\Delta t {\mathcal D}_H ) {TERM00037} 
                            \left[ \pi^{t-\Delta t} 
                                  + \Delta t
                                     \left( \frac{\partial \pi}
                                                 {\partial t} 
                                     \right)_{NG}  \right]
                   \right\} . 
$$



    --- (26)

by using LU decomposition to solve for
Ask for $\bar{D}$,

$$
  \frac{\partial {TERM00039}}{\partial t} 
      =   \left( \frac{\partial {TERM00040}}
                        {\partial t}       \right)_{NG}  
         - \underline{h} {TERM00041}
$$
    --- (27)

$$
  \frac{\partial \pi}{\partial t} 
      =   \left( \frac{\partial \pi}
                        {\partial t}       \right)_{NG}  
         - {TERM00042} \cdot {TERM00043}
$$
    --- (28)

due to
$\partial {$\mathbf{T}$}/\partial t$,
$\partial \pi/\partial t$
and calculate the value of the spectrum in $t+\Delta t$.

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
    --- (29)
    --- (30)
    --- (31)
    --- (32)
    --- (33)

### Conversion of Predictive Variables to Grid Values

Spectral values of vorticity and divergence from $\zeta_n^m, D_n^m$
Find the horizontal wind speed grid values $u_{ij}, v_{ij}$.

$$
  u_{ij}
  =  \frac{1}{\cos \varphi_j}
     {\mathcal R}{TERM00049} \sum_{m=-N}^{N} 
                       \sum_{\stackrel{n=|m|}{n \neq 0}}^{N} 
    \left\{
             \frac{a}{n(n+1)} \zeta_n^m 
            (1-\mu^{2}) \frac{\partial{}}{\partial {\mu}} {Y_n^m}_{ij}
          -  \frac{im a}{n(n+1)} D_n^m {Y_n^m}_{ij}
    \right\}
$$
    --- (34)

$$
  v_{ij}
  =  \frac{1}{\cos \varphi_j}
     {\mathcal R}{TERM00050} \sum_{m=-N}^{N}
                       \sum_{\stackrel{n=|m|}{n \neq 0}}^{N}
    \left\{
          -  \frac{im a}{n(n+1)} \zeta_n^m  {Y_n^m}_{ij}
          -  \frac{a}{n(n+1)} \tilde{D}_n^m 
            (1-\mu^{2}) \frac{\partial{}}{\partial {\mu}} {Y_n^m}_{ij}
    \right\}
$$
     --- (35)

Furthermore,

$$
  T_{ij} 
   =  {\mathcal R}{TERM00051} \sum_{m=-N}^{N} \sum_{n=|m|}^{N} 
      T_n^m  {Y_n^m}_{ij} \; ,
$$
    --- (36)

$T_{ij}, \pi_{ij}, q_{ij}$ are obtained by such methods as

$$
  {p_S}_{ij} = \exp \pi_{ij} 
$$
    --- (37)

to calculate.

### Pseudo etc. $p$ Surface Diffusion Correction

Horizontal diffusion is applied on the $\sigma$ surface and so on,
In large areas of mountain slopes, water vapor is transported uphill,
Causing problems such as bringing false precipitation at the top of the mountain.
To mitigate that, etc. $p$ close to the diffusion of the surface
Insert corrections for $T,q,l$.

$$
  {\mathcal D}_p (T) = (-1)^{N_D/2} K \nabla^{N_D}_p T  
                \simeq  (-1)^{N_D/2} K \nabla^{N_D}_{\sigma} T  
                      - \frac{\partial{\sigma}}{\partial {p}} 
                      (-1)^{N_D/2} K \nabla^{N_D}_{\sigma} p
                      \cdot \frac{\partial{T}}{\partial {\sigma}}                   \\
                =      (-1)^{N_D/2} K \nabla^{N_D}_{\sigma} T  
                    -  (-1)^{N_D/2} K \nabla^{N_D}_{\sigma} \pi
                          \cdot \sigma \frac{\partial{T}}{\partial {\sigma}}  \\
                =    {\mathcal D} (T) 
                    -  {\mathcal D} (\pi) 
                       \sigma \frac{\partial{T}}{\partial {\sigma}}
$$


    --- (38)

So,

$$
  T_k \leftarrow  T_k 
       -  2 \Delta t
        \sigma_{k} \frac{T_{k+1}-T_{k-1}}{\sigma_{k+1} - \sigma_{k-1}}
        {\mathcal D}(\pi)
$$
    --- (39)

And so on.
${\mathcal D}(\pi)$ has been replaced by the spectral value of $pi$, $\pi_n^m$
The spectral representation of the diffusion coefficient multiplied by
It is used to convert to a grid value.

### Consideration of frictional heat from diffusion

Frictional heat from diffusion is ,

$$
  Q_{DIF} = - \left( u_{ij} {\mathcal D}(u)_{ij} 
                   + v_{ij} {\mathcal D}(v)_{ij} \right)
$$
    --- (40)

It is estimated that .
Therefore,

$$
  T_k \leftarrow  T_k 
       -  \frac{2 \Delta t}{C_p}
           \left( u_{ij} {\mathcal D}(u)_{ij} 
                 + v_{ij} {\mathcal D}(v)_{ij} \right)
$$
    --- (41)

### Correction for conservation of mass

The spectral method is not used,
The global integration of the $\pi = \ln p_S$ is preserved except for rounding errors,
The conservation of the mass, i.e. the global integration of $p_S$, is not guaranteed.
Also, with the expiration of the spectral wavenumber, the
Negative values of the grid points of water vapor are sometimes observed.
For these reasons ,
Let the mass of dry air and water vapor, the mass of cloud water be preserved,
In addition, corrections are made to remove areas with negative water vapor content.

First, at the beginning of the mechanics calculation, `MODULE:[FIXMAS]`,
Calculate the global integral of each component of water vapor and cloud water, $M_q, M_l$.

$$
  M_q^0  =  \sum_{ijk} q p_S  \Delta\lambda_i w_j \Delta\sigma_k  \\
  M_l^0  =  \sum_{ijk} l p_S  \Delta\lambda_i w_j \Delta\sigma_k 
$$
    --- (42)
    --- (43)

Also, in the first step of the calculation
Calculate and memorize the dry mass $M_d$.

$$
  M_d^0 = \sum_{ijk} (1-q-l) p_S \Delta\lambda_i w_j \Delta\sigma_k 
$$
    --- (44)

At the end of the dynamics calculation, `MODULE:[MASFIX]`,
The following procedure is used to make the correction.

First, we discuss the grid points with negative water vapor content,
 The water vapor is distributed from the grid points directly below,
 Remove the negative water vapor.
 If this is     $q_k < 0 $,

$$
        q_k'      =  0          \\
        q_{k-1}'  =  q_{k-1} + \frac{\Delta p_k}{\Delta p_{k-1}} q_k
$$
    --- (45)
    --- (46)

 However, this should only be done if it is $q_{k-1}' \ge 0 $.

Next, set the value to zero for the grid points not removed by the above procedure.

3. calculate the global integration value $M_q$,
 Make sure this is consistent with $M_q^0$,
 Multiply the global water vapor content by a certain percentage.

$$
        q'' = \frac{M_q^0}{M_q} q' 
$$
    --- (47)

4. perform dry air mass correction.
 Similarly, calculate the $M_d$,

$$
        p_S'' = \frac{M_d^0}{M_d} p_S
$$
    --- (48)

### Horizontal Diffusion and Rayleigh Friction

The coefficients of horizontal diffusion can be expressed spectrally,

$$
 {{\mathcal D}_M}_n^m = K_M 
                      \left[ \left( \frac{n(n+1)}{a^2} \right)^{N_D/2} 
                                - \left( \frac{2}{a^2} \right)^{N_D/2} 
                      \right]
                  + K_R
$$
    --- (49)

$$
  {{\mathcal D}_H}_n^m = K_M \left( \frac{n(n+1)}{a^2} \right)^{N_D/2} 
$$
    --- (50)

$$
  {{\mathcal D}_E}_n^m = K_E \left( \frac{n(n+1)}{a^2} \right)^{N_D/2} 
$$
    --- (51)

The $K_R$ is the Rayleigh coefficient of friction.
The Rayleigh coefficient of friction is

$$
  K_R = K_R^0 \left[ 1+\tanh \left( \frac{z-z_R}{H_R} \right) \right]
$$
     --- (52)

given in profiles like
However,

$$
  z = - H \ln \sigma 
$$
    --- (53)

Approximate to .
Standard value is, $K_R^0 = {(30day)}^{-1}$,
$z_R = -H \ln \sigma_{top}$ ($\sigma_{top}$ : top level of the model),
$H = 8000$ m,
$H_R = 7000$ m.

### Time Filter.

To remove the computation mode in leap frog
Apply the time filter of Asselin (1972) at every step.

$$
  \bar{T}^{t}
    = ( 1-2 \epsilon_f ) T^{t}
    +  \epsilon_f 
        \left( \bar{T}^{t-\Delta t} + T^{t+\Delta t} \right)
$$
     --- (54)

and $\bar{T}$.
The $T^{t-\Delta t}$ used in the next step of the mechanical process is
Using this $\bar{T}^t$.
For a $\epsilon_f$, the standard value of 0.05 should be used.

In fact.
First, in the `MODULE:[GENGD]` conversion of the predictor to a grid of values, the following variables are used,

$$
  \bar{T}^{t*}
    = ( 1 -\epsilon_f )^{-1} 
     \left[ ( 1-2 \epsilon_f ) T^{t} + \epsilon_f \bar{T}^{t-\Delta t}
     \right]
$$
    --- (55)

and when the physical process is done
After fixing the value of $T^{t+\Delta t}$, you can use `MODULE:[TFILT]` to determine the value of $T^{t+\Delta t}$,

$$
 \bar{T}^{t}
    = ( 1 -\epsilon_f ) \bar{T}^{t*}  
       +  \epsilon_f \bar{T}^{t+\Delta t}
$$
     --- (56)

.
