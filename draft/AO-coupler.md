<!--

Coupler
==========

-   Fluxes into atmospheric model
    -   atmosphere/ocean flux
    -   atmosphere/land flux
    -   total flux into atmospheric model
-   land model/river model flux
    -   land/river flux and river model
    -   runoff of land
    -   runin of lake from river
-   Flux into ocean model
    -   boudary condition at sea surface grid
    -   海面グリッドで計算した大気海洋間のフラックスの海洋グリッドへの変換
    -   海洋モデルでのフラックスの再配分
    -   河川から海洋への水の流出
    -   海面グリッドの分割個数と海洋モデルへの解像度
-->

# Miscellaneous

## Coupler
### Fluxes to Atmospheric Models

#### Fluxes between Atmosphere and Ocean

Fluxes from the sea surface to the atmosphere ($FLXO$) are calculated on the sea surface grid of the atmospheric model.

Boundary conditions such as sea surface temperature, sea ice concentration, sea ice thickness, snow depth over sea ice, sea ice internal temperature, and ocean surface current velocity are obtained from the ocean model through an exchanger (sea ice surface temperature is determined from the sea ice internal temperature, sea ice thickness, and atmospheric conditions over the sea ice. The sea ice velocity is not currently used for flux calculations in MIROC).
The atmospheric boundary conditions such as wind speed, temperature, and specific humidity at sea are converted from the atmospheric grid to the sea surface grid using linear or cubic spline completion.
The fluxes from the sea surface are calculated separately for seawater and sea ice, averaged by area weight, and passed to the atmosphere.
When using a sea ice model categorized by sea ice thickness, it may be necessary to calculate fluxes for each sea ice thickness category, but the current model specification calculates fluxes for the average sea ice thickness.
The conversion of fluxes and boundary conditions between the atmosphere and ocean by the exchanger will be described in detail later.

#### Fluxes between Atmospheric land Surface

Fluxes from the land surface to the atmosphere ($FLXL$) are calculated on a land surface grid.
A land surface grid consists of multiple soil covers and lakes.
Freezing and thawing of lakes and snow cover are considered by a vertical 1D ice model (0-layer
model).
If the area of the land surface grid is $SL$, the area occupied by the lake and each soil cover is respectively

$$ SL^{lake}=SL  \times  LKFRC \times FLND $$

$$ SL^{grd}_k = SL \times GRFRC_k \times (1-LKFRC) \times FLND $$

where $LKFRC$ is the percentage of lakes on land, $k$ is the type of soil cover, and $GRFRC_k$ is the percentage of soil cover $k$ on land excluding lakes.
Fluxes from the land surface are calculated separately over each of these soil covers and lakes, averaged by area weight, and passed to the atmosphere.

$$ FLXL = LKFRC \times FLXL^{lake} + (1-LKFRC) \times \sum_{k=1}^{km} (GRFRC_k \times FLXL_k^{grd}) $$

where $FLXL^{lake}$ is the flux at the lake surface, $FLXL_{k}^{grd}$ is the flux at soil cover $k$, and $km$ is the number of soil cover types.



#### Total Flux to the Atmosphere

Since the river is treated without area property in the model, the flux to the atmosphere ($FLXA$) can be obtained as a weighted average of the sea-land distribution of the fluxes on the land grid ($FLXL$) and at the sea grid ($FLXO$) as follows

$$ FLXA = \frac{1}{SA} \times [ \sum _ {j=1}^{jldiv} \sum_{i=1}^{ildiv}(SL _ {ij} \times FLND^{land} _ {ij} \times FLXL_{ij}) \notag\\ + \sum _ {j=1}^{jodiv}\sum _ {i=1}^{iodiv }(SO _ {ij} \times (1-FLND^{oc} _ {ij}) \times FLXO _ {ij})] $$.

where, (ildiv,jldiv) is the number of east-west and north-south divisions of the land surface grid.
Fluxes computed in the atmospheric model, such as precipitation, are also included in $FLXL$ and $FLXO$.
In the case of such fluxes, all the fluxes in the partitioned land and sea surface grids have the same value as the corresponding grid.

### Fluxes between Land Surface Model and River Model

#### Fluxes between Land Surfaces and the River

In the current specification of the model, the fluxes of water between river and land surfaces deal only with the inflow of water from the river to the lake ($RUNIN$), the outflow from the lake to the river ($RUNOFF$), the inflow of water to the land surface at the inland vanishing point ($RUNIN$), and the outflow of water overflowing the soil to the river ($RUNOFF$).
Here, the inland vanishing point indicates the point where the endpoint of the river disappears, such as in deserts.
The water balance in the river model is divided into ice and water.
The ice in the river model corresponds to a pseudo-glacier.
Here, the phase change in the river model is not considered to guarantee the conservation of melting heat.
In addition, the flow rate of a river is defined as the amount of water present in the river grid divided by its area.
Water and ice are transported downstream in the river model according to the river channel network data.
In the river model in MIROC6, the river discharge at the inland vanishing point of the river is scattered over the global ocean to obtain the water balance.

#### Water Runoff from Land Surface

When each soil cover in the land surface grid can no longer hold water or snow and ice, water or ice is passed from each soil model to the river model through the coupler.

$$ RUNOFF^{grd}_{all} =
    (1-LKFRC) \times \sum_{k=1}^{km}(GFLRC_{k} \times RUNOFF^{grd}_{k}) $$

The details of the runoff from each soil cover can be found in the documentation of the land surface model MATSIRO.
In the lake model, when the lake level or snow/ice thickness ($H$) exceeds a constant value ($H_c$), the water flows out to the river at a time constant $\tau_h$

$$ RUNOFF^{lake} = LKFRC \times \frac{(H-H_c)}{\tau_h},~~~~~~ (H>H_c) $$

$$ RUNOFF^{lake} = 0,~~~~~~~~~~ (H<H_c) $$

The average runoff from the land surface is as follows.

$$ RUNOFF^{land}_{all} = RUNOFF^{lake} + RUNOFF^{grd}_{all} $$


When considering the average runoff volume of the land surface grid, it is necessary to multiply the above equation by the percentage of land surface $FLND$.
In the river model, $RUNOFF^{land}_{all}$ is converted to the river grid with the weight of sea-land distribution, and the runoff amount $RUNOFF^{riv}$ is used for calculation.


#### Runin of Water from a River to a Lake

When a lake exists in the middle of a river channel, water flows into the lake according to the river flow rate.
In order to calculate the amount of water flowing into the lake, the river flow $GDRIV$ in the river grid is converted to the river flow $GDRIVL$ in the land surface grid through the coupler.
Here, $GDRIVL$ is the amount normalized by the area of the land surface grid.
In the land surface grid, the river inflow to the lake, $RUNINN$, is defined by the river flow ($GDRIVL$) and the time constant $\tau$ as follows

$$ RUNINN^{lake}=GDRIVL/\tau $$.

Since the current specification only considers inflow from rivers to lakes, except at the inland vanishing point, the average inflow at the land surface is

$$ RUNINN^{land}=RUNINN^{lake} \times LKFRC $$.

When there are multiple river grids corresponding to a land surface grid, if the river water inflow to the land surface averaged over the land surface grid is returned to the river grid using only the area weights as in $RUNOFF$, it is possible that more water will flow out of the river than exists in the river grid.
Therefore, we convert the ratio of discharge to river flow from the land surface grid to the river grid, and estimate the river discharge (inflow to the land surface) in each river grid.
The runoff ratio of the river flow to the land surface grid is

$$ RINN^{land}=RUNINN^{land}/GDRIVL $$.

If the discharge rate converted to the river grid is $RINN^{riv}$, the discharge (inflow to the land surface) in the river grid is

$$ RUNINN^{riv}=RINN^{riv} \times GDRIV $$.

### Fluxes to the Ocean Model

#### Boundary Conditions for the Ocean on a Sea Level Grid

As mentioned above, the fluxes between the atmosphere and the ocean are calculated on the sea level grid.
In this section, we describe the conversion from the ocean model grid to the sea surface grid.
The standard variables to be converted from the ocean model to the atmospheric sea surface grid are sea surface temperature ($SST$), sea ice concentration ($AI$), sea ice thickness ($HI$), snow depth over sea ice ($HSN$), sea ice internal temperature ($TI$), and ocean surface current velocity ($UO,VO$).
In order to clarify which grid we are dealing with in the future, variables in the ocean model grid will be denoted by superscript $OGCM$ and variables in the sea surface grid by superscript $oc$. In addition, the position in the ocean grid is denoted by $LO$ and the position in the sea surface grid by $LC$.
The boundary condition of the ocean in the sea level grid is defined as follows.

$$ SST^{oc}(LC) = \sum_{N=1}^{IJO(LC)}[SST^{OGCM}(IJO2C(LC,N)) \times SOCN(LC,N)]/SOCNG(LC) $$

$$ AI^{oc}(LC) = \sum_{N=1}^{IJO(LC)}[AI^{OGCM}(IJO2C(LC,N)) \times SOCN(LC,N)]/SOCNG(LC) $$

$$ HI^{oc}(LC) = \frac{1}{{SOCNG(LC) \times AI^{oc}(LC)}}\sum_{N=1}^{IJO(LC)}[HI^{OGCM}(IJO2C(LC,N)) \notag\\ \times AI^{OGCM}(IJO2C(LC,N))   \times SOCN(LC,N)] $$

$$ HSN^{oc}(LC) = \frac{1}{{SOCNG(LC) \times AI^{oc}(LC)}}\sum_{N=1}^{IJO(LC)}[HSN^{OGCM}(IJO2C(LC,N)) \notag\\ \times AI^{OGCM}(IJO2C(LC,N)) \times SOCN(LC,N)] $$

$$ TI^{oc}(LC) = \frac{1}{{SOCNG(LC) \times HI^{oc}(LC) \times AI^{oc}(LC)}}  \sum_{N=1}^{IJO(LC)}[TI^{OGCM}(IJO2C(LC,N)) \notag\\ \times HI^{OGCM}(IJO2C(LC,N)) \times AI^{OGCM}(IJO2C(LC,N)) \times SOCN(LC,N)]  $$

$$ UO^{oc}(LC)= RUO(LC) \times  \frac{\sum_{N=1}^{IJO(LC)}[UO^{OGCM}(IJO2C(LC,N)) \times SOCN(LC,N)]}{SOCNG(LC)}  \notag\\ + RVO(LC) \times  \frac{\sum_{N=1}^{IJO(LC)}[VO^{OGCM}(IJO2C(LC,N)) \times SOCN(LC,N)]}{SOCNG(LC)} $$

$$ VO^{oc}(LC)=-RVO(LC) \times  \frac{\sum_{N=1}^{IJO(LC)}[UO^{OGCM}(IJO2C(LC,N)) \times SOCN(LC,N)]}{SOCNG(LC)} \notag\\ + RUO(LC) \times  \frac{\sum_{N=1}^{IJO(LC)}[VO^{OGCM}(IJO2C(LC,N)) \times SOCN(LC,N)]}{SOCNG(LC)} $$

$$ SOCNG(LC)= \sum_{N=1}^{IJO(LC)}SOCN(LC,N) $$

where,
$IJO(LC)$: Number of ocean grids corresponding to the sea level grid ($LC$) in the atmospheric node.

$IJO2C(LC,N)$: Location of the ocean grid corresponding to the sea surface grid in the atmospheric node.

$SOCN(LC,N)$: Area of the ocean grid corresponding to the sea surface grid in the atmospheric node.

$RUO(LC)$: Cosine of the rotation angle of the vector.

$RVO(LC)$: Sine of the rotation angle of the vector

$SOCNG(LC)$: Area of ocean occupied by sea surface grid.

The ratio of land surface to the sea level grid is also defined as follow.

$FLND^{oc}=(1-SOCNG)/SO$

where, $SO$ is the area of sea surface grid.

The variables related to sea ice that are converted to the sea surface grid are calculated as the average of variables categorized by sea ice layer thickness ($AIM,HIM,HSM,TIM$) as follows.

$$ AI^{OGCM} = \sum_{L=1}^{NIC} AIM^{OGCM}(L) $$

$$ HI^{OGCM} = \sum_{L=1}^{NIC} HIM^{OGCM}(L) \times AIM^{OGCM}(L)/AI^{OGCM} $$

$$ HSN^{OGCM} = \sum_{L=1}^{NIC} HSM^{OGCM}(L) \times AIM^{OGCM}(L)/AI^{OGCM} $$

$$ TI^{OGCM} = \sum_{L=1}^{NIC} TIM^{OGCM}(L) \times AIM^{OGCM}(L)/(AI^{OGCM} \times HI^{OGCM}) $$

where, $NIC$ is the number of category of sea ice.


#### Conversion of Air-Sea Fluxes Calculated on the Sea Surface Grid to the Ocean Grid

Fluxes calculated on the sea surface grid are calculated at sea surface and sea ice surface, respectively, and fluxes to the atmosphere are calculated as

$$ FLXO=(1-AI) \times FLUXO+AI \times FLUXI $$

These fluxes are time-integrated by the flux coupler in the atmospheric model with weights for sea surface and sea ice extent, and then converted to the ocean grid by the coupled atmosphere-ocean time step and passed to the ocean model.

$$ FLUXOA^{OGCM}(LO) = ROCN(LO) \notag\\ \times \sum_{N=1}^{IJA(LO)} \frac{FLUXOA^{oc}(IJC2O(LO,N)) \times SATM(LO,N)}{SATMG(LO)} $$

$$ FLUXIA^{OGCM}(LO) = ROCN(LO) \notag\\ \times \sum_{N=1}^{IJA(LO)} \frac{FLUXIA^{oc}(IJC2O(LO,N)) \times SATM(LO,N)}{SATMG(LO)} $$

$$ SATMG(LO)=ROCN(LO) \times \sum_{N=1}^{IJA(LO)} SATM(LO,N) $$

$$ ROCN(LO)=SATMG(LO)/S^{OGCM}(LO) $$

$$ FLUXOA^{oc}=(1-AI^{oc}) \times FLUXO^{oc} $$

$$ FLUXIA^{oc}=AI^{oc} \times FLUXI^{oc} $$

where,
$IJA(LO)$：Number of sea level grids in the atmospheric model corresponding to the ocean grid ($LO$)

$IJC2O(LO,N)$：Location of the sea surface grid of the atmospheric model corresponding to the ocean grid

$SATM(LO,N)$：Area of the sea surface grid of the atmospheric model corresponding to the ocean grid

$SATM(LO,N)=SOCN(LC,L),LC=IJC2O(LO,N),LO=IJO2C(LC,L)$

$S^{OGCM}(LO)$：Area of the ocean grid

The area of the ocean grid and the sum of the areas of the corresponding ocean grids should match, although the coordinate systems of the atmospheric model and the ocean model are different (the surface areas of the earth in the atmospheric model and the ocean model do not match exactly).

When creating the conversion file, the grid of the atmospheric model is divided into small areas, and the area of the corresponding ocean grid is estimated from the sum of these areas, so they do not match exactly.
For this reason, the flux balance between the atmosphere and the ocean is adjusted by multiplying by the ratio ($ROCN$).
The wind stresses to the ocean are also calculated as wind stresses over sea level ($TXO$, $TYO$) and over sea ice ($TXI$, $TYI$), but without multiplying the weights of sea level and sea ice area.

$$ TXO^{OGCM}(LO) =  \notag\\ + RU(LO) \times ROCN(LO) \times \sum_{N=1}^{IJA(LO)} \frac{[TXO^{oc}(IJC2O(LO,N)) \times SATM(LO,N)]}{SATMG(LO)} \notag\\ + RV(LO) \times ROCN(LO) \times \sum_{N=1}^{IJA(LO)}\frac{[TYO^{oc}(IJC2O(LO,N)) \times SATM(LO,N)]}{SATMG(LO)} $$

$$ TYO^{OGCM}(LO)= \notag\\ -RV(LO) \times ROCN(LO) \times \sum_{N=1}^{IJA(LO)} \frac{[TXO^{oc}(IJC2O(LO,N)) \times SATM(LO,N)]}{SATMG(LO)} \notag\\ + RU(LO) \times ROCN(LO) \times \sum_{N=1}^{IJA(LO)}\frac{[TYO^{oc}(IJC2O(LO,N)) \times SATM(LO,N)]}{SATMG(LO)} $$

where,

$RU(LO)$：cosine of the rotation angle of the vector

$RV(LO)$：sine of the rotation angle of the vector


#### Redistribution of Fluxes in the Ocean Model

The fluxes converted to the ocean grid are updated at each time step of the coupling.
Since the coupling time step is longer than the ocean model time step, the sea level/sea ice area ratio in the ocean model is updated to a different value than the one used to calculate the flux.
Therefore, in order to obtain an accurate heat and water balance, the fluxes need to be distributed according to the updated sea surface and sea ice area ratios.
The fluxes $FLUXOA$ and $FLUXIA$ at sea surface and sea ice surface are ocean grid-averaged values.
Fluxes to each sea ice category are currently distributed evenly independent of sea ice thickness.

$$ FLUXIAM(L)=FLUXIA \times AIM(L)$$

$$ FLUXOA=FLUXOA+FLUXIA \times [1.0-\sum_{L=1}^{LMAX}AIM(L)]$$

where, $AIM$ denotes the percentage of area covered by sea ice in the grid (sea ice concentration), $L$ denotes the type of sea ice thickness category, and $LMAX$ denotes the number of thickness categories.
If there is no sea ice surface, all fluxes will be at sea surface.
If sea ice disappears in the middle of the coupling time step, the flux due to sublimation is divided into the heat flux assuming a sea ice surface and the freshwater flux (sea ice loss).
The heat flux is directly reflected in the temperature change of the first layer of ocean.
On the other hand, the freshwater flux due to sublimation is converted into heat flux and freshwater flux and given to the first layer of the ocean, assuming that sea ice is generated by the sublimation.
As for the wind stress, it is not weighted by sea level and sea ice area before the grid transformation, so it is driven by the respective area weights in each sea ice thickness category in the ocean model.
For this reason, momentum is not conserved.

#### Water Runoff from Rivers to the Ocean

At the end of the river model, we calculate the water flowing from the estuary of river to the ocean.
Water arriving at the estuary of the river grid is first converted to the atmospheric sea surface grid and time integrated in a flux coupler.
After that, it is converted to the ocean grid via an exchanger and passed to the ocean model in the same way as the atmospheric precipitation data.
At this point, the temperature of the river water is treated as the same as the sea surface temperature, as is the case with precipitation.
Therefore, strictly speaking, heat is not conserved.
Ice runoff is handled in the same way as snowfall.


#### Number of Divisions in the Sea Surface Grid and Resolution of the Ocean Model

The sea surface grid is created by dividing the latitude and longitude of the atmospheric grid, but if the number of divisions is not sufficient and the ocean model grid has a higher resolution than the atmospheric sea surface grid, the structure of the atmospheric grid size may remain when the flux is converted to the ocean grid through the exchanger. .
In addition, data such as precipitation from the atmosphere is not interpolated when converting from the atmospheric grid to the ocean grid, so the atmospheric grid structure remains in the ocean grid for these fluxes.
When linear interpolation is used instead of cubic spline interpolation when converting to the sea surface grid, the atmospheric grid structure may remain for differential quantities such as wind stress curl.
