# Mechanical Processes.

## Basic Equations.

### Basic Equations.

The fundamental equations are a system of primitive equations at the spherical ($\lambda,\varphi$) and $\sigma$ coordinates, given as follows ( Haltiner and Williams , 1980 ).

1. a series of equations

$$
  \frac{\partial \pi}{\partial t} 
    + {$\mathbf{v}$}_{H} \cdot \nabla_{\sigma} \pi
     =  - \nabla_{\sigma} \cdot {$\mathbf{v}$}_{H} 
          - \frac{\partial \dot{\sigma}}{\partial \sigma}
$$


2. hydrostatic pressure formula

$$
  \frac{\partial \Phi}{\partial \sigma} = - \frac{RT_v}{\sigma} 
$$


3. equation of motion

$$
  \frac{\partial \zeta}{\partial t} 
     =   \frac{1}{a\cos\varphi}
            \frac{\partial A_v}{\partial \lambda}
          - \frac{1}{a\cos \varphi}
            \frac{\partial}{\partial \varphi} ( A_u \cos\varphi )
          - {\mathcal D}(\zeta) 
$$


$$
  \frac{\partial D}{\partial t} 
     =    \frac{1}{a\cos\varphi}
            \frac{\partial A_u}{\partial \lambda}
          + \frac{1}{a\cos\varphi}
            \frac{\partial }{\partial \varphi} ( A_v \cos\varphi )
          - \nabla^{2}_{\sigma}
           ( \Phi + R \bar{T} \pi + E ) 
          - {\mathcal D}(D) 
$$


4. thermodynamic equation

$$
  \frac{\partial T}{\partial t}
     =  - \frac{1}{a\cos\varphi}
               \frac{\partial uT'}{\partial \lambda}
          - \frac{1}{a}
               \frac{\partial }{\partial \varphi} ( vT' \cos\varphi )
          + T' D  \\
        - \dot{\sigma} 
              \frac{\partial T }{\partial \sigma}
          + \kappa T \left( \frac{\partial \pi}{\partial t}
                            + {$\mathbf{v}$}_{H} \cdot \nabla_{\sigma} \pi 
                            + \frac{ \dot{\sigma} }{ \sigma } 
                     \right)
          + \frac{Q}{C_{p}}
          + \frac{Q_{diff}}{C_{p}}
          - {\mathcal D}(T) 
$$



5. water vapor formula

$$
  \frac{\partial q}{\partial t}
   =  - \frac{1}{a\cos\varphi}
               \frac{\partial uq}{\partial \lambda}
          - \frac{1}{a\cos\varphi}
               \frac{\partial }{\partial \varphi} (vq \cos\varphi)
          + q D  \\
        - \dot{\sigma} \frac{\partial q }{\partial \sigma}
          + S_{q}
          - {\mathcal D}(q) 
$$



Here,

$$
\theta  \equiv  T \left( p/p_{0} \right)^{-\kappa} \\
\kappa  \equiv  R/C_{p} \\
  \Phi  \equiv  gz \\
   \pi  \equiv  \ln p_{S} \\
%
 \dot{\sigma}  \equiv   \frac{d \sigma}{d t} \\
%
     T_v  \equiv  T ( 1+\epsilon_v q ) \\
     T  \equiv   \bar{T}(\sigma) + T^{\prime} \\
%
 \zeta  \equiv  \frac{1}{a \cos\varphi }
                    \frac{\partial v}{\partial \lambda} 
             -    \frac{1}{a \cos\varphi }
                    \frac{\partial }{\partial \varphi}
                    ( u \cos\varphi ) \\
%
     D  \equiv  \frac{1}{a \cos\varphi }
                    \frac{\partial u}{\partial \lambda} 
             +    \frac{1}{a \cos\varphi }
                    \frac{\partial }{\partial \varphi}
                    ( v \cos\varphi ) \\
%
    A_u  \equiv   ( \zeta + f ) v
             - \dot{\sigma} \frac{\partial u}{\partial \sigma} 
             - \frac{RT^{\prime}}{a\cos\varphi} 
                  \frac{\partial \pi}{\partial \lambda} 
             + {\mathcal F}_x \\
%
    A_v  \equiv  - ( \zeta + f ) u
             - \dot{\sigma} \frac{\partial v}{\partial \sigma} 
             - \frac{RT^{\prime}}{a}
                  \frac{\partial \pi}{\partial \varphi} 
             + {\mathcal F}_y \\
%
     E  \equiv   \frac{u^{2}+v^{2}}{2} \\
%
 {$\mathbf{v}$}_{H} \cdot \nabla
        \equiv  \frac{u}{a \cos \varphi} 
         \left( \frac{\partial }{\partial \lambda} \right)_{\sigma}
     + \frac{v}{a}
         \left( \frac{\partial }{\partial \varphi} \right)_{\sigma} 
            \\
  \nabla^{2}_{\sigma}  
        \equiv  
               \frac{1}{a^{2}\cos^2\varphi} 
                 \frac{\partial^{2} }{\partial \lambda^{2}} 
             + \frac{1}{a^{2}\cos\varphi} 
                 \frac{\partial }{\partial \varphi}
                 \left[ \cos\varphi
                       \frac{\partial }{\partial \varphi} \right]  .
$$















${\mathcal D}(\zeta), {\mathcal D}(D), {\mathcal D}(T), {\mathcal D}(q)$ are horizontal diffusion terms, ${\mathcal F}_\lambda, {\mathcal F}_\varphi$ are forces due to small-scale kinetic processes (treated as 'physical processes'), $Q$ are forces due to radiation, condensation, small-scale kinetic processes, etc. Heating and temperature change due to 'physical processes', and $S_q$ is a water vapor source term due to 'physical processes' such as condensation and small-scale motion. $Q_{diff}$ is the heat of friction and

$$
  Q_{diff}
 = - {$\mathbf{v}$} \cdot  ( \frac{\partial {$\mathbf{v}$}}{\partial t} )_{diff} .
$$


$( \frac{\partial {$\mathbf{v}$}}{\partial t} )_{diff} $ is a time-varying term of $u,v$ due to horizontal and vertical diffusion.

### Boundary Conditions.

The boundary conditions for lead-direct current are

$$
  \dot{\sigma} = 0  \ \ \ at \ \ \sigma = 0 , \ 1 .
$$


Therefore, from (14), we can calculate the time variation of surface pressure and the vertical velocity of the $\sigma$ system. Therefore, from (14), the equation for the time variation of surface pressure and the diagnostic equation for vertical velocity ($\dot{\sigma}$) in the $\sigma$ system

$$
   \frac{\partial \pi}{\partial t}
   = - \int_{0}^{1} {$\mathbf{v}$}_{H} \cdot \nabla_{\sigma} \pi d \sigma
     - \int_{0}^{1} D  d \sigma ,
$$


$$
   \dot{\sigma} 
   = - \sigma 
     \frac{\partial \pi}{\partial t}
     - \int_{0}^{\sigma} D d \sigma
     - \int_{0}^{\sigma} 
         {$\mathbf{v}$}_{H} \cdot \nabla_{\sigma} \pi d \sigma ,
$$


is led.
