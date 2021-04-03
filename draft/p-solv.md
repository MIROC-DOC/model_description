## Solving the diffuse balance equation for atmospheric and surface systems

**NOTE: the descriptions in this section are outdated.**

### Basic Solutions.

Some of the terms in the radiation, vertical diffusion, and boundary layer and surface processes are treated as implicit terms, and the time integration is performed at the end of the calculation. As the time-varying term for the vector quantity <span>q</span>, we divide it into two terms, ${\mathcal A}$ for the Euler method and ${\mathcal B}$ for the implicit method.

$$
  {\mathbf q}^+
      = {\mathbf q} + 2 \Delta t {\mathcal A}( {\mathbf q}   )
                           + 2 \Delta t {\mathcal B}( {\mathbf q}^+ ) \; .
$$

Although this is difficult to solve in the general case, it can be approximated by linearizing $B$.

$$
  {\mathcal B}( {\mathbf q}^+ )
                           \simeq {\mathcal B}( {\mathbf q} )
                            + B( {\mathbf q}^+ - {\mathbf q} )
$$

and linearize it using the matrix $B$ as where ,

$$
  B_{ij} = \frac{\partial{{\cal B}_i}}{\partial {q_j}}
$$

but if you write $\Delta {\mathbf q} \equiv {\mathbf q}^+ - {\mathbf q}$ Then write $\Delta {\mathbf q} \equiv {\mathbf q}^+ - {\mathbf q}$,

$$
  ( I - 2 \Delta t B ) \Delta {\mathbf q}
      = 2 \Delta t \left(  {\mathcal A}( {\mathbf q} )
                         + {\mathcal B}( {\mathbf q} ) \right) \; .
$$

It is easy to solve in principle by matrix operations.

### Fundamental Equations.

The equations for radiation, vertical diffusion, and ground boundary layer/surface processes are basically expressed as follows.

$$
     \frac{\partial{u}}{\partial {t}}   =   - g \frac{\partial{}}{\partial {p}} F_u \; , \\
     \frac{\partial{v}}{\partial {t}}   =   - g \frac{\partial{}}{\partial {p}} F_v \; , \\
 c_p \frac{\partial{T}}{\partial {t}}   =   - g \frac{\partial{}}{\partial {p}} ( F_T + F_R ) \; , \\
     \frac{\partial{q}}{\partial {t}}   =   - g \frac{\partial{}}{\partial {p}} F_q \; , \\
 C_g \frac{\partial{G}}{\partial {t}}   =   -   \frac{\partial{}}{\partial {z}} F_g \; .
$$

where $F_u, F_v, F_T, F_q$ are the vertical energy flux densities of the vertical diffusion fluxes of $u, v, c_p T, q$, respectively. $F_R$ is the vertical upward energy flux density of the vertical diffuse flux density of $u, v, c_p T, q$, respectively.

The atmosphere is discretized using the $\sigma=p/p_S$ coordinate system. Wind speed, temperature, etc. are defined by the layer $\sigma_k$. The flux is defined by the layer boundary $\sigma_{k-1/2}$. $k$ increases from the lower levels to the upper levels. Also, $\sigma_{1/2} = 1$ and $\sigma_{k} \simeq (\sigma_{k-1/2} + \sigma_{k+1/2})/2$ are defined in the upper levels. The $\sigma$ coordinates can be considered to be the same as those of $p$ except for the difference by a constant ($p_S$) factor, as long as we consider a one-dimensional vertical process. Here,

$$
  \Delta \sigma_{k} = \sigma_{k-1/2} - \sigma_{k+1/2} \; ,
$$

$$
  \Delta m_{k} = \frac{1}{g} \Delta p_k
   = \frac{p_S}{g} ( \sigma_{k-1/2} - \sigma_{k+1/2} )
$$

And write .

### implicit time difference

For terms that can be linearized, such as the vertical diffusion term, we use the implicit method. Although the diffusion coefficients depend on the forecast variables, we only obtain the coefficients first and do not solve them iteratively. However, in order to improve the stability of the method, the time step is treated differently (see below).

For example, the discretized equation of $u$ (178) is

$$
  (u_k^{m+1} - u_k^{m})/\Delta t
    = (Fu^{m+1}_{k-1/2}-Fu^{m+1}_{k+1/2})/\Delta m_k
$$

Here, $m$ is a time step. Since $Fu_{k-1/2}$ etc. is a function of $u_k$, we can linearize its dependence on

$$
   Fu^{m+1}_{k-1/2}
  =  Fu^{m}_{k-1/2}
  +  \sum_{k'=1}^{K}
     \frac{\partial{Fu^{m}_{k-1/2}}}{\partial {u_{k'}}} (u^{m+1}_{k'}-u^{m}_{k'})
$$

Thus, if you put $\delta u_k \equiv (u^{m+1}_{k}-u^{m}_{k})/\Delta t$,

$$
  \Delta m_k \delta u_k
  =   \left( Fu^{m}_{k-1/2}
         +  \sum_{k'=1}^{K}
            \frac{\partial{Fu^{m}_{k-1/2}}}{\partial {u_{k'}}} \Delta t \delta u_{k'}
         -   Fu^{m}_{k+1/2}
         -  \sum_{k'=1}^{K}
            \frac{\partial{Fu^{m}_{k+1/2}}}{\partial {u_{k'}}} \Delta t \delta u_{k'}
      \right)
$$

Namely,

$$
  \Delta m_k \delta u_k
  -  \sum_{k'=1}^{K} \left(  \frac{\partial{Fu^{m}_{k-1/2}}}{\partial {u_{k'}}}
                       - \frac{\partial{Fu^{m}_{k+1/2}}}{\partial {u_{k'}}} \right)
                 \Delta t\delta u_{k'}
  = Fu^{m}_{k-1/2} - Fu^{m}_{k+1/2}
$$

It can be written in the following matrix form

$$
  \sum_{k'=1}^{K} M^u_{k,k'} \delta u_k' = Fu^{m}_{k-1/2} - Fu^{m}_{k+1/2}
$$

$$
M^u_{k,k'} \equiv \Delta m_k \delta_{k,k'}
          -  \left(  \frac{\partial{Fu^{m}_{k-1/2}}}{\partial {u_{k'}}}
                   - \frac{\partial{Fu^{m}_{k+1/2}}}{\partial {u_{k'}}} \right) \Delta t
$$

This can be solved by methods such as LU decomposition. Since $M^u_{k,k'}$ is usually a triple diagonal, it can be solved easily. After solving the problem, the consistent fluxes are calculated using (534). The same is true for $v$.

### implicit time difference coupling

Temperature, specific humidity, and ground temperature are not as simple as those in the previous section.

$$
  c_p \Delta m_k \delta T_k
   -  \sum_{k'=0}^{K}
                 \left(  \frac{\partial{F\theta^{m}_{k-1/2}}}{\partial {T_{k'}}}
                       - \frac{\partial{F\theta^{m}_{k+1/2}}}{\partial {T_{k'}}} \right)
                 \Delta t\delta T_{k'}
  - \sum_{k'=0}^{K}
                 \left(  \frac{\partial{FR^{m}_{k-1/2}}}{\partial {T_{k'}}}
                       - \frac{\partial{FR^{m}_{k+1/2}}}{\partial {T_{k'}}} \right)
                 \Delta t\delta T_{k'}  \\
  =   ( F\theta^{m}_{k-1/2} - F\theta^{m}_{k+1/2} )
  + ( FR^{m}_{k-1/2} - FR^{m}_{k+1/2} )
$$

$$
  \Delta m_k \delta q_k
  -  \sum_{k'=0}^{K} \left(  \frac{\partial{Fq^{m}_{k-1/2}}}{\partial {q_{k'}}}
                            - \frac{\partial{Fq^{m}_{k+1/2}}}{\partial {q_{k'}}} \right)
                 \Delta t\delta q_{k'}
  = ( Fq^{m}_{k-1/2} - Fq^{m}_{k+1/2} )
$$

$$
  Cg_l \Delta z_l \delta G_l
  +  \sum_{l'=0}^{L} \left(  \frac{\partial{Fg^{m}_{l-1/2}}}{\partial {G_{l'}}}
                            - \frac{\partial{Fg^{m}_{l+1/2}}}{\partial {G_{l'}}} \right)
                 \Delta t\delta T_{k'}
  = - ( Fg^{m}_{l-1/2} - Fg^{m}_{l+1/2} )
$$

Note that $\sum_{k'}$ and $\sum_{l'}$ in the above equations are taken from $k'=0$ and $l'=0$. This is because the flux at the earth's surface is as follows.

$$
  F\theta_{1/2} =  c_p C_H |{\mathbf{v}}_{1/2}| (\theta_0 - \theta_1)
$$

$$
  Fq_{1/2} =  \beta C_E |{\mathbf{v}}_{1/2}| (q_0 - q_1)
$$

$$
  Fg_{1/2} =  K_g (G_1 - G_0)/z_1
$$

Assuming that the surface skin temperature is set to $T_0$, $\theta_0 = T_0$, $q_0 = q^*(T_0)$ (saturated specific humidity), and $G_0 = T_0$ are all dependent on $T_0$. All of these values depend on the $T_0$. Also, all of the values of $FR_{k}$ depend on the $T_0$.

As with (538), rewriting (539), (540) and (541) using the matrices $M^{\theta}, M^q, M^g$, in $k \ge 2$ (for $\theta, q$) or $l \ge 1$ (for $G$),

$$
    \sum_{k'=1}^{K}  M^\theta_{k,k'} \delta T_{k'}
        =  (F\theta^{m}_{k-1/2} - F\theta^{m}_{k+1/2})
        + (FR^{m}_{k-1/2} - FR^{m}_{k+1/2})   \\
 +  \left(\frac{\partial{FR^{m}_{k-1/2}}}{\partial {T_0}} - \frac{\partial{FR^{m}_{k+1/2}}}{\partial {T_0}} \right)
     \Delta t\delta T_0 \; ,
$$

$$
 \sum_{k'=1}^{K}  M^q_{k,k'} \delta q_{k'}
         = (Fq^{m}_{k-1/2} - Fq^{m}_{k+1/2}) \; ,
$$

$$
  \sum_{l'=0}^{L} M^g_{l,l'} \delta G_{l'}
         = - (Fg^{m}_{l-1/2} - Fg^{m}_{l+1/2}) \; .
$$

However,

$$
M^{\theta}_{k,k'} \equiv c_p \Delta m_k \delta_{k,k'}
          -  \left(  \frac{\partial{F\theta^{m}_{k-1/2}}}{\partial {T_{k'}}}
                   - \frac{\partial{F\theta^{m}_{k+1/2}}}{\partial {T_{k'}}} \right) \Delta t
          -  \left(  \frac{\partial{FR^{m}_{k-1/2}}}{\partial {T_{k'}}}
                   - \frac{\partial{FR^{m}_{k+1/2}}}{\partial {T_{k'}}} \right) \Delta t \; ,
$$

$$
M^{q}_{k,k'} \equiv \Delta m_k \delta_{k,k'}
          -  \left(  \frac{\partial{Fq^{m}_{k-1/2}}}{\partial {q_{k'}}}
                   - \frac{\partial{Fq^{m}_{k+1/2}}}{\partial {q_{k'}}} \right) \Delta t \; ,
$$

$$
M^{g}_{l,l'} \equiv Cg_l \Delta z_l \delta_{l,l'}
          -  \left(  \frac{\partial{Fg^{m}_{l-1/2}}}{\partial {G_{l'}}}
                   - \frac{\partial{Fg^{m}_{l+1/2}}}{\partial {G_{l'}}} \right) \Delta t \; .
$$

In case of $k=1$ (for $\theta, q$) or $l=0$ (for $G$),

$$
    \sum_{k'=1}^{K}  M^\theta_{1,k'} \delta T_{k'}
  +  \frac{\partial{F\theta^{m}_{1/2}}}{\partial {T_1}} \Delta t\delta T_1
        =  (F\theta^{m}_{1/2} - F\theta^{m}_{3/2})
        + (FR^{m}_{1/2} - FR^{m}_{3/2})   \\
 +   \frac{\partial{F\theta^{m}_{1/2}}}{\partial {T_0}} \Delta t\delta T_0
      \\
 +  \left(\frac{\partial{FR^{m}_{1/2}}}{\partial {T_0}} - \frac{\partial{FR^{m}_{3/2}}}{\partial {T_0}} \right)
     \Delta t\delta T_0 \; ,
$$

$$
 \sum_{k'=1}^{K}  M^q_{1,k'} \delta q_{k'}
         - \frac{\partial{Fq^{m}_{1/2}}}{\partial {q_1}} \Delta t\delta q_1
         = (Fq^{m}_{1/2} - Fq^{m}_{3/2})
         + \frac{\partial{Fq^{m}_{1/2}}}{\partial {T_0}} \Delta t\delta T_0 \; ,
$$

$$
  {\sum_{l'=1}^{L} M^g_{0,l'} \delta G_{l'}
           +  \left(    \frac{\partial{F\theta^{m}_{1/2}}}{\partial {T_0}}
           +  L \frac{\partial{Fq^{m}_{1/2}}}{\partial {T_0}}
           +    \frac{\partial{FR^{m}_{1/2}}}{\partial {T_0}}
           -  \frac{\partial{Fg^{m}_{1/2}}}{\partial {T_0}} \right) \Delta t\delta T_0  }
         \\
         =  - F\theta^{m} - L Fq^{m} - FR^{m} +  Fg^{m}_{1/2}  \\
         -    \frac{\partial{F\theta^{m}_{1/2}}}{\partial {T_1}} \Delta t\delta T_1
           -  L \frac{\partial{Fq^{m}_{1/2}}}{\partial {q_1}} \Delta t\delta q_1
           -    \frac{\partial{FR^{m}_{1/2}}}{\partial {T_1}} \Delta t\delta T_1
           +    \frac{\partial{Fg^{m}_{1/2}}}{\partial {G_1}} \Delta t\delta G_1
$$

However,

$$
M^{\theta}_{1,k'} \equiv c_p \Delta m_1 \delta_{1,k'}
          -  \left(
                   - \frac{\partial{F\theta^{m}_{3/2}}}{\partial {T_{k'}}} \right) \Delta t
          -  \left( \frac{\partial{FR^{m}_{1/2}}}{\partial {T_{k'}}}
                   - \frac{\partial{FR^{m}_{3/2}}}{\partial {T_{k'}}} \right) \Delta t \; ,
$$

$$
M^{q}_{1,k'} \equiv \Delta m_1 \delta_{1,k'}
          -  \left(
                   - \frac{\partial{Fq^{m}_{3/2}}}{\partial {q_{k'}}} \right) \Delta t \; ,
$$

$$
M^{g}_{0,l'} \equiv
             \left(
                   - \frac{\partial{Fg^{m}_{1/2}}}{\partial {G_{l'}}} \right) \Delta t \; .
$$

However, (553) is a condition for the balance of the ground surface

$$
   F\theta^{m+1} + L Fq^{m+1} + FR^{m+1} - Fg^{m+1} = 0
$$

Note that we have treated the case of $l=0$ in the soil temperature equation, which is not included in the table of (541).

Taking these, (545), (546), (547), (551), (552), and (553) together, we can solve the equations for the $2K+L+1$ unknowns since we have the same number of equations. In practice, the LU decomposition can be used to solve this problem.

After solving the problem, the consistent fluxes should be obtained as in (534).

### Solving the Coupling Formula for Time Difference

(551), etc., can be written as follows.

$$
  \sum_{k'=1}^{K} ( M_{k,k'} + \delta_{1,k} \delta_{1,k'} \alpha)
    = F_k + \delta_{1,k} ( F_s + \gamma T_0 )
$$

Here, the terms $F_s, \alpha, \gamma$ are associated with surface fluxes, and the other terms are associated with vertical diffusion. If we reverse the upside-down matrix, we get the following results.

$$
  \left( \begin{array}{lll} M_{KK}  \cdots  M_{K1} \\ \vdots
  \vdots \\ M_{1K}  \cdots  M_{11} + \alpha \\
\end{array}  \right)
\left( \begin{array}{l} T_K \\ \vdots \\ T_1 \\
\end{array}  \right)
= \left( \begin{array}{l} F_K \\ \vdots \\ F_1 + F_s + \gamma T_{0} \\
\end{array} \right)
$$

For the sake of brevity, we shall now refer to this document as $K=3$. The following discussion will not lose its generality.

$$
  \left( \begin{array}{lll} M_{33}  M_{32}  M_{31} \\ M_{23}
  M_{22}  M_{21} \\ M_{13}  M_{12}  M_{11} + \alpha \\
\end{array} \right)
\left( \begin{array}{l} T_3 \\ T_2 \\ T_1 \\
\end{array} \right)
= \left( \begin{array}{l} F_3 \\ F_2 \\ F_1 + F_s + \gamma T_{0} \\
\end{array} \right)
$$

Let us consider the equation for $F_s = 0, \alpha=0, \gamma=0$ (which corresponds to the case where flux exchange at the surface is not considered), which is solved by the LU decomposition.

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

for $f'$ (which can be easily solved by starting from $f'_3=F_3$), and then,

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

However, comparing this with (563), we see the following relationship.

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

The result is That is, ,

$$
  ( U_{11} +  \alpha  ) T_1 = f'_1 + F_s + \gamma T_0
$$

Note that $U_{k,k'}$ and $f'_k$ can be obtained by the LU decomposition with the equation (561) of $\alpha=\gamma=0$, i.e., without considering the surface flux term. The physical meaning of these terms is that in the flux exchange process with the ground surface, the entire atmosphere has a heat capacity $U_{11}$, and can be regarded as a layer whose flux $f'_1$ is supplied from above.

In (545) and (551), (546) and (552), (547) and (553), respectively, the equation corresponding to (569) is obtained, which is as follows.

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

Therefore, by concatenating the above three expressions, we can solve for the unknown variables $\delta T_1, \delta q_1, \delta T_0$. Once these are solved, we can then solve for (568) as $x_2,x_3$. After that, we can apply a consistent flux to the obtained temperatures and

$$
  F\theta_c  =  F\theta_{1/2}
                   + \gamma^{T} \delta T_0 -\alpha^{T} \delta T_1 \\
  Fq^P_c  =  Fq^P_{1/2}
                   + \gamma^{q} \delta T_0 -\alpha^{q} \delta q_1
$$

and compute it as Although we have shown that $M$ is a general matrix, it is simpler since it is actually a triple-diagonal matrix.

In the program, `MODULE:[VFTND1(pimtx.F)]` for the atmospheric part and `MODULE:[GNDHT1(pggnd.F)]` for the underground part, the first half of the LU decomposition method (where $f'_k$ is obtained) is performed, and in `MODULE:[ SLVSFC(pgslv.F)]`, the equation of $3\times 3$ is solved, and $\delta q_1, \delta G_1, \delta T_0$ are obtained. Then, in `MODULE:[GNDHT2(pggnd.F)]`, we perform the latter half of the LU decomposition method, solve for the temperature coefficient of variation for the ground, and correct the fluxes so that the convergence of the two equations agrees with each other. In `MODULE:[VFTND2(pimtx.F)]`, the temperature coefficient of variation is solved for the atmosphere, and the fluxes are corrected with `MODULE:[FLXCOR(pimtx.F)]`.

### Combined expression for time difference

The concatenation formula for $\delta T_1, \delta q_1, \delta T_0$ is solved three times with different conditions as follows.

Solve for surface wetness $\beta$ as 1. Surface temperature is a variable.

2. the solution is based on the surface moisture content obtained by `MODULE:[GNDBET]`. The surface temperature is a variable.

3. the solution is given by the surface moisture content obtained by `MODULE:[GNDBET]`. In the case of snow melting, etc., the surface temperature is fixed at the freezing point.

The first calculation is performed to estimate the possible evaporation rate ($Fq^P$). (When the surface wetness is small, diagnosing the possible evaporation rate as $\widetilde{Fq^P} = Fq / \beta$ using $Fq$ obtained from the model energy balance will result in an unrealistically large value.) The possible evaporation rate is defined as,

$$
  Fq^P_c = Fq^P_{1/2}
       + \frac{\partial{Fq^P_{1/2}}}{\partial {q_1}} \delta q_1 2 \Delta t
       + \frac{\partial{Fq^P_{1/2}}}{\partial {T_0}} \delta T_0 2 \Delta t
$$

It becomes The subscript $c$ means, after correction, that this is a consistent flux for the temperature etc. obtained.

In the second and subsequent calculations ,

The value of evaporation ($\beta$) multiplied by the value of possible evaporation determined in the first calculation is the value of evaporation ($Fq_1$).

$$
        Fq = \beta Fq^P
$$

2. evaporation rate $Fq_1$ is

$$
        \beta \rho C_E |{\mathbf{v}}| ( q_*(T_0) - q )
$$

The energy balance is again rebalanced as required by

There are two ways of calculating the evaporation rate, i.e., (1) and (2) (the standard method is used in this case). The third calculation is performed in order to fix the surface temperature at the freezing point, etc. during snow and ice melt or sea ice formation in the mixed layer oceans in order to solve the energy balance. The amount of energy used for the phase change of water is diagnostically determined and is used to calculate the amount of snowmelt later.

The concrete form of the coupling formula is as follows.

$$
  \renewcommand{\arraystretch}{1.5}
  \left( \begin{array}{ccc}
      U_{11}^T - \frac{\partial{F\theta_{1/2}}}{\partial {T_1}} 2 \Delta t
      0
      - \left( \frac{\partial{F\theta_{1/2}}}{\partial {T_0}}
                         + \frac{\partial{FR_{1/2}}}{\partial {T_0}}\right) 2 \Delta t \\
      0
      U_{11}^q - \beta \frac{\partial{Fq^P_{1/2}}}{\partial {q_1}} \Delta t
      - \beta \frac{\partial{Fq^P_{1/2}}}{\partial {T_0}} \Delta t \\
        \frac{\partial{F\theta_{1/2}}}{\partial {T_1}} \Delta t
      L \beta \frac{\partial{Fq_{1/2}}}{\partial {q_1}} \Delta t
      U_{00}^g + \left(\frac{\partial{F\theta_{1/2}}}{\partial {T_0}}
                + L \beta \frac{\partial{Fq_{1/2}}}{\partial {T_0}}
                + \frac{\partial{FR_{1/2}}}{\partial {T_0}} \right) 2 \Delta t \\
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

Here, $U_{11}^T, U_{11}^q, U_{00}^g$, and $f_1^T, f_1^q, f_0^g$ are components of the matrices and vectors obtained by the first half of the LU decomposition method. When the ground surface is covered with snow or ice, the sublimation latent heat $Ls = L + L_M$ is used instead of the latent heat $L$. $L_M$ is the latent heat of the melting of water. However, in the second calculation, if the first method is used to estimate evaporation, the result will be as follows.

$$
 \renewcommand{\arraystretch}{1.5}
  \left( \begin{array}{ccc}
      U_{11}^T - \frac{\partial{F\theta_{1/2}}}{\partial {T_1}} 2 \Delta t
      0
      - \left( \frac{\partial{F\theta_{1/2}}}{\partial {T_0}}
                         + \frac{\partial{FR_{1/2}}}{\partial {T_0}}\right) 2 \Delta t \\
      0
      U_{11}^q - \beta \frac{\partial{Fq^P_{1/2}}}{\partial {q_1}} \Delta t  \\
        \frac{\partial{F\theta_{1/2}}}{\partial {T_1}} \Delta t
      U_{00}^g + \left(\frac{\partial{F\theta_{1/2}}}{\partial {T_0}}
                + \frac{\partial{FR_{1/2}}}{\partial {T_0}} \right) 2 \Delta t \\
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
      U_{11}^T - \frac{\partial{F\theta_{1/2}}}{\partial {T_1}} 2 \Delta t
      0 \\
      0
      U_{11}^q - \frac{\partial{Fq_{1/2}}}{\partial {q_1}} 2 \Delta t \\
  \end{array} \right)
  \left( \begin{array}{l}
      \delta T_1 \\ \delta q_1 \\
  \end{array} \right)  \\
=
  \left( \begin{array}{l}
      f_1^T + + F\theta_{1/2}
      + \left( \frac{\partial{F\theta_{1/2}}}{\partial {T_0}}
                    + \frac{\partial{FR_{1/2}}}{\partial {T_0}} \right) \delta_0 T_0 2 \Delta t \\
      f_1^q +  \beta Fq^P_{1/2}
      + \frac{\partial{Fq_{1/2}}}{\partial {T_0}} \delta_0 T_0 2 \Delta t \\
  \end{array} \right) \; .
$$

Here, $\delta_0 T_0$ is the rate of change to the temperature to be fixed,

$$
   \delta_0 T_0 = ( T_0^{fix} - T_0 ) / \Delta t \; .
$$

The value of $T_0^{fix}$ is 273.15 K for snow and ice melt, and 271.15 K for sea ice formation. When the second method of evaporation calculation is used, $Fq^P_c$ is used instead of $Fq^P_{1/2}$, and the differential term of $F_q$ is set to zero. In this case, the differential term of $F_q$ is set to zero,

$$
\Delta s  =  f_0^g - F\theta_{1/2} - L \beta Fq^P_{1/2} - U_{00}^g
          -  \left(\frac{\partial{F\theta_{1/2}}}{\partial {T_0}}
                + L \beta \frac{\partial{Fq_{1/2}}}{\partial {T_0}}
                + \frac{\partial{FR_{1/2}}}{\partial {T_0}} \right) \delta_0 T_0 \Delta t
                 \\
          -  \frac{\partial{F\theta_{1/2}}}{\partial {T_1}} \delta T_1 \Delta t
                - L \beta \frac{\partial{Fq^P_{1/2}}}{\partial {q_1}} \delta q_1 \Delta t \; .
$$

$\Delta s$, which is calculated by $\Delta s$, is the surface energy balance and is the energy used for the water phase change.

### implicit Treatment of Time Steps in Time Differences

Although the implicit method is used for the time difference of the vertical diffusion term, the diffusion coefficients are generally nonlinear, and the explicit evaluation of these coefficients may lead to numerical instability problems. In order to improve the stability, we follow Kalnay and Kanamitsu (19?) in treating the time step as in Kalnay and Kanamitsu (19?). In order to improve the stability, we follow Kalnay and Kanamitsu (19?) in treating the time step.

For simplicity, we will take the following ordinary differential equations as an example.

$$
  \frac{\partial{X}}{\partial {t}} = - K(X) X
$$

The coefficient $K(X)$ expresses the nonlinearity. Evaluating only the coefficients explicitly and making them implicitly differential, we obtain the following equation.

$$
  \frac{X^{m+1} - X^m}{\Delta t} = - K( X^m ) X^{m+1}
$$

However, consider the value of $X$ two steps ahead, $X^{\ast}$,

$$
  \frac{X^{\ast} - X^m}{2\Delta t} = - K ( X^m ) X^{\ast}
$$

$$
  X^{m+1} = \frac{X^{\ast} + X^m}2
$$

and (586). In general, (585) and (586) are known to be more stable than (584).

By rewriting (585) and (586) into a form for determining the rate of change over time, we obtain the following.

$$
  \left(\frac{\Delta X}{\Delta t}\right)^{\ast} =
     - K( X^m ) \left( X^m +
        \left(\frac{\Delta X}{\Delta t}\right)^{\ast}
        2 \Delta t \right)
$$

$$
  X^{m+1} = X^m + \left(\frac{\Delta X}{\Delta t}\right)^{\ast} \Delta t
$$

In other words, the time step in determining the rate of change is twice the time integration step.
