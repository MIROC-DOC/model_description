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

| Header0 | Header1 | Header2 | Header3 |
| ------- | ------- | ------- | ------- |
| earth radius | TERM00151 | m | 6.37 TERM00152 |
| acceleration of gravity | TERM00153 | TERM00154 | 9.8 |
| atmospheric pressure specific heat | TERM00155 | J TERM00156 TERM00157 | 1004.6 |
| Atmospheric gas constant | TERM00158 | J TERM00159 TERM00160 | 287.04 |
| Latent heat of water evaporation | TERM00161 | J TERM00162 | 2.5 TERM00163 |
| Water vapor constant pressure specific heat | TERM00164 | J TERM00165 TERM00166 | 1810\bsp. |
| Gas constant of water | TERM00167 | J TERM00168 TERM00169 | 461\. |
| Density of liquid water | TERM00170 | J TERM00171 TERM00172 | 1000. |
| 0 in TERM00173. | TERM00174(273K) | Pa. | 611 |
| Stefan Bolzman | TERM00175 | W TERM00176 TERM00177 | 5.67 |
| Kárman Constant | TERM00179 |  | 0.4 |
| Latent heat of ice melting | TERM00180 | J TERM00181 | 3.4 TERM00182 |
| Water Freezing Point | TERM00183 | K | 273.15 |
| Constant pressure specific heat of water | TERM00184 | J TERM00185 | 4,200\. |
| The freezing point of seawater | TERM00186 | K | 271.35 |
| Specific heat ratio of ice at constant pressure | TERM00187 |  | 2397\. |
| water vapor molecular weight ratio | TERM00188 |  | 0.622 |
| coefficient of provisional temperature | TERM00189 |  | 0.606 |
| Ratio of specific heat to gas constant | TERM00190 |  | 0.286 |
