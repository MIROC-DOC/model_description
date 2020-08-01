## Basic Settings.

Here we present the basic setup of the model.

### Coordinate System.

The coordinate system is basically,
Longitude TERM00000, Latitude TERM00001, Normalized Pressure TERM00002
(TERM00003 and TERM00003 are surface pressure.)
and treat each as orthogonal.
However, TERM00004 is used as the vertical coordinates.

Longitude is discretized at equal intervals `MODULE:[ASETL]`.

     EQ=00000.     --- (1)

Latitude is the Gauss latitude TERM00005 described in Mechanics, and `MODULE:[ASETL]`,
Gauss-Legendre derived from the integral formula.
This takes TERM00006 as its argument
J The zero point of the next Legendre polynomial `MODULE:[GAUSS]`.

If J is large, we can approximate

     EQ=00001.    --- (2)

Normally, the grid spacing of longitude and latitude is taken as TERM00007 almost equally.
This is based on the triangular truncation of the spectral method.

Normalized atmospheric pressure (TERM00008) is designed to give a good representation of the vertical structure of the atmosphere,
suitably discretized at unequal intervals `MODULE:[ASETS]`.
As we will discuss later in Mechanics, the value of the layer boundaries
Define the TERM00009 in TERM00010 and then ,

     EQ=00002.     --- (3)

Find the TERM00011 representing the layer by
Figure [a-setup:level\]] (#a-setup:level) shows the 20 levels of the standard.

Each forecast variable is all, TERM00012,TERM00012
or defined on the grid of TERM00013,TERM00013.
(The underground level, TERM00014, is discussed in the Physical Processes section.)

In the time direction, they are discretized at equally spaced TERM00015,
The time integration of the forecasting equation is performed.
However, if the stability of the time integration may be compromised
TERM00016 can change.

### Physical Constants.

The basic physical constants are shown below `MODULE:[APCON]`.

 - TAB00000:0.0
 earth radius

 - TAB00000:0.1
     TERM00017

 - TAB00000:0.2
     m

 - TAB00000:0.3
     6.37 TERM00018

 - TAB00000:1.0
 acceleration of gravity

 - TAB00000:1.1
     TERM00019

 - TAB00000:1.2
     TERM00020

 - TAB00000:1.3
     9.8

 - TAB00000:2.0
 atmospheric pressure specific heat

 - TAB00000:2.1
     TERM00021

 - TAB00000:2.2
     J TERM00022 TERM00023

 - TAB00000:2.3
     1004.6

 - TAB00000:3.0
 Atmospheric gas constant

 - TAB00000:3.1
     TERM00024

 - TAB00000:3.2
     J TERM00025 TERM00026

 - TAB00000:3.3
     287.04

 - TAB00000:4.0
 Latent heat of water evaporation

 - TAB00000:4.1
     TERM00027

 - TAB00000:4.2
     J TERM00028

 - TAB00000:4.3
     2.5 TERM00029

 - TAB00000:5.0
 Water vapor constant pressure specific heat

 - TAB00000:5.1
     TERM00030

 - TAB00000:5.2
     J TERM00031 TERM00032

 - TAB00000:5.3
     1810\bsp.

 - TAB00000:6.0
 Gas constant of water

 - TAB00000:6.1
     TERM00033

 - TAB00000:6.2
     J TERM00034 TERM00035

 - TAB00000:6.3
     461\.

 - TAB00000:7.0
 Density of liquid water

 - TAB00000:7.1
     TERM00036

 - TAB00000:7.2
     J TERM00037 TERM00038

 - TAB00000:7.3
     1000.

 - TAB00000: 8.0
     0 in TERM00039.
 saturation vapor

 - TAB00000:8.1
     TERM00040(273K)

 - TAB00000:8.2
     Pa.

 - TAB00000:8.3
     611

 - TAB00000:9.0
     Stefan Bolzman
 constant

 - TAB00000:9.1
     TERM00041

 - TAB00000:9.2
     W TERM00042 TERM00043

 - TAB00000:9.3
     5.67
     TERM00044

 - TAB00000:10.0
     Kárman Constant

 - TAB00000:10.1
     TERM00045

 - TAB00000:10.2

 - TAB00000:10.3
     0.4

 - TAB00000:11.0
 Latent heat of ice melting

 - TAB00000:11.1
     TERM00046

 - TAB00000:11.2
     J TERM00047

 - TAB00000:11.3
     3.4 TERM00048

 - TAB00000:12.0
 Water Freezing Point

 - TAB00000:12.1
     TERM00049

 - TAB00000:12.2
     K

 - TAB00000:12.3
     273.15

 - TAB00000:13.0
 Constant pressure specific heat of water

 - TAB00000:13.1
     TERM00050

 - TAB00000:13.2
     J TERM00051

 - TAB00000:13.3
     4,200\.

 - TAB00000:14.0
 The freezing point of seawater

 - TAB00000:14.1
     TERM00052

 - TAB00000:14.2
     K

 - TAB00000:14.3
     271.35

 - TAB00000:15.0
 Specific heat ratio of ice at constant pressure

 - TAB00000:15.1
     TERM00053

 - TAB00000:15.2

 - TAB00000:15.3
     2397\.

 - TAB00000:16.0
 water vapor molecular weight ratio

 - TAB00000:16.1
     TERM00054

 - TAB00000:16.2

 - TAB00000:16.3
     0.622

 - TAB00000:17.0
 coefficient of provisional temperature

 - TAB00000:17.1
     TERM00055

 - TAB00000:17.2

 - TAB00000:17.3
     0.606

 - TAB00000:18.0
 Ratio of specific heat to gas constant

 - TAB00000:18.1
     TERM00056

 - TAB00000:18.2

 - TAB00000:18.3
     0.286