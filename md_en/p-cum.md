## cumulus convection

### Overview of the Cumulus Convection Scheme

The cumulus convection scheme describes the condensation, precipitation, and convection processes involved in cumulus convection, and calculates changes in temperature and water vapor content and precipitation due to latent heat release and associated convective motion. It also calculates the cloud water content and cloud coverage involved in radiation. The main input data are temperature ($T$) and specific humidity ($q$), and the output data are the time rate of change of temperature and specific humidity, $\partial T/\partial t, \partial q/\partial t, \partial l/\partial t$, and cloud cover ($l^{cR}$) of cumulus clouds used for radiation ($C^c$).

The framework of the cumulus convection scheme is basically based on Arakawa and Schubert (1974). The vertical air column on a horizontal grid is considered as the basic unit of parameterization. Clouds are characterized by temperature, specific humidity, cloud water content, and vertical mass fluxes of clouds, and several clouds with different cloud tops are considered in a single vertical column. The clouds occupy part of the horizontal grid, and in the rest of the surrounding area, there is a downward motion equal to the cloud mass flux (the compensating downward motion). This compensatory downward motion and the outflow of air into the surrounding region (detraining) cause changes in the temperature and specific humidity fields in the surrounding region. Since we assume that the area of the upwelling is small and treat the grid-averaged temperature and specific humidity fields as the same as that of the surrounding region, this gives us the change in the grid-averaged temperature and specific humidity.

The cloud model determines the temperature, specific humidity, and cloud water content in clouds. Here, an entrainment-prime model is used, as in Moorthi and Suarez (1992), which assumes a linear increase in mass flux with respect to height. The cloud bases are defined as the lifted condensation height of the surface air, and several cloud tops are considered depending on the fraction of entrainment in the surrounding region. However, if no cloud base exists, then the possibility of clouds with higher cloud bases is also considered.

The mass flux of each cloud is diagnostically determined using the cloud work function. The cloud work function is defined as the vertical integration of the buoyant work per unit mass flux. The cloud work function gives a mass flux that approaches zero at a certain relaxation time due to the compensating downward motion of the cumulus, etc. The cloud work function is defined as the vertical integral of the buoyant work per unit mass flux.

In addition, the evaporation of precipitation and the associated downdraft effects are considered in a very simple way.

The outline of the calculation procedure is as follows. In parentheses are the names of the corresponding subroutines.

1) Evaluate the cloud base height as the lifted condensation height of the surface atmosphere.

2. to obtain vertical distributions of cloud temperature, specific humidity, cloud water content, and mass fluxes (relative values) for cloud tops, using a cloud model `MODULE:[UPDRF]`.

3. calculate the cloud work function `MODULE:[CWF]`.

4. find the hypothetical change of temperature and specific humidity in the surrounding region due to a unit mass flux cloud `MODULE:[CLDTST]`.

5. calculate the cloud-work function for the virtual change of temperature and specific humidity `MODULE:[CWF]`.

6. calculate cloud mass fluxes at the cloud base using the cloud work function before and after the virtual change `MODULE:[CBFLX]`.

7. calculate the vertical distribution of cloud mass flux detrainment and precipitation `MODULE:[CMFLX]`.

8. evaluate cloud water and cloud cover due to cumulus clouds `MODULE:[CMCLD]`.

9. find the change of temperature and specific humidity by detraining `MODULE:[CLDDET]`.

10. get the change of temperature and specific humidity by compensated descent `MODULE:[CLDSBH]`.

11. find vertical distributions of cloud temperature, specific humidity, and mass flux of precipitation evaporation and downdraft `MODULE:[DWNEVP]`.

12. find the change of temperature and specific humidity by detraining the downdraft `MODULE:[CLDDDE]`.

13. find the change of temperature and specific humidity due to the compensated upward flow of downdraft `MODULE:[CLDSBH]`.

### The Basic Framework of the Arakawa-Schubert Scheme

The cloud mass flux $M$, detraining $D$ is ,

$$
  M(z)     =  M_B \eta(z) \; , \\
  D(z)     =  M_B \eta(z_T) \delta (z-z_T) \; .
$$



expressed as where $M_B$ is the mass flux at the cloud base $z_B$ and $\eta$ is the dimensionless mass flux at that point.

From this, the time variation of the mean field is calculated as

$$
  \frac{\partial{\bar{h}}}{\partial {t}}  =  M \frac{\partial{\bar{h}}}{\partial {z}} 
                       + D( h^t - \bar{h} ) \; , \\
  \frac{\partial{\bar{q}}}{\partial {t}}  =  M\frac{\partial{\bar{q}}}{\partial {z}} 
                       + D( q^t + l^t - \bar{q} ) \; .
$$



where $\bar{h}, \bar{q}$ are the wet static energy and specific humidity of the mean field, and $h^t, q^t, l^t$ are the wet static energy, specific humidity and cloud water content of the air in the detrainment.

$\eta, h^t, q^t, l^t$ are determined by the cloud model. $M_B$ is obtained by closure assumptions using the cloud work function.

### Cloud Model.

The cloud model is essentially an entrained-purume model. Each cloud is characterized by an entrainment rate, and has various cloud-top heights, depending on the entrainment rate. For the sake of the sake of later computation, we will specify the cloud top height and obtain the corresponding entrainment rate to obtain the vertical structure of the clouds. By assuming a linear increase in mass flux with respect to height, we can obtain the vertical structure of the cloud. This calculation is simplified to a form that does not include a sequential approximation.

The cloud base altitude ($z_T$) is defined as the lifted condensation height of the surface atmosphere, i.e,

$$
   \bar{q}(0) \geq
                \bar{q}^*(z)
                + \frac{\gamma}{L(1+\gamma)} 
                    \left(\bar{h}(0)-\bar{h}(z) \right) \; , 
$$


Define it as the lowest $z$ that meets the requirements of the

The dimensionless mass flux $\eta$ has the entrainment rate as $\lambda$,

$$
  \frac{\partial{\eta}}{\partial {z}} = \lambda \; ,
$$


Namely,

$$
  \eta (z)  =  1 + \lambda ( z - z_B ) \\
            \equiv  1 + \lambda \hat{\eta}(z)  \; .
$$



The balance of payments for wet static energy $h^c$ and total water volume $w^c$ in the clouds is,

$$
  \frac{\partial{}}{\partial {z}}( \eta h^c   )  =  \lambda \bar{h}      \; , \\
  \frac{\partial{}}{\partial {z}}( \eta w^c   )  =  \lambda \bar{q} - \pi  \; .
$$



where $\bar{h}, \bar{q}, \pi$ are mean field $h$ and $q$, precipitation production, respectively.

Integrating,

$$
   \eta (z) h^c(z)  =  h^c(z_B)
                         + \lambda \int_{z_B}^{z} \bar{h}(\xi) d\xi \\
                    \equiv  h^c(z_B) + \lambda \hat{h}^c(z) \; ,
$$



$$
   \eta (z) w^c(z)  =  w^c(z_B)
                         + \lambda \int_{z_B}^{z} \bar{q}(\xi) d\xi
                         - R(z) \\
                    \equiv  w^c(z_B) + \lambda \hat{w}^c(z) 
                              - R(z)             \\
                    \equiv  \eta(z) w^a(z) - R(z)  \; . 
$$




The mass flux is assumed to be zero at the surface and to increase linearly below the cloud base,

$$
 \eta (z) =   \frac{z}{z_B} \; \; \; ( z<z_B ) \; .
$$


By calculating the entrainment below the cloud base, we can obtain the values of $h^c,w^c$ at the cloud base. In other words,

$$
  h^c(z_B)  =  \frac{1}{z_B} \int_0^{z_B} \bar{h}(z) dz \; , \\
  w^c(z_B)  =  \frac{1}{z_B} \int_0^{z_B} \bar{q}(z) dz \; .
$$



The buoyancy per unit mass flux due to clouds is ,

$$
   B  =   \frac{g}{\bar{T}} ( T_v^c - \bar{T}_v ) \\
      =   \frac{g}{\bar{T}} 
            \left[ T^c ( 1+\epsilon q^c-l^c ) 
                      - \bar{T} ( 1+\epsilon \bar{q} ) \right] \\
      \simeq  \frac{g}{\bar{T}} 
               \left[ ( T^c - \bar{T} ) 
               - \bar{T} \left( \epsilon(q^c-\bar{q}) -l^c \right) 
                                                     \right] \\
      \simeq  \frac{g}{\bar{T}} 
                \left[ \frac{1}{C_p(1+\gamma)} (h^c-\bar{h}^*)
                       + \bar{T} \left( \epsilon \frac{\gamma}{L(1+\gamma)} 
                                                     (h^c-\bar{h}^*)
                               + \epsilon (\bar{q}^* - \bar{q} ) 
                               - l^c                      \right) \right] \; .
$$





Here, $T_v$ is the provisional temperature, $q^*$ is the saturated specific humidity, $\epsilon = R_{{H}_2{O}}/R_{{air}} -1$, and $\gamma = L/C_p \partial q^*/\partial T$, and $\bar{q}^*, \bar{h}^*$ represent the values at the saturation of the mean field, respectively. $q^c, l^c$ are the cloud water vapor and cloud water content, respectively,

$$
  q^c  =  q^*(T^c) \, \simeq \,
           \bar{q}^* + \frac{1}{L(1+\gamma)} ( h^c - \bar{h}^* ) \; , \\  
  l^c  =  w^c - q^c \; .
$$



For the cloud top ($z_T$), the buoyancy $B$ is zero. Therefore, solving for $B(z_T)=0$ yields $\lambda$, which corresponds to a given cloud top height ($z_T$). Here, the precipitation rate ($R(z)$) integrated upward from the ground surface is assumed to be expressed by the well-known function $r(z)$ as follows

$$
  R(z)   = \eta(z) r(z) \left[ w^a(z) - q^c(z) \right] \; .
$$


So..,

$$
\frac{\bar{T}}{g} B \simeq 
 \frac{1}{1+\gamma} 
 \left[ \frac{1}{C_p} + \bar{T} (\epsilon+1-r) \frac{\gamma}{L} \right]
  (h^c-\bar{h}^*)
  + (\epsilon+1-r) \bar{T} \bar{q}^* 
  - \epsilon  \bar{T} \bar{q}
  - \bar{T} (1-r) w^a \; .
$$


$B(z_T) =0 $ is easy to solve and,

$$
  \lambda = \frac{ a\left[ h^c(z_B)-\bar{h}^*(z_T) \right]
                  +\bar{T}(z_T)\left[ b -(1-r(z_T))q^c(z_B) \right] }
                 { a\left[ \hat{\eta}(z_T) \bar{h}^*(z_T) 
                               - \hat{h}^c(z_T) \right]
                  -\bar{T}(z_T)\left[ b \hat{\eta}(z_T) 
                                     - (1-r(z_T))\hat{q}_t^c(z_T) \right] }
$$


However,

$$
a  \equiv  \frac{1}{1+\gamma}
             \left[ \frac{1}{C_p} 
                + \bar{T}(z_T) 
                  \left( \epsilon+1-r(z_T) \right) 
               \frac{\gamma}{L}                \right] \; ,\\
b  \equiv  \left(\epsilon+1-r(z_T) \right) \bar{q}^*(z_T) 
                    - \epsilon \bar{q}(z_T) \; .
$$



As mentioned above, we originally set $\lambda$ to obtain $z_T$ and there is no guarantee that a physically meaningful $\lambda$ can be obtained for a given $z_T$. Although this needs to be examined, we will take into account that the smaller the value of $\lambda$, the lower the value of $z_T$ should be.

$$
  \frac{\partial{\lambda}}{\partial {z_T}} < 0
$$


If not, we assume that there are no clouds with a cloud top ($z_T$). A minimum value is set for $\lambda$, and no cloud with a $\lambda$ smaller than this value is assumed to exist. This corresponds to the fact that there is a maximum value for the size of the cloud, considering that the entrainment rate is inversely proportional to the size of the cloud.

Cloud water content $l^c(z)$ is ,

$$
  l^c(z)  =  w^a(z)-q^c(z)-R(z)/\eta(z)   \\
          =  \left( 1-r(z) \right) \left[ w^a(z)-q^c(z) \right] \; .
$$



In the case of $w^a(z) < q^c(z)$, however, it must be $l^c(z)=0$. Furthermore, since it is unlikely that a precipitation event will change to cloud water after it rises, $R(z)$ must be an increasing function of $z$. This leads to a limitation on $r(z)$.

The characteristic value of the detrainment air is ,

$$
  h^t  =  h^c(z_T) \; , \\
  q^t  =  q^c(z_T) \; , \\
  l^t  =  l^c(z_T) \; .
$$




In the case of $ h^c(z_B) < \bar{h}^* (z_T) $, it is assumed that there are no clouds. In this case, we assume that the cloud does not exist,

$$
  \bar{h}(z'_B) > \bar{h}^* (z_T) \; , \;\;\; z_B < z < z_T 
$$


If there is a $z'_B$ that satisfies the above condition, the immediate area above it is newly designated as $z_B$,

$$
  h^c(z_B)  =  \bar{h}(z'_B) \; , \\
  w^c(z_B)  =  \bar{q}(z'_B) \; 
$$



Seek as .

### Cloud Work Function (CWF)

The cloud work function (CWF), $A$ is,

$$
  A \equiv \int_{z_B}^{z_T} B \eta dz 
$$


It is,

$$
A = \int_{z_B}^{z_T} \frac{g}{\bar{T}} \left[
        (T^c-\bar{T})
      + \bar{T} \left\{ \epsilon (q^c - \bar{q} ) 
                     - l^c                 \right\}
       \right] \eta dz \; .
$$


We should account for the work associated with downdrafting, which we will discuss below, but we ignore it here for the sake of simplicity.

If the cloud has negative buoyancy once it has positive buoyancy, starting from the bottom, then the cloud top should exist at the point where it becomes negative, and we assume that the cloud top we are considering does not exist.

### Cloud Mass Flux at Cloudbase

We assume that the cloud mass flux at the cloud base is determined on a certain time scale ($\tau_a$) such that the cloud action causes the cloud work function to approach zero.

In order to estimate this, we first calculate the time variation of the mean field in the unit cloud mass flux $M_0$.

$$
  \frac{\partial{\bar{h}'}}{\partial {t}}  =  M_0 \eta \frac{\partial{\bar{h}}}{\partial {z}} 
                       + \eta(z_T) \delta(z-z_T) ( h^t - \bar{h} ) \; , \\
  \frac{\partial{\bar{q}'}}{\partial {t}}  =  M_0 \eta \frac{\partial{\bar{q}}}{\partial {z}} 
                       + \eta(z_T) \delta(z-z_T) ( q^t + l^t - \bar{q} ) \; .
$$



With this,

$$
  \bar{h}'  =  \bar{h} + \frac{\partial{\bar{h}'}}{\partial {t}} \delta t \; , \\
  \bar{q}'  =  \bar{q} + \frac{\partial{\bar{q}'}}{\partial {t}} \delta t 
$$



and the cloud work function calculated from (235) using $\bar{h}', \bar{q}'$ is defined as $A'$.

So..,

$$
  M_B = \frac{A}{A-A'} \frac{\delta t}{\tau_a} M_0 
$$


The results of this calculation are as follows. Although the vertical cloud structures corresponding to $\bar{h}', \bar{q}'$ should have been re-calculated in order to obtain $A'$, the same cloud structures were used in the present study.

### Cloud Mass Flux, Precipitation

The cloud mass flux of the sum of clouds at each cloud-top altitude, $M$, is

$$
  M(z)   = \int^i M_B^i \eta^i(z) \; .
$$


Also, precipitation flux $P(z)$ is

$$
 P(z) = \int_i M_B^i \left[ R^i(z_T)-R^i(z) \right]  \; .
$$


### Time variation of the average field

The time variation of the mean field due to the compensated downward motion and detrainment is calculated as follows.

$$
  \frac{\partial{\bar{h}}}{\partial {t}}  =  M \frac{\partial{\bar{h}}}{\partial {z}} 
                    + \int_i D^i ( (h^t)^i - \bar{h} ) \; , \\
  \frac{\partial{\bar{q}}}{\partial {t}}  =  M\frac{\partial{\bar{q}}}{\partial {z}} 
                    + \int_i D^i ( (q^t)^i + (l^t)^i - \bar{q}(z_T^i) ) \; .
$$



However, it is $D^i = M_B^i \eta^i(z_T^i)$.

### Evaporation and downdrafting of precipitation

The precipitation falls through the unsaturated atmosphere, while some of it evaporates. Some of it also forms a downdraft.

Evaporation Rate $E$ is ,

$$
 E = \rho a_e {\rho_p}^{b_e} \left( \bar{q}_{w} - \bar{q} \right) \; ,
$$


However, $\bar{q}_{w}$ is the saturation specific humidity corresponding to the wet bulb temperature,

$$
  \bar{q}_w = \bar{q} 
            + \frac{\bar{q}^* - \bar{q}}{1+ \frac{L}{C_P}\frac{\partial{q^*}}{\partial {T}}} \; .
$$


$a_e, b_e$ are parameters of microphysics. $\rho_p$ is the density of precipitation particles and $V_T$ is the terminal velocity of precipitation,

$$
  \rho_p = \frac{P}{V_T} \; .
$$


The current standard values are $a_e=0.25$, $b_e=1$ and $V_T=10$ m/s.

For downdrafting, we make the following assumptions.

 - If $z_d$ is set at the top of the region where $\bar{h}$ decreases monotonically with height above the cloud base, then the downdraft occurs in the region of $z < z_d$.

 - A certain percentage of the precipitation evaporation that occurs at each altitude is used to form a downdraft. The air in the surrounding area, which has just become saturated by the evaporation of precipitation, is drawn into the downdraft (entrainment).

 - In $z < z_B$, detraining occurs and the mass flux decreases linearly.

That is, in $z_B < z < z_d$, the mass flux $M^d(z)$, $h^d(z),q^d(z)$, and $h^d(z),q^d(z)$ of the downdrafted air mass follow the following equation. Note that the wet static energy is conserved during evaporation, and the specific humidity when saturated by evaporation is $\bar{q}_{w}$.

$$
  \frac{\partial{M^d}}{\partial {z}} =  - f_d \frac{E}{\bar{q}_{w}-\bar{q}} \;  ,
$$


$$
  \frac{\partial{}}{\partial {z}} ( M^d h^d )  =  \bar{h}     \frac{\partial{M^d}}{\partial {z}} \; ,\\
  \frac{\partial{}}{\partial {z}} ( M^d q^d )  =  \bar{q}_{w} \frac{\partial{M^d}}{\partial {z}} \; .
$$



In the above equation, $f_d$ is the part of the evaporation that is captured in the downdraft, and $(1-f_d)$ evaporates directly into the mean field. It is assumed that the mass flux of the downdraft ($M^d$) does not exceed the total mass flux of the cloud base ($M$) by a factor of $f_m$. The current standard values are $f_d=0.5, f_m=1.0$.

### cloud water and cloud cover

Assuming that the grid-averaged cloud cover used for radiation ($l^{cR}$) is defined as the ratio of the strong upward area of cumulus clouds including the cloud cover ($l^c$) to $\delta^c$,

$$
  l^{cR} = \delta^c l^c \; .
$$


The mass flux ($M^c$) is determined by using this $\delta^c$ and the upstream vertical velocity ($v^c$)

$$
  M = \delta^c \rho v^c 
$$


So, in the end,

$$
  l^{cR} = \frac{M^c}{\rho v^c} l^c = \alpha M^c l^c \; .
$$


The cloud cover used in the estimation of radiation, $C^c$, is more reasonable than $\delta^c$, considering that the actual distribution of upwelling and cloud water has a horizontal extent. In this section, we will briefly consider the following,

$$
  C^c = \beta M_B
$$


The current standard values are $\alpha=0.3$ and $\beta=10$. The current standard values are $\alpha=0.3$ and $\beta=10$.
