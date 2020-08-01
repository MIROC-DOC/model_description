# Mechanical Processes.

## Basic Equations.

### Basic Equations.

The basic equation is ,
It is a system of primitive equations at the spherical ($\lambda,\varphi$) and $\sigma$ coordinates,
It is given as follows ( Haltiner and Williams , 1980 ).

1. a series of equations

$$
  \frac{\partial \pi}{\partial t} 
    + {TERM00002}_{H} \cdot \nabla_{\sigma} \pi
     =  - \nabla_{\sigma} \cdot {TERM00003}_{H} 
          - \frac{\partial \dot{\sigma}}{\partial \sigma}
$$
     --- (1)

2. hydrostatic pressure formula

$$
  \frac{\partial \Phi}{\partial \sigma} = - \frac{RT_v}{\sigma} 
$$
    --- (2)

3. equation of motion

$$
  \frac{\partial \zeta}{\partial t} 
     =   \frac{1}{a\cos\varphi}
            \frac{\partial A_v}{\partial \lambda}
          - \frac{1}{a\cos \varphi}
            \frac{\partial}{\partial \varphi} ( A_u \cos\varphi )
          - {\mathcal D}(\zeta) 
$$
     --- (3)

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
     --- (4)

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
                            + {TERM00004}_{H} \cdot \nabla_{\sigma} \pi 
                            + \frac{ \dot{\sigma} }{ \sigma } 
                     \right)
          + \frac{Q}{C_{p}}
          + \frac{Q_{diff}}{C_{p}}
          - {\mathcal D}(T) 
$$

     --- (5)

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

     --- (6)

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
 {TERM00005}_{H} \cdot \nabla
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
     --- (7)
     --- (8)
     --- (9)
     --- (10)
     --- (11)
     --- (12)
     --- (13)
     --- (14)
     --- (15)
     --- (16)
    --- (17)
     --- (18)

     --- (19)

${\mathcal D}(\zeta), {\mathcal D}(D), {\mathcal D}(T), {\mathcal D}(q)$
is the horizontal diffusion term,
${\mathcal F}_\lambda, {\mathcal F}_\varphi$
are forces due to small-scale kinetic processes (treated as 'physical processes'),
The $Q$ is a process of 'physical processes' such as radiation, condensation, and small-scale kinetic processes
Heating and temperature changes,
The $S_q$ is a process that involves physical processes such as condensation and small-scale motion
It is a water vapor source term.
Also, the $Q_{diff}$ is a frictional heat,

$$
  Q_{diff}
 = - {TERM00011} \cdot  ( \frac{\partial {TERM00012}}{\partial t} )_{diff} .
$$
    --- (20)

$( \frac{\partial {$\mathbf{v}$}}{\partial t} )_{diff} $ is ,
It is a time-varying term of $u,v$ due to horizontal and vertical diffusion.

### Boundary Conditions.

The boundary conditions for lead-direct current are

$$
  \dot{\sigma} = 0  \ \ \ at \ \ \sigma = 0 , \ 1 .
$$
     --- (21)

Therefore, from (1) Therefore, from (1),
The time-varying surface pressure equation and
Diagnostic Formula for determining the vertical velocity ($\dot{\sigma}$) in the $\sigma$ system

$$
   \frac{\partial \pi}{\partial t}
   = - \int_{0}^{1} {TERM00017}_{H} \cdot \nabla_{\sigma} \pi d \sigma
     - \int_{0}^{1} D  d \sigma ,
$$
     --- (22)

$$
   \dot{\sigma} 
   = - \sigma 
     \frac{\partial \pi}{\partial t}
     - \int_{0}^{\sigma} D d \sigma
     - \int_{0}^{\sigma} 
         {TERM00018}_{H} \cdot \nabla_{\sigma} \pi d \sigma ,
$$
     --- (23)

is led.
