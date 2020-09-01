## Vertical Diffusion.

### Vertical Diffusion Scheme Overview.

The vertical diffusion scheme evaluates the vertical flux of physical quantities due to sub-grid scale turbulent diffusion. The main input data are wind speed, $u, v$, air temperature, $T$, specific humidity, $q$, and cloud water, $l$, and the output data are the vertical fluxes of momentum, heat, water vapor, and cloud water, as well as the derivative values for obtaining the implicit solution.

The vertical diffusion coefficients are estimated using the level 2 parameterization of the Mellor and Yamada (1974, 1982) turbulent flow closure model.

The outline of the calculation procedure is as follows.

Calculate the Richardson number as the stability of the atmosphere.

2. calculate the diffusion coefficient from Richardson number `MODULE:[VDFCOF]`.

3. calculate the flux and its derivative from the diffusion coefficient.

### Basic Formula for Flux Calculations

The vertical diffuse flux in the atmosphere is evaluated by using the diffusion coefficient $K$ as follows

$$
  F{u} = K_{M} \frac{\partial{u}}{\partial {\sigma}} 
$$


$$
  F{v} = K_M \frac{\partial{v}}{\partial {\sigma}} 
$$


$$
  F{\theta} = K_H \frac{\partial{\theta}}{\partial {\sigma}} 
$$


$$
  F{q} = K_q \frac{\partial{q}}{\partial {\sigma}} 
$$


### Richardson Number.

The bulk Richardson number ($R_{iB}$), which is the benchmark for atmospheric stratification stability, is

$$
R_{iB} = \frac{\displaystyle 
               \frac{g}{\theta_s} \frac{\Delta \theta}{\Delta z} }
              {\displaystyle
                  \left( \frac{\Delta u}{\Delta z} \right)^2 
                + \left( \frac{\Delta v}{\Delta z} \right)^2      }
$$


defined by Here, $(\Delta A)_{k-1/2}$ represents $A_{k} - A_{k-1}$. Also, $(\Delta z)_{k-1/2}$ is defined by the hydrostatic pressure equation,

$$
(\Delta z)_{k-1/2} = \frac{R Tv_{k}}{g} 
                     \frac{(\Delta \sigma)_{k-1/2}}{\sigma_{k-1/2}}
$$


Flux Ricahrdson number $R_{if}$ is ,

$$
R_{if} = \frac{1}{2 \beta_2}
      \left[ \beta_1 + \beta_4 R_{iB}
              - \sqrt{ ( \beta_1 + \beta_4 R_{iB} )^2 
                       - 4 \beta_2 \beta_3 R_{iB} }
              \right] ,
$$


However,

$$
\alpha_1  =  3 A_2 \gamma_1  \\
\alpha_2  =  3 A_2 (\gamma_1+\gamma_2) \\
\beta_1   =  A_1 B_1 ( \gamma_1 - C_1 ) \\
\beta_2   =  A_1 [ B_1 ( \gamma_1 - C_1 ) + 6 A_1 + 3 A_2 ] \\
\beta_3   =  A_2 B_1 \gamma_1 \\
\beta_4   =  A_2 [ B_1 ( \gamma_1 + \gamma_2 ) - 3 A_1 ] ,
$$







$$
(A_1, B_1, A_2, B_2, C_1 ) = ( 0.92, 16.6, 0.74, 10.1, 0.08 ) ,
$$


$$
\gamma_1 = \frac{1}{3} - \frac{2 A_1}{B_1}\, , \, \, \, 
\gamma_2 = \frac{B_2}{B_1} + 6\frac{A_1}{B_1} .
$$


The relationship between $R_{iB}$ and $R_{if}$ is illustrated in the figure[#p-dif:rib-rif]](#p-dif:rib-rif).

### Diffusion Coefficient.

The diffusion coefficients are given for each layer boundary ($k-1/2$ level) as follows.

$$
K_M        =  l^2 \frac{\Delta |{$\mathbf{v}$}|}{\Delta z} S_M  \\
K_H = K_q  =  l^2 \frac{\Delta |{$\mathbf{v}$}|}{\Delta z} S_H 
$$



Here, $S_M, S_H$ are

$$
\widetilde{S_H} = \frac{ \alpha_1-\alpha_2 R_{if} }{ 1-R_{if} }
$$


$$
\widetilde{S_M} = \frac{ \beta_1-\beta_2 R_{if} }{ \beta_3-\beta_4 R_{if} } 
                  \widetilde{S_H} ,
$$


with ,

$$
S_M  =  B_1^{1/2} ( 1- R_{if} )^{1/2} 
          \widetilde{S_M}^{3/2} \\
S_H  =  B_1^{1/2} ( 1- R_{if} )^{1/2} 
          \widetilde{S_M}^{1/2} \widetilde{S_H} .
$$



$l$ is a mixing distance, according to Blakadar (1962),

$$
l = \frac{kz}{1+kz/l_0}
$$


Take the following. $k$ is the Kárman constant. The current standard value is $l_0=200$ m.



### Calculating Flux.

Using the above, we calculate the fluxes and flux derivatives.

$$
  Fu_{k-1/2} = K_{M,k-1/2}(u_{k-1}-u_{k})/(\sigma_{k-1}-\sigma_{k})
$$


$$
  Fv_{k-1/2} = K_{M,k-1/2}(v_{k-1}-v_{k})/(\sigma_{k-1}-\sigma_{k})
$$


$$
  F\theta_{k-1/2} 
  = K_{H,k-1/2}(\theta_{k-1}-\theta_{k})/(\sigma_{k-1}-\sigma_{k})
$$


$$
  Fq_{k-1/2} = K_{q,k-1/2}(q_{k-1}-q_{k})/(\sigma_{k-1}-\sigma_{k})
$$


$$
     \frac{\partial{Fu_{k-1/2}}}{\partial {u_{k-1}}} =   \frac{\partial{Fv_{k-1/2}}}{\partial {v_{k-1}}} 
  = -\frac{\partial{Fu_{k-1/2}}}{\partial {u_{k}}} = - \frac{\partial{Fv_{k-1/2}}}{\partial {v_{k}}}  
  = K_{M,k-1/2}/(\sigma_{k-1}-\sigma_{k})
$$


$$
  \frac{\partial{F\theta_{k-1/2}}}{\partial {T_{k-1}}}
  = \sigma_{k-1}^{-\kappa} K_{H,k-1/2}/(\sigma_{k-1}-\sigma_{k})
$$


$$
  \frac{\partial{F\theta_{k-1/2}}}{\partial {T_{k}}}
 = \sigma_{k}^{-\kappa} K_{H,k-1/2}/(\sigma_{k-1}-\sigma_{k})
$$


$$
  \frac{\partial{Fq_{k-1/2}}}{\partial {u_{k-1}}}
 = - \frac{\partial{Fq_{k-1/2}}}{\partial {u_{k}}}
 = K_{q,k-1/2}/(\sigma_{k-1}-\sigma_{k})
$$


### Minimum Diffusion Coefficient.

In the very stable case, the above estimate gives zero as the diffusion coefficient. If this value is used as it is, various adverse effects on the behavior of the model are observed. The current standard value is $K_{min}=$ 0.15 m$^{2}$/s, which is common to all fluxes.

### Other Notes.

We call shallow cumulus convection `MODULE:[SHLCOF]`, which is a dummy by default.
