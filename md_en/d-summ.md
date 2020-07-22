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

10. pseudo, etc. $p$ plane spreading correction `MODULE:[CORDIF(ddifc )]`

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
 
> <span id="d-summ:uv-zeta" label="d- summ:uv-zeta">[d-summ:uv-zeta]</ span>


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
 
> <span id="d-summ:uv-D" label="d-summ: uv-D">\\[d-summ:uv-D\]</span>


I'll take that further,

$$
  \zeta_{ij} 
   =  {\mathcal R}\mathbf{e} \sum_{m=-N}^{N} \sum_{n=|m|}^{N} 
      \zeta_n^m  {Y_n^m}_{ij} \; ,
$$


and so on.

### Calculating a Provisional Temperature

Provisional Temperature $T_v$ is ,

$$
  T_v = T ( 1 + \epsilon_v q - l ) \; ,
$$


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


to a spectral representation and then ,

$$
   \frac{1}{a \cos \varphi} 
   \left( \frac{\partial \pi}{\partial \lambda} \right)_{ij}
     = 
   \frac{1}{a \cos \varphi} 
        {\mathcal R}\mathbf{e} \sum_{m=-N}^{N} \sum_{n=|m|}^{N} 
       im \tilde{X}_n^m {Y_n^m}_{ij}  \; ,
$$


$$
   \frac{1}{a}
   \left( \frac{\partial \pi}{\partial \varphi} \right)_{ij}
     =  
   \frac{1}{a \cos \varphi} 
       {\mathcal R}\mathbf{e} \sum_{m=-N}^{N} \sum_{n=|m|}^{N} 
       \pi_n^m 
       ( 1-\mu^{2} ) \frac{\partial }{\partial \mu} {Y_n^m}_{ij}  \; .
$$


### Diagnostic calculations of vertical flow.

Barometric pressure change term, and lead DC,

$$
  \frac{\partial \pi}{\partial t}
 = - \sum_{k=1}^{K} ( D_k + \mathbf{v}_k \cdot \nabla \pi ) 
       \Delta  \sigma_k
$$


$$
  \dot{\sigma}_{k-1/2}
 = - \sigma_{k-1/2} \frac{\partial \pi}{\partial t}
   - \sum_{l=k}^{K} ( D_l + \mathbf{v}_l \cdot \nabla \pi )          
       \Delta  \sigma_l
$$


and its non-gravity components.

$$
  \left( \frac{\partial \pi}{\partial t} \right)^{NG}
   =   - \sum_{k=1}^{K} \mathbf{v}_{k} \cdot \nabla \pi  
       \Delta  \sigma_{k}  \\
$$


$$
  \dot{\sigma}^{NG}_{k-1/2}
 = - \sigma_{k-1/2} \left( \frac{\partial \pi}{\partial t} \right)^{NG}
   - \sum_{l=k}^{K} \mathbf{v}_{l} \cdot \nabla \pi
       \Delta  \sigma_{l}
$$


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
 


$$
 \hat{E}_k    
  = \frac{1}{2} ( u^2 + v^2 ) 
    +  \sum_{k'=1}^{k} \left[  C_p \alpha_k ( T_v - T )_{k'}
                              + C_p \beta_k ( T_v - T )_{k'-1} \right]
$$


Temperature advection term:

$$
 (u T')_k  = u_k (T_k - \bar{T} )
$$


$$
 (v T')_k  = v_k (T_k - \bar{T} )
$$


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
         + \hat{\kappa}_{k} T_{v,k} \mathbf{v}_{k} \cdot \nabla \pi
                \\
         - \frac{\alpha_{k}}{\Delta \sigma_{k} } T_{v,k}
             \sum_{l=k}^{K} \mathbf{v}_{l} \cdot \nabla \pi 
               \Delta \sigma_{l}
           - \frac{\beta_{k}}{\Delta \sigma_{k} } T_{v,k}
             \sum_{l=k+1}^{K} \mathbf{v}_{l} \cdot \nabla \pi 
               \Delta \sigma_{l}
                \\
         - \frac{\alpha_{k}}{\Delta \sigma_{k} } T'_{v,k}
             \sum_{l=k}^{K} D_l  \Delta \sigma_{l}
           - \frac{\beta_{k}}{\Delta \sigma_{k} } T'_{v,k}
             \sum_{l=k+1}^{K} D_l  \Delta \sigma_{l}
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
       - \frac{1}{2 \Delta \sigma_k} 
             [   \dot{\sigma}_{k-1/2} ( q_{k-1} - q_k   )
               + \dot{\sigma}_{k+1/2} ( q_k   - q_{k+1} ) ]
$$


### Conversion of Predictive Variables into Spectra


([\\\d\[d-summ:uv-D\]](#d-summ:uv-D)) to

$u_{ij}^{t-\Delta t}, v_{ij}^{t-\Delta t}$.
Spectral representation of vorticity and divergence
Convert to $\zeta_n^m, D_n^m$.
Furthermore,
Temperature $T^{t-\Delta t}$, Specific Humidity $q^{t-\Delta t}$,
$\pi = \ln p_S^{t-\Delta t}$.

$$
  X_n^m  =  \frac{1}{I} \sum_{i=1}^{I} \sum_{j=1}^{J}  
               X_{ij} {Y_n^{m *}}_{ij}  w_j \; ,
$$


to a spectral representation.

### Conversion of time-varying terms to spectra

Time Variation Term of Vorticity

$$
  \frac{\partial \zeta_n^m}{\partial t} 
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
 
 


The non-gravity wave component of the time-varying term of the divergence

$$
  \left( \frac{\partial D_n^m}{\partial t} \right)^{NG}
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
 
 
 


The non-gravity wave component of the time-varying term of temperature

$$
  \left( \frac{\partial T_n^m}{\partial t} \right)^{NG}
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
 
 


Time-varying term of water vapor

$$
  \frac{\partial q_n^m}{\partial t}
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
 
 


### Spectral value time integration

Equations in matrix form

$$
      \left\{ ( 1+2\Delta t {\mathcal D}_H )( 1+2\Delta t {\mathcal D}_M )
           \underline{I}  
      - ( \Delta t )^{2}  ( \underline{W} \ \underline{h} 
           + (1+2\Delta t {\mathcal D}_M)
             \mathbf{G} \mathbf{C}^{T} ) \nabla^{2}_{\sigma}
  \right\}
      \overline{ \mathbf{D} }^{t} 
       \\
  = ( 1+2\Delta t {\mathcal D}_H )( 1-\Delta t {\mathcal D}_M ) 
       \mathbf{D}^{t-\Delta t}
  + \Delta t 
         \left( \frac{\partial \mathbf{D}}{\partial t} \right)_{NG}  
  \\
  -  \Delta t \nabla^{2}_{\sigma}     
                   \left\{  ( 1+2\Delta t {\mathcal D}_H ) \mathbf{\Phi}_{S} 
                          + \underline{W} 
                            \left[ ( 1-2\Delta t {\mathcal D}_H ) 
                                    \mathbf{T}^{t-\Delta t}
                                  + \Delta t 
                                      \left( \frac{\partial \mathbf{T}}
                                                  {\partial t}     
                                      \right)_{NG} \right]
                   \right.
  \\
                 \left.  \hspace*{20mm} 
                          + ( 1+2\Delta t {\mathcal D}_H ) \mathbf{G} 
                            \left[ \pi^{t-\Delta t} 
                                  + \Delta t
                                     \left( \frac{\partial \pi}
                                                 {\partial t} 
                                     \right)_{NG}  \right]
                   \right\} . 
$$
 
 
 


by using LU decomposition to solve for
Ask for $\bar{D}$,

$$
  \frac{\partial \mathbf{T}}{\partial t} 
      =   \left( \frac{\partial \mathbf{T}}
                        {\partial t}       \right)_{NG}  
         - \underline{h} \mathbf{D}
$$


$$
  \frac{\partial \pi}{\partial t} 
      =   \left( \frac{\partial \pi}
                        {\partial t}       \right)_{NG}  
         - \mathbf{C} \cdot \mathbf{D}
$$


due to
$\partial \mathbf{T}/\partial t$,
$\partial \pi/\partial t$
and calculate the value of the spectrum in $t+\Delta t$.

$$
  \zeta^{t+\Delta t}  =  \left( \zeta^{t-\Delta t}
                                +   2 \Delta t \frac{\partial \zeta}{\partial t} \right)
                          ( 1 + 2 \Delta t {\mathcal D}_M )^{-1} \\
  D^{t+\Delta t}  =  2 \bar{D} - D^{t-\Delta t}\\
  T^{t+\Delta t}  =  \left( T^{t-\Delta t}
                                +  2 \Delta t  \frac{\partial T}{\partial t} \right)
                          ( 1 + 2 \Delta t {\mathcal D}_H )^{-1} \\
  q^{t+\Delta t}  =  \left( q^{t-\Delta t}
                                +  2 \Delta t \frac{\partial q}{\partial t} \right)
                          ( 1 + 2 \Delta t {\mathcal D}_E )^{-1} \\
\pi^{t+\Delta t}  =  \pi^{t-\Delta t}
                                +  2 \Delta t \frac{\partial \pi}{\partial t}
$$
 
 
 
 


### Conversion of Predictive Variables to Grid Values

Spectral values of vorticity and divergence from $\zeta_n^m, D_n^m$
Find the grid values of the horizontal wind speed $u_{ij}, v_{ij}$.

$$
  u_{ij}
  =  \frac{1}{\cos \varphi_j}
     {\mathcal R}\mathbf{e} \sum_{m=-N}^{N} 
                       \sum_{\stackrel{n=|m|}{n \neq 0}}^{N} 
    \left\{
             \frac{a}{n(n+1)} \zeta_n^m 
            (1-\mu^{2}) \frac{\partial }{\partial \mu} {Y_n^m}_{ij}
          -  \frac{im a}{n(n+1)} D_n^m {Y_n^m}_{ij}
    \right\}
$$


$$
  v_{ij}
  =  \frac{1}{\cos \varphi_j}
     {\mathcal R}\mathbf{e} \sum_{m=-N}^{N}
                       \sum_{\stackrel{n=|m|}{n \neq 0}}^{N}
    \left\{
          -  \frac{im a}{n(n+1)} \zeta_n^m  {Y_n^m}_{ij}
          -  \frac{a}{n(n+1)} \tilde{D}_n^m 
            (1-\mu^{2}) \frac{\partial }{\partial \mu} {Y_n^m}_{ij}
    \right\}
$$


Furthermore,

$$
  T_{ij} 
   =  {\mathcal R}\mathbf{e} \sum_{m=-N}^{N} \sum_{n=|m|}^{N} 
      T_n^m  {Y_n^m}_{ij} \; ,
$$


$T_{ij}, \pi_{ij}, q_{ij}$ is obtained by such methods as

$$
  {p_S}_{ij} = \exp \pi_{ij} 
$$


to calculate.

### Pseudo etc. $p$ Surface Diffusion Correction

Horizontal diffusion is applied on the surface of $\sigma$ and so on,
In large areas of mountain slopes, water vapor is transported uphill,
Causing problems such as bringing false precipitation at the top of the mountain.
To mitigate that, etc. close to the diffusion of the $p$ surface
Insert corrections for $T,q,l$.

$$
  {\mathcal D}_p (T) = (-1)^{N_D/2} K \nabla^{N_D}_p T  
                \simeq  (-1)^{N_D/2} K \nabla^{N_D}_{\sigma} T  
                      - \frac{\partial \sigma}{\partial p} 
                      (-1)^{N_D/2} K \nabla^{N_D}_{\sigma} p
                      \cdot \frac{\partial T}{\partial \sigma}                   \\
                =      (-1)^{N_D/2} K \nabla^{N_D}_{\sigma} T  
                    -  (-1)^{N_D/2} K \nabla^{N_D}_{\sigma} \pi
                          \cdot \sigma \frac{\partial T}{\partial \sigma}  \\
                =    {\mathcal D} (T) 
                    -  {\mathcal D} (\pi) 
                       \sigma \frac{\partial T}{\partial \sigma}
$$
 
 


So,

$$
  T_k \leftarrow  T_k 
       -  2 \Delta t
        \sigma_{k} \frac{T_{k+1}-T_{k-1}}{\sigma_{k+1} - \sigma_{k-1}}
        {\mathcal D}(\pi)
$$


And so on.
${\mathcal D}(\pi)$ has been replaced by the spectral value of $pi$ in the $\pi_n^m$
The spectral representation of the diffusion coefficient multiplied by
It is used to convert to a grid value.

### Consideration of frictional heat from diffusion.

Frictional heat from diffusion is ,

$$
  Q_{DIF} = - \left( u_{ij} {\mathcal D}(u)_{ij} 
                   + v_{ij} {\mathcal D}(v)_{ij} \right)
$$


It is estimated that .
Therefore,

$$
  T_k \leftarrow  T_k 
       -  \frac{2 \Delta t}{C_p}
           \left( u_{ij} {\mathcal D}(u)_{ij} 
                 + v_{ij} {\mathcal D}(v)_{ij} \right)
$$


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
Calculate global integrals $M_q, M_l$ for each component of water vapor and cloud water.

$$
  M_q^0  =  \sum_{ijk} q p_S  \Delta\lambda_i w_j \Delta\sigma_k  \\
  M_l^0  =  \sum_{ijk} l p_S  \Delta\lambda_i w_j \Delta\sigma_k 
$$
 


Also, in the first step of the calculation
Calculate and memorize dry mass $M_d$.

$$
  M_d^0 = \sum_{ijk} (1-q-l) p_S \Delta\lambda_i w_j \Delta\sigma_k 
$$


At the end of the dynamics calculation, `MODULE:[MASFIX]`,
The following procedure is used to make the correction.

First, we discuss the grid points with negative water vapor content,
 The water vapor is distributed from the grid points directly below,
 Remove the negative water vapor.
 If it is     $q_k < 0 $,
     
$$
        q_k'      =  0          \\
        q_{k-1}'  =  q_{k-1} + \frac{\Delta p_k}{\Delta p_{k-1}} q_k
$$
 

     
 However, this should only be done if this is $q_{k-1}' \ge 0 $.

Next, set the value to zero for the grid points not removed by the above procedure.

3. calculate the global integration value $M_q$
 Make sure this matches the $M_q^0$,
 Multiply the global water vapor content by a certain percentage.
     
$$
        q'' = \frac{M_q^0}{M_q} q' 
$$


4. perform dry air mass correction.
 Similarly, calculate $M_d$,
     
$$
        p_S'' = \frac{M_d^0}{M_d} p_S
$$


### Horizontal Diffusion and Rayleigh Friction

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


The $K_R$ is the Rayleigh coefficient of friction.
The Rayleigh coefficient of friction is

$$
  K_R = K_R^0 \left[ 1+\tanh \left( \frac{z-z_R}{H_R} \right) \right]
$$


given in profiles like
However,

$$
  z = - H \ln \sigma 
$$


Approximate to .
The standard value is, $K_R^0 = {(30day)}^{-1}$,
$z_R = -H \ln \sigma_{top}$ ($\sigma_{top}$ : the top level of the model),
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


and $\bar{T}$.
The $T^{t-\Delta t}$ for the next step of the mechanical process is
Using this $\bar{T}^t$.
The standard value for $\epsilon_f$ is 0.05.

In fact.
First, in the `MODULE:[GENGD]` conversion of the predictor to a grid of values, the following variables are used,

$$
  \bar{T}^{t*}
    = ( 1 -\epsilon_f )^{-1} 
     \left[ ( 1-2 \epsilon_f ) T^{t} + \epsilon_f \bar{T}^{t-\Delta t}
     \right]
$$


and when the physical process is done
After determining the value of $T^{t+\Delta t}$, you can use `MODULE:[TFILT]` to determine the value of the $T^{t+\Delta t}$,

$$
 \bar{T}^{t}
    = ( 1 -\epsilon_f ) \bar{T}^{t*}  
       +  \epsilon_f \bar{T}^{t+\Delta t}
$$


.

