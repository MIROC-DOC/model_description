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
  \bar{q_t}(z_1) \geq \bar{q_v}^* + \frac{\gamma}{L(1+\gamma)} \left[\bar{h}(z_1)-\bar{h}^*(z) \right]\,,
$$

where $q_t$ denotes total water, L the latent heat of vaporization, $z_1$ the height of the lowest model layer at the full level and 

$$
 \gamma \equiv \frac{L}{C_p}\left(\frac{\partial \bar{q}^*}{\partial \bar{T}}\right)_{\bar{p}}.
$$

$C_p$ denotes the specific heat of dry air at constant pressure and the stars indicate saturation values. 

The normalized mass flux below the cloud base is given by $\eta = (z/z_B)^{1/2}$ for all of the updraft types where $z_B$ denotes the cloud base height.

### Updraft velocity and entrainment rate

The entrainment rate is defined by

$$
 \epsilon = \frac{1}{M}\frac{\partial M}{\partial z}
$$

where $M$ is mass flux of cumulus updraft and is allowed to vary vertically. Based on the formulation of Gregory (2001), the rate of change of updraft velocity with height is

$$
 \frac{1}{2}\frac{\partial \hat{w}^2}{\partial z} = aB - \epsilon \hat{w}^2 \qquad\tag{1}
$$

where $\hat{w}$ and $B$ are the updraft velocity and the buoyancy of cloud air parcel, respectively, and $a$ is a dimensionless
constant parameter ranging from 0 to 1 and represents a ratio of buoyancy force used to accelerate mean updraft velocity. Here, $a$is set at 0.15. The other part of the force is used for the energy of perturbation. The second term on the right-hand side represents reduction in the upward momentum of cloud air parcel through the entrainment process. Then it is assumed that

$$
 \epsilon \hat{w}^2 \simeq C_\epsilon a B,
$$

where $C_\epsilon$ is a dimensionless constant parameter ranging from 0 to 1. Here, $C_\epsilon$ is set at 0.6. This expression denotes that a certain fraction of buoyancy-generated energy is reduced by entrainment, which is identical to the fraction used to accelerate entrained air to the mean updraft velocity. Thus, entrainment rate is written as

$$
 \epsilon = C_\epsilon\frac{aB}{\hat{w}^2}. \qquad\tag{2}
$$

Eqs. (1) and (2) lead to

$$
 \frac{1}{2}\frac{\partial \hat{w}^2}{\partial z} = a(1 - C_\epsilon) B
$$

which shows that $\hat{w}$ is continuously accelerated upward when buoyancy is positive. Many CRM and LES results show, however, that updraft velocity is often reduced if the parcel approaches cloud top. For this reason, an additional term is added when used with Eq. (2), and the equation becomes

$$
 \frac{1}{2}\frac{\partial \hat{w}^2}{\partial z} = a(1 - C_\epsilon) B - \frac{1}{z_0}\frac{\hat{w}^2}{2}\qquad\tag{4}
$$

where the last term denotes that the energy of the updraft velocity is relaxed to zero with a height scale $z_0$. Here, $z_0$ is set at 2 km. Eq. (4) is discretized as

$$
 \frac{1}{2}\frac{\hat{w}^2_{k+1/2} - \hat{w}^2_{k-1/2}}{\Delta z_k} = a(1 - C_\epsilon) B - \frac{1}{z_0}\frac{\hat{w}_{k+1/2}^2}{2} \qquad\quad\tag{A5}
$$

Note that the equation is solved with respect to $\hat{w}^2$ rather than $\hat{w}$.

Buoyancy of cloud air parcel is determined by

$$
 B  =   \frac{g}{\bar{T}} ( \hat{T}_v - \bar{T}_v )
$$

$$
 =   \frac{g}{\bar{T}} \left[ \hat{T} ( 1+\varepsilon \hat{q}-\hat{l} ) - \bar{T} ( 1+\varepsilon \bar{q} - \bar{l}) \right]
$$

$$
 \simeq  g \left[ \frac{\hat{T} - \bar{T}}{\bar{T}} + \varepsilon(\hat{q}-\bar{q}) - (\hat{l} - \bar{l}) \right]
$$

$$
 \simeq g \left[ \frac{1}{\bar{T}}\frac{\hat{h} - \bar{h}^*}{C_p (1 + \gamma)} + \varepsilon(\hat{q}-\bar{q}) - (\hat{l} - \bar{l}) \right]
$$

where $\varepsilon = R_\mathrm{{H}_2{O}}/R_\mathrm{air} - 1$.

### Normalized mass flux and In-cloud properties

In-cloud properties are determined by

$$
 \frac{\partial \eta \hat{h}}{\partial z} = \epsilon \eta \bar{h} + Q_i, \qquad\tag{5}
$$

$$
 \frac{\partial \eta \hat{q_t}}{\partial z} = \epsilon \eta \bar{q_t} - P,\,\mathrm{and} \qquad\tag{6}
$$

$$
 \frac{\partial \eta}{\partial z} = \epsilon \eta, \qquad\tag{7}
$$

where $h$ and $q_t$ are moist static energy and total water, respectively. Also, $Q_i$ and $P$ denote heating by liquid-ice transition and precipitation, respectively. All other variables such as temperature, specific humidity, and liquid and ice cloud water are computed by these quantities; the details are described in appendix B. Tracers such as aerosols are determined by a method identical to that for $\hat{q}_t$. Following Arakawa and Schubert (1974), detrainment occurs only at cloud top.

Equation (7) leads to

$$
 \frac{\partial \ln \eta}{\partial z} = \epsilon.
$$

Then, $\eta$ and $\epsilon$ are discretized as

$$
 \frac{\ln \eta_{k+1/2} - \ln \eta_{k-1/2}}{\Delta z_k} = \epsilon_k \qquad\quad\tag{A1}
$$

where the subscript $k$ is an index of full levels. Here, $k + 1/2$ and $k - 1/2$ are the adjacent half levels above and below the level $k$, respectively, and $\Delta z_k$ is a vertical length of the level $k$. Note that this discrete form leads to an exact solution if $\epsilon$ is vertically constant. Also, $\eta$ is finite as far as $\epsilon$ is. For $\epsilon_k,$ a maximum value of $4 \times 10^{-3}$ is applied.

Equations (5) and (6) are written as

$$
 \frac{\partial \eta \hat{h}}{\partial z} = E \bar{h} + Q_i, \mathrm{and}
$$

$$
 \frac{\partial \eta \hat{q}_t}{\partial z} = E \bar{q}_t -P,
$$

where $E = \epsilon\eta$. These are discretized as

$$
 \frac{\eta_{k+1/2} \hat{h}_{k+1/2} - \eta_{k-1/2} \hat{h}_{k-1/2}}{\Delta z_k} = E_k \bar{h}_k + {Q_i}_k  \qquad\quad\tag{A2}
$$

$$
 \frac{\eta_{k+1/2} {\hat{q}_t}_{k+1/2} - \eta_{k-1/2} {\hat{q}_t}_{k-1/2}}{\Delta z_k} = E_k {\bar{q}_t}_k - P_k  \qquad\quad\tag{A3}
$$

Considering the relation that $\partial h/\partial z = \epsilon\eta$, $E_k$ is expressed by

$$
 E_k = \frac{\eta_{k+1/2} - \eta_{k-1/2}}{\Delta z_k}  \qquad\quad\tag{A4}
$$

Note that conservation of mass, energy, and water is guaranteed with Eqs. (A1)–(A4). This set of equations leads to exact solutions of $\hat{h}$ under the special case that $\epsilon$ and $\bar{h}$ are vertically constant and $Q_i$ is zero. From Eqs. (A1), (A2), and (A4), assuming $Q_i$ is zero,

$$
 \hat{h}_{k+1/2} = e^{-\epsilon_k \Delta z_k} \hat{h}_{k - 1/2} + (1 - e^{-\epsilon_k \Delta z_k}) \bar{h}_k,
$$

which shows that $\hat{h}_{k+1/2}$ is a linear interpolation between $\hat{h}_{k - 1/2}$ and $\bar{h}_k$. Thus, the stability of $\hat{h}$ is guaranteed. The same concept is applied to $\hat{q}_t$ as well when assuming $P$ is zero.

Properties in detrained air parcel are determined by

$$
 h^t  =  \hat{h}(z_T) \, ,
$$

$$
 q^t  =  \hat{q}(z_T) \, , \mathrm{and}
$$

$$
 l^t  =  \hat{l}(z_T) \,,
$$

where superscript $t$ denote detrained properties.

### Spectral representation

Following the spirit of the Arakawa–Schubert scheme, cloud types are spectrally represented. The Arakawa–Schubert scheme considered different types of clouds according to different values of the entrainment rate. In the scheme developed here, however, the entrainment rate is calculated using Eq. (2).

In the Arakawa–Schubert scheme, a cloud-top level is first given and then the entrainment rate corresponding to the level is inversely solved. Since the formulation of entrainment rate is more complicated here, mathematically there is no guarantee that cloud-base updraft velocity that corresponds to the midst of a given cloud-top level always exists. Therefore, different values of cloud-base updraft velocity are first given from the minimum to the maximum with a fixed interval. The minimum and maximum values are set at 0.1 and 1.4 m/s2, with an interval of 0.1 m/s2.

In-cloud properties are then integrated upward with Eqs. (2), (4), (5), (6), and (7). This upward integration continues even if the buoyancy is negative as long as the updraft velocity is positive. If the velocity becomes negative at some point, the parcel detrains at the neutral buoyancy level that is below and closest to the point. That is, the scheme automatically judges whether the rising parcel can penetrate the negative buoyancy layers when there is a positive buoyancy layer above. The effect of CIN near cloud base is also represented by this. Note, however, that an effect of overshooting above cloud top is not included for simplicity (i.e., detrainment never occurs above cloud top).

A numerical scheme for solving the set of the equations is devised considering accuracy, stability, and column conservation of mass, energy, and water. The details are described in appendix A. For determination of $\hat{h}$ and $\hat{q}_t$ at cloud base, see appendix B

### Cloud-base mass flux

Cloud-base mass flux is determined with the prognostic convective kinetic energy closure proposed by Arakawa and Xu (1990). That is, cloud kinetic energy for each cloud type is explicitly predicted by

$$
 \frac{\partial K}{\partial t} = AM_B - \frac{K}{\tau_p}\,,  \qquad\tag{8}
$$

where $K$ and $A$ are cloud kinetic energy and cloud work function, respectively, and $t_p$ denotes a time scale of dissipation. Cloud work function $A$ is defined as

$$
 A \equiv \int_{z_B}^{z_T} B \eta \,dz\,.
$$

The energy is linked with $M_B$ by

$$
 K = \alpha M_B^2.
$$

Cloud-base mass flux is then solved for each cloud type ($\tau_p$ and $\alpha$ are set at $1.0 \times 10^3\, \mathrm{s}$ and $5.0 \times 10^7\, \mathrm{kg}^{-1} \mathrm{m}^4$, respectively).

### Microphysics

The method to obtain temperature and specific humidity of in-cloud air from moist static energy is identical to that in Arakawa and Schubert (1974). The ratio of precipitation to the total amount of condensates generated from cloud base to a given height $z$ is expressed by

$$
 F_p(z) = 1 - e^{-(z - z_B - z_0)/z_p},
$$

where $z_0$ and $z_p$ are set at 1.5 and 4 km, respectively.

The ratio of ice cloud to cloud water is determined simply by a linear function of temperature,

$$
 F_i(T) = \begin{cases} 1 & T \leq T_1 \\ (T_2 - T)/(T_2 - T_1) & T_1 < T < T_2 \\ 0  & T \geq T_2 \end{cases}
$$

where $T_1$ and $T_2$ are set at 258.15 and 273.15 K. The ratio of snowfall to precipitation is also determined by this function.

From the conservation of condensate static energy, $C_p T + gz + L_v q - L_i q_i$, for a cloud parcel, $Q_i$ in Eq. (5) is written as

$$
 Q_i = L_i \left(\frac{\partial \eta \hat{q}_i}{\partial z} - \epsilon\eta\bar{q}\right)_i
$$

and discretized as

$$
 {Q_i}_k = L_i \left(\frac{\eta_{k+1/2} {\hat{q}_i}_{k+1/2} - \eta_{k-1/2} {\hat{q}_i}_{k-1/2}}{\Delta z_k} - E_k {\bar{q}_i}_k \right)
$$

Strictly, the ratio of ice to water should be recalculated after the modification of temperature by $Q_i$ and the iterations are required; however, it is omitted for simplicity.

Melting and freezing of precipitation occurs depending on wet-bulb temperature of large-scale environment and cumulus mass flux.

### Evaporation, sublimation and downdraft

A part of precipitation is evaporated at each level as

$$
 E_v = a_e (\bar{q}_w - \bar{q}) \left(\frac{P}{V_T}\right),
$$

where $E_v, q_w, P,$ and $V_T$ are the mass of evaporation per a unit volume and time, wet-bulb saturated specific humidity, precipitation, and terminal velocity of precipitation, respectively, and $a_e$ is a constant. Here, $a_e$ and $V_T$ are taken as $0.3 \,\mathrm{s}^{-1}$ and $5 \,\mathrm{m}\,\mathrm{s}^{-1}$, respectively. Downdraft mass flux $M_d$ is generated as

$$
 \frac{\partial M_d}{\partial z} = -b_e \bar{\rho} (\bar{T}_w - \bar{T}) P,
$$

where $\rho$ and $T_w$ are density and wet-bulb temperature, respectively; $b_e$ is a constant set at $5\times10^{-4} \,\mathrm{m}^2 \,\mathrm{kg}^{-1} \,\mathrm{K}^{-1}$. Properties of downdraft air are determined by budget equations and the detrainment occurs at neutral buoyancy level and below cloud base.

If precipitation is composed of both rain and snow, the rain (snow) is evaporated (sublimated) in the same ratio as the ratio of rain (snow) to total precipitation when the precipitation evaporates to produce downdrafts.

### Cloudiness

Fractional cloudiness used in the radiation scheme is expressed by

$$
 C = \frac{C_\mathrm{max} - C_\mathrm{min}}{\ln M_\mathrm{max} - \ln M_\mathrm{min}}(\ln M - \ln M_\mathrm{min}) + C_\mathrm{min},
$$

where $C_\mathrm{max}, C_\mathrm{min}, M_\mathrm{max}, M_\mathrm{min},$and $M$ are the maximum and minimum values of the cloudiness and cumulus mass flux and the total cumulus mass flux, respectively; $C_\mathrm{max}, C_\mathrm{min}, M_\mathrm{max},$ and $M_\mathrm{min}$ are set at $0.1, 1 \times 10^{-3}, 0.3 \,\mathrm{kg} \,\mathrm{m}^{-2} \,\mathrm{s}^{-1},$and $2 \times 10^{-3} \,\mathrm{kg} \,\mathrm{m}^{-2} \,\mathrm{s}^{-1}$, respectively.

The grid mean liquid cloud mixing ratio is given by

$$
 l_c = \frac{\beta C}{M} \sum_i \hat{q}_l^i M^i,
$$

where $i$ denotes an index of cloud type, $q_l$ is liquid water, and $\beta$ is a dimensionless constant set at 0.1. The grid mean ice cloud mixing ratio is determined similarly.

### Cumulus Momentum Transport

The tendencies of zonal and meridional momentum by cumulus momentum transport are calculated as

$$
 \left(\frac{\partial u}{\partial t}\right)_{\mathrm{CMT},k} = -g\frac{(\rho\overline{u'w'})_{k+1/2} - (\rho\overline{u'w'})_{k-1/2}}{\Delta p_k}, \,\mathrm{and}
$$

$$
 \left(\frac{\partial v}{\partial t}\right)_{\mathrm{CMT},k} = -g\frac{(\rho\overline{v'w'})_{k+1/2} - (\rho\overline{v'w'})_{k-1/2}}{\Delta p_k},
$$

respectively, where $\rho\overline{u'w'}$ and $\rho\overline{v'w'}$ are total zonal and meridional momentum flux, respectively. This total momentum fluxes are carried by both cumulus updrafts and downdrafts.
