# Dynamics

## Basic Equations

### Basic Equations

The basic equations are a system of primitive equations at the spherical
($\lambda,\varphi$) and $\eta$ coordinates, given as follows (Arakawa
and Konor 1996).

1. Continuity equation

$$
\frac{\partial m}{\partial t}
  + \nabla_{\eta} \cdot (m\mathbf{v}_H)+ \frac{\partial (m\dot{\eta})}{\partial \eta} = 0  $$

2. Hydrostatic equation

$$
\frac{\partial \Phi}{\partial \eta} = - \frac{RT_v}{p} m
$$

3. Equation of motion

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
          - \nabla^{2}_{\eta}
           ( \Phi + R \bar{T} \pi + E )
          - {\mathcal D}(D)   $$

4. Thermodynamic equation

$$
\begin{aligned}
    \frac{\partial T}{\partial t}
    = & - \frac{1}{a\cos\varphi}
      \frac{\partial uT'}{\partial \lambda}
      - \frac{1}{a}
      \frac{\partial }{\partial \varphi} ( vT' \cos\varphi + T' D \\
    & - \dot{\eta}
    \frac{\partial T }{\partial \eta}
    + \frac{\kappa T}{\sigma} \left[ B\left( \frac{\partial \pi}{\partial t}
    + {\mathbf{v}}_{H} \cdot \nabla_{\eta}\pi \right)
    + \frac{ m\dot{\eta} }{ p_s }
    \right]
    + \frac{Q}{C_{p}}
    + \frac{Q_{diff}}{C_{p}}
      - {\mathcal D}(T)
\end{aligned} $$

5. Tracers

For any tracer whose conservative quantity (e.g. mixing ratio) is
denoted as $q$,
$$
\begin{aligned}
  \frac{\partial q}{\partial t}
    = & - \frac{1}{a\cos\varphi}
  \frac{\partial uq}{\partial \lambda} - \frac{1}{a\cos\varphi} \frac{\partial }{\partial \varphi} (vq \cos\varphi) + q D \\
  & - \dot{\eta} \frac{\partial q }{\partial \eta}
    + S_{q}
    - {\mathcal D}(q)
\end{aligned} $$

Here,
$$
m \equiv  \left(\frac{\partial p}{\partial \eta}\right)_{p_s},
$$
$$
\theta  \equiv   T \left( p/p_{0} \right)^{-\kappa},
$$
$$
\kappa  \equiv   R/C_{p},
$$
$$
\Phi  \equiv   gz,
$$
$$
\pi  \equiv   \ln p_{S},
$$
$$
\dot{\eta}  \equiv    \frac{\mathrm{d}\eta}{\mathrm{d}t},
$$
$$
T_v  \equiv   T ( 1+\epsilon_v q ),
$$
$$
T  \equiv   \bar{T} + T^{\prime},
$$
$$
\bar{T} \equiv 300 \ \mathrm{K},
$$

$$
  \zeta  \equiv  \frac{1}{a \cos\varphi }
  \frac{\partial v}{\partial \lambda}
    -  \frac{1}{a \cos\varphi }
  \frac{\partial }{\partial \varphi}
  ( u \cos\varphi ),
$$

$$
  D  \equiv \frac{1}{a \cos\varphi }
  \frac{\partial u}{\partial \lambda}
      + \frac{1}{a \cos\varphi }
  \frac{\partial }{\partial \varphi}
    ( v \cos\varphi ),
$$

$$
  A_u  \equiv ( \zeta + f ) v
    - \dot{\eta} \frac{\partial u}{\partial \eta}
    - \frac{RT^{\prime}}{a\cos\varphi}
  \frac{\partial \pi}{\partial \lambda}
    + {\mathcal F}_x,
$$

$$
  A_v  \equiv - ( \zeta + f ) u
    - \dot{\eta} \frac{\partial v}{\partial \eta}
    - \frac{RT^{\prime}}{a}
  \frac{\partial \pi}{\partial \varphi}
    + {\mathcal F}_y,
$$

$$
E  \equiv \frac{u^{2}+v^{2}}{2},
$$

$$
  {\mathbf{v}}_{H} \cdot \nabla
  \equiv \frac{u}{a \cos \varphi}
  \left( \frac{\partial }{\partial \lambda} \right)_{\sigma}
    + \frac{v}{a}
  \left( \frac{\partial }{\partial \varphi} \right)_{\sigma},
$$

$$
  \nabla^{2}_{\eta}
  \equiv
  \frac{1}{a^{2}\cos^2\varphi}
  \frac{\partial^{2} }{\partial \lambda^{2}}
    + \frac{1}{a^{2}\cos\varphi}
  \frac{\partial }{\partial \varphi}
  \le:wq
  t[ \cos\varphi
  \frac{\partial }{\partial \varphi} \right].
$$

$f$ is the Coriolis parameter.
${\mathcal D}(\zeta), {\mathcal D}(D), {\mathcal D}(T), {\mathcal D}(q)$
are horizontal diffusion terms,
${\mathcal F}_\lambda, {\mathcal F}_\varphi$ are forces due to
small-scale kinetic processes (treated as 'physical processes'), $Q$ are
forces due to radiation, condensation, small-scale kinetic processes,
etc. Heating and temperature change due to 'physical processes', and
$S_q$ is a water vapor source term due to 'physical processes' such as
condensation and small-scale motion. $Q_{\mathrm{diff}}$ is the heat of
friction and

$$
Q_{\mathrm{diff}}
= - {\mathbf{v}} \cdot  \left( \frac{\partial {\mathbf{v}}}{\partial t} \right)_{\mathrm{diff}} .
$$

$( \frac{\partial {\mathbf{v}}}{\partial t} )_{\mathrm{diff}}$ is a
time-varying term of $u,v$ due to horizontal and vertical diffusion.

### Boundary Conditions

Upper and lower boundary conditions for the vertical velocity is:
$$
\dot{\eta} = 0  \ \ \ \text{at~} \ \ \eta = 0 , \ 1 .
$$

The prognostic equation for $p_s$ and the diagnostic equation for the
vertical velocity can be derived by integrating the continuity equation
and applying these boundary conditions.
