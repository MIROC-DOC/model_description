## Time integration.

The time difference scheme is essentially a leap frog.
However, the diffusion terms and physical process terms are backward or forward differences.
A time filter (Asselin, 1972) is used to suppress the computational mode.
In order to increase the value of TERM00000, we use a time filter (Asselin, 1972),
Applying the semi-implicit method to the gravitational wave term (Bourke, 1988).

### Time integration and time filtering by leap frog

We use leap frog as a time integration scheme for advection terms and so on.
The backward difference of TERM00001 is used for the horizontal diffusion term.
The pseudo TERM00002 surface correction of the diffusion term and the frictional heat by horizontal diffusion term are combined with
treated as a correction and becomes a forward difference in TERM00003.
The physical process terms (TERM00004 and TERM00004) are treated as
We still use the forward difference of TERM00005.
(However, for the calculation of the time-varying term of vertical diffusion, we treat it as a backward difference.
Please refer to the chapter on physical processes for details.)

Representing each of the forecast variables as TERM00006, we obtain

> EQ=00000.

TERM00007 is an advection term etc,
TERM00008 is a horizontal diffusion term.

In TERM00009, there is a horizontal diffusion term,
Pseudo, etc. TERM00010 Correction of frictional heat (TERM00011) by surface and horizontal diffusion
and physical processes (TERM00012) have been added,
TERM00013.

> EQ=00001.

To remove the calculation mode in leap frog
The time filter of Asselin (1972) is applied at every step.
I.e. ,

> EQ=00002.

and TERM00014.
Normally 0.05 is used as the TERM00015.

### semi-implicit time integration

For mechanics calculations, the leap frog is basically used,
We treat some terms as implicit.
Here, the implicit considers the trapezoidal implicit.
For the vector quantity TERM00016,
The value in TERM00017 is converted to TERM00018,
The value in TERM00019 was converted to TERM00020,
If you write the value of TERM00021 as TERM00022,
What is trapezoidal implicit?
TERM00023.
We use the time-varying terms evaluated by using
Now, as a time-varying term in <span>q</span>,
The term A is treated in the leap forg method and the term B is treated in the trapezoidal implicit method.
Assume that A is nonlinear with respect to <span>q</span>, while B is linear.
In other words,

> EQ=00003.

where TERM00024 is a square matrix. Then,
TERM00025
And then you can write,

> EQ=00004.

This can be easily solved by matrix operations.

### semi-implicit time integration applied

Then, we apply this method and treat the term of linear gravity waves as implicit.
This allows us to reduce the time step (TERM00026).

In the system of equations, the basic field is such that TERM00027
Separation of the linear gravity wave term and the other terms (with the index TERM00028).
Vertical Vector Representation
Using TERM00029, TERM00030,

> EQ=00005.

> EQ=00006.

> EQ=00032.

where the non-gravitational wave term is,

> EQ=00007.
> <span id="Section Z" label="Section Z" label="Section Z" label=">\\\\\.} </span>

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

where the vector and matrix of the gravitational wave terms (underlined) are,

> EQ=00012.
> <span id="Coefficient C" label="Coefficient C">\\c\[Coefficient C]</span>

> EQ=00013.

> EQ=00014.

> EQ=00015.

> EQ=00016.

> EQ=00017.

> EQ=00018.
> <span id="Coefficient R" label="Coefficient R">\R\[Coefficient R]</span>.

Here, for example, TERM00031 is the same as
It is a function that is 1 if TERM00032 is true and 0 otherwise.

Using the following expression,

> EQ=00019.
> <span id="Shemiinp" label="Shemiinp">\\centric="Shemiinp\centric"> </span>.

> EQ=00034.  
> EQ=00034.

Applying the semi-implicit method to a system of equations,

> EQ=00020.
> <span id="semi-imp pi" label="semi-imp pi" label="semi-imp pi">\[semi-imp pi]</span>

> EQ=00021.
> <span id="semi-imp D" label="semi-imp D" label="semi-imp D">\[semi-imp D\\[semi-imp D\]</span>

> EQ=00022.
> <span id="semi-imp T" label="semi-imp T" label="semi-imp T">\[semi-imp T]</span>

So..,

> <span id="semi-imp barD" label="semi-imp barD" label="semi-imp barD">\\brachos[semi-imp barD\brachos]</span>
> EQ=00035.  
> EQ=00035.  
> EQ=00035.  
> EQ=00035.

Since we use the spherical harmonic expansion, we can use it,

and the above formula can be solved for TERM00033.
After that,

> EQ=00023.

and ([semi-imp pi\]](#semi-imp%20pi), ([semi-imp T\\](#semi-imp%20T))
The value in TERM00034 according to TERM00035
is required .

### Time scheme properties and time step estimates

advectional equation

> EQ=00024.

Consider the stability of the leap frog discretization in
Now,

If we place the difference between

> EQ=00025.

where
Here ,
\\lambda = X^{n+1}/X^n = X^n/X^{n-1}}\\\\bars}]
So,

> EQ=00026.

The solution is labeled TERM00036,

> EQ=00027.

This absolute value is

> EQ=00028.

In the case of TERM00037, it would be TERM00038,
The solution becomes exponentially larger in absolute value with time.
This indicates that the computation is unstable.

On the other hand, in the case of TERM00039, the value is TERM00040,
The calculation is neutral.
However, there are two solutions for TERM00041,
One of them, when TERM00042 is set to
This is a TERM00043, but..,
The other is TERM00044.
This indicates a time-varying solution.
This mode is called "calculation mode",
One of the problems with the leap frog method.
This mode can be applied by applying a time filter to the
It can be attenuated.

The terms of the TERM00045 are,
Given the horizontal discretization grid spacing TERM00046, the
This will cause the maximum value of TERM00047 to be
\More than one person can be in a position to do so.
From becoming ,

> EQ=00029.

In the case of the spectral model, the maximum wavenumber of
For the spectral model, the maximum wavenumber is determined by TERM00048,
Earth radius is set to TERM00049,

> EQ=00030.

This is the stability condition.

To guarantee the stability of the integral,
As for TERM00050, it has the fastest advection and propagation speed,
You may use a time step smaller than TERM00051 which is determined by the semi-implicit method.
If semi-implicit is not used, the propagation speed of the gravitational wave
(TERM00052) is the criterion for stability,
When semi-implicit is used, advection by the east-west wind is usually
This is a limiting factor.
Therefore, the TERM00053 sets TERM00054 as the maximum value of the east-west wind,

> EQ=00031.

In practice, this is multiplied by a safety factor.
In practice, this should be multiplied by a safety factor.

### Treatment at the beginning of time integration.

Not calculated by AGCM,
If you start with an appropriate initial value, you can use a model-consistent
You cannot give the physical quantities for two times of TERM00055 and TERM00056.
However, if you give an inconsistent value for TERM00057, then you should not give an inconsistent value for TERM00057,
A large calculation mode is generated.

So, first, as TERM00058, in the time step of TERM00059
\{X^{{X}^{D\Delta t/2} = X^0 + X^0 + {{X}^{D\Delta t/2}
                 = X^0 + t/2 \\Dentro{X}^0\0}]
and furthermore, in the time step of TERM00060,
\\\\lopen}t = X^{X}^{X}^^{X}^{\Delta t/2}}\lopen}t = X^0 + \lopen}t\lopen}t\lopen}t/2\lopen}t
And, in the original time step,
\\\\ltraLabella t} = X^{2\Delta t} = X^0 + 2\labella t\labella t\labella t}^{X}^{\labella t}]
and then perform the calculation with leap frog as usual,
The occurrence of computation modes is reduced.
