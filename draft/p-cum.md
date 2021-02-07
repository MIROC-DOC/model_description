## Cumulus scheme

### Outline of cumulus scheme

The Chikira scheme (Chikira and Sugiyama 2010) has been adopted since version 5 of MIROC. It represents updrafts, downdrafts, their detrainment and compensating downward motion over the surrounding area as well as microphysical processes associated with updrafts and downdrafts.

The updraft is based on an entraining plume model, where the mass flux increases upward due to lateral entrainment. The detrainment occurs only at the cloud top which is defined as the neutral buoyancy level of the updraft air parcel. The lateral entrainment rate is formulated in terms of buoyancy and vertical velocity of the air parcel at each level following Gregory (2001). The momentum transport is formulated following Gregory et al. (1997).

The cloud base mass fluxes are determined by the prognostic convective kinetic energy closure proposed by Arakawa and Xu (1990) and Xu (1991, 1993), which was adopted in the prognostic Arakawa–Schubert scheme (Randall and Pan 1993; Pan 1995; Randall et al. 1997; Pan and Randall 1998). The convective kinetic energy increases by buoancy and decreases by dissipation. 

The cloud types are spectrally represented according to the updraft vertical velocity at the cloud base. Larger (smaller) vertical velocities give smaller (larger) entrainment rates which result in higher (lower) cloud tops. The cloud base is diagnosed as the lifting condensation level of the air parcel at the lowest model layer.

The scheme has a simple downdraft model, where a part of the precipitation caused by the updrafts evaporates and forms the cold air which enters into the downdrafts. The detrainment of the downdraft mass fluxes occurs at the neutral buoyancy level and near the surface. 

The interaction of the updrafs and downdrafts with the surrounding environment is formulated following Arakawa and Schubert (1974). The areal fractions of the updrafts and downdrafts are assumed to be sufficiently small and the grid-mean prognostic variables are supposed to be the same as those over the environmental area, which are changed by the detrainment of the updrafts and downdrafts, the compensating subsidence and the evaporation and sublimation of the precipitation associated with the updrafts. 

The input variables to this scheme are temperature $T$, specific humidity $q$, cloud liquid water $q_l$, cloud ice $q_i$, zonal wind $u$, meridional wind $v$, all tracers including aerosols and greenhouse gases, height $z$, pressure $p$, and cloud cover $C$. The scheme gives the tendencies of $T$, $q_v$, $q_l$, $q_i$, $u$, $v$, $C$ and all the tracers. The vertical profiles of the rainfall and snowfall fluxes, cloud liquid water, cloud ice and cloud fraction associated with the updrafts are also output as diagnostic variables. 

The procedure of the calculations is given as follows along with the names of the subroutines.

1. calculation of cloud base `CUMBAS`.
2. calculation of in-cloud properties `CUMUP`.
3. calculation of cloud base mass flux `CUMBMX`.
4. calculation of cloud mass flux, detrainment, and precipitation `CUMFLX`.
5. diagnosis of cloud water and cloud cover by cumulus `CUMCLD`.
6. calculation of tendencies by detrainment `CLDDET`.
7. calculation of freezing, melting, evaporation, sublimation, and downdraft mass flux `CUMDWN`.
8. calculation of tendencies by compensating subsidence `CLDSBH`.
9. calculation of cumulus momentum transport `CUMCMT`.
10. calculation of tracer updraft `CUMUPR`.
11. calculation of tracer downdraft `CUMDNR`.
12. calculation of tracer subsidence `CUMSBR`.
13. fixing tracer mass `CUMFXR` .

### Interaction between cumulus ensemble and large-scale environment

Following Arakawa and Schubert (1974), the equations for tendencies of the grid-mean variables are written as

$$
 \frac{\partial \bar{h}}{\partial t} = M \frac{\partial \bar{h}}{\partial z} + \sum_j D_j \left[ h_j(z_{T,j}) - \bar{h} \right],
$$

$$
 \frac{\partial \bar{q}}{\partial t} = M\frac{\partial \bar{q}}{\partial z} + \sum_j D_j \left[ q_j(z_{T,j}) - \bar{q} \right],
$$

where $M$, $D$, $h$ denote total mass flux, detrainment mass flux and moist static energy. $q$ is a substitute for $q_v$, $q_l$ and $q_i$ and any tracers which are calculated in the same way. $z_T$ is the height of the updraft. The hats indicate in-cloud properties, the overbars grid-mean. The subscripts $j$ are an index for the updraft types. 

The total mass flux $M$ and detrainment $D$ are defined as

$$
M(z) = \sum_j M_{u,j} + M_d \, ,
$$

$$
 D_j(z) = M_{u,j}(z_{T,j}) \delta (z-z_{T,j})
$$

respectively, where $M_u$ and $M_d$ denote mass fluxes of updraft and downdraft respectively. The updraft mass flux is formulated as

$$
 M_{u,j}(z) = M_{B,j} \, \eta_j(z)
$$

where $M_B$ and $\eta$ are the updraft mass flux at its cloud base and normalized mass flux.

### Cloud base

The cloud base is determined as the lifting condensation level of the air at the lowest model layer. It is defined as the smallest $z$ which satisfies

$$
  \bar{q_t}(z_1) \geq \bar{q_v}^* + \frac{\gamma}{L_v(1+\gamma)} \left[\bar{h}(z_1)-\bar{h}^*(z) \right]\,,
$$

where $q_t$ denotes total water, $L_v$ the latent heat of vaporization, $z_1$ the height of the lowest model layer at the full level and 

$$
 \gamma \equiv \frac{L_v}{C_p}\left(\frac{\partial \bar{q}^*}{\partial \bar{T}}\right)_{\bar{p}}.
$$

$C_p$ denotes the specific heat of dry air at constant pressure and the stars indicate saturation values. 

The normalized mass flux below the cloud base is given by $\eta = (z/z_B)^{1/2}$ for all of the updraft types where $z_B$ denotes the cloud base height.

### Updraft velocity and entrainment rate

The entrainment rate is defined by

$$
 \epsilon = \frac{1}{M_u}\frac{\partial M_u}{\partial z}
$$

and allowed to vary vertically. Based on the formulation of Gregory (2001), the updraft velocity is calculated by

$$
 \frac{1}{2}\frac{\partial \hat{w}^2}{\partial z} = aB - \epsilon \hat{w}^2 \qquad\tag{1}
$$

where $w$ and $B$ are the vertical velocity and the buoyancy of updraft air parcel respectively. $a$ is a dimensionless constant parameter ranging from 0 to 1 and represents a ratio of buoyancy force used to accelerate the updraft velocity. The hats indicate the values of the updraft. The second term on the right-hand side represents reduction in the upward momentum of the air parcel through the entrainment. Here and hereafter, the equation number corresponds to that in Chikira and Sugiyama (2010).

Then it is assumed that

$$
 \epsilon \hat{w}^2 \simeq C_\epsilon a B,
$$

where $C_\epsilon$ is a dimensionless constant parameter ranging from 0 to 1. This formulation denotes that a certain fraction of the buoyancy-generated energy is reduced by the entrainment, which is identical to the fraction used to accelerate the entrained air to the updraft velocity. Thus, the entrainment rate is written as

$$
 \epsilon = C_\epsilon\frac{aB}{\hat{w}^2}. \qquad\tag{2}
$$

Eqs. (1) and (2) lead to

$$
 \frac{1}{2}\frac{\partial \hat{w}^2}{\partial z} = a(1 - C_\epsilon) B
$$

which shows that $\hat{w}$ is continuously accelerated upward when buoyancy is positive. Many CRM and LES results show, however, that updraft velocity is often reduced if the parcel approaches its cloud top. For this reason, adding an additional term, we use

$$
 \frac{1}{2}\frac{\partial \hat{w}^2}{\partial z} = a(1 - C_\epsilon) B - \frac{1}{z_0}\frac{\hat{w}^2}{2}\qquad\tag{4}
$$

where the last term denotes that the energy of the updraft velocity is relaxed to zero with a height scale $z_0$. Eq. (4) is discretized as

$$
 \frac{1}{2}\frac{\hat{w}^2_{k+1/2} - \hat{w}^2_{k-1/2}}{\Delta z_k} = a(1 - C_\epsilon) B_k - \frac{1}{z_0}\frac{\hat{w}_{k+1/2}^2}{2} \qquad\quad\tag{A5}
$$

where $k$ is an index of full levels and $k+1/2$ and $k-1/2$ indicate the upper and lower sides of the half levels. $\Delta z$ is the depth of the model layer. Note that the equation is solved for $\hat{w}^2$ rather than $\hat{w}$.

The buoyancy of the cloud air parcel is determined by

$$
 B  =   \frac{g}{\bar{T}} ( \hat{T}_v - \bar{T}_v )
$$

$$
 \simeq g \left\{ \frac{\hat{h} - \bar{h}^*}{C_p \bar{T}(1 + \gamma)} + \varepsilon(\hat{q_v}-\bar{q_v}) - \left[ (\hat{q_l}+\hat{q_i}) - (\bar{q_l}+\bar{q_i}) \right] \right\}
$$

where $g$ and $T_v$ denote gravity and virtual temperature respectively. $\varepsilon = R_v/R_d - 1$ where $R_v$ and $R_d$ are the gas constants for water vapor and dry air respectively. 

$\hat{w}$, $B$ and $\epsilon$ are calculated for each of the updraft types separately, but we omit the subscript $j$ for convenience. 

### Normalized mass flux and updraft properties

The properties of the updraft are determined by

$$
 \frac{\partial \eta \hat{h}}{\partial z} = \epsilon \eta \bar{h} + Q_i, \qquad\tag{5}
$$

$$
 \frac{\partial \eta \hat{q_t}}{\partial z} = \epsilon \eta \bar{q_t} - P \qquad\tag{6}
$$

and

$$
 \frac{\partial \eta}{\partial z} = \epsilon \eta, \qquad\tag{7}
$$

where $Q_i$ and $P$ denote heating by liquid-ice transition and precipitation respectively. All the other variables such as temperature, specific humidity, and liquid and ice cloud water are computed from these quantities. Tracers are calculated by a method identical to that for $\hat{q}_t$.

Equation (7) leads to

$$
 \frac{\partial \ln \eta}{\partial z} = \epsilon.
$$

Then, $\eta$ and $\epsilon$ are discretized as

$$
 \frac{\ln \eta_{k+1/2} - \ln \eta_{k-1/2}}{\Delta z_k} = \epsilon_k. \qquad\quad\tag{A1}
$$

Note that this discrete form leads to an exact solution if $\epsilon$ is vertically constant. Also, $\eta$ is finite as far as $\epsilon$ is. For $\epsilon_k,$ a maximum value of $4 \times 10^{-3} m^{-1}$ is applied.

Equations (5) and (6) are written as

$$
 \frac{\partial \eta \hat{h}}{\partial z} = E \bar{h} + Q_i,
$$

$$
 \frac{\partial \eta \hat{q}_t}{\partial z} = E \bar{q}_t -P
$$

respectivuly, where $E = \epsilon\eta$. These equations are discretized as

$$
 \frac{\eta_{k+1/2} \hat{h}_{k+1/2} - \eta_{k-1/2} \hat{h}_{k-1/2}}{\Delta z_k} = E_k \bar{h}_k + {Q_{i,k}}  \qquad\quad\tag{A2}
$$

$$
 \frac{\eta_{k+1/2} \hat{q}_{t,k+1/2} - \eta_{k-1/2} \hat{q}_{t,k-1/2}}{\Delta z_k} = E_k {\bar{q}_{t,k}} - P_k  \qquad\quad\tag{A3}
$$

Considering the relation that $\partial \eta/\partial z = \epsilon\eta$, we descretize $E_k$ as

$$
 E_k = \frac{\eta_{k+1/2} - \eta_{k-1/2}}{\Delta z_k}  \qquad\quad\tag{A4}
$$

Note that conservation of mass, energy, and water is guaranteed with Eqs. (A1)–(A4). This set of equations leads to exact solutions of $\hat{h}$ under the special case that $\epsilon$ and $\bar{h}$ are vertically constant and $Q_i$ is zero. From Eqs. (A1), (A2), and (A4), assuming $Q_i$ is zero,

$$
 \hat{h}_{k+1/2} = e^{-\epsilon_k \Delta z_k} \hat{h}_{k - 1/2} + (1 - e^{-\epsilon_k \Delta z_k}) \bar{h}_k,
$$

which shows that $\hat{h}_{k+1/2}$ is a linear interpolation between $\hat{h}_{k - 1/2}$ and $\bar{h}_k$. Thus, the stability of $\hat{h}$ is guaranteed. The same property applies to $\hat{q}_t$ as well, if $P$ is zero.

These calculations are made for each of the updraft types separately, but we omit the subscript $j$ for convenience.

### Spectral representation

Following the spirit of the Arakawa–Schubert scheme, updraft types are spectrally represented. Different values of cloud-base updraft velocities are given from the minimum to the maximum values with a fixed interval. The minimum and maximum values are set to 0.1 and 1.4 $m s^{-1}$, with an interval of 0.1 $m s^{-1}$.

Then, the updraft properties are calculated upward with Eqs. (2), (4), (5), (6), and (7). This upward calculation continues even if the buoyancy is negative as long as the updraft velocity is positive. If the velocity becomes negative at some level, the air parcel detrains at the neutral buoyancy level which is below and closest to the level. That is, the scheme automatically judges whether the rising parcel can penetrate the negative buoyancy layers when there is a positive buoyancy layer above. The effect of the convective inhibition (CIN) near cloud base is also represented by this method. Note, however, that an effect of overshooting above cloud top is not represented for simplicity (i.e., detrainment never occurs above cloud top).

### Cloud-base mass flux

The cloud-base mass flux is determined with the prognostic convective kinetic energy closure proposed by Arakawa and Xu (1990). That is, the cloud kinetic energy for each of the updraft types is explicitly predicted by

$$
 \frac{\partial K}{\partial t} = AM_B - \frac{K}{\tau_p}\,,  \qquad\tag{8}
$$

where $K$ and $A$ are the cloud kinetic energy and cloud work function respectively, and $\tau_p$ denotes a time scale of dissipation. The cloud work function $A$ is defined as

$$
 A \equiv \int_{z_B}^{z_T} B \eta \,dz\,.
$$

The cloud kinetic energy is linked with $M_B$ by

$$
 K = \alpha M_B^2.  \tag{9}
$$

The cloud-base mass flux is then solved for each of the updraft types.

### Microphysics

The method to obtain temperature and specific humidity of in-cloud air from moist static energy is identical to that in Arakawa and Schubert (1974). The ratio of precipitation to the total amount of condensates generated from cloud base to a given height $z$ is formulated as

$$
 F_p(z) = 1 - e^{-(z - z_B - z_0)/z_p},
$$

where $z_0$ and $z_p$ are tuning parameters.

The ratio of cloud ice to cloud condensate is determined simply by a linear function of temperature,

$$
 F_i(T) = \begin{cases} 1 & T \leq T_1 \\ (T_2 - T)/(T_2 - T_1) & T_1 < T < T_2 \\ 0  & T \geq T_2 \end{cases}
$$

where $T_1$ and $T_2$ are set to 258.15 and 273.15 K. The ratio of snowfall to precipitation is also determined by this function.

From the conservation of condensate static energy, $C_p T + gz + L_v q - L_i q_i$ where $L_i$ is the latent heat of fusion, for a cloud parcel, $Q_i$ in Eq. (5) is written as

$$
 Q_i = L_i \left(\frac{\partial \eta \hat{q}_i}{\partial z} - \epsilon\eta\bar{q}_i\right)
$$

and discretized as

$$
 {Q_i}_k = L_i \left(\frac{\eta_{k+1/2} \hat{q}_{i,k+1/2} - \eta_{k-1/2} \hat{q}_{i,k-1/2}}{\Delta z_k} - E_k \bar{q}_{i,k} \right)
$$

Strictly, the ratio of the cloud ice to the cloud condensate should be recalculated after the modification of temperature by $Q_i$ and the iterations of the calculation are required; however, it is omitted for simplicity.

Melting and freezing of precipitation occurs depending on wet-bulb temperature of large-scale environment and cumulus mass flux.

### Evaporation, sublimation and downdraft

A part of precipitation is evaporated at each level as

$$
 E_v = a_e (\bar{q}_w - \bar{q}) \left(\frac{P}{V_T}\right),
$$

where $E_v$, $q_w$ and $V_T$ are the mass of evaporation per a unit volume and time, wet-bulb saturated specific humidity and terminal velocity of precipitation respectively $a_e$ is a constant. Downdraft mass flux $M_d$ is generated as

$$
 \frac{\partial M_d}{\partial z} = -b_e \bar{\rho} (\bar{T}_w - \bar{T}) P,
$$

where $\rho$ and $T_w$ are density and wet-bulb temperature, respectively; $b_e$ is a constant. Properties of downdraft air are determined by budget equations and the detrainment occurs at neutral buoyancy level and below cloud base.

If the precipitation is composed of both rain and snow, the rain (snow) is evaporated (sublimated) in the same ratio as the ratio of rain (snow) to the total precipitation when the precipitation evaporates to produce downdrafts.

### Cloudiness

Fractional cloudiness of the updrafts $C_u$ used in the radiation scheme is diagnosed by

$$
 C_u = \frac{C_\mathrm{max} - C_\mathrm{min}}{\ln M_\mathrm{max} - \ln M_\mathrm{min}}(\ln \sum_j M_{u,j} - \ln M_\mathrm{min}) + C_\mathrm{min},
$$

where $C_\mathrm{max}$, $C_\mathrm{min}$, $M_\mathrm{max}$, $M_\mathrm{min}$ are the maximum and minimum values of the cloudiness and cumulus mass flux respectively.

The grid mean liquid cloud mixing ratio in the updrafts is given by

$$
 l_c = \frac{\beta C_u}{M} \sum_j \hat{q}_{l,j} M_{u,j},
$$

where $\beta$ is a dimensionless constant. The grid mean ice cloud mixing ratio is determined similarly.

### Cumulus Momentum Transport

Following Gregory et al. (1997), the zonal and meridional velocities of the updrafts are calculated as

$$
 \frac{\partial \eta \hat{u}}{\partial z} = \epsilon \eta \bar{u} + C_m \eta \frac{\partial \bar{u}}{\partial z},
$$

where $C_m$ is a constant from 0 to 1 representing the effect of pressure. This equation  can be rewitten as
$$
 \frac{\partial \eta \hat{u}}{\partial z} = (1-C_m) \epsilon \eta \bar{u} + C_m \frac{\partial \eta \bar{u}}{\partial z},
$$

and is discretized as

$$
 \begin{align}
  \frac{\eta_{k+1/2} \hat{u}_{k+1/2} - \eta_{k-1/2} \hat{u}_{k-1/2}}{\Delta z_k} = & (1-C_m) E_k \bar{u}_k \\
         & + C_m \frac{\eta_{k+1/2} \bar{u}_{k+1/2} - \eta_{k-1/2} \bar{u}_{k-1/2}}{\Delta z_k}.
 \end{align}
$$

The horizontal velocities of the downdrafts are calculated similarly. The tendencies of zonal and meridional velocities by the cumulus momentum transport (CMT) are calculated as

$$
 \left(\frac{\partial u}{\partial t}\right)_{\mathrm{CMT},k} = -g\frac{(\rho\overline{u'w'})_{k+1/2} - (\rho\overline{u'w'})_{k-1/2}}{\Delta p_k},
$$

$$
 \left(\frac{\partial v}{\partial t}\right)_{\mathrm{CMT},k} = -g\frac{(\rho\overline{v'w'})_{k+1/2} - (\rho\overline{v'w'})_{k-1/2}}{\Delta p_k}
$$

respectively, where $\rho\overline{u'w'}$ and $\rho\overline{v'w'}$ are total zonal and meridional momentum fluxes respectively and $\Delta p_k = p_k - p_{k+1}$.
