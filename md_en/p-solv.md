## Solving the diffuse balance equation for atmospheric and surface systems

### Basic Solutions.

Radiative, vertical diffusion, ground boundary layer and surface processes are
Some terms are treated as implicit in the
Compute the time-varying term and do time integration at the end.
As a time-varying term for the vector quantity <span>q</span>,
The term ${\mathcal A}$ for the Euler method and the term ${\mathcal B}$ for the implicit method are considered separately.

$$
  {\mathbf q}^+ 
      = {\mathbf q} + 2 \Delta t {\mathcal A}( {\mathbf q}   )
                           + 2 \Delta t {\mathcal B}( {\mathbf q}^+ ) \; . 
$$


It is difficult to solve this in the general case, but,
It can be solved by linearizing $B$ in an approximate manner.

$$
  {\mathcal B}( {\mathbf q}^+ ) 
                           \simeq {\mathcal B}( {\mathbf q} ) 
                            + B( {\mathbf q}^+ - {\mathbf q} )
$$


using the matrix $B$ as
Here,

$$
  B_{ij} = \frac{\partial {\mathcal B}_i}{\partial q_j}
$$


It is.
So..,
$\Delta {\mathbf q} \equiv {\mathbf q}^+ - {\mathbf q}$
And then you can write,

$$
  ( I - 2 \Delta t B ) \Delta {\mathbf q} 
      = 2 \Delta t \left(  {\mathcal A}( {\mathbf q} )
                         + {\mathcal B}( {\mathbf q} ) \right) \; . 
$$


It is easy to solve in principle by matrix operations.

### Fundamental Equations.

Radiation, vertical diffusion, ground boundary layer and surface processes
The equations are basically expressed as follows.

$$
     \frac{\partial u}{\partial t}   =   - g \frac{\partial }{\partial p} F_u \; , \\
     \frac{\partial v}{\partial t}   =   - g \frac{\partial }{\partial p} F_v \; , \\
 c_p \frac{\partial T}{\partial t}   =   - g \frac{\partial }{\partial p} ( F_T + F_R ) \; , \\
     \frac{\partial q}{\partial t}   =   - g \frac{\partial }{\partial p} F_q \; , \\
 C_g \frac{\partial G}{\partial t}   =   -   \frac{\partial }{\partial z} F_g \; .
$$






where $F_u, F_v, F_T, F_q$ are
By vertical diffusion, $u, v, c_p T, q$, respectively
is the vertical upward flux density of
Also, the $F_R$ is a radiant
It is a vertical upward energy flux density.

The atmosphere is discretized in the $\sigma=p/p_S$ coordinate system.
Wind speed, temperature, etc. are defined in layer $\sigma_k$.
The flux is defined by the layer boundary $\sigma_{k-1/2}$.
$k$ increases from lower to higher levels.
Also, $\sigma_{1/2} = 1$,
This is the $\sigma_{k} \simeq (\sigma_{k-1/2} + \sigma_{k+1/2})/2$.
$\sigma$ The coordinates are only available when we consider a one-dimensional vertical process,
It can be considered to be the same as $p$ coordinates except for the difference in the constant ($p_S$) times.
Here,

$$
  \Delta \sigma_{k} = \sigma_{k-1/2} - \sigma_{k+1/2} \; , 
$$


$$
  \Delta m_{k} = \frac{1}{g} \Delta p_k  
   = \frac{p_S}{g} ( \sigma_{k-1/2} - \sigma_{k+1/2} )
$$


And write .

### implicit time difference

For terms that can be linearized, such as the vertical diffusion term, we use the implicit method.
Diffusion coefficients and other factors also depend on the forecast variables,
The coefficients are only calculated first, not iteratively.
However, the treatment of the time step is devised to improve the stability (see below).

For example, the discretized equation of $u$ ([\[u-eq.orig]](#u-eq.orig)) is

$$
  (u_k^{m+1} - u_k^{m})/\Delta t 
    = (Fu^{m+1}_{k-1/2}-Fu^{m+1}_{k+1/2})/\Delta m_k
$$


Here, $m$ is a time step.
Since $Fu_{k-1/2}$ etc. is a function of $u_k$, its dependency is linearized and the

$$
   Fu^{m+1}_{k-1/2} 
  =  Fu^{m}_{k-1/2} 
  +  \sum_{k'=1}^{K} 
     \frac{\partial Fu^{m}_{k-1/2}}{\partial u_{k'}} (u^{m+1}_{k'}-u^{m}_{k'})
$$

> <span id="u-flux.next" label="u-flux.next" label="u-flux.next">\\\[u-flux.next\]</span>

Thus, if you put $\delta u_k \equiv (u^{m+1}_{k}-u^{m}_{k})/\Delta t$,

$$
  \Delta m_k \delta u_k
  =   \left( Fu^{m}_{k-1/2}
         +  \sum_{k'=1}^{K} 
            \frac{\partial Fu^{m}_{k-1/2}}{\partial u_{k'}} \Delta t \delta u_{k'}
         -   Fu^{m}_{k+1/2}
         -  \sum_{k'=1}^{K}
            \frac{\partial Fu^{m}_{k+1/2}}{\partial u_{k'}} \Delta t \delta u_{k'}
      \right) 
$$


Namely,

$$
  \Delta m_k \delta u_k
  -  \sum_{k'=1}^{K} \left(  \frac{\partial Fu^{m}_{k-1/2}}{\partial u_{k'}} 
                       - \frac{\partial Fu^{m}_{k+1/2}}{\partial u_{k'}} \right)
                 \Delta t\delta u_{k'}
  = Fu^{m}_{k-1/2} - Fu^{m}_{k+1/2}
$$


It can be written in the following matrix form

$$
  \sum_{k'=1}^{K} M^u_{k,k'} \delta u_k' = Fu^{m}_{k-1/2} - Fu^{m}_{k+1/2}
$$


$$
M^u_{k,k'} \equiv \Delta m_k \delta_{k,k'}
          -  \left(  \frac{\partial Fu^{m}_{k-1/2}}{\partial u_{k'}} 
                   - \frac{\partial Fu^{m}_{k+1/2}}{\partial u_{k'}} \right) \Delta t
$$

> <span id="u-matrix" label="u-matrix">\blazer[u-matrix]</span>

This can be solved by LU decomposition or some other method.
Normally, $M^u_{k,k'}$ is easy to solve since it is a triple diagonal.
After solving it, ([[u-flux.next\]](#u-flux.next)), you can use
We calculate the consistent flux to this method.
The same is true for $v$.

### implicit time difference coupling

Temperature, specific humidity, and ground temperature are not as simple as those in the previous section.

$$
  c_p \Delta m_k \delta T_k
   -  \sum_{k'=0}^{K}
                 \left(  \frac{\partial F\theta^{m}_{k-1/2}}{\partial T_{k'}} 
                       - \frac{\partial F\theta^{m}_{k+1/2}}{\partial T_{k'}} \right)
                 \Delta t\delta T_{k'}
  - \sum_{k'=0}^{K}
                 \left(  \frac{\partial FR^{m}_{k-1/2}}{\partial T_{k'}} 
                       - \frac{\partial FR^{m}_{k+1/2}}{\partial T_{k'}} \right)
                 \Delta t\delta T_{k'}  \\
  =   ( F\theta^{m}_{k-1/2} - F\theta^{m}_{k+1/2} )
  + ( FR^{m}_{k-1/2} - FR^{m}_{k+1/2} )
$$

> <span id="deq-theta" label="deq-theta">\[deq-theta]</span>


$$
  \Delta m_k \delta q_k
  -  \sum_{k'=0}^{K} \left(  \frac{\partial Fq^{m}_{k-1/2}}{\partial q_{k'}} 
                            - \frac{\partial Fq^{m}_{k+1/2}}{\partial q_{k'}} \right)
                 \Delta t\delta q_{k'}
  = ( Fq^{m}_{k-1/2} - Fq^{m}_{k+1/2} )
$$

> <span id="deq-q" label="deq-q">\blazer[deq-q]</span>

$$
  Cg_l \Delta z_l \delta G_l
  +  \sum_{l'=0}^{L} \left(  \frac{\partial Fg^{m}_{l-1/2}}{\partial G_{l'}} 
                            - \frac{\partial Fg^{m}_{l+1/2}}{\partial G_{l'}} \right)
                 \Delta t\delta T_{k'}
  = - ( Fg^{m}_{l-1/2} - Fg^{m}_{l+1/2} )
$$

> <span id="deq-g" label="deq-g">\blazer[deq-g]</span>

Here, $\sum_{k'}$ and $\sum_{l'}$ in the above equations are
Note that I took this from $k'=0$, $l'=0$. because,
This is because the flux at the surface is as follows

$$
  F\theta_{1/2} =  c_p C_H |\mathbf{v}_{1/2}| (\theta_0 - \theta_1)
$$


$$
  Fq_{1/2} =  \beta C_E |\mathbf{v}_{1/2}| (q_0 - q_1)
$$


$$
  Fg_{1/2} =  K_g (G_1 - G_0)/z_1
$$


Where the surface skin temperature is set to $T_0$,
$\theta_0 = T_0$, $q_0 = q^*(T_0)$ (saturated specific humidity), $G_0 = T_0$.
They all depend on the $T_0$.
Also, the value of the $FR_{k}$ depends on the $T_0$ for all $k$ values.

(as with [\[u-matrix]](#u-matrix)), using the matrices $M^{\theta}, M^q, M^g$
([deq-theta\] (#deq-theta)), ([deq-q\] (#deq-q)), ([deq-g\\] (#deq-g)), and ([deq-g\\] (#deq-g)) are rewritten,
For $k \ge 2$ (for $\theta, q$) or $l \ge 1$ (for $G$),

$$
    \sum_{k'=1}^{K}  M^\theta_{k,k'} \delta T_{k'}
        =  (F\theta^{m}_{k-1/2} - F\theta^{m}_{k+1/2}) 
        + (FR^{m}_{k-1/2} - FR^{m}_{k+1/2})   \\
 +  \left(\frac{\partial FR^{m}_{k-1/2}}{\partial T_0} - \frac{\partial FR^{m}_{k+1/2}}{\partial T_0} \right)
     \Delta t\delta T_0 \; ,
$$

> <span id="combo-theta2" label="combo-theta2">\\[combo-theta2\\blazer]</span>


$$
 \sum_{k'=1}^{K}  M^q_{k,k'} \delta q_{k'}
         = (Fq^{m}_{k-1/2} - Fq^{m}_{k+1/2}) \; ,
$$

> <span id="combo-q2" label="combo-q2">\blazer[combo-q2]</span>

$$
  \sum_{l'=0}^{L} M^g_{l,l'} \delta G_{l'}
         = - (Fg^{m}_{l-1/2} - Fg^{m}_{l+1/2}) \; .
$$

> <span id="combo-g2" label="combo-g2">\blazer[combo-g2]</span>

However,

$$
M^{\theta}_{k,k'} \equiv c_p \Delta m_k \delta_{k,k'}
          -  \left(  \frac{\partial F\theta^{m}_{k-1/2}}{\partial T_{k'}} 
                   - \frac{\partial F\theta^{m}_{k+1/2}}{\partial T_{k'}} \right) \Delta t
          -  \left(  \frac{\partial FR^{m}_{k-1/2}}{\partial T_{k'}} 
                   - \frac{\partial FR^{m}_{k+1/2}}{\partial T_{k'}} \right) \Delta t \; , 
$$


$$
M^{q}_{k,k'} \equiv \Delta m_k \delta_{k,k'}
          -  \left(  \frac{\partial Fq^{m}_{k-1/2}}{\partial q_{k'}} 
                   - \frac{\partial Fq^{m}_{k+1/2}}{\partial q_{k'}} \right) \Delta t \; ,
$$


$$
M^{g}_{l,l'} \equiv Cg_l \Delta z_l \delta_{l,l'}
          -  \left(  \frac{\partial Fg^{m}_{l-1/2}}{\partial G_{l'}} 
                   - \frac{\partial Fg^{m}_{l+1/2}}{\partial G_{l'}} \right) \Delta t \; .
$$


In case of $k=1$ (for $\theta, q$) or $l=0$ (for $G$),

$$
    \sum_{k'=1}^{K}  M^\theta_{1,k'} \delta T_{k'}
  +  \frac{\partial F\theta^{m}_{1/2}}{\partial T_1} \Delta t\delta T_1
        =  (F\theta^{m}_{1/2} - F\theta^{m}_{3/2}) 
        + (FR^{m}_{1/2} - FR^{m}_{3/2})   \\
 +   \frac{\partial F\theta^{m}_{1/2}}{\partial T_0} \Delta t\delta T_0 
      \\
 +  \left(\frac{\partial FR^{m}_{1/2}}{\partial T_0} - \frac{\partial FR^{m}_{3/2}}{\partial T_0} \right)
     \Delta t\delta T_0 \; ,
$$


> <span id="comb-theta" label="comb-theta" label="comb-theta">\centric[comb-theta]</span>


$$
 \sum_{k'=1}^{K}  M^q_{1,k'} \delta q_{k'}
         - \frac{\partial Fq^{m}_{1/2}}{\partial q_1} \Delta t\delta q_1
         = (Fq^{m}_{1/2} - Fq^{m}_{3/2}) 
         + \frac{\partial Fq^{m}_{1/2}}{\partial T_0} \Delta t\delta T_0 \; ,
$$

> <span id="combo-q" label="combo-q">\\centric\centric\centric\centric\centric\centric\centric\centric\centric\centric\centric\centric\centric\centric\centric\centric\centric\centric\centric\centric\centric\centric\centric\centric\centric\centric\centric\centric\centric\centric\fadabraz</c>.

$$
  {\sum_{l'=1}^{L} M^g_{0,l'} \delta G_{l'}
           +  \left(    \frac{\partial F\theta^{m}_{1/2}}{\partial T_0}
           +  L \frac{\partial Fq^{m}_{1/2}}{\partial T_0} 
           +    \frac{\partial FR^{m}_{1/2}}{\partial T_0}
           -  \frac{\partial Fg^{m}_{1/2}}{\partial T_0} \right) \Delta t\delta T_0  }
         \\
         =  - F\theta^{m} - L Fq^{m} - FR^{m} +  Fg^{m}_{1/2}  \\
         -    \frac{\partial F\theta^{m}_{1/2}}{\partial T_1} \Delta t\delta T_1
           -  L \frac{\partial Fq^{m}_{1/2}}{\partial q_1} \Delta t\delta q_1
           -    \frac{\partial FR^{m}_{1/2}}{\partial T_1} \Delta t\delta T_1
           +    \frac{\partial Fg^{m}_{1/2}}{\partial G_1} \Delta t\delta G_1  
$$


> <span id="combo-g" label="combo-g">\cleaner[combo-g]</span>


However,

$$
M^{\theta}_{1,k'} \equiv c_p \Delta m_1 \delta_{1,k'}
          -  \left(
                   - \frac{\partial F\theta^{m}_{3/2}}{\partial T_{k'}} \right) \Delta t
          -  \left( \frac{\partial FR^{m}_{1/2}}{\partial T_{k'}} 
                   - \frac{\partial FR^{m}_{3/2}}{\partial T_{k'}} \right) \Delta t \; , 
$$


$$
M^{q}_{1,k'} \equiv \Delta m_1 \delta_{1,k'}
          -  \left(
                   - \frac{\partial Fq^{m}_{3/2}}{\partial q_{k'}} \right) \Delta t \; ,
$$


$$
M^{g}_{0,l'} \equiv
             \left(
                   - \frac{\partial Fg^{m}_{1/2}}{\partial G_{l'}} \right) \Delta t \; .
$$


However, ([comb-g]](#comb-g)), the balance condition of the ground surface

$$
   F\theta^{m+1} + L Fq^{m+1} + FR^{m+1} - Fg^{m+1} = 0
$$


as the case of $l=0$ in the soil temperature equation,
(Note that it is not included in the formula of [deq-g](#deq-g)].

These,
([comb-theta2\] (#comb-theta2)), ([comb-q2\] (#comb-q2)), ([comb-g2\] (#comb-g2)),
([comb-theta\](#comb-theta)), ([comb-q](#comb-q)), ([comb-g\\lopen[comb-g\]](#comb-g))
for the $2K+L+1$ unknowns,
There are equations of equality that can be solved.
In practice, the LU decomposition can be used to solve the problem.

Once you're untied,
([u-flux.next]](#u-flux.next)) as well as ,
Consistent flux should be sought.

### Solving the Coupling Formula for Time Difference

([comb-theta]](#comb-theta)), etc., can be written as follows.

$$
  \sum_{k'=1}^{K} ( M_{k,k'} + \delta_{1,k} \delta_{1,k'} \alpha)
    = F_k + \delta_{1,k} ( F_s + \gamma T_0 )
$$


Where, $F_s, \alpha, \gamma$
The term in Section 3.1 is a term associated with surface flux,
The others are terms associated with vertical diffusion.
Here, if we reverse the top and bottom and represent it as a matrix, we get the following.

$$
  \left( \begin{array}{lll} M_{KK}  \cdots  M_{K1} \\ \vdots  
  \vdots \\ M_{1K}  \cdots  M_{11} + \alpha \\
\end{array}  \right)
\left( \begin{array}{l} T_K \\ \vdots \\ T_1 \\
\end{array}  \right)
= \left( \begin{array}{l} F_K \\ \vdots \\ F_1 + F_s + \gamma T_{0} \\
\end{array} \right)
$$


For the sake of brevity, we shall now refer to this document as $K=3$. For the sake of notation simplicity, we will now refer to it as $K=3$.
You can't lose the.

$$
  \left( \begin{array}{lll} M_{33}  M_{32}  M_{31} \\ M_{23} 
  M_{22}  M_{21} \\ M_{13}  M_{12}  M_{11} + \alpha \\
\end{array} \right)
\left( \begin{array}{l} T_3 \\ T_2 \\ T_1 \\
\end{array} \right)
= \left( \begin{array}{l} F_3 \\ F_2 \\ F_1 + F_s + \gamma T_{0} \\
\end{array} \right)
$$


Here,
The expression for $F_s = 0, \alpha=0, \gamma=0$,
(This corresponds to the case where flux replacement at the surface is not considered.)
by LU decomposition.

$$
  \left( \begin{array}{lll} M_{33}  M_{32}  M_{31} \\ M_{23} 
  M_{22}  M_{21} \\ M_{13}  M_{12}  M_{11} \\
         \end{array} \right)
  \left( \begin{array}{l}
         T'_3 \\ T'_2 \\ T'_1 \\
         \end{array} \right)
  = 
  \left(  \begin{array}{l}
          F_3 \\ F_2 \\ F_1 \\
          \end{array} \right)
$$

> <span id="summe-0" label="summe-0">\blazer[summe-0]</span>

LU. Take it apart,

$$
  \left( \begin{array}{lll}
         1       0       0      \\
         L_{23}  1       0      \\
         L_{13}  L_{12}  1      \\
         \end{array} \right)
  \left( \begin{array}{lll}
         U_{33}  U_{32}  U_{31} \\
         0       U_{22}  U_{21} \\
         0       0       U_{11} \\
         \end{array} \right)
  \left( \begin{array}{l}
         T'_3 \\ T'_2 \\ T'_1 \\
         \end{array} \right)
  = 
  \left(  \begin{array}{l}
          F_3 \\ F_2 \\ F_1 \\
          \end{array} \right)
$$


Now..,

$$
  \left( \begin{array}{lll}
         1       0       0      \\
         L_{23}  1       0      \\
         L_{13}  L_{12}  1      \\
         \end{array} \right)
  \left( \begin{array}{l}
         f'_3 \\ f'_2 \\ f'_1 \\
         \end{array} \right)
  = 
  \left(  \begin{array}{l}
          F_3 \\ F_2 \\ F_1 \\
          \end{array} \right)
$$

> <span id="solve-z" label="solve-z">\blazer[solve-z]</span>

for $f'$ (which can be easily solved by starting from $f'_3=F_3$),
And then..,

$$
  \left( \begin{array}{lll}
         U_{33}  U_{32}  U_{31} \\
         0       U_{22}  U_{21} \\
         0       0       U_{11} \\
         \end{array} \right)
  \left( \begin{array}{l}
         T'_3 \\ T'_2 \\ T'_1 \\
         \end{array} \right)
  = 
  \left(  \begin{array}{l}
          f'_3 \\ f'_2 \\ f'_1 \\
          \end{array} \right)
$$


for $f'$, starting from $x'_1=z'_1/U_{11}$, and solving in sequence.

For $\alpha \neq 0, \gamma \neq 0$, the LU decomposition is

$$
  \left( \begin{array}{lll}
         1       0       0      \\
         L_{23}  1       0      \\
         L_{13}  L_{12}  1      \\
         \end{array} \right)
  \left( \begin{array}{lll}
         U_{33}  U_{32}  U_{31} \\
         0       U_{22}  U_{21} \\
         0       0       U_{11}+\alpha \\
         \end{array} \right)
  \left( \begin{array}{l}
         T_3 \\ T_2 \\ T_1 \\
         \end{array} \right)
  = 
  \left(  \begin{array}{l}
          F_3 \\ F_2 \\ F_1 + F_s + \gamma T_0 \\
          \end{array} \right)
$$


Now..,

$$
  \left( \begin{array}{lll}
         1       0       0      \\
         L_{23}  1       0      \\
         L_{13}  L_{12}  1      \\
         \end{array} \right)
  \left( \begin{array}{l}
         f_3 \\ f_2 \\ f_1 \\
         \end{array} \right)
  = 
  \left(  \begin{array}{l}
          F_3 \\ F_2 \\ F_1 + F_s + \gamma T_0 \\
          \end{array} \right)
$$


However, comparing this with ([\ltra[solve-z]](#solve-z)), we see the following relationship.

$$
  \left( \begin{array}{l}
         f_3 \\ f_2 \\ f_1 \\
         \end{array} \right)
 = 
  \left( \begin{array}{l}
         f'_3 \\ f'_2 \\ f'_1 + F_s + \gamma T_0 \\
         \end{array} \right)
$$


With this,

$$
  \left( \begin{array}{lll}
         U_{33}  U_{32}  U_{31} \\
         0       U_{22}  U_{21} \\
         0       0       U_{11} + \alpha \\
         \end{array} \right)
  \left( \begin{array}{l}
         T_3 \\ T_2 \\ T_1 \\
         \end{array} \right)
  = 
  \left(  \begin{array}{l}
          f'_3 \\ f'_2 \\ f'_1 + F_s + \gamma x_0 \\
          \end{array} \right)
$$

> <span id="solve-x" label="solve-x">\blazer[solve-x]</span>

The result is That is, ,

$$
  ( U_{11} +  \alpha  ) T_1 = f'_1 + F_s + \gamma T_0 
$$

> <span id="solve-1" label="solve-1">\blazer[solve-1\blazer]</span>

where, $U_{k,k'}$ and, $f'_k$ are,

In other words, without considering the surface flux term
Note that this can be obtained by performing LU decomposition.
The physical meaning of these terms is ,
During the flux exchange process with the ground surface,
The entire atmosphere has a heat capacity of $U_{11}$,
Flux ($f'_1$) from the top
Indicates that it can be regarded as one layer to be supplied.

([comb-theta2]](#comb-theta2)) and ([comb-theta\]](#comb-theta)),
([combo-q2\](#comb-q2)) and ([combo-q\\\\clean}](#comb-q)),
([comb-g2\](#comb-g2)) and ([comb-g](#comb-g))
(the formula corresponding to [\ltra[solve-1\]](#solve-1)) is obtained and is as follows

$$
  ( U^{T}_{11} +  \alpha^{T}  ) \delta T_1 - \gamma^{T} \delta T_0 
      = f^{T}_1 + F\theta_{1/2}
$$


$$
  ( U^{q}_{11} +  \alpha^{q}  ) \delta q_1 - \gamma^{q} \delta T_0
      = f^{q}_1 + Fq^P_{1/2}
$$


$$
  ( U^{g}_{00} +  \alpha^{g}  ) \delta T_0 - \gamma^{g1} \delta T_1
                                           - \gamma^{g2} \delta q_1
      = f^{g}_0 - F\theta_{1/2} - L Fq_{1/2}
$$


Therefore, if we concatenate the three equations above, we get
We can solve for the unknown variables $\delta T_1, \delta q_1, \delta T_0$.
If we can solve these problems, we can then
([\[solve-x]](#solve-x)) can be solved sequentially as $x_2,x_3$.
Afterwards, the consistuous flux is applied to the obtained temperature

$$
  F\theta_c  =  F\theta_{1/2} 
                   + \gamma^{T} \delta T_0 -\alpha^{T} \delta T_1 \\
  Fq^P_c  =  Fq^P_{1/2} 
                   + \gamma^{q} \delta T_0 -\alpha^{q} \delta q_1
$$



Calculate as.
Here, we show the case where $M$ is a general matrix,
It is even simpler since it is actually a triple diagonal matrix.

During the program,
For atmospheric parts in `MODULE:[VFTND1(pimtx.F)]`,
MODULE:[GNDHT1(pggnd.F)]` for the underground part, the first half of the LU decomposition method.
(where $f'_k$ is obtained),
In `MODULE:[SLVSFC(pgslv.F)]`, solve the equation of $3\times 3$,
Seeking $\delta q_1, \delta G_1, \delta T_0$.
Then, in `MODULE:[GNDHT2(pggnd.F)]`
The second half of the LU decomposition method is performed and the rate of change of temperature in the ground is solved,
Correct the fluxes so that the balance is matched.
Also, in `MODULE:[VFTND2(pimtx.F)]`, for the atmosphere
Solving the rate of temperature change,
Fluxes are corrected with `MODULE:[FLXCOR(pimtx.F)]`.

### Combined expression for time difference

The coupling formula for finding $\delta T_1, \delta q_1, \delta T_0$ is ,
Solve three times under different conditions as follows.

Solve for surface wetness $\beta$ as 1. Surface temperature is a variable.

2. the surface wetness obtained by `MODULE:[GNDBET]`.
 Surface temperature is a variable .

3. the surface wetness obtained by `MODULE:[GNDBET]`.
 In case of snowmelt, the surface temperature is fixed at the freezing point.

The first calculation is performed to estimate the possible evaporation rate, $Fq^P$.
(When the surface wetness is small, the energy balance of the model indicates that
Using the obtained $Fq$, the possible evaporation rate can be calculated by
$\widetilde{Fq^P} = Fq / \beta$
diagnosed as, would result in unrealistically large values).
Possible evaporation rate is ,

$$
  Fq^P_c = Fq^P_{1/2}
       + \frac{\partial Fq^P_{1/2}}{\partial q_1} \delta q_1 2 \Delta t 
       + \frac{\partial Fq^P_{1/2}}{\partial T_0} \delta T_0 2 \Delta t 
$$


That would be.
The subscript $c$ means after correction,
This is a consistent flux to the obtained temperature etc.

In the second and subsequent calculations ,

1. to the amount of possible evaporation found in the first calculation
 Surface wetness (evaporation efficiency) $\beta$
 multiplied by the amount of evaporation $Fq_1$.

$$
        Fq = \beta Fq^P
$$


2. evaporation quantity $Fq_1$ is

$$
        \beta \rho C_E |\mathbf{v}| ( q_*(T_0) - q )
$$


 As required by ,
 Once again, rebalancing the energy.

Two methods of calculating the amount of evaporation can be used
(The standard uses the method in 1.).
The third calculation is performed during snow and ice melt and sea ice formation in the mixed layer ocean.
This is done in order to fix the surface temperature at the freezing point, for example, to unbalance the energy.
In this case, the amount of energy used for the phase change of water, such as snowmelt, is diagnostically determined,
It will be used later to calculate the amount of snow melt, etc.

The concrete form of the coupling formula is as follows.

$$
  \renewcommand{\arraystretch}{1.5}
  \left( \begin{array}{ccc}
      U_{11}^T - \frac{\partial F\theta_{1/2}}{\partial T_1} 2 \Delta t 
      0 
      - \left( \frac{\partial F\theta_{1/2}}{\partial T_0} 
                         + \frac{\partial FR_{1/2}}{\partial T_0}\right) 2 \Delta t \\
      0 
      U_{11}^q - \beta \frac{\partial Fq^P_{1/2}}{\partial q_1} \Delta t 
      - \beta \frac{\partial Fq^P_{1/2}}{\partial T_0} \Delta t \\
        \frac{\partial F\theta_{1/2}}{\partial T_1} \Delta t 
      L \beta \frac{\partial Fq_{1/2}}{\partial q_1} \Delta t 
      U_{00}^g + \left(\frac{\partial F\theta_{1/2}}{\partial T_0}
                + L \beta \frac{\partial Fq_{1/2}}{\partial T_0}
                + \frac{\partial FR_{1/2}}{\partial T_0} \right) 2 \Delta t \\
  \end{array} \right)
  \left( \begin{array}{l}
      \delta T_1 \\ \delta q_1 \\ \delta T_0 \\
  \end{array} \right)   \\
=  \left( \begin{array}{l}
      f_1^T + F\theta_{1/2} \\  
      f_1^q + \beta Fq^P_{1/2} \\  
      f_0^g - F\theta_{1/2} - L \beta Fq^P_{1/2} \\  
  \end{array} \right) \; .
$$

> <span id="combin-eq" label="combin-eq">\\brain[combin-eq]</span>


Here, $U_{11}^T, U_{11}^q, U_{00}^g$, $U_{11}^T, U_{11}^q, U_{00}^g$ and $f_1^T, f_1^q, f_0^g$, $f_1^T, f_1^q, f_0^g$ are,
The components of the matrices and vectors obtained by doing the first half of the LU decomposition method.
When the ground is covered with snow or ice, instead of the latent heat $L$
Using the Latent Heat of Sublimation $Ls = L + L_M$ $L_M$ is the latent heat of melting of water.
However, in the second calculation,
If the first method is used as an estimate of evaporation, we get the following.

$$
 \renewcommand{\arraystretch}{1.5}
  \left( \begin{array}{ccc}
      U_{11}^T - \frac{\partial F\theta_{1/2}}{\partial T_1} 2 \Delta t 
      0 
      - \left( \frac{\partial F\theta_{1/2}}{\partial T_0} 
                         + \frac{\partial FR_{1/2}}{\partial T_0}\right) 2 \Delta t \\
      0 
      U_{11}^q - \beta \frac{\partial Fq^P_{1/2}}{\partial q_1} \Delta t  \\
        \frac{\partial F\theta_{1/2}}{\partial T_1} \Delta t  
      U_{00}^g + \left(\frac{\partial F\theta_{1/2}}{\partial T_0}
                + \frac{\partial FR_{1/2}}{\partial T_0} \right) 2 \Delta t \\
  \end{array} \right)
  \left( \begin{array}{l}
      \delta T_1 \\ \delta q_1 \\ \delta T_0 \\
  \end{array} \right)   \\
=
  \left( \begin{array}{l}
      f_1^T + F\theta_{1/2} \\  
      f_1^q + \beta Fq^P_c \\  
      f_0^g - F\theta_{1/2} - L \beta Fq^P0_c \\  
  \end{array} \right) \; .
$$



In the third calculation, the concatenation equation for a fixed surface temperature is

$$
 \renewcommand{\arraystretch}{1.5}
  \left( \begin{array}{cc}
      U_{11}^T - \frac{\partial F\theta_{1/2}}{\partial T_1} 2 \Delta t 
      0 \\
      0 
      U_{11}^q - \frac{\partial Fq_{1/2}}{\partial q_1} 2 \Delta t \\
  \end{array} \right)
  \left( \begin{array}{l}
      \delta T_1 \\ \delta q_1 \\
  \end{array} \right)  \\
=
  \left( \begin{array}{l}
      f_1^T + + F\theta_{1/2}
      + \left( \frac{\partial F\theta_{1/2}}{\partial T_0} 
                    + \frac{\partial FR_{1/2}}{\partial T_0} \right) \delta_0 T_0 2 \Delta t \\
      f_1^q +  \beta Fq^P_{1/2} 
      + \frac{\partial Fq_{1/2}}{\partial T_0} \delta_0 T_0 2 \Delta t \\
  \end{array} \right) \; .
$$

> <span id="combin-eq3" label="combin-eq3">\brain[combin-eq3]</span>


Here, $\delta_0 T_0$ is the rate of change to the temperature to be fixed,

$$
   \delta_0 T_0 = ( T_0^{fix} - T_0 ) / \Delta t \; .
$$


$T_0^{fix}$ is 273.15K for snow and ice melting,
In the case of sea ice production it is 271.15K.
If the second method of evaporation calculation is used, then
Similarly, use $Fq^P_c$ instead of $Fq^P_{1/2}$,
Calculate the differential term of $F_q$ as 0.
In this case,

$$
\Delta s  =  f_0^g - F\theta_{1/2} - L \beta Fq^P_{1/2} - U_{00}^g
          -  \left(\frac{\partial F\theta_{1/2}}{\partial T_0}
                + L \beta \frac{\partial Fq_{1/2}}{\partial T_0}
                + \frac{\partial FR_{1/2}}{\partial T_0} \right) \delta_0 T_0 \Delta t 
                 \\
          -  \frac{\partial F\theta_{1/2}}{\partial T_1} \delta T_1 \Delta t
                - L \beta \frac{\partial Fq^P_{1/2}}{\partial q_1} \delta q_1 \Delta t \; .
$$



$\Delta s$, calculated by the Surface Energy Balance,
It is the amount of energy used for the phase change of water.

### implicit Treatment of Time Steps in Time Differences

Although the implicit method is used for the time difference of the vertical diffusion term,
In general, the diffusion coefficients are nonlinear, and we explicitly evaluate these coefficients
This can cause problems of numerical instability.
To improve stability, Kalnay and Kanamitsu (19?) following the
I'm working on how to handle the time steps.

For simplicity, we will take the following ordinary differential equations as an example.

$$
  \frac{\partial X}{\partial t} = - K(X) X
$$


The coefficient $K(X)$ represents the nonlinearity.
If we evaluate only the coefficients explicitly and make them implicitly different, we get the following equation.

$$
  \frac{X^{m+1} - X^m}{\Delta t} = - K( X^m ) X^{m+1}
$$

> <span id="normal-fd" label="normal-fd">\centric[normal-fd]</span>

However, consider the value of $X$ two steps ahead, $X^{\ast}$,

$$
  \frac{X^{\ast} - X^m}{2\Delta t} = - K ( X^m ) X^{\ast}
$$

> <span id="modify-fd1" label="modify-fd1">\[modify-fd1\\blade]</span>

$$
  X^{m+1} = \frac{X^{\ast} + X^m}2
$$

> <span id="modify-fd2" label="modify-fd2">\[modify-fd2\Backlash]</span>

.
Generally, ([modify-fd1\]](#modify-fd1)), ([modify-fd2\](#modify-fd2)) is better
([normal-fd]](#normal-fd)) is known to be more stable than [normal-fd]).

([modifie-fd1\](#modifie-fd1)), ([modifie-fd2\lenses](#modifie-fd2)) to find the rate of change in time
Rewriting it into a form yields the following.

$$
  \left(\frac{\Delta X}{\Delta t}\right)^{\ast} = 
     - K( X^m ) \left( X^m + 
        \left(\frac{\Delta X}{\Delta t}\right)^{\ast} 
        2 \Delta t \right)
$$


$$
  X^{m+1} = X^m + \left(\frac{\Delta X}{\Delta t}\right)^{\ast} \Delta t
$$


That is, the time step in determining the rate of change of the rate of change of time includes the following,
Using twice the time integration step.

