<!-- TOC START min:1 max:5 link:true asterisk:false update:true -->
- [1 Sea Surface Conditions](#1-sea-surface-conditions)
	- [1.1 Overview [済 10月]](#11-overview-済-10月)
	- [1.2 AGCMと陸面/海水面スキーム間での変数の受け渡し `[PGSFC]`[未 1月作業予定]](#12-agcmと陸面海水面スキーム間での変数の受け渡し-pgsfc未-1月作業予定)
	- [1.3 Setting Sea Surface Conditions [7割済 12月]](#13-setting-sea-surface-conditions-7割済-12月)
		- [1.3.1 Input variables from the atmosphere](#131-input-variables-from-the-atmosphere)
		- [1.3.2 Ocean Surface Conditions `[OCNBCS]`](#132-ocean-surface-conditions-ocnbcs)
			- [1.3.2.1 Albedo](#1321-albedo)
			- [1.3.2.2 Roughness](#1322-roughness)
			- [1.3.2.3 Sea Surface heat flux](#1323-sea-surface-heat-flux)
	- [1.4 Surface Flux [8割済 11月]](#14-surface-flux-8割済-11月)
		- [1.4.1 Overview](#141-overview)
			- [1.4.2 Basic Formula for Flux Calculations](#142-basic-formula-for-flux-calculations)
		- [1.4.2 Roughness `[SEA0F]`](#142-roughness-sea0f)
			- [1.4.2.1 variables](#1421-variables)
		- [1.4.3 Richardson Number `[PSFCL]`](#143-richardson-number-psfcl)
		- [1.4.4 Bulk factor `[BLKCOF]`](#144-bulk-factor-blkcof)
		- [1.4. Calculation of surface turbulent fluxes `[PSFCM]`](#14-calculation-of-surface-turbulent-fluxes-psfcm)
	- [1.5 Radiation Flux at Sea Surface `[RADSFC]` [7割済 12月]](#15-radiation-flux-at-sea-surface-radsfc-7割済-12月)
	- [1.6 Surface Heat Balance `[OCNSLV]`　[7割済 12月]](#16-surface-heat-balance-ocnslv7割済-12月)
		- [1.6.1 Variables](#161-variables)
		- [1.6.2 Calculating heat Balance](#162-calculating-heat-balance)
<!-- TOC END -->



# 1 Sea Surface Conditions
地表過程は、大気・地表間の運動量・熱・水フラックスの交換を通して大気下端の境界条件を与える。[CCSR/NIES AGCM]()までは陸面・海面ともに大気物理過程のひとつとして扱われていたが、[MIROC3 (Hasumi and Emori, 2004)]()以降、陸面過程がMATSIROとして独立した。本章では、今(MIROC6)なお大気物理過程の枠組み内で扱われている、海水面過程について記述する。陸面過程については、[ILSの記述](https://github.com/integrated-land-simulator/model_description)を参照されたい。

## 1.1 Overview [済 10月]

`MODULE: [PGSFC]`において、海面については`[OCNFLX]`(`MODULE: [POCEN]`)、陸面についてはMATSIROモデルの`[LNDFLX]` をそれぞれ呼び出している。`[OCNFLX]`では、以下の手順で海表面過程を扱う。

1. 海氷密接度を用いて、海氷域と無海氷域それぞれについての変数を準備する。
2. 表層境界条件を求める。
3. フラックス収支を求める。
4. 海表面での放射収支を求める。
5. (CHASERによるdepositionを求める。)
6. 海表面における熱バランスを解き、表面温度と各フラックスの値を更新する。


本章で取り上げるモジュールは次の4つである。

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

## 1.2 AGCMと陸面/海水面スキーム間での変数の受け渡し `[PGSFC]`[未 1月作業予定]

海面については`OCNFLX`(`MODULE: [POCEN]`)、陸面についてはMATSIROモデルの`LNDFLX` をそれぞれ呼び出している。


[カップラーのセクション](https://github.com/MIROC-DOC/model_description/blob/coupler_iwakiri/draft/AO-coupler.md)とmerge予定。

## 1.3 Setting Sea Surface Conditions [7割済 12月]

### 1.3.1 Input variables from the atmosphere

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

$$
	PFLX = PFLXC + PFLXL
$$



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

- Output variables

| Original | Presentation                      | Meanings          |
|:---------|:----------------------------------|:------------------|
| GRALB    | $\alpha$                          | surface albedo    |
| GRZ0     |                                   | surface roughness |
| GFLUXS   | $G$                               | heat flux         |
| DGFDS    | $\frac{\partial G}{\partial T_s}$ | dG/dTs            |

- Input variables

| Original | Presentation | Meanings         |
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

| Original | Presentation | Meanings      |
|:---------|:-------------|:--------------|
| GRSNR    |              | snow fraction |


#### 1.3.2.1 Albedo

海水面アルベド$\alpha_{(d,b)}$について、$b=1,2,3$ はそれぞれ可視、近赤外、赤外の波長帯を表す。また、$d=1,2$はそれぞれ直達光、散乱光を表す。

1. Sea Surface Albedo for Visible `[SEAALB]`



緯度$\thetaにおける$太陽天頂角$\beta (\theta)$をもちいて、

$$
	A = \mathrm{min}(\mathrm{max(cos}(\beta(\theta)), \mathrm{cos}	(88^\circ)),\mathrm{cos}	(16^\circ))
$$

$$
	S=(\mathrm{tan}(57.7^\circ) * A + \mathrm{tan}(-77.9^\circ))*A + \mathrm{tan}(-36.8^\circ)
$$

$$
	\alpha_{1,1} = e^S
$$

$$
	\alpha_{2,1} = 0.06
$$

2. Sea Surface Albedo for Near-Infrared and Infrared

近赤外$b=2$については、可視と同じアルベドを用いる。

$$
	\alpha_{1,2} =\alpha_{1,1}
$$

$$
	\alpha_{2,2} =\alpha_{2,1}
$$

また、赤外$b=3$については、太陽天頂角によらず、一定値を用いる。

3. Albedo modification by ice

グリッド平均のアルベドは、海氷密接度$R_{ice}$を考慮して、

$$
	\alpha = \alpha -R_{ice} \alpha_{ice}
$$

$\alpha_{ice}$は標準で$\alpha_{ice,1}=0.5,\alpha_{ice,2}=0.5,\alpha_{ice,3}=0.05$として与えられる。

4. Albedo modification by snow


さらに、積雪の影響を考慮したい。ここで、温度によるアルベド変化を考慮する。積雪温度の閾値として$T_{al,2}=258.15 \mathrm{[K]}$、$T_{al,1}=273.15 \mathrm{[K]}$を標準で設定し、温度変化に対して線形に、雪のアルベドが$\alpha_{snow,1}=0.75$から$\alpha_{snow,2}$まで変化するとする。$0\le \tau \le 1$である係数$\tau_{snow}$を

$$
\tau_{snow} = \frac{T_s - T_{al,1}}{T_{al,2}-T_{al,1}}
$$

として、雪のアルベド$\alpha_{snow}$を更新する。

$$
	\alpha_{snow} = \alpha_{snow,0} + \tau_{snow}(\alpha_{snow,2}-\alpha_{snow,1})
$$

#### 1.3.2.2 Roughness
[1.4節に記載](#13221-sea-surface-roughness-seaz0f) - どっちに入れるか

1. Sea Surface Roughness `[SEAZ0F]`

The roughness variation of the sea surface is determined by the friction velocity $u^*$

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
When the sea ice exists ($L=1$),
海氷が存在する時($L=1$)、$D_{f,ice}$ (海氷の熱拡散係数), 海氷密度 $\sigma_{ice}$をもちいて、海氷の熱伝導率$k_{ice}^*$を求める。

$$
k_{ice}^* = \frac{D_{f,ice}}{\mathrm{max}(R_{ice}/\sigma_{ice}, \epsilon)}
$$

2. Conductivity modification by snow


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

3. Calculate flux and its derivative

よって、熱伝導フラックスとその微分は、

$$
 G = k_{ice} (T_b - T_s)
$$

$$
 \frac{\partial G}{\partial T} = k_{ice}
$$

なお、無海氷域($L=2$)においては、

$$
G=k_{ocn}
$$

としておく。ここで、$k_{ocn}$は海洋表層の熱フラックス。



## 1.4 Surface Flux [8割済 11月]


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

| Original | Presentation | Meanings              |
|:---------|:-------------|:----------------------|
| GRZ0M    | $r_{0,M}$    | surface roughness (V) |
| GRZ0H    | $r_{0,H}$    | surface roughness (T) |
| GRZ0E    | $r_{0,E}$    | surface roughness (q) |

- Input variables

| Original | Presentation | Meanings         |
|:---------|:-------------|:-----------------|
| USFC     | $U_0$        | u sfc wind speed |
| VSFC     | $V_0$        | v sfc wind speed |

- Internal variables

| Original | Presentation | Meanings          |
|:---------|:-------------|:------------------|
| USTAR    | $u^*$        | friction velocity |

- Internal parameters

| Original | Presentation | Meanings            | Values |
|:---------|:-------------|:--------------------|-------:|
| Z0M0     | $r_{0,M_0}$  | base                |      0 |
| Z0MR     | $r_{0,M_R}$  | rough factor        |   0.18 |
| Z0MS     | $r_{0,M_S}$  | smooth factor       |   0.11 |
| Z0H0     | $r_{0,H_0}$  | base                | 1.4^-5 |
| Z0HR     | $r_{0,H_R}$  | rough factor        |    0.0 |
| Z0HS     | $r_{0,H_S}$  | smooth factor       |    0.4 |
| Z0E0     | $r_{0,E_0}$  | base                | 1.3^-4 |
| Z0ER     | $r_{0,E_R}$  | rough factor        |    0.0 |
| Z0ES     | $r_{0,E_S}$  | smooth factor       |   0.62 |
| VISAIR   | $\nu$        | kinematic viscosity | 1.5^-5 |
| CM0      | $C_{M_0}$    | bulk coef for $u^*$ | 1.0^-3 |
| USTRMN   |              | min(u*)             | 1.0^-3 |
| Z0MMIN   |              | minimum             | 3.0^-5 |
| Z0HMIN   |              | minimum             | 3.0^-5 |
| Z0EMIN   |              | minimum             | 3.0^-5 |

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


| Original | Presentation | Meanings  |
|:---------|:-------------|:----------|
| UFLUXS   |              | flux of U |
| VFLUXS   |              | flux of V |
| TFLUXS   |              | flux of T |
| QFLUXS   |              | flux of q |

- Output variables


| Original | Presentation | Meanings        |
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

| Original | Presentation | Meanings                 |
|:---------|:-------------|:-------------------------|
| GDUA     |              | westerly u               |
| GDVA     |              | southern wind v          |
| GDTA     |              | temperature T            |
| GDQA     |              | humidity q               |
| GDPA     |              | pressure (lev=1)         |
| GDPS     |              | surface pressure         |
| GDTS     |              | surface skin temperature |
| GRZ0     |              | surface roughness        |
| GRBET    |              | soil wetness             |
| GRUA     |              | ocean u                  |
| GRVA     |              | ocean v                  |


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




## 1.5 Radiation Flux at Sea Surface `[RADSFC]` [7割済 12月]

地表面アルベド$\alpha_{(d,b)}$について、$b=1,2$はそれぞれ可視、近赤外の波長帯を表す。また、$d=1,2$はそれぞれ直達、散乱である。地表面に入射する下向き短波放射$SW^\downarrow$および上向き短波放射$SW^\uparrow$について、直達光と散乱光を合わせて

$$
	SW^\downarrow = SW^\downarrow_{(1,1)}+SW^\downarrow_{(1,2)}+SW^\downarrow_{(2,1)}+SW^\downarrow_{(2,2)}
$$

$$
SW^\uparrow = SW^\downarrow_{(1,1)}\cdot\alpha_{(1,1)}+SW^\downarrow_{(1,2)}\cdot\alpha_{(1,2)}+SW^\downarrow_{(2,1)}\cdot\alpha_{(2,1)}+SW^\downarrow_{(2,2)}\cdot\alpha_{(2,2)}
$$

## 1.6 Surface Heat Balance `[OCNSLV]`　[7割済 12月]
### 1.6.1 Variables

- Modified in this subroutine

| Header0               | name in the texts | name in the program | dimension | unit |
|:----------------------|:------------------|:--------------------|:----------|:-----|
| skin temperature      | $T_s$             | GDTS                | IJLSDM    |      |
| surface heat flux \*1 | $G$               | GFLUXS              | IJLSDM    |      |
| flux of T             | $H$               | TFLUXS              | IJLSDM    |      |
| flux of q             | $E$               | QFLUXS              | IJLDSM    |      |

- Outputs


| Header0                | name in the texts | name in the program | dimension | unit |
|:-----------------------|:------------------|:--------------------|:----------|:-----|
| surface water flux \*1 | $W_{free/ice}$    | WFLUXS              | IJLSDM,2  |      |
| upward long wave       | $LW^\uparrow$     | RFLXLU              | IJLSDM    |      |
| flux balance           | $F$               | SFLXBL              | IJLSDM    |      |

	- \*1 コメントアウトには*soil*とかかれているが、陸面スキームから流用したプログラムのためであり、特に意味はない。


 - Inputs


 | Header0                             | name in the texts                 | name in the program |
 |:------------------------------------|:----------------------------------|:--------------------|
 | dH/dTs                              | $\frac{\partial H}{\partial T_s}$ | DTFDS               |
 | dE/dTs                              | $\frac{\partial E}{\partial T_s}$ | DQFDS               |
 | dG/dTs                              | $\frac{\partial G}{\partial T_s}$ | DGFDS               |
 | downward SW radiation               | $SW^\downarrow$                   | RFLXSD              |
 | upward SW radiation                 | $SW^\uparrow$                     | RFLXLU              |
 | downward LW radiation               | $LW^\downarrow$                   | RFLXLD              |
 | lake surface LW albedo (1-emission) | $\alpha_L$                        | GRALBL              |
 | snow/ice ration                     | $R_ice$                           | GRICR               |

  - note: コメントアウトには添字の*g*が使われているが、陸面スキームから流用したプログラムのためであり、特に意味はない。

- The others


| Header0                        | name in the texts                       | name in the program | dimension |
|:-------------------------------|:----------------------------------------|:--------------------|:----------|
| 昇華潜熱                       | $l_s$                                   | ESUB                |           |
| emissivity of the lake surface | $\epsilon_L$                            | EMIS                |           |
| black body radiation           | $(1-\alpha_L)\sigma T_s^4 $             | STG                 |           |
| dR/dTs                         | $\frac{\partial R}{\partial T_s}$       | DRFDS               |           |
| 地表面から射出されるフラックス | $F^*$                                   | SFLUX               |           |
| 正味の地表面フラックス         | $F^*-G$                                 | GSFLUX              |           |
| dG/dTs (更新後)                | $\frac{dG_s}{dT_s}$                     | DGSFDS              |           |
| 無海氷域における地表フラックス | $G_{free}$                              | GFLUXF              |           |
| 海氷域における顕熱フラックス   | $\delta H_{ice}$                        | SFLUXBI             |           |
| 海氷域における dG/dTs          | $\frac{\partial G_{ice}}{\partial T_s}$ | DSBDSI              |           |
| 海氷域における地表面温度変化   | $\delta T_{ice}$                        | DTI                 |           |
| 海氷域における潜熱フラックス   | $\delta E_{ice}$                        | EVAPI               |           |
| 海氷域における地表フラックス   | $G_{ice}$                               | GFLUXI              |           |
| sea ice free fraction          | $1-R_{ice}$                             | FF                  |           |
| sea ice fraction               | $R_{ice}$                               | FI                  |           |
|                                | $R_{ice}\delta T_{ice}$                 | DTX                 |           |

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
	\frac{\partial G}{\partial T_s} = \frac{\partial G}{\partial T_s}+\frac{\partial H}{\partial T_s}+\frac{\partial R}{\partial T_s}
$$

無海氷域($L=2$)では、凝結によって得られた潜熱フラックスを足して、

$$
	G_{free}=F^* + l_cE
$$


一方、海氷域($L=1$)では、

$$
	G_{ice} = G - l_s E
$$

$$
	\frac{\partial G_{ice}}{\partial T_s}=\frac{\partial G}{\partial T_s} + l_s\frac{\partial E}{\partial T_s}
$$

よって、地表面温度変化は、

$$
	\delta T_{ice} = G_{ice} ( \frac{\partial G_{ice}}{\partial T_s})^{-1}
$$

このとき、潜熱フラックス、顕熱フラックスはそれぞれ

$$
	E_{ice} = E + \frac{\partial E}{\partial T_s} \delta T_{ice}
$$

$$
	H_{ice} = E + \frac{\partial H}{\partial T_s} \delta T_{ice}
$$

以上より、地表面温度を更新する。

$$
	T_s = T_s +R_{ice}\delta T_{ice}
$$

また、各フラックスも更新する。

$$
	H=H+\frac{\partial H}{\partial T_s} R_{ice} \delta T_{ice}
$$

$$
	LW^\uparrow=LW^\uparrow + \frac{\partial R}{\partial T_s} R_{ice} \delta T_{ice}
$$

$$
	E=(1-R_{ice})E + R_{ice}E_{ice}
$$

$$
	G=(1-R_{ice})G_{free} + R_{ice}G_{ice}
$$

$$
	W_{free} = (1-R_{ice}) E
$$

$$
	W_{ice} = R_{ice} E_{ice}
$$

$$
	F = R_{ice} H_{ice}
$$
