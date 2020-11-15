Table of contents

<!-- TOC START min:1 max:3 link:true asterisk:false update:true -->
- [1. Surface Flux](#1-surface-flux)
	- [1.1. 本章でとりあげるプログラム [済 10月]](#11-本章でとりあげるプログラム-済-10月)
	- [1.2. PGSFC: AGCMと陸面/海水面スキーム間での変数の受け渡し [未 11月下旬作業予定]](#12-pgsfc-agcmと陸面海水面スキーム間での変数の受け渡し-未-11月下旬作業予定)
	- [1.3. Surface Flux Scheme [8割済 12月中旬に追加作業予定]](#13-surface-flux-scheme-8割済-12月中旬に追加作業予定)
		- [1.3.1. Overview](#131-overview)
		- [1.3.1. SEAZ0F: Roughness](#131-seaz0f-roughness)
		- [1.3.2. PSFCL: Richardson Number](#132-psfcl-richardson-number)
		- [1.3.3. PSFCL: Bulk factor](#133-psfcl-bulk-factor)
		- [1.3.4. PSFCM: Calculation of surface turbulent fluxes](#134-psfcm-calculation-of-surface-turbulent-fluxes)
- [2. POECN: Sea surface conditions for AGCM [未 11月下旬作業予定]](#2-poecn-sea-surface-conditions-for-agcm-未-11月下旬作業予定)
	- [2.1. fixed sea surface](#21-fixed-sea-surface)
<!-- TOC END -->



# 1. Surface Flux
## 1.1. 本章でとりあげるプログラム [済 10月]
メモ的に書き出したセクションなので、今後削除するかもしれません。

| module name      | file name            | contents                          |
|:-----------------|:---------------------|:----------------------------------|
| `MODULE:[PGSFC]` | `./physics/pgsfc.F ` | surface driver                    |
| `MODULE:[PSFCL]` | `./physics/psfcl.F`  | surface bulk transfer coefficient |
| `MODULE:[PSFCM]` | `./physics/psfcm.F`  | surface fluxes                    |
| `MODULE:[POCEN]` | `./physics/pgocn.F`  | mixed layer/fixed SST ocean       |

- `MODULE:[PGSFC]` (./physics/pgsfc.F)

| routine name | contents       |
|:-------------|:---------------|
| `SURFCE`     | surface driver |
| `RADSFC`     | --             |


- `MODULE:[PSFCL]` (./physics/psfcl.F)

| routine name | contents                  |
|:-------------|:--------------------------|
| `BLKCOF`     | bulk transfer coefficient |

- `MODULE:[PSFCM]` (./physics/psfcm.F)

| routine name | contents     |
|:-------------|:-------------|
| `SFCFLX`     | surface flux |


- `MODULE:[POCEN]` (./physics/pgocn.F)

| routine name  | contents                               |
|:--------------|:---------------------------------------|
| `OCEAN`       | mixed layer ocean driver               |
| `OCNSLV`      | surface temperature                    |
| `OCNSUB`      | mixed layer ocean                      |
| `ICEADJ`      | ice/temp. adjustment                   |
| `OSETCO`      | --                                     |
| `SEAALB`      | sea surface albedo                     |
| `SEAZ0F`      | roughness of ocean (flux dependent)    |
| `TICEMG`      | merge two different ice data, and etc. |
| `TICEMG2`     | --                                     |
| `ORSTRT`      | read physical initial value            |
| `OCHKV`       | valid range monitor                    |
| `OCEAN_DUMMY` | --                                     |


## 1.2. PGSFC: AGCMと陸面/海水面スキーム間での変数の受け渡し [未 11月下旬作業予定]

海面については`PGOCN`、陸面についてはMATSIROモデルの`LNDFLX` をそれぞれ呼び出す。

## 1.3. Surface Flux Scheme [8割済 12月中旬に追加作業予定]
### 1.3.1. Overview

The surface flux scheme evaluates the physical quantity fluxes between the atmospheric surfaces due to turbulent transport in the boundary layer. The main input data are wind speed ($u, v$),  temperature ($T$), and specific humidity ($q$), and the output data are the vertical fluxes and the differential values (for obtaining implicit solutions) of momentum, heat, and water vapor.

The bulk coefficients are obtained according to [Louis (1979)](./papers/Louis1979_Article_AParametricModelOfVerticalEddy.pdf) and [Louis <span>*et al.*</span>(1982)](./papers/Louis1982_a_short_history_of_the_operational_pbl_parameterization_at_ecmwf.pdf), except for the correction for the difference in roughness between momentum and heat. However, corrections are made to take into account the difference between momentum and heat roughness.

The outline of the calculation procedure is as follows.


1. calculate the roughness including modifications by ice and snow. `MODULE:[SEAZ0F]`
2. Calculate the Richardson number as the stability of the atmosphere. `MODULE:[PSFCL]`
3. calculate the bulk coefficient from Richardson number.  `MODULE:[PSFCL]`
4. calculate the flux and its derivative from the bulk coefficient. `MODULE:[PSFCM]`
5. If necessary, the calculated fluxes are re-calculated after taking into account the roughness effect, the free flow effect, and the wind speed correction.

### 1.3.1. SEAZ0F: Roughness

At sea level, we follow [Miller et al. 1992](./paper/Millers1992_Measuring_dynamic_surface\ and_interfacial_tensions.pdf) and consider the following two effects.

- Free convection is preeminent when the wind speed is low The roughness of the sea surface varies with the wind speed.
- Roughness of sea surface is caulculated following


The effect of free convective motion is estimated by calculating the buoyancy flux $F_B$,

$$
F_B = F_\theta/c_p + \epsilon T_0 F_q^P
$$

When $F_B > 0$,

$$
	w^* = (H_B F_B)^{1/3}\\
	| \mathbf{v} _1 | = \big( {u_1}^2 + {v_1}^2 + (w^*)^2 \big) ^{1/2}
$$


The $H_B$ corresponds to the mixed layer thickness scale. $H_B$ corresponds to the thickness scale of the mixing layer. The current standard value is $H_B=2000 \mathrm{m}$.

he roughness variation of the sea surface is determined by the friction velocity $u^*$

$$
u^{\star} = \sqrt{C_{M_0} ({U_0}^2  +{V_0}^2)}
$$

We perform successive approximation calculation of ${C_{M_0}}$, because $F_u,F_v,F_\theta,F_q$ are required.

$$
	r_{0,M} = z_{0,M_0} + z_{0,M_R} + \frac{z_{0,M_R} {u^\star }^2 }{g} + \frac{z_{0,M_S}\nu }{u^\star}\\
	r_{0,H} = z_{0,H_0} + z_{0,H_R} + \frac{z_{0,H_R} {u^\star }^2 }{g} + \frac{z_{0,H_S}\nu }{u^\star}\\
	r_{0,E} = z_{0,E_0} + z_{0,E_R} + \frac{z_{0,E_R} {u^\star }^2 }{g} + \frac{z_{0,E_S}\nu }{u^\star}
$$

Here, $\nu = 1.5 \times 10^{-5} \mathrm{m^2/s}$ is the kinetic viscosity of the atmosphere.
$z_{0,M},z_{0,H}$ and $z_{0,E}$ are surface roughness for momentum, heat, and vapor, respectively.
$z_{0,M_0},z_{0,H_0}$ and $z_{0,E_0}$ are base, and rough factor ($z_{0,M_R},z_{0,M_R}$ and $z_{0,E_R}$) and smooth factor ($z_{0,M_S},z_{0,M_S}$ and $z_{0,E_S}$) are taken into account.

When the sea ice exists,

$$
	z_{0,M} = z_{0,M} + ( z_{0,ice,M} - z_{0,M})  \alpha_{ice}\\
	z_{0,H} = z_{0,H} + ( z_{0,ice,H} - z_{0,H})  \alpha_{ice}\\
	z_{0,E} = z_{0,E} + ( z_{0,ice,E} - z_{0,E})  \alpha_{ice}
$$

Here, $r_{0,ice,*}$ is roughness of sea ice, $\alpha_{ice}$ is the sea ice concentration.

When the snow even exists,

$$
	z_{0,M} = z_{0,M} + ( z_{0,snow,M} - z_{0,M})  \alpha_{snow}\\
	z_{0,H} = z_{0,H} + ( z_{0,snow,H} - z_{0,H})  \alpha_{snow}\\
	z_{0,E} = z_{0,E} + ( z_{0,snow,E} - z_{0,E})  \alpha_{snow}
$$

Here, $r_{0,snow,*}$ is roughness of sea ice, $\alpha_{snow}$ is the sea ice concentration.

### 1.3.2. PSFCL: Richardson Number

The bulk Richardson number ($R_{iB}$), which is used as a benchmark for the stability between the atmospheric surfaces, is

$$
R_{iB} =
			\frac{ \frac{g}{\theta_s} (\theta_1 - \theta(z_0))/z_1 }
              { (u_1/z_1)^2                                  }\\
       = \frac{g}{\theta_s}
         \frac{T_1 (p_s/p_1)^\kappa - T_0 }{u_1^2/z_1} f_T .
$$


Here, $g$ is the gravitational accerelation\, $\theta_s$ ($\Theta_0$ in MATSIRO description) is the basic potential temperature, $T_1$ is the atmospheric temperature of the 1st layer, $T_0$ is the surface skin temperature, $p_s$ is the surface pressure, $p_1$ is the pressure of the 1st layer, $\kappa $ ($k$ in MATSIRO description) is the Karman constant, and

$$
f_T = (\theta_1 - \theta(z_0))/(\theta_1 - \theta_0)
$$


is a correction factor, which is approximated from the uncorrected bulk Richardson number, but we abbreviate the calculation here.

### 1.3.3. PSFCL: Bulk factor

The bulk coefficients of $C_M,C_H,C_E$ are calculated according to [Louis (1979)](./papers/Louis1979_Article_AParametricModelOfVerticalEddy.pdf) and [Louis <span>*et al.*</span>(1982)](./papers/Louis1982_a_short_history_of_the_operational_pbl_parameterization_at_ecmwf.pdf). However, corrections are made to take into account the difference between momentum and heat roughness. If the roughnesses for momentum, heat, and water vapor are set to $z_{0,M}, z_{0,H}, z_{0,E}$, respectively, the results are generally $z_{0,M} > z_{0,H}, z_{0,E}$, but the bulk coefficients for heat and water vapor for the fluxes from the height of $z_{0,M}$ are also set to $\widetilde{C_H}$, $\widetilde{C_E}$ first, and then corrected.

$$
C_M = \left\{
      \begin{array}{lr}
      C_{0,M} [ 1 + (b_M/e_M)  R_{iB} ]^{-e_M}
			&,
          R_{iB} \geq 0 \\
      C_{0,M} \left[ 1 - b_M R_{iB} \left( 1+ d_M b_M C_{0,M}
                                  \sqrt{\frac{z_1}{z_{0,M}}| R_{iB}|} \,
                                  \right)^{-1} \right]     
		  &,
          R_{iB} < 0 \\
      \end{array} \right.
$$


$$
\widetilde{C_H} = \left\{
      \begin{array}{lr}
      \widetilde{C_{0,H}} [ 1 + (b_H/e_H) R_{iB} ]^{-e_H}
			&,
          R_{iB} \geq 0 \\
      \widetilde{C_{0,H}} \left[ 1 - b_H R_{iB}
                                  \left( 1+ d_H b_H \widetilde{C_{0,H}}
                                  \sqrt{\frac{z_1}{z_{0,M}}| R_{iB}|} \,
                                  \right)^{-1} \right]
			 &,     
          R_{iB} < 0 \\
      \end{array} \right.
$$


$$
C_H = \widetilde{C_H} f_T
$$


$$
\widetilde{C_E} = \left\{
      \begin{array}{lr}
      \widetilde{C_{0,E}} [ 1 + (b_E/e_E) R_{iB} ]^{-e_E}
			&,
          R_{iB} \geq 0 \\
      \widetilde{C_{0,E}} \left[ 1 - b_E R_{iB}
                                  \left( 1+ d_E b_E \widetilde{C_{0,E}}
                                  \sqrt{\frac{z_1}{z_{0,M}}| R_{iB}|} \,
                                  \right)^{-1} \right]      
		  &,
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


but the method of calculation is omitted. The coefficients of Louis factors are $( b_M, d_M, e_M ) = ( 9.4, 7.4, 2.0 )$, $( b_H, d_H, e_H ) = ( b_E, d_E, e_E ) = ( 9.4, 5.3, 2.0 )$.


### 1.3.4. PSFCM: Calculation of surface turbulent fluxes

The turbulent fluxes at the ground surface are solved by bulk formulae as follows. Then, by solving the surface energy balance, the ground surface temperature ($T_s$) is updated, and the surface flux values with respect to those values are also updated. The solutions obtained here are temporary values. In order to solve the energy balance by linearizing with respect to $T_s$, the differential with respect to $T_s$ of each flux is calculated beforehand.

- Momentum flux

$$
 \tau_x = - \rho C_{M}|V_a| u_a \\
 \tau_y = - \rho C_{M}|V_a| v_a
$$


where $\tau_x$ and $\tau_y$  are the momentum fluxes (surface stress) of the zonal and meridional directions, respectively.

- Sensible heat flux

$$
 H_s = c_p \rho C_{Hs}|V_a| (T_s - (P_s/P_a)^{\kappa}T_a)\\
 $$

where $H_s$ is the sensible heat flux from the sea surface; $\kappa = R_{air} / c_p$ and $R_{air}$are the gas constants of air; and $c_p$ is the specific heat of air.

- Bare sea surface evaporation flux

$$
\hat{F}q^P_{1/2} = \rho_{1/2} C_E |{\mathbf{v}}_1| \left( q^*(T_0) - q_1 \right)
$$

# 2. POECN: Sea surface conditions for AGCM [未 11月下旬作業予定]
## 2.1. fixed sea surface
