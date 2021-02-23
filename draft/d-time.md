Table of contents

- Time Integration
  - Time integration and time filtering with leap frog (変更なし)
  - Semi-implicit time integration (変更なし)
  - Applying semi-implicit time integration (数式をハイブリッド化済)
  - Time scheme properties and time step estimates (変更なし)
  - Handling of the initiation of time integration (変更なし)

## Time Integration `MODULE: [DYNSTP]`

The time difference scheme is essentially a leap frog. However, the diffusion terms and physical process terms are backward or forward differences. A time filter (Williams, 2009) is used to suppress the computational modes. A semi-implicit method is applied to the gravitational wave term to make the $\Delta t$ larger (Bourke, 1988).

### Time integration and time filtering with leap frog `MODULE: [DADVNC]`

We use leap frog as a time integration scheme for advection terms and so on. A backward difference of $2 \Delta t$ is used for the horizontal diffusion term. The pseudo $p$ surface correction of the diffusion term and the frictional heat due to horizontal diffusion term are treated as corrections, which are forward differences of $2 \Delta t$. The physical process terms (${\mathcal F}_\lambda, {\mathcal F}_\varphi, Q, S_q$) still use the forward difference of $2 \Delta t$ (except for the vertical diffusion term, which uses the forward difference of ${\mathcal F}_\lambda, {\mathcal F}_\varphi, Q, S_q$). (However, the calculation of the time-varying term of vertical diffusion is treated as a backward difference. Please refer to the chapter on physical processes for details.)

Expressed as ${X}$ on behalf of each forecast variable,

$$
  \hat{X}^{t+\Delta t} 
    =  \bar{X}^{t-\Delta t}
    + 2 \Delta t 
      \dot{X}_{adv}\left( {X}^{t} \right)
    + 2 \Delta t 
      \dot{X}_{dif}\left( \hat{X}^{t+\Delta t} \right)
$$

$\dot{X}_{adv}$ is the advection term etc., and $\dot{X}_{dif}$ is the horizontal diffusion term.

To $\hat{X}^{t+\Delta t}$, the term ${X}^{t+\Delta t}$ has been added with corrections for the heat of friction ($\dot{X}_{dis}$) and physical processes ($\dot{X}_{phy}$) for pseudo-equivalent $p$ surface diffusion and horizontal diffusion.

$$
  {X}^{t+\Delta t} 
    =  \hat{X}^{t+\Delta t}
    + 2 \Delta t 
      \dot{X}_{dis}\left( \hat{X}^{t+\Delta t} \right)
    + 2 \Delta t 
      \dot{X}_{phy}\left( \hat{X}^{t+\Delta t} \right)
$$


The time filter of Asselin (1972) is applied every step to remove computational modes in leap frog. I.e., the time filter of Asselin(1972) is applied every step of the way to remove the computation mode in

$$
  \bar{X}^{t}
    = ( 1-2 \epsilon_f ) {X}^{t}
    +  \epsilon_f 
        \left( \bar{X}^{t-\Delta t} + {X}^{t+\Delta t} \right)
$$

and $\bar{X}$. Normally, 0.05 is used as the $\epsilon_f$.

### Semi-implicit time integration

Basically, the leap frog is used in mechanics calculations, but some terms are treated as implicit. Here, we consider the trapezoidal implicit as the implicit. For the vector quantity ${\mathbf q}$, the value of $t$ is written as ${\mathbf q}$, the value of $t+\Delta t$ as ${\mathbf q}^+$, and the value of $t-\Delta t$ as ${\mathbf q}^-$, then the trapezoidal implicit means that the time change term evaluated by $({\mathbf q}^+ +  {\mathbf q}^- )/2$ is This is the solution of the problem by using the leap forg method. We now divide <span>q</span> into two time varying terms, one for the leap forg method and the other for the trapezoidal implicit method, B. We assume that A is nonlinear to <span>q</span>, while B is linear. In other words,

$$
  {\mathbf q}^+ 
      = {\mathbf q}^- 
      + 2 \Delta t {\mathcal A}( {\mathbf q}  )
      + 2 \Delta t B (   {\mathbf q}^+ 
                       + {\mathbf q}^-   )/2
$$

However, $B$ is a square matrix. Then write $\Delta {\mathbf q} \equiv {\mathbf q}^+ - {\mathbf q}$ and you will get

$$
  ( I - \Delta t B ) \Delta {\mathbf q} 
      = 2 \Delta t \left( {\mathcal A}({\mathbf q})
                         + B {\mathbf q} \right) 
$$


This can be easily solved by matrix operations.

### Applying semi-implicit time integration

Then, we apply this method and treat the term of linear gravity waves as implicit. This allows us to reduce the time step $\Delta t$.

In the system of equations, we divide the equation into a linear gravitational wave term ($T=\bar{T}_k$) with a stationary field as the basic field and other terms (with the indices $NG$). Using a vector representation of vertical direction (${\mathbf{D}}=\{ D_{k} \}$ and ${\mathbf{T}}=\{ T_{k} \}$) ERR miura 122

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
         - {\mathcal D}_H {\mathbf{T}} ,
$$

Here, the non-gravitational wave term is

$$
  \left( \frac{\partial \pi}{\partial t} \right)^{NG}
   =   - \sum_{k=1}^{K} {\mathbf{v}}_{k} \cdot \nabla \pi  
       \Delta B_{k}
$$

$$
  \frac{(m\dot{\eta})^{NG}_{k-1/2}}{p_s}
 = - B_{k-1/2} \left( \frac{\partial \pi}{\partial t} \right)^{NG}
   - \sum_{l=k}^{K} {\mathbf{v}}_{l} \cdot \nabla \pi
       \Delta B_{l}
$$

$$
  \left( \frac{\partial D}{\partial t} \right)^{NG}
       =   \frac{1}{a\cos\varphi}
            \frac{\partial (A_u)_{k}}{\partial \lambda}
          + \frac{1}{a\cos\varphi}
            \frac{\partial }{\partial \varphi} (A_v \cos\varphi)_k
          - \nabla^{2}_{\eta} \hat{E}_{k} 
          - {\mathcal D}(D_{k}) 
$$

$$
  \left( \frac{\partial T_{k}}{\partial t} \right)^{NG} 
      =   - \frac{1}{a\cos\varphi} 
               \frac{\partial u_k T'_k}{\partial \lambda}
          - \frac{1}{a\cos\varphi}
               \frac{\partial }{\partial \varphi} (v_k T'_k \cos\varphi)
          + \hat{H}_{k} 
          - {\mathcal D}(T_{k}) 
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
         + \frac{Q_k + (Q_{diff})_k}{C_p}
$$

$$
  \hat{E}_k = E_{k} 
            + \sum_{k=1}^{K} W_{kl} ( T_{v,l}-T_{l} )
$$

where the vector and matrix of the gravitational wave term (underlined) are

$$
  C_{k} = \Delta \sigma_{k}
$$


$$
  W_{kl} = C_{p} \alpha_{l} \delta_{k \geq l}
         + C_{p} \beta_{l} \delta_{k-1 \geq l}
$$

$$
  G_{k} = R\bar{T}
$$

$$
h_{kl} = \frac{\bar{T}}{\Delta\sigma_k}\left[\alpha_k \Delta\sigma_l \delta_{k\ge l}+\beta_k \Delta\sigma_l \delta_{k+1\le l}\right]
$$

Here, for example, $\delta_{k \leq l}$ is 1 if $k \leq l$ is valid and 0 otherwise.

Using the following expression ,

$$
  \delta_{t} {X} \equiv \frac{1}{2 \Delta t} 
        \left( {X}^{t+\Delta t} - {X}^{t-\Delta t} \right)
$$

$$
    \overline{X}^{t}
   \equiv  \frac{1}{2} \left( {X}^{t+\Delta t} 
                              + {X}^{t-\Delta t} \right)
$$
$$
   =  {X}^{t-\Delta t} + \delta_{t} {X} \Delta t   ,
$$

If we apply the semi-implicit method to the system of equations,

$$
  \delta_{t} \pi =
          \left( \frac{\partial \pi}{\partial t} \right)_{NG}  
     - {\mathbf{C}} \cdot \overline{ {\mathbf{D}} }^{t}
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
                         + 2 \Delta t \delta_{t} {\mathbf{D}} )
$$

$$
  \delta_{t} {\mathbf{T}} =
        \left( \frac{\partial {\mathbf{T}}}{\partial t} \right)_{NG}  
         - \underline{h} \overline{ {\mathbf{D}} }^{t} 
         - {\mathcal D}_H ( {\mathbf{T}}^{t-\Delta t}
                        + 2 \Delta t \delta_{t} {\mathbf{T}} )
$$

So..,

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

Since the spherical harmonic expansion is used, we can solve the above equation for $\overline{ {\mathbf{D}}_n^m }^{t}$ with the result that it is in fact, a spherical harmonic expansion is used. After that,

$$
   D^{t+\Delta t} = 2\overline{ {\mathbf{D}} }^{t} - D^{t-\Delta t}
$$

and, (109), (111) to obtain the value $\hat{X}^{t+\Delta t}$ in $t+\Delta t$.

### Time scheme properties and time step estimates

advectional equation

$$
  \frac{\partial{X}}{\partial {t}} = c \frac{\partial{X}}{\partial {x}}
$$


Considering the stability of the discretization in the leap frog in Now,

$$
  X = X_0 \exp(ikx)
$$


If we place the difference between

$$
  X^{n+1} = X^{n-1} + 2 i k \Delta t X^n
$$


That would be. Here,

$$
  \lambda = X^{n+1}/X^n = X^n/X^{n-1} 
$$


So,

$$
  \lambda^2 = 1 + 2 i kc \Delta t \lambda \; .
$$


The solution is called $kc \Delta t = p$,

$$
 \lambda = -i p \pm \sqrt{1-p^2}
$$


This absolute value is

$$
  |\lambda| = \left\{ 
             \begin{array}{ll}
               1 & |p| \le 1 \\
               p \pm \sqrt{p^2-1} & |p| > 1
             \end{array}
             \right.
$$


and in the case of $|p|>1$, we get $|\lambda| > 1$, and the absolute value of the solution increases exponentially with time. This indicates that the computation is unstable.

In the case of $|p| \le 1$, however, the calculation is neutral since the value of $|\lambda| = 1$. However, there are two solutions to $\lambda$, one of which, when set to $\Delta t \rightarrow 1$, leads to $\lambda \rightarrow 1$, while the other leads to $\lambda \rightarrow -1$. This indicates a time-varying solution. This mode is called "computational mode" and is one of the problems of the leap frog method. This mode can be degraded by applying a time filter.

The condition for $|p|=kc \Delta t \le 1$ is that given the horizontal discretization grid spacing $\Delta x$, it causes the maximum value of $k$ to be

$$
  \max k = \frac{\pi}{\Delta x}
$$


From becoming ,

$$
   \Delta t \le \frac{\Delta x}{\pi c}
$$


In the case of the spectral model, the In the case of the spectral model, the Earth's radius is defined as $a$ by the maximum wavenumber, $N$,

$$
   \Delta t \le \frac{a}{N c}  
$$


This is a condition for stability.

In order to guarantee the stability of the integral, for $c$, the fastest advection and propagation speed can be adopted and a time step smaller than $\Delta t$, which is determined by this speed, can be used. When the semi-implicit method is not used, the propagation speed of the gravity wave ($c \sim 300m/s$) is the criterion for stability, but when the semi-implicit method is used, the advection caused by the easterly wind is usually a limiting factor. Therefore, $\Delta t$ assumes that $U_{max}$ is the maximum value of zonal wind,

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
