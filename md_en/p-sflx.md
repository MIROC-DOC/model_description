## Surface Flux.

### Overview of the Surface Flux Scheme

The surface flux scheme evaluates the physical quantity fluxes between the atmospheric surfaces due to turbulent transport in the boundary layer. The main input data are wind speed ($u, v$), temperature ($u, v$), temperature ($T$), and specific humidity ($q$), and the output data are the vertical fluxes of momentum, heat, and water vapor as well as the differential values for obtaining implicit solutions.

The bulk coefficients are obtained according to Louis(1979) and Louis <span>*et al.*</span>(1982), except for the correction for the difference in roughness between momentum and heat. However, corrections are made to take into account the difference between momentum and heat roughness.

The outline of the calculation procedure is as follows.

Calculate the Richardson number as the stability of the atmosphere.

2. calculate the bulk coefficient from Richardson number `MODULE:[PSFCL]`.

3. calculate the flux and its derivative from the bulk coefficient.

If necessary, the calculated fluxes are re-calculated after taking into account the roughness effect, the free flow effect, and the wind speed correction.

### Basic Formula for Flux Calculations

Surface fluxes ($ Fu, Fv, F\theta, Fq$) are expressed using the bulk coefficients ($C_M, C_H, C_E$) as follows

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


Note that $Fq^P$ is the possible evaporation rate. The calculation of actual evaporation is described in the sections "Surface processes" and "Solution of diffuse-type balance equations for atmospheric surface systems".

### Richardson Number.

The bulk Richardson number ($R_{iB}$), which is used as a benchmark for the stability between the atmospheric surfaces, is

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


is a correction factor, which is approximated from the uncorrected bulk Richardson number, but we abbreviate the calculation here.

### Bulk factor.

The bulk coefficients of $C_M,C_H,C_E$ are calculated according to Louis (1979) and Louis <span>*et al.*</span> (1982). However, corrections are made to take into account the difference between momentum and heat roughness. If the roughnesses for momentum, heat, and water vapor are set to $z_{0M}, z_{0H}, z_{0E}$, respectively, the results are generally $z_{0M} > z_{0H}, z_{0E}$, but the bulk coefficients for heat and water vapor for the fluxes from the height of $z_{0M}$ are also set to $\widetilde{C_H}$, $\widetilde{C_E}$ first, and then corrected.

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


$C_{0M}, \widetilde{C_{0H}}, \widetilde{C_{0E}}$ is the bulk coefficient (for fluxes from $z_{0M}$) at neutral,

$$
C_{0M}  =  \widetilde{C_{0H}}  =  \widetilde{C_{0E}}  = 
       \frac{k^2}{\left[\ln \left(\frac{z_1}{z_{0M}}\right)\right]^2 } .
$$


Correction Factor $f_q$ is ,

$$
  f_q = (q_1 - q(z_0))/(q_1 - q^{\ast}(\theta_0))
$$


but the method of calculation is omitted. The coefficients are $( b_M, d_M, e_M ) = ( 9.4, 7.4, 2.0 ), \;
( b_H, d_H, e_H ) = ( b_E, d_E, e_E ) = ( 9.4, 5.3, 2.0 )$.

The dependence of the bulk coefficient on the $Ri_B$ is illustrated in Figure [\brachio[p-sflx:cm\]] (#p-sflx:cm) and Figure [\brachio[p-sflx:ch\c\]] (#p-sflx:ch).

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


Here, it is important to note that $T_0$ is a quantity that is not required at this point in time. The surface temperature is the condition of the surface heat balance

$$
   F\theta(T_0,T_1) + L \beta Fq^P(T_0,q_1) + FR(T_0) - Fg(T_0,G_1) = 0
$$


is determined to satisfy. At this point, $T_0$ evaluates the fluxes in the previous time step. The true value of the flux that satisfies the surface balance is determined by solving this equation in conjunction with surface processes. In this sense, we have marked the above fluxes with $\hat{{}}$.

### handling at sea level.

At sea level, we follow Miller et al. (1992) and consider the following two effects.

 - Free convection is preeminent when the wind speed is low

 - The roughness of the sea surface varies with the wind speed.

The effect of free convective motion is estimated by calculating the buoyancy flux $F_B$,

$$
  F_B = F\theta/c_p + \epsilon T_0 F_q^P
$$


When it was $F_B >0$,

$$
  w^* = ( H_{B} F_B )^{1/3}
$$


$$
  |{$\mathbf{v}$}_1| = \left( u_1^2 + v_1^2 + (w^*)^2 \right)^{1/2}
$$


The $H_B$ corresponds to the mixed layer thickness scale. $H_B$ corresponds to the thickness scale of the mixing layer. The current standard value is $H_B=2000$ m.

The roughness variation of the sea surface is determined by the friction velocity ($u^*$)

$$
  u^* = \left( \sqrt{Fu^2 + Fv^2}/\rho \right)^{1/2}
$$


with ,

$$
  Z_{0M}  =  A_M + B_M (u^*)^2/g + C_M \nu/u^* \\
  Z_{0H}  =  A_H + B_H (u^*)^2/g + C_H \nu/u^* \\
  Z_{0E}  =  A_E + B_E (u^*)^2/g + C_E \nu/u^* 
$$




The evaluation is performed as follows. $\nu=1.5\times10^{-5}$ m$^2$ s$^{-1}$ is the kinematic viscosity coefficient of the atmosphere and the other standard values of the coefficients are $(A_M, B_M, C_M) = (0, 0.018, 0.11) $, $(A_H, B_H, C_H) = (1.4\times10^{-5}, 0, 0.4) $, $(A_E, B_E, C_E) = (1.3\times10^{-4}, 0, 0.62) $.

In the above calculations, we perform successive approximation calculations because $Fu, Fv, F\theta, Fq$ are required.

### Wind Speed Correction

In general, the downward transport of momentum is more efficient on a large rough surface than on a small rough surface, which results in a weaker wind over the surface, and the difference in wind speed can cancel out the difference in $C_D$ due to the difference in roughness.

In the model, the wind speed passed to the surface flux calculation is the value calculated by the time integration of the dynamic process and smoothed by the spectral expansion. Therefore, this compensation effect cannot be well represented in a region where the land and sea surfaces with widely different roughnesses coexist at small scales, for example, where the sea surface and the land surface. The momentum fluxes are calculated once, and then the wind speed in the lowermost layer of the atmosphere is corrected by the fluxes and the momentum, heat and water fluxes are recalculated once again.

### Minimum wind speed.

The minimum value of the surface wind speed ($|{$\mathbf{v}$}_1|$) for calculating the surface fluxes is set to take into account the effects of small-scale motions. The current standard value is 3m/s, which is common to all fluxes.
