## Massive Coagulation

### Overview of Large Scale Condensation Schemes.

The large-scale condensation scheme is used to represent cloud-related condensation processes other than cumulus convection, and to calculate the latent heat release, water vapor loss, and precipitation. The amount of cloud water and cloud coverage involved in the radiation are also calculated. The main input data are temperature ($T$), specific humidity ($q$), and cloud water content ($l$), and the output data are the rate of change of temperature, specific humidity, and cloud water content over time ($\partial T/\partial t, \partial q/\partial t, \partial l/\partial t$), $\partial T/\partial t, \partial q/\partial t, \partial l/\partial t$, and cloud cover ($C$).

In addition to the water-vapor mixing ratio (specific humidity $q$), cloud water content ($l$) is also predicted in the CCSR/NIES AGCM model. In practice, the large-scale condensation routine first calculates the sum of these two variables, total water ($q^t = q+l$), and then divides the sum into cloud water and water vapor, so that the model has only one predictor, total water ($q^t$). By assuming the distribution of the variation of $q^t$ within a grid, the cloud cover (horizontal cloud coverage) and cloud water content within each grid is diagnosed. The conversion of cloud water into precipitation and the evaporation of precipitation during its fall are also considered.

The outline of the calculation procedure is as follows.

1. add the amount of water vapor ($q$) and the amount of cloud water ($l$) to obtain the total amount of water ($q^t$). The air temperature is obtained by evaporating cloud water, liquid water temperature $T_l$

2. assume the distribution of the variation of $q^t$, obtain the cloud cover and separate it into cloud water and water vapor again.

The distribution of cloud cover, cloud water content, and water vapor is determined by successive approximations, taking into account the temperature variation caused by condensation.

4. evaluate the conversion of cloud water to precipitation.

5. evaluate the ice fall.

6. evaluate precipitation and evaporation of falling ice.

### Diagnosis of cloud water levels

Given a grid-averaged total water volume ($\bar{q}^t = \bar{q} + \bar{l}$), the total water volume ($q^t$) is assumed to be uniformly distributed between $(1-b)\bar{q}^t$ and $(1+b)\bar{q}^t$. In other words, the probability density function is defined as

$$
  F(q^t) = \left\{ 
           \begin{array}{ll}
             (2b\bar{q}^t)^{-1} \; \; 
                 (1-b)\bar{q}^t < q^t <  (1+b)\bar{q}^t \\
             0                         その他
           \end{array}
           \right. \; .
$$


This distribution is considered to be a horizontal distribution. On the other hand, the lattice mean of $\bar{q}^*$ is used for the saturated specific humidity.

Consider a cloud in a grid point, in the region of $q^t > q^*$ (Figure [lsc:fig-cloud\]](#lsc:fig-cloud).

Then, as shown in the shading of the figure, the horizontal ratio of the area where the total water volume exceeds the saturation, $C$, is

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

The cloud cover ($l$) is the result of integrating $q^t - q^*$ in the region where $q^t > q^*$ is found,

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

First, find the total water volume ($q^t$) and liquid water temperature ($T_l$) from the steam $q$ and the cloud water $l$ and the temperature ($T$).

$$
  q^t   =  q + l \; , \\
  T_l   =  T - \frac{L}{C_P} l \; .
$$



$T_l$ corresponds to the temperature at which all cloud water is evaporated. $T^{(0)} = T_l$ and $l^{(0)} = 0$ are defined as follows.

Assuming that $l^{(1)}$ is the amount of cloud water evaluated by the aforementioned method as a function of the saturation specific humidity relative to the temperature ($T_l$), the temperature will change,

$$
  T^{(1)} = T_l +  \frac{L}{C_P} l^{(1)} \; .
$$


This temperature is solved by successive approximations to $l^{(2)}$ as the evaluated cloud water content and $T^{(2)}$ as the temperature changed by the saturation specific humidity. In order to accelerate this successive convergence, the Newton method is employed. In other words, instead of (260), we use

$$
  T^{(1)} = T_l +  \frac{L}{C_P} l^{(1)} 
                   \left( 1 - \frac{L}{C_P} \frac{dl}{dT} \right)^{-1}
$$


We assume that $dl/dT$ can be obtained analytically using (257).

### precipitation process.

Precipitation depends on the diagnosed cloud water content. If the precipitation rate (in 1/s) is set to $P$,

$$
  P = l / \tau_P \; .
$$


$\tau_P$ is a precipitation time scale,

$$
  \tau_P  = \tau_0 \left\{ 1 - \exp\left[ - \left(\frac{l}{l_C}\right)^2  
                                   \right]  \right\}^{-1} \; .
$$


Here, $l_C$ is the critical cloud water content, taking into account the Bergeron-Findeisen effect,

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


$l_C^0=10^{-4}$, $\alpha=50$, $\beta=0.03$, $T_0=273.15$ K, $T_c=258.15$ K.

Precipitation results in a decrease in $l$.

$$
  P          =  l / \tau_P \; , \\
  \frac{\partial{l}}{\partial {t}}  =  -P \; .
$$



Integrating this during $\Delta t$,

$$
  P \Delta t  =  \left\{ 1- \exp(- \Delta t/\tau_P) \right\} l \; .
$$


If the precipitation flux (in kg m$^{-2}$ s$^{-1}$) at a certain height ($p$) is defined as $F_P$,

$$
  F_P(p) = \int_0^p P \frac{dp}{g} \; .
$$


### Ice Falling Process.

The cloud water is divided into ice clouds and water clouds depending on the temperature. The ratio of ice clouds is

$$
   f_I = \frac{ T_0 - T }{ T_0 - T_1 }
$$


(with a maximum value of 1 and a minimum value of 0). We also consider the effect of the ice cloud in $T_0 = 273.15{K}, T_1 = 258.15{K}$, assuming that it descends slowly. The rate of descent ($V_S$) is

$$
  V_S = V_S^0 ( \rho_a f_I l )^\gamma \; .
$$


However, $V_S^0=3$ m/s, $\gamma=0.17$,

$$
  \tau_S = \frac{\Delta p}{\rho g V_S} 
$$


as well as precipitation.

### Evaporation process of precipitation.

Evaporation of precipitation $E$ is estimated to be as follows.

$$
E = k_E (q^w - q) \frac{F_P}{V_T} \; .
$$


If $q^w < q$ is set to 0, however, it is set to 0. $q_w$ is the saturation specific humidity corresponding to the wet bulb temperature,

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

The calculations are performed from the topmost layer down. For convenience, the calculation starts from evaluating the evaporation of precipitation from the layer above the precipitation layer.

Falling ice is treated as cloud water already in the layer below, and is included in the total water volume.
