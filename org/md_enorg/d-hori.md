## Horizontal discretization

The horizontal discretization of the
Using the spectral transformation method (Bourke, 1988).
The differential terms for longitude and latitude are evaluated by the orthogonal function expansion,
On the other hand, the nonlinear term is computed on the grid points.

### Spectral Expansion.

As an expansion function system, it is a Laplacian eigenfunction system on a sphere
Using the spherical harmonic functions TERM00000 and TERM00000.
However, it is TERM00001.
TERM00002 satisfies the following equation,

> EQ=00000.

Using the Legendre jury function TERM00003 it is written as follows.

> EQ=00001.

However, it is TERM00004.

The expansion by spherical harmonic functions is ,

> EQ=00002.

When I write ,

> EQ=00003.
> <span id="spherical expansion" label="spherical expansion">\centric expansion </span>.

The inverse of that is ,

> EQ=00017. 
> <span id="Deployment factor" label="Deployment factor">\blendon[Deployment factor </span>.
> EQ=00017.

expressed as follows.
When evaluating the sum of the integral, you can substitute the sum of ,
See Gauss's trapezoidal formula for the TERM00006 integral,
Use the Gauss-Legendre integral formula for the TERM00007 integral.
TERM00008 is the Gauss latitude and TERM00009 is the Gauss load.
The TERM00010 is an evenly spaced grid.

Using spectral expansion,
The grid point values for the terms containing the derivatives are found as follows.

> EQ=00004.
> <span id="barometric pressure x" label="barometric pressure x">\blazer.com[barometric pressure x]& lt;/span>

> EQ=00005.
> <span id="barometric pressure y" label="barometric pressure y">\blazer[barometric pressure y]& lt;/span>

Furthermore,
From the spectral components of TERM00011 and TERM00012,
The grid point values for TERM00013 and TERM00013 are obtained as follows.

> EQ=00006.
> <span id="Seeking U" label="Seeking U" >\blaze[U Seeking a seat

> EQ=00007.
> <span id="Ask for V" label="Ask for V" >\blaze[V Seeking a seat

The derivative that appears in the advection term of the equation is,
The following is required.

> <span id="A integral" label="A integral" label="A integral">A Integral\[A integral]& lt;/span>
> EQ=00018. 
> EQ=00018. 
> EQ=00018.

> <span id="BIntegral" label="BIntegral">\blazer[BIntegral\.com]& lt;/span>
> EQ=00019. 
> EQ=00019. 
> EQ=00019.

Furthermore,

> EQ=00008.

to be used for the evaluation of the TERM00014 section.

### Horizontal Diffusion Term

The horizontal diffusion term is entered in the form TERM00015 as follows.

> EQ=00009.
> <span id="Horizontal Diffusion" label="Horizontal Diffusion">\blaze[horizontal diffusion </span>.

> EQ=00010.

> EQ=00011.

> EQ=00012.

This horizontal diffusion term has strong implications for computational stability.
To represent selective horizontal diffusion on small scales,
For TERM00016, use 4 TERM00017 16.
Here, the extra terms on vorticity and divergence diffusion are
This shows that the term for rigid body rotation in TERM00018 is not damped.

### Spectral representation of equations

1. a series of equations
     
     > EQ=00020. 
     > EQ=00020.
     
 Here,
     
     > EQ=00013.

2. equation of motion
     
     > EQ=00021. 
     > EQ=00021. 
     > EQ=00021.
     
     > EQ=00022. 
     > EQ=00022. 
     > EQ=00022. 
     > EQ=00022.
     
 However,
     
     > EQ=00014.

3. thermodynamic equation
     
     > EQ=00023. 
     > EQ=00023. 
     > EQ=00023. 
     > EQ=00023.
     
 However,
     
     > EQ=00015.

4. water vapor formula
     
     > EQ=00024. 
     > EQ=00024. 
     > EQ=00024. 
     > EQ=00024.
     
 However,
     
     > EQ=00016.

