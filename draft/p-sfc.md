<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [1 Sea Surface Conditions](#1-sea-surface-conditions)
	- [1.1 Overview [済 1月]](#11-overview-済-1月)
	- [1.2 Passing variables between AGCM and land/sea level schemes `[PGSFC]`[not yet done, work to be done in January].](#12-passing-variables-between-agcm-and-landsea-level-schemes-pgsfcnot-yet-done-work-to-be-done-in-january)
	- [1.3 Setting Sea Surface Conditions [済 1月]](#13-setting-sea-surface-conditions-済-1月)
		- [1.3.1 Input variables from the atmosphere](#131-input-variables-from-the-atmosphere)
		- [1.3.2 Ocean Surface Conditions `[OCNBCS]`](#132-ocean-surface-conditions-ocnbcs)
			- [1.3.2.1 Albedo](#1321-albedo)
			- [1.3.2.2 Roughness](#1322-roughness)
			- [1.3.2.3 Sea Surface heat flux](#1323-sea-surface-heat-flux)
	- [1.4 Surface Flux [済 1月]](#14-surface-flux-済-1月)
		- [1.4.1 Overview](#141-overview)
			- [1.4.2 Basic Formula for Flux Calculations](#142-basic-formula-for-flux-calculations)
		- [1.4.2 Roughness `[SEA0F]`](#142-roughness-sea0f)
			- [1.4.2.1 variables](#1421-variables)
		- [1.4.3 Richardson Number `[PSFCL]`](#143-richardson-number-psfcl)
		- [1.4.4 Bulk factor `[BLKCOF]`](#144-bulk-factor-blkcof)
		- [1.4. Calculation of surface turbulent fluxes `[PSFCM]`](#14-calculation-of-surface-turbulent-fluxes-psfcm)
	- [1.5 Radiation Flux at Sea Surface `[RADSFC]` [済 1月]](#15-radiation-flux-at-sea-surface-radsfc-済-1月)
	- [1.6 Surface Heat Balance `[OCNSLV]`　[済 1月]](#16-surface-heat-balance-ocnslv-済-1月)

<!-- /TOC -->


# 1 Sea Surface Conditions
Sea surface processes provide the boundary conditions at the lower end of the atmosphere through the exchange of momentum, heat, and water fluxes between the atmosphere and the surface. Until [CCSR/NIES AGCM](), both land surface and sea surface were treated as one of the atmospheric physical processes, but after MIROC3 (Hasumi and Emori, 2004), land surface processes became independent as MATSIRO. However, since MIROC3 (Hasumi and Emori, 2004), land surface processes have been separated into MATSIRO. This chapter describes sea surface processes, which are still treated within the framework of atmospheric physical processes (MIROC6). For the land surface processes, please refer to [Description of ILS](https://github.com/integrated-land-simulator/model_description).

## 1.1 Overview [済 1月]

In `MODULE: [PGSFC]`, `[OCNFLX]` (`MODULE: [POCEN]`) is called for the sea surface, and `[LNDFLX]` of MATSIRO model is called for the land surface. In `[OCNFLX]`, the following procedure is used to deal with sea surface processes.

1. prepare variables for sea ice extent and no ice extent, respectively, using sea ice concentration. 2.
Determine the surface boundary conditions. 3.
Calculate the flux balance. 4.
Calculate the radiation budget at the sea surface. 5.
(3) Calculate the deposition by CHASER.
6. solve the heat balance at the sea surface and update the surface temperature and each flux value.


The four modules discussed in this chapter are as follows.

| module name      | file name            | contents                          |
|:-----------------|:---------------------|:----------------------------------|
| `MODULE:[PGSFC]` | `./physics/pgsfc.F ` | surface driver                    |
| `MODULE:[PSFCL]` | `./physics/psfcl.F`  | surface bulk transfer coefficient |
| `MODULE:[PSFCM]` | `./physics/psfcm.F`  | surface fluxes                    |
| `MODULE:[PGOCN]` | `./physics/pgocn.F`  | mixed layer/fixed SST ocean       |

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

| routine name  | contents                            |
|:--------------|:------------------------------------|
| `OCEAN`       | mixed layer ocean driver            |
| `OCNSLV`      | surface temperature                 |
| `OCNSUB`      | mixed layer ocean                   |
| `ICEADJ`      | ice/temp. adjustment                |
| `OSETCO`      | --                                  |
| `SEAALB`      | sea surface albedo                  |
| `SEAZ0F`      | roughness of ocean (flux dependent) |
| `TICEMG`      | merge two different ice |, and etc. |
| `TICEMG2`     | --                                  |
| `ORSTRT`      | read physical initial value         |
| `OCHKV`       | valid range monitor                 |
| `OCEAN_DUMMY` | --                                  |


## 1.2 Passing variables between AGCM and land/sea level schemes `[PGSFC]`[not yet done, work to be done in January].

Calling `OCNFLX` (`MODULE: [POCEN]`) for sea level and `LNDFLX` of the MATSIRO model for land level, respectively.


[カップラーのセクション](https://github.com/MIROC-DOC/model_description/blob/coupler_iwakiri/draft/AO-coupler.md)とmerge予定。

## 1.3 Setting Sea Surface Conditions [済 1月]

### 1.3.1 Input variables from the atmosphere

| variable | meaning                  |
|:---------|:-------------------------|
| GAUA     | u-wind                   |
| GAVA     | v-wind                   |
| GATA     | temperature T            |
| GAQA     | humidity q               |
| GAPA     | pressure P               |
| GAPS     | surface pressure Ps      |
| GAZS     | surface height           |
| RSFCD    | surface radiation fluxes |
| RCOSZ    | cos(solar angle)         |

If use CHASER, variables below are also needed.

| variable | meaning                                              |
|:---------|:-----------------------------------------------------|
| EH       | Henry const                                          |
| PFLXC    | precipitation flux (cumulus convection scheme)       |
| PFLXL    | precipitation flux (large scale condensation scheme) |
| LLAT     | latitude                                             |

Practically, precipitation flux from 2 schemes are treated together.


$$.
	Pr = Pr_c + Pr_l
$$.



In the sea ice area ($L=1$), the surface temperature $T_s$ is the sea ice surface temperature $T_{ice}$. However, if $T_{ice}$ is higher than $T_{melt}=0$, then $T_{melt}$ is used.

$$.
	T_s = min(T_{ice},T_{melt})
$$.

The sea ice bottom temperature $T_b$ is assumed to be the ocean surface temperature $T_{o(1)}$.

$$.
	T_b = T_{o(1)}
$$.

The amount of sea ice W_{ice} and the amount of snow on it W_{snow} are converted per unit area by considering $R_{ice}$ and used in the calculation. However, a limiter $\epsilon$ is provided to prevent the values from becoming too small.

$$.
R_{ice} =\mathrm{max}( R_{ice,orginal}, \epsilon)
$$.


In the ice-free region ($L=2$), the surface temperature $T_s$ and sea ice bottom temperature $T_b$ are assumed to be the ocean surface temperature $T_{o(1)}$.

$$.
	T_s = T_b = T_{o(1)}
$$.


The evaporation coefficient is assumed to be $GRBET=1$ for both $L=1 and 2$.


If the sea ice concentration $R_{ice}$ is not given, it can be diagnosed simply from the sea ice volume $W_{ice}$.

$$.
R_{ice} = \mathrm{min}\Big(\sqrt{\frac{\mathrm{max}(W_{ice},0)}{W_{ice,c}}},1.0\Big)
$$.

The standard gives the amount of sea ice per area as $W_{ice,c}=300 \mathrm{[kg/m^2]}$.


### 1.3.2 Ocean Surface Conditions `[OCNBCS]`

- Output variables

| variable | Presentation                      | Meaning           |
|:---------|:----------------------------------|:------------------|
| GRALB    | $\alpha$                          | surface albedo    |
| GRZ0     |                                   | surface roughness |
| GFLUXS   | $G$                               | heat flux         |
| DGFDS    | $\frac{\partial G}{\partial T_s}$ | dG/dTs            |

- Input variables

| Variable | Presentation | Meaning          |
|:---------|:-------------|:-----------------|
| GRTS     | $T_s$        | skin temperature |
| GRTB     | $T_{b,ice}$  | ice base temp.   |
| GRICE    |              | sea ice          |
| GRSNW    |              | snow smount      |
| GRICR    | $R_{ice}$    | ice fraction     |
| GDUA     | $U_0$        | u sfc wind       |
| GDVA     | $V_0$        | v sfc wind       |
| RCOSZ    |              | cos(sol.zenith)  |

- Internal variables

| variable | Presentation | Meaning       |
|:---------|:-------------|:--------------|
| GRSNR    |              | snow fraction |


#### 1.3.2.1 Albedo

In this module, surface albedo and roughness are calculated. They are calculated supposing ice-free conditions, then modified.

First, let us consider the sea albedo. The sea level $\alpha_{(d,b)}$, $b=1,2,3$ represent the visible, near-infrared, and infrared wavelength bands, respectively. Also, $d=1,2$ represents direct and scattered light, respectively.

1. Sea Surface Albedo for Visible `[SEAALB]`

- Internal parameters

| Meaning | Presentation     | Variable | unit | value                          |
|:--------|:-----------------|:---------|:-----|:-------------------------------|
|         | $C_1, C_2, C_3$  | CC       | [-]  | $-0.7479, -4.677039, 1.583171$ |
|         | $\alpha_{L(2)} $ | ALBDIF   | [-]  | $0.06$                         |


For sea surface level albedo $\alpha_{L(d)}$, $d=1,2$ represents direct and scattered light, respectively.


Using the solar zenith angle at latitude $\theta$, the albedo for direct light is presented by

$$
	\alpha_{L(1)} = e^{(C_3A^* + C_2) A^* +C_1}
$$

where $A = \mathrm{min}(\mathrm{max}(\mathrm{cos}(\theta),0.03459),0.961) $

On the other hand, the albedo for scattered light is uniformly set to a constant parameter.

$$
	\alpha_{L(2)} = 0.06
$$

2. Sea Surface Albedo for Near-Infrared and Infrared

 The albedo for near-infrared is set to same as the visible one.

$$
	\alpha_{1,2} =\alpha_{1,1}
$$

$$
	\alpha_{2,2} =\alpha_{2,1}
$$

 The albedo for infrared is uniformly set to a constant value.

3. Albedo modification by ice

The grid-averaged albedo, taking into account the sea ice concentration $R_{ice}$, is

$$
	\alpha = \alpha -R_{ice} \alpha_{ice}
$$

\alpha_{ice}$ is given by the standard as $\alpha_{ice,1}=0.5,\alpha_{ice,2}=0.5,\alpha_{ice,3}=0.05$. 4.

4. albedo modification by snow

In addition, we want to consider the effect of snow cover. Here, we consider the albedo modification by temperature. The standard threshold values for snow temperature are $T_{al,2}=258.15 \mathrm{[K]}$ and $T_{al,1}=273.15 \mathrm{[K]}$. The snow albedo changes linearly with temperature change from $\alpha_{snow,1}=0.75$ to $\alpha_{ snow,2}$. Let the coefficient $\tau_{snow}$, which is $0\le \tau \le 1$.

$$
\tau_{snow} = \frac{T_s - T_{al,1}}{T_{al,2}-T_{al,1}}
$$

Update the snow albedo $\alpha_{snow}$ as

$$
	\alpha_{snow} = \alpha_{snow,0} + \tau_{snow}(\alpha_{snow,2}-\alpha_{snow,1})
$$

#### 1.3.2.2 Roughness

1. Sea Surface Roughness `[SEAZ0F]`

The roughness variation of the sea surface is determined by the friction velocity $u^\star$

$$
u^{\star} = \sqrt{C_{M_0} ({U_0}^2  +{V_0}^2)}
$$

We perform successive approximation calculation of ${C_{M_0}}$, because $F_u,F_v,F_\theta,F_q$ are required.

$$
	r_{0,M} = z_{0,M_0} + z_{0,M_R} + \frac{z_{0,M_R} {u^\star }^2 }{g} + \frac{z_{0,M_S}\nu }{u^\star}
$$

$$
	r_{0,H} = z_{0,H_0} + z_{0,H_R} + \frac{z_{0,H_R} {u^\star }^2 }{g} + \frac{z_{0,H_S}\nu }{u^\star}
$$

$$
	r_{0,E} = z_{0,E_0} + z_{0,E_R} + \frac{z_{0,E_R} {u^\star }^2 }{g} + \frac{z_{0,E_S}\nu }{u^\star}
$$

Here, $\nu = 1.5 \times 10^{-5} \mathrm{[m^2/s]}$ is the kinetic viscosity of the atmosphere.
$z_{0,M},z_{0,H}$ and $z_{0,E}$ are surface roughness for momentum, heat, and vapor, respectively.
$z_{0,M_0},z_{0,H_0}$ and $z_{0,E_0}$ are base, and rough factor ($z_{0,M_R},z_{0,M_R}$ and $z_{0,E_R}$) and smooth factor ($z_{0,M_S},z_{0,M_S}$ and $z_{0,E_S}$) are taken into account.


2. Roughness modification by ice

When the sea ice exists ($L=1$),

$$
	z_{0,M} = z_{0,M} + ( z_{0,ice,M} - z_{0,M})  \alpha_{ice}
$$

$$
	z_{0,H} = z_{0,H} + ( z_{0,ice,H} - z_{0,H})  \alpha_{ice}
$$

$$
	z_{0,E} = z_{0,E} + ( z_{0,ice,E} - z_{0,E})  \alpha_{ice}
$$

Here, $r_{0,ice,*}$ is roughness of sea ice, $\alpha_{ice}$ is the sea ice concentration.


3. Roughness modification by snow

When the snow even exists,

$$
	z_{0,M} = z_{0,M} + ( z_{0,snow,M} - z_{0,M})  \alpha_{snow}
$$

$$
	z_{0,H} = z_{0,H} + ( z_{0,snow,H} - z_{0,H})  \alpha_{snow}
$$

$$
	z_{0,E} = z_{0,E} + ( z_{0,snow,E} - z_{0,E})  \alpha_{snow}
$$

Here, $r_{0,snow,*}$ is roughness of sea ice, $\alpha_{snow}$ is the sea ice concentration.

#### 1.3.2.3 Sea Surface heat flux

1. Conductivity of ice

When sea ice exists ($L=1$), the thermal conductivity $k_{ice}^*$ of sea ice is obtained by using $D_{f,ice}$ (thermal diffusivity of sea ice) and sea ice density $\sigma_{ice}$.

$$
k_{ice}^* = \frac{D_{f,ice}}{\mathrm{max}(R_{ice}/\sigma_{ice}, \epsilon)}
$$

2. conductivity modification by snow

The calculated thermal conductivity is modified to $k_{ice}$$ to take into account that it varies with snow cover.

$$
h_{snow} = \mathrm{min}(
	\mathrm{max}(
	R_{snow}/\sigma_{snow}),\epsilon
		),h_{snow,max}
		)
$$

$$		
k_{ice} = k_{ice}^* (1-R_{ice}) + \frac{D_{ice}}{1+\| D_{ice}/D_{snow} \cdot h_{snow} \|} R_{ice}
$$

where $h_{snow}$ is the snow depth, $R_{snow}$ is the snow area fraction, $\sigma_{snow}$ is the snow density, $h_{snow,max}$ is the maximum snow depth, and $D_{snow}$ is the thermal diffusivity of snow. 3.

3. calculate flux and its derivative

Therefore, the heat conduction flux and its derivative are

$$
 G = k_{ice} (T_b - T_s)
$$

$$
 \frac{\partial G}{\partial T} = k_{ice}
$$.

Note that in the ice-free region ($L=2$)

$$
G=k_{ocn}
$$ G=k_{ocn}

where $k_{ocn}$$ is the heat flux in the ocean surface layer. Here, $$k_{ocn}$$ is the heat flux in the ocean surface layer.

## 1.4 Surface Flux [済 1月]


### 1.4.1 Overview
The surface flux scheme evaluates the physical quantity fluxes between the atmospheric surfaces due to turbulent transport in the boundary layer. The main input | are wind speed ($u, v$),  temperature ($T$), and specific humidity ($q$), and the output | are the vertical fluxes and the differential values (for obtaining implicit solutions) of momentum, heat, and water vapor.

The bulk coefficients are obtained according to [Louis (1979)](./papers/Louis1979_Article_AParametricModelOfVerticalEddy.pdf) and [Louis <span>*et al.*</span>(1982)](./papers/Louis1982_a_short_history_of_the_operational_pbl_parameterization_at_ecmwf.pdf), except for the correction for the difference in roughness between momentum and heat. However, corrections are made to take into account the difference between momentum and heat roughness.

The outline of the calculation procedure is as follows.


1. Calculate the roughness including modifications by ice and snow. `MODULE:[SEAZ0F]`
2. Calculate the Richardson number as the stability of the atmosphere. `MODULE:[PSFCL]`
3. Calculate the bulk coefficient from Richardson number.  `MODULE:[PSFCL]`
4. Calculate the flux and its derivative from the bulk coefficient. `MODULE:[PSFCM]`
5. If necessary, the calculated fluxes are re-calculated after taking into account the roughness effect, the free flow effect, and the wind speed correction.

#### 1.4.2 Basic Formula for Flux Calculations

Surface fluxes ($F_u, F_v, F_\theta, F_q$) are expressed using the bulk coefficients ($C_M, C_H, C_E$) as follows

$$
	F_u  =  - \rho C_M |{\mathbf{v}}| u
$$


$$
	F_v  =  - \rho C_M |{\mathbf{v}}| v
$$


$$
	F_\theta  = \rho c_p C_H |{\mathbf{v}}| ( \theta_g - \theta )
$$


$$
	F_q^P =  \rho C_E |{\mathbf{v}}| ( q_g - q )
$$

Note that $F_q^P$ is the possible evaporation flux.


### 1.4.2 Roughness `[SEA0F]`

#### 1.4.2.1 variables
- Output Variables

| Variable | Presentation | Meaning               |
|:---------|:-------------|:----------------------|
| GRZ0M    | $r_{0,M}$    | surface roughness (V) |
| GRZ0H    | $r_{0,H}$    | surface roughness (T) |
| GRZ0E    | $r_{0,E}$    | surface roughness (q) |

- Input variables

| Variable | Presentation | Meaning          |
|:---------|:-------------|:-----------------|
| USFC     | $U_0$        | u sfc wind speed |
| VSFC     | $V_0$        | v sfc wind speed |

- Internal variables

| Variable | Presentation | Meaning           |
|:---------|:-------------|:------------------|
| USTAR    | $u^\star$    | friction velocity |

- Internal parameters

| Variable | Presentation | Meaning             |     Values |
|:---------|:-------------|:--------------------|-----------:|
| Z0M0     | $r_{0,M_0}$  | base                |        $0$ |
| Z0MR     | $r_{0,M_R}$  | rough factor        | $   0.18 $ |
| Z0MS     | $r_{0,M_S}$  | smooth factor       | $   0.11 $ |
| Z0H0     | $r_{0,H_0}$  | base                | $ 1.4^-5 $ |
| Z0HR     | $r_{0,H_R}$  | rough factor        | $    0.0 $ |
| Z0HS     | $r_{0,H_S}$  | smooth factor       | $    0.4 $ |
| Z0E0     | $r_{0,E_0}$  | base                | $ 1.3^-4 $ |
| Z0ER     | $r_{0,E_R}$  | rough factor        | $    0.0 $ |
| Z0ES     | $r_{0,E_S}$  | smooth factor       | $   0.62 $ |
| VISAIR   | $\nu$        | kinematic viscosity | $ 1.5^-5 $ |
| CM0      | $C_{M_0}$    | bulk coef for $u^*$ | $ 1.0^-3 $ |
| USTRMN   |              | min(u*)             | $ 1.0^-3 $ |
| Z0MMIN   |              | minimum             | $ 3.0^-5 $ |
| Z0HMIN   |              | minimum             | $ 3.0^-5 $ |
| Z0EMIN   |              | minimum             | $ 3.0^-5 $ |

### 1.4.3 Richardson Number `[PSFCL]`

The bulk Richardson number ($R_{iB}$), which is used as a benchmark for the stability between the atmospheric surfaces, is

$$
R_{iB} =
			\frac{ \frac{g}{\theta_s} (\theta_1 - \theta(z_0))/z_1 }
              { (u_1/z_1)^2                                  }
       = \frac{g}{\theta_s}
         \frac{T_1 (p_s/p_1)^\kappa - T_0 }{u_1^2/z_1} f_T
$$


Here, $g$ is the gravitational accerelation\, $\theta_s$ ($\Theta_0$ in MATSIRO description) is the basic potential temperature, $T_1$ is the atmospheric temperature of the 1st layer, $T_0$ is the surface skin temperature, $p_s$ is the surface pressure, $p_1$ is the pressure of the 1st layer, $\kappa $ ($k$ in MATSIRO description) is the Karman constant, and

$$
f_T = (\theta_1 - \theta(z_0))/(\theta_1 - \theta_0)
$$


is a correction factor, which is approximated from the uncorrected bulk Richardson number, but we abbreviate the calculation here.

### 1.4.4 Bulk factor `[BLKCOF]`

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
       \frac{k^2}{\left[\ln \left(\frac{z_1}{z_{0M}}\right)\right]^2 }
$$


Correction Factor $f_q$ is ,

$$
  f_q = (q_1 - q(z_0))/(q_1 - q^{\ast}(\theta_0))
$$

but the method of calculation is omitted. The coefficients of Louis factors are $( b_M, d_M, e_M ) = ( 9.4, 7.4, 2.0 )$, $( b_H, d_H, e_H ) = ( b_E, d_E, e_E ) = ( 9.4, 5.3, 2.0 )$.


### 1.4. Calculation of surface turbulent fluxes `[PSFCM]`
- Modified variables


| Variable | Presentation | Meaning   |
|:---------|:-------------|:----------|
| UFLUXS   |              | flux of U |
| VFLUXS   |              | flux of V |
| TFLUXS   |              | flux of T |
| QFLUXS   |              | flux of q |

- Output variables


| variable | Presentation | Meaning         |
|:---------|:-------------|:----------------|
| DUFDU    |              | -d(tau)/du      |
| DTFDT    |              | -dH/dTa         |
| DQFDQ    |              | -dLE/dqa        |
| DTFDS    |              | dH/dTs          |
| DQFDS    |              | dLE/dTs         |
| CDVE     |              | bulk coef.      |
| RM10     |              | coef. for 10m u |
| RH2      |              | coef. for 2m T  |
| RE2      |              | coef. for 2m q  |
| U10      |              | 10m u           |
| V10      |              | 10m v           |
| T2       |              | 2m T            |
| Q2       |              | 2m q            |

- Input variables

| Meaning                  | Presentation | Variable | dimension | unit |
|:-------------------------|:-------------|:----------------------------|
| westerly u               |              | GDUA                        |
| southern wind v          |              | GDVA                        |
| temperature T            |              | GDTA                        |
| humidity q               |              | GDQA                        |
| pressure (lev=1)         |              | GDPA                        |
| surface pressure         |              | GDPS                        |
| surface skin temperature |              | GDTS                        |
| surface roughness        |              | GRZ0                        |
| soil wetness             |              | GRBET                       |
| ocean u                  |              | GRUA                        |
| ocean v                  |              | GRVA                        |


The turbulent fluxes at the sea surface are solved by bulk formulae as follows. Then, by solving the surface energy balance, the ground surface temperature ($T_s$) is updated, and the surface flux values with respect to those values are also updated. The solutions obtained here are temporary values. In order to solve the energy balance by linearizing with respect to $T_s$, the differential with respect to $T_s$ of each flux is calculated beforehand.

- Momentum flux

$$
 \tau_x = - \rho C_{M}|V_a| u_a
$$

$$
 \tau_y = - \rho C_{M}|V_a| v_a
$$


where $\tau_x$ and $\tau_y$  are the momentum fluxes (surface stress) of the zonal and meridional directions, respectively.

- Sensible heat flux

$$
 H_s = c_p \rho C_{Hs}|V_a| (T_s - (P_s/P_a)^{\kappa}T_a)
$$

where $H_s$ is the sensible heat flux from the sea surface; $\kappa = R_{air} / c_p$ and $R_{air}$are the gas constants of air; and $c_p$ is the specific heat of air.

- Bare sea surface evaporation flux

$$
\hat{F}q^P_{1/2} = \rho_{1/2} C_E |{\mathbf{v}}_1| \left( q^*(T_0) - q_1 \right)
$$




## 1.5 Radiation Flux at Sea Surface `[RADSFC]` [済 1月]


For the ground surface albedo $\alpha_{(d,b)}$, $b=1,2$ represent the visible and near-infrared wavelength bands, respectively. Also, $d=1,2$ are direct and scattered, respectively. For the downward shortwave radiation $SW^\downarrow$ and upward shortwave radiation $SW^\uparrow$ incident on the earth's surface, the direct and scattered light together are

$$
	SW^\downarrow = SW^\downarrow_{(1,1)}+SW^\downarrow_{(1,2)}+SW^\downarrow_{(2,1)}+SW^\downarrow_{(2,2)}
$$

$$
SW^\uparrow = SW^\downarrow_{(1,1)}\cdot\alpha_{(1,1)}+SW^\downarrow_{(1,2)}\cdot\alpha_{(1,2)}+SW^\downarrow_{(2,1)}\cdot\alpha_{(2,1)}+SW^\downarrow_{(2,2)}\cdot\alpha_{(2,2)}
$$

## 1.6 Surface Heat Balance `[OCNSLV]`　[済 1月]

The comments for some variables say "soil", but this is because the program was adapted from a land surface scheme, and has no particular meaning.

- Outputs

| Meaning                | Presentation   | Variable | dimension | unit |
|:-----------------------|:---------------|:---------|:----------|:-----|
| surface water flux \*1 | $W_{free/ice}$ | WFLUXS   | IJLSDM,2  |      |
| upward long wave       | $LW^\uparrow$  | RFLXLU   | IJLSDM    |      |
| flux balance           | $F$            | SFLXBL   | IJLSDM    |      |


- Inputs variables

| Meaning                       | Presentation                      | Variable |
|:------------------------------|:----------------------------------|:---------|
| sensible heat flux coefficent | $\frac{\partial H}{\partial T_s}$ | DTFDS    |
| latent heat flux coefficient  | $\frac{\partial E}{\partial T_s}$ | DQFDS    |
| surface heat flux coefficient | $\frac{\partial G}{\partial T_s}$ | DGFDS    |
| downward SW radiation         | $SW^\downarrow$                   | RFLXSD   |
| upward SW radiation           | $SW^\uparrow$                     | RFLXLU   |
| downward LW radiation         | $LW^\downarrow$                   | RFLXLD   |
| sea surface albedo            | $\alpha$                          | GRALBL   |
| sea ice concentration         | $R_{ice}$                         | GRICR    |

- Modified in this subroutine

| Meaning                        | Presentation | Variable | dimension | unit |
|:-------------------------------|:-------------|:---------|:----------|:-----|
| skin temperature               | $T_s$        | GDTS     | IJLSDM    |      |
| surface heat flux from `seaBC` | $G$          | GFLUXS   | IJLSDM    |      |
| sensible heat flux             | $H$          | TFLUXS   | IJLSDM    |      |
| latent heat flux               | $E$          | QFLUXS   | IJLDSM    |      |

- Internal work

| Meaning                                         | Presentation                            | Variable | dimension |
|:------------------------------------------------|:----------------------------------------|:---------|:----------|
| latent heat for sublimation                     | $l_s$                                   | ESUB     |           |
| emissivity of the sea surface                   | $\epsilon$                              | EMIS     |           |
| black body radiation                            | $(1-\alpha)\sigma T_s^4 $               | STG      |           |
| dR/dTs                                          | $\frac{\partial R}{\partial T_s}$       | DRFDS    |           |
| net surface flux                                | $F^*$                                   | SFLUX    |           |
| net heat flux (downward positive)               | $G^*$                                   | GSFLUX   |           |
| The temperature derivative term of $G^*$        | $\frac{dG^*}{dT_s}$                     | DGSFDS   |           |
| surface heat flux for ice-free area             | $G_{free}$                              | GFLUXF   |           |
| sensible heat flux for ice covered area         | $\delta H_{ice}$                        | SFLUXBI  |           |
| temperature derivative term of $G_{ice}$        | $\frac{\partial G_{ice}}{\partial T_s}$ | DSBDSI   |           |
| surface temperature change for ice-covored area | $\Delta T_{ice}$                        | DTI      |           |
| latennt heat flux for ice covered area          | $E_{ice}$                               | EVAPI    |           |
| surface heat flux for ice covered area          | $G_{ice}$                               | GFLUXI   |           |
|                                                 | $1-R_{ice}$                             | FF       |           |
| sea ice fraction                                | $R_{ice}$                               | FI       |           |
|                                                 | $R_{ice}\Delta T_{ice}$                 | DTX      |           |

- Others (appeared in texts)

| Meaning                                               | Presentation | Variable | dimension | unit |
|:------------------------------------------------------|:-------------|:---------|:----------|:-----|
| sea surface albedo for shortwave radiation (ice-free) | $\alpha_S$   |          | [-]       |      |
| the Stefan-Boltzmann constant                         | $\sigma$     | STB      |           |      |

Reference: [Hasumi, 2015, Appendices A](https://ccsr.aori.u-tokyo.ac.jp/~hasumi/COCO/coco4.pdf)

Downward radiative fluxes are not directly dependent on the condition of the sea surface, and their observed values are simply specified to drive the model. Shotwave emission from the sea surface is negligible, so the upward part of the shortwave radiative flux is accounted for solely by reflection of the incoming downward flux. Let $\alpha _S$ be the sea surface albedo for shortwave radiation. The upward shortwave radiative flux is represented by

$$
	SW^\uparrow = - \alpha_S SW^\downarrow
$$

On the other hand, the upward longwave radiative flux has both reflection of the incoming flux and emission from the sea surface. Let $\alpha$ be the sea surface albedo for longwave radiation and $\epsilon$ be emissivity of the sea surface relative to the black body radiation. The upward shortwave radiative flux is represented by

$$
	LW^\uparrow = - \alpha LW^\downarrow + \epsilon \sigma T_s ^4
$$

where $\sigma$ is the Stefan-Boltzmann constant and $T_s$ is skin temperature. If sea ice exists, snow or sea ice temperature is considered by fractions. When radiative equilibrium is assumed, emissivity becomes identical to co-albedo:

$$
	\epsilon = 1 - \alpha
$$

The net surface flux is presented by

$$
	F^*=H + (1-\alpha)\sigma T_s^4 + \alpha LW^\uparrow - LW^\downarrow +SW^\uparrow - SW^\downarrow		
$$

The heat flux into the sea surface is presented, with the surface heat flux calculated in `PSFCM`

$$
	G^* = G - F^*
$$

Note that $G^*$ is downward positive.

The temperature derivative term is

$$
	\frac{\partial G^*}{\partial T_s} = \frac{\partial G}{\partial T_s}+\frac{\partial H}{\partial T_s}+\frac{\partial R}{\partial T_s}
$$

When the sea ice exists, the sublimation flux is considered

$$
	G_{ice} = G^* - l_s E
$$

The temperature derivative term is

$$
	\frac{\partial G_{ice}}{\partial T_s}=\frac{\partial G^*}{\partial T_s} + l_s\frac{\partial E}{\partial T_s}
$$

Finally, we can update the surface temperature with the sea ice concentration with $\Delta T_s=G_{ice} ( \frac{\partial G_{ice}}{\partial T_s})^{-1}$


$$
	T_s = T_s +R_{ice} \Delta T_s
$$

Then, the sensible and latent heat flux on the sea ice is updated.

$$
	E_{ice} = E + \frac{\partial E}{\partial T_s}\Delta T_s
$$

$$
	H_{ice} = H + \frac{\partial H}{\partial T_s}\Delta T_s
$$

When the sea ice does not existed, otherwise, the evaporation flux is added to the net flux.

$$
	G_{free}=F^* + l_cE
$$

Finally each flux is updated.

For the sensible heat flux, the temperature change on the sea ice is considered.

$$
	H=H+ R_{ice}  H_{ice}
$$

Then, the heat used for the temperature change is saved.

$$
	F = R_{ice} H_{ice}
$$

For the upward longwave radiative flux, the temperature change on the sea ice is considered.

$$
	LW^\uparrow=LW^\uparrow +  4\frac{\sigma}{T_s}R_{ice}  \Delta T_s
$$

For the surface heat flux, the sea ice  concentration is considered.

$$
	G=(1-R_{ice})G_{free} + R_{ice}G_{ice}
$$

For the latent heat flux, the sea ice  concentration is considered.

$$
	E=(1-R_{ice})E + R_{ice}E_{ice}
$$

Each term above are saved as freshwater flux.

$$
	W_{free} = (1-R_{ice}) E
$$

$$
	W_{ice} = R_{ice} E_{ice}
$$|$
