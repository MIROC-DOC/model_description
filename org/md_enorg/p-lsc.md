## Massive Coagulation

### Overview of Large Scale Condensation Schemes.

The large-scale condensation scheme is used to represent cloud-related condensation processes other than cumulus convection, and to calculate the latent heat release, water vapor loss, and precipitation. The amount of cloud water and cloud coverage involved in the radiation are also calculated. The main input data are temperature (TERM00586), specific humidity (TERM00587), and cloud water content (TERM00588), and the output data are the rate of change of temperature, specific humidity, and cloud water content over time (TERM00589), TERM00589, and cloud cover (TERM00590).

In addition to the water-vapor mixing ratio (specific humidity TERM00591), cloud water content (TERM00592) is also predicted in the CCSR/NIES AGCM model. In practice, the large-scale condensation routine first calculates the sum of these two variables, total water (TERM00593), and then divides the sum into cloud water and water vapor, so that the model has only one predictor, total water (TERM00594). By assuming the distribution of the variation of TERM00595 within a grid, the cloud cover (horizontal cloud coverage) and cloud water content within each grid is diagnosed. The conversion of cloud water into precipitation and the evaporation of precipitation during its fall are also considered.

The outline of the calculation procedure is as follows.

1. add the amount of water vapor (TERM00596) and the amount of cloud water (TERM00597) to obtain the total amount of water (TERM00598). The air temperature is obtained by evaporating cloud water, liquid water temperature TERM00599

2. assume the distribution of the variation of TERM00600, obtain the cloud cover and separate it into cloud water and water vapor again.

The distribution of cloud cover, cloud water content, and water vapor is determined by successive approximations, taking into account the temperature variation caused by condensation.

4. evaluate the conversion of cloud water to precipitation.

5. evaluate the ice fall.

6. evaluate precipitation and evaporation of falling ice.

### Diagnosis of cloud water levels

Given a grid-averaged total water volume (TERM00601), the total water volume (TERM00602) is assumed to be uniformly distributed between TERM00603 and TERM00604. In other words, the probability density function is defined as

     EQ=00221.

This distribution is considered to be a horizontal distribution. On the other hand, the lattice mean of TERM00605 is used for the saturated specific humidity.

Consider a cloud in a grid point, in the region of TERM00606 (Figure [lsc:fig-cloud\]](#lsc:fig-cloud).

Then, as shown in the shading of the figure, the horizontal ratio of the area where the total water volume exceeds the saturation, TERM00607, is

     EQ=00222.

and this is the cloud cover (horizontal cloud coverage).

The cloud cover (TERM00608) is the result of integrating TERM00610 in the region where TERM00609 is found,

     EQ=00223.

### Determination by successive approximation

First, find the total water volume (TERM00614) and liquid water temperature (TERM00615) from the steam TERM00611 and the cloud water TERM00612 and the temperature (TERM00613).

     EQ=00238.
     EQ=00238.

TERM00616 corresponds to the temperature at which all cloud water is evaporated. TERM00617 and TERM00618 are defined as follows.

Assuming that TERM00620 is the amount of cloud water evaluated by the aforementioned method as a function of the saturation specific humidity relative to the temperature (TERM00619), the temperature will change,

     EQ=00224.

This temperature is solved by successive approximations to TERM00621 as the evaluated cloud water content and TERM00622 as the temperature changed by the saturation specific humidity. In order to accelerate this successive convergence, the Newton method is employed. In other words, instead of (260), we use

     EQ=00225.

We assume that TERM00623 can be obtained analytically using (257).

### precipitation process.

Precipitation depends on the diagnosed cloud water content. If the precipitation rate (in 1/s) is set to TERM00624,

     EQ=00226.

TERM00625 is a precipitation time scale,

     EQ=00227.

Here, TERM00626 is the critical cloud water content, taking into account the Bergeron-Findeisen effect,

     EQ=00228.

TERM00627, TERM00628, TERM00629, TERM00630 K, TERM00631 K.

Precipitation results in a decrease in TERM00632.

     EQ=00239.
     EQ=00239.

Integrating this during TERM00633,

     EQ=00229.

If the precipitation flux (in kg TERM00635 TERM00636) at a certain height (TERM00634) is defined as TERM00637,

     EQ=00230.

### Ice Falling Process.

The cloud water is divided into ice clouds and water clouds depending on the temperature. The ratio of ice clouds is

     EQ=00231.

(with a maximum value of 1 and a minimum value of 0). We also consider the effect of the ice cloud in TERM00638 and TERM00638, assuming that it descends slowly. The rate of descent (TERM00639) is

     EQ=00232.

However, TERM00640 m/s, TERM00641,

     EQ=00233.

as well as precipitation.

### Evaporation process of precipitation.

Evaporation of precipitation TERM00642 is estimated to be as follows.

     EQ=00234.

If TERM00643 is set to 0, however, it is set to 0. TERM00644 is the saturation specific humidity corresponding to the wet bulb temperature,

     EQ=00235.

This means that precipitation is

     EQ=00236.

The temperature drop due to evaporation is estimated to be We also estimate the temperature drop due to evaporation.

     EQ=00237.

### Other Notes.

The calculations are performed from the topmost layer down. For convenience, the calculation starts from evaluating the evaporation of precipitation from the layer above the precipitation layer.

Falling ice is treated as cloud water already in the layer below, and is included in the total water volume.