## Time integration.

The time difference scheme is essentially a leap frog.
However, the diffusion terms and physical process terms are backward or forward differences.
A time filter (Asselin, 1972) is used to suppress the computational mode.
In order to increase the value of $\Delta t$, we use a time filter (Asselin, 1972),
Applying the semi-implicit method to the gravitational wave term (Bourke, 1988).

### Time integration and time filtering by leap frog

We use leap frog as a time integration scheme for advection terms and so on.
The backward difference of $2 \Delta t$ is used for the horizontal diffusion term.
The pseudo $p$ surface correction of the diffusion term and the frictional heat by horizontal diffusion term are combined with
treated as a correction and becomes a forward difference in $2 \Delta t$.
The physical process terms (${\mathcal F}_\lambda, {\mathcal F}_\varphi, Q, S_q$) are treated as
We still use the forward difference of $2 \Delta t$.
(However, for the calculation of the time-varying term of vertical diffusion, we treat it as a backward difference.
Please refer to the chapter on physical processes for details.)

Representing each of the forecast variables as ${X}$, we obtain

$$
  \hat{X}^{t+\Delta t} 
    =  \bar{X}^{t-\Delta t}
    + 2 \Delta t 
      \dot{X}_{adv}\left( {X}^{t} \right)
    + 2 \Delta t 
      \dot{X}_{dif}\left( \hat{X}^{t+\Delta t} \right)
$$


$ \dot{X}_{adv} $ is an advection term etc,
$ \dot{X}_{dif} $ is a horizontal diffusion term.

In $ \hat{X}^{t+\Delta t} $, there is a horizontal diffusion term,
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


To remove the calculation mode in leap frog
The time filter of Asselin (1972) is applied at every step.
I.e. ,

$$
  \bar{X}^{t}
    = ( 1-2 \epsilon_f ) {X}^{t}
    +  \epsilon_f 
        \left( \bar{X}^{t-\Delta t} + {X}^{t+\Delta t} \right)
$$


and $\bar{X}$.
Normally 0.05 is used as the $\epsilon_f$.

### semi-implicit time integration

For mechanics calculations, the leap frog is basically used,
We treat some terms as implicit.
Here, the implicit considers the trapezoidal implicit.
For the vector quantity ${\mathbf q}$,
The value in $t$ is converted to ${\mathbf q}$,
The value in $t+\Delta t$ was converted to ${\mathbf q}^+$,
If you write the value of $t-\Delta t$ as ${\mathbf q}^-$,
What is trapezoidal implicit?
$({\mathbf q}^+ +  {\mathbf q}^- )/2$.
We use the time-varying terms evaluated by using
Now, as a time-varying term in <span>q</span>,
The term A is treated in the leap forg method and the term B is treated in the trapezoidal implicit method.
Assume that A is nonlinear with respect to <span>q</span>, while B is linear.
In other words,

$$
  {\mathbf q}^+ 
      = {\mathbf q}^- 
      + 2 \Delta t {\mathcal A}( {\mathbf q}  )
      + 2 \Delta t B (   {\mathbf q}^+ 
                       + {\mathbf q}^-   )/2
$$


where $B$ is a square matrix. Then,
$\Delta {\mathbf q} \equiv {\mathbf q}^+ - {\mathbf q}$
And then you can write,

$$
  ( I - \Delta t B ) \Delta {\mathbf q} 
      = 2 \Delta t \left( {\mathcal A}({\mathbf q})
                         + B {\mathbf q} \right) 
$$


This can be easily solved by matrix operations.

### semi-implicit time integration applied

Then, we apply this method and treat the term of linear gravity waves as implicit.
This allows us to reduce the time step ($\Delta t$).

In the system of equations, the basic field is such that $T=\bar{T}_k$
Separation of the linear gravity wave term and the other terms (with the index $NG$).
Vertical Vector Representation
Using $\mathbf{D}=\{ D_{k} \}$, $\mathbf{T}=\{ T_{k} \}$,

$$
   \frac{\partial \pi}{\partial t} = 
          \left( \frac{\partial \pi}{\partial t} \right)_{NG}  
     - \mathbf{C} \cdot \mathbf{D}  ,
$$


$$
  \frac{\partial \mathbf{D}}{\partial t} = 
          \left( \frac{\partial \mathbf{D}}{\partial t} \right)_{NG}  
          - \nabla^{2}_{\sigma} ( \mathbf{\Phi}_{S} 
                                  + \underline{W} \mathbf{T}
                                  + \mathbf{G} \pi )  
          - {\mathcal D}_M \mathbf{D} ,
$$


$$
  \frac{\partial \mathbf{T}}{\partial t} 
      =   \left( \frac{\partial \mathbf{T}}
                        {\partial t}       \right)_{NG}  
         - \underline{h} \mathbf{D}
         - {\mathcal D}_H \mathbf{T} ,
$$


where the non-gravitational wave term is,

$$
  \left( \frac{\partial \pi}{\partial t} \right)^{NG}
   =   - \sum_{k=1}^{K} \mathbf{v}_{k} \cdot \nabla \pi  
       \Delta  \sigma_{k}  \\
   =   Z_{k}
$$

> <span id="Section Z" label="Section Z" label="Section Z" label=">\\\\\.} </span>

$$
  \dot{\sigma}^{NG}_{k-1/2}
 = - \sigma_{k-1/2} \left( \frac{\partial \pi}{\partial t} \right)^{NG}
   - \sum_{l=k}^{K} \mathbf{v}_{l} \cdot \nabla \pi
       \Delta  \sigma_{l}
$$


$$
  \left( \frac{\partial D}{\partial t} \right)^{NG}
       =   \frac{1}{a\cos\varphi}
            \frac{\partial (A_u)_{k}}{\partial \lambda}
          + \frac{1}{a\cos\varphi}
            \frac{\partial }{\partial \varphi} (A_v \cos\varphi)_k
          - \nabla^{2}_{\sigma} \hat{E}_{k} 
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
         + \hat{\kappa}_{k} T_{v,k} \mathbf{v}_{k} \cdot \nabla \pi
                \\
         - \frac{\alpha_{k}}{\Delta \sigma_{k} } T_{v,k}
             \sum_{l=k}^{K} \mathbf{v}_{l} \cdot \nabla \pi 
               \Delta \sigma_{l}
           - \frac{\beta_{k}}{\Delta \sigma_{k} } T_{v,k}
             \sum_{l=k+1}^{K} \mathbf{v}_{l} \cdot \nabla \pi 
               \Delta \sigma_{l}
                \\
         - \frac{\alpha_{k}}{\Delta \sigma_{k} } T'_{v,k}
             \sum_{l=k}^{K} D_l  \Delta \sigma_{l}
           - \frac{\beta_{k}}{\Delta \sigma_{k} } T'_{v,k}
             \sum_{l=k+1}^{K} D_l  \Delta \sigma_{l}
                \\
         + \frac{Q_k + (Q_{diff})_k}{C_p}
$$
  
  
  
  
  
  


$$
  \hat{E}_k = E_{k} 
            + \sum_{k=1}^{K} W_{kl} ( T_{v,l}-T_{l} )
$$


where the vector and matrix of the gravitational wave terms (underlined) are,

$$
  C_{k} = \Delta \sigma_{k}
$$

> <span id="Coefficient C" label="Coefficient C">\\c\[Coefficient C]</span>

$$
  W_{kl} = C_{p} \alpha_{l} \delta_{k \geq l}
         + C_{p} \beta_{l} \delta_{k-1 \geq l}
$$


$$
  G_{k} = \hat{\kappa}_{k} C_{p} \bar{T}_{k}
$$


$$
\underline{h} = \underline{Q}\underline{S} - \underline{R}
$$


$$
  Q_{kl} = \frac{1}{\Delta \sigma_{k}} 
             ( \hat{\bar{T}}_{k-1/2} - \bar{T}_{k} ) \delta_{k=l} 
         + \frac{1}{\Delta \sigma_{k}} 
             ( \bar{T}_{k} - \hat{\bar{T}}_{k+1/2}  ) \delta_{k+1=l} 
$$


$$
  S_{kl} = \sigma_{k-1/2} \Delta \sigma_{l} 
           - \Delta \sigma_{l} \delta_{k \leq l } 
$$


$$
  R_{kl} = - \left(  \frac{ \alpha_{k} }{ \Delta \sigma_{k} } 
                     \Delta \sigma_{l} \delta_{k \leq l} 
                   + \frac{ \beta_{k} }{ \Delta \sigma_{k} } 
                     \Delta \sigma_{l} \delta_{k+1 \leq l}  
             \right) \bar{T}_{k} .
$$

> <span id="Coefficient R" label="Coefficient R">\R\[Coefficient R]</span>.

Here, for example, $\delta_{k \leq l}$ is the same as
It is a function that is 1 if $ k \leq l$ is true and 0 otherwise.

Using the following expression,

$$
  \delta_{t} {X} \equiv \frac{1}{2 \Delta t} 
        \left( {X}^{t+\Delta t} - {X}^{t-\Delta t} \right)
$$

> <span id="Shemiinp" label="Shemiinp">\\centric="Shemiinp\centric"> </span>.

$$
    \overline{X}^{t}
   \equiv  \frac{1}{2} \left( {X}^{t+\Delta t} 
                              + {X}^{t-\Delta t} \right)
         \\ 
   =  {X}^{t-\Delta t} + \delta_{t} {X} \Delta t   ,
$$
  


Applying the semi-implicit method to a system of equations,

$$
  \delta_{t} \pi =
          \left( \frac{\partial \pi}{\partial t} \right)_{NG}  
     - \mathbf{C} \cdot \overline{ \mathbf{D} }^{t}
$$

> <span id="semi-imp pi" label="semi-imp pi" label="semi-imp pi">\[semi-imp pi]</span>

$$
  \delta_{t} \mathbf{D} =
          \left( \frac{\partial \mathbf{D}}{\partial t} \right)_{NG}  
          - \nabla^{2}_{\sigma} ( \mathbf{\Phi}_{S} 
                                  + \underline{W} 
                                     \overline{ \mathbf{T} }^{t}
                                  + \mathbf{G}
                                  \overline{\pi}^{t} ) 
          - {\mathcal D}_M ( \mathbf{D}^{t-\Delta t} 
                         + 2 \Delta t \delta_{t} \mathbf{D} )
$$

> <span id="semi-imp D" label="semi-imp D" label="semi-imp D">\[semi-imp D\\[semi-imp D\]</span>

$$
  \delta_{t} \mathbf{T} =
        \left( \frac{\partial \mathbf{T}}{\partial t} \right)_{NG}  
         - \underline{h} \overline{ \mathbf{D} }^{t} 
         - {\mathcal D}_H ( \mathbf{T}^{t-\Delta t}
                        + 2 \Delta t \delta_{t} \mathbf{T} )
$$

> <span id="semi-imp T" label="semi-imp T" label="semi-imp T">\[semi-imp T]</span>

So..,

> <span id="semi-imp barD" label="semi-imp barD" label="semi-imp barD">\\brachos[semi-imp barD\brachos]</span>
$$
      \left\{ ( 1+2\Delta t {\mathcal D}_H )( 1+2\Delta t {\mathcal D}_M )
           \underline{I}  
      - ( \Delta t )^{2}  ( \underline{W} \ \underline{h} 
           + (1+2\Delta t {\mathcal D}_M)
             \mathbf{G} \mathbf{C}^{T} ) \nabla^{2}_{\sigma}
  \right\}
      \overline{ \mathbf{D} }^{t} 
       \\
  = ( 1+2\Delta t {\mathcal D}_H )( 1+\Delta t {\mathcal D}_M ) 
       \mathbf{D}^{t-\Delta t}
  + \Delta t 
     \left( \frac{\partial \mathbf{D}}{\partial t} \right)_{NG}  
  \\
  -  \Delta t \nabla^{2}_{\sigma}     
                   \left\{  ( 1+2\Delta t {\mathcal D}_H ) \mathbf{\Phi}_{S} 
                          + \underline{W} 
                            \left[ ( 1-2\Delta t {\mathcal D}_H ) 
                                    \mathbf{T}^{t-\Delta t}
                                  + \Delta t 
                                      \left( \frac{\partial \mathbf{T}}
                                                  {\partial t}     
                                      \right)_{NG} \right]
                   \right.
  \\
                 \left.  \hspace*{20mm} 
                          + ( 1+2\Delta t {\mathcal D}_H ) \mathbf{G} 
                            \left[ \pi^{t-\Delta t} 
                                  + \Delta t
                                     \left( \frac{\partial \pi}
                                                 {\partial t} 
                                     \right)_{NG}  \right]
                   \right\} . 
$$
  
  
  


Since we use the spherical harmonic expansion, we can use it,

and the above formula can be solved for $\overline{ \mathbf{D}_n^m }^{t}$.
After that,

$$
   D^{t+\Delta t} = 2\overline{ \mathbf{D} }^{t} - D^{t-\Delta t}
$$


and ([semi-imp pi\]](#semi-imp%20pi), ([semi-imp T\\](#semi-imp%20T))
The value in $t+\Delta t$ according to $\hat{X}^{t+\Delta t}$
is required .

### Time scheme properties and time step estimates

advectional equation

$$
  \frac{\partial X}{\partial t} = c \frac{\partial X}{\partial x}
$$


Consider the stability of the leap frog discretization in
Now,

If we place the difference between

$$
  X^{n+1} = X^{n-1} + 2 i k \Delta t X^n
$$


where
Here ,
\\lambda = X^{n+1}/X^n = X^n/X^{n-1}}\\\\bars}]
So,

$$
  \lambda^2 = 1 + 2 i kc \Delta t \lambda \; .
$$


The solution is labeled $kc \Delta t = p$,

$$
 \lambda = -i p \pm \sqrt{1-p^2}
$$


This absolute value is

$$
  |\lambda| = \left\{ 
             \begin{array}{ll}
               1                      |p| \le 1 \\
               p \pm \sqrt{p^2-1} \;\;    |p| > 1
             \end{array}
             \right.
$$


In the case of $|p|>1$, it would be $|\lambda| > 1$,
The solution becomes exponentially larger in absolute value with time.
This indicates that the computation is unstable.

On the other hand, in the case of $|p| \le 1$, the value is $|\lambda| = 1$,
The calculation is neutral.
However, there are two solutions for $\lambda$,
One of them, when $\Delta t \rightarrow 1$ is set to
This is a $\lambda \rightarrow 1$, but..,
The other is $\lambda \rightarrow -1$.
This indicates a time-varying solution.
This mode is called "calculation mode",
One of the problems with the leap frog method.
This mode can be applied by applying a time filter to the
It can be attenuated.

The terms of the $|p|=kc \Delta t \le 1$ are,
Given the horizontal discretization grid spacing $\Delta x$, the
This will cause the maximum value of $k$ to be
\More than one person can be in a position to do so.
From becoming ,

$$
   \Delta t \le \frac{\Delta x}{\pi c}
$$


In the case of the spectral model, the maximum wavenumber of
For the spectral model, the maximum wavenumber is determined by $N$,
Earth radius is set to $a$,

$$
   \Delta t \le \frac{a}{N c}  
$$


This is the stability condition.

To guarantee the stability of the integral,
As for $c$, it has the fastest advection and propagation speed,
You may use a time step smaller than $\Delta t$ which is determined by the semi-implicit method.
If semi-implicit is not used, the propagation speed of the gravitational wave
($c \sim 300m/s$) is the criterion for stability,
When semi-implicit is used, advection by the east-west wind is usually
This is a limiting factor.
Therefore, the $\Delta t$ sets $U_{max}$ as the maximum value of the east-west wind,

$$
   \Delta t \le \frac{a}{N U_{max}}  
$$


In practice, this is multiplied by a safety factor.
In practice, this should be multiplied by a safety factor.

### Treatment at the beginning of time integration.

Not calculated by AGCM,
If you start with an appropriate initial value, you can use a model-consistent
You cannot give the physical quantities for two times of $t$ and $t-\Delta t$.
However, if you give an inconsistent value for $t-\Delta t$, then you should not give an inconsistent value for $t-\Delta t$,
A large calculation mode is generated.

So, first, as $X^{\Delta t/4} = X^0$, in the time step of $1/4$
\{X^{{X}^{D\Delta t/2} = X^0 + X^0 + {{X}^{D\Delta t/2}
                 = X^0 + t/2 \\Dentro{X}^0\0}]
and furthermore, in the time step of $1/2$,
\\\\lopen}t = X^{X}^{X}^^{X}^{\Delta t/2}}\lopen}t = X^0 + \lopen}t\lopen}t\lopen}t/2\lopen}t
And, in the original time step,
\\\\ltraLabella t} = X^{2\Delta t} = X^0 + 2\labella t\labella t\labella t}^{X}^{\labella t}]
and then perform the calculation with leap frog as usual,
The occurrence of computation modes is reduced.

