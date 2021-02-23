Table of contents

- Time Integration
  - Time integration and time filtering with leap frog (変更なし)
  - Semi-implicit time integration (変更なし)
  - Applying semi-implicit time integration (数式をハイブリッド化済)
  - Time scheme properties and time step estimates (変更なし)
  - Handling of the initiation of time integration (変更なし)

## Time Integration

The time discretization is essentially the leap frog scheme. However, backward or forward differences are used for diffusion terms and physical process terms. A time filter (Williams, 2009), which is a modified version of the Asselin time filter (Asselin 1972), is used to suppress the computational modes. A semi-implicit method is applied to the gravitational wave term to make the $\Delta t$ larger (Bourke, 1988).

### Time integration and time filtering with leap frog

We use leap frog as the time integration scheme for advection terms and other dynamic terms. A backward difference of $2 \Delta t$ is used for the horizontal diffusion term. The $p$-surface correction of the diffusion term and the frictional heat due to horizontal diffusion term are treated as corrections, which are forward differences of $2 \Delta t$. The physical process terms (${\mathcal F}_\lambda, {\mathcal F}_\varphi, Q, S_q$) still use the forward difference of $2 \Delta t$ (except for the vertical diffusion term, which uses the forward difference of ${\mathcal F}_\lambda, {\mathcal F}_\varphi, Q, S_q$). However, the calculation of the prognositc veriables of vertical diffusion is treated as a backward difference. Please refer to the chapter on physical processes for details.)

Expressing each prognistic variable as ${X}$,

$$
  \hat{X}^{t+\Delta t} 
    =  \bar{X}^{t-\Delta t}
    + 2 \Delta t 
      \dot{X}_{adv}\left( {X}^{t} \right)
    + 2 \Delta t 
      \dot{X}_{dif}\left( \hat{X}^{t+\Delta t} \right),
$$

where $\dot{X}_{adv}$ is the advection term etc., and $\dot{X}_{dif}$ is the horizontal diffusion term.

$\hat{X}^{t+\Delta t}$ is then corrected for diffusion ($\dot{X}_{dis}$ for $p$-surface correction and the heat of friction) and physical processes ($\dot{X}_{phy}$), yielding ${X}^{t+\Delta t}$.

$$
  {X}^{t+\Delta t} 
    =  \hat{X}^{t+\Delta t}
    + 2 \Delta t 
      \dot{X}_{dis}\left( \hat{X}^{t+\Delta t} \right)
    + 2 \Delta t 
      \dot{X}_{phy}\left( \hat{X}^{t+\Delta t} \right)
$$


To reduce numerical mode, a time filter (Williams, 2009) is applied to leap-frog method at every steps.
The time filter is given as follow.
The terms with over bars is filtered.

$$
\bar{\bar{X}}^{t} = \bar{X}^{t} + \nu \alpha [\bar{\bar{X}}^{t-\Delta t} - \bar{X}^{t} + X^{t+\Delta t}],
$$
$$
\bar{X}^{t+\Delta t} = X^{t+\Delta t} + \nu (1-\alpha) [\bar{\bar{X}}^{t-\Delta t} - 2 \bar{X}^{t} + X^{t+\Delta t}],
$$

where $\nu=0.05$ and $\alpha=0.5$.

### Semi-implicit time integration

Basically, the leap frog is used for the dynamic processes, but the trapezoidal implicit scheme is used for some terms. For a vector quantity ${\mathbf q}$, let us write the value at $t$ as ${\mathbf q}$, the value at $t+\Delta t$ as ${\mathbf q}^+$, and the value at $t-\Delta t$ as ${\mathbf q}^-$. Then, in the trapezoidal implicit scheme, the time change term is evaluated for $({\mathbf q}^+ +  {\mathbf q}^- )/2$, instead of ${\mathbf q}$ used in the simple leap forg method. We now divide ${\mathbf q}$ into two time varying terms, one (${\mathcal A}$) for the leap forg method and the other (${\mathcal B}$) for the trapezoidal implicit method. We assume that (${\mathcal A}$) is nonlinear to ${\mathbf q}$, while (${\mathcal B}$) is linear. In other words,

$$
  {\mathbf q}^+ 
      = {\mathbf q}^- 
      + 2 \Delta t {\mathcal A}( {\mathbf q}  )
      + 2 \Delta t B (   {\mathbf q}^+ 
                       + {\mathbf q}^-   )/2,
$$

where (${\mathcal B}$) is a square matrix. Defining $\Delta {\mathbf q} \equiv {\mathbf q}^+ - {\mathbf q}$, we get

$$
  ( I - \Delta t B ) \Delta {\mathbf q} 
      = 2 \Delta t \left( {\mathcal A}({\mathbf q})
                         + B {\mathbf q} \right).
$$

This can be easily solved by matrix operations.

### Applying the semi-implicit time integration

Here, we apply the semi-implicit method and treat terms associated with linear gravity waves as implicit, which allows us to increase the time step $\Delta t$.

We divide the basic equation into a linear gravity wave term ($T=\bar{T}_k$) with a static field as the basic field and other terms (with the indices $NG$). Using a vector representation for the vertical direction (${\mathbf{D}}=\{ D_{k} \}$ and ${\mathbf{T}}=\{ T_{k} \}$),

$$
   \frac{\partial \pi}{\partial t} = 
          \left( \frac{\partial \pi}{\partial t} \right)_{NG}  
     - {\mathbf{C}} \cdot {\mathbf{D}},
$$

$$
  \frac{\partial {\mathbf{D}}}{\partial t} = 
          \left( \frac{\partial {\mathbf{D}}}{\partial t} \right)_{NG}  
          - \nabla^{2}_{\eta} ( {\mathbf{\Phi}}_{S} 
                                  + \underline{W} {\mathbf{T}}
                                  + {\mathbf{G}} \pi )  
          - {\mathcal D}_M {\mathbf{D}} ,
$$

$$
  \frac{\partial {\mathbf{T}}}{\partial t} 
      =   \left( \frac{\partial {\mathbf{T}}}
                        {\partial t}       \right)_{NG}  
         - \underline{h} {\mathbf{D}}
         - {\mathcal D}_H {\mathbf{T}}.
$$

Here, the non-gravitational wave term is

$$
  \left( \frac{\partial \pi}{\partial t} \right)^{NG}
   =   - \sum_{k=1}^{K} {\mathbf{v}}_{k} \cdot \nabla \pi  
       \Delta B_{k},
$$

$$
  \frac{(m\dot{\eta})^{NG}_{k-1/2}}{p_s}
 = - B_{k-1/2} \left( \frac{\partial \pi}{\partial t} \right)^{NG}
   - \sum_{l=k}^{K} {\mathbf{v}}_{l} \cdot \nabla \pi
       \Delta B_{l},
$$

$$
  \left( \frac{\partial D}{\partial t} \right)^{NG}
       =   \frac{1}{a\cos\varphi}
            \frac{\partial (A_u)_{k}}{\partial \lambda}
          + \frac{1}{a\cos\varphi}
            \frac{\partial }{\partial \varphi} (A_v \cos\varphi)_k
          - \nabla^{2}_{\eta} \hat{E}_{k} 
          - {\mathcal D}(D_{k}),
$$

$$
  \left( \frac{\partial T_{k}}{\partial t} \right)^{NG} 
      =   - \frac{1}{a\cos\varphi} 
               \frac{\partial u_k T'_k}{\partial \lambda}
          - \frac{1}{a\cos\varphi}
               \frac{\partial }{\partial \varphi} (v_k T'_k \cos\varphi)
          + \hat{H}_{k} 
          - {\mathcal D}(T_{k}),
$$

$$
 \hat{H}_k  =  T_{k}^{\prime} D_{k}
$$
$$
         - \left[   \frac{(m\dot{\eta})_{k-1/2}}{p_s} \frac{\hat{T}_{k-1/2} - T_k}{\Delta\sigma_k}
               + \frac{(m\dot{\eta})_{k+1/2}}{p_s} \frac{T_k - \hat{T}_{k+1/2}}{\Delta\sigma_k} \right]
$$
$$
         + \hat{\kappa}_{k} T_{v,k} {\mathbf{v}}_{k} \cdot \nabla \pi
$$
$$
         - \frac{\alpha_{k}}{\Delta \sigma_{k} } T_{v,k}
             \sum_{l=k}^{K} {\mathbf{v}}_{l} \cdot \nabla \pi 
               \Delta B_{l}
           - \frac{\beta_{k}}{\Delta \sigma_{k} } T_{v,k}
             \sum_{l=k+1}^{K} {\mathbf{v}}_{l} \cdot \nabla \pi 
               \Delta B_{l}
$$
$$
         - \frac{\alpha_{k}}{\Delta \sigma_{k} } T'_{v,k}
             \sum_{l=k}^{K} D_l  \Delta \sigma_{l}
           - \frac{\beta_{k}}{\Delta \sigma_{k} } T'_{v,k}
             \sum_{l=k+1}^{K} D_l  \Delta \sigma_{l}
$$
$$
         + \frac{Q_k + (Q_{diff})_k}{C_p},
$$

$$
  \hat{E}_k = E_{k} 
            + \sum_{k=1}^{K} W_{kl} ( T_{v,l}-T_{l} ),
$$

where the vector and matrix of the gravitational wave term (underlined) are

$$
  C_{k} = \Delta \sigma_{k},
$$


$$
  W_{kl} = C_{p} \alpha_{l} \delta_{k \geq l}
         + C_{p} \beta_{l} \delta_{k-1 \geq l},
$$

$$
  G_{k} = R\bar{T},
$$

$$
h_{kl} = \frac{\bar{T}}{\Delta\sigma_k}\left[\alpha_k \Delta\sigma_l \delta_{k\ge l}+\beta_k \Delta\sigma_l \delta_{k+1\le l}\right].
$$

Here, $\delta_{k \leq l}$ is 1 if $k \leq l$ is valid and 0 otherwise.

We now use the following expressions for time differences:

$$
  \delta_{t} {X} \equiv \frac{1}{2 \Delta t} 
        \left( {X}^{t+\Delta t} - {X}^{t-\Delta t} \right),
$$

$$
    \overline{X}^{t}
   \equiv  \frac{1}{2} \left( {X}^{t+\Delta t} 
                              + {X}^{t-\Delta t} \right)
$$
$$
   =  {X}^{t-\Delta t} + \delta_{t} {X} \Delta t.
$$

Then, applying the semi-implicit method to the system of equations, we get

$$
\label{#eqn_for_pi}
  \delta_{t} \pi =
          \left( \frac{\partial \pi}{\partial t} \right)_{NG}  
     - {\mathbf{C}} \cdot \overline{ {\mathbf{D}} }^{t},
$$

$$
  \delta_{t} {\mathbf{D}} =
          \left( \frac{\partial {\mathbf{D}}}{\partial t} \right)_{NG}  
          - \nabla^{2}_{\eta} ( {\mathbf{\Phi}}_{S} 
                                  + \underline{W} 
                                     \overline{ {\mathbf{T}} }^{t}
                                  + {\mathbf{G}}
                                  \overline{\pi}^{t} ) 
          - {\mathcal D}_M ( {\mathbf{D}}^{t-\Delta t} 
                         + 2 \Delta t \delta_{t} {\mathbf{D}} ),
$$

$$
\label{eqn_for_t}
  \delta_{t} {\mathbf{T}} =
        \left( \frac{\partial {\mathbf{T}}}{\partial t} \right)_{NG}  
         - \underline{h} \overline{ {\mathbf{D}} }^{t} 
         - {\mathcal D}_H ( {\mathbf{T}}^{t-\Delta t}
                        + 2 \Delta t \delta_{t} {\mathbf{T}} ).
$$

Thus,

$$
      \left\{ ( 1+2\Delta t {\mathcal D}_H )( 1+2\Delta t {\mathcal D}_M )
           \underline{I}  
      - ( \Delta t )^{2}  ( \underline{W} \ \underline{h} 
           + (1+2\Delta t {\mathcal D}_M)
             {\mathbf{G}} {\mathbf{C}}^{T} ) \nabla^{2}_{\eta}
  \right\}
      \overline{ {\mathbf{D}} }^{t} 
$$
$$
  = ( 1+2\Delta t {\mathcal D}_H )( 1+\Delta t {\mathcal D}_M ) 
       {\mathbf{D}}^{t-\Delta t}
  + \Delta t 
     \left( \frac{\partial {\mathbf{D}}}{\partial t} \right)_{NG}  
$$
$$
  -  \Delta t \nabla^{2}_{\eta}     
                   \left\{  ( 1+2\Delta t {\mathcal D}_H ) {\mathbf{\Phi}}_{S} 
                          + \underline{W} 
                            \left[ ( 1+2\Delta t {\mathcal D}_H ) 
                                    {\mathbf{T}}^{t-\Delta t}
                                  + \Delta t 
                                      \left( \frac{\partial {\mathbf{T}}}
                                                  {\partial t}     
                                      \right)_{NG} \right]
                   \right.
$$
$$
                 \left.  \hspace*{20mm} 
                          + ( 1+2\Delta t {\mathcal D}_H ) {\mathbf{G}} 
                            \left[ \pi^{t-\Delta t} 
                                  + \Delta t
                                     \left( \frac{\partial \pi}
                                                 {\partial t} 
                                     \right)_{NG}  \right]
                   \right\} . 
$$

Since the spherical harmonic expansion is used, we can rewrite $\nabla_{\eta}^2$ as the following:

$$
\nabla_{\eta}^2=-\frac{n(n+1)}{a^2},
$$

which enables us to solve the above equations for $\overline{ {\mathbf{D}}_n^m }^{t}$. Then, using (\ref{eqn_for_pi}), (\ref{eqn_for_t}) and $D^{t+\Delta t} = 2\overline{ {\mathbf{D}} }^{t} - D^{t-\Delta t},$

we can obtain the value of prognostic variables $\hat{X}^{t+\Delta t}$ at $t+\Delta t$.

### Time scheme properties and requiments for time steps

Let us consider solving the advection equation with the leap-frog method:

$$
  \frac{\partial{X}}{\partial {t}} = c \frac{\partial{X}}{\partial {x}}.
$$

Assuming $X = X_0 \exp(ikx)$, the descretized form of the above equation becomes:

$$
  X^{n+1} = X^{n-1} + 2 i k \Delta t X^n.
$$

Assuming $X$ evolves exponentially, we can define $\lambda$ such that

$$
  \lambda = X^{n+1}/X^n = X^n/X^{n-1},
$$
$$
  \lambda^2 = 1 + 2 i kc \Delta t \lambda \; .
$$

Defining $p \equiv kc \Delta t$, the solution becomes:

$$
 \lambda = -i p \pm \sqrt{1-p^2}.
$$

The absolute value of those solutions are

$$
  |\lambda| = \left\{ 
             \begin{array}{ll}
               1 & |p| \le 1 \\
               p \pm \sqrt{p^2-1} & |p| > 1
             \end{array}
             \right.
$$


and in the case of $|p|>1$, we get $|\lambda| > 1$, and the absolute value of the solution increases exponentially with time. This indicates that the computation is unstable.

In the case of $|p| \le 1$, however, the calculation is neutral since the value of $|\lambda| = 1$. However, there are two solutions to $\lambda$, one of which, when set to $\Delta t \rightarrow 1$, leads to $\lambda \rightarrow 1$, while the other leads to $\lambda \rightarrow -1$, which indicates an osscilating solution. This mode is called "computational mode" and is one of the problems of the leap frog method. This mode can be damped by applying a time filter described later.

Given the horizontal grid spacing $\Delta x$, the maximum value of $k$ to becomes

$$
  \max k = \frac{\pi}{\Delta x}.
$$

Then, the condition $|p|=kc \Delta t \le 1$ requires

$$
   \Delta t \le \frac{\Delta x}{\pi c}.
$$

In case of a spectral model, using the Earth's radius $a$ and the maximum wavenumber $N$, the requirement becomes

$$
   \Delta t \le \frac{a}{N c},
$$

which is a condition for the numerical stability.

In order to guarantee the stability of the integration, for $c$, the fastest advection and propagation speed can be adopted and a time step smaller than $\Delta t$, which is determined by this speed, can be used. When the semi-implicit method is not used, the propagation speed of the gravity wave ($c \sim 300m/s$) is the criterion for stability, but when the semi-implicit method is used, the advection caused by the easterly wind is usually a limiting factor. Therefore, $\Delta t$ assumes that $U_{max}$ is the maximum value of zonal wind,

$$
   \Delta t \le \frac{a}{N U_{max}}  
$$


In practice, this is multiplied by a safety factor. In practice, this is multiplied by a safety factor.

### Handling of the initiation of time integration

When starting from a suitable initial value that is not calculated by AGCM, it is not possible to give two physical quantities of time, $t$ and $t-\Delta t$, that are consistent with the model. However, giving an inconsistent value for $t-\Delta t$ will result in a large computation mode.

So, firstly, as $X^{\Delta t/4} = X^0$, in the time step of $1/4$

$$
  X^{\Delta t/2} = X^0 + \Delta t/2 \dot{X}^{\Delta t/4}
                 = X^0 + \Delta t/2 \dot{X}^0
$$

and furthermore, in the time step of $1/2$,

$$
  X^{\Delta t}   = X^0 + \Delta t \dot{X}^{\Delta t/2}
$$

And, in the original time step,

$$
  X^{2\Delta t}   = X^0 + 2 \Delta t \dot{X}^{\Delta t}
$$

and use leap frog as usual, it prevents the occurrence of the calculation mode.
