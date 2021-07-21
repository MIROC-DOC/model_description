## cumulus convection

### Overview of the Cumulus Convection Scheme

The cumulus convection scheme describes the condensation, precipitation, and convection processes involved in cumulus convection, and calculates changes in temperature and water vapor content and precipitation due to latent heat release and associated convective motion. It also calculates the cloud water content and cloud coverage involved in radiation. The main input data are temperature (TERM00488) and specific humidity (TERM00489), and the output data are the time rate of change of temperature and specific humidity, TERM00490, TERM00490, and cloud cover (TERM00491) of cumulus clouds used for radiation (TERM00492).

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

The cloud mass flux TERM00493, detraining TERM00494 is ,

     EQ=00204.
     EQ=00204.

expressed as where TERM00495 is the mass flux at the cloud base TERM00496 and TERM00497 is the dimensionless mass flux at that point.

From this, the time variation of the mean field is calculated as

     EQ=00205.
     EQ=00205.

where TERM00498 and TERM00498 are the wet static energy and specific humidity of the mean field, and TERM00499 and TERM00499 are the wet static energy, specific humidity and cloud water content of the air in the detrainment.

TERM00500 and TERM00500 are determined by the cloud model. TERM00501 is obtained by closure assumptions using the cloud work function.

### Cloud Model.

The cloud model is essentially an entrained-purume model. Each cloud is characterized by an entrainment rate, and has various cloud-top heights, depending on the entrainment rate. For the sake of the sake of later computation, we will specify the cloud top height and obtain the corresponding entrainment rate to obtain the vertical structure of the clouds. By assuming a linear increase in mass flux with respect to height, we can obtain the vertical structure of the cloud. This calculation is simplified to a form that does not include a sequential approximation.

The cloud base altitude (TERM00502) is defined as the lifted condensation height of the surface atmosphere, i.e,

     EQ=00183.

Define it as the lowest TERM00503 that meets the requirements of the

The dimensionless mass flux TERM00504 has the entrainment rate as TERM00505,

     EQ=00184.

Namely,

     EQ=00206.
     EQ=00206.

The balance of payments for wet static energy TERM00506 and total water volume TERM00507 in the clouds is,

     EQ=00207.
     EQ=00207.

where TERM00508 and TERM00508 are mean field TERM00509 and TERM00510, precipitation production, respectively.

Integrating,

     EQ=00208.
     EQ=00208.

     EQ=00209.
     EQ=00209.
     EQ=00209.

The mass flux is assumed to be zero at the surface and to increase linearly below the cloud base,

     EQ=00185.

By calculating the entrainment below the cloud base, we can obtain the values of TERM00511 and TERM00511 at the cloud base. In other words,

     EQ=00210.
     EQ=00210.

The buoyancy per unit mass flux due to clouds is ,

     EQ=00211.
     EQ=00211.
     EQ=00211.
     EQ=00211.

Here, TERM00512 is the provisional temperature, TERM00513 is the saturated specific humidity, TERM00514, and TERM00515, and TERM00516 and TERM00516 represent the values at the saturation of the mean field, respectively. TERM00517 and TERM00517 are the cloud water vapor and cloud water content, respectively,

     EQ=00212.
     EQ=00212.

For the cloud top (TERM00518), the buoyancy TERM00519 is zero. Therefore, solving for TERM00520 yields TERM00522, which corresponds to a given cloud top height (TERM00521). Here, the precipitation rate (TERM00523) integrated upward from the ground surface is assumed to be expressed by the well-known function TERM00524 as follows

     EQ=00186.

So..,

     EQ=00187.

TERM00525 is easy to solve and,

     EQ=00188.

However,

     EQ=00213.
     EQ=00213.

As mentioned above, we originally set TERM00526 to obtain TERM00527 and there is no guarantee that a physically meaningful TERM00529 can be obtained for a given TERM00528. Although this needs to be examined, we will take into account that the smaller the value of TERM00530, the lower the value of TERM00531 should be.

     EQ=00189.

If not, we assume that there are no clouds with a cloud top (TERM00532). A minimum value is set for TERM00533, and no cloud with a TERM00534 smaller than this value is assumed to exist. This corresponds to the fact that there is a maximum value for the size of the cloud, considering that the entrainment rate is inversely proportional to the size of the cloud.

Cloud water content TERM00535 is ,

     EQ=00214.
     EQ=00214.

In the case of TERM00536, however, it must be TERM00537. Furthermore, since it is unlikely that a precipitation event will change to cloud water after it rises, TERM00538 must be an increasing function of TERM00539. This leads to a limitation on TERM00540.

The characteristic value of the detrainment air is ,

     EQ=00215.
     EQ=00215.
     EQ=00215.

In the case of TERM00541, it is assumed that there are no clouds. In this case, we assume that the cloud does not exist,

     EQ=00190.

If there is a TERM00542 that satisfies the above condition, the immediate area above it is newly designated as TERM00543,

     EQ=00216.
     EQ=00216.

Seek as .

### Cloud Work Function (CWF)

The cloud work function (CWF), TERM00544 is,

     EQ=00191.

It is,

     EQ=00192.

We should account for the work associated with downdrafting, which we will discuss below, but we ignore it here for the sake of simplicity.

If the cloud has negative buoyancy once it has positive buoyancy, starting from the bottom, then the cloud top should exist at the point where it becomes negative, and we assume that the cloud top we are considering does not exist.

### Cloud Mass Flux at Cloudbase

We assume that the cloud mass flux at the cloud base is determined on a certain time scale (TERM00545) such that the cloud action causes the cloud work function to approach zero.

In order to estimate this, we first calculate the time variation of the mean field in the unit cloud mass flux TERM00546.

     EQ=00217.
     EQ=00217.

With this,

     EQ=00218.
     EQ=00218.

and the cloud work function calculated from (235) using TERM00547 and TERM00547 is defined as TERM00548.

So..,

     EQ=00193.

The results of this calculation are as follows. Although the vertical cloud structures corresponding to TERM00550 and TERM00550 should have been re-calculated in order to obtain TERM00549, the same cloud structures were used in the present study.

### Cloud Mass Flux, Precipitation

The cloud mass flux of the sum of clouds at each cloud-top altitude, TERM00551, is

     EQ=00194.

Also, precipitation flux TERM00552 is

     EQ=00195.

### Time variation of the average field

The time variation of the mean field due to the compensated downward motion and detrainment is calculated as follows.

     EQ=00219.
     EQ=00219.

However, it is TERM00553.

### Evaporation and downdrafting of precipitation

The precipitation falls through the unsaturated atmosphere, while some of it evaporates. Some of it also forms a downdraft.

Evaporation Rate TERM00554 is ,

     EQ=00196.

However, TERM00555 is the saturation specific humidity corresponding to the wet bulb temperature,

     EQ=00197.

TERM00556 and TERM00556 are parameters of microphysics. TERM00557 is the density of precipitation particles and TERM00558 is the terminal velocity of precipitation,

     EQ=00198.

The current standard values are TERM00559, TERM00560 and TERM00561 m/s.

For downdrafting, we make the following assumptions.

 - If TERM00563 is set at the top of the region where TERM00562 decreases monotonically with height above the cloud base, then the downdraft occurs in the region of TERM00564.

 - A certain percentage of the precipitation evaporation that occurs at each altitude is used to form a downdraft. The air in the surrounding area, which has just become saturated by the evaporation of precipitation, is drawn into the downdraft (entrainment).

 - In TERM00565, detraining occurs and the mass flux decreases linearly.

That is, in TERM00566, the mass flux TERM00567, TERM00568, and TERM00568 of the downdrafted air mass follow the following equation. Note that the wet static energy is conserved during evaporation, and the specific humidity when saturated by evaporation is TERM00569.

     EQ=00199.

     EQ=00220.
     EQ=00220.

In the above equation, TERM00570 is the part of the evaporation that is captured in the downdraft, and TERM00571 evaporates directly into the mean field. It is assumed that the mass flux of the downdraft (TERM00572) does not exceed the total mass flux of the cloud base (TERM00573) by a factor of TERM00574. The current standard values are TERM00575 and TERM00575.

### cloud water and cloud cover

Assuming that the grid-averaged cloud cover used for radiation (TERM00576) is defined as the ratio of the strong upward area of cumulus clouds including the cloud cover (TERM00577) to TERM00578,

     EQ=00200.

The mass flux (TERM00579) is determined by using this TERM00580 and the upstream vertical velocity (TERM00581)

     EQ=00201.

So, in the end,

     EQ=00202.

The cloud cover used in the estimation of radiation, TERM00582, is more reasonable than TERM00583, considering that the actual distribution of upwelling and cloud water has a horizontal extent. In this section, we will briefly consider the following,

     EQ=00203.

The current standard values are TERM00584 and TERM00585. The current standard values are TERM00584 and TERM00585.