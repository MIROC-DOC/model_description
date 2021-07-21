## Basic Settings.

Here we present the basic setup of the model.

### Coordinate System.

The coordinate system is basically based on the longitude TERM00134, latitude TERM00135, and normalized atmospheric pressure TERM00136 (TERM00137 and TERM00137 being surface atmospheric pressure), which are treated as orthogonal to each other. However, the vertical coordinates of the underground coordinate system (TERM00138) are used.

Longitude is discretized at equal intervals `MODULE:[ASETL]`.

     EQ=00005.

The latitude is the Gauss latitude TERM00139 described in Mechanics, and it is derived from `MODULE:[ASETL]`, the Gauss-Legendre integral formula. This is the zero point of the Legendre polynomial of order J with TERM00140 as the argument, `MODULE:[GAUSS]`.

If J is large, we can approximate

     EQ=00006.

Usually, the grid spacing of longitude and latitude is taken to be approximately equal to TERM00141. This is based on the triangular truncation of the spectral method.

The normalized atmospheric pressure TERM00142 is discretized appropriately at unequal intervals so as to better represent the vertical structure of the atmosphere `MODULE:[ASETS]`. As described later in Mechanics, the value of the layer boundaries (TERM00143) is defined in TERM00144, and then

     EQ=00007.

to find the TERM00145 that represents the layers by Figure [a-setup:level\]] (#a-setup:level) shows the standard 20 levels of layers used.

Each predictor is entirely defined on a grid of TERM00146,TERM00146 or TERM00147,TERM00147. (The underground level, TERM00148, is described in the section on physical processes.)

In the time direction, the predictive equations are discretized at evenly spaced TERM00149 and time integration is performed. However, if the stability of the time integration may be impaired, the TERM00150 may change.

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
     0 Saturated vapor at 0 TERM00173

 - TAB00002:8.1
     TERM00174(273K)

 - TAB00002:8.2
     Pa.

 - TAB00002:8.3
     611

 - TAB00002:9.0
     Stefan Bolzman Constant

 - TAB00002:9.1
     TERM00175

 - TAB00002:9.2
     W TERM00176 TERM00177

 - TAB00002:9.3
     5.67 TERM00178

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