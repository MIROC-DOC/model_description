## Gravitational wave resistance

### Gravitational Wave Resistance Scheme Overview

The gravitational wave resistance scheme represents the upward momentum flux of the gravitational waves induced by sub-grid scale topography and calculates the horizontal wind deceleration associated with its convergence. The main input data are east-west wind (TERM01164), north-south wind (TERM01165), and temperature (TERM01166), and the output data are the rates of temporal variation of east-west wind and north-south wind, TERM01167 and TERM01167.

The outline of the calculation procedure is as follows.

The momentum flux at the ground surface is calculated from the dispersion of surface height, the horizontal wind speed at the lowest level, and the stratification stability.

We consider the upward propagation of gravitational waves with momentum fluxes. If the momentum flux exceeds the critical fluid number, the momentum flux is determined by the critical fluid number, then breaking waves occur and the flux becomes the critical value of the momentum flux.

3. compute the time evolution of the horizontal wind as the momentum flux converges in each layer.

### Relationship between local fluid number and momentum flux

Considering the vertical flux of horizontal momentum due to surface-derived gravitational waves, the difference between the flux (TERM01168) and the local fluid number (TERM01169) at a certain altitude is

     EQ=00490.

This relationship holds for the following cases where TERM01170 is the Brant-Visala frequency, TERM01171 is the density of the atmosphere, TERM01172 is the wind speed, and TERM01173 is the proportional constant corresponding to the horizontal scale of the rippling at the surface. From now on,

     EQ=00491.

The local fluid number (TERM01174) cannot exceed the critical fluid number (TERM01175) at a certain value. If the local fluid number calculated from (589) exceeds the critical fluid number TERM01176, the gravitational wave becomes supersaturated and the flux decreases to the momentum flux corresponding to the critical fluid number.

### Momentum fluxes at the surface.

The magnitude of the vertical flux of horizontal momentum due to gravitational waves excited at the earth's surface, TERM01177, is calculated by substituting the local fluid number TERM01178 into (590),

     EQ=00492.

where TERM01179 is the surface wind speed, TERM01180 and TERM01180 are estimated to be the stability and density of the atmosphere near the earth's surface, respectively. where TERM01179 is the surface wind speed, and TERM01180 and TERM01180 are the stability and density of the atmosphere near the earth's surface, respectively. TERM01181 is an indicator of the change in the surface height of the sub-grid and is assumed to be equal to the standard deviation of the surface height (TERM01182).

Here, when the local fluid number (TERM01183) exceeds the critical fluid number (TERM01184), the momentum flux is suppressed to the value obtained by substituting (590) for TERM01185. In other words,

     EQ=00493.

### Momentum fluxes in the upper levels.

Suppose that the momentum flux TERM01187 is required for level TERM01186. When no saturation occurs, TERM01188 is equal to TERM01189. If the momentum flux (TERM01190) exceeds the momentum flux calculated from the critical fluid number at the TERM01191 level, wave breaking occurs in the TERM01192 layer and the momentum flux decreases to the critical flux.

     EQ=00494.

Note that TERM01193 is the magnitude of the projective component of the wind speed vectors for each layer relative to the direction of the lowest level of the horizontal wind,

     EQ=00495.

### The magnitude of the time variation of horizontal wind due to momentum convergence.

The temporal rate of change of the projective component of the horizontal wind, TERM01194, is ,

     EQ=00496.

as determined by i.e. ,

     EQ=00497.

Using this, the temporal rates of change for the east-west and north-south winds are calculated as follows

     EQ=00498.
     EQ=00498.

### Other Notes.

1. it is assumed that no gravitational waves are excited at the ground surface when the wind speed is small (TERM01195) and when the undulations at the surface are small (TERM01196).