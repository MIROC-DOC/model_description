## Solving the diffuse balance equation for atmospheric and surface systems

### Basic Solutions.

Radiative, vertical diffusion, ground boundary layer and surface processes are
Some terms are treated as implicit in the
Compute the time-varying term and do time integration at the end.
As a time-varying term for the vector quantity <span>q</span>,
The term TERM00000 for the Euler method and the term TERM00001 for the implicit method are considered separately.

> EQ=00000.

It is difficult to solve this in the general case, but,
It can be solved by linearizing TERM00002 in an approximate manner.

> EQ=00001.

using the matrix TERM00003 as
Here,

> EQ=00002.

It is.
So..,
TERM00004
And then you can write,

> EQ=00003.

It is easy to solve in principle by matrix operations.

### Fundamental Equations.

Radiation, vertical diffusion, ground boundary layer and surface processes
The equations are basically expressed as follows.

> EQ=00051.
> EQ=00051.
> EQ=00051.
> EQ=00051.
> EQ=00051.

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
It can be considered to be the same as TERM00016 coordinates except for the difference in the constant (TERM00015) times.
Here,

> EQ=00004.

> EQ=00005.

And write .

### implicit time difference

For terms that can be linearized, such as the vertical diffusion term, we use the implicit method.
Diffusion coefficients and other factors also depend on the forecast variables,
The coefficients are only calculated first, not iteratively.
However, the treatment of the time step is devised to improve the stability (see below).

For example, the discretized equation of TERM00017 ([\[u-eq.orig]](#u-eq.orig)) is

> EQ=00006.

Here, TERM00018 is a time step.
Since TERM00019 etc. is a function of TERM00020, its dependency is linearized and the

> EQ=00007.
> <span id="u-flux.next" label="u-flux.next" label="u-flux.next">\\\[u-flux.next\]</span>

Thus, if you put TERM00021,

> EQ=00008.

Namely,

> EQ=00009.

It can be written in the following matrix form

> EQ=00010.

> EQ=00011.
> <span id="u-matrix" label="u-matrix">\blazer[u-matrix]</span>

This can be solved by LU decomposition or some other method.
Normally, TERM00022 is easy to solve since it is a triple diagonal.
After solving it, ([[u-flux.next\]](#u-flux.next)), you can use
We calculate the consistent flux to this method.
The same is true for TERM00023.

### implicit time difference coupling

Temperature, specific humidity, and ground temperature are not as simple as those in the previous section.

> EQ=00052.
> <span id="deq-theta" label="deq-theta">\[deq-theta]</span>
> EQ=00052.

> EQ=00012.
> <span id="deq-q" label="deq-q">\blazer[deq-q]</span>

> EQ=00013.
> <span id="deq-g" label="deq-g">\blazer[deq-g]</span>

Here, TERM00024 and TERM00025 in the above equations are
Note that I took this from TERM00026, TERM00027. because,
This is because the flux at the surface is as follows

> EQ=00014.

> EQ=00015.

> EQ=00016.

Where the surface skin temperature is set to TERM00028,
TERM00029, TERM00030 (saturated specific humidity), TERM00031.
They all depend on the TERM00032.
Also, the value of the TERM00033 depends on the TERM00035 for all TERM00034 values.

(as with [\[u-matrix]](#u-matrix)), using the matrices TERM00036,TERM00036
([deq-theta\] (#deq-theta)), ([deq-q\] (#deq-q)), ([deq-g\\] (#deq-g)), and ([deq-g\\] (#deq-g)) are rewritten,
For TERM00037 (for TERM00038 and TERM00038) or TERM00039 (for TERM00040),

> EQ=00053.
> <span id="combo-theta2" label="combo-theta2">\\[combo-theta2\\blazer]</span>
> EQ=00053.

> EQ=00017.
> <span id="combo-q2" label="combo-q2">\blazer[combo-q2]</span>

> EQ=00018.
> <span id="combo-g2" label="combo-g2">\blazer[combo-g2]</span>

However,

> EQ=00019.

> EQ=00020.

> EQ=00021.

In case of TERM00041 (for TERM00042 and TERM00042) or TERM00043 (for TERM00044),

> EQ=00054.
> EQ=00054.
> <span id="comb-theta" label="comb-theta" label="comb-theta">\centric[comb-theta]</span>
> EQ=00054.

> EQ=00022.
> <span id="combo-q" label="combo-q">\\centric\centric\centric\centric\centric\centric\centric\centric\centric\centric\centric\centric\centric\centric\centric\centric\centric\centric\centric\centric\centric\centric\centric\centric\centric\centric\centric\centric\centric\centric\fadabraz</c>.

> EQ=00055.
> EQ=00055.
> <span id="combo-g" label="combo-g">\cleaner[combo-g]</span>
> EQ=00055.

However,

> EQ=00023.

> EQ=00024.

> EQ=00025.

However, ([comb-g]](#comb-g)), the balance condition of the ground surface

> EQ=00026.

as the case of TERM00045 in the soil temperature equation,
(Note that it is not included in the formula of [deq-g](#deq-g)].

These,
([comb-theta2\] (#comb-theta2)), ([comb-q2\] (#comb-q2)), ([comb-g2\] (#comb-g2)),
([comb-theta\](#comb-theta)), ([comb-q](#comb-q)), ([comb-g\\lopen[comb-g\]](#comb-g))
for the TERM00046 unknowns,
There are equations of equality that can be solved.
In practice, the LU decomposition can be used to solve the problem.

Once you're untied,
([u-flux.next]](#u-flux.next)) as well as ,
Consistent flux should be sought.

### Solving the Coupling Formula for Time Difference

([comb-theta]](#comb-theta)), etc., can be written as follows.

> EQ=00027.

Where, TERM00047,TERM00047
The term in Section 3.1 is a term associated with surface flux,
The others are terms associated with vertical diffusion.
Here, if we reverse the top and bottom and represent it as a matrix, we get the following.

> EQ=00028.

For the sake of brevity, we shall now refer to this document as TERM00048. For the sake of notation simplicity, we will now refer to it as TERM00048.
You can't lose the.

> EQ=00029.

Here,
The expression for TERM00049,TERM00049,
(This corresponds to the case where flux replacement at the surface is not considered.)
by LU decomposition.

> EQ=00030.
> <span id="summe-0" label="summe-0">\blazer[summe-0]</span>

LU. Take it apart,

> EQ=00031.

Now..,

> EQ=00032.
> <span id="solve-z" label="solve-z">\blazer[solve-z]</span>

for TERM00050 (which can be easily solved by starting from TERM00051),
And then..,

> EQ=00033.

for TERM00052, starting from TERM00053, and solving in sequence.

For TERM00054 and TERM00054, the LU decomposition is

> EQ=00034.

Now..,

> EQ=00035.

However, comparing this with ([\ltra[solve-z]](#solve-z)), we see the following relationship.

> EQ=00036.

With this,

> EQ=00037.
> <span id="solve-x" label="solve-x">\blazer[solve-x]</span>

The result is That is, ,

> EQ=00038.
> <span id="solve-1" label="solve-1">\blazer[solve-1\blazer]</span>

where, TERM00055 and, TERM00056 are,

In other words, without considering the surface flux term
Note that this can be obtained by performing LU decomposition.
The physical meaning of these terms is ,
During the flux exchange process with the ground surface,
The entire atmosphere has a heat capacity of TERM00058,
Flux (TERM00059) from the top
Indicates that it can be regarded as one layer to be supplied.

([comb-theta2]](#comb-theta2)) and ([comb-theta\]](#comb-theta)),
([combo-q2\](#comb-q2)) and ([combo-q\\\\clean}](#comb-q)),
([comb-g2\](#comb-g2)) and ([comb-g](#comb-g))
(the formula corresponding to [\ltra[solve-1\]](#solve-1)) is obtained and is as follows

> EQ=00039.

> EQ=00040.

> EQ=00041.

Therefore, if we concatenate the three equations above, we get
We can solve for the unknown variables TERM00060,TERM00060.
If we can solve these problems, we can then
([\[solve-x]](#solve-x)) can be solved sequentially as TERM00061,TERM00061.
Afterwards, the consistuous flux is applied to the obtained temperature

> EQ=00056.
> EQ=00056.

Calculate as.
Here, we show the case where TERM00062 is a general matrix,
It is even simpler since it is actually a triple diagonal matrix.

During the program,
For atmospheric parts in `MODULE:[VFTND1(pimtx.F)]`,
MODULE:[GNDHT1(pggnd.F)]` for the underground part, the first half of the LU decomposition method.
(where TERM00063 is obtained),
In `MODULE:[SLVSFC(pgslv.F)]`, solve the equation of TERM00064,
Seeking TERM00065,TERM00065.
Then, in `MODULE:[GNDHT2(pggnd.F)]`
The second half of the LU decomposition method is performed and the rate of change of temperature in the ground is solved,
Correct the fluxes so that the balance is matched.
Also, in `MODULE:[VFTND2(pimtx.F)]`, for the atmosphere
Solving the rate of temperature change,
Fluxes are corrected with `MODULE:[FLXCOR(pimtx.F)]`.

### Combined expression for time difference

The coupling formula for finding TERM00066,TERM00066 is ,
Solve three times under different conditions as follows.

Solve for surface wetness TERM00067 as 1. Surface temperature is a variable.

2. the surface wetness obtained by `MODULE:[GNDBET]`.
 Surface temperature is a variable .

3. the surface wetness obtained by `MODULE:[GNDBET]`.
 In case of snowmelt, the surface temperature is fixed at the freezing point.

The first calculation is performed to estimate the possible evaporation rate, TERM00068.
(When the surface wetness is small, the energy balance of the model indicates that
Using the obtained TERM00069, the possible evaporation rate can be calculated by
TERM00070
diagnosed as, would result in unrealistically large values).
Possible evaporation rate is ,

> EQ=00057.

That would be.
The subscript TERM00071 means after correction,
This is a consistent flux to the obtained temperature etc.

In the second and subsequent calculations ,

1. to the amount of possible evaporation found in the first calculation
 Surface wetness (evaporation efficiency) TERM00072
 multiplied by the amount of evaporation TERM00073.

     > EQ=00042.

2. evaporation quantity TERM00074 is

     > EQ=00043.

 As required by ,
 Once again, rebalancing the energy.

Two methods of calculating the amount of evaporation can be used
(The standard uses the method in 1.).
The third calculation is performed during snow and ice melt and sea ice formation in the mixed layer ocean.
This is done in order to fix the surface temperature at the freezing point, for example, to unbalance the energy.
In this case, the amount of energy used for the phase change of water, such as snowmelt, is diagnostically determined,
It will be used later to calculate the amount of snow melt, etc.

The concrete form of the coupling formula is as follows.

> EQ=00058.
> <span id="combin-eq" label="combin-eq">\\brain[combin-eq]</span>
> EQ=00058.

Here, TERM00075, TERM00075 and TERM00076, TERM00076 are,
The components of the matrices and vectors obtained by doing the first half of the LU decomposition method.
When the ground is covered with snow or ice, instead of the latent heat TERM00077
Using the Latent Heat of Sublimation TERM00078 TERM00079 is the latent heat of melting of water.
However, in the second calculation,
If the first method is used as an estimate of evaporation, we get the following.

> EQ=00059.
> EQ=00059.

In the third calculation, the concatenation equation for a fixed surface temperature is

> EQ=00060.
> <span id="combin-eq3" label="combin-eq3">\brain[combin-eq3]</span>
> EQ=00060.

Here, TERM00080 is the rate of change to the temperature to be fixed,

> EQ=00044.

TERM00081 is 273.15K for snow and ice melting,
In the case of sea ice production it is 271.15K.
If the second method of evaporation calculation is used, then
Similarly, use TERM00083 instead of TERM00082,
Calculate the differential term of TERM00084 as 0.
In this case,

> EQ=00061.
> EQ=00061.

TERM00085, calculated by the Surface Energy Balance,
It is the amount of energy used for the phase change of water.

### implicit Treatment of Time Steps in Time Differences

Although the implicit method is used for the time difference of the vertical diffusion term,
In general, the diffusion coefficients are nonlinear, and we explicitly evaluate these coefficients
This can cause problems of numerical instability.
To improve stability, Kalnay and Kanamitsu (19?) following the
I'm working on how to handle the time steps.

For simplicity, we will take the following ordinary differential equations as an example.

> EQ=00045.

The coefficient TERM00086 represents the nonlinearity.
If we evaluate only the coefficients explicitly and make them implicitly different, we get the following equation.

> EQ=00046.
> <span id="normal-fd" label="normal-fd">\centric[normal-fd]</span>

However, consider the value of TERM00087 two steps ahead, TERM00088,

> EQ=00047.
> <span id="modify-fd1" label="modify-fd1">\[modify-fd1\\blade]</span>

> EQ=00048.
> <span id="modify-fd2" label="modify-fd2">\[modify-fd2\Backlash]</span>

.
Generally, ([modify-fd1\]](#modify-fd1)), ([modify-fd2\](#modify-fd2)) is better
([normal-fd]](#normal-fd)) is known to be more stable than [normal-fd]).

([modifie-fd1\](#modifie-fd1)), ([modifie-fd2\lenses](#modifie-fd2)) to find the rate of change in time
Rewriting it into a form yields the following.

> EQ=00049.

> EQ=00050.

That is, the time step in determining the rate of change of the rate of change of time includes the following,
Using twice the time integration step.
