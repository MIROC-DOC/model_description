# Physics

## Overview of Physical Parameterizations

As a physical process, we can consider the following

- Cumulus convection
- Shallow convection
- Large scale condensation
- Cloud microphysics
- Radiation
- Turbulence
- Surface fluxes
- Gravity wave drag

We compute the time-varying terms $F_x, F_y, Q, M, S$ for the prognostic variables from these processes, and perform time integration.

### Time Integration of Physical Parameterizations

**NOTE: the descriptions in this section are outdated.**

In terms of time integration of predictors, we can classify the physical Parameterizations in the following three orders of execution.

1. Cumulus convection, shallow convection, large-scale condensation, and cloud microphysics

2. Radiation, turbulence and surface fluxes

3. Gravity wave drag

For cumulus convection, shallow convection, large-scale condensation, and cloud microphysics, the values are updated by the usual Euler difference as follows.

$$
  \hat{T}^{t+\Delta t,(1)} = \hat{T}^{t+\Delta t}
                         +  2 \Delta t Q_{CUM}(\hat{T}^{t+\Delta t})
$$


$$
  \hat{T}^{t+\Delta t,(2)} = \hat{T}^{t+\Delta t,(1)}
                         +  2 \Delta t Q_{LSC}(\hat{T}^{t+\Delta t,(1)})
$$


Note that the large-scale condensation scheme is updated by the cumulus convection scheme. In practice, the routines of cumulus convection and large-scale condensation output the heating rates and so on, and the time integration is performed immediately afterwards by `MODULE:[GDINTG]`.

The calculations of the radiative, vertical diffusion, ground boundary layer and surface processes in the following groups are basically performed with these updated values ($\hat{T}^{t+\Delta t,(1)}, \hat{q}^{t+\Delta t,(2)}$, etc.). However, in order to calculate some of the terms as implicit, we calculate the heating rates and so on for all of these terms together, and then perform time integration at the end. In other words, if we write symbolically

$$
  \hat{T}^{t+\Delta t,(3)} = \hat{T}^{t+\Delta t,(2)}
              + 2 \Delta t Q_{RAD,DIF,SFC}
               (\hat{T}^{t+\Delta t,(2)},\hat{T}^{t+\Delta t,(3)})
$$


That would be the gravity wave drag, mass modulation, and dry convection modulation are the same as those for cumulus convection and large-scale condensation.

$$
  \hat{T}^{t+\Delta t,(4)} = \hat{T}^{t+\Delta t,(3)}
              +  2 \Delta t Q_{ADJ}(\hat{T}^{t+\Delta t,(3)})
$$

### Various Physical Quantities

Here are definitions of various physical quantities that can be computed simply from the prognostic variables. Some of them are calculated with `MODULE:[PSETUP]`.

1. Virtual temperature

Virtual Temperature $T_v$ is calculated as follows.

$$
  T_v = T ( 1 + \epsilon_v q - l )
$$


2. Air density

 The air density $\rho$ is calculated as follows.

$$
  \rho = \frac{p}{RT_v}
$$


3. Altitude

The altitude $z$ is evaluated in the same way as the calculation of the geopotential height in the dynamics.

$$
  z = \frac{\Phi}{g}
$$

$$
 \Phi_{1}  =  \Phi_{s} + C_{p} ( \sigma_{1}^{-\kappa} - 1  ) T_{v,1}
$$

$$
 \Phi_k - \Phi_{k-1}
   =  C_{p}
   \left[ \left( \frac{ \sigma_{k-1/2} }{ \sigma_k } \right)^{\kappa}
          - 1 \right] T_{v,k}
       + C_{p}
   \left[ 1-
         \left( \frac{ \sigma_{k-1/2} }{ \sigma_{k-1} } \right)^{\kappa}
              \right] T_{v,k-1}
$$

4. Half-level temperature

Half-level temperature is calculated by performing a linear interpolation on $\ln p$, i.e., $\ln \sigma$.

$$
  T_{k-1/2} = \frac{\ln \sigma_{k-1} - \ln \sigma_{k-1/2}}
                   {\ln \sigma_{k-1} - \ln \sigma_k      } T_k
            + \frac{\ln \sigma_{k-1/2} - \ln \sigma_k}
                   {\ln \sigma_{k-1} - \ln \sigma_k      } T_{k-1}
$$


5. Saturated specific humidity

The saturated specific humidity $q^{*}(T,p)$ is approximated using the saturated vapor pressure $e^{*}(T)$,

$$
q^{*}(T,p) = \frac{\epsilon e^{*}(T)}{p} .
$$

Here, it is $\epsilon=0.622$,

$$
\frac{1}{e^{*}_v} \frac{\partial{e^{*}_v}}{\partial {T}} = \frac{L}{R_v T^2} \tag{p199}
$$

Therefore, if the latent heat of evaporation ($L$) and the gas constant of water vapor ($R_v$) are held constant,

$$
  e^{*}(T) = e^{*}(T=273{K})
                      \exp \left[ \frac{L}{R_v}
                            \left( \frac{1}{273} - \frac{1}{T} \right)
                       \right] ,
$$

where $e^{*}(T=273 \mathrm{[K]}) = 611 \mathrm{[hPa]}$.

From eq.[p199](#p199),

$$
\frac{\partial{q^{*}}}{\partial {T}} = \frac{L}{R_v T^2} q^{*}(T,p) .
$$


It is noted that if the temperature is lower than the freezing point $273.15 \mathrm{[K]}$, the sublimation latent heat $L+L_M$ is used as the latent heat $L$.

6. Dry static energy and moisture static energy

The dry static energy $s$ is defined by

$$
  s = C_p T + g z
$$

The moisture static Energy $h$ is defined by

$$
  h = C_p T + g z + L q
$$
