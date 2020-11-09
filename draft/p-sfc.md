# Sea Surface Flux (海表面フラックス)
## 1. 本章でとりあげる or 関連するプログラム
**contents** are just quoted by the programs.

| module name      | file name            | contents                          |
|:-----------------|:---------------------|:----------------------------------|
| `MODULE:[PLAND]` | `./physics/pglnd.F ` | land surface                      |
| `MODULE:[POCEN]` | `./physics/pgocn.F`  | mixed layer/fixed SST ocean       |
| `MODULE:[PGRIV]` | `./physics/pgriv.F ` | river routing submodel            |
| `MODULE:[PGSFC]` | `./physics/pgsfc.F ` | surface driver                    |
| `MODULE:[PSFCL]` | `./physics/psfcl.F`  | surface bulk transfer coefficient |
| `MODULE:[PSFCM]` | `./physics/psfcm.F`  | surface fluxes                    |

### SUBROUTINES

#### `MODULE:[PLAND]` (./physics/pglnd.F)

| routine name | contents                           |
|:-------------|:-----------------------------------|
| `LAND`       | land driver                        |
| `LNDSLV`     | surface temperature                |
| `LNDSUB`     | land surface                       |
| `LNDIMP`     | change in underground values       |
| `GRWNML`     | file of surface parameter          |
| `PGPGET`     | set surface parameters             |
| `LSETCO`     | coordinates of submodel            |
| `SETGLV`     | set land vartical coordinates      |
| `SETGL`      | vertical coordinates               |
| `LRSTRT`     | read land initial values           |
| `LCHKV`      | valid range monitor                |
| `SETDTL`     | land time step (dummy for matsiro) |


#### `MODULE:[POCEN]` (./physics/pgocn.F)

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


#### `MODULE:[PGRIV]` (./physics/pgriv.F)

| routine name | contents          |
|:-------------|:------------------|
| `RIVER`      | river routing     |
| `RIVDST`     | river destination |



#### `MODULE:[PGSFC]` (./physics/pgsfc.F)

| routine name | contents       |
|:-------------|:---------------|
| `SURFCE`     | surface driver |
| `RADSFC`     | --             |


#### `MODULE:[PSFCL]` (./physics/psfcl.F)

| routine name | contents                  |
|:-------------|:--------------------------|
| `BLKCOF`     | bulk transfer coefficient |

#### `MODULE:[PSFCM]` (./physics/psfcm.F)

| routine name | contents     |
|:-------------|:-------------|
| `SFCFLX`     | surface flux |



## 2. Calculation of bulk coefficient with respect to momentum and heat

After Watanabe (1994), the bulk coefficient is also calculated using Monin-Obukhov similarity as

$$
 C_M = k^2 \left[ \ln \frac{z_a-d}{z_0} + \Psi_m(\zeta) \right]^{-2} \\
 C_H = k^2 \left[ \ln \frac{z_a-d}{z_0} + \Psi_m(\zeta) \right]^{-1}
             \left[ \ln \frac{z_a-d}{z_T} + \Psi_h(\zeta) \right]^{-1} \\
 C_{Hs} = k^2 \left[ \ln \frac{z_a-d}{z_0} + \Psi_m(\zeta_g) \right]^{-1}
             \left[ \ln \frac{z_a-d}{z_T^{\dagger}} + \Psi_h(\zeta_g) \right]^{-1} \\
 C_{Hc} = C_H - C_{Hs}
$$


where $C_M$ and $C_H$ are the bulk coefficients of the overall canopy (leaf surface + forest floor) with respect to momentum and heat, respectively; $C_{Hs}$ is the bulk coefficient of the ground surface (forest floor) flux with respect to heat; $C_{Hc}$ is the bulk coefficient of the canopy (leaf surface) flux with respect to heat; $\Psi_m$ and $\Psi_h$ are Monin-Obukhov shear functions with respect to momentum and heat, respectively; and $z_a$ is the reference height of the atmosphere (height of the troposphere). Using the Monin-Obukhov lengths $\zeta$ and $\zeta_g$ related to the overall canopy and ground surface (forest floor), respectively, $L$ and $L_g$ are respectively expressed as:


$$
 \zeta = \frac{z_a - d}{L} \\
 \zeta_g = \frac{z_a - d}{L_g}
$$

and the Monin-Obukhov lengths are expressed as:

$$
 L = \frac{\Theta_0 C_M^{3/2}|V_a|^2}{kg(C_{Hs}(T_s - T_a) + C_{Hc}(T_c - T_a))} \\
 L_s = \frac{\Theta_0 C_M^{3/2}|V_a|^2}{kg C_{Hs}(T_s - T_a)}
$$


where $\Theta_0$ =300K; $|V_a|$ is the absolute value of the surface wind speed; $k$ is the Karman constant; $g$ is the gravitational acceleration; and $T_a,$T_c$ and $T_s$ are the temperature of the troposphere, canopy (leaf surface), and ground surface (forest floor), respectively.

Since the bulk coefficient is necessary for calculation of the Monin-Obukhov length, and the Monin-Obukhov length is necessary for calculation of the bulk coefficient, the calculation is iterated (twice as a standard) with a neutral bulk coefficient as the initial value.

Prior to this calculation, the snow depth in the snow-covered portion is added to the zero-plane displacement. However, the upper limit is set so that the zero-plane displacement does not exceed the value of $z_a$:


$$
 d = \min( d + D_{Sn} ,\  f_{\max} \cdot z_a )
$$


As a standard, $f_${\max}$ is set at 0.5.

## 4.3 Calculation of bulk coefficient with respect to vapor

This calculation is performed after the calculation of stomatal resistance, described later.

When the stomatal resistance ($r_{st}$)  and ground surface evaporation resistance　($r_{soil}$)  have been solved, the bulk coefficient with respect to vapor is solved as:

$$
 C_{Ec} |V_a| = \left[ (C_{Hc} |V_a|)^{-1} + r_{st} / LAI\right]^{-1} \\
 C_{Es} |V_a| = \left[ (C_{Hs} |V_a|)^{-1} + r_{soil}\right]^{-1}
$$

(Previously, this parameter was solved by converting stomatal resistance, etc. into a decrease of the exchange coefficient via roughness. However, since this approach seems to be problematic, a simpler method had been adopted in its place.)

In addition, when there is no stomatal resistance, etc. (such as evaporation from wet surfaces), the same value as for the bulk coefficient of heat is used for the bulk coefficient of vapor.


## 2. Calculation of surface turbulent fluxes (地表フラックス)


The turbulent fluxes at the ground surface are solved by bulk formulae as follows. Then, by solving the surface energy balance, the ground surface temperature ($T_s$) and canopy temperature ($T_c$) are updated, and the surface flux values with respect to those values are also updated. The solutions obtained here are temporary values. In order to solve the energy balance by linearizing with respect to $T_s$ and $T_c$, the differential with respect to $T_s$ and $T_c$ of each flux is calculated beforehand.

- Momentum flux

$$
 \tau_x = - \rho C_{M}|V_a| u_a \\
 \tau_y = - \rho C_{M}|V_a| v_a
$$


where $\tau_x$ and $\tau_y$  are the momentum fluxes (surface stress) of the zonal and meridional directions, respectively.

- Sensible heat flux

$$
 H_s = c_p \rho C_{Hs}|V_a| (T_s - (P_s/P_a)^{\kappa}T_a) \tag{eq107}
  \\
 H_c = c_p \rho C_{Hc}|V_a| (T_c - (P_s/P_a)^{\kappa}T_a) \\
 \partial H_s/\partial T_s = c_p \rho C_{Hs}|V_a| \\
 \partial H_c/\partial T_c = c_p \rho C_{Hc}|V_a|
$$

where $H_s$ and $H_c$ are the sensible heat flux from the ground surface (forest floor) and canopy (leaf surface), respectively; $\kappa = R_{air} / c_p$ and $R_{air}$are the gas constants of air; and $c_p$ is the specific heat of air.

- Bare soil surface (forest floor) evaporation flux

$$
 Et_{(1,1)} = (1-A_{Sn})(1-f_{ice})\cdot
           \rho \widetilde{C_{Es}}|V_a|(h_{soil}q^*(T_s) - q_a) \\
 Et_{(2,1)} = (1-A_{Sn})f_{ice}\cdot
           \rho \widetilde{C_{Es}}|V_a|(h_{soil}q^*(T_s) - q_a) \\
 \partial Et_{(1,1)}/\partial T_s = (1-A_{Sn})(1-f_{ice})\cdot
           \rho \widetilde{C_{Es}}|V_a|h_{soil}\cdot dq^*/dT |_{T_s} \\
 \partial Et_{(2,1)}/\partial T_s = (1-A_{Sn})f_{ice}\cdot
           \rho \widetilde{C_{Es}}|V_a|h_{soil}\cdot dq^*/dT |_{T_s}
$$

where $Et_{(1,1)}$ and $Et_{(2,1)}$ are the water evaporation and ice sublimation fluxes at the bare soil surface, respectively; $q^*(T_s)$ is the saturation specific humidity at the ground surface temperature; $h_{soil}$ is the relative humidity at the soil surface layer; $A_{Sn}$ is the snow-covered ratio; and $f_{ice}$ is the ratio of ice in the uppermost soil layer, expressed as

$$
  f_{ice} = w_{i(1)}/w_{(1)}
$$

Since the snow-free portion and snow-covered portion are calculated separately, it should be noted that $A_{Sn}$ takes the value of either 0 (snow-free portion) or 1 (snow-covered portion). When the flux is downward (i.e., dew formation), there is no soil moisture resistance; therefore, the bulk coefficient is taken as:

$$
  \widetilde{C_{Es}} = \left\{
  \begin{array}{ll}
   C_{Es} (h_{soil}q^*(T_s) - q_a > 0 {のとき})\\
   C_{Hs} (h_{soil}q^*(T_s) - q_a \leq 0 {のとき})
  \end{array}
  \right.
$$

- Transpiration flux

$$
 Et_{(1,2)} = (1-f_{cwet}) \cdot \rho \widetilde{C_{Ec}}|V_a|(q^*(T_c) - q_a) \\
 Et_{(2,2)} = 0 \\
 \partial Et_{(1,2)}/\partial T_c =
  (1-f_{cwet}) \cdot \rho \widetilde{C_{Ec}}|V_a|\cdot dq^*/dT|_{T_c} \\
 \partial Et_{(2,2)}/\partial T_c = 0
$$

where $Et_{(1,2)}$ and $Et_{(2,2)}$ are transpiration of water and ice, respectively; and $Et_{(2,2)}$ is always 0. $f_{cwet} = w_c / w_{c,cap}$ is the wet fraction of the canopy. When the flux is downward, which is considered to be dew formation on the dry part of the leaf, the bulk coefficient is taken as:

$$
  \widetilde{C_{Ec}} = \left\{
  \begin{array}{ll}
   C_{Ec} (q^*(T_c) - q_a > 0 {のとき})\\
   C_{Hc} (q^*(T_c) - q_a \leq 0 {のとき})
  \end{array}
  \right.
$$

- Canopy evaporation flux

When      $T_c$ $\geq$ 0 $^{\circ}$ C:


$$
 Et_{(1,3)} =
  f_{cwet} \cdot \rho C_{Hc}|V_a|(q^*(T_c) - q_a) \\
 Et_{(2,3)} = 0 \\
 \partial Et_{(1,3)} \partial T_c =
  f_{cwet} \cdot \rho C_{Hc}|V_a|\cdot dq^*/dT|_{T_c} \\
 \partial Et_{(2,3)} \partial T_c = 0
$$

when  $T_c$ $<$ 0 $^{\circ}$ In case of C:

$$
 Et_{(1,3)} = 0 \\
 Et_{(2,3)} =
  f_{cwet} \cdot \rho C_{Hc}|V_a|(q^*(T_c) - q_a) \\
 \partial Et_{(1,3)} \partial T_c = 0 \\
 \partial Et_{(2,3)} \partial T_c =
  f_{cwet} \cdot \rho C_{Hc}|V_a|\cdot dq^*/dT|_{T_c}
$$

where $Et_{(1,3)}$ and $Et_{(2,3)}$ are the evaporation of water and the sublimation of ice at the canopy surface, respectively.

- Snow sublimation flux

$$
 E_{Sn} = A_{Sn}\cdot \rho C_{Hs}|V_a|(q^*(T_s) - q_a) \\
 \partial E_{Sn}/\partial T_s = A_{Sn}\cdot \rho C_{Hs}|V_a|
 \cdot dq^*/dT|_{T_s}
$$

where $E_{Sn}$ is the snow sublimation flux. Since the snow-free portion and snow-covered portion are calculated separately, it should also be noted here that $A_{Sn}$ takes the value of either 0 (snow-free portion) or 1 (snow-covered portion).


## 3. Calculation of heat conduction fluxes

The heat conduction fluxes in the snow-free and snow-covered portions are calculated. Similarly to the turbulent fluxes, when the energy balance is solved later and the surface temperature is updated, the heat conduction flux values are updated with respect to that value.

In addition, it should also be noted here that since the snow-free portion and snow-covered portion are calculated separately, $A_{Sn}$ takes the value of either 0 (snow-free portion) or 1 (snow-covered portion).

- Heat conduction flux in the snow-free portion

$$
  F_{g(1/2)} = (1 - A_{Sn}) \cdot k_{g(1/2)} / \Delta z_{g(1/2)} (T_{g(1)} - T_s) \\
  \partial F_{g(1/2)}/\partial T_s =
  - (1 - A_{Sn}) \cdot k_{g(1/2)} / \Delta z_{g(1/2)}
$$
where $F_{g(1/2)}$ is the heat conduction flux, $k_{g(1/2)}$ is the soil heat conductivity, $\Delta z_{g(1/2)}$  is the thickness from the temperature definition point of the uppermost soil layer to the ground surface, and $T_{g(1)}$ is the temperature of the uppermost soil layer.

- Heat conduction flux in the snow-covered portion　

$$
  F_{Sn(1/2)} = A_{Sn} \cdot k_{Sn(1/2)} / \Delta z_{Sn(1/2)} (T_{Sn(1)} - T_s)
 \\
  \partial F_{Sn(1/2)}/\partial T_s =
  - A_{Sn} \cdot k_{Sn(1/2)} / \Delta z_{Sn(1/2)} \tag{eq135}
$$

where $F_{Sn(1/2)}$ is the heat conduction flux, $k_{Sn(1/2)}$ is the snow heat conductivity, $\Delta z_{Sn(1/2)}$ is the thickness from the temperature definition point of the uppermost snow layer to the ground surface, and $T_{Sn(1)}$ is the temperature of the uppermost snow layer.

## 4. Solution of energy balance at ground surface and canopy

The energy balance is solved for two cases: (1) when there is no melting at the ground surface, and (2) when there is melting at the ground surface. In case (2), the solution is obtained by fixing the ground surface temperature ($T_s$) at 0°C, and the energy available for use in melting is diagnosed from the energy balance. Snowmelt on vegetation is treated by correction later on; therefore, that case is not solved separately here. Moreover, the case of the snow completely melting within the time steps is also treated by correction later on.

### 4.1 Energy balance at ground surface and canopy

The energy divergence at the ground surface (forest floor) is

$$
 \Delta F_s =
  H_s + R^{net}_s + l Et_{(1,1)} + l_s ( Et_{(2,1)} + E_{Sn} )
  - F_{g(1/2)} - F_{Sn(1/2)} \tag{eq136}
$$

where  $l$ and $l_s$  are the latent heat of evaporation and sublimation, respectively; and $R^{net}_s$ is the net radiation divergence at the ground surface, given by

$$
  R^{net}_s = -(R^{\downarrow}_S - R^{\uparrow}_S) {\mathcal{T}}_{cS}
              - \epsilon R^{\downarrow}_L {\mathcal{T}}_{cL}
              + \epsilon \sigma T_s^4
              - \epsilon \sigma T_c^4 (1 - {\mathcal{T}}_{cL})
$$

where $\sigma$ is the Stefan-Boltzmann constant.

The energy divergence at the canopy (leaf surface) is

$$
  \Delta F_c =
  H_c + R^{net}_c + l ( Et_{(1,2)} + Et_{(1,3)} )
  + l_s ( Et_{(2,2)} + Et_{(2,3)} )
$$

where $R^{net}_c$ is the net radiation divergence at the canopy, given by

$$
  R^{net}_c = -(R^{\downarrow}_S - R^{\uparrow}_S) (1-{\mathcal{T}}_{cS})
              - \epsilon R^{\downarrow}_L (1-{\mathcal{T}}_{cL})
              + ( 2 \epsilon \sigma T_c^4
              - \epsilon \sigma T_s^4 ) (1 - {\mathcal{T}}_{cL}) \tag{eq139}
$$


### 4.2 Case 1: When there is no melting at the ground surface

When there is no melting at the ground surface, $\Delta F_s=\Delta F_c=0$ are solved so that $T_s$ and $T_c$ holds true for the energy balance at the ground surface and canopy.

The energy balance equation linearizing each term with respect to $T_s$ and $T_c$ can be expressed as


$$
 \left(
\begin{array}{l}
 \Delta F_s \\
 \Delta F_c \\
\end{array}
\right)^{current}
=
\left(
\begin{array}{l}
 \Delta F_s \\
 \Delta F_c \\
\end{array}
\right)^{past}
+
\left(
\begin{array}{ll}
 {\partial \Delta F_s}/{\partial T_s}
 {\partial \Delta F_s}/{\partial T_c} \\
 {\partial \Delta F_c}/{\partial T_s}
 {\partial \Delta F_c}/{\partial T_c} \\
\end{array}
\right)
\left(
\begin{array}{l}
 \Delta T_s \\
 \Delta T_c \\
\end{array}
\right)
=
\left(
\begin{array}{l}
 0 \\
 0 \\
\end{array}
\right) \tag{eq140}
$$

The part with $pst$ on the right-hand side is where the fluxes calculated [Eq. (107)](eq107) to [Eq. (135)](#eq135) are substituted into [Eq. (136)](eq136) to [Eq. (139)](#eq139) using the values of $T_s$ and $T_c$ obtained in the previous step.

The differential terms are as follows:

$$
 \frac{\partial \Delta F_s}{\partial T_s} =
 \frac{\partial H_s}{\partial T_s}
+\frac{\partial R^{net}_s}{\partial T_s}
+l\frac{\partial Et_{(1,1)}}{\partial T_s}
+l_s\left(\frac{\partial Et_{(2,1)}}{\partial T_s}
+    \frac{\partial E_{Sn}}{\partial T_s}\right)
-\frac{\partial F_{g(1/2)}}{\partial T_s}
-\frac{\partial F_{Sn(1/2)}}{\partial T_s} \\
 \frac{\partial \Delta F_s}{\partial T_c} =
 \frac{\partial R^{net}_s}{\partial T_c} \\
 \frac{\partial \Delta F_c}{\partial T_s} =
 \frac{\partial R^{net}_c}{\partial T_s} \\
 \frac{\partial \Delta F_c}{\partial T_c} =
 \frac{\partial H_c}{\partial T_c}
+\frac{\partial R^{net}_c}{\partial T_c}
+l  \left(\frac{\partial Et_{(1,2)}}{\partial T_c}
+         \frac{\partial Et_{(1,3)}}{\partial T_c}\right)
+l_s\left(\frac{\partial Et_{(2,2)}}{\partial T_c}
+         \frac{\partial Et_{(2,3)}}{\partial T_c}\right)
$$

where


$$
 \frac{\partial R^{net}_s}{\partial T_s} =
 \epsilon 4 \sigma T_s^3 \\
 \frac{\partial R^{net}_s}{\partial T_c} =
 - ( 1 - {\mathcal{T}}_{cL} ) \epsilon 4 \sigma T_c^3 \\
 \frac{\partial R^{net}_c}{\partial T_s} =
 - ( 1 - {\mathcal{T}}_{cL} ) \epsilon 4 \sigma T_s^3 \\
 \frac{\partial R^{net}_c}{\partial T_c} =
  2( 1 - {\mathcal{T}}_{cL} ) \epsilon 4 \sigma T_c^3
$$

Using the above equations, [Eq. (140)]($eq140) is solved for $T_s$ and $T_c$.

### 4.3 Case 2: When there is melting at the ground surface

When either there is snow on the ground surface or the land cover type is ice sheet, and also the ground surface temperature solved in case 1, $T_s^{current} = T_s^{past}+\Delta T_s$, is higher than 0°C, melting at the ground surface occurs. When there is melting at the ground surface, the ground surface temperature is fixed at 0°C. That is:

$$
 \Delta T_s = \Delta T_s^{melt} = T_{melt} - T_s^{past}
$$

where $T_{melt}$ is the melting point (0°C) of ice.

With $T_c$ known, $\Delta T_s$ is solved by the following equation similarly to [Eq. (140)](#eq140):

$$
 \Delta T_c = \left( - \Delta F_c^{past}
            - \frac{\partial \Delta F_c}{\partial T_s} \Delta T_s^{melt}
              \right) \Bigm/ \frac{\partial \Delta F_c}{\partial T_c}
$$

Thus, $\Delta T_s$ and $\Delta T_c$ are determined, and the energy convergence at the ground surface to be used for melting is solved by the following equation:

$$
 \Delta F_{conv} =
 - \Delta F_s^{current} = - \Delta F_s^{past}
 - \frac{\partial \Delta F_s}{\partial T_s} \Delta T_s^{melt}
 - \frac{\partial \Delta F_s}{\partial T_c} \Delta T_c
$$

### 4.4 Conditions for solutions

Several conditions are set for the solution of the ground surface energy balance. After solving the energy balance, if any of the conditions are not followed, the flux that has contravened the conditions is fixed at the limit value that satisfies the conditions, and the energy balance is solved again.

1. Vapor in the troposphere should not be excessively removed.

Due to the instability of temporal calculations, it is possible that large downward latent heat is produced. The conditions are set so that even in such a case, the vapor in the troposphere from the surface is not completely removed; that is,

$$
  Et_{(i,j)}^{current} > - q_a ( P_s - P_a ) / (g \Delta t)
   \ \ \ \ \ (i=1,2 ; j=1,2,3) \\
  E_{Sn}^{current} > - q_a ( P_s - P_a ) / (g \Delta t)
$$


where $g$ is the gravitational acceleration and $\Delta t$ denotes the time steps of the atmospheric model. For the values of $Et$ etc. to be used for judgment, the updated flux values ($current$) with respect to the values of $T_s$ and $T_c$that have been updated so as to satisfy the energy balance are used. The same applies to all of the other conditions listed below. Updating of the flux values is described later.

2. Soil moisture should not take a negative value.

Soil moisture should not take a negative value due to transpiration; that is,

$$
   Et_{(1,2)}^{current} <
     \sum_{k\in rootzone} \rho_w w_{k}\Delta z_{g(k)} /\Delta t_L
$$

where $\rho_w$  is the water density and $\Delta t_L$ denotes the time steps of the land surface model.

3. Canopy water should not take a negative value.

Canopy water should not take a negative value due to evaporation; that is,

$$
   Et_{(i,3)}^{current} < \rho_w w_c /\Delta t_L
   \ \ \ \ \ (i=1,2)
$$

4. The snow water equivalent should not take a negative value.

The snow water equivalent should not take a negative value due to sublimation of snow; that is,

$$
   E_{Sn}^{current} < Sn /\Delta t_L
$$

### 4.5 Updating of ground surface and canopy temperatures

The ground surface temperature and canopy temperature are updated as follows:

$$
 T_s^{current} = T_s^{past} + \Delta T_s \\
 T_c^{current} = T_c^{past} + \Delta T_c
$$

Based on the updated canopy temperature, the canopy water is diagnosed in advance as being either liquid or solid. This information is used when treating freezing and melting of the canopy water, as follows:


$$
 A_{Snc} = \left\{
\begin{array}{ll}
 0 (T_c \geq T_{melt})\\
 1 (T_c <    T_{melt})
\end{array}
\right.
$$

where $A_{Snc}$ is the frozen fraction on the canopy.

### 4.6 Updating of flux values

The flux values are updated with respect to the updated values of $T_s$ and $T_c$. When $F$ denotes any given flux, updating of the values is performed as follows:

$$
 F^{current} = F^{past} + \frac{\partial F}{\partial T_s} \Delta T_s
                        + \frac{\partial F}{\partial T_c} \Delta T_c
$$

Using the updated flux values, the fluxes output into the atmosphere, etc. are calculated as follows:


$$
 H = H_s + H_c \\
 E = \sum_{j=1}^3 \sum_{i=1}^2 Et_{(i,j)} + E_{Sn} \\
 R^{\uparrow}_L = {\mathcal{T}}_{cL} \epsilon \sigma T_s^4
 + (1 - {\mathcal{T}}_{cL}) \epsilon \sigma T_c^4
 + (1 - \epsilon) R^{\downarrow}_L \\
 T_{sR} = ( R^{\uparrow}_L / \sigma )^{1/4}
$$


where $T_{sR}$ is the radiation temperature at the ground surface.

The root uptake flux in each soil layer is then calculated as follows:

$$
 F_{root(k)} = f_{rootup(k)} Et_{(1,2)} \ \ \ \ (k=1,\ldots,K_g)
$$

where $F_{root(k)}$ is the root uptake flux and  $f_{rootup(k)}$ is the weighting for distribution of the transpiration to the root uptake flux in each layer.
