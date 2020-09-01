## Drying convection regulation

### Overview of Drying Convective Regulation

The dry convective adjustment is used to adjust the temperature decrement to the dry adiabatic decay rate when the stratification is unstable between two successive levels, i.e., the temperature decrement is greater than the dry adiabatic decay rate. In this case, water vapor and other substances are mixed in. The main input data are the temperature ($T$) and specific humidity ($q$) and the output data are the adjusted temperature ($T$) and specific humidity ($q$).

If the vertical diffusion is efficient, it should essentially eliminate vertical convective instability. However, since this may be insufficient in the stratosphere and so on, convective adjustment is included to stabilize the calculations.

### Drying convection regulation procedures.

The conditions for convective instability in layers $(k-1,k)$ are

$$
\frac{T_{k-1} - T_{k}}{p_{k-1} - p_{k}} 
  > \frac{R}{C_p} \bar{T_{k-1/2}}
  = \frac{R}{C_p}
    \frac{\Delta p_{k-1} T_{k-1} + \Delta p_{k} T_{k}}
         {\Delta p_{k-1} + \Delta p_{k}} 
$$


Namely,

$$
 S = T_{k-1} - T_{k}
     - \frac{R}{C_p} 
        \frac{\Delta p_{k-1} T_{k-1} + \Delta p_{k} T_{k}}
         {\Delta p_{k-1} + \Delta p_{k}} 
       (p_{k-1} - p_{k})
   > 0 
$$


is a condition.

When this is satisfied ,

$$
T_{k-1}  \leftarrow  \frac{\Delta p_{k}}{\Delta p_{k-1} + \Delta p_{k}} S \\
T_{k}  \leftarrow  \frac{\Delta p_{k-1}}{\Delta p_{k-1} + \Delta p_{k}} S 
$$



The temperature is compensated by Additionally,

$$
q_{k-1}, q_{k} \leftarrow
     \frac{\Delta p_{k-1} q_{k-1} + \Delta p_{k} q_{k}}
          {\Delta p_{k-1} + \Delta p_{k}} 
$$


to average the values of specific humidity etc. in the two layers.

Such a procedure may cause instability in the layers above and below it. Therefore, this procedure is repeated from the lower to the upper layers until there are no more convection unstable layers. However, considering the computational errors, this operation is considered to have converged when S is less than a small finite number of non-zero values, as a condition of (600).

Currently, the standard adjustment is between the second and third layer from the bottom and above.
