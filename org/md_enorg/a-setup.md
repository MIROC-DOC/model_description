## Basic Settings.

Here we present the basic setup of the model.

### Coordinate System.

The coordinate system is basically,
Longitude TERM00134, Latitude TERM00135, Normalized Pressure TERM00136
(TERM00137,TERM00137 is surface pressure.)
and treat each as orthogonal.
However, the vertical coordinate of TERM00138 is used as the vertical coordinate.

Longitude is discretized at equal intervals `MODULE:[ASETL]`.

     EQ=00005.

Latitude is the Gauss latitude TERM00139 described in Mechanics, and `MODULE:[ASETL]`,
Gauss-Legendre derived from the integral formula.
This takes TERM00140 as its argument
J The zero point of the next Legendre polynomial `MODULE:[GAUSS]`.

If J is large, we can approximate

     EQ=00006.

Normally, the grid spacing of longitude and latitude is almost equal to TERM00141.
This is based on the triangular truncation of the spectral method.

Normalized atmospheric pressure (TERM00142) is designed to give a good representation of the vertical structure of the atmosphere,
suitably discretized at unequal intervals `MODULE:[ASETS]`.
As we will discuss later in Mechanics, the value of the layer boundaries
After defining the TERM00143 in TERM00144 ,

     EQ=00007.

Find the TERM00145 representing the layer by
Figure [a-setup:level\]] (#a-setup:level) shows the 20 levels of the standard.

Each forecast variable is all, TERM00146,TERM00146
or defined on the TERM00147,TERM00147 grid.
(The subterranean level, TERM00148, is discussed in the Physical Processes section.)

In the time direction, it is discretized with an equally spaced TERM00149,
The time integration of the forecasting equation is performed.
However, if the stability of the time integration may be compromised
TERM00150 can vary.

### Physical Constants.

The basic physical constants are shown below `MODULE:[APCON]`.

 - TAB00002:0.0
 earth radius

 - TAB00002:0.1
     TERM00151

 - TAB00002:0.2
     m

 - TAB00002:0.3
     6.37 TERM00152

 - TAB00002:1.0
 acceleration of gravity

 - TAB00002:1.1
     TERM00153

 - TAB00002:1.2
     TERM00154

 - TAB00002:1.3
     9.8

 - TAB00002:2.0
 atmospheric pressure specific heat

 - TAB00002:2.1
     TERM00155

 - TAB00002:2.2
     J TERM00156 TERM00157

 - TAB00002:2.3
     1004.6

 - TAB00002:3.0
 Atmospheric gas constant

 - TAB00002:3.1
     TERM00158

 - TAB00002:3.2
     J TERM00159 TERM00160

 - TAB00002:3.3
     287.04

 - TAB00002:4.0
 Latent heat of water evaporation

 - TAB00002:4.1
     TERM00161

 - TAB00002:4.2
     J TERM00162

 - TAB00002:4.3
     2.5 TERM00163

 - TAB00002:5.0
 Water vapor constant pressure specific heat

 - TAB00002:5.1
     TERM00164

 - TAB00002:5.2
     J TERM00165 TERM00166

 - TAB00002:5.3
     1810\bsp.

 - TAB00002:6.0
 Gas constant of water

 - TAB00002:6.1
     TERM00167

 - TAB00002:6.2
     J TERM00168 TERM00169

 - TAB00002:6.3
     461\.

 - TAB00002:7.0
 Density of liquid water

 - TAB00002:7.1
     TERM00170

 - TAB00002:7.2
     J TERM00171 TERM00172

 - TAB00002:7.3
     1000.

 - TAB00002:8.0
     0 in TERM00173.
 saturation vapor

 - TAB00002:8.1
     TERM00174(273K)

 - TAB00002:8.2
     Pa.

 - TAB00002:8.3
     611

 - TAB00002:9.0
     Stefan Bolzman
 constant

 - TAB00002:9.1
     TERM00175

 - TAB00002:9.2
     W TERM00176 TERM00177

 - TAB00002:9.3
     5.67
     TERM00178

 - TAB00002:10.0
     Kárman Constant

 - TAB00002:10.1
     TERM00179

 - TAB00002:10.2

 - TAB00002:10.3
     0.4

 - TAB00002:11.0
 Latent heat of ice melting

 - TAB00002:11.1
     TERM00180

 - TAB00002:11.2
     J TERM00181

 - TAB00002:11.3
     3.4 TERM00182

 - TAB00002:12.0
 Water Freezing Point

 - TAB00002:12.1
     TERM00183

 - TAB00002:12.2
     K

 - TAB00002:12.3
     273.15

 - TAB00002:13.0
 Constant pressure specific heat of water

 - TAB00002:13.1
     TERM00184

 - TAB00002:13.2
     J TERM00185

 - TAB00002:13.3
     4,200\.

 - TAB00002:14.0
 The freezing point of seawater

 - TAB00002:14.1
     TERM00186

 - TAB00002:14.2
     K

 - TAB00002:14.3
     271.35

 - TAB00002:15.0
 Specific heat ratio of ice at constant pressure

 - TAB00002:15.1
     TERM00187

 - TAB00002:15.2

 - TAB00002:15.3
     2397\.

 - TAB00002:16.0
 water vapor molecular weight ratio

 - TAB00002:16.1
     TERM00188

 - TAB00002:16.2

 - TAB00002:16.3
     0.622

 - TAB00002:17.0
 coefficient of provisional temperature

 - TAB00002:17.1
     TERM00189

 - TAB00002:17.2

 - TAB00002:17.3
     0.606

 - TAB00002:18.0
 Ratio of specific heat to gas constant

 - TAB00002:18.1
     TERM00190

 - TAB00002:18.2

 - TAB00002:18.3
     0.286