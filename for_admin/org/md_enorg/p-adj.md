## Drying convection regulation

### Overview of Drying Convective Regulation

The dry convective adjustment is used to adjust the temperature decrement to the dry adiabatic decay rate when the stratification is unstable between two successive levels, i.e., the temperature decrement is greater than the dry adiabatic decay rate. In this case, water vapor and other substances are mixed in. The main input data are the temperature (TERM01197) and specific humidity (TERM01198) and the output data are the adjusted temperature (TERM01199) and specific humidity (TERM01200).

If the vertical diffusion is efficient, it should essentially eliminate vertical convective instability. However, since this may be insufficient in the stratosphere and so on, convective adjustment is included to stabilize the calculations.

### Drying convection regulation procedures.

The conditions for convective instability in layers TERM01201 and TERM01201 are

     EQ=00499.

Namely,

     EQ=00500.

is a condition.

When this is satisfied ,

     EQ=00502.
     EQ=00502.

The temperature is compensated by Additionally,

     EQ=00501.

to average the values of specific humidity etc. in the two layers.

Such a procedure may cause instability in the layers above and below it. Therefore, this procedure is repeated from the lower to the upper layers until there are no more convection unstable layers. However, considering the computational errors, this operation is considered to have converged when S is less than a small finite number of non-zero values, as a condition of (600).

Currently, the standard adjustment is between the second and third layer from the bottom and above.