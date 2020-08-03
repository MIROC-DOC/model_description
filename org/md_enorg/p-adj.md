## Drying convection regulation

### Overview of Drying Convective Regulation

Drying convection control ,
Convective instability in the stratum between two successive levels,
In other words, if the temperature decay rate is greater than the dry adiabatic decay rate
The temperature reduction rate is adjusted to the dry adiabatic reduction rate. Water vapor and other substances are mixed in at this time.
The main input data are temperature TERM00000 and specific humidity TERM00001,
The output data is the adjusted air temperature TERM00002 and specific humidity TERM00003.

Essentially, if vertical diffusion is efficient, then
The vertical convective instability should be basically removed.
However, it may be in short supply in the stratosphere,
A convection adjustment has been added to stabilize the calculation.

### Drying convection regulation procedures.

The conditions for convective instability in the layers TERM00004 and TERM00004 are

     EQ=00000.

Namely,

     EQ=00001.

is a condition.

When this is satisfied ,

     EQ=00003.
     EQ=00003.

to compensate for the temperature.
Furthermore,

     EQ=00002.

to average the values of specific humidity etc. in the two layers.

When you do this,
The layers above and below it may become unstable. That's why,
Repeating this operation from the lower level to the upper level.
Repeat until there is no more layer of convective instability.
However, considering the calculation error and so on,
As a condition of (2) ,
It is considered to have converged if S is less than or equal to some small finite value that is not zero.

Currently, the standard adjustment is between the second and third layer from the bottom and above.