
## Configuration of model grid

The atmospheric and oceanic models of MIROC are independent and run on different computational nodes.
The node where the atmospheric model is executed is called the atmospheric node, and the node where the ocean model is executed is called the ocean node.
In the atmospheric node, the land surface model, sea surface model, and river model are executed as sub-models. 
Information exchange between the atmosphere and the oceans is performed through the sea surface model in the atmosphere node.
Information such as sea surface temperature and sea ice concentration of the ocean model in the ocean node is converted to the grid of the sea surface model so that it can be treated as a boundary condition of the model in the atmosphere node.
On the other hand, the heat, freshwater, and momentum fluxes calculated on the grid of the sea surface model in the atmospheric node are converted to the grid of the ocean model and sent to the ocean node.
These series of data communication and conversion are done by the exchanger.
The flux coupler stores data such as boundary conditions, heat and freshwater fluxes calculated by the sea surface model and land surface model, and distributes them to each model as needed.
In general, the flux coupler also includes the function of the exchanger, but this document describes it separately.

## Horizontal grid of model

The horizontal grid of MIROC is defined as the atmospheric grid, the land grid, the river grid, and the sea surface grid for each model in the atmospheric node.
The sea surface grid in the atmospheric node is different from the horizontal grid of the ocean model in the ocean node. 
The land surface grid and the sea surface grid are the horizontal grid of the atmospheric model divided equally into north-south and east-west directions.
The number of divisions can be set arbitrarily for each grid.
However, the number of divisions for the sea surface grid must be divisible by the number of divisions for the land surface model.
The river grid can be the same as the atmospheric grid or an equal latitude/longitude interval grid. The horizontal grid of the ocean model uses horizontal general curvilinear Cartesian coordinates, so it is not necessary to use the same coordinate system as the atmospheric model.
The exchange of data between the atmospheric model and the ocean model is performed by using an exchanger, which is prepared in advance with information on the location, number, area, and vector rotation of the ocean grid that overlaps with the sea surface grid of the atmospheric model.

## Definition of land-sea distribution

The land-sea distribution in MIROC is prioritized by the land-sea distribution defined by the ocean model.
While one grid in the ocean model is defined by land or sea only, the land and ocean grids in the atmospheric model are determined in proportion to the land and sea to be consistent with the ocean model's land-sea distribution.

$SA$ : area of the atmospheric grid, $SL _ {ij}$ : area of the land grid, $SO _ {ij}$ : area of the sea surface grid, $FLND^{atm}$, $FLND^{land} _ {ij}$, $FLND^{oc} _ {ij}$ : percentage of land surface is occupied by each grid. Then, following equation is satisfied.

$$ SA*FLND^{atm} = \sum _ {j=1}^{jldiv}\sum _ {i=1}^{ildiv}(SL _ {ij}*FLND^{land} _ {ij}) = \sum _ {j=1}^{jodiv}\sum _ {i=1}^{iodiv}(SO _ {ij}*FLND^{oc } _{ij}) $$

where, (ildiv,jldiv) is the number of east-west and north-south divisions of the land surface grid, and (iodiv,jodiv) is the number of east-west and north-south divisions of the sea surface grid.
In the land surface grid, if even a small amount of land is defined to exist, boundary values such as land cover are required.
