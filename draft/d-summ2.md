## Summary of the dynamical core

In this section, we enumerate the calculations performed in the dynamical core, although they overlap with the previous descriptions.

### Conversion of Horizontal Wind to Vorticity and Divergence `MODULE: [G2Wpush, G2Wtrans, G2Wshift, W2Gpush, W2Gtrans, W2Gshift]`

Obtain grid point values of vorticity and divergence from the grid point values of $u _ {ij}, v _ {ij}$ for horizontal wind. First, we obtain the vorticity and divergence in spectral space,  $\zeta _ n^m, D _ n^m$,

$$
\zeta _ n^m  =  \frac{1}{I} \sum _ {i=1}^{I} \sum _ {j=1}^{J}  
                  im v _ {ij} \cos\varphi _ j {Y _ n^{m*}} _ {ij}
                \frac{w _ j}{a(1-\mu _ j^{2})}
           +    \frac{1}{I} \sum _ {i=1}^{I} \sum _ {j=1}^{J}  
                     u _ {ij} \cos\varphi _ j (1-\mu _ j^2)
                  \frac{\partial }{\partial \mu} {Y _ n^{m*}} _ {ij}
                 \frac{w _ j}{a(1-\mu _ j^{2})} \; ,
$$



$$
    D _ n^m  =  \frac{1}{I} \sum _ {i=1}^{I} \sum _ {j=1}^{J}  
                  im u _ {ij} \cos\varphi _ j {Y _ n^{m*}} _ {ij}
                \frac{w _ j}{a(1-\mu _ j^{2})}
           -    \frac{1}{I} \sum _ {i=1}^{I} \sum _ {j=1}^{J}  
                  v _ {ij} \cos\varphi _ j  (1-\mu _ j^2)
                  \frac{\partial }{\partial \mu} {Y _ n^{m*}} _ {ij}
                 \frac{w _ j}{a(1-\mu _ j^{2})} ; .
$$


The grid point value is calculated by

$$
  \zeta _ {ij}
   =  {\mathcal R}{\mathbf{e}} \sum _ {m=-N}^{N} \sum _ {n=|m|}^{N}
      \zeta _ n^m  {Y _ n^m} _ {ij} \; ,
$$


and so on.

### Calculating a virtual temperature `MODULE: [VIRTMD]`

virtual Temperature $T _ v$ is ,

$$
  T _ v = T ( 1 + \epsilon _ v q - l ) \; ,
$$


However, it is $\epsilon _ v = R _ v/R - 1$ and $R _ v$ is the gas constant for water vapor (461 Jkg$^{-1}$K$^{-1}$) and $R$ is the gas constant for air (287.04 Jkg$^{-1}$K$^{-1}$).

### Calculating the pressure gradient term `MODULE: [PSDOT]`

The pressure gradient term $\nabla \pi = \frac{1}{p _ S} \nabla p _ S$ is first used to define the $\pi _ n^m$

$$
  \pi _ n^m  =  \frac{1}{I} \sum _ {i=1}^{I} \sum _ {j=1}^{J}  
               (\ln {p _ S}) _ {ij} {Y _ n^{m *}} _ {ij}  w _ j \; ,
$$

to a spectral representation and then ,

$$
   \frac{1}{a \cos \varphi}
   \left( \frac{\partial \pi}{\partial \lambda} \right) _ {ij}
     =
   \frac{1}{a \cos \varphi}
        {\mathcal R}{\mathbf{e}} \sum _ {m=-N}^{N} \sum _ {n=|m|}^{N}
       im \tilde{X} _ n^m {Y _ n^m} _ {ij}  \; ,
$$


$$
   \frac{1}{a}
   \left( \frac{\partial \pi}{\partial \varphi} \right) _ {ij}
     =  
   \frac{1}{a \cos \varphi}
       {\mathcal R}{\mathbf{e}} \sum _ {m=-N}^{N} \sum _ {n=|m|}^{N}
       \pi _ n^m
       ( 1-\mu^{2} ) \frac{\partial }{\partial \mu} {Y _ n^m} _ {ij}  \; .
$$


### Diagnosis of vertical flow. `MODULE: [PSDOT]`

pressure change term and vertical flow,

$$
  \frac{\partial \pi}{\partial t}
 = - \sum _ {k=1}^{K} ( D _ k + {\mathbf{v}} _ k \cdot \nabla \pi )
       \Delta  \sigma _ k
$$


$$
  \dot{\sigma} _ {k-1/2}
 = - \sigma _ {k-1/2} \frac{\partial \pi}{\partial t}
     - \sum _ {l=k}^{K} ( D _ l + {\mathbf{v}} _ l \cdot \nabla \pi )          
       \Delta  \sigma _ l
$$

and its non-gravity components.

$$
  \left( \frac{\partial \pi}{\partial t} \right)^{NG}
   =   - \sum _ {k=1}^{K} {\mathbf{v}} _ {k} \cdot \nabla \pi  
       \Delta  \sigma _ {k}  \\
$$


$$
  \dot{\sigma}^{NG} _ {k-1/2}
  = - \sigma _ {k-1/2} \left( \frac{\partial \pi}{\partial t} \right)^{NG}
    - \sum _ {l=k}^{K} {\mathbf{v}} _ {l} \cdot \nabla \pi
       \Delta  \sigma _ {l}
$$


### tendency terms due to advection `MODULE: [GRTADV, GRUADV]`.

Momentum advection term `MODULE: [GRUADV]`:

$$
  (A _ u) _ k
    =  ( \zeta _ k + f ) v _ k
             - \frac{1}{2 \Delta \sigma _ k}
             [   \dot{\sigma} _ {k-1/2} ( u _ {k-1} - u _ k   )
               + \dot{\sigma} _ {k+1/2} ( u _ k   - u _ {k+1} ) ]
            \\
           - \frac{C _ {p} \hat{\kappa} _ k T _ {v,k}'}{ a \cos \varphi}
                  \frac{\partial \pi}{\partial \lambda}
$$



$$
  (A _ v) _ k
    =  - ( \zeta _ k + f ) u _ k
             - \frac{1}{2 \Delta \sigma _ k}
             [   \dot{\sigma} _ {k-1/2} ( v _ {k-1} - v _ k   )
               + \dot{\sigma} _ {k+1/2} ( v _ k   - v _ {k+1} ) ]
            \\
           - \frac{C _ {p} \hat{\kappa} _ k T _ {v,k}'}{a}
             \frac{\partial \pi}{\partial \varphi}
$$



$$
 \hat{E} _ k    
  = \frac{1}{2} ( u^2 + v^2 )
    +  \sum _ {k'=1}^{k} \left[  C _ p \alpha _ k ( T _ v - T ) _ {k'}
                              + C _ p \beta _ k ( T _ v - T ) _ {k'-1} \right]
$$


Temperature advection term `MODULE: [GRTADV]`:

$$
 (u T') _ k  = u _ k (T _ k - \bar{T} )
$$


$$
 (v T') _ k  = v _ k (T _ k - \bar{T} )
$$


$$
 \hat{H} _ k  =  T _ {k}^{\prime} D _ {k}  \\
         - \frac{1}{\Delta \sigma _ {k}}
             [   \dot{\sigma} _ {k-1/2} ( \hat{T^{\prime}} _ {k-1/2}
                                         - T^{\prime} _ {k}   )
               + \dot{\sigma} _ {k+1/2} ( T^{\prime} _ {k}  
                                         - \hat{T^{\prime}} _ {k+1/2} ) ]
                \\
         - \frac{1}{\Delta \sigma _ {k}}
             [   \dot{\sigma}^{NG} _ {k-1/2} ( \hat{\bar{T}} _ {k-1/2}
                                         - \bar{T} _ {k}   )
               + \dot{\sigma}^{NG} _ {k+1/2} ( \bar{T} _ {k}  
                                         - \hat{\bar{T}} _ {k+1/2} ) ]
                \\
         + \hat{\kappa} _ {k} T _ {v,k} {\mathbf{v}} _ {k} \cdot \nabla \pi
                \\
         - \frac{\alpha _ {k}}{\Delta \sigma _ {k} } T _ {v,k}
             \sum _ {l=k}^{K} {\mathbf{v}} _ {l} \cdot \nabla \pi
               \Delta \sigma _ {l}
           - \frac{\beta _ {k}}{\Delta \sigma _ {k} } T _ {v,k}
             \sum _ {l=k+1}^{K} {\mathbf{v}} _ {l} \cdot \nabla \pi
               \Delta \sigma _ {l}
                \\
         - \frac{\alpha _ {k}}{\Delta \sigma _ {k} } T' _ {v,k}
             \sum _ {l=k}^{K} D _ l  \Delta \sigma _ {l}
           - \frac{\beta _ {k}}{\Delta \sigma _ {k} } T' _ {v,k}
             \sum _ {l=k+1}^{K} D _ l  \Delta \sigma _ {l}
$$







Water vapor advection term:

$$
 (u q) _ k  = u _ k q _ k
$$


$$
 (v q) _ k  = v _ k q _ k
$$


$$
R _ k  =  q _ k D _ k
       - \frac{1}{2 \Delta \sigma _ k}
             [   \dot{\sigma} _ {k-1/2} ( q _ {k-1} - q _ k   )
               + \dot{\sigma} _ {k+1/2} ( q _ k   - q _ {k+1} ) ]
$$


### Transformation of prognostic variables to spectral space `MODULE: [G2Wpush, G2Wtrans, G2Wshift]`

(122) and (123).

Transform $u _ {ij}^{t-\Delta t}, v _ {ij}^{t-\Delta t}$ to a spectral representation of vorticity and divergence $\zeta _ n^m, D _ n^m$. Furthermore, transforming the temperature $T^{t-\Delta t}$, specific humidity $q^{t-\Delta t}$, and $\pi = \ln p _ S^{t-\Delta t}$ to

$$
  X _ n^m  =  \frac{1}{I} \sum _ {i=1}^{I} \sum _ {j=1}^{J}  
               X _ {ij} {Y _ n^{m *}} _ {ij}  w _ j \; ,
$$


to a spectral representation.

### Transformation of tendency terms to spectral space `MODULE: [G2Wpush, G2Wtrans, G2Wshift]`

Tendency Term of Vorticity


$$
  \frac{\partial{\zeta _ n^m}}{\partial {t}}
    =  \frac{1}{I} \sum _ {i=1}^{I} \sum _ {j=1}^{J}  
    im (A _ v) _ {ij} \cos \varphi _ j
    {Y _ n^{m *}} _ {ij}
    \frac{w _ j}{a(1-\mu _ j^{2})}
\\
  +\frac{1}{I} \sum _ {i=1}^{I} \sum _ {j=1}^{J}  
    (A _ u) _ {ij} \cos \varphi _ j
    (1-\mu _ j^2)
    \frac{\partial }{\partial \mu} {Y _ n^{m *}} _ {ij}
    \frac{w _ j}{a(1-\mu _ j^{2})}
$$



The non-gravity wave component of the tendency term of the divergence

$$
  \left( \frac{\partial{D _ n^m}}{\partial {t}} \right)^{NG}
   =  \frac{1}{I} \sum _ {i=1}^{I} \sum _ {j=1}^{J}  
          im (A _ u) _ {ij} \cos \varphi _ j
          {Y _ n^{m *}} _ {ij}
         \frac{w _ j}{a(1-\mu _ j^{2})}
          \\
   -\frac{1}{I} \sum _ {i=1}^{I} \sum _ {j=1}^{J}  
          (A _ v) _ {ij} \cos \varphi _ j
          (1-\mu _ j^2)
          \frac{\partial }{\partial \mu} {Y _ n^{m *}} _ {ij}
          \frac{w _ j}{a(1-\mu _ j^{2})}
          \\
   -\frac{n(n+1)}{a^{2}}
         \frac{1}{I} \sum _ {i=1}^{I} \sum _ {j=1}^{J}  
          \hat{E} _ {ij}  {Y _ n^{m *}} _ {ij} w _ j
          \\
$$





The non-gravity wave component of the tendency term of temperature

$$
  \left( \frac{\partial{T _ n^m}}{\partial {t}} \right)^{NG}
   =  - \frac{1}{I} \sum _ {i=1}^{I} \sum _ {j=1}^{J}  
          im (u T') _ {ij} \cos \varphi _ j
          {Y _ n^{m *}} _ {ij}
         \frac{w _ j}{a(1-\mu _ j^{2})}
          \\
     + \frac{1}{I} \sum _ {i=1}^{I} \sum _ {j=1}^{J}  
          (v T') _ {ij} \cos \varphi _ j
          (1-\mu _ j^2)
          \frac{\partial }{\partial \mu} {Y _ n^{m *}} _ {ij}
          \frac{w _ j}{a(1-\mu _ j^{2})}
          \\
     + \frac{1}{I} \sum _ {i=1}^{I} \sum _ {j=1}^{J}  
          \hat{H} _ {ij}
          {Y _ n^{m *}} _ {ij} w _ j
$$




Tendency term of water vapor

$$
  \frac{\partial{q _ n^m}}{\partial {t}}
   =  - \frac{1}{I} \sum _ {i=1}^{I} \sum _ {j=1}^{J}  
          im (uq) _ {ij} \cos \varphi _ j
          {Y _ n^{m *}} _ {ij}
         \frac{w _ j}{a(1-\mu _ j^{2})}
          \\
     + \frac{1}{I} \sum _ {i=1}^{I} \sum _ {j=1}^{J}  
          (vq) _ {ij} \cos \varphi _ j
          (1-\mu _ j^2)
          \frac{\partial }{\partial \mu} {Y _ n^{m *}} _ {ij}
          \frac{w _ j}{a(1-\mu _ j^{2})}
          \\
     + \frac{1}{I} \sum _ {i=1}^{I} \sum _ {j=1}^{J}  
          R _ {ij}
          {Y _ n^{m *}} _ {ij} w _ j
$$




### Time integration in spectral space `MODULE: [TINTGR]`

Equations in matrix form

$$
      \left\{ ( 1+2\Delta t {\mathcal D} _ H )( 1+2\Delta t {\mathcal D} _ M )
           \underline{I}  
      - ( \Delta t )^{2}  ( \underline{W} \ \underline{h}
           + (1+2\Delta t {\mathcal D} _ M)
             {\mathbf{G}} {\mathbf{C}}^{T} ) \nabla^{2} _ {\sigma}
  \right\}
      \overline{ {\mathbf{D}} }^{t}
       \\
  = ( 1+2\Delta t {\mathcal D} _ H )( 1-\Delta t {\mathcal D} _ M )
       {\mathbf{D}}^{t-\Delta t}
  +\Delta t
         \left( \frac{\partial {\mathbf{D}}}{\partial t} \right) _ {NG}  
  \\
  -\Delta t \nabla^{2} _ {\sigma}     
                   \left\{  ( 1+2\Delta t {\mathcal D} _ H ) {\mathbf{\Phi}} _ {S}
                          + \underline{W}
                            \left[ ( 1-2\Delta t {\mathcal D} _ H )
                                    {\mathbf{T}}^{t-\Delta t}
                                  + \Delta t
                                      \left( \frac{\partial {\mathbf{T}}}
                                                  {\partial t}     
                                      \right) _ {NG} \right]
                   \right.
  \\
                 \left.  \hspace*{20mm}
                          + ( 1+2\Delta t {\mathcal D} _ H ) {\mathbf{G}}
                            \left[ \pi^{t-\Delta t}
                                  + \Delta t
                                     \left( \frac{\partial \pi}
                                                 {\partial t}
                                     \right) _ {NG}  \right]
                   \right\} .
$$





Using LU decomposition, $\bar{D}$ is obtained by solving for

$$
  \frac{\partial {\mathbf{T}}}{\partial t}
      =   \left( \frac{\partial {\mathbf{T}}}
                        {\partial t}       \right) _ {NG}  
         - \underline{h} {\mathbf{D}}
$$


$$
  \frac{\partial \pi}{\partial t}
      =   \left( \frac{\partial \pi}
                        {\partial t}       \right) _ {NG}  
         - {\mathbf{C}} \cdot {\mathbf{D}}
$$


Calculate the value of the spectrum in $\partial {\mathbf{T}}/\partial t$, $\partial \pi/\partial t$ and then calculate the value of the spectrum in $t+\Delta t$ using

$$
  \zeta^{t+\Delta t}  =  \left( \zeta^{t-\Delta t}
                                +   2 \Delta t \frac{\partial{\zeta}}{\partial {t}} \right)
                          ( 1 + 2 \Delta t {\mathcal D} _ M )^{-1} \\
  D^{t+\Delta t}  =  2 \bar{D} - D^{t-\Delta t}\\
  T^{t+\Delta t}  =  \left( T^{t-\Delta t}
                                +  2 \Delta t  \frac{\partial{T}}{\partial {t}} \right)
                          ( 1 + 2 \Delta t {\mathcal D} _ H )^{-1} \\
  q^{t+\Delta t}  =  \left( q^{t-\Delta t}
                                +  2 \Delta t \frac{\partial{q}}{\partial {t}} \right)
                          ( 1 + 2 \Delta t {\mathcal D} _ E )^{-1} \\
\pi^{t+\Delta t}  =  \pi^{t-\Delta t}
                                +  2 \Delta t \frac{\partial{\pi}}{\partial {t}}
$$






### Transformation of prognostic variables to grid point Values `MODULE: [W2Gpush, W2Gtrans, W2Gshift]`

Obtain grid values of horizontal wind speed from the spectral values of vorticity and divergence ($\zeta _ n^m, D _ n^m$) $u _ {ij}, v _ {ij}$.

$$
  u _ {ij}
  =  \frac{1}{\cos \varphi _ j}
     {\mathcal R}{\mathbf{e}} \sum _ {m=-N}^{N}
                       \sum _ {\stackrel{n=|m|}{n \neq 0}}^{N}
    \left\{
             \frac{a}{n(n+1)} \zeta _ n^m
            (1-\mu^{2}) \frac{\partial{}}{\partial {\mu}} {Y _ n^m} _ {ij}
          -  \frac{im a}{n(n+1)} D _ n^m {Y _ n^m} _ {ij}
    \right\}
$$


$$
  v _ {ij}
  =  \frac{1}{\cos \varphi _ j}
     {\mathcal R}{\mathbf{e}} \sum _ {m=-N}^{N}
                       \sum _ {\stackrel{n=|m|}{n \neq 0}}^{N}
    \left\{
          -  \frac{im a}{n(n+1)} \zeta _ n^m  {Y _ n^m} _ {ij}
          -  \frac{a}{n(n+1)} \tilde{D} _ n^m
            (1-\mu^{2}) \frac{\partial{}}{\partial {\mu}} {Y _ n^m} _ {ij}
    \right\}
$$


Furthermore,

$$
  T _ {ij}
   =  {\mathcal R}{\mathbf{e}} \sum _ {m=-N}^{N} \sum _ {n=|m|}^{N}
      T _ n^m  {Y _ n^m} _ {ij} \; ,
$$


$T _ {ij}, \pi _ {ij}, q _ {ij}$, and so on,

$$
  {p _ S} _ {ij} = \exp \pi _ {ij}
$$


to calculate.

### Diffusion Correction along pressure level `MODULE: [CORDIF]`

The horizontal diffusion is applied on the surface of $\sigma$, but it can cause problems in large slopes, such as transporting water vapor uphill and causing false precipitation at the top of a mountain. To mitigate this problem, corrections have been made for $T,q,l$ to make the diffusion closer to that of the $p$ surface, e.g., for $T,q,l$.

$$
  {\mathcal D} _ p (T) = (-1)^{N _ D/2} K \nabla^{N _ D} _ p T  
                \simeq  (-1)^{N _ D/2} K \nabla^{N _ D} _ {\sigma} T  
                      - \frac{\partial{\sigma}}{\partial {p}}
                      (-1)^{N _ D/2} K \nabla^{N _ D} _ {\sigma} p
                      \cdot \frac{\partial{T}}{\partial {\sigma}}                   \\
                =      (-1)^{N _ D/2} K \nabla^{N _ D} _ {\sigma} T  
                    -  (-1)^{N _ D/2} K \nabla^{N _ D} _ {\sigma} \pi
                          \cdot \sigma \frac{\partial{T}}{\partial {\sigma}}  \\
                =    {\mathcal D} (T)
                    -  {\mathcal D} (\pi)
                       \sigma \frac{\partial{T}}{\partial {\sigma}}
$$




So,

$$
  T _ k \leftarrow  T _ k
       -  2 \Delta t
        \sigma _ {k} \frac{T _ {k+1}-T _ {k-1}}{\sigma _ {k+1} - \sigma _ {k-1}}
        {\mathcal D}(\pi)
$$


and so on. In ${\mathcal D}(\pi)$, the spectral value of $pi$ is converted to a grid by multiplying the spectral value of $\pi _ n^m$ by the spectral representation of the diffusion coefficient.

### Frictional heat associated with diffusion. `MODULE: [CORDIF]`

Frictional heat from diffusion is ,

$$
  Q _ {DIF} = - \left( u _ {ij} {\mathcal D}(u) _ {ij}
                   + v _ {ij} {\mathcal D}(v) _ {ij} \right)
$$


It is estimated that Therefore,

$$
  T _ k \leftarrow  T _ k
       -  \frac{2 \Delta t}{C _ p}
           \left( u _ {ij} {\mathcal D}(u) _ {ij}
                 + v _ {ij} {\mathcal D}(v) _ {ij} \right)
$$

### Horizontal Diffusion and Rayleigh Friction `MODULE: [DSETDF]`

The coefficients of horizontal diffusion can be expressed spectrally,

$$
 {{\mathcal D} _ M} _ n^m = K _ M
                      \left[ \left( \frac{n(n+1)}{a^2} \right)^{N _ D/2}
                                - \left( \frac{2}{a^2} \right)^{N _ D/2}
                      \right]
                  + K _ R
$$


$$
  {{\mathcal D} _ H} _ n^m = K _ M \left( \frac{n(n+1)}{a^2} \right)^{N _ D/2}
$$


$$
  {{\mathcal D} _ E} _ n^m = K _ E \left( \frac{n(n+1)}{a^2} \right)^{N _ D/2}
$$


$K _ R$ is the Rayleigh coefficient of friction. The Rayleigh coefficient of friction is

$$
  K _ R = K _ R^0 \left[ 1+\tanh \left( \frac{z-z _ R}{H _ R} \right) \right]
$$


However, the profile is given in the same way as However,

$$
  z = - H \ln \sigma
$$


The results are approximate to those of $K _ R^0 = {(30day)}^{-1}$ and $z _ R = -H \ln \sigma _ {top}$. The standard values are $K _ R^0 = {(30day)}^{-1}$, $z _ R = -H \ln \sigma _ {top}$ ($\sigma _ {top}$: top level of the model), $H = 8000$ m, and $H _ R = 7000$ m.

### Time Filter `MODULE: [DADVNC]`

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

### Correction for conservation of mass `MODULE: [FIXMAS, MASFIX]`

In the spectral method, the global integral of $\pi = \ln p _ S$ is preserved with rounding errors removed, but the preservation of the mass, i.e. the global integral of $p _ S$ is not guaranteed. Moreover, a wavenumber break in the spectra sometimes results in negative values of the water vapor grid points. For this reason, we perform a correction to preserve the masses of dry air, water vapor, and cloud water, and to remove the regions with negative water vapor content.

Before entering dynamical calculations, `MODULE:[FIXMAS]`, the global integrals of water vapor and cloud water are calculated for $M _ q, M _ l$.

$$
  M _ q^0  =  \sum _ {ijk} q p _ S  \Delta\lambda _ i w _ j \Delta\sigma _ k  \\
  M _ l^0  =  \sum _ {ijk} l p _ S  \Delta\lambda _ i w _ j \Delta\sigma _ k
$$



In the first step of the calculation, the dry mass $M _ d$ is calculated and stored.

$$
  M _ d^0 = \sum _ {ijk} (1-q-l) p _ S \Delta\lambda _ i w _ j \Delta\sigma _ k
$$


After exiting dynamical calculation, `MODULE:[MASFIX]`, the following procedure is followed.

First, negative water vapor is removed by dividing the water vapor from the grid points immediately below the grid points. Suppose that $q _ k < 0 $ is used,

$$
        q _ k'      =  0          \\
        q _ {k-1}'  =  q _ {k-1} + \frac{\Delta p _ k}{\Delta p _ {k-1}} q _ k
$$



 However, this should only be done if it is $q _ {k-1}' \ge 0 $.

Next, set the value to zero for the grid points not removed by the above procedure.

3. calculate the global integral value of $M _ q$ and multiply the global water vapor content by a fixed percentage so that it is the same as that of $M _ q^0$.

$$
        q'' = \frac{M _ q^0}{M _ q} q'
$$


4. correct for dry air mass Likewise calculate $M _ d$,

$$
        p _ S'' = \frac{M _ d^0}{M _ d} p _ S
$$


