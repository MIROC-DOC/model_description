## Gravitational wave resistance

### Gravitational Wave Resistance Scheme Overview

The gravitational wave resistance scheme is,
Excited by sub-grid scale terrain
The upward momentum flux of the gravitational wave is represented,
The horizontal wind deceleration associated with its convergence is calculated.
The main input data are: east-west wind TERM00000, north-south wind TERM00001, temperature TERM 00002, and is,
The output data is the time rate of change for the east-west and north-south winds,
TERM00003,TERM00003, is.

The outline of the calculation procedure is as follows.

1. the momentum flux at the ground surface.
 Dispersion of surface altitude,
 The horizontal wind speed at the lowest level, stratification stability, etc.

2. consider the upward propagation of gravitational waves with momentum fluxes.
 Momentum fluxes are determined from the critical fluid number
 If the critical flux is exceeded,
 Suppose a breaking wave occurs and the flux is at its critical value.

3. according to the convergence of the momentum flux at each layer.
 Calculate the time variation of the horizontal wind.

### Relationship between local fluid number and momentum flux

The gravitational waves of surface origin
Given the vertical flux of horizontal momentum,
Fluxes at a certain altitude TERM00004 and
Local Fluid Number TERM00005 and ,

> EQ=00000.
> <span id="p-grav:tau-fl" label="p-grav :tau-fl">\\fl.com[p-grav:tau-fl]</span>

The relationship between the two is valid.
Here, TERM00006 is
Brandt Vaisala Frequency,
TERM00007 is the density of the atmosphere,
TERM00008 corresponds to the wind speed and TERM00009 corresponds to the horizontal scale of the ripples on the ground surface
It is a proportional constant .
Now..,

> EQ=00001.
> <span id="p-grav:fl-tau" label="p-grav :fl-tau">fl-tau\[p-grav:fl-tau]</span>

Local Fluid Number TERM00010 is ,
Assume that a certain value, the critical fluid number TERM00011, cannot be exceeded.
Calculated from ([£l;p-grav:tau-fl\]](#p-grav:tau-fl) used as an example of
If the local fluid number exceeds the critical fluid number TERM00012
The gravitational waves are supersaturated,
Up to the momentum flux corresponding to the critical fluid number
Flux decreases.

### Momentum fluxes at the surface.

due to gravitational waves excited at the earth's surface.
The magnitude of the vertical flux of horizontal momentum TERM00013 is ,
except for the local fluid number at the surface
TERM00014.
Substitute into ([p-grav:fl-tau\]](#p-grav:fl-tau) By ,

> EQ=00002.

It is estimated that .
Here,
The TERM00015 has a surface wind speed of ,
TERM00016 and TERM00016 are the two most common types of data in the atmosphere near the earth's surface.
It is stability and density.
TERM00017 is an indicator of the sub-grid surface elevation change,
Assume that the standard deviation of the surface elevation is equal to TERM00018.

Here, the local fluid number at the surface
If TERM00019 is the critical fluid number
When you exceed the TERM00020,
Momentum fluxes are defined by TERM00021 ([p-grav[p-grav:fl-tau\]](#p- grav:fl-tau))) to the value substituted for
Let's say it can be contained.
Namely,

> EQ=00003.

### Momentum fluxes in the upper levels.

The momentum flux at level TERM00022 is
Suppose we are required to.
TERM00024, when no saturation occurs
Equal to TERM00025.
This momentum flux, TERM00026, is ,
Momentum fluxes calculated from the critical fluid number at the TERM00027 level
In the case of a wave breaking event that exceeds
The momentum flux decreases to the flux corresponding to the criticality.

> EQ=00004.

However, the TERM00029,
. of the wind velocity vector at each layer,
It is the magnitude of the projective component of the lowest level with respect to the direction of the horizontal wind,

> EQ=00005.

### The magnitude of the time variation of horizontal wind due to momentum convergence.

The temporal rate of change of the projective component of the horizontal wind, TERM00030, is

> EQ=00006.

as determined by i.e. ,

> EQ=00007.

With this ,
The rate of change of the east-west and north-south winds over time is calculated as follows.

> EQ=00008.
> EQ=00008.

### Other Notes.

1. when the wind speed at the lowest level is small (TERM00031) and
 In the case of small undulations in the earth's surface (TERM00032),
 Assuming no gravitational waves are excited at the earth's surface.
