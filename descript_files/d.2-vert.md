## Vertical Discretization

Following Arakawa and Konor (1996) except for using the Lorentz grid,
the basic equations are discretized vertically by differences. This
scheme has the following characteristics.

- Conservation of the total integrated mass.

- Conservation of the total integrated energy.

- Conservation of the globally integrated angular momentum.

- Conservation of the total mass-integrated potential temperature.

- The hydrostatic pressure equation is localized (the altitude of the
  lower level is independent of the temperature of the upper level).

- For a given temperature distribution, constant in the horizontal
  direction, the hydrostatic pressure equation becomes precisely
  accurate and the barometric gradient force becomes zero.

- Isothermal atmosphere stays permanently isothermal.

### Model Levels

Model level increases in altitude with the vertical level number $k$.
$k=1/2$ corresponds with the model bottom ($\eta=1$), while $k=K+1/2$
corresponds to the model top ($\eta=0$). Variables $\zeta,D,T,q$ are
defined at integer levels ($k=1,2,\ldots K$), while the vertical
velocity $\dot{\eta}$ is defined at half-integer levels
($k=1/2,3/2,\ldots K+1/2$). Using constants $A_{k+1/2}$ and $B_{k+1/2}$
and variable surface pressure $p_s$, air pressure at half levels are
defined as below:
$$
p_{k+1/2} = A_{k+1/2} +B_{k+1/2}\,p_s.  $$

Thus, the normalized pressure $\sigma\equiv p/p_s$ can be written as
below:
$$
\sigma_{k+1/2} = \frac{A_{k+1/2}}{p_s} +B_{k+1/2}.  $$

Using a reference pressure $p_0$, the hybrid-normalized pressure $\eta$
is defined as below:

$$
\eta_{k+1/2} = \frac{A_{k+1/2}}{p_0} +B_{k+1/2},  $$
which is
a constant at all levels and is used as the vertical coordinate by
default in MIROC 6.0.

Pressure at full levels are interpolated from half-level pressure by the
following formula:

$$
p_k = \left\{ \frac{1}{1+\kappa}
\left( \frac{  p^{\kappa +1}_{k-1/2}
- p^{\kappa +1}_{k+1/2}      }
{ p_{k-1/2} - p_{k+1/2} }
\right)
\right\}^{1/\kappa}.
$$

For later use, let us define the following:
$$
\Delta\sigma_k \equiv \sigma_{k-1/2} - \sigma_{k+1/2},
$$
$$
  \Delta B_k \equiv B_{k-1/2} - B_{k+1/2}.$$

### Vertical Discretization

Basic equations vertically discretized at the $\eta$ hybrid coordinates
are shown below.

1. Continuity equation and diagnosis of the vertical velocity

$$
  \frac{\partial \pi}{\partial t}
 = - \sum_{k=1}^{K} \left\{ D_k \Delta\sigma_k + ({\mathbf{v}}_k \cdot \nabla \pi)\Delta B_k \right\}  $$

In MIRCO 6.0, the discretization is conducted in a manner similar to the
$\sigma$ coordinate, which can be optionally selected and was the
default in previous versions, to commonize source codes. Thus, the
vertical velocity is represented as $\dot{\sigma}=m\dot{\eta}/p_s$.
Furthermore, vertical advection $\dot{\eta}(\partial/\partial\eta)$ is
replaced with an equivalent form
$m\dot{\eta}/p_s(\partial/\partial\sigma)$.

$$
(\dot{\sigma}=) \frac{(m \dot{\eta})_{k-1 / 2}}{p_{s}}=-B_{k-1 / 2} \frac{\partial \pi}{\partial t}-\sum_{l=k}^{K}\left\{D_{l} \Delta \sigma_{l}+\left(\mathbf{v}_{l} \cdot \nabla \pi\right) \Delta B_{l}\right\}
$$

$$
  \frac{(m\dot{\eta})_{1/2}}{p_s} = \frac{(m\dot{\eta})_{k+1/2}}{p_s} = 0  $$

2. Hydrostatic equation

$$
\begin{aligned}
\Phi_{1} &=\Phi_{s}+C_{p}\left(\sigma_{1}^{-\kappa}-1\right) T_{v, 1} \\
&=\Phi_{s}+C_{p} \alpha_{1} T_{v, 1}
\end{aligned}
$$

$$
\begin{aligned}
\Phi_{k}-\Phi_{k-1} &=C_{p}\left[\left(\frac{p_{k-1 / 2}}{p_{k}}\right)^{\kappa}-1\right] T_{v, k}+C_{p}\left[1-\left(\frac{p_{k-1 / 2}}{p_{k-1}}\right)^{\kappa}\right] T_{v, k-1} \\
&=C_{p} \alpha_{k} T_{v, k}+C_{p} \beta_{k-1} T_{v, k-1}
\end{aligned}
$$


Here,
$$
 \alpha_k \equiv \left( \frac{ p_{k-1/2} }
                               { p_k } \right)^{\kappa} -1,
$$
$$
 \beta_k \equiv 1- \left( \frac{ p_{k+1/2} }
                               { p_k } \right)^{\kappa} .$$

3. Equations of motion

$$
\begin{aligned}
  \frac{\partial \zeta_k}{\partial t}
        = & \frac{1}{a\cos\varphi}
            \frac{\partial (A_v)_k}{\partial \lambda}
          & - \frac{1}{a\cos\varphi}
            \frac{\partial }{\partial \varphi} (A_u \cos\varphi)_k
          & - {\mathcal D}(\zeta_k)
 \end{aligned}
$$
$$
  \frac{\partial D}{\partial t}
        =  \frac{1}{a\cos\varphi}
            \frac{\partial (A_u)_k}{\partial \lambda}
          + \frac{1}{a\cos\varphi}
            \frac{\partial }{\partial \varphi} (A_v \cos\varphi)_k
          - \nabla^{2}_{\eta}
           ( \Phi_k + R\bar{T} \pi
             + ({\mathit KE})_k )
          - {\mathcal D}(D_k)
$$
$$
\begin{aligned}
  (A_u)_k
    = & ( \zeta_k + f ) v_k
             - \left[ \frac{(m\dot{\eta})_{k-1/2}}{p_s} \frac{u_{k-1} - u_k}{\Delta\sigma_{k-1}+\Delta\sigma_k}
               + \frac{(m\dot{\eta})_{k+1/2}}{p_s} \frac{u_k   - u_{k+1}}{\Delta\sigma_{k}+\Delta\sigma_{k+1}} \right] \\
           & -  \frac{1}{a\cos\varphi} \frac{\partial \pi}{\partial \lambda}(C_p T_{v,k}\hat{\kappa}-R\bar{T})
             + {\mathcal F}_x
\end{aligned}
$$
$$
\begin{aligned}
  (A_v)_k
    = & - ( \zeta_k + f ) u_k
             - \left[ \frac{(m\dot{\eta})_{k-1/2}}{p_s} \frac{v_{k-1} - v_k}{\Delta\sigma_{k-1}+\Delta\sigma_k}
               + \frac{(m\dot{\eta})_{k+1/2}}{p_s} \frac{v_k   - v_{k+1}}{\Delta\sigma_{k}+\Delta\sigma_{k+1}} \right] \\
           &- \frac{1}{a} \frac{\partial \pi}{\partial \varphi}(C_p T_{v,k}\hat{\kappa}-R\bar{T})
             + {\mathcal F}_y
\end{aligned}
$$
$$
   \hat{\kappa}_k
    =\frac{ B_{k-1/2} \alpha_k + B_{k+1/2} \beta_k }
            { \Delta\sigma_k                                  } $$

4. Thermodynamic equation

$$
  \frac{\partial T_k}{\partial t}
     =  - \frac{1}{a\cos\varphi}
               \frac{\partial u_k T'_k}{\partial \lambda}
          - \frac{1}{a\cos\varphi}
               \frac{\partial }{\partial \varphi} (v_k T'_k \cos\varphi)
          + H_k
        + \frac{Q_k}{C_{p}}
          + \frac{(Q_{diff})_k}{C_p}
          - {\mathcal D}(T_k)  $$

Here,
$$
\begin{aligned}
   H_k
     \equiv &  T_k' D_k
              - \left[   \frac{(m\dot{\eta})_{k-1/2}}{p_s} \frac{\hat{T}_{k-1/2} - T_k}{\Delta\sigma_k}
               + \frac{(m\dot{\eta})_{k+1/2}}{p_s} \frac{T_k - \hat{T}_{k+1/2}}{\Delta\sigma_k} \right] \\
        &+ \left\{ \alpha_k
                    \left[ B_{k-1/2} {\mathbf{v}}_k \cdot \nabla \pi
                          - \sum_{l=k}^{K}
                           (D_l \Delta \sigma_l + ({\mathbf{v}}_l \cdot \nabla \pi)\Delta B_l)
                    \right]
             \right. \\
          &+ \left. \beta_k
                     \left[ B_{k+1/2} {\mathbf{v}}_k \cdot \nabla \pi
                          - \sum_{l=k+1}^{K}
                           (D_l \Delta \sigma_l + ({\mathbf{v}}_l \cdot \nabla \pi)\Delta B_l)
                    \right]
              \right\}
              \frac{1}{\Delta \sigma_k} T_{v,k}\\
     = & T_k' D_k
          - \left[ \frac{(m\dot{\eta})_{k-1/2}}{p_s} \frac{\hat{T}_{k-1/2} - T_k}{\Delta \sigma_l}
               + \frac{(m\dot{\eta})_{k+1/2}}{p_s} \frac{T_k - \hat{T}_{k+1/2}}{\Delta \sigma_l} \right] \\
        &+ \hat{\kappa}_k ({\mathbf{v}}_k \cdot \nabla \pi) T_{v,k} \\
        &- \alpha_k \sum_{l=k}^{K}
                           (D_l \Delta \sigma_l + ({\mathbf{v}}_l \cdot \nabla \pi)\Delta B_l)
                            \frac{T_{v,k}}{\Delta \sigma_k} \\
        &- \beta_k \sum_{l=k+1}^{K}
                           (D_l \Delta \sigma_l + ({\mathbf{v}}_l \cdot \nabla \pi)\Delta B_l)
                            \frac{T_{v,k}}{\Delta \sigma_k},
\end{aligned}
$$
$$
  \hat{T}_{k-1/2}
   = a_k T_k + b_{k-1} T_{k-1},
$$
$$
  a_k  =  \alpha_k
              \left[ 1- \left( \frac{ p_k }{ p_{k-1} }
                        \right)^{\kappa} \right]^{-1},
$$
$$
  b_k  =  \beta_k
              \left[ \left( \frac{ p_k }{ p_{k+1} }
                     \right)^{\kappa} - 1 \right]^{-1} .$$

5. Tracers

$$
  \frac{\partial q_k}{\partial t}
      =  - \frac{1}{a\cos\varphi}
               \frac{\partial u_k q_k}{\partial \lambda}
          - \frac{1}{a\cos\varphi}
               \frac{\partial }{\partial \varphi} ( v_k q_k\cos\varphi)
          + R_k
          + S_{q,k}
          - {\mathcal D}(q_k)
$$
$$
R_k  =  q_k D_k
       - \frac{1}{2}
             \left[   \frac{(m\dot{\eta})_{k-1/2}}{p_s} \frac{q_{k-1} - q_k}{\Delta\sigma_k}
               + \frac{(m\dot{\eta})_{k+1/2}}{p_s} \frac{q_k   - q_{k+1}}{\Delta\sigma_k} \right] $$

### Differences from the $\sigma$-Coordinate

In MIROC 6.0, the discretization is conducted in a similar form to the
$\sigma$ coordinate. Thus, differences of discretized equations between
the $\eta$ and $\sigma$ coordinates are relatively small, which are
listed below:

- In the $\sigma$ coordinate, $A_{k+1/2}$ is equal to zero at all levels.

- While $\Delta B_k$ and $\Delta \sigma_k$ are different in the $\eta$ coordinates, those are equivalent to each other in the $\sigma$ coordinate.
