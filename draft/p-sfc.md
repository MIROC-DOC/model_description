## Surface Flux Scheme (Sea Surface)

Until CCSR/NIES AGCM (1997), both land surface and sea surface were treated as one of the atmospheric physical processes, but after MIROC3 (Hasumi and Emori, 2004), land surface processes became independent as MATSIRO. However, since MIROC3 (Hasumi and Emori, 2004), land surface processes have been separated into MATSIRO (Takata et al., 2003; Nitta et al., 2014). In `SUBROUTINE:[SURFCE]` in pgsfc.F, `ENTRY:[OCNFLX]` (in `SUBROUTINE:[OCEAN]` of pgocn.F) is called for the sea surface, and `ENTRY:[LNDFLX]` (in `SUBROUTINE:[MATSIRO]` of matdrv.F) is called for the land surface, respectively. This chapter describes sea surface processes, which are still treated within the framework of atmospheric physical processes in MIROC6 (Tatebe et al., 2019)). For the land surface processes, please refer to Description of ILS (https://github.com/integrated-land-simulator/model_description).

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

Sea surface processes provide the boundary conditions at the lower end of the atmosphere through the exchange of momentum, heat, and water fluxes between the atmosphere and the surface. In `ENTRY:[OCNFLX]`, the following procedure is used to deal with sea surface processes.

1. prepare variables for sea ice extent and no ice extent, respectively, using sea ice concentration.
2. Determine the surface boundary conditions.
3. Calculate the flux balance.
4. Calculate the radiation budget at the sea surface.
5. Calculate the deposition by CHASER.
6. solve the heat balance at the sea surface and update the skin temperature and each flux value.

No prognostic variables are used in this scheme.
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

where $Pr$ is total precipitation flux, $Pr_c$ is precipitation flux from the cumulus convection scheme, and $Pr_l$ is precipitation flux from the large scale condensation scheme, respectively.

Sea ice covered/free areas are represented by $L=1,2$. Each area is calculated then weighted by  sea ice concentration ($R_{ice}$).

In the sea ice area ($L=1$), the skin temperature ($T_s$) is the sea ice skin temperature ($T_{ice}$). However, if $T_{ice}$ is higher than the melting point ($T_{melt}=273.15 \mathrm{[K]}$), then $T_{melt}$ is used.

$$
	T_s = min(T_{ice},T_{melt})
$$

The sea ice bottom temperature ($T_b$) is assumed to be the sea skin temperature ($T_{o(1)}$).

$$
	T_b = T_{o(1)}
$$

The amount of sea ice ($W_{ice}$) and the amount of snow on it ($W_{snow}$) are converted per unit area by considering sea ice concentration ($R_{ice}$) and used in the calculation. However, a limiter ($\epsilon$) is provided to prevent the values from becoming too small.

$$
R_{ice} =\mathrm{max}( R_{ice,orginal}, \epsilon)
$$

In the ice-free area ($L=2$), the skin temperature ($T_s$) and sea ice bottom temperature ($T_b$) are assumed to be the sea temperature temperature ($T_{o(1)}$).

$$
	T_s = T_b = T_{o(1)}
$$

The evaporation efficiency is set to 1 for both $L=1, 2$.

If sea ice concentration ($R_{ice}$) is not given (as a boundary condition or from an OGCM), it is simply diagnosed with the sea ice volume ($W_{ice}$) in `ENTRY:[OCNICR]` (in `SUBROUTINE:[OCNICR]` of pgocn.F).

$$
R_{ice} = \mathrm{min}\Big(\sqrt{\frac{\mathrm{max}(W_{ice},0)}{W_{ice,c}}},1.0\Big)
$$

The standard gives the amount of sea ice per area as $W_{ice,c}=300 \mathrm{[kg/m^2]}$.


### Boundary Conditions

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

First, let us consider the sea surface level albedo ($\alpha_{(d,b)}$), $b=1,2,3$ represent the visible, near-infrared, and infrared wavelength bands, respectively. Also, $d=1,2$ represents direct and scattered light, respectively.  The albedo for the visible bands are calculated in `SUBROUTINE [SEAALB]` (of pgocn.F), supposing ice-free conditions. The albedo for near-infrared is set to same as the visible one. The albedo for infrared is uniformly set to a constant value.

The grid-averaged albedo, taking into account sea ice concentration ($R_{ice}$), is

$$
	\alpha = \alpha -R_{ice} \alpha_{ice}
$$

$\alpha_{ice}$ is given as $\alpha_{ice,1}=0.5,\alpha_{ice,2}=0.5,\alpha_{ice,3}=0.05$, respectively.

In addition, we want to consider the effect of snow cover. Here, we consider the albedo modification by temperature. Standard threshold values for snow temperature are $T_{al,2}=258.15 \mathrm{[K]}$ and $T_{al,1}=273.15 \mathrm{[K]}$. The snow albedo changes linearly with temperature change from $\alpha_{snow,1}=0.75$ to $\alpha_{ snow,2}$. Let the coefficient $\tau_{snow}$, which is $0\le \tau \le 1$.

$$
\tau_{snow} = \frac{T_s - T_{al,1}}{T_{al,2}-T_{al,1}}
$$

Update the snow albedo ($\alpha_{snow}$) as

$$
	\alpha_{snow} = \alpha_{snow,0} + \tau_{snow}(\alpha_{snow,2}-\alpha_{snow,1})
$$

Second, let us consider sea surface roughnesses. Roughnesses of for momentum, heat and vapor are calculated in `SUBROUTINE:[SEAZ0F]` (of pgocn.F), supposing the ice-free conditions.

When the sea ice exists ($L=1$),  roughnesses of momentum, heat and vapor ($r_{0,M},r_{0,H},r_{0,E}$) is modified to take into account sea ice concentration ($R_{ice}$),

$$
	z_{0,M} = z_{0,M} + ( z_{0,ice,M} - z_{0,M})  R_{ice}
$$

$$
	z_{0,H} = z_{0,H} + ( z_{0,ice,H} - z_{0,H})  R_{ice}
$$

$$
	z_{0,E} = z_{0,E} + ( z_{0,ice,E} - z_{0,E})  R_{ice}
$$

where, $r_{0,ice,M},r_{0,ice,H},r_{0,ice,E}$ is the roughness of sea ice for momentum, heat and vapor, respectively.

$$
	z_{0,M} = z_{0,M} + ( z_{0,snow,M} - z_{0,M})  R_{snow}
$$

$$
	z_{0,H} = z_{0,H} + ( z_{0,snow,H} - z_{0,H})  R_{snow}
$$

$$
	z_{0,E} = z_{0,E} + ( z_{0,snow,E} - z_{0,E})  R_{snow}
$$

where, $r_{0,snow,M},r_{0,snow,H},r_{0,snow,E}$ is the roughness of snow ice for momentum, heat and vapor, respectively.

Third, let us consider conductivity of ice. When sea ice exists ($L=1$), thermal conductivity  of sea ice ($k_{ice}^\star$) is obtained by

$$
k_{ice}^\star = \frac{D_{f,ice}}{\mathrm{max}(R_{ice}/\sigma_{ice}, \epsilon)}
$$

where $D_{f,ice}$ is thermal diffusivity of sea ice, and $\sigma_{ice}$ is sea ice density, respectively.

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

where $h_{snow}$ is snow depth, $R_{snow}$ is snow area fraction, $\sigma_{snow}$ is snow density, $h_{snow,max}$ is maximum snow depth, and $D_{snow}$ is thermal diffusivity of snow, respectively.

Therefore, heat conduction flux and its derivative are

$$
 G = k_{ice} (T_b - T_s)
$$

$$
 \frac{\partial G}{\partial T} = k_{ice}
$$

Note that in the ice-free area ($L=2$)

$$
G=k_{ocn}
$$

where $k_{ocn}$ is heat flux in the sea temperature layer, and $k_{ocn}$ is heat flux in the sea temperature layer, respectively.

#### Albedo for Visible

In `SUBROUTINE [SEAALB]` (of pgocn.F), albedo for the visible bands are calculated supposing ice-free conditions.

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

For sea surface level albedo ($\alpha_{L(d)}$), $d=1,2$ represents direct and scattered light, respectively.

Using the solar zenith angle at latitude $\zeta$, albedo for direct light is presented by

$$
	\alpha_{L(1)} = e^{(C_3A^* + C_2) A^* +C_1}
$$

where

$$
	A = \mathrm{min}(\mathrm{max}(\mathrm{cos}(\theta),0.03459),0.961)
$$

and $C_1,C_2,C_3$ are constant parameters, respectively.

On the other hand, albedo for scattered light ($\alpha_{L(2)}$) is uniformly set to a constant parameter.

$$
	\alpha_{L(2)} = 0.06
$$

#### Roughnesses

In `SUBROUTINE:[SEAZ0F]` (of pgocn.F), the roughnesses of for momentum, heat and vapor are calculated supposing the ice-free conditions. calculated, according to Miller et al. (1992).

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

The roughness variation of the sea surface is determined by the friction velocity ($u^\star$).

$$
u^{\star} = \sqrt{C_{M_0} ({u_a}^2  +{v_a}^2)}
$$

where $C_{M_0}$ is a bulk coefficient for momentum, and $u_a,v_a$ are zonal and vertical winds of the 1st layer of the atmosphere. We perform successive approximation calculation of ${C_{M_0}}$, because $F_u,F_v,F_\theta,F_q$ are required.

Then, roughnesses of sea surface for momentum, heat and vapor are

$$
	z_{0,M} = z_{0,M_0} + z_{0,M_R} + \frac{z_{0,M_R} {u^\star }^2 }{g} + \frac{z_{0,M_S}\nu }{u^\star}
$$

$$
	z_{0,H} = z_{0,H_0} + z_{0,H_R} + \frac{z_{0,H_R} {u^\star }^2 }{g} + \frac{z_{0,H_S}\nu }{u^\star}
$$

$$
	z_{0,E} = z_{0,E_0} + z_{0,E_R} + \frac{z_{0,E_R} {u^\star }^2 }{g} + \frac{z_{0,E_S}\nu }{u^\star}
$$

where, $\nu = 1.5 \times 10^{-5} \mathrm{[m^2/s]}$ is the kinetic viscosity of the atmosphere, $z_{0,M},z_{0,H}$ and $z_{0,E}$ are surface roughness for momentum, heat, and vapor, $z_{0,M_0},z_{0,H_0}$ and $z_{0,E_0}$ are base, and rough factor ($z_{0,M_R},z_{0,M_R}$ and $z_{0,E_R}$), and smooth factor ($z_{0,M_S},z_{0,M_S}$ and $z_{0,E_S}$), respectively.


### Calculation of Momentum, Heat and Water Vapor Fluxes

Treatment of sea surface flux is basically the same with CCSR/NIES AGCM (1997). The surface flux scheme evaluates the physical quantity fluxes between the atmospheric surfaces due to turbulent transport in the boundary layer. The main input are horizontal wind speed ($u_a, v_a$),  temperature ($T_a$), and specific humidity ($q_a$) from the 1st layer of the atmosphere. The output are the vertical fluxes and the differential values (for obtaining implicit solutions) of momentum, heat, and water vapor.

Surface fluxes ($F_u, F_v, F_\theta, F_q$) are expressed using bulk coefficients for momentum, head and vapor ($C_M, C_H, C_E$) as follows

$$
	F_u  =  - \rho C_M |\mathbf{V_a}| u_a
$$

$$
	F_v  =  - \rho C_M |\mathbf{V_a}| v_a
$$

$$
	F_\theta  = \rho c_p C_H |\mathbf{V_a}| ( \theta_s - \theta_a )
$$

$$
	F_q^P =  \rho C_E |\mathbf{V_a}| ( q_s - q_a )
$$

note that $F_q^P$ is the possible evaporation flux, where $\mathbf{V_a}$ is horizontal wind vector, and $\theta_s, \theta_a$ are potential temperature of surface and 1st layer of the atmosphere, respectively.

Turbulent fluxes at the sea surface are solved by bulk formulae as follows. Then, by solving the surface energy balance, the ground skin temperature ($T_s$) is updated, and the surface flux values with respect to those values are also updated. The solutions obtained here are temporary values. In order to solve the energy balance by linearizing with respect to $T_s$, the differential with respect to $T_s$ of each flux is calculated beforehand.

- Momentum flux

$$
 \tau_x = - \rho C_{M}|\mathbf{V_a}| u_a
$$

$$
 \tau_y = - \rho C_{M}|\mathbf{V_a}| v_a
$$


where $\tau_x$ and $\tau_y$  are the momentum fluxes (surface stress) of the zonal and meridional directions, respectively.

- Sensible heat flux

$$
 H_s = c_p \rho C_{Hs}|\mathbf{V_a}| (T_s - (P_s/P_a)^{\kappa}T_a)
$$

where $H_s$ is the sensible heat flux from the sea surface; $\kappa = R_{air} / c_p$ and $R_{air}$ are the gas constants of air, and $c_p$ is the specific heat of air.

- Bare sea surface evaporation flux

$$
	F_q^P = \rho C_E |\mathbf{V_a}| \left( q^{\ast}(T_s) - q_a \right)
$$

#### Bulk factors

In `SUBROUTINE:[BLKCOF]` (of psfcl.F), the bulk factors are calculated. The bulk Richardson number ($R_{iB}$), which is used as a benchmark for the stability between the atmospheric surfaces, is

$$
R_{iB} =
			\frac{ \frac{g}{\theta_s} (\theta_a - \theta(z_0))/z_a }
              { (u_a/z_1)^2                                  }
       = \frac{g}{\theta_s}
         \frac{T_a (p_s/p_a)^\kappa - T_0 }{u_a^2/z_1} f_T
$$


Here, $g$ is the gravitational accerelation\, $\theta_s$ is surface potential temperature, $T_a$ is the atmospheric temperature of the 1st layer, $T_s$ is the surface skin temperature, $p_s$ is the surface pressure, $p_a$ is the pressure of the 1st layer, $\kappa$ is the Karman constant, and

$$
f_T = (\theta_a - \theta(z_0))/(\theta_a - \theta_s)
$$

The bulk coefficients of $C_M,C_H,C_E$ are calculated according to Louis (1979) and Louis et al. (1982) However, corrections are made to take into account the difference between momentum and heat roughness. If the roughnesses for momentum, heat, and water vapor are set to $z_{0,M}, z_{0,H}, z_{0,E}$, respectively, the results are generally $z_{0,M} > z_{0,H}, z_{0,E}$, but the bulk coefficients for heat and water vapor for the fluxes from the height of $z_{0,M}$ are also set to $\widetilde{C_H}$, $\widetilde{C_E}$, then corrected.

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
  f_q = (q_a - q(z_0))/(q_a - q^{\ast}(\theta_0))
$$

but the method of calculation is omitted. The coefficients of Louis factors are $( b_M, d_M, e_M ) = ( 9.4, 7.4, 2.0 )$, $( b_H, d_H, e_H ) = ( b_E, d_E, e_E ) = ( 9.4, 5.3, 2.0 )$.

is a correction factor, which is approximated from the uncorrected bulk Richardson number, but we abbreviate the calculation here.


### Radiation Flux Calculation

In `SUBROUTINE:[RADSFC]` (of pgsfc.F), the radiation flux at sea surface is calculated. For the ground surface albedo ($\alpha_{(d,b)}$), $b=1,2$ represent the visible and near-infrared wavelength bands, respectively. Also, $d=1,2$ are direct and scattered, respectively. For the downward shortwave radiation ($SW^\downarrow$) and upward shortwave radiation ($SW^\uparrow$) incident on the earth's surface, the direct and scattered light together are

$$
	SW^\downarrow = SW^\downarrow_{(1,1)}+SW^\downarrow_{(1,2)}+SW^\downarrow_{(2,1)}+SW^\downarrow_{(2,2)}
$$
$$
SW^\uparrow = SW^\downarrow_{(1,1)}\cdot\alpha_{(1,1)}+SW^\downarrow_{(1,2)}\cdot\alpha_{(1,2)}+SW^\downarrow_{(2,1)}\cdot\alpha_{(2,1)}+SW^\downarrow_{(2,2)}\cdot\alpha_{(2,2)}
$$

### Solving Heat Balance

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

In `SUBROUTINE:[OCNSLV]` (of pgocn.F), heat balance at the sea surface is solved. Downward radiative fluxes are not directly dependent on the condition of the sea surface, and their observed values are simply specified to drive the model (Hasumi, 2015). Shortwave emission from the sea surface is negligible, so the upward part of the shortwave radiative flux is accounted for solely by reflection of the incoming downward flux. Let $\alpha _S$ be the sea surface albedo for shortwave radiation. The upward shortwave radiative flux is represented by

$$
	SW^\uparrow = - \alpha_S SW^\downarrow
$$

On the other hand, the upward longwave radiative flux ($LW^\uparrow$) has both reflection of the incoming flux and emission from the sea surface. Let $\alpha$ be the sea surface albedo for longwave radiation and $\epsilon$ be emissivity of the sea surface relative to the black body radiation, respectively. The upward shortwave radiative flux is represented by

$$
	LW^\uparrow = - \alpha LW^\downarrow + \epsilon \sigma T_s ^4
$$

where $\sigma$ is the Stefan-Boltzmann constant and $T_s$ is skin temperature, respectively
. If sea ice exists ($L=1$), snow or sea ice temperature is considered by fractions. When radiative equilibrium is assumed, emissivity becomes identical to co-albedo:

$$
	\epsilon = 1 - \alpha
$$

The net surface flux ($F^*$) is presented by

$$
	F^*=H + (1-\alpha)\sigma T_s^4 + \alpha LW^\uparrow - LW^\downarrow +SW^\uparrow - SW^\downarrow		
$$

where $H$ is sensible heat flux.

With the surface heat flux calculated in `SUBROUTINE:[SFCFLX]` (of psfcm.F) ($G$), heat flux into the sea surface ($G^*$) is presented as

$$
	G^* = G - F^*
$$

Note that $G^*$ is downward positive.

The temperature derivative term of $G^*$ is

$$
	\frac{\partial G^*}{\partial T_s} = \frac{\partial G}{\partial T_s}+\frac{\partial H}{\partial T_s}+\frac{\partial R}{\partial T_s}
$$
<!--このRは放射?-->

When the sea ice exists ($L=1$), the surface flux $G_{ice}$ is considered with the sublimation flux ($l_s E$).

$$
	G_{ice} = G^* - l_s E
$$

The temperature derivative term of $G_{ice}$ is

$$
	\frac{\partial G_{ice}}{\partial T_s}=\frac{\partial G^*}{\partial T_s} + l_s\frac{\partial E}{\partial T_s}
$$

We can update the skin temperature with sea ice concentration and $\Delta T_s=G_{ice} ( \frac{\partial G_{ice}}{\partial T_s})^{-1}$


$$
	T_s = T_s +R_{ice} \Delta T_s
$$

Then, the sensible and latent heat flux on the sea ice ($E_{ice},H_{ice}$) is updated.

$$
	E_{ice} = E + \frac{\partial E}{\partial T_s}\Delta T_s
$$

$$
	H_{ice} = H + \frac{\partial H}{\partial T_s}\Delta T_s
$$

When the sea ice does not existed ($L=2$), otherwise, the surface heat flux ($G_{free}$) is calculated by addition of evaporation flux $l_cE$ and the net flux $F^\ast$.

$$
	G_{free}=F^\ast + l_cE
$$

Finally each flux is updated. For sensible heat flux ($H$), the temperature change on the sea ice is considered.

$$
	H=H+ R_{ice}  H_{ice}
$$

Then, the heat used for the temperature change ($F$) is saved.

$$
	F = R_{ice} H_{ice}
$$

For upward longwave radiative flux ($LW^\uparrow$), temperature change on the sea ice ($\Delta T_s$) is considered.

$$
	LW^\uparrow=LW^\uparrow +  4\frac{\sigma}{T_s}R_{ice}  \Delta T_s
$$

For the surface heat flux ($G$), sea ice existence is considered.

$$
	G=(1-R_{ice})G_{free} + R_{ice}G_{ice}
$$

For latent heat flux $E$, sea ice existence is considered.

$$
	E=(1-R_{ice})E + R_{ice}E_{ice}
$$

Then, each term above are saved as freshwater fluxes ($W_{free}, W_{ice}$) of ice covered and free areas.

$$
	W_{free} = (1-R_{ice}) E
$$

$$
	W_{ice} = R_{ice} E_{ice}
$$
