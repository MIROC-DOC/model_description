# Mechanical Processes.

## Basic Equations.

### Basic Equations.

The basic equation is ,
It is a system of primitive equations at the spherical ($\lambda,\varphi$) and $\sigma$ coordinates,
It is given as follows ( Haltiner and Williams , 1980 ).

1. a series of expressions

$$
  \frac{\partial \pi}{\partial t} 
    + \mathbf{v}_{H} \cdot \nabla_{\sigma} \pi
     =  - \nabla_{\sigma} \cdot \mathbf{v}_{H} 
          - \frac{\partial \dot{\sigma}}{\partial \sigma}
$$

    > <span id="mass" label="mass" label="mass">\\\\blur[mass]</span>

2. hydrostatic pressure formula

$$
  \frac{\partial \Phi}{\partial \sigma} = - \frac{RT_v}{\sigma} 
$$

    > <span id="hydrostatic" label="hydrostatic" label="hydrostatic pressure">\blaze[hydrostatic pressure]</span>.

3. equation of motion

$$
  \frac{\partial \zeta}{\partial t} 
     =   \frac{1}{a\cos\varphi}
            \frac{\partial A_v}{\partial \lambda}
          - \frac{1}{a\cos \varphi}
            \frac{\partial}{\partial \varphi} ( A_u \cos\varphi )
          - {\mathcal D}(\zeta) 
$$

    > <span id="Vorticity" label="Vorticity" label="Vorticity">\\\\.00002}</span>

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

    > <span id="divergence" label="divergence">\\\[divergence]</span>

4. thermodynamic equation

    > <span id="Heat Power" label="Heat Power">\\blind\blind\blind\.com
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
                            + \mathbf{v}_{H} \cdot \nabla_{\sigma} \pi 
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
 \mathbf{v}_{H} \cdot \nabla
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
  
  
  
  
  
  
  
> <span id="Vorticity definition" label="Vorticity definition">\\\blade\.com.
  
> <span id="Divergent Definitions" label="Divergent Definitions">\\\[Divergent Definitions]</span>
  
> <span id="Section B" label="Section B" label="Section B">\\brachio[Section B]</span>.
  
> <span id="Section A" label="Section A" label="Section A" label="Section A">\\\\\\\.} </span>
  
> <span id="Section E" label="Section E" label="Section E">\\\\\\.}
  
  


${\mathcal D}(\zeta), {\mathcal D}(D), {\mathcal D}(T), {\mathcal D}(q)$
is the horizontal diffusion term,
${\mathcal F}_\lambda, {\mathcal F}_\varphi$
are forces due to small-scale kinetic processes (treated as 'physical processes'),
The $Q$ is a process of 'physical processes' such as radiation, condensation, and small-scale kinetic processes
Heating and temperature changes,
The $S_q$ is a system of 'physical processes' such as condensation and small-scale kinetic processes
The $Q_{diff}$ is a water vapor source term.
The $Q_{diff}$ is the frictional heat,

$$
  Q_{diff}
 = - \mathbf{v} \cdot  ( \frac{\partial \mathbf{v}}{\partial t} )_{diff} .
$$


$( \frac{\partial \mathbf{v}}{\partial t} )_{diff} $ is ,
The time-varying terms of $u,v$ due to horizontal and vertical diffusion.

### Boundary conditions.

The boundary conditions for lead-direct current are

$$
  \dot{\sigma} = 0  \ \ \ at \ \ \sigma = 0 , \ 1 .
$$


. Thus, from ([\\0.25\0.25}(#mass)),
The time-varying surface pressure equation and
Diagnostic Formula for determining the vertical velocity ($\dot{\sigma}$) in the $\sigma$ system

$$
   \frac{\partial \pi}{\partial t}
   = - \int_{0}^{1} \mathbf{v}_{H} \cdot \nabla_{\sigma} \pi d \sigma
     - \int_{0}^{1} D  d \sigma ,
$$

> <span id="barometric tendency" label="barometric tendency">\blazing tendency </span>

$$
   \dot{\sigma} 
   = - \sigma 
     \frac{\partial \pi}{\partial t}
     - \int_{0}^{\sigma} D d \sigma
     - \int_{0}^{\sigma} 
         \mathbf{v}_{H} \cdot \nabla_{\sigma} \pi d \sigma ,
$$

> <span id="vertical speed" label="vertical speed">\blaze[vertical speed]</span>

is led. 

