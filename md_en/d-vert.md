## Vertical discretization

According to Arakawa and Suarez (1983),
Discretize the basic equations vertically by differences.
The scheme has the following characteristics.

 - Save the total integrated mass

 - Save the total integrated energy

 - Preserving angular momentum for global integration

 - Conservation of total mass-integrated potential temperature

 - The hydrostatic pressure equation comes down to local (the altitude of the lower level is independent of the temperature of the upper level)

 - Constant in the horizontal direction, for a given temperature distribution,
 The hydrostatic pressure equation becomes accurate and the barometric gradient force becomes zero.

 - Isothermal atmosphere stays isothermal forever

### How to take a level.

Number the layers from bottom to top.
If the physical quantity of $\zeta,D,T,q$, $\zeta,D,T,q$ is defined at the integer level (layer) I do.
On the other hand, $\dot{\sigma}$ is defined at the half-integer level.
First, the value of $\sigma$ at a half-integer level
$\sigma_{k-1/2}, (k=1,2,\ldots K)$
Define the .
However, level $\frac{1}{2}$ is the lower end ($\sigma=1$),
Level $K+\frac{1}{2}$ should be the upper end ($\sigma=0$).

Value of $\sigma$ in integer level
$\sigma_k, (k=1,2,\ldots K)$
is obtained from the following equation.

$$
 \sigma_k = \left\{ \frac{1}{1+\kappa}
                     \left( \frac{  \sigma^{\kappa +1}_{k-1/2}
                                  - \sigma^{\kappa +1}_{k+1/2}      }
                                  { \sigma_{k-1/2} - \sigma_{k+1/2} }
                     \right)
              \right\}^{1/\kappa}
$$

> <span id="Bear definition" label="Bear definition">Are you sure? GumaDinformation.com]</span>

Furthermore,

$$
  \Delta \sigma_k \equiv \sigma_{k-1/2} - \sigma_{k+1/2}
$$

> <span id="sigma thickness" label="sigma thickness">Are you sure? Bear thickness </span>

.

### Vertical discretization representation.

The discretized representation of each equation is as follows.

1. continuity formula, vertical velocity
     
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

     
$$
  \dot{\sigma}_{1/2} = \dot{\sigma}_{K+1/2} = 0
$$


2. hydrostatic pressure formula
     
$$
 \Phi_{1}  =  \Phi_{s} + C_{p} ( \sigma_{1}^{-\kappa} - 1  ) T_{v,1} \\
           =  \Phi_{s} + C_{p} \alpha_{1} T_{v,1} 
$$
 

     
$$
 \Phi_k - \Phi_{k-1} 
   =  C_{p}
   \left[ \left( \frac{ \sigma_{k-1/2} }{ \sigma_k } \right)^{\kappa}
          - 1 \right] T_{v,k} 
       + C_{p}
   \left[ 1- 
         \left( \frac{ \sigma_{k-1/2} }{ \sigma_{k-1} } \right)^{\kappa}
              \right] T_{v,k-1} \\
   =    C_{p} \alpha_k T_{v,k} + C_{p} \beta_{k-1} T_{v,k-1}
$$
 

     
 Here,
     
     > <span id="Hydrostatic pressure coefficient" label="Hydrostatic pressure coefficient">Drum pressure coefficient Hydraulic Pressure CoefficientPointPoint.com
$$
 \alpha_k   =  \left( \frac{ \sigma_{k-1/2} }
                               { \sigma_k } \right)^{\kappa} -1 \\
 \beta_k    =  1- \left( \frac{ \sigma_{k+1/2} }
                               { \sigma_k } \right)^{\kappa} .
$$
 


3. equation of motion
     
$$
  \frac{\partial \zeta_k}{\partial t} 
        =   \frac{1}{a\cos\varphi} 
            \frac{\partial (A_v)_k}{\partial \lambda}
          - \frac{1}{a\cos\varphi} 
            \frac{\partial }{\partial \varphi} (A_u \cos\varphi)_k
          - {\mathcal D}(\zeta_k) 
$$

     > <span id="Vorticity After All" label="Vorticity After All">\bout_Vorticity After All </span>.
     
$$
  \frac{\partial D}{\partial t} 
        =   \frac{1}{a\cos\varphi} 
            \frac{\partial (A_u)_k}{\partial \lambda}
          + \frac{1}{a\cos\varphi} 
            \frac{\partial }{\partial \varphi} (A_v \cos\varphi)_k
          - \nabla^{2}_{\sigma}
           ( \Phi_k + C_{p} \hat{\kappa}_k \bar{T}_k \pi 
             + ({\mathit KE})_k )
          - {\mathcal D}(D_k) 
$$

     
 Here,
     
$$
  (A_u)_k
    =  ( \zeta_k + f ) v_k 
             - \frac{1}{2 \Delta \sigma_k} 
             [   \dot{\sigma}_{k-1/2} ( u_{k-1} - u_k   )
               + \dot{\sigma}_{k+1/2} ( u_k   - u_{k+1} ) ]
            \\
           - \frac{C_{p} \hat{\kappa}_k T_{v,k}'}{a\cos\varphi} 
                  \frac{\partial \pi}{\partial \lambda} 
             + {\mathcal F}_x
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
             + {\mathcal F}_y
$$
 

     
  First Kpa\\cleaner\cleaner\cleaner.com
$$
   \hat{\kappa}_k 
    =       \frac{  \sigma_{k-1/2}(   \sigma^{\kappa}_{k-1/2} 
                                    - \sigma^{\kappa}_k      ) 
                  + \sigma_{k+1/2}(   \sigma^{\kappa}_k 
                                    - \sigma^{\kappa}_{k+1/2}  ) }
                 { \sigma^{\kappa}_k
                     ( \sigma_{k-1/2} - \sigma_{k+1/2} )         } 
            \\
  =  \frac{ \sigma_{k-1/2} \alpha_k + \sigma_{k+1/2} \beta_k }
            { \Delta \sigma_k                                  } 
$$
 

     
$$
T'_{v,k} = T_{v,k} - \bar{T}_k
$$


4. thermodynamic equation
     
$$
  \frac{\partial T_k}{\partial t}
     =  - \frac{1}{a\cos\varphi}
               \frac{\partial u_k T'_k}{\partial \lambda}
          - \frac{1}{a\cos\varphi}
               \frac{\partial }{\partial \varphi} (v_k T'_k \cos\varphi)
          + H_k  \\
        + \frac{Q_k}{C_{p}}
          + \frac{(Q_{diff})_k}{C_p} 
          - {\mathcal D}(T_k)  \\
$$
 
 

     
 Here,
     
$$
   H_k 
     \equiv  T_k' D_k
              - \frac{1}{\Delta \sigma_k} 
             [   \dot{\sigma}_{k-1/2} ( \hat{T}_{k-1/2} - T_k   )
               + \dot{\sigma}_{k+1/2} ( T_k   - \hat{T}_{k+1/2} ) ]
                \\
        + \left\{ \alpha_k
                    \left[ \sigma_{k-1/2} \mathbf{v}_k \cdot \nabla \pi
                          - \sum_{l=k}^{K} 
                           ( D_l + \mathbf{v}_l \cdot \nabla \pi )
                            \Delta  \sigma_l
                    \right]
             \right.    \\
          + \left. \beta_k
                     \left[ \sigma_{k+1/2} \mathbf{v}_k \cdot \nabla \pi
                          - \sum_{l=k+1}^{K} 
                           ( D_l + \mathbf{v}_l \cdot \nabla \pi )
                            \Delta  \sigma_l
                    \right]
              \right\} 
              \frac{1}{\Delta \sigma_k} T_{v,k}   \\
%
     =  T_k' D_k 
          - \frac{1}{\Delta \sigma_k} 
             [   \dot{\sigma}_{k-1/2} ( \hat{T}_{k-1/2} - T_k   )
               + \dot{\sigma}_{k+1/2} ( T_k   - \hat{T}_{k+1/2} ) ]
                \\
        + \hat{\kappa}_k \mathbf{v}_k \cdot \nabla \pi T_{v,k} 
                \\
        - \alpha_k \sum_{l=k}^{K} 
                           ( D_l + \mathbf{v}_l \cdot \nabla \pi )
                            \Delta  \sigma_l 
                            \frac{T_{v,k}}{\Delta \sigma_k} 
                \\
        - \beta_k \sum_{l=k+1}^{K} 
                           ( D_l + \mathbf{v}_l \cdot \nabla \pi )
                            \Delta  \sigma_l 
                            \frac{T_{v,k}}{\Delta \sigma_k} 
$$
 
 
 
 
 
 

     
$$
  \hat{T}_{k-1/2}
   =  \frac{ \left[ \left( \frac{ \sigma_{k-1/2} }
                               { \sigma_k } \right)^{\kappa}
                  - 1 \right] \sigma_{k-1}^{\kappa} T_k 
          + \left[ 1- 
                   \left( \frac{ \sigma_{k-1/2} }
                               { \sigma_{k-1} } \right)^{\kappa}
                      \right] \sigma_k^{\kappa} T_{k-1}         }
          { \sigma_{k-1}^{\kappa} - \sigma_k^{\kappa}           } \\
   =  a_k T_k + b_{k-1} T_{k-1}
$$
 

     
     > <span id="Temperature Interpolation Factor" label="Temperature Interpolation Factor">\blaze> <span id="Temperature Interpolation Factor Temperature interpolation coefficient\en.com
$$
  a_k  =  \alpha_k 
              \left[ 1- \left( \frac{ \sigma_k }{ \sigma_{k-1} }
                        \right)^{\kappa} \right]^{-1}   \\
  b_k  =  \beta_k 
              \left[ \left( \frac{ \sigma_k }{ \sigma_{k+1} } 
                     \right)^{\kappa} - 1 \right]^{-1} .  
$$
 


5. water vapor formula
     
$$
  \frac{\partial q_k}{\partial t}
      =   - \frac{1}{a\cos\varphi} 
               \frac{\partial u_k q_k}{\partial \lambda}
          - \frac{1}{a\cos\varphi}
               \frac{\partial }{\partial \varphi} ( v_k q_k\cos\varphi)
          + R_k 
          + S_{q,k}
          - {\mathcal D}(q_k) 
$$

  lt;/span>
     
$$
R_k  =  q_k D_k 
       - \frac{1}{2 \Delta \sigma_k} 
             [   \dot{\sigma}_{k-1/2} ( q_{k-1} - q_k   )
               + \dot{\sigma}_{k+1/2} ( q_k   - q_{k+1} ) ]
$$



