<!-- TOC START min:1 max:5 link:true asterisk:false update:true -->
- [1 Sea Surface](#1-sea-surface)
	- [1.1 Overview [済 10月]](#11-overview-済-10月)
	- [1.2 AGCMと陸面/海水面スキーム間での変数の受け渡し `[PGSFC]`[未 1月作業予定]](#12-agcmと陸面海水面スキーム間での変数の受け渡し-pgsfc未-1月作業予定)
	- [1.3 Setting Sea Surface Conditions `[PGOCN]` [7割済 12月]](#13-setting-sea-surface-conditions-pgocn-7割済-12月)
		- [1.3.1 Input from the atmosphere](#131-input-from-the-atmosphere)
		- [1.3.2 Ocean Surface Conditions `[OCNBCS]`](#132-ocean-surface-conditions-ocnbcs)
			- [1.3.2.1 Albedo](#1321-albedo)
				- [1.3.2.1.1 Sea Surface Albedo `[SEAALB]`](#13211-sea-surface-albedo-seaalb)
				- [1.3.2.1.2 Albedo modification by ice and snow](#13212-albedo-modification-by-ice-and-snow)
			- [1.3.2.2 Roughness](#1322-roughness)
				- [1.3.2.2.1 Sea Surface Roughness `[SEAZ0F]`](#13221-sea-surface-roughness-seaz0f)
				- [1.3.2.2.2 Roughness modification by ice and snow](#13222-roughness-modification-by-ice-and-snow)
			- [1.3.2.3 Sea Surface heat flux](#1323-sea-surface-heat-flux)
	- [1.4 Surface Flux [8割済 11月]](#14-surface-flux-8割済-11月)
		- [1.4.1 Overview](#141-overview)
		- [1.4.2 Roughness `[SEA0F]`](#142-roughness-sea0f)
		- [1.4.3 Richardson Number `[PSFCL]`](#143-richardson-number-psfcl)
		- [1.4.4 Bulk factor `[PSFCL]`](#144-bulk-factor-psfcl)
		- [1.4. Calculation of surface turbulent fluxes `[PSFCM]`](#14-calculation-of-surface-turbulent-fluxes-psfcm)
	- [1.5 Radiation Flux at Sea Surface `[RADSFC]` [7割済 12月]](#15-radiation-flux-at-sea-surface-radsfc-7割済-12月)
	- [1.6 Surface Heat Balance `[OCNSLV]`　[7割済 12月]](#16-surface-heat-balance-ocnslv7割済-12月)
		- [1.6.1 Variables](#161-variables)
		- [1.6.2 Calculating heat Balance](#162-calculating-heat-balance)
<!-- TOC END -->



# 1 Sea Surface
## 1.1 Overview [済 10月]

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


## 1.2 AGCMと陸面/海水面スキーム間での変数の受け渡し `[PGSFC]`[未 1月作業予定]

海面については`OCNFLX`、陸面についてはMATSIROモデルの`LNDFLX` をそれぞれ呼び出している。

[カップラーのセクション](https://github.com/MIROC-DOC/model_description/blob/coupler_iwakiri/draft/AO-coupler.md)とmerge予定。

## 1.3 Setting Sea Surface Conditions `[PGOCN]` [7割済 12月]

### 1.3.1 Input from the atmosphere

| variable name | contents                 |
|:--------------|:-------------------------|
| GAUA          | u-wind                   |
| GAVA          | v-wind                   |
| GATA          | temperature T            |
| GAQA          | humidity q               |
| GAPA          | pressure P               |
| GAPS          | surface pressure Ps      |
| GAZS          | surface height           |
| RSFCD         | surface radiation fluxes |
| RCOSZ         | cos(solar angle)         |

If use CHASER, variables below are also needed.

| variable name | contents                                             |
|:--------------|:-----------------------------------------------------|
| EH            | Henry const                                          |
| PFLXC         | precipitation flux (cumulus convection scheme)       |
| PFLXL         | precipitation flux (large scale condensation scheme) |
| LLAT          | latitude                                             |

Practically, precipitation flux from 2 schemes are treated together.


海氷域($L=1$)においては、地表面温度$T_s$は、海氷面温度$T_{ice}$を用いる。ただし、$T_{ice}$が$T_{melt}=0$よりも高い場合は、$T_{melt}$とする。

$$
	T_s = min(T_{ice},T_{melt})
$$

また、海氷底温度$T_b$は、海洋表層水温$T_{o(1)}$とする。

$$
	T_b = T_{o(1)}
$$

海氷量W_{ice}およびその上の積雪量W_{snow}は、$R_{ice}$を考慮して単位面積あたりに換算し、計算に用いる。ただし、リミッター$\epsilon$を設けて、値が小さくなりすぎないようにする。

$$
R_{ice}  =\mathrm{max}( R_{ice,orginal}, \epsilon)
$$


無海氷域($L=2$)においては、地表面温度$T_s$および海氷底温度$T_b$は、海洋表層水温$T_{o(1)}$とする。

$$
	T_s = T_b = T_{o(1)}
$$


また、$L=1,2$いずれのばあいも蒸発係数は$GRBET=1$とする。


海氷密接度$R_{ice}$が与えられない場合は、海氷量$W_{ice}$から簡易的に診断させることもできる。

$$
R_{ice} = \mathrm{min}\Big(\sqrt{\frac{\mathrm{max}(W_{ice},0)}{W_{ice,c}}},1.0\Big)
$$

標準では面積あたりの海氷量を$W_{ice,c}=300 \mathrm{[kg/m^2]}$として与える。


### 1.3.2 Ocean Surface Conditions `[OCNBCS]`

#### 1.3.2.1 Albedo

##### 1.3.2.1.1 Sea Surface Albedo `[SEAALB]`

海水面アルベド$\alpha_{(d,b)}$について、$b=1,2,3$ はそれぞれ可視、近赤外、赤外の波長帯を表す。また、$d=1,2$はそれぞれ直達、散乱である。

緯度$\thetaにおける$太陽天頂角$\beta (\theta)$をもちいて、

$$
	AM1 = \mathrm{min}(\mathrm{max(cos}(\beta(\theta)), \mathrm{cos}	(88^\circ)),\mathrm{cos}	(16^\circ))\\
	S=(\mathrm{tan}(57.7^\circ) * AM1 + \mathrm{tan}(-77.9^\circ))*AM1 + \mathrm{tan}(-36.8^\circ)\\
	\alpha_{1,1} = e^S\\
	\alpha_{2,1} = 0.06\\
$$

近赤外$b=2$については、可視と同じアルベドを用いる。

$$
	\alpha_{1,2} =\alpha_{1,1} \\
	\alpha_{2,2} =\alpha_{2,1}
$$

また、赤外$b=3$については、太陽天頂角によらず、一定値を用いる。

##### 1.3.2.1.2 Albedo modification by ice and snow

グリッド平均のアルベドは、海氷密接度$R_{ice}$を考慮して、

$$
	\alpha = \alpha -R_{ice} \alpha_{ice}
$$

$\alpha_{ice}$は標準で$\alpha_{ice,1}=0.5,\alpha_{ice,2}=0.5,\alpha_{ice,3}=0.05$として与えられる。

さらに、積雪の影響を考慮したい。ここで、温度によるアルベド変化を考慮する。積雪温度の閾値として$T_{al,2}=258.15 \mathrm{[K]}$、$T_{al,1}=273.15 \mathrm{[K]}$を標準で設定し、温度変化に対して線形に、雪のアルベドが$\alpha_{snow,1}=0.75$から$\alpha_{snow,2}$まで変化するとする。$0\le \tau \le 1$である係数$\tau_{snow}$を

$$
\tau_{snow} = \frac{T_s - T_{al,1}}{T_{al,2}-T_{al,1}}
$$

として、雪のアルベド$\alpha_{snow}$を更新する。

$$
	\alpha_{snow} = \alpha_{snow,0} + \tau_{snow}(\alpha_{snow,2}-\alpha_{snow,1})
$$

#### 1.3.2.2 Roughness
[1.4節に記載](#13221-sea-surface-roughness-seaz0f)

##### 1.3.2.2.1 Sea Surface Roughness `[SEAZ0F]`



##### 1.3.2.2.2 Roughness modification by ice and snow

#### 1.3.2.3 Sea Surface heat flux

海氷が存在する時($L=1$)、$D_{f,ice}$ (海氷の熱拡散係数), 海氷密度 $\sigma_{ice}$をもちいて、海氷の熱伝導率$k_{ice}^*$を求める。

$$
k_{ice}^* = \frac{D_{f,ice}}{\mathrm{max}(R_{ice}/\sigma_{ice}, \epsilon)}
$$

求めた熱伝導率は、積雪によって変わることを考慮して、$k_{ice}$に修正される。

$$
h_{snow} = \mathrm{min}(
	\mathrm{max}(
	R_{snow}/\sigma_{snow}),\epsilon
		),h_{snow,max}
		)\\
k_{ice} = k_{ice}^* (1-R_{ice}) + \frac{D_{ice}}{1+\| D_{ice}/D_{snow} \cdot h_{snow} \|} R_{ice}
$$

ここで$h_{snow}$は雪の深さ、$R_{snow}$は積雪面積率、$\sigma_{snow}$は雪の密度、$h_{snow,max}$は積雪最大深度、$D_{snow}$は雪の熱拡散係数。

よって、熱伝導フラックスとその微分は、

$$
 G = k_{ice} (T_b - T_s) \\
 \frac{\partial G}{\partial T} = k_{ice}
$$

なお、無海氷面($L=2$)においては、

$$
G=k_{ocn}
$$

としておく。ここで、$k_{ocn}$は海洋表層の熱フラックス。



## 1.4 Surface Flux [8割済 11月]

### 1.4.1 Overview
The surface flux scheme evaluates the physical quantity fluxes between the atmospheric surfaces due to turbulent transport in the boundary layer. The main input data are wind speed ($u, v$),  temperature ($T$), and specific humidity ($q$), and the output data are the vertical fluxes and the differential values (for obtaining implicit solutions) of momentum, heat, and water vapor.

The bulk coefficients are obtained according to [Louis (1979)](./papers/Louis1979_Article_AParametricModelOfVerticalEddy.pdf) and [Louis <span>*et al.*</span>(1982)](./papers/Louis1982_a_short_history_of_the_operational_pbl_parameterization_at_ecmwf.pdf), except for the correction for the difference in roughness between momentum and heat. However, corrections are made to take into account the difference between momentum and heat roughness.

The outline of the calculation procedure is as follows.


1. calculate the roughness including modifications by ice and snow. `MODULE:[SEAZ0F]`
2. Calculate the Richardson number as the stability of the atmosphere. `MODULE:[PSFCL]`
3. calculate the bulk coefficient from Richardson number.  `MODULE:[PSFCL]`
4. calculate the flux and its derivative from the bulk coefficient. `MODULE:[PSFCM]`
5. If necessary, the calculated fluxes are re-calculated after taking into account the roughness effect, the free flow effect, and the wind speed correction.

### 1.4.2 Roughness `[SEA0F]`

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

### 1.4.3 Richardson Number `[PSFCL]`

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

### 1.4.4 Bulk factor `[PSFCL]`

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


### 1.4. Calculation of surface turbulent fluxes `[PSFCM]`

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




## 1.5 Radiation Flux at Sea Surface `[RADSFC]` [7割済 12月]

地表面アルベド$\alpha_{(d,b)}$について、$b=1,2$ はそれぞれ可視、近赤外の波長帯を表す。また、$d=1,2$はそれぞれ直達、散乱である。地表面に入射する下向き短波放射$SW^{\downarrow}$および上向き短波放射$SW^{\uparrow}$について、直達光と散乱光を合わせて

$$
SW^\downarrow = SW^\downarrow_{(1,1)}+SW^\downarrow_{(1,2)}+SW^\downarrow_{(2,1)}+SW^\downarrow_{(2,2)} \\
SW^\uparrow = SW^\downarrow_{(1,1)}\cdot\alpha_{(1,1)}+SW^\downarrow_{(1,2)}\cdot\alpha_{(1,2)}+SW^\downarrow_{(2,1)}\cdot\alpha_{(2,1)}+SW^\downarrow_{(2,2)}\cdot\alpha_{(2,2)}
$$

## 1.6 Surface Heat Balance `[OCNSLV]`　[7割済 12月]
### 1.6.1 Variables

- Modified in this subroutine

| Original | Presentation | Meanings                                         |
|:---------|:-------------|:-------------------------------------------------|
| GDTS     | $T_s$        | skin temperature                                 |
| GFLUXS   | $G$          | soil heat flux(おそらく地表面からの熱フラックス) |
| TFLUXS   | $H$          | flux of T ($H_s$ from [`[PSFCM]`]())             |
| QFLUXS   | $E$          | flux of q ($F_q^P$ from [`[PSFCM]`]())           |

- Outputs

| Original | Presenatation  | Meanings                       |
|:---------|:---------------|:-------------------------------|
| WFLUXS   | $W_{free/ice}$ | latent heat flux from ice/free |
| RFLXLU   | $LW^\uparrow$  | upward long wave               |
| SFLXBL   | $F$            | flux balance                   |

 - Inputs

| Original | Presentation                      | Meanings             |
|:---------|:----------------------------------|:---------------------|
| DTFDS    | $\frac{\partial H}{\partial T_g}$ | dH/dTg               |
| DQFDS    | $\frac{\partial E}{\partial T_g}$ | dE/dTg               |
| DGFDS    | $\frac{\partial G}{\partial T_g}$ | dG/dTg               |
| RFLXSD   | $SW^\downarrow$                   | down. SW rad.        |
| RFLXSU   | $SW^\uparrow$                     | up. SW rad           |
| RFLXLD   | $LW^\downarrow$                   | down. LW rad.        |
| GRALBL   | $\alpha_L$                        | LW albedo (1-emiss.) |
| GRICR    | $R_{ice}$                         | snow/ice ratio       |

- The others

| Original | Presentation                            | Meanings                       |
|:---------|:----------------------------------------|:-------------------------------|
| ESUB     | $l_s$                                   | 昇華潜熱                       |
| EMIS     | $1-\alpha_L$                            | 長波射出率                     |
| STG      | $(1-\alpha_L)\sigma T_s^4 $             | 黒体放射                       |
| DRFDS    | $\frac{\partial R}{\partial T_g}$       | dR/dTg                         |
| SFLUX    | $F^*$                                   | 地表面から射出されるフラックス |
| GSFLUX   | $F^*-G$                                 | 正味の地表面フラックス         |
| GFLUXF   | $G_{free}$                              | 無海氷域における地表フラックス |
| GFLUXI   | $G_{ice}$                               | 海氷域における地表フラックス   |
| DTI      | $\delta T_{ice}$                        | 海氷域における地表面温度変化   |
| EVAPI    | $\delta E_{ice}$                        | 海氷域における潜熱フラックス   |
| SFLXBI   | $\delta H_{ice}$                        | 海氷域における顕熱フラックス   |
| DGSFDS   | $\frac{\partial G}{\partial T_g}$       | dG/dTg (更新後)                |
| DSBDSI   | $\frac{\partial G_{ice}}{\partial T_g}$ | 海氷域における dG/dTg          |

### 1.6.2 Calculating heat Balance

海表面から出るフラックスは、

$$
F^*=H + (1-\alpha_L)\sigma T_s^4 + \alpha_L LW^\uparrow - LW^\downarrow +SW^\uparrow - SW^\downarrow		
$$

正味で海表面に入るフラックスは、

$$
G = H_s - F^*
$$

 地表面フラックスの温度微分項は、
$$
\frac{\partial G}{\partial T_g} = \frac{\partial G}{\partial T_g}+\frac{\partial H}{\partial T_g}+\frac{\partial R}{\partial T_g}
$$

無海氷域では、凝結によって得られた潜熱フラックスを足して、

$$
	G_{free}=F^* + l_cE
$$


一方、海氷域では、

$$
G_{ice} = G - l_s E\\
\frac{\partial G_{ice}}{\partial T_g}=\frac{\partial G}{\partial T_g} + l_s\frac{\partial E}{\partial T_g}
$$

よって、海氷域での地表面温度変化は、

$$
\delta T_{ice} = G_{ice} ( \frac{\partial G_{ice}}{\partial T_g})^{-1}
$$

このとき、潜熱フラックス、顕熱フラックスはそれぞれ

$$
	E_{ice} = E + \frac{\partial E}{\partial T_g} \delta T_{ice}\\
	H_{ice} = E + \frac{\partial H}{\partial T_g} \delta T_{ice}
$$

以上より、地表面温度を更新する。

$$
	T_s = T_s L R_{ice}\delta T_{ice}
$$

また、各フラックスも更新する。

$$
H=H+\frac{\partial H}{\partial T_g} R_{ice} \delta T_{ice}\\
LW^\uparrow=LW^\uparrow + \frac{\partial R}{\partial T_g} R_{ice} \delta T_{ice}\\
E=(1-R_{ice})E + R_{ice}E_{ice}\\
G=(1-R_{ice})G_{free} + R_{ice}G_{ice}\\
W_{free} = (1-R_{ice}) E\\
W_{ice} = R_{ice} E_{ice}\\
F = R_{ice} H_{ice}
$$
