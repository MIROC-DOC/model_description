# Mechanical Processes.

## Basic Equations.

### Basic Equations.

The basic equation is ,
Sphere ($\lambda,\varphi$, $\lambda,\varphi$), at $\sigma$ coordinates It is a system of primitive equations and
It is given as follows ( Haltiner and Williams , 1980 ).

1. a series of equations
     
$$
  \frac{\partial \pi}{\partial t} 
    + \mathbf{v}_{H} \cdot \nabla_{\sigma} \pi
     =  - \nabla_{\sigma} \cdot \mathbf{v}_{H} 
          - \frac{\partial \dot{\sigma}}{\partial \sigma}
$$

     > <span id="mass" label="mass" label="mass">\\l.lt[mass]&lt ;/span>

2. hydrostatic pressure formula
     
$$
  \frac{\partial \Phi}{\partial \sigma} = - \frac{RT_v}{\sigma} 
$$

  lt;/span>

3. equation of motion
     
$$
  \frac{\partial \zeta}{\partial t} 
     =   \frac{1}{a\cos\varphi}
            \frac{\partial A_v}{\partial \lambda}
          - \frac{1}{a\cos \varphi}
            \frac{\partial}{\partial \varphi} ( A_u \cos\varphi )
          - {\mathcal D}(\zeta) 
$$

     > <span id="Vorticity" label="Vorticity">\centric\centric\centric\centric\centric\centric\lopen}&lt ;/span>
     
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

     > <span id="divergence" label="divergence">\blaze[divergence]&lt ;/span>

4. thermodynamic equation
     
     > <span id="Heat Power" label="Heat Power">\blaze[Heat Power]&lt ;/span>
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
     
     > <span id="Water Vapor" label="Water Vapor">\blazer\blazer.com > <span id="Water Vapor" label="Water Vapor\cleaner\cleaner\.com lt;/span>
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
 
 
 
 
 
 
 
> <span id="Vorticity definition" label="Vorticity definition">Drumming[Vorticity definition </span>.
 
> <span id="divergent definitions" label="divergent definitions">\blaze[divergent definitions </span>.
 
> <span id="Section B" label="Section B" label="Section B" >\blaze[Section B\blaze]&lt ;/span>
 
> <span id="Section A" label="Section A" label="Section A">\\\\\.3F\.3F\.3F\.3F\.3F\.3F\.3F\.3F\.3F\.3F\.3F\.3F\.3F\.3F\.3F.3F\.3F\.3F.3F.3F\.3F.3F.3F\.3F.3F.\.3F.3F.\.3F.3F.\.3F.3F.\.3F.3F.\\.3F.3F.\.3F.\.3F.\.3F.3F.\\.3F.3F.\\.3F.3F.3F.\.3F.3F.\.3F.\.3F.3F.3F.\.3F.\.3F.3F.\.3F.\.3F.\.3F.3F.\.3F.\.3F.3F.\. ;/span>
 
> <span id="Section E" label="Section E" label="Section E.">\\\lopen[E section]&lt ;/span>
 
 


${\mathcal D}(\zeta), {\mathcal D}(D), {\mathcal D}(T), {\mathcal D}(q)$
is the horizontal diffusion term,
${\mathcal F}_\lambda, {\mathcal F}_\varphi$
are forces due to small-scale kinetic processes (treated as 'physical processes'),
The $Q$ is a process of 'physical processes' such as radiation, condensation, and small-scale kinetic processes
Heating and temperature changes,
The $S_q$ is a system of 'physical processes' such as condensation and small-scale kinetic processes
It is a water vapor source term.
Also, $Q_{diff}$ is a frictional heat,

$$
  Q_{diff}
 = - \mathbf{v} \cdot  ( \frac{\partial \mathbf{v}}{\partial t} )_{diff} .
$$


$( \frac{\partial \mathbf{v}}{\partial t} )_{diff} $ is ,
It is a time-varying term of $u,v$ due to horizontal and vertical diffusion.

### Boundary Conditions.

The boundary conditions for lead-direct current are

$$
  \dot{\sigma} = 0  \ \ \ at \ \ \sigma = 0 , \ 1 .
$$


It is. 
The time-varying surface pressure equation and
Diagnostic Formula for determining the vertical velocity ($\dot{\sigma}$) in the $\sigma$ system

$$
   \frac{\partial \pi}{\partial t}
   = - \int_{0}^{1} \mathbf{v}_{H} \cdot \nabla_{\sigma} \pi d \sigma
     - \int_{0}^{1} D  d \sigma ,
$$

> <span id="barometric pressure trend" label="barometric trend">\blindness </span>.

$$
   \dot{\sigma} 
   = - \sigma 
     \frac{\partial \pi}{\partial t}
     - \int_{0}^{\sigma} D d \sigma
     - \int_{0}^{\sigma} 
         \mathbf{v}_{H} \cdot \nabla_{\sigma} \pi d \sigma ,
$$

> <span id="vertical speed" label="vertical speed">\blazing speed </span>.

is led.

