## cumulus convection

### Overview of the Cumulus Convection Scheme

The cumulus convection scheme is ,
This figure represents the condensation, precipitation and convection processes involved in cumulus convection,
Due to the latent heat release and associated convective motion
Calculate precipitation with temperature and with changes in water vapor content.
We also calculate the cloud water content and cloud coverage involved in the radiation.
The main input data are temperature $T$ and specific humidity $q$,
The output data is the time rate of change of temperature and specific humidity,
$\partial T/\partial t, \partial q/\partial t, \partial l/\partial t$,
The cloud water content of the cumulus clouds used for radiation is $l^{cR}$ Cloud volume $C^c$.

The framework of the cumulus convection scheme is
Basically based on Arakawa and Schubert (1974).
Vertical air columns in one horizontal grid.
Considered as the basic unit of parameterization.
Clouds are determined by the temperature, specific humidity, cloud water content and
Characterized by a vertical upward mass flux,
Considering multiple clouds with different cloud tops within a single vertical air column.
Clouds occupy part of the horizontal lattice, and the rest of the surrounding region is
There is a downward flow equal to the cloud mass flux (compensating downward flow).
This compensatory downward flow and outflow of air into the surrounding region in the clouds (detraining)
The temperature and the specific humidity field in the surrounding region are changed by
The area of the upwelling of the cumulus convection is assumed to be small,
The lattice-averaged temperature and specific humidity fields and
Since we treat the temperature and specific humidity fields in the surrounding area as the same, we are able to
This gives the changes in the lattice mean temperature and specific humidity.

It is the cloud model that determines the temperature, specific humidity and cloud water content in clouds.
Here, we use an entrained-purume model,
As with Moorthi and Suarez (1992) ,
We assume a linear mass flux increase with respect to height.
The cloud base is used as the lifted condensation height of the surface atmosphere,
of the percentage of air uptake (entrainment) in the surrounding area.
Consider multiple cloud top altitudes depending on the difference.
However, if a cloud with a cloud base cannot exist, then
Consider the possibility of clouds with higher cloud bases.

The mass flux of each cloud is diagnostically determined using the cloud work function.
The cloud work function is defined as
It is defined as the vertical integral of the work done by buoyancy.
This cloud-work function is driven by the compensating downward motion of cumulus clouds, etc.
It gives a mass flux that approaches zero at a certain relaxation time.

In addition, the evaporation of precipitation and
The effect of the downdrafting that goes with it.
Consider in a very simple way .

The outline of the calculation procedure is as follows.
Parentheses are the names of the corresponding subroutines.

1. cloud-bottom height as the lifted condensation height of the surface atmosphere
 Evaluate .

2. using a cloud model,
 Corresponding to each cloud top altitude
 of cloud temperature, specific humidity, cloud water content, and mass flux (relative value)
 Calculates the vertical distribution `MODULE:[UPDRF]`.

3. calculate the cloud work function `MODULE:[CWF]`.

4. due to a cloud of unit mass fluxes.
 Calculates the hypothetical change of temperature and specific humidity in the surrounding area `MODULE:[CLDTST]`.

5. for a hypothetical change in temperature and specific humidity
 Calculate the cloud work function `MODULE:[CWF]`.

6. using the cloud work function before and after the virtual change
 Calculates the cloud mass flux at the cloud base `MODULE:[CBFLX]`.

7. the cloud mass flux detrainment.
 Calculate the vertical distribution and precipitation `MODULE:[CMFLX]`.

8. evaluate cloud water and cloud cover due to cumulus clouds `MODULE:[CMCLD]`.

9. by detainment.
 Calculate the change of temperature and specific humidity `MODULE:[CLDDET]`.

10. by compensatory downstream flow.
 Calculate the change of temperature and specific humidity `MODULE:[CLDSBH]`.

11. evaporation of precipitation and
 The downdraft.
 of cloud temperature, specific humidity and mass flux
 Calculates the vertical distribution `MODULE:[DWNEVP]`.

12. by downdraft detrainment.
 Calculate the change of temperature and specific humidity `MODULE:[CLDDDE]`.

13. by the compensatory upward flow of downdrafts.
 Calculate the change of temperature and specific humidity `MODULE:[CLDSBH]`.

### The Basic Framework of the Arakawa-Schubert Scheme

Cloud Mass Flux $M$, Detrainment $D$ is,

$$
  M(z)     =  M_B \eta(z) \; , \\
  D(z)     =  M_B \eta(z_T) \delta (z-z_T) \; .
$$



represented as .
The mass flux at the cloud base ($M_B$) is the mass flux at $z_B$,
$\eta$ is a dimensionless mass flux in it.

From this, the time variation of the mean field is calculated as

$$
  \frac{\partial \bar{h}}{\partial t}  =  M \frac{\partial \bar{h}}{\partial z} 
                       + D( h^t - \bar{h} ) \; , \\
  \frac{\partial \bar{q}}{\partial t}  =  M\frac{\partial \bar{q}}{\partial z} 
                       + D( q^t + l^t - \bar{q} ) \; .
$$



However, $\bar{h}, \bar{q}$ are based on the wet static energy of the mean field and the specific humidity,
$h^t, q^t, l^t$ are the air in the detrainment
It is the wet static energy, specific humidity, and cloud water content.

$\eta, h^t, q^t, l^t$ are required by the cloud model.
$M_B$ is obtained by the closure assumption using the cloud work function.

### Cloud Model.

The cloud model is essentially an entrained-purume model.
Each type of cloud is characterized by an entrainment rate,
It will have various cloud top heights accordingly.
However, for the sake of later calculations,
Here, you can specify the cloud top altitude,
By finding the corresponding entrainment rate
Find the vertical structure of clouds.
By assuming a linear mass flux increase with respect to height.
This calculation is simplified to a form that does not include a sequential approximation.

Let's set the cloudbase altitude at $z_T$,
The lifted condensation altitude of the surface atmosphere, i.e., the height of condensation,

$$
   \bar{q}(0) \geq
                \bar{q}^*(z)
                + \frac{\gamma}{L(1+\gamma)} 
                    \left(\bar{h}(0)-\bar{h}(z) \right) \; , 
$$


Define it as the minimum $z$ that meets the following criteria

The dimensionless mass flux $\eta$ is,
The entrainment rate is set to $\lambda$,

$$
  \frac{\partial \eta}{\partial z} = \lambda \; ,
$$


Namely,

$$
  \eta (z)  =  1 + \lambda ( z - z_B ) \\
            \equiv  1 + \lambda \hat{\eta}(z)  \; .
$$



The balance on wet static energy $h^c$ and total water content $w^c$ in the clouds is,

$$
  \frac{\partial }{\partial z}( \eta h^c   )  =  \lambda \bar{h}      \; , \\
  \frac{\partial }{\partial z}( \eta w^c   )  =  \lambda \bar{q} - \pi  \; .
$$



Here, $\bar{h}, \bar{q}, \pi$ are respectively,
$h$ and $q$, in mean field, are precipitation generation.

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




The mass flux is assumed to be zero at the surface,
It is assumed to increase linearly below the cloud base,

$$
 \eta (z) =   \frac{z}{z_B} \; \; \; ( z<z_B ) \; .
$$


By calculating the entrainment below this cloud base,
$h^c,w^c$ are required at cloudbase. That is, ,

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





where $T_v$ is the provisional temperature and $q^*$ is the saturation specific humidity,
$\epsilon = R_{{H}_2{O}}/R_{{air}} -1$,
It is $\gamma = L/C_p \partial q^*/\partial T$,
$\bar{q}^*, \bar{h}^*$ indicate the values at mean-field saturation, respectively.
$q^c, l^c$ are the amounts of cloud water vapor and cloud water,

$$
  q^c  =  q^*(T^c) \, \simeq \,
           \bar{q}^* + \frac{1}{L(1+\gamma)} ( h^c - \bar{h}^* ) \; , \\  
  l^c  =  w^c - q^c \; .
$$



For the cloud top $z_T$, the buoyancy $B$ is assumed to be zero.
Thus, solving the $B(z_T)=0$ corresponds to the given cloud top height of $z_T$
$\lambda$ can be obtained.
Here, for precipitation rate $R(z)$ integrated from the ground upward, we have a problem,
Using the known function $r(z)$
Assume that it is represented.

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



As mentioned above, you should specify $\lambda$ to obtain $z_T$,
A physically meaningful $\lambda$ for a given $z_T$
There is no guarantee that we will seek it.
That scrutiny is necessary, but here it is,
The smaller the $\lambda$ is, the more the $z_T$ is
Take into account that it should be lower.

$$
  \frac{\partial \lambda}{\partial z_T} < 0
$$


We will examine whether or not the
If the value is not satisfied, assume that the cloud with cloud top $z_T$ does not exist.
Also, a minimum value has been set for $\lambda$,
We assume that there are no smaller $\lambda$ clouds.
This means that the entrainment rate can be reduced by
Given the inverse proportions ,
The equivalent of having a maximum in the size of the plume.

Cloud water content $l^c(z)$ is ,

$$
  l^c(z)  =  w^a(z)-q^c(z)-R(z)/\eta(z)   \\
          =  \left( 1-r(z) \right) \left[ w^a(z)-q^c(z) \right] \; .
$$



However, in the case of $w^a(z) < q^c(z)$, it is $l^c(z)=0$.
Furthermore, it is unlikely that a precipitation event will turn into cloudy water once it has risen,
$R(z)$ must be an increasing function of $z$.
This will limit the $r(z)$.

The characteristic value of the detrainment air is ,

$$
  h^t  =  h^c(z_T) \; , \\
  q^t  =  q^c(z_T) \; , \\
  l^t  =  l^c(z_T) \; .
$$




In the case of $ h^c(z_B) < \bar{h}^* (z_T) $,
Suppose that clouds do not exist. In this case,

$$
  \bar{h}(z'_B) > \bar{h}^* (z_T) \; , \;\;\; z_B < z < z_T 
$$


If there is a $z'_B$ that satisfies ,
The area directly above it has been renamed $z_B$,

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

> <span id="p-cum:cwf" label="p-cum:cwf "> >P-Cum[p-cum:cwff\\]</span>

Essentially, the work associated with the downdraft, discussed below, should be
It should be accounted for, but we'll ignore it here for simplicity's sake.

In this calculation, we start at the bottom and
Once a positively buoyant cloud is negatively buoyant, if ,
Since there should be cloud tops where they are supposed to be negative,
Assume that the cloud with the cloud top we are considering does not exist.

### Cloud Mass Flux at Cloudbase

The cloud mass flux at the cloud base is ,
On some time scale $\tau_a$,
Cloud action determines the cloud work function to be close to zero
I make the assumption that.

In order to estimate it, we firstly estimated the unit cloud-bottom mass flux of $M_0$
Find the time variation of the mean field.

$$
  \frac{\partial \bar{h}'}{\partial t}  =  M_0 \eta \frac{\partial \bar{h}}{\partial z} 
                       + \eta(z_T) \delta(z-z_T) ( h^t - \bar{h} ) \; , \\
  \frac{\partial \bar{q}'}{\partial t}  =  M_0 \eta \frac{\partial \bar{q}}{\partial z} 
                       + \eta(z_T) \delta(z-z_T) ( q^t + l^t - \bar{q} ) \; .
$$



With this,

$$
  \bar{h}'  =  \bar{h} + \frac{\partial \bar{h}'}{\partial t} \delta t \; , \\
  \bar{q}'  =  \bar{q} + \frac{\partial \bar{q}'}{\partial t} \delta t 
$$



and using $\bar{h}', \bar{q}'$
Calculated from the cloud work function ([p-cum:cwf\]](#p-cum:cwf)) as $A'$.

So..,

$$
  M_B = \frac{A}{A-A'} \frac{\delta t}{\tau_a} M_0 
$$


That would be.
Here, when determining $A'$, it should be set to $\bar{h}', \bar{q}'$ We've got it.
I should recalculate the vertical structure of the clouds,
Now we are using the same cloud structure.

### Cloud Mass Flux, Precipitation

The sum of the clouds at each cloud top altitude,
Cloud Mass Flux $M$

$$
  M(z)   = \int^i M_B^i \eta^i(z) \; .
$$


Also, precipitation flux $P(z)$ is

$$
 P(z) = \int_i M_B^i \left[ R^i(z_T)-R^i(z) \right]  \; .
$$


### Time variation of the average field

by compensated downstream flow and detraining.
The time variation of the mean field is calculated as follows

$$
  \frac{\partial \bar{h}}{\partial t}  =  M \frac{\partial \bar{h}}{\partial z} 
                    + \int_i D^i ( (h^t)^i - \bar{h} ) \; , \\
  \frac{\partial \bar{q}}{\partial t}  =  M\frac{\partial \bar{q}}{\partial z} 
                    + \int_i D^i ( (q^t)^i + (l^t)^i - \bar{q}(z_T^i) ) \; .
$$



However, it is $D^i = M_B^i \eta^i(z_T^i)$.

### Evaporation and downdrafting of precipitation

Precipitation falls through the unsaturated atmosphere, while some of it evaporates.
In addition, some of them form a downdraft.

Evaporation Rate $E$ is ,

$$
 E = \rho a_e {\rho_p}^{b_e} \left( \bar{q}_{w} - \bar{q} \right) \; ,
$$


Note that $\bar{q}_{w}$ is the saturation specific humidity corresponding to the wet bulb temperature,

$$
  \bar{q}_w = \bar{q} 
            + \frac{\bar{q}^* - \bar{q}}{1+ \frac{L}{C_P}\frac{\partial q^*}{\partial T}} \; .
$$


$a_e, b_e$ is a parameter of the microphysics.
$\rho_p$ is the density of precipitation particles and $V_T$ is the terminal velocity of precipitation,

$$
  \rho_p = \frac{P}{V_T} \; .
$$


The current standard values are $a_e=0.25$, $b_e=1$ and $V_T=10$ m/s.

For downdrafting, we make the following assumptions.

 - $\bar{h}$ decreases monotonically with altitude above cloudbase
 If the upper end of the region is set to $z_d$, the downdraft is
 It occurs in the region of     $z < z_d$.

 - A certain percentage of the precipitation evaporation that occurs at each altitude
 It is used to form downdrafts.
 Evaporation of precipitation has just saturated it.
 The air in the surrounding area.
 Taken into the downdraft (Entrainment).

 - In $z < z_B$, detraining occurs,
 The mass flux decreases linearly.

That is, in $z_B < z < z_d$, the mass flux $M^d(z)$,
The downdraft air masses $h^d(z),q^d(z)$ follow the following equation.
Upon evaporation of precipitation, the wet static energy should be conserved,
and the specific humidity when saturated by evaporation.
Note that this is $\bar{q}_{w}$.

$$
  \frac{\partial M^d}{\partial z} =  - f_d \frac{E}{\bar{q}_{w}-\bar{q}} \;  ,
$$


$$
  \frac{\partial }{\partial z} ( M^d h^d )  =  \bar{h}     \frac{\partial M^d}{\partial z} \; ,\\
  \frac{\partial }{\partial z} ( M^d q^d )  =  \bar{q}_{w} \frac{\partial M^d}{\partial z} \; .
$$



In the above equation, $f_d$ is the portion of the evaporation that is taken up by the downdraft,
$(1-f_d)$ evaporates directly into the mean field.
However, the downdraft mass flux $M^d$
The total mass flux of cloud base shall not exceed the $f_m$ of $M$.
The current standard value is $f_d=0.5, f_m=1.0$.

### cloud water and cloud cover

The lattice-averaged cloud water content used for radiation, $l^{cR}$, is
Strong upwelling areas of cumulus clouds, including cloud water $l^c$
If the ratio of the ratio to the $\delta^c$ ,

$$
  l^{cR} = \delta^c l^c \; .
$$


The mass flux $M^c$ is the same as this $\delta^c$
Using the vertical velocity of the upstream stream, $v^c$

$$
  M = \delta^c \rho v^c 
$$


So, in the end,

$$
  l^{cR} = \frac{M^c}{\rho v^c} l^c = \alpha M^c l^c \; .
$$


The cloud cover used to estimate radiation, $C^c$, is ,
that there is actually a horizontal spread in the distribution of upwelling and cloud water.
It is reasonable to take a larger value than this $\delta^c$.
Here, in brief,

$$
  C^c = \beta M_B
$$


.
The current standard values are $\alpha=0.3$ and $\beta=10$.
