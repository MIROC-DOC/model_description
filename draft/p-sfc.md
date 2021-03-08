<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0

- [Surface Flux](#surface-flux)
- [Sea surface flux `[OCNFLX]`](#sea-surface-flux-ocnflx)
	- [Sea Surface Conditions `[OCNBCS]`](#sea-surface-conditions-ocnbcs)
		- [Sea Surface Albedo for Visible `[SEAALB]`](#sea-surface-albedo-for-visible-seaalb)
		- [Sea Surface Roughness `[SEAZ0F]`](#sea-surface-roughness-seaz0f)
	- [Sea Surface Flux `[SFCFLX]`](#sea-surface-flux-sfcflx)
		- [Bulk factor `[BLKCOF]`](#bulk-factor-blkcof)
	- [Radiation Flux at Sea Surface `[RADSFC]`](#radiation-flux-at-sea-surface-radsfc)
	- [Sea Surface Heat Balance `[OCNSLV]`](#sea-surface-heat-balance-ocnslv)
/TOC -->


# Surface Flux

Until [CCSR/NIES AGCM (1997)](https://github.com/MIROC-DOC/model_description/blob/master/org/AGCM5.6-Tech.pdf), both land surface and sea surface were treated as one of the atmospheric physical processes, but after MIROC3 ([Hasumi and Emori, 2004](https://ccsr.aori.u-tokyo.ac.jp/~hasumi/miroc_description.pdf)), land surface processes became independent as MATSIRO. However, since MIROC3 ([Hasumi and Emori, 2004](https://ccsr.aori.u-tokyo.ac.jp/~hasumi/miroc_description.pdf)), land surface processes have been separated into MATSIRO ([Takata et al., 2003](https://www.sciencedirect.com/science/article/pii/S0921818103000304); [Nitta et al., 2014](https://journals.ametsoc.org/doi/pdf/10.1175/JCLI-D-13-00310.1)). In `SUBROUTINE:[SURFCE]` in pgsfc.F, `ENTRY:[OCNFLX]` (in `SUBROUTINE:[OCEAN]` of pgocn.F) is called for the sea surface, and `ENTRY:[LNDFLX]` (in `SUBROUTINE:[MATSIRO]` of matdrv.F) is called for the land surface, respectively. This chapter describes sea surface processes, which are still treated within the framework of atmospheric physical processes in MIROC6 ([Tatebe et al., 2019](https://www.geosci-model-dev.net/12/2727/2019/gmd-12-2727-2019.pdf))). For the land surface processes, please refer to [Description of ILS](https://github.com/integrated-land-simulator/model_description).

No progostic variables are used in this scheme.

<!--
- Inputs

| Meaning                                     | Presentation  | Variable | dimension         | unit    |
|:--------------------------------------------|:--------------|:---------|:------------------|:--------|
| surface downward radiation                  |               | RFSFCD   | IJSDIM, NRALB     |         |
| cos(solar zenith)                           | $cos(\theta)$ | RCOSZ    | IJSDIM            | [-]     |
| rainfall (cumulus convection scheme)        |               | GPRCC    | IJSDIM, NTR       |         |
| rainfall (Large scale condensation scheme)  |               | GPRCL    | IJSDIM, NTR       |         |
| snowfall (cumulus convection scheme)        |               | GSNWC    | IJSDIM, NTR       |         |
| snowfall (cLarge scale condensation scheme) |               | GSNWL    | IJSDIM, NTR       |         |
| u wind                                      | $u$           | GDU      | IJSDIM, KMAX      | [m/s]   |
| v wind                                      | $v$           | GDV      | IJSDIM, KMAX      | [m/s]   |
| temperature                                 | $T$           | GDT      | IJSDIM, KMAX      | [K]     |
| humidity                                    | $q$           | GDQ      | IJSDIM, KMAX, NTR | [kg/kg] |
| pressure                                    | $P$           | GDP      | IJSDIM, KMAX+1    |         |
| pressure (half level)                       |               | GDPM     | IJSDIM, KMAX+1    |         |
| altitude (half level)                       |               | GDZM     | IJSDIM, KMAX+1    |         |
| time                                        |               | TIME     |                   |         |
| dt for implicit                             |               | DELTP    |                   |         |
| time step (interval)                        |               | DELTI    |                   |         |

The only 1st layer is practically handed to the surface schemes.
-->

# Sea surface flux `[OCNFLX]`

Sea surface processes provide the boundary conditions at the lower end of the atmosphere through the exchange of momentum, heat, and water fluxes between the atmosphere and the surface. In `ENTRY:[OCNFLX]`, the following procedure is used to deal with sea surface processes.

1. prepare variables for sea ice extent and no ice extent, respectively, using sea ice concentration.
2. Determine the surface boundary conditions.
3. Calculate the flux balance.
4. Calculate the radiation budget at the sea surface.
5. Calculate the deposition by CHASER.
6. solve the heat balance at the sea surface and update the skin temperature and each flux value.

<!--
| Meaning                                        | Presentation  | Variable | dimension | unit    |
|:-----------------------------------------------|:--------------|:---------|:----------|:--------|
| u wind of the 1st layer of the atmosphere      | $u_a$         | GAUA     | IJOSDM    | [m/s]   |
| v wind of the 1st layer of the atmosphere      | $v_a$         | GAVA     | IJOSDM    | [m/s]   |
| temperature of the 1st layer of the atmosphere | $T_a$         | GATA     | IJOSDM    | [K]     |
| humidity of the 1st layer of the atmosphere    | $q_a$         | GAQA     | IJOSDM    | [kg/kg] |
| pressure of the 1st layer of the atmosphere    | $P_a$         | GAPA     | IJOSDM    |         |
| surface pressure Ps                            | $P_s$         | GAPS     | IJOSDM    |         |
| surface height                                 |               | GAZS     | IJOSDM    |         |
| surface radiation fluxes                       |               | RSFCD    | IJOSDM    |         |
| cos(solar zenith)                              | $cos(\theta)$ | RCOSZ    | IJOSDM    | [-]     |

If use CHASER, variables below are also needed.

| Meaning                                              | Presentation | Variable | dimension | unit |
|:-----------------------------------------------------|:-------------|:---------|:----------|:-----|
| Henry const                                          |              | EH       | IJOSDM    |      |
| precipitation flux (cumulus convection scheme)       | $Pr_c$       | PFLXC    | IJOSDM    |      |
| precipitation flux (large scale condensation scheme) | $Pr_l$       | PFLXL    | IJOSDM    |      |
| latitude                                             |              | LLAT     | IJOSDM    |      |
-->

Practically, precipitation flux from 2 schemes are treated together.

$$
	Pr = Pr_c + Pr_l
$$

In the sea ice area ($L=1$), the skin temperature ($T_s$) is the sea ice skin temperature ($T_{ice}$). However, if $T_{ice}$ is higher than $T_{melt}=0$, then $T_{melt}$ is used.

$$
	T_s = min(T_{ice},T_{melt})
$$

The sea ice bottom temperature $T_b$ is assumed to be the sea skin temperature ($T_{o(1)}$).

$$
	T_b = T_{o(1)}
$$

The amount of sea ice ($W_{ice}$) and the amount of snow on it ($W_{snow}$) are converted per unit area by considering $R_{ice}$ and used in the calculation. However, a limiter ($\epsilon$) is provided to prevent the values from becoming too small.

$$
R_{ice} =\mathrm{max}( R_{ice,orginal}, \epsilon)
$$

In the ice-free region ($L=2$), the skin temperature ($T_s$) and sea ice bottom temperature ($T_b$) are assumed to be the sea temperature temperature ($T_{o(1)}$).

$$
	T_s = T_b = T_{o(1)}
$$

The evaporation efficiency ise set to 1 for both $L=1, 2$.

If the sea ice concentration ($R_{ice}$) is not given, it can be diagnosed simply from the sea ice volume ($W_{ice}$) in `ENTRY:[OCNICR]` (in `SUBROUTINE:[OCNICR]` of pgocn.F).

$$
R_{ice} = \mathrm{min}\Big(\sqrt{\frac{\mathrm{max}(W_{ice},0)}{W_{ice,c}}},1.0\Big)
$$

The standard gives the amount of sea ice per area as $W_{ice,c}=300 \mathrm{[kg/m^2]}$.


## Sea Surface Conditions `[OCNBCS]`

<!--
- Output variables

| Meaning                    | Presentation                    | Variable | dimension            | unit |
|:---------------------------|:--------------------------------|:---------|:---------------------|:-----|
| surface albedo             | $\alpha$                        | GRALB    | IJLODM, NRDIR, NRBND | --   |
| surface roughness          | $r_0$                           | GRZ0     | IJLODM, NTYZ0        | --   |
| heat flux                  | $G$                             | FOGFLX   | IJLODM               | --   |
| heat diffusion coefficient | $\frac{\partial G}{\partial T}$ | DGFDS    | IJLODM               | --   |

- Input variables

| Meaning                                   | Presentation           | Variable | dimension | unit                |
|:------------------------------------------|:-----------------------|:---------|:----------|:--------------------|
| skin temperature                          | $T_s$                  | GRTS     | IJLODM    | $\mathrm{[K]}$      |
| ice base temperature                      | $T_b$                  | GRTB     | IJLODM    | $\mathrm{[K]}$      |
| lake ice amount                           | $Ic$                   | GRICE    | IJLODM    | $\mathrm{[kg/m^2]}$ |
| snow amount                               | $Sn$                   | GRSNW    | IJLODM    |                     |
| ice concentration                         | $R_{ice}$              | GRICR    | IJLODM    | [-]                 |
| u wind of the 1st layer of the atmosphere | $u_a$                  | GDUA     | IJLODM    | $\mathrm{[m/s]}$    |
| v wind of the 1st layer of the atmosphere | $v_a$                  | GDVA     | IJLODM    | $\mathrm{[m/s]}$    |
| cos(solar zenith)                         | $\mathrm{cos}(\theta)$ | RCOSZ    | IJLODM    | [-]                 |
-->


In `ENTRY[OCNBCS]` (in `SUBROUTINE:[OCNSUB]` of pgocn.F), surface albedo and roughness are calculated. They are calculated supposing ice-free conditions, then modified.

First, let us consider the sea albedo. The sea level $\alpha_{(d,b)}$, $b=1,2,3$ represent the visible, near-infrared, and infrared wavelength bands, respectively. Also, $d=1,2$ represents direct and scattered light, respectively.  The albedo for the visible bands are calculated in `SUBROUTINE [SEAALB]` (of pgocn.F), supposing ice-free conditions.  The albedo for near-infrared is set to same as the visible one. The albedo for infrared is uniformly set to a constant value.

The grid-averaged albedo, taking into account the sea ice concentration ($R_{ice}$), is

$$
	\alpha = \alpha -R_{ice} \alpha_{ice}
$$

$\alpha_{ice}$ is given by the standard as $\alpha_{ice,1}=0.5,\alpha_{ice,2}=0.5,\alpha_{ice,3}=0.05$, respectively.

In addition, we want to consider the effect of snow cover. Here, we consider the albedo modification by temperature. The standard threshold values for snow temperature are $T_{al,2}=258.15 \mathrm{[K]}$ and $T_{al,1}=273.15 \mathrm{[K]}$. The snow albedo changes linearly with temperature change from $\alpha_{snow,1}=0.75$ to $\alpha_{ snow,2}$. Let the coefficient $\tau_{snow}$, which is $0\le \tau \le 1$.

$$
\tau_{snow} = \frac{T_s - T_{al,1}}{T_{al,2}-T_{al,1}}
$$

Update the snow albedo ($\alpha_{snow}$) as

$$
	\alpha_{snow} = \alpha_{snow,0} + \tau_{snow}(\alpha_{snow,2}-\alpha_{snow,1})
$$

Second, let us consider the sea surface roughness. The roughnesses of for momentum, heat and vapor are calculated in `SUBROUTINE:[SEAZ0F]` (of pgocn.F), supposing the ice-free conditions.

When the sea ice exists ($L=1$),  each roughness is modified to take into account the sea concentration ($R_{ice}$),

$$
	z_{0,M} = z_{0,M} + ( z_{0,ice,M} - z_{0,M})  R_{ice}
$$

$$
	z_{0,H} = z_{0,H} + ( z_{0,ice,H} - z_{0,H})  R_{ice}
$$

$$
	z_{0,E} = z_{0,E} + ( z_{0,ice,E} - z_{0,E})  R_{ice}
$$

where, $r_{0,ice,*}$ is the roughness of sea ice for momentum, heat and vapor, respectively.

$$
	z_{0,M} = z_{0,M} + ( z_{0,snow,M} - z_{0,M})  R_{snow}
$$

$$
	z_{0,H} = z_{0,H} + ( z_{0,snow,H} - z_{0,H})  R_{snow}
$$

$$
	z_{0,E} = z_{0,E} + ( z_{0,snow,E} - z_{0,E})  R_{snow}
$$

where, $r_{0,snow,*}$ is the roughness of snow ice for momentum, heat and vapor, respectively.

Third, let us consider the conductivity of ice.

When sea ice exists ($L=1$), the thermal conductivity $k_{ice}^\star$ of sea ice is obtained by

$$
k_{ice}^\star = \frac{D_{f,ice}}{\mathrm{max}(R_{ice}/\sigma_{ice}, \epsilon)}
$$

where $D_{f,ice}$ is the thermal diffusivity of sea ice, and $\sigma_{ice}$ sea ice density, respectively.

The calculated thermal conductivity is modified to $k_{ice}$ to take into account that it varies with snow cover.

$$
h_{snow} = \mathrm{min}(
	\mathrm{max}(
	R_{snow}/\sigma_{snow}),\epsilon
		),h_{snow,max}
		)
$$

$$		
k_{ice} = k_{ice}^\star (1-R_{ice}) + \frac{D_{ice}}{1+\| D_{ice}/D_{snow} \cdot h_{snow} \|} R_{ice}
$$

where $h_{snow}$ is the snow depth, $R_{snow}$ is the snow area fraction, $\sigma_{snow}$ is the snow density, $h_{snow,max}$ is the maximum snow depth, and $D_{snow}$ is the thermal diffusivity of snow, respectively.

Therefore, the heat conduction flux and its derivative are

$$
 G = k_{ice} (T_b - T_s)
$$

$$
 \frac{\partial G}{\partial T} = k_{ice}
$$

Note that in the ice-free region ($L=2$)

$$
G=k_{ocn}
$$

where $k_{ocn}$ is the heat flux in the sea temperature layer, and $k_{ocn}$ is the heat flux in the sea temperature layer, respectively.

### Sea Surface Albedo for Visible `[SEAALB]`

In `SUBROUTINE [SEAALB]` (of pgocn.F), the albedo for the visible bands are calculated supposing ice-free conditions.
<!--
- Inputs

| Meaning           | Presentation  | Variable | dimension | unit |
|:------------------|:--------------|:---------|:----------|:-----|
| cos(solar zenith) | $cos(\theta)$ | COSZ     | IJLODM    | [-]  |

- Outputs

| Meaning                              | Presentation    | Variable | dimension | unit |
|:-------------------------------------|:----------------|:---------|:----------|:-----|
| sea surface albedo (direct, diffuse) | $\alpha_{L(d)}$ | GALB     | IJLODM ,2 | [-]  |
-->

For sea surface level albedo $\alpha_{L(d)}$, $d=1,2$ represents direct and scattered light, respectively.

Using the solar zenith angle at latitude $\zeta$, the albedo for direct light is presented by

$$
	\alpha_{L(1)} = e^{(C_3A^* + C_2) A^* +C_1}
$$

where

$$
	A = \mathrm{min}(\mathrm{max}(\mathrm{cos}(\theta),0.03459),0.961)
$$

On the other hand, the albedo for scattered light is uniformly set to a constant parameter.

$$
	\alpha_{L(2)} = 0.06
$$

### Sea Surface Roughness `[SEAZ0F]`

In `SUBROUTINE:[SEAZ0F]` (of pgocn.F), the roughnesses of for momentum, heat and vapor are calculated supposing the ice-free conditions. calculated, according to [Miller et al. (1992)](https://journals.ametsoc.org/view/journals/clim/5/5/1520-0442_1992_005_0418_tsotem_2_0_co_2.xml).

<!--
- Outputs

| Meaning                        | Presentation | Variable | dimension | unit |
|:-------------------------------|:-------------|:---------|:----------|:-----|
| surface roughness for momentum | $z_{0,M}$    | GRZ0M    | IJLODM    | --   |
| surface roughness for heat     | $z_{0,H}$    | GRZ0H    | IJLODM    | --   |
| surface roughness for vapor    | $z_{0,E}$    | GRZ0E    | IJLSDIM   | --   |

- Inputs

| Meaning                                   | Presentation | Variable | dimension | unit  |
|:------------------------------------------|:-------------|:---------|:----------|:------|
| u wind of the 1st layer of the atmosphere | $u_a$        | GDUA     | IJLODM    | [m/s] |
| v wind of the 1st layer of the atmosphere | $v_a$        | GDVA     | IJLODM    | [m/s] |
-->

The roughness variation of the sea surface is determined by the friction velocity $u^\star$.

$$
u^{\star} = \sqrt{C_{M_0} ({u_a}^2  +{v_a}^2)}
$$

where $u_a,v_a$ are the zonal and vertical winds of the 1st layer of the atmosphere.


We perform successive approximation calculation of ${C_{M_0}}$, because $F_u,F_v,F_\theta,F_q$ are required.

$$
	z_{0,M} = z_{0,M_0} + z_{0,M_R} + \frac{z_{0,M_R} {u^\star }^2 }{g} + \frac{z_{0,M_S}\nu }{u^\star}
$$

$$
	z_{0,H} = z_{0,H_0} + z_{0,H_R} + \frac{z_{0,H_R} {u^\star }^2 }{g} + \frac{z_{0,H_S}\nu }{u^\star}
$$

$$
	z_{0,E} = z_{0,E_0} + z_{0,E_R} + \frac{z_{0,E_R} {u^\star }^2 }{g} + \frac{z_{0,E_S}\nu }{u^\star}
$$

where, $\nu = 1.5 \times 10^{-5} \mathrm{[m^2/s]}$ is the kinetic viscosity of the atmosphere,
$z_{0,M},z_{0,H}$ and $z_{0,E}$ are surface roughness for momentum, heat, and vapor, $z_{0,M_0},z_{0,H_0}$ and $z_{0,E_0}$ are base, and rough factor ($z_{0,M_R},z_{0,M_R}$ and $z_{0,E_R}$), and smooth factor ($z_{0,M_S},z_{0,M_S}$ and $z_{0,E_S}$), respectively.


## Sea Surface Flux `[SFCFLX]`

Treatment of sea surface flux is basically the same with [CCSR/NIES AGCM (1997)](https://github.com/MIROC-DOC/model_description/blob/master/org/AGCM5.6-Tech.pdf). The surface flux scheme evaluates the physical quantity fluxes between the atmospheric surfaces due to turbulent transport in the boundary layer. The main input are wind speed ($u_a, v_a$),  temperature ($T_a$), and specific humidity ($q_s$) from the 1st layer of the atmosphere. The output are the vertical fluxes and the differential values (for obtaining implicit solutions) of momentum, heat, and water vapor.

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
	F_q^P =  \rho C_E |{\mathbf{v}}| ( q_g - q_a )
$$

Note that $F_q^P$ is the possible evaporation flux.

The turbulent fluxes at the sea surface are solved by bulk formulae as follows. Then, by solving the surface energy balance, the ground skin temperature ($T_s$) is updated, and the surface flux values with respect to those values are also updated. The solutions obtained here are temporary values. In order to solve the energy balance by linearizing with respect to $T_s$, the differential with respect to $T_s$ of each flux is calculated beforehand.

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
\hat{F}q^P_{1/2} = \rho_{1/2} C_E |{\mathbf{v}}_1| \left( q^\star(T_0) - q_1 \right)
$$


### Bulk factor `[BLKCOF]`

In `SUBROUTINE:[BLKCOF]` (of psfcl.F), the bulk factors are calculated. The bulk Richardson number ($R_{iB}$), which is used as a benchmark for the stability between the atmospheric surfaces, is

$$
R_{iB} =
			\frac{ \frac{g}{\theta_s} (\theta_1 - \theta(z_0))/z_1 }
              { (u_1/z_1)^2                                  }
       = \frac{g}{\theta_s}
         \frac{T_1 (p_s/p_1)^\kappa - T_0 }{u_1^2/z_1} f_T
$$


Here, $g$ is the gravitational accerelation\, $\theta_s$ ($\Theta_0$ in MATSIRO description) is the basic potential temperature, $T_1$ is the atmospheric temperature of the 1st layer, $T_0$ is the surface skin temperature, $p_s$ is the surface pressure, $p_1$ is the pressure of the 1st layer, $\kappa$ is the Karman constant, and

$$
f_T = (\theta_1 - \theta(z_0))/(\theta_1 - \theta_0)
$$

The bulk coefficients of $C_M,C_H,C_E$ are calculated according to [Louis (1979)](https://link.springer.com/content/pdf/10.1007/BF00117978.pdf) and [Louis <span>*et al.*</span>(1982)](https://www.ecmwf.int/en/elibrary/10845-short-history-pbl-parameterization-ecmwf). However, corrections are made to take into account the difference between momentum and heat roughness. If the roughnesses for momentum, heat, and water vapor are set to $z_{0,M}, z_{0,H}, z_{0,E}$, respectively, the results are generally $z_{0,M} > z_{0,H}, z_{0,E}$, but the bulk coefficients for heat and water vapor for the fluxes from the height of $z_{0,M}$ are also set to $\widetilde{C_H}$, $\widetilde{C_E}$, then corrected.

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

is a correction factor, which is approximated from the uncorrected bulk Richardson number, but we abbreviate the calculation here.


## Radiation Flux at Sea Surface `[RADSFC]`

In `SUBROUTINE:[RADSFC]` (of pgsfc.F), the radiation flux at sea surface is calculated. For the ground surface albedo $\alpha_{(d,b)}$, $b=1,2$ represent the visible and near-infrared wavelength bands, respectively. Also, $d=1,2$ are direct and scattered, respectively. For the downward shortwave radiation $SW^\downarrow$ and upward shortwave radiation $SW^\uparrow$ incident on the earth's surface, the direct and scattered light together are

$$
	SW^\downarrow = SW^\downarrow_{(1,1)}+SW^\downarrow_{(1,2)}+SW^\downarrow_{(2,1)}+SW^\downarrow_{(2,2)} \\
SW^\uparrow = SW^\downarrow_{(1,1)}\cdot\alpha_{(1,1)}+SW^\downarrow_{(1,2)}\cdot\alpha_{(1,2)}+SW^\downarrow_{(2,1)}\cdot\alpha_{(2,1)}+SW^\downarrow_{(2,2)}\cdot\alpha_{(2,2)}
$$

## Sea Surface Heat Balance `[OCNSLV]`

<!--
The comments for some variables say "soil", but this is because the program was adapted from a land surface scheme, and has no particular meaning.

- Outputs

| Meaning            | Presentation   | Variable | dimension | unit |
|:-------------------|:---------------|:---------|:----------|:-----|
| surface water flux | $W_{free/ice}$ | WFLUXS   | IJLODM,2  | --   |
| upward long wave   | $LW^\uparrow$  | RFLXLU   | IJLODM    | --   |
| flux balance       | $F$            | SFLXBL   | IJLODM    | --   |


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
| skin temperature               | $T_s$        | GDTS     | IJLODM    | --   |
| surface heat flux from `seaBC` | $G$          | GFLUXS   | IJLODM    | --   |
| sensible heat flux             | $H$          | TFLUXS   | IJLODM    | --   |
| latent heat flux               | $E$          | QFLUXS   | IJLDSM    | --   |

- Others (appeared in texts)

| Meaning                                               | Presentation | Variable | dimension | unit |
|:------------------------------------------------------|:-------------|:---------|:----------|:-----|
| sea surface albedo for shortwave radiation (ice-free) | $\alpha_S$   | --       | [-]       | --   |
| the Stefan-Boltzmann constant                         | $\sigma$     | STB      | --        | --   |
-->

In `SUBROUTINE:[OCNSLV]` (of pgocn.F), the heat balance at the sea surface is solved. Downward radiative fluxes are not directly dependent on the condition of the sea surface, and their observed values are simply specified to drive the model ([Hasumi, 2015](https://ccsr.aori.u-tokyo.ac.jp/~hasumi/COCO/coco4.pdf)). Shortwave emission from the sea surface is negligible, so the upward part of the shortwave radiative flux is accounted for solely by reflection of the incoming downward flux. Let $\alpha _S$ be the sea surface albedo for shortwave radiation. The upward shortwave radiative flux is represented by

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

The heat flux into the sea surface is presented, with the surface heat flux calculated in `SUBROUTINE:[SFCFLX]` (of psfcm.F).

$$
	G^* = G - F^*
$$

Note that $G^*$ is downward positive.

The temperature derivative term is

$$
	\frac{\partial G^*}{\partial T_s} = \frac{\partial G}{\partial T_s}+\frac{\partial H}{\partial T_s}+\frac{\partial R}{\partial T_s}
$$

When the sea ice exists, the sublimation flux ($l_s E$) is considered

$$
	G_{ice} = G^* - l_s E
$$

The temperature derivative term is

$$
	\frac{\partial G_{ice}}{\partial T_s}=\frac{\partial G^*}{\partial T_s} + l_s\frac{\partial E}{\partial T_s}
$$

Finally, we can update the skin temperature with the sea ice concentration with $\Delta T_s=G_{ice} ( \frac{\partial G_{ice}}{\partial T_s})^{-1}$


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
$$
