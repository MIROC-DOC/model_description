## Surface Flux.

### Overview of the Surface Flux Scheme

The surface flux scheme is ,
due to turbulent transport in the ground boundary layer.
Assessing the flux of physical quantities between atmospheric surfaces.
The main input data are wind speed $u, v$, temperature $T$, and specific humidity $q$,
The output data are the vertical fluxes of momentum, heat, water vapor and
It is the differential value for obtaining an implicit solution.

Bulk coefficients are obtained according to Louis(1979), Louis <span>*et al.*</span>(1982).
However, we take into account the difference between the momentum and heat roughness in the correction.

The outline of the calculation procedure is as follows.

1. as the stability of the atmosphere.
     Richardson numbers.

2. calculate the bulk coefficient from Richardson number `MODULE:[PSFCL]`.

3. calculate the flux and its derivative from the bulk coefficient.

4. if necessary, using the required flux
 After taking into account the roughness effect of sea level, the effect of free convection, and wind speed correction,
 Do the math again.

### Basic Formula for Flux Calculations

Surface Flux $ Fu, Fv, F\theta, Fq$ are
Using the bulk coefficients $C_M, C_H, C_E$
It is expressed as follows.

$$
Fu  =  - \rho C_M |{$\mathbf{v}$}| u
$$


$$
Fv  =  - \rho C_M |{$\mathbf{v}$}| v
$$


$$
F\theta  = \rho c_p C_H |{$\mathbf{v}$}| ( \theta_g - \theta )
$$


$$
Fq^P =  \rho C_E |{$\mathbf{v}$}| ( q_g - q )
$$


However, the $Fq^P$ is the possible evaporation rate.
The calculation of actual evaporation is a combination of "surface processes" and
We will discuss this in the section "Solving Diffusion-Based Budget Equations for Atmospheric Surface Systems".

### Richardson Number.

The standard of stability between atmospheric surfaces,
Bulk Richardson Number $R_{iB}$ is

$$
R_{iB} = \frac{ \frac{g}{\theta_s} (\theta_1 - \theta(z_0))/z_1 }
              { (u_1/z_1)^2                                  }
       = \frac{g}{\theta_s} 
         \frac{T_1 (p_s/p_1)^\kappa - T_0 }{u_1^2/z_1} f_T .
$$


Here,

$$
f_T = (\theta_1 - \theta(z_0))/(\theta_1 - \theta_0)
$$


is a correction factor and is approximated from the uncorrected bulk Richardson number, while
Here, the calculation method is abbreviated.

### Bulk factor.

The bulk coefficients $C_M,C_H,C_E$ are
Louis(1979), Louis <span>*et al.*</span>(1982).
However, we take into account the difference between the momentum and heat roughness in the correction.
i.e., the roughness to momentum, heat, and water vapor.
$z_{0M}, z_{0H}, z_{0E}$ respectively
In general, the $z_{0M} > z_{0H}, z_{0E}$ are used, but heat and water vapor are also
Bulk factor for flux from the height of the $z_{0M}$
Find first the $\widetilde{C_H}$ and $\widetilde{C_E}$ and then correct them.

$$
C_M = \left\{ 
      \begin{array}{lr}
      C_{0M} [ 1 + (b_M/e_M) R_{iB} ]^{-e_M} 
          R_{iB} \geq 0 \\
      C_{0M} \left[ 1 - b_M R_{iB} \left( 1+ d_M b_M C_{0M}
                                  \sqrt{\frac{z_1}{z_{0M}}| R_{iB}|} \,
                                  \right)^{-1} \right]      
          R_{iB} < 0 \\
      \end{array} \right.
$$


$$
\widetilde{C_H} = \left\{ 
      \begin{array}{lr}
      \widetilde{C_{0H}} [ 1 + (b_H/e_H) R_{iB} ]^{-e_H} 
          R_{iB} \geq 0 \\
      \widetilde{C_{0H}} \left[ 1 - b_H R_{iB} 
                                  \left( 1+ d_H b_H \widetilde{C_{0H}}
                                  \sqrt{\frac{z_1}{z_{0M}}| R_{iB}|} \,
                                  \right)^{-1} \right]      
          R_{iB} < 0 \\
      \end{array} \right.
$$


$$
C_H = \widetilde{C_H} f_T 
$$


$$
\widetilde{C_E} = \left\{ 
      \begin{array}{lr}
      \widetilde{C_{0E}} [ 1 + (b_E/e_E) R_{iB} ]^{-e_E} 
          R_{iB} \geq 0 \\
      \widetilde{C_{0E}} \left[ 1 - b_E R_{iB} 
                                  \left( 1+ d_E b_E \widetilde{C_{0E}}
                                  \sqrt{\frac{z_1}{z_{0M}}| R_{iB}|} \,
                                  \right)^{-1} \right]      
          R_{iB} < 0 \\
      \end{array} \right.
$$


$$
C_E = \widetilde{C_E} f_q 
$$


$C_{0M}, \widetilde{C_{0H}}, \widetilde{C_{0E}}$ are
The bulk factor (for fluxes from $z_{0M}$) at neutral,

$$
C_{0M}  =  \widetilde{C_{0H}}  =  \widetilde{C_{0E}}  = 
       \frac{k^2}{\left[\ln \left(\frac{z_1}{z_{0M}}\right)\right]^2 } .
$$


Correction Factor $f_q$ is ,

$$
  f_q = (q_1 - q(z_0))/(q_1 - q^{\ast}(\theta_0))
$$


but the method of calculation is abbreviated.
The coefficients are $( b_M, d_M, e_M ) = ( 9.4, 7.4, 2.0 ), \;
( b_H, d_H, e_H ) = ( b_E, d_E, e_E ) = ( 9.4, 5.3, 2.0 )$.

The dependence of the bulk coefficient on the $Ri_B$ is illustrated in Fig,
Figure [p-sflx:cm\] (#p-sflx:cm), Figure [p-sflx:ch\] (#p-sflx:ch).

### Calculating Flux.

This will calculate the flux.

$$
\hat{F}u_{1/2}  =  - \rho_{1/2} C_M |{$\mathbf{v}$}_1| u_1
$$


$$
\hat{F}v_{1/2}  =  - \rho_{1/2} C_M |{$\mathbf{v}$}_1| v_1
$$


$$
\hat{F}\theta_{1/2}  = \rho_{1/2} c_p C_H |{$\mathbf{v}$}_1| 
                    \left( T_0 - \sigma_1^{-\kappa} T_1 \right)
$$


$$
\hat{F}q^P_{1/2}  =  \rho_{1/2} C_E |{$\mathbf{v}$}_1| 
                    \left( q^*(T_0) - q_1 \right)
$$


The differential term is as follows

$$
\frac{\partial{Fu_{1/2}}}{\partial {u_1}} = \frac{\partial{Fv_{1/2}}}{\partial {v_1}} 
= - \rho_{1/2} C_M |{$\mathbf{v}$}_1|
$$


$$
\frac{\partial{F\theta_{1/2}}}{\partial {T_1}} 
= - \rho_{1/2} c_p C_H |{$\mathbf{v}$}_1| \sigma_1^{-\kappa}
$$


$$
\frac{\partial{F\theta_{1/2}}}{\partial {T_0}} 
= \rho_{1/2} c_p C_H |{$\mathbf{v}$}_1|
$$


$$
\frac{\partial{Fq_{1/2}}}{\partial {q_1}} 
 =  - \beta \rho_{1/2} C_E |{$\mathbf{v}$}_1| 
$$


$$
\frac{\partial{Fq^P_{1/2}}}{\partial {T_0}} 
 =  \beta \rho_{1/2} C_E |{$\mathbf{v}$}_1| \left( \frac{d {q^*}}{d {T}} \right)_{1/2}
$$


Here, it's important to note,
$T_0$ is a quantity that is not required at this time.
Epidermal temperature is ,
Conditions for surface heat balance

$$
   F\theta(T_0,T_1) + L \beta Fq^P(T_0,q_1) + FR(T_0) - Fg(T_0,G_1) = 0
$$


Determined to meet.
At this point, for $T_0$, we use the one from the previous time step to evaluate.
The true flux value that meets the surface balance is ,
It is determined by solving this equation in conjunction with surface processes.
In that sense, I have added $\hat{{}}$ to the flux above.

### handling at sea level.

At sea level, we follow Miller et al. (1992) and consider the following two effects.

 - Free convection is preeminent when the wind speed is low

 - The roughness of the sea surface varies with the wind speed.

The effect of free convection is calculated using the buoyancy flux $F_B$,

$$
  F_B = F\theta/c_p + \epsilon T_0 F_q^P
$$


During the $F_B >0$,

$$
  w^* = ( H_{B} F_B )^{1/3}
$$


$$
  |{$\mathbf{v}$}_1| = \left( u_1^2 + v_1^2 + (w^*)^2 \right)^{1/2}
$$


to be considered by making $H_B$ corresponds to the thickness scale of the mixed layer.
The current standard value is $H_B=2000$ m.

The roughness variation of the sea surface is represented by the friction velocity ($u^*$)

$$
  u^* = \left( \sqrt{Fu^2 + Fv^2}/\rho \right)^{1/2}
$$


with ,

$$
  Z_{0M}  =  A_M + B_M (u^*)^2/g + C_M \nu/u^* \\
  Z_{0H}  =  A_H + B_H (u^*)^2/g + C_H \nu/u^* \\
  Z_{0E}  =  A_E + B_E (u^*)^2/g + C_E \nu/u^* 
$$




Evaluate as follows. $\nu=1.5\times10^{-5}$ m$^2$ s$^{-1}$ is
It is the kinematic viscosity of the atmosphere,
The standard values for the other coefficients are
$(A_M, B_M, C_M) = (0, 0.018, 0.11) $,
$(A_H, B_H, C_H) = (1.4\times10^{-5}, 0, 0.4) $,
$(A_E, B_E, C_E) = (1.3\times10^{-4}, 0, 0.62) $.

For the above calculations, $Fu, Fv, F\theta, Fq$ are required,
Perform successive approximation calculations.

### Wind Speed Correction

In general, the roughness of the ground surface is greater on large surfaces than on small surfaces.
The downward transport of momentum is so efficient that the wind just above it is weak,
The difference in wind speed cancels out the difference in roughness in $C_D$.

In the model, the wind speed passed to the surface flux calculation is
It is a value calculated by time integration of the mechanical processes,
The values are smoothed by spectral expansion.
This is the reason why the surface of the ground with widely different roughnesses, such as sea level and land level, is
In an area that is mixed on a small scale ,
I can't describe this compensation effect well.
Therefore, once the momentum flux is calculated and
The wind speed in the lowest layer of the atmosphere is corrected for by it, and then
Recalculate the momentum, heat, and water fluxes again.

### Minimum wind speed.

Consider the effects of small-scale exercise,
Surface wind speed in the calculation of surface flux
Set the minimum value of $|{$\mathbf{v}$}_1|$.
The current standard values are the same for all fluxes and
It is 3 m/s.
