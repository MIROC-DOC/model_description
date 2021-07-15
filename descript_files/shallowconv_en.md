Shallow Convection Scheme
-------------------------

### Overview of Shallow Convection

Shallow convection is the most frequent type of convective cloud in the
tropics and subtropics Its impact on climate through the energy budget
due to atmospheric radiation is considered important (Stevens, 2005).
Shallow convection is responsible for transporting the boundary layer
air to the free atmosphere. It is often not accompanied by precipitation
and is characterized by the fact that precipitation-induced downdraft
does not reach the surface as in deep convection.

This section briefly describes the vertical structure of the boundary
layer favorable for shallow convection. When the ground surface is
heated by sunlight or cold air flows in from above, the energy of
convective instability is dissipated by turbulence in the bottom of the
atmosphere, forming a mixed layer with a nearly uniform vertical
distribution of potential temperature and water vapor at a thickness of
about 600 m to 800 m from the surface. At the upper end of the mixed
layer, there is a transition layer of weakly stable stratification,
which is the height at which water vapor in updraft begins to condense
(lifting condensation level, LCL). Above LCL, the temperature decreases
according to the moist adiabatic lapse rate, and the updraft is observed
as clouds. Above the level of free convection (LFC), the cloud continues
to grow while mixing with surrounding air. The growth of these
convective clouds is limited by the temperature inversion layer at the
lower end of the free atmosphere, and the cloud tops are often located
about 2 km from the surface.

In the former versions of MIROC, A cumulus parameterization proposed by
Chikira and Sugiyama (2010) deals with multiple cloud types including
shallow cumulus and deep convective clouds. However, it tends to
overestimate low-level cloud amounts. To cope with this bias and improve
the performance for reproducing current climate, the shallow convection
scheme is introduced from the 6th version of MIROC (Tatebe et al., 2019,
Ogura et al., 2017, Ogura, 2015)． The source code in concern (pshcn.F)
consists of `SUBROUTINE:[PSHCN]` and `SUBROUTINE:[DISTANCE]`. The input
values for `SUBROUTINE:[PSHCN]` are temperature, water vapor mixing
ratio, and liquid water mixing ratio, ice mixing ratio. It predicts
liquid water potential temperature, total water mixing ratio, ice mixing
ratio, and horizontal components of wind in response to vertical
transport. It also diagnoses cloud fraction and precipitation.
`SUBROUTINE:[DISTANCE]`, which is called inside `SUBROUTINE:[PSHCN]`,
calculates the degree of buoyancy-induced updraft and mixing with the
environment. Since the variables diagnosed in the cumulus scheme
(`SUBROUTINE:[CUMLUS]`) are referenced to determine the conditions for
shallow convection, `SUBROUTINE:[PSHCN]` is required to be run after
`SUBROUTINE:[CUMULUS]`, followed by the diagnosis of cloud fraction. On
the other hand, it should be run before the land surface process
`SUBROUTINE:[SURFCE]` because precipitation by convection is referenced
in the land surface and ocean models.

### Basics of Cloud Model

Subgrid clouds are modeled based on the frameworks proposed by
Bretherton et al. (2004) and Park and Bretherton (2009). This scheme
employs a simple plume model for cloud to calculate vertical transport
of conserved variables and precipitation due to updraft. An ensemble of
shallow convection in a horizontal grid, which is expressed as a single
updraft plume, is supposed to experience horizontal mixing with the
environment (entrainment/detrainment). The flux of vertical transport of
mass is assumed in the following form:
$$ \tag{def-Mu}
    \rho \overline {w' \psi '}\approx M_u (\psi_u-\overline{\psi}) ,$$
where $M_u=\rho_u\sigma_u w_u$ is mass flux of updraft
($\rho_u$,$\sigma_u$, and $w_u$ stand for density in updraft, area
fraction of updraft in a grid, and vertical velocity, respectively)，
$\psi_u$ is a conserved variable transported by convection (e.g. liquid
water potential temperature, total water mixing ratio, horizontal
components of momentum) in updraft， $\overline{\psi}$ denotes the
average value in the environmental field of the same conserved value.
The effects of vertical transport due to shallow convection are
represented by determining the vertical profiles of unknown values $M_u$
and $\psi_u$. Flux of mass and conserved values are diagnosed as
$$
    \frac{\partial M_u}{\partial z} = E - D \tag{zprof-Mu}
$$
$$
    \frac{\partial}{\partial z} (\psi_u M_u) = X_\psi + S_\psi M_u,\tag{zprof-psi} $$
where $X_\psi$ represents horizontal mixing with environmental air, and
$S_\psi$ is source term. $E$ and $D$ are rates of entrainment and
detrainment, which are described in fractional from
$$
    E =\epsilon M_u \tag{fracE}
$$
$$
    D =\delta M_u. \tag{fracD} $$ Substituting
$\overline{\psi}$ for grid value and assuming the horizontal mixing term
as $X_{\psi}=E \overline{\psi} - D\psi_u$ results in
$$
    \frac{\partial M_u}{\partial z} = M_u (\epsilon - \delta) \tag{zprof-Mu'}
$$
$$
    \frac{\partial \psi_u}{\partial z} = \epsilon(\overline{\psi} - \psi_u) + S_{\psi}. \tag{zprof-psi'}$$
In MIROC6, changes in liquid water potential temperature due to
precipitation and the effect of subgrid pressure gradient on horizontal
momentum are included in $S_{\psi}$. Consequently, equations
([zprof_Mu](zprof-Mu')) and ([zprof_psi](zprof-psi')) results in a closure problem of two parameters
$\delta$ and $\epsilon$. By determining $\delta$ and $\epsilon$ by the
formulation described in section
([0.1.3.4](diagnosing-vertical-profile-of-updraft-mass-flux)) and
solving differential equations along with boundary condition at cloud
base, vertical profiles of $M_u$ and $\psi_u$ are calculated.

### Computation in PSHCN {#computation-in-PSHCN}

The effect of convective updraft is calculated as follows.

-   Liquid water potential temperature $\theta_l$ and total water $q_t$
    are diagnosed from input temperature $T$, water vapor mixing ratio
    $q_v$, liquid water mixing ratio $q_l$, ice mixing ratio $q_i$,

-   Updraft mass flux at cloud base is diagnosed.

-   Height of cloud base is diagnosed.

-   Presence of shallow convection is determined.

-   Vertical profiles of $M_u$, $\theta_l$, $q_t$, horizontal wind
    components $u$ and $v$ are diagnosed.

-   $\theta_l$, $q_t$, $q_i$, $u$, $v$, liquid water temperature $T_l$
    are predicted.

-   $T$, $q_v$, and $q_l$ are diagnosed according to $T_l$ and $q_t$.

#### Lower boundary condition: diagnosis of cloud base mass flux {#lower-boundary-condition}

The mass flux at cloud base is formulated as it depends on turbulent
kinetic energy (TKE) in boundary layer and convective inhibition (CIN)
at the top of boundary layer.

Firstly, the vertical profile of updraft velocity is supposed to fulfill
$$\tag{zprof-wu}
    \frac{1}{2}\frac{\partial}{\partial z}w_u^2=aB_u-b\epsilon w_u^2$$
all over the layers with shallow convection. $B_u$ means updraft
buoyancy, $a$ and $b$ are empirical parameters. The first term of the
right-hand side of ([zprof_wu](zprof-wu)) is acceleration by buoyancy, and the second term
represents drag by entrainment. By assuming no entrainment below LFC and
integrating ([zprof_wu](zprof-wu)) from cloud base to LFC, The critical value of
upward velocity for updraft plume to reach LFC, $w_c$, can be determined

$$\tag{wc}
    w_c = \sqrt{2a(CIN)}.$$ Updrafts that exceed this critical value
penetrates from cloud base.

Computation of CIN is based on Appendix C of Bretherton et al.,
$$\begin{aligned}
\tag{def-CIN}
    CIN = [B_u(p_{base}) + B_u(p_{LCL})]\frac{p_{LCL}-p_{base}}{g(\rho_{LCL}+\rho_{base})} + B_u(p_{LCL})\frac{p_{LFC}-p_{LCL}}{g(\rho_{LFC}+\rho_{LCL})}.\end{aligned}$$
In the following, subscript $\mathit{base}$ represents the value at the
top of mixing layer. In MIROC6, for simplicity, $B_u(p_{base})$ is set
to zero.

Secondly, to obtain the information of vertical velocity at cloud base,
the statistical distribution of $w$ is assumed to follow Gaussian
distribution
$$\tag{distr-w}
    f(w) = \frac{1}{2\pi k_f e_{avg}}\exp\left[ -\frac{w^2}{2k_fe_{avg}}\right]$$
with variance equal to $k_f e_{avg}$, where $e_{avg}$ is average TKE
diagnosed in turbulent and vertical diffusion scheme. $k_f$ is an
empirical parameter describing the partitioning of TKE between
horizontal and vertical motions at the subcloud layer inversion, whose
recommended value based on large eddy simulation is 0.5.

By taking average of vertical velocity above the critical value $w_c$,
cloud base mass flux $M_{u,base}$ is diagnosed as
$$\tag{Mubase}
    M_{u,base}=\overline{\rho_{base}}\int_{w_c}^{\infty}wf(w)dw =\overline{\rho_{base}}\sqrt{\frac{k_f e_{avg}}{2\pi}}\exp\left[-\frac{w_c^2}{2k_fe_{avg}}\right],$$
where $\overline{\rho_{base}}$ is density at LFC. This mass flux is
larger for larger boundary layer TKE and smaller for larger CIN.

#### Diagnosing height of cloud base {#diagno-height-of-cloud-base}

The cloud base height is set between the top of the boundary layer and
the LCL. The larger the CIN is, the lower the cloud base becomes. The
top of boundary layer is diagnosed as the level with maximum vertical
gradient of relative humidity. Let $z_{Hi}$ be the higher of this level
and LCL, and $z_{Lo}$ be the lower, then the cloud base altitude
$z_{base}$ is set
$$\tag{zbase}
    z_{base} = z_{Hi} - (z_{Hi}-z_{Lo})\frac{CIN-CIN_{Lo}}{CIN_{Hi} - CIN_{Lo}}.$$
$CIN_{Hi}$ and $CIN_{Lo}$ are coefficients which satisfy
$CIN_{Lo}\le CIN \le CIN_{Hi}$ for a typical value of CIN.

#### Determination of the presence of shallow convection {#presence-of-shallow-convection}

For each horizontal column, whether shallow convection occurs is
determined with following criteria.

-   If estimated inversion strength (EIS; Wood and Bretherton, 2006)
    exceeds a certain threshold, the environmental field is judged to be
    dominated by stratocumulus clouds, and shallow convection is not
    generated. This criterion is introduced because the vertical
    resolution of climate models does not sufficiently represent the
    thin and strong inversion layer over the boundary layer, and
    underestimates CIN, which leads to an overestimation of shallow
    convection. EIS is estimated by
    $EIS=\theta_{700}-\theta_{0}-\Gamma_m^{850}(z_{700}-LCL)$ where
    $\theta_{700}$ and $\theta_0$ are potential temperature at 700hPa
    and surface, $\Gamma_m^{850}$ is moist adiabatic lapse rate at
    850hPa, and $z_{700}$ is height of 700hPa.

-   If the intensity of cumulus convection diagnosed by
    `SUBROUTINE:[CUMULUS]` exceeds a threshold, the environmental field
    is supposed to be dominated by deep convection and shallow
    convection is not generated.

-   If the areal fraction of shallow convection is under a threshold,
    computation of shallow convection is omitted.

#### Diagnosing vertical profile of updraft mass flux

For the grid boxes that contain shallow convection, entrainment and
detrainment is calculated using the value of $\psi_u$ at cloud base and
$M_{u,base}$. Fractional entrainment and detrainment are computed based
on the framework of buoyancy sorting suggested by Kain and Fritsch
(1990). In a layer of thickness $\delta z$, equal parts
$\epsilon_0 M_u \delta z$ of updraft and environmental air are involved
in the lateral mixing process that creates a spectrum of mixtures. This
yields a total mixing mass flux $2\epsilon_0 M_u \delta z$, with
fractional mixing rate $\epsilon_0=c_0/H$ ($c_0$ is a certain empirical
coefficient and $H$ is the height from surface). In the mixed air, there
exists states with probability density such that the air from the
environmental field occupies a proportion $\chi$. Here, for simplicity
of calculation, it is considered that the state from pure moist air
($\chi=0$) to pure environmental air ($\chi=1$) is distributed with
uniform probability (Kain-Fritsch scheme assumes Gaussian distribution).
Based on the buoyancy force on the mixed air, the entrainment or
detrainment is determined. `SUBROUTINE:[DISTANCE]` is called in
`SUBROUTINE:[PSHCN]`. The output variables in this subroutine are liquid
water potential temperature (THETLU) and bool value for entrainment or
detrainment (JUDGE).

The occurrence of entrainment is judged as follows. Firstly, if the
updraft air is not saturated, entrainment is not assumed to occur.
Nextly, with virtual potential energy in the environmental field
($\overline{\theta_v}$) and updraft ($\theta_{vu}$), buoyancy force on
the parcel is defined:
$$\tag{buoy-u}
    B_u = g\frac{\theta_{vu} - \overline{\theta_{v}}}{ \overline{\theta_v}}$$
and entrainment occurs when the buoyancy on parcel is positive.
Furthermore, even when the buoyancy is negative, entrainment occurs if
the parcel can travel longer than a certain eddy mixing distance
$l_c=c_1 H$, where $c_1=0.1$ is an empirical constant, chosen to
optimize the trade-cumulus case. This criterion corresponds to the
critical buoyancy value
$$\tag{buoy-c}
    B_c = -\frac{1}{2}\frac{w_u^2}{l_c}$$ and otherwise, all the mixed
air is detrained. Therefore, Once the critical value of the mixing state
$\chi_c$ is obtained, which allows the updraft to rise a distance $l_c$
under negative buoyancy, the air in the environmental field entrained
into the cloud and the air in the updraft that is detrained can be
determined as follows
$$
    M_u\epsilon=2\epsilon_0 M_u\int_0^{\chi_c}\chi q(\chi) d\chi = \epsilon_0 M_u \chi_c^2 \tag{flux-entre}
    $$
$$
    M_u\delta=2\epsilon_0 M_u\int_{\chi_c}^{1}(1-\chi) q(\chi) d\chi = \epsilon_0 M_u (1-\chi_c)^2. \tag{flux-detre}$$
Thus, letting
$$
    \epsilon=\epsilon_0\chi_c^2 \tag{Etilde}\\
$$
$$
    \delta=\epsilon_0(1-\chi_c)^2, \tag{Dtilde}$$
equatinons ([zprof_Mu](zprof-Mu')) and
([zprof_psi](zprof_psi')) are expressed as follows
$$
    \frac{1}{M_u}\frac{\partial M_u}{\partial z} = \epsilon - \delta = \epsilon_0(2\chi_c - 1) \tag{zprof-Mu-param}
$$
$$
    \frac{\partial \psi_u}{\partial z} = \epsilon (\overline{\psi}-\psi_u) + S_{\psi} = \epsilon_0\chi_c^2(\overline{\psi}-\psi_u) + S_{\psi}, \tag{zprof-psi-param}$$
where $\chi_c$ is computed based on virtual potential temperature of
mixed air
$$\tag{virt-pot-t}
    \theta_v(\chi)=\theta_{vu}+\chi\left[ \beta(\overline{\theta_l}-\theta_{lu})-\left(\frac{\beta L}{c_p\Pi}-\theta_u\right)(\overline{q_t}-q_{tu})\right]$$
(Bretherton et al., 2004). $\beta$ is a thermodynamic parameter which
depends on temperature and pressure defined by Randall (1980),
$\theta_{lu}$ is liquid water potential temperature in updraft,
$\theta_u$ is updraft potential temperature，$\overline{q_t}$ is total
water mixing ratio of environment， $q_{tu}$ is total water mixing ratio
of updraft, $L$ is latent heat of vaporization，$c_p$ is specific heat
capacity of dry air at constant pressure, and $\Pi$ is the Exner
function.

Consequently, the governing equations
([zprof_wu](zprof-wu)),
([zprof_Mu_param](zprof-Mu-param)), and
([zprof\_psi\_param](zprof-psi-param)) for vertical profiles of $w_u$, $M_u$, and
$\psi_u$ are obtained. These equations are discretized and integrated
upward one layer at a time using the lower boundary condition in section
[0.1.3.1](lower-boundary-condition) to yield the vertical profile of
each variables.

Afterward, from liquid water potential temperature and total water
mixing ratio, liquid water mixing ratio $q_l$ and water vapor mixing
ratio $q_v$ are diagnosed. The cloud water that exceeds a threshold is
disposed as rainwater $q_r$, and liquid water potential temperature is
updated according to the amount of $q_r$. This corresponds to $S_\psi$
in ([virt_pot_t](virt-pot-t)).

The formulation of the vertical flux in this scheme is equal to the
assumption that the updraft is not large enough to replace all of the
air in a grid box in the time step $\Delta t$. Therefore, the following
limiter is imposed to prevent numerical instability when diagnosing mass
flux of the updraft.
$$\tag{Mu-limit}
    M_u = min.\left(M_u, \frac{\rho\Delta z}{\Delta t}\right)$$
