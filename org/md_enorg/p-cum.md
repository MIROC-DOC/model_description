## cumulus convection

### Overview of the Cumulus Convection Scheme

The cumulus convection scheme is ,
This figure represents the condensation, precipitation and convection processes involved in cumulus convection,
Due to the latent heat release and associated convective motion
Calculate precipitation with temperature and with changes in water vapor content.
We also calculate the cloud water content and cloud coverage involved in the radiation.
The main input data are temperature TERM00000 and specific humidity TERM00001,
The output data is the time rate of change of temperature and specific humidity,
TERM00002,TERM00002,
The cloud water content of the cumulus clouds used for radiation is TERM00003 Cloud volume TERM00004.

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

Cloud Mass Flux TERM00005, Detrainment TERM00006 is,

> EQ=00021.
> EQ=00021.

represented as .
The mass flux at the cloud base (TERM00007) is the mass flux at TERM00008,
TERM00009 is a dimensionless mass flux in it.

From this, the time variation of the mean field is calculated as

> EQ=00022.
> EQ=00022.

However, TERM00010 and TERM00010 are based on the wet static energy of the mean field and the specific humidity,
TERM00011,TERM00011 are the air in the detrainment
It is the wet static energy, specific humidity, and cloud water content.

TERM00012,TERM00012 are required by the cloud model.
TERM00013 is obtained by the closure assumption using the cloud work function.

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

Let's set the cloudbase altitude at TERM00014,
The lifted condensation altitude of the surface atmosphere, i.e., the height of condensation,

> EQ=00000.

Define it as the minimum TERM00015 that meets the following criteria

The dimensionless mass flux TERM00016 is,
The entrainment rate is set to TERM00017,

> EQ=00001.

Namely,

> EQ=00023.
> EQ=00023.

The balance on wet static energy TERM00018 and total water content TERM00019 in the clouds is,

> EQ=00024.
> EQ=00024.

Here, TERM00020 and TERM00020 are respectively,
TERM00021 and TERM00022, in mean field, are precipitation generation.

Integrating,

> EQ=00025.
> EQ=00025.

> EQ=00026.
> EQ=00026.
> EQ=00026.

The mass flux is assumed to be zero at the surface,
It is assumed to increase linearly below the cloud base,

> EQ=00002.

By calculating the entrainment below this cloud base,
TERM00023 and TERM00023 are required at cloudbase. That is, ,

> EQ=00027.
> EQ=00027.

The buoyancy per unit mass flux due to clouds is ,

> EQ=00028.
> EQ=00028.
> EQ=00028.
> EQ=00028.

where TERM00024 is the provisional temperature and TERM00025 is the saturation specific humidity,
TERM00026,
It is TERM00027,
TERM00028 and TERM00028 indicate the values at mean-field saturation, respectively.
TERM00029 and TERM00029 are the amounts of cloud water vapor and cloud water,

> EQ=00029.
> EQ=00029.

For the cloud top TERM00030, the buoyancy TERM00031 is assumed to be zero.
Thus, solving the TERM00032 corresponds to the given cloud top height of TERM00033
TERM00034 can be obtained.
Here, for precipitation rate TERM00035 integrated from the ground upward, we have a problem,
Using the known function TERM00036
Assume that it is represented.

> EQ=00003.

So..,

> EQ=00004.

TERM00037 is easy to solve and,

> EQ=00005.

However,

> EQ=00030.
> EQ=00030.

As mentioned above, you should specify TERM00038 to obtain TERM00039,
A physically meaningful TERM00041 for a given TERM00040
There is no guarantee that we will seek it.
That scrutiny is necessary, but here it is,
The smaller the TERM00042 is, the more the TERM00043 is
Take into account that it should be lower.

> EQ=00006.

We will examine whether or not the
If the value is not satisfied, assume that the cloud with cloud top TERM00044 does not exist.
Also, a minimum value has been set for TERM00045,
We assume that there are no smaller TERM00046 clouds.
This means that the entrainment rate can be reduced by
Given the inverse proportions ,
The equivalent of having a maximum in the size of the plume.

Cloud water content TERM00047 is ,

> EQ=00031.
> EQ=00031.

However, in the case of TERM00048, it is TERM00049.
Furthermore, it is unlikely that a precipitation event will be followed by cloudy water,
TERM00050 must be an increasing function of TERM00051.
This will limit the TERM00052.

The characteristic value of the detrainment air is ,

> EQ=00032.
> EQ=00032.
> EQ=00032.

In the case of TERM00053,
Suppose that clouds do not exist. In this case,

> EQ=00007.

If there is a TERM00054 that satisfies ,
The area directly above it has been renamed TERM00055,

> EQ=00033.
> EQ=00033.

Seek as .

### Cloud Work Function (CWF)

The cloud work function (CWF), TERM00056 is,

> EQ=00008.

It is,

> EQ=00009.
> <span id="p-cum:cwf" label="p-cum:cwf" label="p-cum:cwf">\blaze[p-cum:cwf]</span>

Essentially, the work associated with the downdraft, discussed below, should be
It should be accounted for, but we'll ignore it here for simplicity's sake.

In this calculation, we start at the bottom and
Once a positively buoyant cloud is negatively buoyant, if ,
Since there should be cloud tops where they are supposed to be negative,
Assume that the cloud with the cloud top we are considering does not exist.

### Cloud Mass Flux at Cloudbase

The cloud mass flux at the cloud base is ,
On some time scale TERM00057,
Cloud action determines the cloud work function to be close to zero
I make the assumption that.

In order to estimate it, we firstly estimated the unit cloud-bottom mass flux of TERM00058
Find the time variation of the mean field.

> EQ=00034.
> EQ=00034.

With this,

> EQ=00035.
> EQ=00035.

and using TERM00059 and TERM00059
Let TERM00060 be the cloud work function calculated from ([p-cum:cwf\]](#p-cum:cwf)).

So..,

> EQ=00010.

That would be.
Here, when obtaining TERM00061, the original TERM00062 and TERM00062 were used
I should recalculate the vertical structure of the clouds,
Now we are using the same cloud structure.

### Cloud Mass Flux, Precipitation

The sum of the clouds at each cloud top altitude,
Cloud Mass Flux TERM00063

> EQ=00011.

Also, precipitation flux TERM00064 is

> EQ=00012.

### Time variation of the average field

by compensated downstream flow and detraining.
The time variation of the mean field is calculated as follows

> EQ=00036.
> EQ=00036.

However, it is TERM00065.

### Evaporation and downdrafting of precipitation

Precipitation falls through the unsaturated atmosphere, while some of it evaporates.
In addition, some of them form a downdraft.

Evaporation Rate TERM00066 is ,

> EQ=00013.

Note that TERM00067 is the saturation specific humidity corresponding to the wet bulb temperature,

> EQ=00014.

TERM00068,TERM00068 is a parameter of the microphysics.
TERM00069 is the density of precipitation particles and TERM00070 is the terminal velocity of precipitation,

> EQ=00015.

The current standard values are TERM00071, TERM00072 and TERM00073 m/s.

For downdrafting, we make the following assumptions.

 - TERM00074 decreases monotonically with altitude above cloudbase
 If the upper end of the region is set to TERM00075, the downdraft is
 It occurs in the region of     TERM00076.

 - A certain percentage of the precipitation evaporation that occurs at each altitude
 It is used to form downdrafts.
 Evaporation of precipitation has just saturated it.
 The air in the surrounding area.
 Taken into the downdraft (Entrainment).

 - In TERM00077, detraining occurs,
 The mass flux decreases linearly.

That is, in TERM00078, the mass flux TERM00079,
The downdraft air masses TERM00080 and TERM00080 follow the following equation.
Upon evaporation of precipitation, the wet static energy should be conserved,
and the specific humidity when saturated by evaporation.
Note that this is TERM00081.

> EQ=00016.

> EQ=00037.
> EQ=00037.

In the above equation, TERM00082 is the portion of the evaporation that is taken up by the downdraft,
TERM00083 evaporates directly into the mean field.
However, the downdraft mass flux TERM00084 is
The total mass flux of cloud base shall not exceed the TERM00086 of TERM00085.
The current standard value is TERM00087,TERM00087.

### cloud water and cloud cover

The lattice-averaged cloud water content used for radiation, TERM00088, is
Strong upwelling areas of cumulus clouds, including cloud water TERM00089
If the ratio of the ratio to the TERM00090 ,

> EQ=00017.

The mass flux TERM00091 is the same as this TERM00092
Using the vertical velocity of the upstream stream, TERM00093

> EQ=00018.

So, in the end,

> EQ=00019.

The cloud cover used to estimate radiation, TERM00094, is ,
that there is actually a horizontal spread in the distribution of upwelling and cloud water.
It is reasonable to take a larger value than this TERM00095.
Here, in brief,

> EQ=00020.

.
The current standard values are TERM00096 and TERM00097.
