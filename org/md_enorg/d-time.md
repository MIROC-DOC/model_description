## Time integration.

The time difference scheme is basically a leap frog.
However, the terms of the diffusion terms and physical processes are backward or forward differences.
A time filter (Asselin, 1972) is used to suppress the computational mode.
And to make the TERM00000 larger,
Applying the semi-implicit method to the term gravitational wave (Bourke, 1988).

### Time integration and time filtering with leap frog

The leap frog is used as a time integration scheme for advection terms and so on.
The backward difference of TERM00001 is used for the horizontal diffusion term.
In addition, the pseudo TERM00002 surface correction of the diffusion term and the frictional heat term by horizontal diffusion are
treated as a correction and becomes the forward difference in TERM00003.
The physical process section (TERM00004,TERM00004) is ,
I still use the forward differential of TERM00005.
(However, we treat the calculation of the time varying term of vertical diffusion as a backward difference.
See the chapter on physical processes for details.)

Expressed as TERM00006 on behalf of each forecast variable,

> EQ=00000.

TERM00007 is an advection term etc,
TERM00008 is a horizontal diffusion term.

TERM00009 has a ,
Pseudo, etc. TERM00010 Correction of frictional heat (TERM00011) by surface and horizontal diffusion
and physical processes (TERM00012) have been added,
TERM00013.

> EQ=00001.

To remove the computation mode in leap frog
Apply the time filter of Asselin (1972) at every step.
Namely,

> EQ=00002.

and TERM00014.
For TERM00015 it is standard to use 0.05.

### semi-implicit time integration

For mechanics calculations, the leap frog is basically used,
Compute some terms as implicit.
Here, implicit considers a trapezoidal implicit.
Regarding the vector quantity TERM00016,
The value in TERM00017 is converted to TERM00018,
The value in TERM00019 was converted to TERM00020,
If you write the value of TERM00021 as TERM00022,
What is trapezoidal implicit?
TERM00023.
The solution is done by using the time-varying terms evaluated by using
Now, as a time-varying term in <span>q</span>,
The term A is treated in the leap forg method and the term B is treated in the trapezoidal implicit method.
A is nonlinear with respect to <span>q</span>, while B is Suppose it is linear.
Namely,

> EQ=00003.

Note that TERM00024 is a square matrix. Then,
TERM00025
And then you can write,

> EQ=00004.

This can be easily solved by matrix operations.

### Applying semi-implicit time integration

So we apply this method and treat the term of linear gravity waves as implicit.
This makes the time step TERM00026 smaller.

In a system of equations, the basic field is such that TERM00027
Separation of the linear gravitational wave term and the other terms (with the index TERM00028).
Vertical Vector Representation
Using TERM00029, TERM00030,

> EQ=00005.

> EQ=00006.

> EQ=00032.

Here, the non-gravitational wave term is

> EQ=00007.
> <span id="Section Z" label="Section Z" label="Section Z" >\bout[Section Z]&lt ;/span>

> EQ=00008.

> EQ=00009.

> EQ=00010.

> EQ=00033. 
> EQ=00033. 
> EQ=00033. 
> EQ=00033. 
> EQ=00033. 
> EQ=00033. 
> EQ=00033.

> EQ=00011.

where the vector and matrix of the gravitational wave term (underlined) are

> EQ=00012.
> <span id="Coefficient C" label="Coefficient C">Dr./Ing. lt;/span>

> EQ=00013.

> EQ=00014.

> EQ=00015.

> EQ=00016.

> EQ=00017.

> EQ=00018.
> <span id="Coefficient R" label="Coefficient R" >Dr.R.[Coefficient R]& lt;/span>

Here, for example, TERM00031 is the same as
A function that is 1 if the TERM00032 is valid and 0 otherwise.

Using the following expression ,

> EQ=00019.
 PluginPointPointPoint.com

> EQ=00034. 
> EQ=00034.

If we apply the semi-implicit method to the system of equations,

> EQ=00020.
> <span id="semi-imp pi" label="semi-imp 

> EQ=00021.
> <span id="semi-imp D" label="semi-imp D ">\\brahammer[semi-imp D\\\]</span>

> EQ=00022.
> <span id="semi-imp T" label="semi-imp T "> >Semi-imp T\\[semi-imp T]</span>.

So..,

> <span id="semi-imp barD" label="semi- imp barD">\blank\[semi-imp barD\blank]</span></a
> EQ=00035. 
> EQ=00035. 
> EQ=00035. 
> EQ=00035.

Since the spherical harmonic expansion is used,
\braham[EQ=00036.com]
and the above equation can be solved for TERM00033.
And then..,

> EQ=00023.

and, ([[semi-imp pi\]](#semi-imp%20pi)), ([\\blink\blink}](#semi-imp%20pi) semi-imp T\]](#semi-imp%20T))
The value in TERM00034 according to TERM00035
is required.

### Time scheme properties and time step estimates

advectional equation

> EQ=00024.

Considering the stability of the discretization in the leap frog in
Now,

If we place the difference between

> EQ=00025.

That would be.
Here,
\\lambda = X^{n+1}/X^n = X^n/X^{n-1}}\\\\bars}]
So,

> EQ=00026.

The solution is called TERM00036,

> EQ=00027.

This absolute value is

> EQ=00028.

In the case of TERM00037, it is TERM00038,
It is a solution whose absolute value increases exponentially with time.
This indicates that the computation is unstable.

On the other hand, for TERM00039, the number is TERM00040,
The calculation is neutral.
However, there are two solutions for TERM00041,
One of them, when TERM00042 is set to
This is a TERM00043, but..,
The other is TERM00044.
This indicates that the solution oscillates strongly in time.
This mode is called calculation mode,
One of the problems with the leap frog method.
This mode can be used by applying a time filter to the
It can be attenuated.

The terms of the TERM00045 are ,
Given the horizontal discretization grid spacing TERM00046, the
This will cause the maximum value of TERM00047 to be
\More than one person can be in a position to do so.
From becoming ,

> EQ=00029.

That would be.
In the case of a spectral model, the maximum wavenumber depends on the TERM00048,
Earth radius is set to TERM00049,

> EQ=00030.

This is a condition for stability.

To guarantee the stability of the integration,
As for TERM00050, it has the fastest advection and propagation speed,
You can use a time step smaller than TERM00051 determined by that.
When semi-implicit is not used, the propagation speed of gravity wave
(TERM00052) is the criterion for stability,
When semi-implicit is used, advection by the east-west wind is usually
Limiting factors.
Therefore, TERM00053 sets TERM00054 as the maximum value of the east-west wind,

> EQ=00031.

Take to meet the .
In practice, this is multiplied by a safety factor.

### Handling of the Initiation of Time Integration

Not calculated by AGCM,
If you start with an appropriate initial value, you can use a model-consistent
You cannot give two physical quantities of time in TERM00055 and TERM00056.
However, if you give an inconsistent value for TERM00057
A large calculation mode occurs.

So, first, as TERM00058, in the time step of TERM00059
\{X^{X}^{D}t/2} = X^0 + X^0 + {{X}^{D}^{X}^^{\\\finger}}. Delta t/4}
                  = X^0 + t/2 \\Dentro{X}^0\0}]
and furthermore, in the time step of TERM00060,
\\\\ltraL\Delta t} = X^0 +    X^0+\l\Delta t/2 }]
And, in the original time step,
\\blossom[X^{2\Delta t} = X^0 + 2\blossomDot{X}^{2\blossomDelta t} = X^0 + 2\blossomDelta t    }]
and then perform the calculation with leap frog as usual,
The occurrence of computation mo

