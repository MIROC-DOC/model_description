## Drying convection regulation

### Overview of Drying Convective Regulation

Drying convection control ,
Convective instability in the stratum between two successive levels,
In other words, if the temperature decay rate is greater than the dry adiabatic decay rate
The temperature reduction rate is adjusted to the dry adiabatic reduction rate. Water vapor and other substances are mixed in at this time.
The main input data are temperature $T$ and specific humidity $q$,
The output data is the adjusted air temperature $T$ and specific humidity $q$.

Essentially, if vertical diffusion is efficient, then
The vertical convective instability should be basically removed.
However, it may be in short supply in the stratosphere,
A convection adjustment has been added to stabilize the calculation.

### Drying convection regulation procedures.

The conditions for convective instability in the layers $(k-1,k)$ are

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

> <span id="p-adj:cond" label="p-adj:cond" label="p-adj:cond" label="p-adj:cond" label="p-adj:cond" label="p-adj:cond" label="p-adj:cond" label="p-adj:cond"> </span>.

is a condition.

When this is satisfied ,

$$
T_{k-1}  \leftarrow  \frac{\Delta p_{k}}{\Delta p_{k-1} + \Delta p_{k}} S \\
T_{k}  \leftarrow  \frac{\Delta p_{k-1}}{\Delta p_{k-1} + \Delta p_{k}} S 
$$



to compensate for the temperature.
Furthermore,

$$
q_{k-1}, q_{k} \leftarrow
     \frac{\Delta p_{k-1} q_{k-1} + \Delta p_{k} q_{k}}
          {\Delta p_{k-1} + \Delta p_{k}} 
$$


to average the values of specific humidity etc. in the two layers.

When you do this,
The layers above and below it may become unstable. That's why,
Repeating this operation from the lower level to the upper level.
Repeat until there is no more layer of convective instability.
However, considering the calculation error and so on,
(as a condition of [\\p\[p-adj:condo\]](#p-adj:condo)),
It is considered to have converged if S is less than or equal to some small finite value that is not zero.

Currently, the standard adjustment is between the second and third layer from the bottom and above.

