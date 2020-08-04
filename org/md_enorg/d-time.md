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

     EQ=00000.

TERM00007 is an advection term etc,
TERM00008 is a horizontal diffusion term.

TERM00009 has a ,
Pseudo, etc. TERM00010 Correction of frictional heat (TERM00011) by surface and horizontal diffusion
and physical processes (TERM00012) have been added,
TERM00013.

     EQ=00001.

To remove the computation mode in leap frog
Apply the time filter of Asselin (1972) at every step.
Namely,

     EQ=00002.

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
Assume that A is nonlinear for <span>q</span>, but B is linear.
Namely,

     EQ=00003.

Note that TERM00024 is a square matrix. Then,
TERM00025
And then you can write,

     EQ=00004.

This can be easily solved by matrix operations.

### Applying semi-implicit time integration

So we apply this method and treat the term of linear gravity waves as implicit.
This makes the time step TERM00026 smaller.

In a system of equations, the basic field is such that TERM00027
Separation of the linear gravitational wave term and the other terms (with the index TERM00028).
Vertical Vector Representation
Using TERM00029, TERM00030,

     EQ=00005.

     EQ=00006.

     EQ=00038.

Here, the non-gravitational wave term is

     EQ=00007.

     EQ=00008.

     EQ=00009.

     EQ=00010.

     EQ=00039.
     EQ=00039.
     EQ=00039.
     EQ=00039.
     EQ=00039.
     EQ=00039.
     EQ=00039.

     EQ=00011.

where the vector and matrix of the gravitational wave term (underlined) are

     EQ=00012.

     EQ=00013.

     EQ=00014.

     EQ=00015.

     EQ=00016.

     EQ=00017.

     EQ=00018.

Here, for example, TERM00048 is
A function that is 1 if TERM00049 is valid and 0 otherwise.

Using the following expression ,

     EQ=00019.

     EQ=00040.
     EQ=00040.

If we apply the semi-implicit method to the system of equations,

     EQ=00020.

     EQ=00021.

     EQ=00022.

So..,

     EQ=00041.
     EQ=00041.
     EQ=00041.
     EQ=00041.

Since the spherical harmonic expansion is used,

and the above equation can be solved for TERM00073.
And then..,

     EQ=00023.

and, (24), (26)
The value in TERM00075 according to TERM00076
is required.

### Time scheme properties and time step estimates

advectional equation

     EQ=00024.

Considering the stability of the discretization in the leap frog in
Now,

     EQ=00025.

If we place the difference between

     EQ=00026.

That would be.
Here,

     EQ=00027.

So,

     EQ=00028.

The solution is called TERM00077,

     EQ=00029.

This absolute value is

     EQ=00030.

and in the case of TERM00078, it is TERM00079,
It is a solution whose absolute value increases exponentially with time.
This indicates that the computation is unstable.

On the other hand, in the case of TERM00080, because it is TERM00081,
The calculation is neutral.
However, there are two solutions to the value of TERM00082,
One of them is TERM00083, and the other is
This is TERM00084, but ,
The other would be TERM00085.
This indicates that the solution oscillates strongly in time.
This mode is called calculation mode,
One of the problems with the leap frog method.
This mode can be used by applying a time filter to the
It can be attenuated.

The terms of the TERM00086 are ,
Given the horizontal discretization lattice interval TERM00087, if
This will cause the maximum value of TERM00088 to be

     EQ=00031.

From becoming ,

     EQ=00032.

That would be.
In the case of spectral models, the maximum wavenumber is determined by TERM00089,
Earth radius is set to TERM00090,

     EQ=00033.

This is a condition for stability.

To guarantee the stability of the integration,
As for TERM00091, it has the fastest advection and propagation speed,
You can use a smaller time step than TERM00092 determined by that.
When semi-implicit is not used, the propagation speed of gravity wave
(TERM00093) is the criterion for stability, but ,
When semi-implicit is used, advection by the east-west wind is usually
Limiting factors.
Thus, TERM00094 assumes that TERM00095 is the maximum value of the east-west wind,

     EQ=00034.

Take to meet the .
In practice, this is multiplied by a safety factor.

### Handling of the Initiation of Time Integration

Not calculated by AGCM,
If you start with an appropriate initial value, you can use a model-consistent
You cannot give two physical quantities of time in TERM00096 and TERM00097.
However, if you give an inconsistent value for TERM00098
A large calculation mode occurs.

So, first, as TERM00099, in the time step of TERM00100

     EQ=00035.

and furthermore, in the time step of TERM00101,

     EQ=00036.

And, in the original time step,

     EQ=00037.

and then perform the calculation with leap frog as usual,
The occurrence of computation modes is reduced.