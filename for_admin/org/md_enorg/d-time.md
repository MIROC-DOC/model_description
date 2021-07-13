## Time integration.

The time difference scheme is essentially a leap frog. However, the diffusion terms and physical process terms are backward or forward differences. A time filter (Asselin, 1972) is used to suppress the computational modes. A semi-implicit method is applied to the gravitational wave term to make the TERM00254 larger (Bourke, 1988).

### Time integration and time filtering with leap frog

We use leap frog as a time integration scheme for advection terms and so on. A backward difference of TERM00255 is used for the horizontal diffusion term. The pseudo TERM00256 surface correction of the diffusion term and the frictional heat due to horizontal diffusion term are treated as corrections, which are forward differences of TERM00257. The physical process terms (TERM00258 and TERM00258) still use the forward difference of TERM00259 (except for the vertical diffusion term, which uses the forward difference of TERM00258). (However, the calculation of the time-varying term of vertical diffusion is treated as a backward difference. Please refer to the chapter on physical processes for details.)

Expressed as TERM00260 on behalf of each forecast variable,

     EQ=00064.

TERM00261 is the advection term etc., and TERM00262 is the horizontal diffusion term.

To TERM00263, the term TERM00267 has been added with corrections for the heat of friction (TERM00265) and physical processes (TERM00266) for pseudo-equivalent TERM00264 surface diffusion and horizontal diffusion.

     EQ=00065.

The time filter of Asselin (1972) is applied every step to remove computational modes in leap frog. I.e., the time filter of Asselin(1972) is applied every step of the way to remove the computation mode in

     EQ=00066.

and TERM00268. Normally, 0.05 is used as the TERM00269.

### semi-implicit time integration

Basically, the leap frog is used in mechanics calculations, but some terms are treated as implicit. Here, we consider the trapezoidal implicit as the implicit. For the vector quantity TERM00270, the value of TERM00271 is written as TERM00272, the value of TERM00273 as TERM00274, and the value of TERM00275 as TERM00276, then the trapezoidal implicit means that the time change term evaluated by TERM00277 is This is the solution of the problem by using the leap forg method. We now divide <span>q</span> into two time varying terms, one for the leap forg method and the other for the trapezoidal implicit method, B. We assume that A is nonlinear to <span>q</span>, while B is linear. In other words,

     EQ=00067.

However, TERM00278 is a square matrix. Then write TERM00279 and you will get

     EQ=00068.

This can be easily solved by matrix operations.

### Applying semi-implicit time integration

Then, we apply this method and treat the term of linear gravity waves as implicit. This allows us to reduce the time step TERM00280.

In the system of equations, we divide the equation into a linear gravitational wave term (TERM00281) with a stationary field as the basic field and other terms (with the indices TERM00282). Using a vector representation of vertical direction (TERM00283 and TERM00284)

     EQ=00069.

     EQ=00070.

     EQ=00102.

Here, the non-gravitational wave term is

     EQ=00071.

     EQ=00072.

     EQ=00073.

     EQ=00074.

     EQ=00103.
     EQ=00103.
     EQ=00103.
     EQ=00103.
     EQ=00103.
     EQ=00103.
     EQ=00103.

     EQ=00075.

where the vector and matrix of the gravitational wave term (underlined) are

     EQ=00076.

     EQ=00077.

     EQ=00078.

     EQ=00079.

     EQ=00080.

     EQ=00081.

     EQ=00082.

Here, for example, TERM00302 is 1 if TERM00303 is valid and 0 otherwise.

Using the following expression ,

     EQ=00083.

     EQ=00104.
     EQ=00104.

If we apply the semi-implicit method to the system of equations,

     EQ=00084.

     EQ=00085.

     EQ=00086.

So..,

     EQ=00105.
     EQ=00105.
     EQ=00105.
     EQ=00105.

Since the spherical harmonic expansion is used, we can solve the above equation for TERM00327 with the result that it is in fact, a spherical harmonic expansion is used. After that,

     EQ=00087.

and, (109), (111) to obtain the value TERM00330 in TERM00329.

### Time scheme properties and time step estimates

advectional equation

     EQ=00088.

Considering the stability of the discretization in the leap frog in Now,

     EQ=00089.

If we place the difference between

     EQ=00090.

That would be. Here,

     EQ=00091.

So,

     EQ=00092.

The solution is called TERM00331,

     EQ=00093.

This absolute value is

     EQ=00094.

and in the case of TERM00332, we get TERM00333, and the absolute value of the solution increases exponentially with time. This indicates that the computation is unstable.

In the case of TERM00334, however, the calculation is neutral since the value of TERM00335. However, there are two solutions to TERM00336, one of which, when set to TERM00337, leads to TERM00338, while the other leads to TERM00339. This indicates a time-varying solution. This mode is called "computational mode" and is one of the problems of the leap frog method. This mode can be degraded by applying a time filter.

The condition for TERM00340 is that given the horizontal discretization grid spacing TERM00341, it causes the maximum value of TERM00342 to be

     EQ=00095.

From becoming ,

     EQ=00096.

In the case of the spectral model, the In the case of the spectral model, the Earth's radius is defined as TERM00344 by the maximum wavenumber, TERM00343,

     EQ=00097.

This is a condition for stability.

In order to guarantee the stability of the integral, for TERM00345, the fastest advection and propagation speed can be adopted and a time step smaller than TERM00346, which is determined by this speed, can be used. When the semi-implicit method is not used, the propagation speed of the gravity wave (TERM00347) is the criterion for stability, but when the semi-implicit method is used, the advection caused by the easterly wind is usually a limiting factor. Therefore, TERM00348 assumes that TERM00349 is the maximum value of zonal wind,

     EQ=00098.

In practice, this is multiplied by a safety factor. In practice, this is multiplied by a safety factor.

### Handling of the Initiation of Time Integration

When starting from a suitable initial value that is not calculated by AGCM, it is not possible to give two physical quantities of time, TERM00350 and TERM00351, that are consistent with the model. However, giving an inconsistent value for TERM00352 will result in a large computation mode.

So, firstly, as TERM00353, in the time step of TERM00354

     EQ=00099.

and furthermore, in the time step of TERM00355,

     EQ=00100.

And, in the original time step,

     EQ=00101.

and use leap frog as usual, it prevents the occurrence of the calculation mode.