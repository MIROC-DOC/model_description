## Solving the diffuse balance equation for atmospheric and surface systems

### Basic Solutions.

Radiative, vertical diffusion, ground boundary layer and surface processes are
Some terms are treated as implicit in the
Compute the time-varying term and do time integration at the end.
As a time-varying term for the vector quantity <span>q</span>,
The term TERM00000 for the Euler method and the term TERM00001 for the implicit method are considered separately.

     EQ=00000.

It is difficult to solve this in the general case, but,
It can be solved by linearizing TERM00002 in an approximate manner.

     EQ=00001.

using the matrix TERM00003 as
Here,

     EQ=00002.

It is.
So..,
TERM00004
And then you can write,

     EQ=00003.

It is easy to solve in principle by matrix operations.

### Fundamental Equations.

Radiation, vertical diffusion, ground boundary layer and surface processes
The equations are basically expressed as follows.

     EQ=00051.
     EQ=00051.
     EQ=00051.
     EQ=00051.
     EQ=00051.

where TERM00005 and TERM00005 are
By vertical diffusion, TERM00006 and TERM00006, respectively
is the vertical upward flux density of
Also, the TERM00007 is a radiant
It is a vertical upward energy flux density.

The atmosphere is discretized in the TERM00008 coordinate system.
Wind speed, temperature, etc. are defined in layer TERM00009.
The flux is defined by the layer boundary TERM00010.
TERM00011 increases from lower to higher levels.
Also, TERM00012,
This is the TERM00013.
TERM00014 The coordinates are only available when we consider a one-dimensional vertical process,
It can be considered to be the same as the TERM00016 coordinates except for the difference in the constant (TERM00015) times.
Here,

     EQ=00004.

     EQ=00005.

And write .

### implicit time difference

For terms that can be linearized, such as the vertical diffusion term, we use the implicit method.
Diffusion coefficients and other factors also depend on the forecast variables,
The coefficients are only calculated first, not iteratively.
However, the treatment of the time step is devised to improve the stability (see below).

For example, the discretized equation of TERM00017 ([\[u-eq.orig]](#u-eq.orig)) is

     EQ=00006.

Here, TERM00018 is a time step.
Since TERM00019 etc. is a function of TERM00020, its dependency is linearized and the

     EQ=00007.

Thus, if you put TERM00021,

     EQ=00008.

Namely,

     EQ=00009.

It can be written in the following matrix form

     EQ=00010.

     EQ=00011.

This can be solved by LU decomposition or some other method.
Normally, TERM00022 is easy to solve since it is a triple diagonal.
After solving the problem, (13) is used to compute
We calculate the consistent flux to this method.
The same is true for TERM00023.

### implicit time difference coupling

Temperature, specific humidity, and ground temperature are not as simple as those in the previous section.

     EQ=00052.
     EQ=00052.

     EQ=00012.

     EQ=00013.

Here, TERM00024 and TERM00025 in the above equations are
Note that I took this from TERM00026, TERM00027. because,
This is because the flux at the surface is as follows

     EQ=00014.

     EQ=00015.

     EQ=00016.

If the surface skin temperature is set to TERM00030,
TERM00031, TERM00032 (saturated specific humidity), TERM00033.
They all depend on TERM00034.
Also, in TERM00035, all values in TERM00036 depend on TERM00037.

Similarly to (17), using the matrices TERM00038 and TERM00038
(18), (19), and (20) are rewritten as,
In case of TERM00039 (for TERM00040,TERM00040) or TERM00041 (for TERM00042),

     EQ=00053.
     EQ=00053.

     EQ=00017.

     EQ=00018.

However,

     EQ=00019.

     EQ=00020.

     EQ=00021.

In TERM00043 (for TERM00044 and TERM00044) or TERM00045 (for TERM00046),

     EQ=00054.
     EQ=00054.
     EQ=00054.

     EQ=00022.

     EQ=00055.
     EQ=00055.
     EQ=00055.

However,

     EQ=00023.

     EQ=00024.

     EQ=00025.

However, (32) is a condition of surface balance

     EQ=00026.

as the case of TERM00047 in the soil temperature equation,
Note that it is not included in the table of (20).

These,
(24), (25), (26),
(30), (31), (32)
for the TERM00048 unknowns,
There are equations of equality that can be solved.
In practice, the LU decomposition can be used to solve the problem.

Once you're untied,
(13) as well as ,
Consistent flux should be sought.

### Solving the Coupling Formula for Time Difference

(30), etc., can be written as follows.

     EQ=00027.

Where, TERM00049,TERM00049
The term in Section 3.1 is a term associated with surface flux,
The others are terms associated with vertical diffusion.
Here, if we reverse the top and bottom and represent it as a matrix, we get the following.

     EQ=00028.

For the sake of brevity, we shall now refer to this document as TERM00050. For the sake of notation simplicity, we will now refer to it as TERM00050.
You can't lose the.

     EQ=00029.

Here,
The expression for TERM00051,TERM00051,
(This corresponds to the case where flux replacement at the surface is not considered.)
by LU decomposition.

     EQ=00030.

LU. Take it apart,

     EQ=00031.

Now..,

     EQ=00032.

for TERM00052 (which can be easily solved by starting from TERM00053),
And then..,

     EQ=00033.

for TERM00054, starting from TERM00055 and solving in sequence.

For TERM00056 and TERM00056, the LU decomposition is

     EQ=00034.

Now..,

     EQ=00035.

However, comparing this with (42), we can see the following relationship.

     EQ=00036.

With this,

     EQ=00037.

The result is That is, ,

     EQ=00038.

Here, TERM00057 and TERM00058 are,
Equation (40) with TERM00059,
In other words, without considering the surface flux term
Note that this can be obtained by performing LU decomposition.
The physical meaning of these terms is ,
During the flux exchange process with the ground surface,
The entire atmosphere has a heat capacity of TERM00060,
Top: Flux TERM00061
Indicates that it can be regarded as one layer to be supplied.

(24) and (30),
(25) and (31),
(26) and (32), respectively.
(48), which yields the equation corresponding to

     EQ=00039.

     EQ=00040.

     EQ=00041.

Therefore, if we concatenate the three equations above, we get
We can solve for the unknown variables TERM00062 and TERM00062.
If we can solve these problems, we can then
(47) can be solved with TERM00063 and TERM00063 in sequence.
Afterwards, the consistuous flux is applied to the obtained temperature

     EQ=00056.
     EQ=00056.

Calculate as.
We show the case where TERM00064 is a general matrix,
It is even simpler since it is actually a triple diagonal matrix.

During the program,
For atmospheric parts in `MODULE:[VFTND1(pimtx.F)]`,
MODULE:[GNDHT1(pggnd.F)]` for the underground part, the first half of the LU decomposition method.
(where the TERM00065 is obtained),
In `MODULE:[SLVSFC(pgslv.F)]`, solve the equation of TERM00066,
Seeking TERM00067,TERM00067.
Then, in `MODULE:[GNDHT2(pggnd.F)]`
The second half of the LU decomposition method is performed and the rate of change of temperature in the ground is solved,
Correct the fluxes so that the balance is matched.
Also, in `MODULE:[VFTND2(pimtx.F)]`, for the atmosphere
Solving the rate of temperature change,
Fluxes are corrected with `MODULE:[FLXCOR(pimtx.F)]`.

### Combined expression for time difference

The coupling formula for finding TERM00068, TERM00068 is,
Solve three times under different conditions as follows.

Solve for surface wetness TERM00069 as 1. Surface temperature is a variable.

2. the surface wetness obtained by `MODULE:[GNDBET]`.
 Surface temperature is a variable .

3. the surface wetness obtained by `MODULE:[GNDBET]`.
 In case of snowmelt, the surface temperature is fixed at the freezing point.

The first calculation is performed to estimate the possible evaporation rate, TERM00070.
(When the surface wetness is small, the energy balance of the model indicates that
Using the obtained TERM00071, the possible evaporation rate can be calculated by
TERM00072
diagnosed as, would result in unrealistically large values).
Possible evaporation rate is ,

     EQ=00057.

That would be.
The subscript TERM00073 means after correction,
This is a consistent flux to the obtained temperature etc.

In the second and subsequent calculations ,

1. to the amount of possible evaporation found in the first calculation
 Surface wetness (evaporation efficiency) TERM00074
 Multiply the value multiplied by the amount of evaporation (TERM00075).

         EQ=00042.

2. evaporation quantity TERM00076 is

         EQ=00043.

 As required by ,
 Once again, rebalancing the energy.

Two methods of calculating the amount of evaporation can be used
(The standard uses the method in 1.).
The third calculation is performed during snow and ice melt and sea ice formation in the mixed layer ocean.
This is done in order to fix the surface temperature at the freezing point, for example, to unbalance the energy.
In this case, the amount of energy used for the phase change of water, such as snowmelt, is diagnostically determined,
It will be used later to calculate the amount of snow melt, etc.

The concrete form of the coupling formula is as follows.

     EQ=00058.
     EQ=00058.

Here, TERM00078, TERM00078 and TERM00079, TERM00079 are,
The components of the matrices and vectors obtained by doing the first half of the LU decomposition method.
When the ground surface is covered with snow or ice, instead of the latent heat TERM00080
Using the Latent Heat of Sublimation TERM00081. TERM00082 is the latent heat of melting of water.
However, in the second calculation,
If the first method is used as an estimate of evaporation, we get the following.

     EQ=00059.
     EQ=00059.

In the third calculation, the concatenation equation for a fixed surface temperature is

     EQ=00060.
     EQ=00060.

where TERM00083 is the rate of change to the temperature to be fixed,

     EQ=00044.

TERM00084 is 273.15K for snow and ice melting,
In the case of sea ice production it is 271.15K.
If the second method of evaporation calculation is used, then
Similarly, instead of TERM00085, use TERM00086,
Calculate the differential term of TERM00087 as 0.
In this case,

     EQ=00061.
     EQ=00061.

TERM00088, calculated by the Surface Energy Balance,
It is the amount of energy used for the phase change of water.

### implicit Treatment of Time Steps in Time Differences

Although the implicit method is used for the time difference of the vertical diffusion term,
In general, the diffusion coefficients are nonlinear, and we explicitly evaluate these coefficients
This can cause problems of numerical instability.
To improve stability, Kalnay and Kanamitsu (19?) following the
I'm working on how to handle the time steps.

For simplicity, we will take the following ordinary differential equations as an example.

     EQ=00045.

The coefficient TERM00089 represents the nonlinearity.
If we evaluate only the coefficients explicitly and make them implicitly different, we get the following equation.

     EQ=00046.

However, consider the value of TERM00090 two steps ahead, TERM00091,

     EQ=00047.

     EQ=00048.

.
In general, it is better to use (64), (65)
(63), which is known to have better stability than (63).

(64), (65) to find the rate of change over time
Rewriting it into a form yields the following.

     EQ=00049.

     EQ=00050.

That is, the time step in determining the rate of change of the rate of change of time includes the following,
Using twice the time integration step.