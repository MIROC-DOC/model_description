## Massive Coagulation

### Overview of Large Scale Condensation Schemes.

Large-scale condensation schemes are ,
This is a representation of the condensation processes involved in clouds other than cumulus convection,
Calculating latent heat release and water vapor reduction, precipitation.
We also calculate the cloud water content and cloud coverage involved in the radiation.
The main input data are temperature $T$, specific humidity $q$, and cloud cover $l$,
The output data is the time rate of change of temperature, specific humidity and cloud water content,
$\partial T/\partial t, \partial q/\partial t, \partial l/\partial t$,
The cloud cover is $C$.

In the CCSR/NIES AGCM, in addition to the water-vapor mixture ratio (specific humidity $q$), the
Cloud water content ($l$) is also a forecast variable in the model.
In fact, in this large-scale condensation routine
First, calculate the sum of the two, the total amount of water ($q^t = q+l$),
We are dividing it again into cloud water and water vapor,
In effect, the forecast variable is a single total water volume ($q^t$).
By assuming the distribution of the variation of $q^t$ in the grid,
Diagnosis of the cloud cover and cloud water content in each grid.
The conversion of cloud water into precipitation and the evaporation of precipitation during its fall are also considered.

The outline of the calculation procedure is as follows.

1. add the amount of water vapor ($q$) and the amount of cloud water ($l$)
 Total water volume $q^t$
 The temperature has evaporated the cloud water,
 Set the     liquid water temperature $T_l$.

2. assuming the distribution of the variation in $q^t$,
 Find the cloud cover and separate it again into cloud water and water vapor.

3. considering the temperature change due to condensation,
 By successive approximation
 Determine the cloud cover, cloud water content, and water vapor distribution.

4. evaluate the conversion of cloud water to precipitation.

5. evaluate the ice fall.

6. evaluate precipitation and evaporation of falling ice.

### Diagnosis of cloud water levels

When the grid-averaged total water volume $\bar{q}^t = \bar{q} + \bar{l}$ is given,
Distribution of the total water volume $q^t$ in the grid,
Between $(1-b)\bar{q}^t$ and $(1+b)\bar{q}^t$
It is assumed to be uniformly distributed. That is, the probability density function is ,

$$
  F(q^t) = \left\{ 
           \begin{array}{ll}
             (2b\bar{q}^t)^{-1} \; \; 
                 (1-b)\bar{q}^t < q^t <  (1+b)\bar{q}^t \\
             0                         その他
           \end{array}
           \right. \; .
$$


We consider this distribution to be a horizontal distribution.
On the other hand, the saturation specific humidity is based on the grid average of $\bar{q}^*$.

In the grid,
Consider the presence of a cloud in a region in $q^t > q^*$ (Figure [lsc[lsc:fig-cloud\]](#lsc:fig-cloud)).

Then, as shown by the shading in the figure, the
The horizontal ratio of the portion of the total water volume exceeding saturation $C$ is ,

$$
  C = \left\{ 
           \begin{array}{ll}
             0 \; \;  (1+b)\bar{q}^t \leq \bar{q}^* \\
             \displaystyle
             \frac{(1+b)\bar{q}^t - \bar{q}^*}
                  {2b\bar{q}^t}                    
               \; \;  (1-b)\bar{q}^t < \bar{q}^* < (1+b)\bar{q}^t \\
             1 \; \;  (1-b)\bar{q}^t \leq \bar{q}^*
           \end{array}
        \right.
$$


and this is the cloud cover (horizontal cloud coverage).

In addition, the cloud cover of $l$ is in the region of $q^t > q^*$
This is an integral of $q^t - q^*$,

$$
  l = \left\{ 
           \begin{array}{ll} \displaystyle
             0 \; \;  (1+b)\bar{q}^t \leq \bar{q}^* \\
            \displaystyle
             \frac{\left[(1+b)\bar{q}^t - \bar{q}^*\right]^2}
                  {4b\bar{q}^t}
               \; \;  (1-b)\bar{q}^t \leq \bar{q}^* \leq (1+b)\bar{q}^t  \\
            \displaystyle
             \bar{q}^t - \bar{q}^*
                \; \;  (1-b)\bar{q}^t \geq \bar{q}^*
           \end{array}
        \right. 
$$


### Determination by successive approximation

First, from the Water Vapor $q$ and Cloud Water $l$ and the Temperature $T$,
Find the total water volume $q^t$ and liquid water temperature $T_l$.

$$
  q^t   =  q + l \; , \\
  T_l   =  T - \frac{L}{C_P} l \; .
$$



The $T_l$ corresponds to the temperature at which all cloud water is evaporated.
$T^{(0)} = T_l$, $l^{(0)} = 0$

By saturation specific humidity relative to temperature $T_l$,
Assuming that the cloud water content evaluated by the aforementioned method is $l^{(1)}$,
It changes the temperature,

$$
  T^{(1)} = T_l +  \frac{L}{C_P} l^{(1)} \; .
$$


The cloud water content evaluated using the saturation specific humidity versus temperature was estimated from $l^{(2)}$,
The resulting temperature change is solved by successive approximation as $T^{(2)}$ ...
In order to speed up this sequential convergence, we use the Newton method.
That is, instead of (6)

$$
  T^{(1)} = T_l +  \frac{L}{C_P} l^{(1)} 
                   \left( 1 - \frac{L}{C_P} \frac{dl}{dT} \right)^{-1}
$$


.
$dl/dT$ can be obtained analytically using (3).

### precipitation process.

Precipitation occurs dependent on the amount of cloud water diagnosed.
If the precipitation rate (in 1/s) is set to $P$,

$$
  P = l / \tau_P \; .
$$


$\tau_P$ is the time scale of precipitation,

$$
  \tau_P  = \tau_0 \left\{ 1 - \exp\left[ - \left(\frac{l}{l_C}\right)^2  
                                   \right]  \right\}^{-1} \; .
$$


where $l_C$ is the critical cloud water content,
In view of the Bergeron-Findeisen effect ,

$$
  l_C = \left\{ 
        \begin{array}{ll}
          l_C^0 \; \;  T \ge T_0 \\
          l_C^0 \left\{ 1+\alpha \exp\left[ - \beta(T-Tc)^2 \right] 
                \right\}^{-1}\; \; 
                       T_0 > T >  T_c \\
          l_C^0 ( 1+\alpha )^{-1}
                       T \le T_c
        \end{array}
        \right. \; .
$$


$l_C^0=10^{-4}$, $\alpha=50$, $\beta=0.03$,
$T_0=273.15$ K, $T_c=258.15$ K

Precipitation results in a decrease in $l$.

$$
  P          =  l / \tau_P \; , \\
  \frac{\partial{l}}{\partial {t}}  =  -P \; .
$$



Integrating this during $\Delta t$,

$$
  P \Delta t  =  \left\{ 1- \exp(- \Delta t/\tau_P) \right\} l \; .
$$


Precipitation flux at a certain height, $p$
If (unit kg m$^{-2}$ s$^{-1}$) is set to $F_P$

$$
  F_P(p) = \int_0^p P \frac{dp}{g} \; .
$$


### Ice Falling Process.

Cloud water is divided into ice and water clouds depending on the temperature.
The ice cloud ratio is

$$
   f_I = \frac{ T_0 - T }{ T_0 - T_1 }
$$


(but with a maximum value of 1 and a minimum value of 0). Also,
$T_0 = 273.15{K}, T_1 = 258.15{K}$.
The ice cloud will fall at a slow speed,
Consider the effect. Rate of descent $V_S$ is,

$$
  V_S = V_S^0 ( \rho_a f_I l )^\gamma \; .
$$


However, $V_S^0=3$ m/s, $\gamma=0.17$.
So..,

$$
  \tau_S = \frac{\Delta p}{\rho g V_S} 
$$


as well as precipitation.

### Evaporation process of precipitation.

Evaporation of precipitation The evaporation of precipitation, $E$, is estimated as follows.

$$
E = k_E (q^w - q) \frac{F_P}{V_T} \; .
$$


However, if $q^w < q$ is set, this should be zero.
The $q_w$ is the saturation specific humidity corresponding to the wet bulb temperature,

$$
  q^w = q + \frac{q^* - q}{1+ \frac{L}{C_P}\frac{\partial{q^*}}{\partial {T}}} \; .
$$


This means that precipitation is

$$
  F_P(p) = \int_0^p (P - E) \frac{dp}{g}
$$


The temperature drop due to evaporation is estimated to be We also estimate the temperature drop due to evaporation.

$$
  \frac{\partial{T}}{\partial {t}} = - \frac{L}{C_P} E \; .
$$


### Other Notes.

Calculations are made from the topmost layer down.
 For convenience, the calculation is based on the precipitation from the upper layers of the
 We start by evaluating evaporation in that layer.

2. fallen ice in the layer just below.
 It will be treated the same as the cloud water that already exists in that layer,
 incorporated into the total water volume.
