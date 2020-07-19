## Vertical discretization

According to Arakawa and Suarez (1983),
Discretize the basic equations vertically by differences.
The scheme has the following characteristics.

 - Save the total integrated mass

 - Save the total integrated energy

 - Preserving angular momentum for global integration

 - Conservation of total mass-integrated potential temperature

 - The hydrostatic pressure equation comes down to local (the altitude of the lower level is independent of the temperature of the upper level)

 - Constant in the horizontal direction, for a given temperature distribution,
 The hydrostatic pressure equation becomes accurate and the barometric gradient force becomes zero.

 - Isothermal atmosphere stays isothermal forever

### How to take a level.

Number the layers from bottom to top.
If the physical quantity of TERM00000, TERM00000 is defined at the integer level (layer) I do.
On the other hand, TERM00001 is defined at the half-integer level.
First, the value of TERM00002 at a half-integer level
TERM00003,TERM00003
Define the .
However, level TERM00004 is the lower end (TERM00005),
Level TERM00006 should be the upper end (TERM00007).

Value of TERM00008 in integer level
TERM00009,TERM00009
is obtained from the following equation.

> EQ=00000.
> <span id="Bear definition" label="Bear definition">Are you sure? GumaDinformation.com]</span>

Furthermore,

> EQ=00001.
> <span id="sigma thickness" label="sigma thickness">Are you sure? Bear thickness </span>

.

### Vertical discretization representation.

The discretized representation of each equation is as follows.

1. continuity formula, vertical velocity
     
     > EQ=00002.
     
     > EQ=00003.
     
     > EQ=00004.

2. hydrostatic pressure formula
     
     > EQ=00010. 
     > EQ=00010.
     
     > EQ=00011. 
     > EQ=00011.
     
 Here,
     
     > <span id="Hydrostatic pressure coefficient" label="Hydrostatic pressure coefficient">Drum pressure coefficient Hydraulic Pressure CoefficientPointPoint.com
     > EQ=00012. 
     > EQ=00012.

3. equation of motion
     
     > EQ=00005.
     > <span id="Vorticity After All" label="Vorticity After All">\bout_Vorticity After All </span>.
     
     > EQ=00006.
     
 Here,
     
     > EQ=00013. 
     > EQ=00013.
     
     > EQ=00014. 
     > EQ=00014.
     
  First Kpa\\cleaner\cleaner\cleaner.com
     > EQ=00015. 
     > EQ=00015.
     
     > EQ=00007.

4. thermodynamic equation
     
     > EQ=00016. 
     > EQ=00016. 
     > EQ=00016.
     
 Here,
     
     > EQ=00017. 
     > EQ=00017. 
     > EQ=00017. 
     > EQ=00017. 
     > EQ=00017. 
     > EQ=00017. 
     > EQ=00017.
     
     > EQ=00018. 
     > EQ=00018.
     
     > <span id="Temperature Interpolation Factor" label="Temperature Interpolation Factor">\blaze> <span id="Temperature Interpolation Factor Temperature interpolation coefficient\en.com
     > EQ=00019. 
     > EQ=00019.

5. water vapor formula
     
     > EQ=00008.
  lt;/span>
     
     > EQ=00009.

