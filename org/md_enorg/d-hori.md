## Horizontal discretization

The horizontal discretization of the
The spectral transformation method is used (Bourke, 1988).
The differential terms for longitude and latitude are evaluated by orthogonal function expansion,
On the other hand, non-linear terms are computed on the grid points.

### Spectral Expansion.

As an expansion function system, it is a Laplacian eigenfunction system on a sphere
The spherical harmonic function TERM00000 and TERM00000 are used.
with TERM00001.
TERM00002 satisfies the following equation,

> EQ=00000.

Using the Legendre junction number TERM00003 it is written as follows.

> EQ=00001.

but TERM00004.

The expansion by the spherical harmonic function is written as ,

> EQ=00002.

If you write ,

> EQ=00003.
> <span id="Spherical Expansion" label="Spherical Expansion">\\\blur[Spherical Expansion]</span>

The inverse of that is ,

> EQ=00017.  
> <span id="Deployment Factor" label="Deployment Factor">\\\.com[Deployment Factor]</span>
> EQ=00017.

.
When evaluating by replacing the integral with the sum,
See Gauss's trapezoidal formula for the TERM00006 integral,
We use the Gauss-Legendre integral formula for the TERM00007 integral.
TERM00008 is the Gauss latitude and TERM00009 is the Gauss load.
Also, TERM00010 is a grid of evenly spaced Gauss loads.

Using the spectral expansion, we can obtain a new formula for Gauss-Legendre integration,
The grid point values for the terms containing the derivatives are found as follows.

> EQ=00004.
> <span id="barometric pressure x" label="barometric pressure x">\a[barometric pressure x]</span>.

> EQ=00005.
> <span id="barometric y" label="barometric y" label="barometric y">\blaze[barometric y]</span>.

Furthermore,
From the spectral components of TERM00011 and TERM00012,
The grid point values for TERM00013 and TERM00013 are obtained as follows.

> EQ=00006.
> <span id="Seeking U" label="Seeking U" label="Seeking U">\\[Seeking U]</span>.

> EQ=00007.
> <span id="Seeking V" label="Seeking V">\\\[V seeking]</span>

The derivative that appears in the advection term of the equation is,
It is required as follows.

> <span id="A integral" label="A integral" label="A integral">\[A integral]</span>
> EQ=00018.  
> EQ=00018.  
> EQ=00018.

> <span id="B integral" label="B integral" label="B integral">B integral\blazer\blazer]</span>.
> EQ=00019.  
> EQ=00019.  
> EQ=00019.

Further ,

> EQ=00008.

to evaluate the term TERM00014.

### Horizontal Diffusion Term.

The horizontal diffusion term is entered in the form TERM00015 as follows.

> EQ=00009.
> <span id="Horizontal Diffusion" label="Horizontal Diffusion">Regular\[Horizontal Diffusion]</span>.

> EQ=00010.

> EQ=00011.

> EQ=00012.

This horizontal diffusion term has strong implications for computational stability.
In order to represent selective horizontal diffusion on small scales,
For TERM00016, 4 TERM00017 16 is used.
The extra terms on the diffusion of vorticity and divergence are
It represents that the term for rigid body rotation in TERM00018 does not decay.

### Spectral representation of the equation

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
