## Vertical discretization

According to Arakawa and Suarez (1983),
The basic equations are discretized vertically by differences.
This scheme has the following features.

  - Conservation of the total domain-integrated mass

  - Save the total integrated energy

  - Preserving angular momentum for global integration

  - Conservation of total mass-integrated potential temperature

  - The hydrostatic pressure equation comes down to local (the altitude of the lower level is independent of the temperature of the upper level)

  - Constant in the horizontal direction, for a given temperature distribution,
    The hydrostatic pressure equation becomes accurate and the barometric gradient force becomes zero.

  - The isothermal atmosphere stays at the isothermal level indefinitely

### How to take a level.

Number the layers from the bottom to the top.
Assume that the physical quantity of $\zeta,D,T,q$ is defined in terms of integer levels (layers).
On the other hand, $\dot{\sigma}$ is defined by the half-integer level (level).
First, let the value of $\sigma$ at the half-integer level be
$\sigma_{k-1/2}, (k=1,2,\ldots K)$
is defined.
except that level $\frac{1}{2}$ is the lower end ($\sigma=1$),
Level $K+\frac{1}{2}$ should be the uppermost ($\sigma=0$).

The value of $\sigma$ for an integer level
$\sigma_k, (k=1,2,\ldots K)$
is found by the following formula.

$$
 \sigma_k = \left\{ \frac{1}{1+\kappa}
                     \left( \frac{  \sigma^{\kappa +1}_{k-1/2}
                                  - \sigma^{\kappa +1}_{k+1/2}      }
                                  { \sigma_{k-1/2} - \sigma_{k+1/2} }
                     \right)
              \right\}^{1/\kappa}
$$

> <span id="Bear definition" label="Bear definition">\blindness\.0000

Furthermore,

$$
  \Delta \sigma_k \equiv \sigma_{k-1/2} - \sigma_{k+1/2}
$$

> <span id="sigma thickness" label="sigma thickness">Sigma thickness\[sigma thickness]</span>

.

### vertical discretization representation.

The discretized representation of each equation is as follows.

The equation of continuity, vertical velocity

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


2. hydrostatic pressure equation

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
  


    Here ,

    > <span id="Hydrostatic pressure coefficient" label="Hydrostatic pressure coefficient">Are you sure you can't take a look at it?
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

    > <span id="Vorticity After All" label="Vorticity After All">\\\.com\.} </span>.

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
  


    > <span id="Hatchetkappa" label="Hatchetkappa">\\blade\.com\blade\bladeCoCoCoCo.} </span>.
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
  
  


    Where ,

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
  


    > <span id="Temperature Interpolation Factor" label="Temperature Interpolation Factor">\\BackBackBacklash\.com
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

    > <span id="q eventually" label="q eventually" label="q eventually">\\blana[q eventually]</span>

$$
R_k  =  q_k D_k 
       - \frac{1}{2 \Delta \sigma_k} 
             [   \dot{\sigma}_{k-1/2} ( q_{k-1} - q_k   )
               + \dot{\sigma}_{k+1/2} ( q_k   - q_{k+1} ) ]
$$


