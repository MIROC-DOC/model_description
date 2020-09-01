## Surface Processes.

### Overview of Surface Processes.

Surface processes provide boundary conditions at the lower edge of the atmosphere through the exchange of momentum, heat, and water fluxes between the atmosphere and the surface. The surface process evaluates the thermal inertia of the earth's surface, water accumulation, snow accumulation, sea ice accumulation, etc. by using original forecast variables such as temperature ($T_g$), moisture ($W_g$), and snow cover ($W_y$). The main input data are the diffusion of geophysical quantities between the atmosphere and the earth's surface, as well as radiation and precipitation fluxes. The output data consist of surface temperature ($T_s$) and various boundary condition parameters such as albedo and roughness.

Surface processes are classified as follows.

1. geothermal diffusion processes - Determining the geothermal structure

2. geological and hydrological processes - Determining the structure of underground water, runoff, etc.

3. snow accumulation process - snow accumulation, snowmelt, etc., expression of snow-related processes

4. oceanic mixed layer processes - determining ocean temperature and sea ice thickness (optional)

We briefly list the characteristics of the CCSR/NIES AGCM surface processes:

Evaluate the thermal conductivity and water diffusion (optional) of multiple layers in the ground.

2. assessing the surface heat balance using the surface temperature.

3. diffusional conduction of heat and water is solved by the implicit method.

Snow is not treated as a separate layer, but is evaluated together with the first surface layer.

5. assessing oceanic mixed layers and sea ice in multiple layers (optional)

We follow the flow of the calculations and give a brief description of the scheme. \The entries in the square brackets are the names of the corresponding subroutines and the ones in parentheses are the file names. The entries enclosed in parentheses refer to the description in other sections.

1. (Evaluate surface fluxes `MODULE:[SFCFLX(psfcm)]`)
 The heat, water (evaporation), and momentum fluxes between the atmosphere and the earth's surface are estimated using the bulk formula. However, the evaporation efficiency ($\beta$) is set to 1.

2. evaluate the surface roughness `MODULE:[GNDZ0(pgsfc)]`
 Basically, it is given from the outside, depending on the file and surface type, but it can be changed depending on the amount of snowfall and other factors.

3. assessing the heat flux and heat capacity within the ground surface . `MODULE:[LNDFLX(pglnd), SEAFLX(pgsea), SNWFLX(pgsnw)]`
 The heat capacity of the land and sea layers is estimated, and the heat fluxes at the boundary of each layer are estimated from the heat conduction equation. When snowfall is present, the heat capacity and fluxes are changed.

4. evaluate the water flux and capacity of the land surface `MODULE:[LNDWFX(pglnd)]`
 Estimate the capacity of water in each layer of land and the water flux at the boundary of each layer from the water diffusion equation

5. evaluate the evaporation efficiency `MODULE:[GNDBET(pgsfc)]`
 For the land surface, the calculation depends on soil moisture and stomatal resistance.

6. implicit solution of geo-thermal conduction up to the middle `MODULE:[GNDHT1(pggnd)]`
 We evaluate the temperature change due to heat conduction in the ground. However, since the evaluation is done implicitly including the change in surface temperature, we only perform the first stage of the evaluation here.

7. solving the surface heat balance `MODULE:[SLVSFC(pgslv)]`
 Solves the equation for the heat balance at the earth's surface and obtains the temporal variation of temperature at the earth's surface and temperature and specific humidity in the first layer of the atmosphere. These equations are used to correct the heat/water (evaporation) fluxes between the atmosphere and the ground surface and the heat conduction fluxes at the ground surface. When there is snow or ice cover and the surface temperature exceeds the freezing point, the surface temperature is used as the freezing point, and the residual flux is evaluated as the flux used for snow melting.

8. implicit solution for geothermal conduction `MODULE:[GNDHT2(pggnd)]`
 Since the change in surface temperature was obtained, it is used to solve for the change in underground temperature due to heat conduction.

9. evaluate snow reduction by snow sublimation `MODULE:[SNWSUB(pgsnw)]`
 For snow accumulation conditions, the evaporation (sublimation) flux reduces the snow accumulation by the calculated flux.

10. assessing the increase in snow cover due to snowfall `MODULE:[SNWFLP(pgsnw)]`
 It discriminates between snowfall and rainfall and increases the snowpack when it falls.

11. assessing snowfall reduction due to snowmelt `MODULE:[SNWMLP(pgsnw)]`
 When the surface temperature or the first layer temperature is above the freezing point during snow accumulation, snowmelt is assumed to occur and the snow accumulation is reduced by keeping the temperature below the freezing point.

12. implicit solution for groundwater diffusion `MODULE:[GNDWTR(pggnd)]`
 Solving changes in subsurface moisture due to subsurface water fluxes.

13. evaluate precipitation interception by snowpack `MODULE:[SNWROF(pgsnw)]`
 When there is snowfall, the infiltration of precipitation into the soil is prevented and rainfall and snowmelt water (part of it) become runoff.

14. assessing surface runoff `MODULE:[LNDROF(pglnd)]`
 Calculation of surface runoff of rainfall and snowmelt. Three evaluation methods can be selected: the bucket model, the new bucket model, and runoff evaluation using infiltration capacity.

15. evaluate the freezing process `MODULE:[LNDFRZ(pglnd)]`
 Calculates the temperature change due to the freezing and thawing of the ground moisture and the resulting latent heat release. However, this routine is optional and is usually skipped.

16. assessing the growth of sea ice `MODULE:[SEAICE(pgsea)]`
 With the oceanic mixed layer option, the increase or decrease in the thickness of the sea ice due to heat transfer is calculated.

17. evaluate the melting of sea ice surface `MODULE:[SEAMLT(pgsea)]`
 If the surface temperature or the first layer temperature of the sea ice is above the freezing point, melting is assumed to occur and the temperature is kept below the freezing point to reduce the thickness of the sea ice.

18. nudge the ocean temperature `MODULE:[SEANDG(pgsea)]`
 With the oceanic mixed layer option, nudging can be added to the sea surface temperature to bring it closer to a given temperature.

19. evaluate the wind speed on the ground `MODULE:[SLVWND(pggnd)]`
 Solving for changes in wind speed in the first layer of the atmosphere.

Some of the above routines are further subdivided into subroutines for the evaluation of land, sea and snow surfaces as follows

1. setting the boundary conditions `MODULE:[GNDSFC(pgbnd)]`

     1. read the surface conditions `MODULE:[GETIDX(pgbnd)]`

     2. read the sea level condition `MODULE:[GETSEA(pgbnd)]`

     3. set the condition of sea level `MODULE:[SEATMP(pgsea)]`

2. evaluate the surface albedo `MODULE:[GNDALB(pgsfc)]`

     1. load the albedo `MODULE:[GETALB(pgbnd)]`

     2. change the land surface albedo `MODULE:[LNDALB(pglnd)]`

     3. change the sea-surface albedo `MODULE:[SEAALB(pgsea)]`

     4. change the snow albedo `MODULE:[SNWALB(pgsnw)]`

3. evaluate the surface roughness `MODULE:[GNDZ0(pgsfc)]`

     1. read the roughness `MODULE:[GETZ0(pgbnd)]`

     2. change the land surface roughness `MODULE:[LNDZ0(pglnd)]`

     3. change the sea surface roughness `MODULE:[SEAZ0(pgsea)]`

     4. change the snow surface roughness `MODULE:[SNWZ0(pgsnw)]`

4. evaluate the surface wetness `MODULE:[GNDBET(pgsfc)]`

     1. read the degree of wetness `MODULE:[GETBET(pgbnd)]`

     2. change the surface wetness `MODULE:[LNDBET(pglnd)]`

     3. change the degree of sea surface wetness `MODULE:[SEABET(pgsea)]`

     4. change the snow surface wetness `MODULE:[SNWBET(pgsnw)]`

### classification of the ground surface.

The ground surface is classified according to the externally given conditions as follows, according to the surface type $m$.

| Header0 | Header1 |
| ------- | ------- |
| m | requirement |
| \-I can't even begin to tell you what to do. | mixed-layered ocean |
| \-I can't tell you how many times I've been in a row. | Sea Ice (given from outside) |
| 0 | Sea level (providing temperature from outside) |
| 1 | land ice |
| $\ge$ 2 | land surface |

In addition, depending on the internally variable ice conditions, we have the following surface conditions ($n$).

| Header0 | Header1 |
| ------- | ------- |
| n | state |
| 0 | Sea surface without ice |
| 1 | Sea Ice and Land Ice |
| $\ge$ 2 | land surface |

These are defined in `MODULE:[GNDSFC(pgsfc)]`.

### Surface Heat Balance.

The conditions of the surface heat balance are ,

$$
   F\theta(T_0,T_1) + L \beta Fq^P(T_0,q_1) + FR(T_0) - Fg(T_0,G_1) = 0
$$


in $F\theta, Fq^P, FR, Fg$. $F\theta, Fq^P, FR, Fg$ use atmospheric and subsurface predicted variables and the atmospheric and subsurface predicted variables prior to the evaluation of surface processes, but this balance is generally not satisfied in $T_0$, which was used at that time.

There are several ways to solve this problem.

1. how to consider only $T_0$ as an unknown

2. how to consider $T_0,T_1,q_1,G_1$ as unknowns

The latter method is used in the CCSR/NIES AGCM. It is necessary to combine all the variables in all layers of the atmosphere and ground to solve the problem. The details will be described in the section "Solving the diffuse balance equation for atmospheric and ground systems".

There are two ways to evaluate the evaporation term $\beta Fq^P(T_0,q_1)$.

1. as $\beta=1$, multiply $Fq^P$ (possible evaporation rate) obtained by solving (439) by $\beta$.

Solve (439) directly using $\beta$.

The temperature used in the calculation of $\beta Fq^P$ is different between the former and the latter. In the former case, the temperature in the case of $\beta=1$ is used, while in the latter case the actual temperature is used.

In the CCSR/NIES AGCM, the former method is used as the standard method. When $T_0$ resulting from the solution of (439) on a snow or ice surface exceeds the freezing point, or $T_0$ on a sea surface divides the freezing temperature of seawater (in the case of the oceanic mixed layer model), the temperature of $T_0$ is fixed to the freezing point and each flux is calculated by fixing the temperature of $T_0$ to the freezing point, and the residuals of the equation in (439) ( energy residuals) will be used to freeze and thaw the snow and ice.

### Set the discrete coordinate system `MODULE:[SETGLV,SETWLV,SETSLV]`

The subsurface is discretized in the $z$ coordinate system. Land temperature is defined by the $zg_l$ layer, water content by the $zw_l$ layer, and ocean temperature by the $zs_l$ layer. $l$ increases from the upper to the lower levels. The flux is defined by the layer boundary $zg_{k-1/2}, zw_{k-1/2}$.

In addition, a layer with a thickness of zero is considered in $z=0$ and the skin temperature is defined as $T_s$. For convenience, it is represented by $l=0$ and set to $zg_{0} = zg_{1/2} = zg_{-1/2} = 0$.

### Calculating land heat flux and heat capacity `MODULE:[LNDFLX]`

The evaluation of physical properties such as heat and moisture fluxes in the ground and wetness is carried out separately according to whether the ground surface is sea or land surface, and in the case of land surface, whether or not there is snow cover. In the following, we firstly describe the evaluation method for the case of land surface without snow. The differences in the evaluation methods for the cases of sea and snow surfaces will be described later.

The heat capacity of the land surface is ,

$$
  Cg_{l}  = \tilde{C}g_{l}(zg_{l+1/2} - zg_{l-1/2})
          = \tilde{C}g_{l} \Delta zg_{l} \; .
$$


where $\tilde{C}g_{l}$ is the volume specific heat.

The land heat flux is treated as a constant heat transfer coefficient (which may depend on the $l$).

$$
  Fg_{l-1/2} = Kg_{l-1/2} (G_l - G_{l-1})(zg_l - zg_{l-1}) \; ,
$$


$$
  \frac{\partial{Fg_{l-1/2}}}{\partial {G_l}} = - \frac{\partial{Fg_{l-1/2}}}{\partial {G_{l-1}}}
 = Kg_{l-1/2}/(zg_l - zg_{l-1}) \; .
$$


### Calculating the water flux on land `MODULE:[LNDWFX]`

The capacity of water in each layer $C_w$ is ,

$$
  Cw_{l}  = \rho_w (zw_{l+1/2} - zw_{l-1/2}) 
          = \rho_w \Delta zw_{l} \; .
$$


However, in practice, it is not possible to store this much water. The maximum storage capacity, i.e., the saturation capacity, is defined as the saturation water content of $ws$,

$$
  Cws_{l}  = ws_{l} \rho_w (zw_{l+1/2} - zw_{l-1/2})
           = ws_{l} \rho_w \Delta zw_{l} \; .
$$


The basic formula for the groundwater flux can be written as follows.

$$
  F{w} = - K_{w} \left( \frac{\partial{w}}{\partial {z}} + g_w \right)
$$


Here, $g_w$ represents the effect of gravity.

There are two ways to evaluate the groundwater flux on land.

1. fixed diffusion coefficient method

2. moisture content dependent diffusion coefficient method `MODULE:[HYDFLX]`

In the method of fixed diffusion coefficients, it is simply expressed as follows. $K_w$ is the diffusion coefficient and $\rho_w$ is the density of liquid water. Here, the gravitational potential term $g_w$ in (445) is neglected.

$$
  Fw_{l-1/2} = \rho_w Kw_{l-1/2} (w_l - w_{l-1})/(zw_l - zw_{l-1}) \; ,
$$


$$
  \frac{\partial{Fw_{l-1/2}}}{\partial {w_l}} = - \frac{\partial{Fw_{l-1/2}}}{\partial {w_{l-1}}}
 = \rho_w Kw_{l-1/2}/(zw_l - zw_{l-1}) \; .
$$


On the other hand, in the method with the moisture content-dependent diffusion coefficients, the hydraulic potential is obtained as follows.

$$
  Fw_{l-1/2} = \rho_w Kw_{l-1/2} (W_{l-1/2})^{2B+3} 
             ( (\psi_{l} - \psi_{l-1})/(zw_{l} - zw_{l-1}) -1 ) \; ,
$$


$$
  \frac{\partial{Fw_{l-1/2}}}{\partial {w_l}} = \rho_w Kw_{l-1/2} (W_{l-1/2})^{2B+3} 
                     \frac{\partial{\psi_{l}}}{\partial {w_l}}/(zw_l - zw_{l-1}) \; ,\\
- \frac{\partial{Fw_{l-1/2}}}{\partial {w_{l-1}}} = \rho_w Kw_{l-1/2} (W_{l-1/2})^{2B+3} 
                     \frac{\partial{\psi_{l-1}}}{\partial {w_{l-1}}}/(zw_l - zw_{l-1}) \; .
$$



where $Kw$ is the saturated hydraulic conductivity, $W$ is the saturation degree, and $\psi$ is the pressure potential, which is given as follows

$$
  W_l = w_l / ws_l \; , \;\;
  W_{l-1/2} = (W_{l-1} + W_{l})/(Cw_{l-1} + Cw_{l}) \; ,
$$


$$
  \psi_l = \psi s_l (W_l)^{-B}\; , \;\;
  \frac{\partial{\psi_l}}{\partial {w_l}} = -B \psi_l W_l / ws \; .
$$


$Kw$, $B$, and $\psi s$ are constants and may depend on the ground surface types $m$ and $l$.

### Calculating land surface spill`MODULE:[LNDROF]`

The following three methods can be used to evaluate runoff.

1. bucket model

2. new bucket model

3. surface runoff with consideration of infiltration capacity

In the bucket model ,

$$
w_1^{m+1,*} = w_1^{m+1} +  \frac{P - E}{Cw_1} \Delta t
$$


and this is

$$
 w_1^{m+1,*} > w_s 
$$


with the outflow as $R_B$,

$$
  w_1^{m+1}  =  w_s \\
  R_B   =   Cw_1 ( w_1^{m+1,*} - w_s )/\delta t
$$



The other two are Otherwise ,

$$
  w_1^{m+1}  =   w_1^{m+1,*} \\
  R_B        =   0                  \; .
$$



The new bucket model (Kondo, 1993) is a model for estimating the average groundwater infiltration rate for spatially non-uniform surface soil types and depths. The model was originally developed to estimate the daily average runoff, but it was modified to use the model at each time step. In the new bucket model, precipitation infiltration and post-runoff soil moisture are estimated as follows.

$$
w_1^{m+1} = w_1^m + ( ws_1 - w_1^m ) 
\tanh\left( \frac{(P-E)\tau_B}{Cw_1(ws_1 - w_1^m)} \right) 
\Delta t / \tau_B \; .
$$


Here, $\tau_B$ is a time constant (standard value of 3600s). The runoff rate ($R_N$) is calculated from the surface water balance

$$
     R_N  =  P - E - Cw_1 ( w_1^{m+1} - w_1^m ) / \Delta t \\
          =  (P - E) \left( 1 - \frac{\tanh x}{x} \right)
$$



It is estimated that However,

$$
  x = \frac{(P-E)\tau_B}{Cw_1(ws_1 - w_1^m)} \; .
$$


The evaluation of surface runoff ($R_I$) considering infiltration capacity is given by $C_I$ for infiltration capacity, $P_l$ for stratiform rainfall intensity, and $P_c$ for convective rainfall intensity, as follows

$$
  R_I = \left\{
    \begin{array}{ll}
       P_c \exp [ -(C_I-P_l) / (P_c/\kappa) ]  \;\; ( P_l \le C_I ) \\
       P_l + P_c - C_I                         \;\; ( P_l > C_I ) 
    \end{array}
  \right. \; .
$$


The amount of precipitation input percolating to the ground surface is modified as follows.

$$
  \widetilde{P_c} = \left\{
    \begin{array}{ll}
      P_c - R_I  \;\; ( P_l \le C_I ) \\
      0             \;\; ( P_l > C_I )
    \end{array}
  \right. \; , \\
  \widetilde{P_l} = \left\{
    \begin{array}{ll}
      P_l   \;\; ( P_l \le C_I ) \\
      C_I  \;\; ( P_l > C_I )
    \end{array}
  \right. \; .
$$



In the case above equation (463), the exponential distribution of the precipitation intensity probability of convective rainfall is assumed in the rainfall intensity probability $f(P_c)$, which is derived from the following equation

$$
  f(P_c) = \frac{\kappa}{\overline{P_c}} 
            \exp\left[-\frac{\kappa}{\overline{P_c}}P_c\right] \; ,
$$


$$
  \frac{R_I}{\kappa} = \int_{\widetilde{C_I}}^{\infty}
                        (P_c-\widetilde{C_I})f(P_c) d(P_c) \; .
$$


However, the effective infiltration capacity is set to $\widetilde{C_I} = C_I - P_l$ based on the assumption that stratiform rainfall infiltration is uniform. The value of $\kappa$ is a constant (typically 0.6) for the fraction of convective rainfall area in the total grid area.

When considering multi-layered soil water transfer, we can also consider the drainage from each layer in proportion to the permeability coefficient.

### Evaluating Albedo on land `MODULE:[LNDALB]`

The evaluation of albedo is basically based on a constant value given by an external source. There are two ways to give them.

1. give a distribution in a file

2. specify a value for each surface type $m$

For each wavelength band, two components are given in the visible and near-infrared regions (the same values are used in the standard).

It is also possible to take into account the effects of surface wetness and the zenith angle of solar radiation as follows (not taken into account in the standard).

$$
  \alpha = \alpha - f_w \alpha w_1 \; ,
$$


$$
  \alpha = \alpha + \Delta f_{\zeta} (1 - \alpha)(1 - \cos^2 \zeta) \; .
$$


Here, the wetness factor ($f_w$) and the zenith angle factor ($f_{\zeta}$) are constants.

### Evaluating roughness on land surface`MODULE:[LNDZ0]`

The evaluation of roughness is basically based on a constant value given by an external source. The two methods of evaluation are as follows.

1. give a distribution in a file

2. specify a value for each ground surface type $m$

The roughness $z_{0H}$ for heat and the roughness $z_{0E}$ for water vapor should be a constant multiple of the roughness $z_{0M}$ for momentum if not given. ($z_{0H} = z_{0E} = 0.1 z_{0M}$ by default)

### Evaluating surface wetness on land`MODULE:[LNDBET]`

On the land surface, $\beta$ has a constant value of 1. For the non-ice surface, there are several evaluation methods that can be used for the non-ice surface as follows.

1. using an externally given constant value. As a way of giving ,

     1. give a distribution in a file

     2. specify a value for each ground surface type $m$

 There are two possibilities.

2. soil moisture Calculated as a function of $w$.

 Define the saturation degree $W \equiv w/w_s$ and give it as a function.

     Function type 1. 1 if critical saturation exceeds $W_c$, below that depends on a linearity.

$$
          \beta = \min \left( W/W_c, 1 \right)
$$


     2. that depend nonlinearly on function type 2. $W$.

$$
          \beta = 1-\exp \left[-3(W/W_c)^{a} \right]
$$


In the following, we describe the different treatment of the sea surface from that of the land surface.

### Calculating heat flux and heat capacity at sea level `MODULE:[SEAFLX]`

At sea level, the heat capacity varies depending on the presence of sea ice. Using the volume specific heat of seawater ($\tilde{C}_s$) and the volume specific heat of sea ice ($\tilde{C}_i$), $h_i$ is used as the thickness of sea ice,

$$
  Cg_{l}  = \left\{ 
    \begin{array}{ll}
      \tilde{C}_s (zg_{l+1/2} - zg_{l-1/2})
               ( h_i \le zg_{l-1/2} )\\
      \tilde{C}_s (zg_{l+1/2} - h_i)
    + \tilde{C}_i ( h_i - zg_{l-1/2} )
               ( zg_{l-1/2} < h_i < zg_{l+1/2} )\\
      \tilde{C}_i (zg_{l+1/2} - zg_{l-1/2})
               ( h_i \ge zg_{l+1/2} ) \\
    \end{array} 
    \right. \; .
$$


Even at sea level, the thermal conductivity is kept constant (depending on $l$).

$$
  Fg_{l-1/2} = Ks_{l-1/2} (G_l - G_{l-1})/(zs_l - zs_{l-1}) \; ,
$$


$$
  \frac{\partial{Fg_{l-1/2}}}{\partial {G_l}} = - \frac{\partial{Fg_{l-1/2}}}{\partial {G_l-1}} 
 = Ks_{l-1/2}/(zs_l - zs_{l-1}) \; .
$$


However, in the area where sea ice exists, the temperature between sea ice and seawater is set to $T_i$ ($=$ 271.15K), and the thermal conductivity is set to the value of the sea ice.

$$
  Fg_{l-1/2}  = \left\{ 
    \begin{array}{ll}
      Ks_{l-1/2} (G_l - G_{l-1})/(zs_l - zs_{l-1}) \;\; 
               (h_i < zg_{l-3/2} ) \\
      Ks_{l-1/2} (G_l - T_i)/(zs_l - h_i) \;\; 
               ( zg_{l-3/2} \le h_i < zg_{l-1/2} )\\
      K_i (T_i - G_{l-1})/(h_i - zs_{l-1}) \;\; 
               ( zg_{l-1/2} \le h_i < zg_{l+1/2} )\\
      K_i (G_l - G_{l-1})(zs_l - zs_{l-1}) \;\; 
               (h_i \ge zg_{l+1/2} )
    \end{array} 
    \right. \; .
$$


Heat fluxes in the oceans outside the sea ice area are only meaningful when using an oceanic mixed layer model.

### Evaluating surface wetness at sea level `MODULE:[SEABET]`

The surface moisture content ($\beta$) used to evaluate evaporation is a constant value of 1 for the sea surface and sea ice.

### albedo and roughness at sea level

The albedo at the sea surface not covered by sea ice is calculated in the radiation routine for each wavelength range as a function of the optical thickness of the atmosphere and the solar incidence angle in `MODULE:[SSRFC]` .

The roughness of the sea surface not covered by the ocean is calculated as a function of the momentum flux in the surface flux routine `MODULE:[SEAZ0F]` .

The albedo and roughness of the sea surface covered with sea ice are given as constant values. `MODULE:[SEAALB, SEAZ0]`. The current standard values are albedo 0.7 and roughness 1 $\times10^{-3}$ m.

In the following, we describe the different treatment of the snow surface from that of the land surface.

### Snow Heat Flux Correction `MODULE:[SNWFLX]`

The snow is treated as the same thermal layer as the first layer of the ground surface. In other words, the heat capacity and thermal diffusivity of the first layer are modified by the presence of snow.

The heat capacity can be simply summed, where $C_y$ is the specific heat per mass of snow and $W_y$ is the mass per unit area of snow,

$$
  Cg_{l} = Cg'_{l} + C_y W_y \; .
$$


However, $Cg'_{l}$ is the heat capacity for the case without snow.

The heat flux is defined as the hypothetical temperature at the snow-soil interface of $G_I$,

$$
  Fg_{1/2} = K_y (G_I-T_0)/h_y = Kg_{1/2} (G_1 - G_I)(zg_1 - zg_0) \; .
$$


However, if $h_y$ is the snow depth and $\rho_y$ is the snow density, then the value of $h_y = W_y/\rho_y$ is obtained. Removing $G_I$ from the above equation results in

$$
  Fg_{1/2}  = \left[ \left( K_y/h_y \right)^{-1} 
                   +  \left( K_g /(zg_1 - zg_0) \right)^{-1} 
              \right]^{-1} (G_1-T_0)
                    \\
            = \left[ \left( K_y (G_1-T_0)/h_y \right)^{-1} 
                    +  (Fg_{1/2})^{-1}
                \right]^{-1} \; .
$$



However, $Fg'_{1/2}$ is the flux for the case without snow. Therefore, if this has already been calculated, the fluxes for the case with snow can be obtained by taking the harmonic mean of that and the fluxes for snow only. The temperature differential coefficients $\frac{\partial{Fg_{1/2}}}{\partial {G_1}}$ and $\frac{\partial{Fg_{1/2}}}{\partial {T_0}}$ can also be obtained by taking the harmonic mean of the temperature differential coefficients.

If there is more than a certain amount of snow cover, the temperature of $G_1$ should be regarded as the temperature of snow cover rather than the temperature of the soil. To account for such a case, in the above equation, $h_y/2$ is actually used instead of $h_y$, and not only $F_{1/2}$ but also $F_{3/2}$ is treated as being affected by snow cover.

$$
  Fg_{1/2} = \left[ \left( K_y (G_1-T_0)/(h_y/2) \right)^{-1} 
                    +  (Fg'_{1/2})^{-1}
                \right]^{-1} \; ,
$$


$$
  Fg_{3/2} = \left[ \left( K_y (G_2-G_1)/(h_y/2) \right)^{-1} 
                    +  (Fg'_{3/2})^{-1}
                \right]^{-1} \; .
$$


### Calculating snow sublimation `MODULE:[SNWSUB]`

Decrease the snowpack by the amount of sublimation flux.

$$
  \tilde{Wy} = Wy - Fq_1 \Delta t \; .
$$


When the snow accumulation is fully sublimated, the shortage of water flux is evaporated from the soil. In this case, the surface energy balance is calculated on the assumption that all the surface moisture fluxes have sublimated, and it is necessary to correct the soil temperature.

$$
  \tilde{G}_1 = G_1 + L_M ( Fq_1 \Delta t - Wy ) / Cg_1 \; .
$$


### Calculating snowfall `MODULE:[SNWFLP]`

When precipitation arrives at the ground surface, it is judged whether it is solid (snow) or liquid (rain).

Atmosphere First Layer Wet Bulb Temperature $Tw_1$

$$
Tw_1 = T_1 - L / Cp ( q^* - q_1 ) / ( 1 + L / Cp \frac{\partial{q^*}}{\partial {T}} )
$$


If the freezing point ($Tw_1$) is lower than the freezing point ($Tm$), the temperature is regarded as snow, and if it is higher than the freezing point ($Tm$), the temperature is regarded as rain. The purpose of using the wet-ball temperature is to incorporate the effect of the temperature of precipitation reaching the earth's surface depending on the evaporation rate of precipitation during its fall.

In the case of snowfall, the snowpack is increased by the amount of snowfall.

$$
\tilde{Wy} = Wy + Py \Delta t \; .
$$


$Py$ is a snowfall flux.

### Snowmelt calculation `MODULE:[SNWMLP]`

If the surface energy balance ($\Delta s$) is positive and/or the temperature of the first layer of soil (including snow) is higher than the freezing point at a snow location, the amount of snowmelt is calculated and the latent heat of melting is corrected for the soil temperature.

Assuming that the soil temperature before the correction is set to $\hat{G_1}$, the amount of snow melt ($\tilde{My} \Delta t$) and the soil temperature ($\tilde{G_1}$) when snow melt is assumed to be equal to the amount of energy balance removed is

In $\hat{G_1} \ge Tm$,

$$
\tilde{My} \Delta t = ( Cg_1 ( \hat{G_1} - Tm ) + \Delta s \Delta t ) / L_M \; ,
$$


$$
\tilde{G_1} = Tm \, .
$$


When using $\hat{G_1} < Tm$ ,

$$
\tilde{My} \Delta t = \Delta s \Delta t / ( L_M + Cp_I ( Tm - \hat{G_1} ) ) \; ,
$$


$$
\tilde{G_1} = \hat{G_1} \; .
$$


In the case of $\hat{G_1} < Tm$, it is assumed that the temperature of the snow part other than the melting snow does not change due to the energy balance. $L_M$ is the latent heat of melting, $Tm$ is the freezing point, and $Cp_I$ is the specific heat of ice.

The actual snowmelt and soil temperature are based on the current amount of snow melt and the case where the $Wy$ melts completely,

$$
My \Delta t = \left\{
   \begin{array}{ll}
      \tilde{My} \Delta t  ( \tilde{My} \Delta t \le Wy ) \\
      Wy                   ( \tilde{My} \Delta t >   Wy ) \\
   \end{array}
\right. \; ,
$$


$$
G_1 = \left\{
   \begin{array}{ll}
      \tilde{G_1}   ( \tilde{My} \Delta t \le Wy ) \\
      \hat{G_1} + ( \Delta s \Delta t - L_M Wy - Cp_I Wy ( Tm - \hat{G_1} ) )
                / ( Cg_1 - Cp_I Wy )
                    ( \tilde{My} \Delta t >   Wy ) \\
   \end{array}
\right. \; .
$$


### Calculating Snow Surface Runoff`MODULE:[SNWROF]`

If there is a snow accumulation ($Wy$), prior to calculating the snow runoff, the snow runoff ($R_S$) is evaluated as follows and excluded from the surface moisture input. Also, snowmelt water ($My$) is added to the surface moisture input at this point.

$$
  Is = \left\{
    \begin{array}{ll}
      1 - Wy / Wy_{Ci}  \;\; ( Wy < Wy_{Ci} ) \\
      0                 \;\; ( Wy \ge Wy_{Ci} )
    \end{array}
  \right. \; ,
$$


$$
  \widetilde{P_c} = Is P_c \; ,\\
  \widetilde{P_l} = Is ( P_c + My ) \; ,\\
  R_S        = ( 1 - Is )( P_c + P_l + My ) \; .
$$




Here, $Is$ is the surface infiltration rate due to snow cover. The standard value of the critical snowpack ($Wy_{Ci}$) for infiltration is 200 kg/m$^2$.

### Evaluating albedo on snow-covered surfaces`MODULE:[SNWALB]`

If snow $Wy$ is present, the snow cover ratio is considered to be proportional to the square root of the snowpack, and the albedo approaches the snow value $\alpha s$ in proportion to the square root of the snowpack (the critical value $Wy_C$ is 200kg/m$^2$ in standard).

$$
  \alpha = \left\{ 
  \begin{array}{ll}
    \alpha' + (\alpha s-\alpha')\sqrt{Wy/Wy_{C}} \;\;   (Wy < Wy_{C}) \\
    \alpha s                                            (Wy \ge Wy_{C})
  \end{array}
  \right. \; .
$$


In addition, the effect of snow albedo reduction during melting and wet snow cover is taken into account as follows.

$$
  \alpha s = \left\{
    \begin{array}{ll}
      \alpha s_d                         \;\; (T_0 \le Td) \\
      \alpha s_d - (\alpha s_m -\alpha s_d)
                   (T_0 - Td)/(Td - Tm)  \;\; (Td < T_0 \le Tm) \\
      \alpha s_m                         \;\; (T_0 > Tm)
    \end{array}
  \right. \; .
$$


where $T_0$ is the surface temperature. The standard values for dry snow albedo ($\alpha s_d$) and wet snow albedo ($\alpha s_m$) are 0.7 and 0.5, respectively. The critical temperatures ($Td$ and $Tm$) are 258.15 and 273.15, respectively.

Furthermore, we can take into account the effect of the zenith angle dependence of solar radiation as in the absence of snow (not taken into account in the standard).

### Evaluating Surface Roughness on Snow Covered Surfaces`MODULE:[SNWZ0]`

When the snow cover is $Wy$, the ratio of snow cover is considered to be proportional to the square root of the snowpack, and the surface roughness approaches the snow roughness in proportion to the square root of the snowpack (the critical value of $Wy_C$ is 200kg/m$^2$ in standard).

$$
  z_0 = \left\{ 
  \begin{array}{ll}
    z_0' + (z_0s-z_0')\sqrt{Wy/Wy_{C}}  \;\;   (Wy < Wy_{C}) \\
    z_0s                                       (Wy \ge Wy_{C})
  \end{array}
  \right. \; .
$$


The standard values for snow roughness are 10 $^{-2}$, 10 $^{-3}$, and 10 $^{-3}$ for momentum, temperature, and water vapor, respectively.

### Evaluating Surface Wetness on Snow Covered Surfaces`MODULE:[SNWBET]`

In the case of snow cover ($Wy$), the snow cover ratio is considered to be proportional to the square root of the snow cover, and the surface wetness approaches snow wetness 1 in proportion to the square root of the snow cover (the critical value of $Wy_C$ is 200kg/m$^2$ in standard).

$$
  \beta = \left\{ 
  \begin{array}{ll}
    \beta' + (1-\beta')\sqrt{Wy/Wy_{C}}  \;\;   (Wy < Wy_{C}) \\
    1                                           (Wy \ge Wy_{C})
  \end{array}
  \right. \; .
$$


In the following section, we describe the optional surface processes.

### Calculating the freezing process `MODULE:[LNDFRZ]`

To use this option, the number of vertical layers in terms of temperature and moisture must be equal to the level of each layer.

After calculating the ground temperature by thermal diffusion,

 - If the ground temperature is lower than the freezing point and liquid moisture is present, the freezing of moisture will be

 - If the ground temperature is higher than the freezing point and solid moisture is present, the water will melt.

Calculate.

Assuming that the freezing rate of the $l$ layer is $w_{Fl}$, the freezing moisture $\Delta w_{Fl}$ is

$$
  \Delta w_{Fl} = \left\{
    \begin{array}{ll}
      - w_{Fl}
         \;\; ( \Delta_0 w_{Fl} \le - w_{Fl} ) \\
      \Delta_0 w_{Fl}
         \;\; ( - w_{Fl} < \Delta_0 w_{Fl} \le w_l - w_{Fl} ) \\
      w_l - w_{Fl}
         \;\; ( \Delta_0 w_{Fl} >  w_{Fl} )
    \end{array}
  \right. \; .
$$


However, a negative value of $\Delta w_{Fl}$ represents the water to be melted. $\Delta_0 w_{Fl}$ is the value of $\Delta w_{Fl}$ when freezing/thawing occurs until the soil temperature reaches the freezing point, and is given by

$$
  \Delta_0 w_{Fl} = Cg_l (Tm - G_l)/(L_M Cw_l) \; .
$$


$Tm$ has an ice point of 273.16K.

The change in soil temperature due to the latent heat of the soil moisture phase change is given by

$$
  \tilde{G}_l = G_l + L_M Cw_l \Delta w_{Fl} / Cg_l \; .
$$


### oceanic mixed layer model `MODULE:[SEAFRZ]`

In the mixed layer model, the temporal variation of ocean temperature and sea ice thickness is calculated by solving the heat budget of the ocean.

Although a multi-layered model is also possible, we will take a single-layer model of thickness ($D$) as an example here. The predictor variables are temperature ($G$) and sea ice thickness ($h_I$).

First, the heat capacity of the oceans and surface fluxes are determined by `MODULE:[SEAFLX]` The heat capacity of the oceans is defined as the specific heat of water ($C_w$), the specific heat of ice ($C_I$), and the density of water and ice ($\rho_w$),

$$
  C_s  = C_I \rho_w h_I +   C_w \rho_w (D - h_I)
$$


 In the absence of sea ice, the heat transfer flux is

$$
  Fs_{1/2} = K_s \frac{ G - T_0 }{d/2}
$$


 On the other hand, if there is sea ice,

$$
 Fs_{1/2} = K_I \frac{ T_I - T_0 }{h_I}
$$


 where $T_I$ is the freezing temperature of sea ice at 271.35 K. where $T_I$ is the freezing temperature of sea ice at 271.35K.

     The heat flux in the $z=D$ is usually zero, but it can be provided by an external source. This is used for flux correction considering ocean heat transport.

Using this heat flux and heat capacity, we can determine the change in temperature ($G$) as well as the land surface.

3. the melting of the sea ice surface is treated in the same way as snow. `MODULE:[SEAFLX]`

 First, let's get the melting value ($\tilde{M_I}$)
 When the     $G \ge T_I$ ,

$$
  M_I
  =  \frac{C_s ( G - T_I ) + \Delta s \Delta t )}
          {\rho_w ( C_w - C_I ) T_I }
$$


 When the     $G < T_I$ ,

$$
  M_I
  =  \frac{\Delta s \Delta t )}
          {\rho_w ( C_w - C_I ) G}
$$


 In the case of full melting, however, the value is set to $M_I=h_I$ and the heat is corrected for the difference.

$$
  G \leftarrow G + \frac{ \Delta s \Delta t 
                          - \rho_w ( C_w - C_I ) h_I G  }
                        { C_w + \rho_w ( C_w - C_I ) h_I}
$$


 Varying the thickness of the ice,

$$
  h_I \leftarrow h_I - M_I 
$$


 Then, vary the heat capacity correspondingly.

$$
  C_s = C_s + \rho_w ( C_w - C_I ) h_I
$$


The next step is to consider the growth process from the bottom of the sea ice.

     1. when there is no sea ice ($h_I=0$)

 When         $G <  T_I$ ,

$$
  \tilde{f_I}
  =  \frac{C_s ( T_I - G ) - \Delta s \Delta t )}
          {\rho_w ( C_w - C_I ) T_I }
$$


 When the         $G \ge T_I$ ,

$$
  \tilde{f_I}
  =  \frac{- \Delta s \Delta t )}
          {\rho_w ( C_w - C_I ) G}
$$


 If this is positive, the sea ice is produced. If this value is positive, sea ice is produced. Note that $\Delta s$ becomes positive when $T_0$ becomes less than or equal to $T_I=271.35$ K.

$$
  h_I  \leftarrow  f_I \\
  C_s  \leftarrow  C_s - \rho_w ( C_w - C_I ) f_I \\
  G    \leftarrow  \max( G, T_I )
$$




     2. when the sea ice already exists ($h_I>0$)

 Heat fluxes from the seawater beneath the sea ice to the bottom of the sea ice.

$$
  F_b = K_s \frac{ G - T_I }{ D/2 - h_I }
$$


 Estimated by The difference between $F_b$ and the heat flux from the ocean upward to $Fs_{1/2}$ is used for the growth or melting of sea ice.

$$
  f_I = \frac{ Fs_{1/2} - F_b }
             { \rho_w ( C_w - C_I ) G } \Delta t
$$


 So..,

$$
  h_I  \leftarrow  h_I + f_I \\
  G    \leftarrow  G \frac{C_s}{C_s - \rho_w ( C_w - C_I ) f_I} \\
  C_s  \leftarrow  C_s - \rho_w ( C_w - C_I ) f_I
$$




5. you can externally give the reference temperature $G_{ref}$ and apply nudging to it.

$$
        G \leftarrow G + \frac{G_{ref} - G}{\tau} \Delta t
$$


 This is a heat flux

$$
        F_n = C_s \frac{G_{ref} - G}{\tau}
$$


 The equivalent of giving a .

 To perform     flux correction, you can perform nudging by giving an appropriate $\tau$, memorize $F_n$, and give it as $Fs_{1+1/2}$.
