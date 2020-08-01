## Time integration.

The time difference scheme is basically a leap frog.
However, the terms of the diffusion terms and physical processes are backward or forward differences.
A time filter (Asselin, 1972) is used to suppress the computational mode.
And to make the $\Delta t$ larger,
Applying the semi-implicit method to the term gravitational wave (Bourke, 1988).

### Time integration and time filtering with leap frog

The leap frog is used as a time integration scheme for advection terms and so on.
The backward difference of $2 \Delta t$ is used for the horizontal diffusion term.
In addition, the pseudo $p$ surface correction of the diffusion term and the frictional heat term by horizontal diffusion are
treated as a correction and becomes the forward difference in $2 \Delta t$.
The physical process section (${\mathcal F}_\lambda, {\mathcal F}_\varphi, Q, S_q$) is ,
I still use the forward differential of $2 \Delta t$.
(However, we treat the calculation of the time varying term of vertical diffusion as a backward difference.
See the chapter on physical processes for details.)

Expressed as ${X}$ on behalf of each forecast variable,

$$
  \hat{X}^{t+\Delta t} 
    =  \bar{X}^{t-\Delta t}
    + 2 \Delta t 
      \dot{X}_{adv}\left( {X}^{t} \right)
    + 2 \Delta t 
      \dot{X}_{dif}\left( \hat{X}^{t+\Delta t} \right)
$$
     --- (1)

$ \dot{X}_{adv} $ is an advection term etc,
$ \dot{X}_{dif} $ is a horizontal diffusion term.

$ \hat{X}^{t+\Delta t} $ has a ,
Pseudo, etc. $p$ Correction of frictional heat ($ \dot{X}_{dis} $) by surface and horizontal diffusion
and physical processes ($ \dot{X}_{phy} $) have been added,
$ {X}^{t+\Delta t} $.

$$
  {X}^{t+\Delta t} 
    =  \hat{X}^{t+\Delta t}
    + 2 \Delta t 
      \dot{X}_{dis}\left( \hat{X}^{t+\Delta t} \right)
    + 2 \Delta t 
      \dot{X}_{phy}\left( \hat{X}^{t+\Delta t} \right)
$$
    --- (2)

To remove the computation mode in leap frog
Apply the time filter of Asselin (1972) at every step.
Namely,

$$
  \bar{X}^{t}
    = ( 1-2 \epsilon_f ) {X}^{t}
    +  \epsilon_f 
        \left( \bar{X}^{t-\Delta t} + {X}^{t+\Delta t} \right)
$$
     --- (3)

and $\bar{X}$.
For $\epsilon_f$ it is standard to use 0.05.

### semi-implicit time integration

For mechanics calculations, the leap frog is basically used,
Compute some terms as implicit.
Here, implicit considers a trapezoidal implicit.
Regarding the vector quantity ${\mathbf q}$,
The value in $t$ is converted to ${\mathbf q}$,
The value in $t+\Delta t$ was converted to ${\mathbf q}^+$,
If you write the value of $t-\Delta t$ as ${\mathbf q}^-$,
What is trapezoidal implicit?
$({\mathbf q}^+ +  {\mathbf q}^- )/2$.
The solution is done by using the time-varying terms evaluated by using
Now, as a time-varying term in <span>q</span>,
The term A is treated in the leap forg method and the term B is treated in the trapezoidal implicit method.
Assume that A is nonlinear for <span>q</span>, but B is linear.
Namely,

$$
  {\mathbf q}^+ 
      = {\mathbf q}^- 
      + 2 \Delta t {\mathcal A}( {\mathbf q}  )
      + 2 \Delta t B (   {\mathbf q}^+ 
                       + {\mathbf q}^-   )/2
$$
     --- (4)

Note that $B$ is a square matrix. Then,
$\Delta {\mathbf q} \equiv {\mathbf q}^+ - {\mathbf q}$
And then you can write,

$$
  ( I - \Delta t B ) \Delta {\mathbf q} 
      = 2 \Delta t \left( {\mathcal A}({\mathbf q})
                         + B {\mathbf q} \right) 
$$
     --- (5)

This can be easily solved by matrix operations.

### Applying semi-implicit time integration

So we apply this method and treat the term of linear gravity waves as implicit.
This makes the time step $\Delta t$ smaller.

In a system of equations, the basic field is such that $T=\bar{T}_k$
Separation of the linear gravitational wave term and the other terms (with the index $NG$).
Vertical Vector Representation
Using ${$\mathbf{D}$}=\{ D_{k} \}$, ${$\mathbf{T}$}=\{ T_{k} \}$,

$$
   \frac{\partial \pi}{\partial t} = 
          \left( \frac{\partial \pi}{\partial t} \right)_{NG}  
     - {TERM00031} \cdot {TERM00032}  ,
$$
     --- (6)

$$
  \frac{\partial {TERM00033}}{\partial t} = 
          \left( \frac{\partial {TERM00034}}{\partial t} \right)_{NG}  
          - \nabla^{2}_{\sigma} ( {TERM00035}_{S} 
                                  + \underline{W} {TERM00036}
                                  + {TERM00037} \pi )  
          - {\mathcal D}_M {TERM00038} ,
$$
     --- (7)

$$
  \frac{\partial {TERM00039}}{\partial t} 
      =   \left( \frac{\partial {TERM00040}}
                        {\partial t}       \right)_{NG}  
         - \underline{h} {TERM00041}
         - {\mathcal D}_H {TERM00042} ,
$$
     --- (8)

Here, the non-gravitational wave term is

$$
  \left( \frac{\partial \pi}{\partial t} \right)^{NG}
   =   - \sum_{k=1}^{K} {TERM00043}_{k} \cdot \nabla \pi  
       \Delta  \sigma_{k}  \\
   =   Z_{k}
$$
     --- (9)

$$
  \dot{\sigma}^{NG}_{k-1/2}
 = - \sigma_{k-1/2} \left( \frac{\partial \pi}{\partial t} \right)^{NG}
   - \sum_{l=k}^{K} {TERM00044}_{l} \cdot \nabla \pi
       \Delta  \sigma_{l}
$$
     --- (10)

$$
  \left( \frac{\partial D}{\partial t} \right)^{NG}
       =   \frac{1}{a\cos\varphi}
            \frac{\partial (A_u)_{k}}{\partial \lambda}
          + \frac{1}{a\cos\varphi}
            \frac{\partial }{\partial \varphi} (A_v \cos\varphi)_k
          - \nabla^{2}_{\sigma} \hat{E}_{k} 
          - {\mathcal D}(D_{k}) 
$$
     --- (11)

$$
  \left( \frac{\partial T_{k}}{\partial t} \right)^{NG} 
      =   - \frac{1}{a\cos\varphi} 
               \frac{\partial u_k T'_k}{\partial \lambda}
          - \frac{1}{a\cos\varphi}
               \frac{\partial }{\partial \varphi} (v_k T'_k \cos\varphi)
          + \hat{H}_{k} 
          - {\mathcal D}(T_{k}) 
$$
     --- (12)

$$
 \hat{H}_k  =  T_{k}^{\prime} D_{k}  \\
         - \frac{1}{\Delta \sigma_{k}} 
             [   \dot{\sigma}_{k-1/2} ( \hat{T^{\prime}}_{k-1/2} 
                                         - T^{\prime}_{k}   )
               + \dot{\sigma}_{k+1/2} ( T^{\prime}_{k}  
                                         - \hat{T^{\prime}}_{k+1/2} ) ]
                \\
         - \frac{1}{\Delta \sigma_{k}} 
             [   \dot{\sigma}^{NG}_{k-1/2} ( \hat{\bar{T}}_{k-1/2} 
                                         - \bar{T}_{k}   )
               + \dot{\sigma}^{NG}_{k+1/2} ( \bar{T}_{k}  
                                         - \hat{\bar{T}}_{k+1/2} ) ]
                \\
         + \hat{\kappa}_{k} T_{v,k} {TERM00045}_{k} \cdot \nabla \pi
                \\
         - \frac{\alpha_{k}}{\Delta \sigma_{k} } T_{v,k}
             \sum_{l=k}^{K} {TERM00046}_{l} \cdot \nabla \pi 
               \Delta \sigma_{l}
           - \frac{\beta_{k}}{\Delta \sigma_{k} } T_{v,k}
             \sum_{l=k+1}^{K} {TERM00047}_{l} \cdot \nabla \pi 
               \Delta \sigma_{l}
                \\
         - \frac{\alpha_{k}}{\Delta \sigma_{k} } T'_{v,k}
             \sum_{l=k}^{K} D_l  \Delta \sigma_{l}
           - \frac{\beta_{k}}{\Delta \sigma_{k} } T'_{v,k}
             \sum_{l=k+1}^{K} D_l  \Delta \sigma_{l}
                \\
         + \frac{Q_k + (Q_{diff})_k}{C_p}
$$






     --- (13)

$$
  \hat{E}_k = E_{k} 
            + \sum_{k=1}^{K} W_{kl} ( T_{v,l}-T_{l} )
$$
    --- (14)

where the vector and matrix of the gravitational wave term (underlined) are

$$
  C_{k} = \Delta \sigma_{k}
$$
    --- (15)

$$
  W_{kl} = C_{p} \alpha_{l} \delta_{k \geq l}
         + C_{p} \beta_{l} \delta_{k-1 \geq l}
$$
    --- (16)

$$
  G_{k} = \hat{\kappa}_{k} C_{p} \bar{T}_{k}
$$
    --- (17)

$$
\underline{h} = \underline{Q}\underline{S} - \underline{R}
$$
    --- (18)

$$
  Q_{kl} = \frac{1}{\Delta \sigma_{k}} 
             ( \hat{\bar{T}}_{k-1/2} - \bar{T}_{k} ) \delta_{k=l} 
         + \frac{1}{\Delta \sigma_{k}} 
             ( \bar{T}_{k} - \hat{\bar{T}}_{k+1/2}  ) \delta_{k+1=l} 
$$
    --- (19)

$$
  S_{kl} = \sigma_{k-1/2} \Delta \sigma_{l} 
           - \Delta \sigma_{l} \delta_{k \leq l } 
$$
    --- (20)

$$
  R_{kl} = - \left(  \frac{ \alpha_{k} }{ \Delta \sigma_{k} } 
                     \Delta \sigma_{l} \delta_{k \leq l} 
                   + \frac{ \beta_{k} }{ \Delta \sigma_{k} } 
                     \Delta \sigma_{l} \delta_{k+1 \leq l}  
             \right) \bar{T}_{k} .
$$
     --- (21)

Here, for example, $\delta_{k \leq l}$ is
A function that is 1 if $ k \leq l$ is valid and 0 otherwise.

Using the following expression ,

$$
  \delta_{t} {X} \equiv \frac{1}{2 \Delta t} 
        \left( {X}^{t+\Delta t} - {X}^{t-\Delta t} \right)
$$
    --- (22)

$$
    \overline{X}^{t}
   \equiv  \frac{1}{2} \left( {X}^{t+\Delta t} 
                              + {X}^{t-\Delta t} \right)
         \\ 
   =  {X}^{t-\Delta t} + \delta_{t} {X} \Delta t   ,
$$

    --- (23)

If we apply the semi-implicit method to the system of equations,

$$
  \delta_{t} \pi =
          \left( \frac{\partial \pi}{\partial t} \right)_{NG}  
     - {TERM00050} \cdot \overline{ {TERM00051} }^{t}
$$
    --- (24)

$$
  \delta_{t} {TERM00052} =
          \left( \frac{\partial {TERM00053}}{\partial t} \right)_{NG}  
          - \nabla^{2}_{\sigma} ( {TERM00054}_{S} 
                                  + \underline{W} 
                                     \overline{ {TERM00055} }^{t}
                                  + {TERM00056}
                                  \overline{\pi}^{t} ) 
          - {\mathcal D}_M ( {TERM00057}^{t-\Delta t} 
                         + 2 \Delta t \delta_{t} {TERM00058} )
$$
     --- (25)

$$
  \delta_{t} {TERM00059} =
        \left( \frac{\partial {TERM00060}}{\partial t} \right)_{NG}  
         - \underline{h} \overline{ {TERM00061} }^{t} 
         - {\mathcal D}_H ( {TERM00062}^{t-\Delta t}
                        + 2 \Delta t \delta_{t} {TERM00063} )
$$
     --- (26)

So..,

$$
      \left\{ ( 1+2\Delta t {\mathcal D}_H )( 1+2\Delta t {\mathcal D}_M )
           \underline{I}  
      - ( \Delta t )^{2}  ( \underline{W} \ \underline{h} 
           + (1+2\Delta t {\mathcal D}_M)
             {TERM00064} {TERM00065}^{T} ) \nabla^{2}_{\sigma}
  \right\}
      \overline{ {TERM00066} }^{t} 
       \\
  = ( 1+2\Delta t {\mathcal D}_H )( 1+\Delta t {\mathcal D}_M ) 
       {TERM00067}^{t-\Delta t}
  + \Delta t 
     \left( \frac{\partial {TERM00068}}{\partial t} \right)_{NG}  
  \\
  -  \Delta t \nabla^{2}_{\sigma}     
                   \left\{  ( 1+2\Delta t {\mathcal D}_H ) {TERM00069}_{S} 
                          + \underline{W} 
                            \left[ ( 1-2\Delta t {\mathcal D}_H ) 
                                    {TERM00070}^{t-\Delta t}
                                  + \Delta t 
                                      \left( \frac{\partial {TERM00071}}
                                                  {\partial t}     
                                      \right)_{NG} \right]
                   \right.
  \\
                 \left.  \hspace*{20mm} 
                          + ( 1+2\Delta t {\mathcal D}_H ) {TERM00072} 
                            \left[ \pi^{t-\Delta t} 
                                  + \Delta t
                                     \left( \frac{\partial \pi}
                                                 {\partial t} 
                                     \right)_{NG}  \right]
                   \right\} . 
$$



    --- (27)

Since the spherical harmonic expansion is used,

and the above equation can be solved for $\overline{ {$\mathbf{D}$}_n^m }^{t}$.
And then..,

$$
   D^{t+\Delta t} = 2\overline{ {TERM00074} }^{t} - D^{t-\Delta t}
$$
     --- (28)

and, (24), (26)
The value in $t+\Delta t$ according to $\hat{X}^{t+\Delta t}$
is required.

### Time scheme properties and time step estimates

advectional equation

$$
  \frac{\partial{X}}{\partial {t}} = c \frac{\partial{X}}{\partial {x}}
$$
    --- (29)

Considering the stability of the discretization in the leap frog in
Now,

$$
  X = X_0 \exp(ikx)
$$


If we place the difference between

$$
  X^{n+1} = X^{n-1} + 2 i k \Delta t X^n
$$
    --- (30)

That would be.
Here,

$$
  \lambda = X^{n+1}/X^n = X^n/X^{n-1} 
$$


So,

$$
  \lambda^2 = 1 + 2 i kc \Delta t \lambda \; .
$$
     --- (31)

The solution is called $kc \Delta t = p$,

$$
 \lambda = -i p \pm \sqrt{1-p^2}
$$
    --- (32)

This absolute value is

$$
  |\lambda| = \left\{ 
             \begin{array}{ll}
               1                      |p| \le 1 \\
               p \pm \sqrt{p^2-1} \;\;    |p| > 1
             \end{array}
             \right.
$$
     --- (33)

and in the case of $|p|>1$, it is $|\lambda| > 1$,
It is a solution whose absolute value increases exponentially with time.
This indicates that the computation is unstable.

On the other hand, in the case of $|p| \le 1$, because it is $|\lambda| = 1$,
The calculation is neutral.
However, there are two solutions to the value of $\lambda$,
One of them is $\Delta t \rightarrow 1$, and the other is
This is $\lambda \rightarrow 1$, but ,
The other would be $\lambda \rightarrow -1$.
This indicates that the solution oscillates strongly in time.
This mode is called calculation mode,
One of the problems with the leap frog method.
This mode can be used by applying a time filter to the
It can be attenuated.

The terms of the $|p|=kc \Delta t \le 1$ are ,
Given the horizontal discretization lattice interval $\Delta x$, if
This will cause the maximum value of $k$ to be

$$
  \max k = \frac{\pi}{\Delta x}
$$


From becoming ,

$$
   \Delta t \le \frac{\Delta x}{\pi c}
$$
     --- (34)

That would be.
In the case of spectral models, the maximum wavenumber is determined by $N$,
Earth radius is set to $a$,

$$
   \Delta t \le \frac{a}{N c}  
$$
    --- (35)

This is a condition for stability.

To guarantee the stability of the integration,
As for $c$, it has the fastest advection and propagation speed,
You can use a smaller time step than $\Delta t$ determined by that.
When semi-implicit is not used, the propagation speed of gravity wave
($c \sim 300m/s$) is the criterion for stability, but ,
When semi-implicit is used, advection by the east-west wind is usually
Limiting factors.
Thus, $\Delta t$ assumes that $U_{max}$ is the maximum value of the east-west wind,

$$
   \Delta t \le \frac{a}{N U_{max}}  
$$
    --- (36)

Take to meet the .
In practice, this is multiplied by a safety factor.

### Handling of the Initiation of Time Integration

Not calculated by AGCM,
If you start with an appropriate initial value, you can use a model-consistent
You cannot give two physical quantities of time in $t$ and $t-\Delta t$.
However, if you give an inconsistent value for $t-\Delta t$
A large calculation mode occurs.

So, first, as $X^{\Delta t/4} = X^0$, in the time step of $1/4$

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


and then perform the calculation with leap frog as usual,
The occurrence of computation modes is reduced.
