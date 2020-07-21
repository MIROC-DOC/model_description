## Surface Processes.

### Overview of Surface Processes.

The surface processes are the processes of momentum, heat, and water between the atmosphere and the earth's surface
Giving boundary conditions at the lower end of the atmosphere through flux exchange.
Surface processes are described in the Ground Temperature $T_g$, Ground Moisture $W_g$,
Handle your own forecast variables, such as snow cover $W_y$,
Thermal inertia of the ground surface, water accumulation, snow accumulation,
Evaluate the accumulation of sea ice and other factors.
The main input data are the diffusion of geophysical quantities between the atmosphere and the surface
and the fluxes due to radiation and precipitation.
The output data are the surface temperature ($T_s$) and
Various boundary condition parameters such as albedo and roughness.

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

The scheme is outlined in detail along the calculation flow.
\where the part in the square brackets is the name of the corresponding subroutine and the part in ( ) is the file name.
The entries enclosed in parentheses refer to the descriptions in other sections.

1. (Evaluate surface fluxes `MODULE:[SFCFLX(psfcm)]`)
 The heat, water (evaporation), and momentum fluxes between the atmosphere and the surface are
 Estimate in bulk.
 However, the evaporation efficiency ($\beta$) is set to 1.

2. evaluate the surface roughness `MODULE:[GNDZ0(pgsfc)]`
 Basically, it depends on the file and the surface type.
 I can get it from the outside,
 Change according to snowfall and other factors.

3. evaluate the heat flux and heat capacity within the ground surface .
     `MODULE:[LNDFLX(pglnd), SEAFLX(pgsea), SNWFLX (pgsnw)]`
 Estimate the heat capacity of each layer of land and sea,
 The heat flux at each layer boundary is estimated from the heat transfer equation.
 If there is snowfall, change the heat capacity and flux.

4. evaluate the water flux and capacity of the land surface `MODULE:[LNDWFX(pglnd)]`
 Estimate the capacity of each layer of water on land,
 Estimate the water flux at each layer boundary from the water diffusion equation

5. evaluate the evaporation efficiency `MODULE:[GNDBET(pgsfc)]`
 For the land surface, the calculation depends on soil moisture and stomatal resistance.

6. perform an implicit solution of geothermal conduction up to the middle `MODULE:[GNDHT1( pggnd)]`
 Evaluate the temperature change due to heat conduction in the ground.
 However, taking into account the surface temperature changes
 Since it is done     implicitly, only the first step is done here.

7. solving the surface heat balance `MODULE:[SLVSFC(pgslv)]`
 Solving the equation for the heat balance between the surface temperature and
 Time variation of temperature and specific humidity in the first layer of the atmosphere.
 Using this, the heat/water (evaporation) flux between the atmosphere and the ground surface
 and compensate for the heat transfer flux at the surface.
 If there is snow or ice and the surface temperature is above the freezing point,
 With the surface temperature as the freezing point,
 Evaluate the residual flux as the flux used for snowmelt.

8. implicit solution for geothermal conduction `MODULE:[GNDHT2(pggnd )]`
 Since the change in surface temperature was obtained, we used it to determine
 Solving for changes in ground temperature due to heat conduction in the ground.

9. evaluate snow reduction by snow sublimation `MODULE:[SNWSUB(pgsnw)]`
 For snow cover conditions, the calculated evaporation (sublimation) fluxes allow
 Decrease the snowpack.

10. assessing the increase in snow cover due to snowfall `MODULE:[SNWFLP(pgsnw)]`
 It discriminates between snowfall and rainfall and increases the snowpack when it falls.

11. assessing snowfall reduction due to snowmelt `MODULE:[SNWMLP(pgsnw)]`
 If the surface temperature or first layer temperature exceeds the freezing point during snowfall ,
 If the snow melts, it will keep the temperature below the freezing point,
 Decrease the snowpack.

12. solves the diffusion of groundwater by implicit method `MODULE:[GNDWTR( pggnd)]`
 Solving changes in subsurface moisture due to subsurface water fluxes.

13. evaluate precipitation interception by snowpack `MODULE:[SNWROF(pgsnw)]`
 Snowfall prevents precipitation infiltration into the soil,
 Rainfall and snowmelt water (part of it) will be runoff.

14. assessing surface runoff `MODULE:[LNDROF(pglnd)]`
 Calculating surface runoff of rainfall and snowmelt water.
 Bucket Model, New Bucket Model,
 There are 3 evaluation methods to choose from, including runoff evaluation using permeability.

15. evaluate the freezing process `MODULE:[LNDFRZ(pglnd)]`
 Freezing and thawing of groundwater and
 Calculate the temperature change due to the latent heat release associated with it.
 However, this routine is optional,
 Usually skipped.

16. assessing the growth of sea ice `MODULE:[SEAICE(pgsea)]`
 If you specify the marine mixed layer option ,
 Calculate the increase or decrease in the thickness of the sea ice due to heat conduction.

17. evaluate the melting of sea ice surface `MODULE:[SEAMLT(pgsea)]`
 If the surface temperature or first layer temperature of the sea ice exceeds the freezing point,
 The temperature is kept below the freezing point,
 Decrease the thickness of the sea ice.

18. nudge the ocean temperature `MODULE:[SEANDG(pgsea)]`
 With the oceanic mixed layer option, the given
 Nudging to get closer to the temperature.
 It can be added to the temperature of the sea surface.

19. evaluate the wind speed on the ground `MODULE:[SLVWND(pggnd)]`
 Solving for changes in wind speed in the first layer of the atmosphere.

Also, some of the routines mentioned above are
In addition, the following subroutines for the evaluation of land, sea and snow surfaces are used
There's a split.

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

The ground surface is a condition given by the outside world,
According to the surface type $m$, they are classified as follows.

| Header0 | Header1 |
| ------- | ------- |
| m | requirement |
| \-I can't even begin to tell you what to do. | mixed-layered ocean |
| \-I can't tell you how many times I've been in a row. | Sea Ice (given from outside) |
| 0 | Sea level (providing temperature from outside) |
| 1 | land ice |
| $\ge$ 2 | land surface |

Furthermore, depending on the possible internal changes in the ice conditions,
Take the following ground surface conditions $n$.

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

> <span id="p-sfc:sfc-balance" label="p- sfc:sfc-balance">[p-sfc:sfc-balance\[p-sfc:sfc-balance]& lt;/span>

It is.
$F\theta, Fq^P, FR, Fg$, $F\theta, Fq^P, FR, Fg$ is ,
Atmospheric and subsurface forecast variables before evaluating surface processes and ,
The evaluation is performed using the
In the $T_0$ used at that time, this balance is generally not met.

There are several ways to solve this problem.

1. how to consider only $T_0$ as an unknown

2. how to consider $T_0,T_1,q_1,G_1$ as unknown numbers

The CCSR/NIES AGCM uses the latter method.
In doing so, it is necessary to combine and solve for all the variables of the atmospheric and ground layers.
The details are described in the section "Solving the Diffusion-Based Budget Equations for Atmospheric Surface Systems".

There are two ways to evaluate the evaporation terms $\beta Fq^P(T_0,q_1)$.

1. as a $\beta=1$
     ([p-sfc:sfc-balance\]](#p-sfc:sfc-balance $Fq^P$, obtained by solving for (1)
     (possible evaporation amount) multiplied by $\beta$.

2. using $\beta$.
     ([p-sfc:sfc-balance\]](#p-sfc:sfc-balance )) directly.

The temperatures used in the calculations in $\beta Fq^P$ are different between the former and the latter.
In the former case, the temperature in the case of $\beta=1$,
In the latter case, the actual temperature is used.

The CCSR/NIES AGCM uses the former method as standard.
On a snow or ice surface ([p-sfc[p-sfc:sfc-balance\]](#p-sfc: sfc-balance)) of the result of solving
If the $T_0$ exceeds the freezing point,
Or, when $T_0$ divides the freezing temperature of seawater at the sea surface (in the case of oceanic mixed-layer model)
by fixing the temperature of the $T_0$ at the freezing point and calculating each flux,
([p-sfc:sfc-balance\]](#p-sfc:sfc-balance )), and the residuals (energy residuals) of the formula
Suppose it is used for freezing and thawing snow and ice.

### Set the discrete coordinate system `MODULE:[SETGLV,SETWLV,SETSLV]`

The ground is discretized with the $z$ coordinate system.
Land temperature is layer $zg_l$, water content is layer $zw_l$,
Ocean temperature is defined in layer $zs_l$.
The $l$ increases from the top to the bottom.
The flux is defined by the layer boundary $zg_{k-1/2}, zw_{k-1/2}$.

Also, consider a layer of zero thickness on the $z=0$,
Define skin temperature $T_s$.
For convenience, it is represented by $l=0$ and $zg_{0} = zg_{1/2} = zg_{-1/2} = 0$.

### Calculating land heat flux and heat capacity `MODULE:[LNDFLX]`

Physical quantities, such as heat and moisture fluxes in the ground, and wetness
The evaluation of surface characteristics is based on whether the surface is sea or land, and in the case of land surface
This is done separately if there is snowfall or not.
In the following section, we will first evaluate the evaluation method for the land surface case without snow.
We shall describe in brief. We will describe the difference between the case of sea level and snow surface in detail later.

The heat capacity of the land surface is ,

$$
  Cg_{l}  = \tilde{C}g_{l}(zg_{l+1/2} - zg_{l-1/2})
          = \tilde{C}g_{l} \Delta zg_{l} \; .
$$


where $\tilde{C}g_{l}$ is the volume specific heat.

The heat flux of the land surface is treated as a constant heat conduction coefficient (which may depend on $l$). ).

$$
  Fg_{l-1/2} = Kg_{l-1/2} (G_l - G_{l-1})(zg_l - zg_{l-1}) \; ,
$$


$$
  \frac{\partial Fg_{l-1/2}}{\partial G_l} = - \frac{\partial Fg_{l-1/2}}{\partial G_{l-1}}
 = Kg_{l-1/2}/(zg_l - zg_{l-1}) \; .
$$


### Calculating the water flux on land `MODULE:[LNDWFX]`

The capacity of water in each layer $C_w$ is ,

$$
  Cw_{l}  = \rho_w (zw_{l+1/2} - zw_{l-1/2}) 
          = \rho_w \Delta zw_{l} \; .
$$


However, in practice, it is not possible to store this much water.
The maximum storage capacity, i.e., the saturation capacity, is defined as the saturation water content of $ws$,

$$
  Cws_{l}  = ws_{l} \rho_w (zw_{l+1/2} - zw_{l-1/2})
           = ws_{l} \rho_w \Delta zw_{l} \; .
$$


The basic formula for the groundwater flux can be written as follows.

$$
  F{w} = - K_{w} \left( \frac{\partial w}{\partial z} + g_w \right)
$$

> <span id="basic-Fw" label="basic-Fw"& gt;gt;\\braham\[basic-Fw]< /span>

Here, $g_w$ represents the effect of gravity.

There are two ways to evaluate the groundwater flux on land.

1. fixed diffusion coefficient method

2. moisture content dependent diffusion coefficient method `MODULE:[HYDFLX]`

In the method of fixed diffusion coefficients, we simply express it as follows.
$K_w$ is the diffusion coefficient and $\rho_w$ is the density of liquid water.
where the gravitational potential in ([basic-Fw\]](#basic-Fw)) The term $g_w$ is
Ignore it.

$$
  Fw_{l-1/2} = \rho_w Kw_{l-1/2} (w_l - w_{l-1})/(zw_l - zw_{l-1}) \; ,
$$


$$
  \frac{\partial Fw_{l-1/2}}{\partial w_l} = - \frac{\partial Fw_{l-1/2}}{\partial w_{l-1}}
 = \rho_w Kw_{l-1/2}/(zw_l - zw_{l-1}) \; .
$$


On the other hand, the method with the moisture content dependent diffusion coefficient is not applicable,
Using the hydraulic potential, we obtain the following.

$$
  Fw_{l-1/2} = \rho_w Kw_{l-1/2} (W_{l-1/2})^{2B+3} 
             ( (\psi_{l} - \psi_{l-1})/(zw_{l} - zw_{l-1}) -1 ) \; ,
$$


$$
  \frac{\partial Fw_{l-1/2}}{\partial w_l} = \rho_w Kw_{l-1/2} (W_{l-1/2})^{2B+3} 
                     \frac{\partial \psi_{l}}{\partial w_l}/(zw_l - zw_{l-1}) \; ,\\
- \frac{\partial Fw_{l-1/2}}{\partial w_{l-1}} = \rho_w Kw_{l-1/2} (W_{l-1/2})^{2B+3} 
                     \frac{\partial \psi_{l-1}}{\partial w_{l-1}}/(zw_l - zw_{l-1}) \; .
$$



where $Kw$ is the saturated hydraulic conductivity, $W$ is the saturation degree, $\psi$ is the pressure potential,
It is given as follows.

$$
  W_l = w_l / ws_l \; , \;\;
  W_{l-1/2} = (W_{l-1} + W_{l})/(Cw_{l-1} + Cw_{l}) \; ,
$$


$$
  \psi_l = \psi s_l (W_l)^{-B}\; , \;\;
  \frac{\partial \psi_l}{\partial w_l} = -B \psi_l W_l / ws \; .
$$


$Kw$, $B$, and $\psi s$ are constants, surface type May depend on $m$ and $l$.

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



.
Other than that ,

$$
  w_1^{m+1}  =   w_1^{m+1,*} \\
  R_B        =   0                  \; .
$$



The new bucket model (Kondo, 1993) is based on the idea that surface soil types and depths are spatially
It is a model for estimating the average groundwater infiltration rate for non-uniform cases.
It was originally developed to estimate the daily average outflow of ,
Here, we changed it to be used at each time step.
In the new bucket model, precipitation infiltration and post-runoff soil moisture are estimated as follows.

$$
w_1^{m+1} = w_1^m + ( ws_1 - w_1^m ) 
\tanh\left( \frac{(P-E)\tau_B}{Cw_1(ws_1 - w_1^m)} \right) 
\Delta t / \tau_B \; .
$$


Here, $\tau_B$ is a time constant (standard value 3600s).
In this case, the runoff volume ($R_N$) is calculated from the surface water balance

$$
     R_N  =  P - E - Cw_1 ( w_1^{m+1} - w_1^m ) / \Delta t \\
          =  (P - E) \left( 1 - \frac{\tanh x}{x} \right)
$$



It is estimated that .
However,

$$
  x = \frac{(P-E)\tau_B}{Cw_1(ws_1 - w_1^m)} \; .
$$


The evaluation of the surface runoff $R_I$ considering soil infiltration capacity is based on the evaluation of the infiltration capacity of the $C_I$,
Assuming that the intensity of stratiform rainfall is $P_l$ and that of convective rainfall is $P_c$,
Given below.

$$
  R_I = \left\{
    \begin{array}{ll}
       P_c \exp [ -(C_I-P_l) / (P_c/\kappa) ]  \;\; ( P_l \le C_I ) \\
       P_l + P_c - C_I                         \;\; ( P_l > C_I ) 
    \end{array}
  \right. \; .
$$

> <span id="inf-exs" label="inf-exs"&gt ;inf-exs]< /span>

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



On the formula ([index[inf-exs\]](#inf-exs)), convective rainfall intensity To probability $f(P_c)$
It is derived from the following equation, which assumes an exponential distribution.

$$
  f(P_c) = \frac{\kappa}{\overline{P_c}} 
            \exp\left[-\frac{\kappa}{\overline{P_c}}P_c\right] \; ,
$$


$$
  \frac{R_I}{\kappa} = \int_{\widetilde{C_I}}^{\infty}
                        (P_c-\widetilde{C_I})f(P_c) d(P_c) \; .
$$


However, assuming that stratocumulus rainfall is uniformly infiltrating, the effective infiltration capacity of
$\widetilde{C_I} = C_I - P_l$.
$\kappa$ is the percentage of convective rainfall area in the total grid area,
It is a constant (0.6 by default).

When considering multi-layered soil moisture transfer,
We can also consider the drainage from each layer proportional to the permeability coefficient.

### Evaluating Albedo on land `MODULE:[LNDALB]`

The evaluation of albedo is basically based on a constant value given by an external source.
There are two ways to give it.

1. give a distribution in a file

2. specify a value for each surface type $m$

For each wavelength band, we can give two components in the visible and near-infrared
(The same values are used in the standard).

We can also consider the effects of surface wetness and solar radiation zenith angle as follows
(Not considered in the standard).

$$
  \alpha = \alpha - f_w \alpha w_1 \; ,
$$


$$
  \alpha = \alpha + \Delta f_{\zeta} (1 - \alpha)(1 - \cos^2 \zeta) \; .
$$


where the wetness factor ($f_w$) and the zenith angle factor ($f_{\zeta}$) are constants Yes.

### Evaluating roughness on land surface`MODULE:[LNDZ0]`

The evaluation of roughness is basically based on a constant value given by an external source.
There are two ways to give it.

1. give a distribution in a file

2. specify a value for each surface type $m$

The roughness $z_{0H}$ for heat and the roughness $z_{0E}$ for water vapor are
If not given, the roughness to momentum is a constant multiple of $z_{0M}$.
($z_{0H} = z_{0E} = 0.1 z_{0M}$ by default)

### Evaluating surface wetness on land`MODULE:[LNDBET]`

On land ice, $\beta$ has a constant value of 1.
For non-icy land surfaces, we can use several evaluation methods as follows.

1. using an externally given constant value. As a way of giving ,

     1. give a distribution in a file

     2. specify a value for each surface type $m$

 There are two possibilities.

2. soil moisture calculated as a function of $w$.

 Define the saturation degree $W \equiv w/w_s$,
 We give it as a function.

     Function type 1.
 The critical saturation is 1 if it exceeds the critical saturation value of $W_c$, and is linearly dependent below it.

$$
          \beta = \min \left( W/W_c, 1 \right)
$$


     2. that depend nonlinearly on function type 2. $W$.

$$
          \beta = 1-\exp \left[-3(W/W_c)^{a} \right]
$$


In the following, we describe the different treatment of the sea surface from that of the land surface.

### Calculating heat flux and heat capacity at sea level `MODULE:[SEAFLX]`

At the sea surface, the heat capacity varies depending on the presence of sea ice.
Volumetric Specific Heat of Seawater $\tilde{C}_s$ and
Using the volume specific heat of sea ice with $\tilde{C}_i$, $h_i$ is used as the thickness of the sea ice,

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
  \frac{\partial Fg_{l-1/2}}{\partial G_l} = - \frac{\partial Fg_{l-1/2}}{\partial G_l-1} 
 = Ks_{l-1/2}/(zs_l - zs_{l-1}) \; .
$$


However, in areas where there is sea ice,
The temperature of the boundary between sea ice and seawater is set to $T_i$ ($=$ 271.15K),
Let the thermal conductivity be the value of the sea ice.

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


Heat fluxes in the oceans outside the sea ice area are significant because
This is only the case with the oceanic mixed layer model.

### Evaluating surface wetness at sea level `MODULE:[SEABET]`

The surface moisture content of the $\beta$ used to evaluate evaporation is ,
The constant value of 1 for the sea surface and sea ice.

### albedo and roughness at sea level

The albedo at the sea surface, which is not covered by sea ice, is in the radiation routine,
Calculated at each wavelength as a function of atmospheric optical thickness and solar incidence angle
`MODULE:[SSRFC]` .

The roughness of the ocean surface that is not covered by the ocean is determined in the surface flux routine,
Calculated as a function of momentum flux
`MODULE:[SEAZ0F]` .

The albedo and roughness of the sea surface covered with sea ice are
Give a constant value.
`MODULE:[SEAALB, SEAZ0]`.
The current standard value is 0.7, albedo,
The roughness is 1 $\times10^{-3}$ m.

In the following, we describe the different treatment of the snow surface from that of the land surface.

### Snow Heat Flux Correction `MODULE:[SNWFLX]`

The snow is treated thermally as the same layer as the first layer of the ground surface.
That is, the heat capacity and thermal diffusivity of the first layer are
The shape will be changed by the presence of snow.

The heat capacity is expressed as a simple sum of
$C_y$ as the specific heat per mass of snow, $W_y$ as the mass per unit area of snow So,

$$
  Cg_{l} = Cg'_{l} + C_y W_y \; .
$$


However, $Cg'_{l}$ is the heat capacity in the absence of snow.

The heat flux is defined as the hypothetical temperature at the snow-soil interface, which is set to $G_I$,

$$
  Fg_{1/2} = K_y (G_I-T_0)/h_y = Kg_{1/2} (G_1 - G_I)(zg_1 - zg_0) \; .
$$


However, the depth of the snow cover in $h_y$ is
Let $\rho_y$ be the density of snow, and $h_y = W_y/\rho_y$ be the density of snow.
Eliminating $G_I$ from the equation above,

$$
  Fg_{1/2}  = \left[ \left( K_y/h_y \right)^{-1} 
                   +  \left( K_g /(zg_1 - zg_0) \right)^{-1} 
              \right]^{-1} (G_1-T_0)
                    \\
            = \left[ \left( K_y (G_1-T_0)/h_y \right)^{-1} 
                    +  (Fg_{1/2})^{-1}
                \right]^{-1} \; .
$$



However, the $Fg'_{1/2}$ is the flux when there is no snow.
Therefore, if this has already been calculated,
By taking the harmonic mean of that and the snow only flux,
Fluxes are required in the presence of snow.
Also, the temperature differential coefficient of the fluxes $\frac{\partial Fg_{1/2}}{\partial G_1}$ and $\frac{\partial Fg_{1/2}}{\partial T_0}$
is similarly obtained by the harmonic mean of the temperature differential coefficients.

If there is more than a certain amount of snowfall ,
The temperature $G_1$ should be regarded as the temperature of the snowpack rather than the temperature of the soil.
To account for such cases, in fact, the
In the above formula, instead of $h_y$, $h_y/2$ is used,
Furthermore, not only $F_{1/2}$, but also $F_{3/2}$ is changed by snow
Handling.

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


When the snowfall is fully sublimated, the missing water flux is evaporated from the soil.
The energy balance of the earth's surface is assumed to be the same as if the surface moisture flux were all sublimated
We need to correct for the soil temperature because it has been calculated.

$$
  \tilde{G}_1 = G_1 + L_M ( Fq_1 \Delta t - Wy ) / Cg_1 \; .
$$


### Calculating snowfall `MODULE:[SNWFLP]`

When precipitation arrives at the ground surface, it is judged whether it is solid (snow) or liquid (rain).

Atmosphere First Layer Wet Bulb Temperature $Tw_1$

$$
Tw_1 = T_1 - L / Cp ( q^* - q_1 ) / ( 1 + L / Cp \frac{\partial q^*}{\partial T} )
$$


and if the $Tw_1$ is lower than the freezing point $Tm$, snow, TERM If it's over 00101, it shall be considered rain.
The reason why the wet-ball temperature is used is that the temperature of precipitation reaching the surface is
This is to incorporate effects that depend on the likelihood of evaporation during the fall of precipitation.

In the case of snowfall, the snowpack is increased by the amount of snowfall.

$$
\tilde{Wy} = Wy + Py \Delta t \; .
$$


$Py$ is a snowfall flux.

### Snowmelt calculation `MODULE:[SNWMLP]`

If the surface energy balance ($\Delta s$) is positive, as a result of the calculation of the surface energy balance
and/or Soil first layer in areas with snow cover (including snowpack)
When the temperature of the soil is higher than the freezing point, the amount of snowmelt is calculated and the latent heat of melting is calculated.
Make corrections.

If the soil temperature before correction is set to $\hat{G_1}$,
If the snowmelt occurred to the extent that it would resolve the energy balance
Snowmelt $\tilde{My} \Delta t$ and soil temperature $\tilde{G_1}$ are ,

When the $\hat{G_1} \ge Tm$ ,

$$
\tilde{My} \Delta t = ( Cg_1 ( \hat{G_1} - Tm ) + \Delta s \Delta t ) / L_M \; ,
$$


$$
\tilde{G_1} = Tm \, .
$$


When the $\hat{G_1} < Tm$ ,

$$
\tilde{My} \Delta t = \Delta s \Delta t / ( L_M + Cp_I ( Tm - \hat{G_1} ) ) \; ,
$$


$$
\tilde{G_1} = \hat{G_1} \; .
$$


In the case of $\hat{G_1} < Tm$, the temperature of the part of the snow that melts in the energy balance except for the snow is
I'm assuming it doesn't change.
$L_M$ is the latent heat of melting, $Tm$ is the freezing point, $Cp_I$ is the specific heat of ice It is.

The actual snowmelt and soil temperature are based on the current amount of snow and soil temperature in the case of full melting of the $Wy$,

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

If there is a snow $Wy$, prior to calculating the land surface runoff
The runoff due to snow accumulation was evaluated as follows,
Exclude moisture from the surface input.
Snowmelt water ($My$) is added to the surface water input here.

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




where $Is$ is the surface infiltration rate due to snow cover.
The standard value of critical snowpack for infiltration for $Wy_{Ci}$ is 200 kg/m$^2$ .

### Evaluating albedo on snow-covered surfaces`MODULE:[SNWALB]`

If you have a snow $Wy$ ,
The ratio of snow cover is considered to be proportional to the square root of the snowpack,
Albedo approaches the snow value $\alpha s$ in proportion to the square root of the snowpack
(The critical value of $Wy_C$ is 200 kg/m$^2$ in standard).

$$
  \alpha = \left\{ 
  \begin{array}{ll}
    \alpha' + (\alpha s-\alpha')\sqrt{Wy/Wy_{C}} \;\;   (Wy < Wy_{C}) \\
    \alpha s                                            (Wy \ge Wy_{C})
  \end{array}
  \right. \; .
$$


Also, when melting occurs and the snowpack is wet, the snow albedo
The smaller effect is considered as follows.

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


where $T_0$ is the surface temperature.
Dry Snow Albedo $\alpha s_d$, Wet Snow Albedo $\alpha s_m$
The standard values for
Critical temperature ($Td$ and $Tm$) was 258.15 and 273.15, respectively Yes.

Furthermore, as in the absence of snow, we can take into account the effect of the zenith angle dependence of solar radiation
(Not considered in the standard).

### Evaluating Surface Roughness on Snow Covered Surfaces`MODULE:[SNWZ0]`

If you have a snow $Wy$ ,
The ratio of snow cover is considered to be proportional to the square root of the snowpack,
Surface roughness approaches snow roughness in proportion to the square root of the snowpack.
(The critical value, $Wy_C$, is 200 kg/m$^2$ in standard).

$$
  z_0 = \left\{ 
  \begin{array}{ll}
    z_0' + (z_0s-z_0')\sqrt{Wy/Wy_{C}}  \;\;   (Wy < Wy_{C}) \\
    z_0s                                       (Wy \ge Wy_{C})
  \end{array}
  \right. \; .
$$


The standard values for snow roughness are for momentum, temperature and water vapor, respectively.
10 $^{-2}$, 10 $^{-3}$, 10 $^{-3}$.

### Evaluating Surface Wetness on Snow Covered Surfaces`MODULE:[SNWBET]`

If you have a snow $Wy$ ,
The ratio of snow cover is considered to be proportional to the square root of the snowpack,
Surface wetness approaches snow wetness 1 in proportion to the square root of the snowpack
(The critical value of $Wy_C$ is 200 kg/m$^2$ in standard).

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

To use this option, you must use the
The number of vertical layers in the ground and the level of each layer must be equal.

After calculating the ground temperature by thermal diffusion,

 - If the ground temperature is lower than the freezing point and liquid moisture is present, the freezing of moisture will be

 - If the ground temperature is higher than the freezing point and solid moisture is present, the water will melt.

Calculate.

If the icing ratio of the $l$ layer is set to $w_{Fl}$, the freezing water in the $\Delta w_{Fl}$ is,

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


where the negative $\Delta w_{Fl}$ represents the water to be melted.
The $\Delta_0 w_{Fl}$ will freeze/thaw until the soil temperature reaches the freezing point.
This is the value of $\Delta w_{Fl}$ if it were to occur, given by

$$
  \Delta_0 w_{Fl} = Cg_l (Tm - G_l)/(L_M Cw_l) \; .
$$


$Tm$ has an ice point of 273.16K.

The change in soil temperature due to the latent heat of the soil moisture phase change is given by

$$
  \tilde{G}_l = G_l + L_M Cw_l \Delta w_{Fl} / Cg_l \; .
$$


### oceanic mixed layer model `MODULE:[SEAFRZ]`

In the oceanic mixed layer model ,
By solving for the heat balance of the oceans, the temperature of the oceans and
Determine the time variation of sea ice thickness.

Multi-layered models are possible, but,
Here we will take a single layer model of thickness $D$ as an example.
The predictor variables are temperature ($G$) and sea ice thickness ($h_I$).

First, determine the heat capacity and surface flux of the ocean.
     `MODULE:[SEAFLX]`
 The heat capacity of the oceans is ,
 Specific Heat of Water $C_w$, Specific Heat of Ice $C_I$, Density of Water and Ice $\rho_w$ as ,

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


 where $T_I$ is the freezing temperature of sea ice at 271.35 K. where $T_I$ is the freezing temperature of sea ice at 271.35 K.

 Heat flux     in the $z=D$ is usually zero while the $Fs_{1+1/2}$ is usually zero,
 It can be given from the outside.
 It is used in the case of flux correction for oceanic heat transport.

2. using this heat flux and heat capacity
 As with the land surface, determine the change in temperature ($G$).

The melting of the sea ice surface is treated in the same way as snow.
     `MODULE:[SEAFLX]`

 First, I'll set the melting value, $\tilde{M_I}$, to
 When     the $G \ge T_I$ ,

$$
  M_I
  =  \frac{C_s ( G - T_I ) + \Delta s \Delta t )}
          {\rho_w ( C_w - C_I ) T_I }
$$


 When     the $G < T_I$ ,

$$
  M_I
  =  \frac{\Delta s \Delta t )}
          {\rho_w ( C_w - C_I ) G}
$$


 Estimate in ,
 However, if it has melted completely, set the value to $M_I=h_I$ and compensate for the heat.

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

 When         the $G <  T_I$ ,

$$
  \tilde{f_I}
  =  \frac{C_s ( T_I - G ) - \Delta s \Delta t )}
          {\rho_w ( C_w - C_I ) T_I }
$$


 When         the $G \ge T_I$ ,

$$
  \tilde{f_I}
  =  \frac{- \Delta s \Delta t )}
          {\rho_w ( C_w - C_I ) G}
$$


 Estimate in .
 When it is positive, sea ice is produced.
 Here, $\Delta s$ is $T_0$ is $T_I=271.35$ K or less
 Note that it is positive when the

$$
  h_I  \leftarrow  f_I \\
  C_s  \leftarrow  C_s - \rho_w ( C_w - C_I ) f_I \\
  G    \leftarrow  \max( G, T_I )
$$




     2. when the sea ice is already present ($h_I>0$)

 Heat fluxes from the seawater beneath the sea ice to the bottom of the sea ice.

$$
  F_b = K_s \frac{ G - T_I }{ D/2 - h_I }
$$


 Estimate in .
 The difference between         $F_b$ and the heat flux from the ocean to the top of $Fs_{1/2}$
 Used for the growth or melting of sea ice.

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




5. give an external reference temperature of $G_{ref}$
 You can nudging it.

$$
        G \leftarrow G + \frac{G_{ref} - G}{\tau} \Delta t
$$


 This is a heat flux

$$
        F_n = C_s \frac{G_{ref} - G}{\tau}
$$


 The equivalent of giving a .

     To do flux correction,
 Provide the appropriate $\tau$ and perform nudging,
 Remember     the $F_n$,
 You can give it to me as $Fs_{1+1/2}$.

