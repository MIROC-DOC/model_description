## Massive Coagulation

### Overview of Large Scale Condensation Schemes.

Large-scale condensation schemes are ,
This is a representation of the condensation processes involved in clouds other than cumulus convection,
Calculating latent heat release and water vapor reduction, precipitation.
We also calculate the cloud water content and cloud coverage involved in the radiation.
The main input data are temperature TERM00000, specific humidity TERM00001, and cloud cover TERM00002,
The output data is the time rate of change of temperature, specific humidity and cloud water content,
TERM00003,TERM00003,
The cloud cover is TERM00004.

In the CCSR/NIES AGCM, in addition to the water-vapor mixture ratio (specific humidity TERM00005), the
Cloud water content (TERM00006) is also a forecast variable in the model.
In fact, in this large-scale condensation routine
First, calculate the sum of the two, the total amount of water (TERM00007),
We are dividing it again into cloud water and water vapor,
In effect, the forecast variable is a single total water volume (TERM00008).
By assuming the distribution of the variation of TERM00009 in the grid,
Diagnosis of the cloud cover and cloud water content in each grid.
The conversion of cloud water into precipitation and the evaporation of precipitation during its fall are also considered.

The outline of the calculation procedure is as follows.

1. add the amount of water vapor (TERM00010) and the amount of cloud water (TERM00011)
 Total water volume TERM00012
 The temperature has evaporated the cloud water,
 Set the     liquid water temperature TERM00013.

2. assuming the distribution of the variation in TERM00014,
 Find the cloud cover and separate it again into cloud water and water vapor.

3. considering the temperature change due to condensation,
 By successive approximation
 Determine the cloud cover, cloud water content, and water vapor distribution.

4. evaluate the conversion of cloud water to precipitation.

5. evaluate the ice fall.

6. evaluate precipitation and evaporation of falling ice.

### Diagnosis of cloud water levels

When the grid-averaged total water volume TERM00015 is given,
Distribution of the total water volume TERM00016 in the grid,
Between TERM00017 and TERM00018
It is assumed to be uniformly distributed. That is, the probability density function is ,

     EQ=00000.

We consider this distribution to be a horizontal distribution.
On the other hand, the saturation specific humidity is based on the grid average of TERM00019.

In the grid,
Consider the presence of a cloud in a region in TERM00020 (Figure [lsc[lsc:fig-cloud\]](#lsc:fig-cloud)).

Then, as shown by the shading in the figure, the
The horizontal ratio of the portion of the total water volume exceeding saturation TERM00021 is ,

     EQ=00001.

and this is the cloud cover (horizontal cloud coverage).

In addition, the cloud cover of TERM00022 is in the region of TERM00023
This is an integral of TERM00024,

     EQ=00002.

### Determination by successive approximation

First, from the Water Vapor TERM00025 and Cloud Water TERM00026 and the Temperature TERM00027,
Find the total water volume TERM00028 and liquid water temperature TERM00029.

     EQ=00017.
     EQ=00017.

The TERM00030 corresponds to the temperature at which all cloud water is evaporated.
TERM00031, TERM00032

By saturation specific humidity relative to temperature TERM00033,
Assuming that the cloud water content evaluated by the aforementioned method is TERM00034,
It changes the temperature,

     EQ=00003.

The cloud water content evaluated using the saturation specific humidity versus temperature was estimated from TERM00035,
The resulting temperature change is solved by successive approximation as TERM00036 ...
In order to speed up this sequential convergence, we use the Newton method.
That is, instead of (6)

     EQ=00004.

.
TERM00037 can be obtained analytically using (3).

### precipitation process.

Precipitation occurs dependent on the amount of cloud water diagnosed.
If the precipitation rate (in 1/s) is set to TERM00038,

     EQ=00005.

TERM00039 is the time scale of precipitation,

     EQ=00006.

where TERM00040 is the critical cloud water content,
In view of the Bergeron-Findeisen effect ,

     EQ=00007.

TERM00041, TERM00042, TERM00043,
TERM00044 K, TERM00045 K

Precipitation results in a decrease in TERM00046.

     EQ=00018.
     EQ=00018.

Integrating this during TERM00047,

     EQ=00008.

Precipitation flux at a certain height, TERM00048
If (unit kg TERM00049 TERM00050) is set to TERM00051

     EQ=00009.

### Ice Falling Process.

Cloud water is divided into ice and water clouds depending on the temperature.
The ice cloud ratio is

     EQ=00010.

(but with a maximum value of 1 and a minimum value of 0). Also,
TERM00052,TERM00052.
The ice cloud will fall at a slow speed,
Consider the effect. Rate of descent TERM00053 is,

     EQ=00011.

However, TERM00054 m/s, TERM00055.
So..,

     EQ=00012.

as well as precipitation.

### Evaporation process of precipitation.

Evaporation of precipitation The evaporation of precipitation, TERM00056, is estimated as follows.

     EQ=00013.

However, if TERM00057 is set, this should be zero.
The TERM00058 is the saturation specific humidity corresponding to the wet bulb temperature,

     EQ=00014.

This means that precipitation is

     EQ=00015.

The temperature drop due to evaporation is estimated to be We also estimate the temperature drop due to evaporation.

     EQ=00016.

### Other Notes.

Calculations are made from the topmost layer down.
 For convenience, the calculation is based on the precipitation from the upper layers of the
 We start by evaluating evaporation in that layer.

2. fallen ice in the layer just below.
 It will be treated the same as the cloud water that already exists in that layer,
 incorporated into the total water volume.