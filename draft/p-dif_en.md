## Turbulence scheme
The turbulence scheme represents the effect of subgrid-scale turbulence on the grid-averaged quantities. The turbulence scheme accounts for the vertical diffusion of momentum, heat, water and other tracers. The Mellor-Yamada-Nakanishi-Niino scheme (the MYNN scheme; Nakanishi 2001; Nakanishi and Niino 2004), an improved version of the Mellor-Yamada scheme (Mellor 1973; Mellor and Yamada 1974; Mellor and Yamada 1982), has been used as the turbulence scheme in MIROC since version 5. Closure level is 2.5. Level 3 is also available, but it is a non-standard option because it does not provide a performance gain worth the increase in computation.

In the MYNN scheme, liquid water potential temperature $\theta_l$ and total water $q_w$ are used as thermodynamic variables and are defined as follows, respectively. These are conserved quantities that do not depend on the phase change of water.

$$ \theta_l \equiv \left(T - \frac{L_v}{C_p}q_l - \frac{L_v+L_f}{C_p}q_i \right) \left(\frac{p_s}{p}\right)^{\frac{R_d}{C_p}} $$

$$ q_w \equiv q_v+q_l+q_i $$

where $T$ and $p$ are temperature and pressure; $q_v$, $q_l$, and $q_i$ are specific humidity, cloud water, and cloud ice; $C_p$ and $R_d$ are specific heat at constant pressure and gas constant of dry air; and $L_v$ and $L_f$ are latent heat of vaporization and per unit mass, respectively. $p_s$ is 1000 hPa.

In Level 2.5, the amount of kinetic energy of turbulence multiplied by two is a forecast variable, and its time evolution is also calculated within this scheme. This value is defined by

$$q^2 \equiv \langle u^2 + v^2 + w^2 \rangle$$

where $u$, $v$, and $w$ are velocities in the zonal, meridional, and vertical directions, respectively. Hereafter in this chapter, uppercase variables will represent grid mean quantities, and the lowercase variables will represent the deviation from them. $\langle \ \rangle$ denotes an ensemble mean. For Level 3,  $\langle {\theta_l}^2 \rangle$, $\langle {q_w}^2 \rangle$, $\langle \theta_l q_w \rangle$ are also forecast variables, but the details are not explained here.

The outline of the calculation procedure is given as follows along with the names of the subroutines.

1. calculation of the friction velocity and the Monin-Obukhov length
2. calculation of the buoyancy coefficients in consideration of partial condensation [`VDFCND`]
3. calculation of the stability functions in Level 2 [`VDFLEV2`]
4. calculation of the depth of the planetary boundary layer [`PBLHGT`]
5. calculation of the master turbulent length scale [`VDFMLS`]
6. calculation of the diffusion coefficients, and the vertical fluxes and their derivatives [`VDFLEV3`]
7. calculation of the generation and dissipation terms of turbulent flow [`VDFLEV3`]
8. computation of implicit time integration of prognostic variables

### Surface boundary layer
The friction velocity $u_*$ and the Monin-Obukhov length $L_M$ are given as follows.

$$u_*=\left({\langle uw \rangle_g}^2+{\langle vw \rangle_g}^2 \right)^\frac{1}{4}$$

$$L_M=-\frac{\Theta_{v,g} {u_*}^3}{kg \langle w\theta_v \rangle_g}$$

where the subscript $g$ indicates that the value is near the surface of the earth, and the value of the lowest layer of the model is used. $\Theta_v$ and $\theta_v$ denote virtual potential temperature, $k$ the Von Karman constant, and $g$ the gravitational acceleration.

### Diagnosis of the buoyancy coefficients
The calculation of the buoyancy term appearing in the turbulence equation requires the value of $\langle w\theta_v \rangle$. Following Mellor (1982), this term can be written as

$$\langle w\theta_v \rangle=\beta_\theta \langle w\theta_l \rangle + \beta_q \langle wq_w \rangle$$

by assuming a probability distribution in the grid of $\theta_l$, $q_w$. However, unlike Mellor (1982) and Nakanishi and Niino (2004), the probability distribution is not Gaussian, but triangular in shape as given by the PDF-based prognostic large-scale condensation scheme (Watanabe et al. 2008). The buoyancy coefficients $\beta_\theta$, $\beta_q$ are written as follows.

$$\beta_\theta=1+\epsilon Q_w-(1+\epsilon)Q_l-Q_i-\tilde{R}abc$$

$$\beta_q=\epsilon \Theta +\tilde{R}ac$$

where $\epsilon=R_v/R_d-1$. $R_d$ and $R_v$ are the gas constants for dry air and water vapor, respectively. Also,

$$a=\left(1+\frac{L_v}{C_p}\left.\frac{\partial Q_s}{\partial T}\right|_{T=T_l}\right)^{-1}$$

$$b=\frac{T}{\Theta}\left.\frac{\partial Q_s}{\partial T}\right|_{T=T_l}$$

$$c=\frac{\Theta}{T}\frac{L_v}{C_p}\left[1+\epsilon Q_w-(1+\epsilon)Q_l-Q_i\right]-(1+\epsilon)\Theta$$

$$\tilde{R}=R\left\{1-a\left[Q_w-Q_s(T_l)\right]\frac{Q_l}{2\sigma_s}\right\}-\frac{{Q_l}^2}{4{\sigma_s}^2}$$

$${\sigma_s}^2=\langle {q_w}^2 \rangle -2b \langle \theta_l q_w \rangle + b^2\langle {\theta_l}^2 \rangle$$

where $R,Q_l$ are the amount of cloud and liquid water diagnosed from the probability distribution in the grid, respectively, and $Q_s$ is the amount of saturated water vapor.

### Stability functions in the Level 2
It is known that the Mellor-Yamada Level 2.5 scheme fails to capture the behavior of growing turbulence realistically (Helfand and Labraga 1988). Therefore, the MYNN scheme first calculates the kinetic energy of turbulence at Level2, ${q_2}^2/2$, where the local equilibrium is assumed, and then applies a correction when $q<q_2$, i.e., the turbulence is in the growth phase. The stability functions $S_{H2},S_{M2}$ of Level 2, which are required for the calculation of $q_2$, can be obtained as follows.

$$S_{H2}=S_{HC}\frac{Rf_c-Rf}{1-Rf}$$

$$S_{M2}=S_{MC}\frac{R_{f1}-Rf}{R_{f2}-Rf}S_{H2}$$

where $Rf$ denotes the flux Richardson number which is given as follows.

$$Rf=R_{i1}\left(Ri+R_{i2}-\sqrt{Ri^2-R_{i3}Ri+R_{i4}}\right)$$

$Ri$ is the gradient Richardson number calculated as follows.

$$Ri=\frac{g}{\Theta}\left(\beta_\theta \frac{\partial \Theta_l}{\partial z}+\beta_q \frac{\partial Q_w}{\partial z}\right) \Bigg/ \left[ \left(\frac{\partial U}{\partial z}\right)^2+\left(\frac{\partial V}{\partial z}\right)^2 \right]$$

The other symbols are quantities that are independent of the environmental field and are given as follows.

$$S_{HC}=3A_2(\gamma_1+\gamma_2)$$

$$S_{MC}=\frac{A_1}{A_2}\frac{F_1}{F_2}$$

$$Rf_c=\frac{\gamma_1}{\gamma_1+\gamma_2}$$

$$R_{f1}=B_1\frac{\gamma_1-C_1}{F_1}$$

$$R_{f2}=B_1\frac{\gamma_1}{F_2}$$

$$R_{i1}=\frac{1}{2S_{Mc}}$$

$$R_{i2}=R_{f1}S_{MC}$$

$$R_{i3}=4R_{f2}S_{MC}-2R_{i2}$$

$$R_{i4}={R_{i2}}^2$$

where

$$A_1=B_1\frac{1-3\gamma_1}{6}$$

$$A_2=A_1\frac{\gamma_1-C_1}{\gamma_1 Pr}$$

$$C_1=\gamma_1-\frac{1}{3A_1{B_1}^{\frac{1}{3}}}$$

$$F_1=B_1(\gamma_1-C_1)+2A_1(3-2C_2)+3A_2(1-C_2)(1-C_5)$$

$$F_2=B_1(\gamma_1+\gamma_2)-3A_1(1-C_2)$$

$$\gamma_2=\frac{B_2}{B_1}\left(1-C_3\right)+\frac{2A_1}{B_1}\left(3-2C_2\right)$$

and

$$
(Pr,\gamma_1,B_1,B_2,C_2,C_3,C_4,C_5)=(0.74,0.235,24.0,15.0,0.7,0.323,0.0,0.2)
$$

### Master turbulent length scale

#### Formulation by Nakanishi (2001)
Nakanishi (2001) proposed the following formula as the master length scale $L$.

$$\frac{1}{L}=\frac{1}{L_S}+\frac{1}{L_T}+\frac{1}{L_B} \tag{1} $$

$L_S, L_T, L_B$ represent the length scales in the surface layer, convective boundary layer, and stably stratified layer, respectively, and are formulated as follows.

$$
L_S=\left\{
    \begin{array}{lr}
      kz/3.7, &\zeta\ge 1\\
      kz/(2.7+\zeta), &0\le\zeta< 1\\
      kz(1-\alpha_4\zeta)^{0.2}, &\zeta< 0\\
    \end{array}
  \right.
$$

$$L_T=\alpha_1\frac{\displaystyle \int_0^\infty{qz}\,dz}{\displaystyle \int_0^\infty{q}\,dz}$$

$$
L_B=\left\{
    \begin{array}{ll}
      \alpha_2 q/N, &\partial\Theta_v/\partial z> 0 \quad\rm{and}\quad\zeta\ge 0\\
      \left[\alpha_2+\alpha_3\sqrt{q_c/L_TN}\right]q/N, &\partial\Theta_v/\partial z> 0 \quad\rm{and}\quad\zeta< 0\\
      \infty, &\partial\Theta_v/\partial z\le 0\\
    \end{array}
  \right.
$$

where $\zeta\equiv z/L_M$ is the height normalized by the Monin-Obukhov length $L_M$, $N\equiv\left[(g/\Theta)(\partial\Theta_v/\partial z)\right]^{1/2}$ is the Brunt-Väisälä frequency, and $q_c\equiv [(g/\Theta)\langle w\theta_v \rangle_gL_T]^{1/3}$ is the velocity scale in the convective boundary layer.

#### Modifications in the implementation for MIROC
The above formulation in Nakanishi (2001) is appropriate when the domain of the model is limited to the atmospheric boundary layer and its peripheral region.
However, when the model includes the upper troposphere, problems such as follows may arise depending on the conditions: $L_T$, the length scale of the convective boundary layer, is used in the free atmosphere, and the turbulent energy in the free atmosphere is included as $q$ in the calculation of $L_T$.

Therefore, for implementation in MIROC, the top height of the convective boundary layer $H_{PBL}$ is estimated and the region below $h=\sqrt{(F_H H_{PBL})^2+H_0^2}$ is considered as the region where boundary-layer turbulence is dominant. Here, $F_H=1.5$ and $H_0=500$m.

Below the altitude $h$, equation (1) is used as the master length scale, but in $L_T$, the range of integration is modified as follows.

$$\frac{1}{L}=\frac{1}{L_S}+\frac{1}{L_A}+\frac{1}{L_{max}}$$

where $L_A=\alpha_5\,q/N$ is the length scale when an air mass moves vertically due to turbulence in stable stratification. $\alpha_5$ represents the effect of dissipation and $\alpha_5=0.53$.  $L_{max}=500$m gives the upper limit of $L$.

#### Estimation of the top height of the convection boundary layer
Based on Holtslag and Boville (1993), the estimate of $H_{PBL}$ is calculated using the bulk Richardson number $Ri_B$ given as follows.

$$Ri_B=\frac{[g/\Theta_v(z_1)][\Theta_v(z_k)-\Theta_{v,g}](z_k-z_g)}{[U(z_k)-U(z_1)]^2+[V(z_k)-V(z_1)]^2+F_u{u_*}^2}$$

where $z_k$ is the full level altitude of the kth layer from the bottom, $z_1$ is the full level altitude of the lowest layer of the model, and $z_g$ is the surface altitude. $F_u$ is a dimensionless tuning parameter. Also,

$$\Theta_{v,g}=\Theta_v(z_1)+F_b \frac{\langle w\theta_v \rangle_g}{w_m}$$

$$w_m=u_*/\phi_m$$

$$\phi_m=\left(1-15\frac{z_s}{L_M}\right)^{-\frac{1}{3}}$$

where $z_s$ is the altitude of the surface layer, and $z_s=0.1H_{PBL}$. $F_b$ is a dimensionless tuning parameter.

$Ri_B$ is calculated in turn from $k=2$ upward, and is linearly interpolated between the layer where $Ri_B>0.5$ for the first time and the layer immediately below it. The height where $Ri_B=0.5$ exactly is used as $H_{PBL}$. Since $H_{PBL}$ is required for the calculation of $z_s$, $H_{PBL}$ is first calculated using $z_s$ with the temporary value $H_{PBL}=z_1-z_g$ substituted, and then the true $H_{PBL}$ is recalculated using $z_s$ with this $H_{PBL}$ substituted.

### Calculation of diffusion coefficients

#### Turbulent kinetic energy in the Level 2
The turbulent kinetic energy of level 2, ${q_2}^2/2$, is calculated from the following equation, which neglects the time derivative, advection, and diffusion terms in the time evolution equation of the turbulent kinetic energy.

$$ P_s + P_b - \varepsilon = 0 \tag{2} $$

where $P_s$, $P_b$, $\varepsilon$ denote the generation term by shear, the generation term by buoyancy, and the dissipation term, respectively. $P_s$, $P_b$ are represented as follows.

$$ P_s = -\langle wu \rangle \frac{\partial U}{\partial z} - \langle wv \rangle \frac{\partial V}{\partial z} $$

$$ P_b = \frac{g}{\Theta}\langle w\theta_v \rangle $$

In the Level 2 of the MYNN scheme, they are written as follows.

$$ P_s = LqS_{M2} \left[ \left(\frac{\partial U}{\partial z}\right)^2 + \left(\frac{\partial V}{\partial z}\right)^2 \right] \tag{3} $$

$$ P_b = LqS_{H2} \frac{g}{\Theta}\left[ \beta_\theta \frac{\partial \Theta_l}{\partial z} + \beta_q \frac{\partial Q_w}{\partial z} \right] \tag{4} $$

$$ \varepsilon = \frac{q^3}{B_1 L} \tag{5} $$

From (2), (3), (4), and (5), ${q_2}^2$ is calculated as follows.

$${q_2}^2=B_1L^2\left\{S_{M2}\left[\left(\frac{\partial U}{\partial z}\right)^2+\left(\frac{\partial V}{\partial z}\right)^2\right]+S_{H2}\frac{g}{\Theta}\left(\beta_\theta \frac{\partial \Theta_l}{\partial z}+\beta_q \frac{\partial Q_w}{\partial z}\right)\right\}$$

#### Stability functions in the Level 2.5
When $q<q_2$, i.e., the turbulence is in the growth phase, the stability functions of level 2.5, $S_M$ and $S_H$, are calculated as follows using the coefficient $\alpha=q/q_2$ introduced by Helfand and Labraga (1998).

$$S_M=\alpha S_{M2},\quad S_H=\alpha S_{H2}$$

On the other hand, when $q \geq q_2$, $S_M$ and $S_H$ are calculated as follows. The following equations differ from those in Nakanishi (2001) in the description method, but gives equivalent results with less computation.

$$S_M=A_1\frac{E_3-3C_1 E_4}{E_2 E_4+E_5 E_3}$$

$$S_H=A_2\frac{E_2+3C_1 E_5}{E_2 E_4+E_5 E_3}$$

where

$$E_1=1-3A_2B_2(1-C_3)G_H$$

$$E_2=1-9A_1A_2(1-C_2)G_H$$

$$E_3=E_1+9{A_2}^2(1-C_2)(1-C_5)G_H$$

$$E_4=E_1-12A_1A_2(1-C_2)G_H$$

$$E_5=6{A_1}^2G_M$$

$$G_M=\frac{L^2}{q^2}\left[\left(\frac{\partial U}{\partial z}\right)^2+\left(\frac{\partial V}{\partial z}\right)^2\right]$$

$$G_H=-\frac{L^2}{q^2}\frac{g}{\Theta}\left(\beta_\theta \frac{\partial \Theta_l}{\partial z}+\beta_q \frac{\partial Q_w}{\partial z}\right)$$

#### Calculation of diffusion coefficients
The diffusion coefficients $K_M$, $K_q$, $K_H$, and $K_w$ for wind speed, turbulent energy, heat, and water are calculated as follows from $S_M,S_H$.

$$K_M=LqS_M$$

$$K_q=3LqS_M$$

$$K_H=LqS_H$$

$$K_w=LqS_H$$

#### Calculation of fluxes
The vertical flux $F$ of each physical quantity is calculated as follows.

$$F_{u,k-1/2}=-\rho_{k-1/2}K_{M,k-1/2}\frac{U_{k}-U_{k-1}}{\Delta z_{k-1/2}}$$

$$F_{v,k-1/2}=-\rho_{k-1/2}K_{M,k-1/2}\frac{V_{k}-V_{k-1}}{\Delta z_{k-1/2}}$$

$$F_{q,k-1/2}=-\rho_{k-1/2}K_{q,k-1/2}\frac{{q^2}_ {k}-{q^2}_ {k-1}}{\Delta z_{k-1/2}}$$

$$F_{T,k-1/2}=-\rho_{k-1/2}K_{H,k-1/2}\,C_p\Pi_{k-1/2}\frac{\Theta_{l,k}-\Theta_{l,k-1}}{\Delta z_{k-1/2}}$$

$$F_{w,k-1/2}=-\rho_{k-1/2}K_{w,k-1/2}\frac{Q_{w,k}-Q_{w,k-1}}{\Delta z_{k-1/2}}$$

where $\rho$ is density and $\Pi$ is the Exner function. In order to perform time integration with implicit scheme, the derivative of each vertical flux is also obtained as follows.

$$\frac{\partial F_{u,k-1/2}}{\partial U_{k-1}}=\frac{\partial F_{v,k-1/2}}{\partial V_{k-1}}=-\frac{\partial F_{u,k-1/2}}{\partial U_{k}}=-\frac{\partial F_{v,k-1/2}}{\partial V_{k}}=\rho_{k-1/2}K_{M,k-1/2}\frac{1}{\Delta z_{k-1/2}}$$

$$\frac{\partial F_{q,k-1/2}}{\partial {q^2}_ {k-1}}=-\frac{\partial F_{q,k-1/2}}{\partial {q^2}_ {k}}=\rho_{k-1/2}K_{q,k-1/2}\frac{1}{\Delta z_{k-1/2}}$$

$$\frac{\partial F_{T,k-1/2}}{\partial T_{k-1}}=\rho_{k-1/2}K_{H,k-1/2}C_p\frac{\Pi_{k-1/2}}{\Pi_{k-1}}\frac{1}{\Delta z_{k-1/2}}$$

$$\frac{\partial F_{T,k-1/2}}{\partial T_{k}}=-\rho_{k-1/2}K_{H,k-1/2}C_p\frac{\Pi_{k-1/2}}{\Pi_{k}}\frac{1}{\Delta z_{k-1/2}}$$

$$\frac{\partial F_{w,k-1/2}}{\partial Q_{w,k-1}}=-\frac{\partial F_{w,k-1/2}}{\partial Q_{w,k}}=\rho_{k-1/2}K_{w,k-1/2}\frac{1}{\Delta z_{k-1/2}}$$

where $\Delta z_{k-1/2}=z_k-z_{k-1}$. The fluxes for other tracers are also calculated in the same way using $K_w$.

### Calculation of turbulent variables

#### Calculation of turbulent kinetic energy
The prognostic equation for $q^2$ is expressed as follows.

$$ \frac{d q^2}{dt}=-\frac{1}{\rho}\frac{\partial F_q}{\partial z}+2\left(P_s+P_b-\varepsilon\right) $$

In the Level 2.5, $P_s,P_b,\varepsilon$ are written as follows.

$$P_s=Lq S_M \left[\left(\frac{\partial U}{\partial z}\right)^2+\left(\frac{\partial V}{\partial z}\right)^2\right]$$

$$P_b=Lq S_H \frac{g}{\Theta}\left(\beta_\theta \frac{\partial \Theta_l}{\partial z}+\beta_q \frac{\partial Q_w}{\partial z}\right)$$

$$\varepsilon=\frac{q^3}{B_1L}$$

Advection terms are calculated using tracer transport routines in the dynamics scheme. In the turbulence scheme, the time evolution by diffusion, generation and dissipation terms of $q^2$ is calculated by the implicit scheme.

#### Diagnosis of variance and covariance
The prognostic equations for $\langle {\theta_l}^2 \rangle,\langle {q_w}^2 \rangle,\langle \theta_l q_w \rangle$ are expressed as follows.

$$
\frac{d\left\langle{\theta_l}^{2}\right\rangle}{d t}=-\frac{\partial}{\partial z}\left\langle w \theta_{l}^{2}\right\rangle-2\left\langle w \theta_{l}\right\rangle \frac{\partial \Theta_{l}}{\partial z}-2 \varepsilon_{\theta l}
$$

$$
\frac{d\left\langle {q_w}^{2}\right\rangle}{d t}=-\frac{\partial}{\partial z}\left\langle w q_{w}^{2}\right\rangle-2\left\langle w q_{w}\right\rangle \frac{\partial Q_{w}}{\partial z}-2 \varepsilon_{q w}
$$

$$
\frac{d\left\langle\theta_{l} q_{w}\right\rangle}{d t}=-\frac{\partial}{\partial z}\left\langle w \theta_{l} q_{w}\right\rangle-\left\langle w q_{w}\right\rangle \frac{\partial \Theta_{l}}{\partial z}-\left\langle w \theta_{l}\right\rangle \frac{\partial Q_{w}}{\partial z}-2 \varepsilon_{\theta q}
$$

In the Level 2.5, the time derivative, advection, and diffusion terms in these equations are ignored, and the following balances are assumed locally.

$$ -\left\langle w \theta_{l}\right\rangle \frac{\partial \Theta_{l}}{\partial z}-\varepsilon_{\theta l} = 0 \tag{6}$$

$$ -\left\langle w q_{w}\right\rangle \frac{\partial Q_{w}}{\partial z}-\varepsilon_{q w} = 0 \tag{7}$$

$$ -\left\langle w q_{w}\right\rangle \frac{\partial \Theta_{l}}{\partial z}-\left\langle w \theta_{l}\right\rangle \frac{\partial Q_{w}}{\partial z}-2 \varepsilon_{\theta q} = 0 \tag{8}$$

In the Level 2.5 of MYNN scheme, $-\left\langle w \theta_{l}\right\rangle$, $-\left\langle w q_{w}\right\rangle$, $\varepsilon_{\theta l}$, $\varepsilon_{q w}$, $\varepsilon_{\theta q}$ are represented as follows.

$$ -\left\langle w \theta_{l}\right\rangle = LqS_H \frac{\partial \Theta_{l}}{\partial z} \tag{9}$$

$$ -\left\langle w q_{w}\right\rangle = LqS_H \frac{\partial Q_{w}}{\partial z} \tag{10}$$

$$
\varepsilon_{\theta l}=\frac{q}{B_{2} L}\left\langle\theta_{l}^{2}\right\rangle \tag{11}
$$

$$
\varepsilon_{q w}=\frac{q}{B_{2} L}\left\langle q_{w}^{2}\right\rangle \tag{12}
$$

$$
\varepsilon_{\theta q}=\frac{q}{B_{2} L}\left\langle\theta_{l} q_{w}\right\rangle \tag{13}
$$

from (6)-(13), $\langle {\theta_l}^2 \rangle$, $\langle {q_w}^2 \rangle$, $\langle \theta_l q_w \rangle$ can be diagnosed as follows.

$$\langle {\theta_l}^2 \rangle =B_2L^2S_H\left(\frac{\partial \Theta_l}{\partial z}\right)^2$$

$$\langle {q_w}^2 \rangle =B_2L^2S_H\left(\frac{\partial Q_w}{\partial z}\right)^2$$

$$\langle \theta_l q_w \rangle =B_2L^2S_H\frac{\partial \Theta_l}{\partial z}\frac{\partial Q_w}{\partial z}$$

#### Treatment in the bottom layer
Since the lowest layer of the model corresponds to the ground layer where the vertical gradient of geophysical quantities change rapidly, the following Monin-Obukhov similarity theory is used to evaluate the vertical gradient accurately.

$$ \frac{\partial M}{\partial z} = \frac{u_*}{kz}\phi_m \tag{14}$$

$$ \frac{\partial \Theta}{\partial z} = \frac{\theta_*}{kz}\phi_h \tag{15}$$

$$ \frac{\partial Q_v}{\partial z} = \frac{q_{v*}}{kz}\phi_h \tag{16}$$

where $M$ is the wind speed when the horizontal axis is in the direction of the horizontal wind in the surface layer. $\phi_m$ and $\phi_h$ are the dimensionless gradient functions for momentum and heat, respectively. $\theta_*$, $q_{v*}$ are the scales of potential temperature and water vapor in the surface layer, respectively, and satisfy the following relationships.

$$ \langle wm \rangle_g = -u_*^2 \tag{17}$$

$$ \langle w\theta \rangle_g = -u_*\theta_* \tag{18}$$

$$ \langle wq_v \rangle_g = -u_*q_{v*} \tag{19}$$

$m$ is the deviation of $M$ from the grid average. Using $M$ and $m$, the generation term of turbulence kinetic energy can be written as

$$ P_s + P_b = \langle wm \rangle \frac{\partial M}{\partial z} + \frac{g}{\Theta} \langle w\theta_v \rangle $$

Using (14), (17) and the defining equation of the Monin-Obukhov length, this can be calculated as follows.

$$ P_s + P_b = \frac{u_*^3}{kz_1}\left[\phi_m\left(\zeta_1\right)-\zeta_1\right] $$

Here, $\zeta_1$ is $\zeta$ at the full level of the lowest layer of the model.

By assuming that there are no cloud particles in the surface layer, $\langle {\theta_l}^2\rangle$, $\langle {q_w}^2\rangle$, $\langle \theta_lq_w\rangle$ can be calculated diagnostically from (6)-(8), (11)-(13), (15), (16), (18), and (19) as follows.

$$\langle {\theta_l}^2\rangle=\frac{\phi_h\left(\zeta_1\right)}{u_*kz_1}{\langle w\theta \rangle_g}^2 \bigg/ \frac{q}{B_2L} $$

$$\langle {q_w}^2\rangle=\frac{\phi_h\left(\zeta_1\right)}{u_*kz_1}{\langle wq_v\rangle_g}^2 \bigg/ \frac{q}{B_2L} $$

$$\langle \theta_lq_w\rangle=\frac{\phi_h\left(\zeta_1\right)}{u_*kz_1}\langle w\theta \rangle_g\langle wq_v \rangle_g \bigg/ \frac{q}{B_2L} $$

$\phi_m,\phi_h$ are formulated as follows based on Businger et al. (1971).

$$
\phi_m(\zeta)=\left\{
    \begin{array}{lr}
      1+\beta_1\zeta, &\zeta\ge 0\\
      \left(1-\gamma_1\zeta\right)^{-1/4}, &\zeta< 0\\
    \end{array}
  \right.
$$

$$
\phi_h(\zeta)=\left\{
    \begin{array}{lr}
      \beta_2+\beta_1\zeta, &\zeta\ge 0\\
      \beta_2\left(1-\gamma_2\zeta\right)^{-1/2}, &\zeta< 0\\
    \end{array}
  \right.
$$

$$(\beta_1,\beta_2,\gamma_1,\gamma_2)=(4.7,0.74,15.0,9.0)$$

### Time integration with implicit scheme