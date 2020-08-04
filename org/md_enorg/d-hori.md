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

     EQ=00000.

Using the Legendre jury function TERM00003 it is written as follows.

     EQ=00001.

However, it is TERM00004.

The expansion by spherical harmonic functions is ,

     EQ=00002.

When I write ,

     EQ=00003.

The inverse of that is ,

     EQ=00017.
     EQ=00017.

expressed as follows.
When evaluating the summation of the integral,
See Gauss's trapezoidal formula for the TERM00007 integral,
Use the Gauss-Legendre integral formula for the TERM00008 integral.
TERM00009 is the Gauss latitude and TERM00010 is the Gauss load.
The TERM00011 is an evenly spaced grid.

Using spectral expansion,
The grid point values for the terms containing the derivatives are found as follows.

     EQ=00004.

     EQ=00005.

Furthermore,
From the spectral components of TERM00014 and TERM00015,
The grid point values for TERM00016 and TERM00016 are obtained as follows.

     EQ=00006.

     EQ=00007.

The derivative that appears in the advection term of the equation is,
The following is required.

     EQ=00018.
     EQ=00018.
     EQ=00018.

     EQ=00019.
     EQ=00019.
     EQ=00019.

Furthermore,

     EQ=00008.

for the evaluation in TERM00019.

### Horizontal Diffusion Term

The horizontal diffusion term is entered in the form TERM00020 as follows.

     EQ=00009.

     EQ=00010.

     EQ=00011.

     EQ=00012.

This horizontal diffusion term has strong implications for computational stability.
To represent selective horizontal diffusion on small scales,
For TERM00021, use 4 TERM00022 16.
Here, the extra terms on vorticity and divergence diffusion are
This shows that the term for rigid body rotation in TERM00023 is not damped.

### Spectral representation of equations

1. a series of equations

         EQ=00020.
         EQ=00020.

 Here,

         EQ=00013.

2. equation of motion

         EQ=00021.
         EQ=00021.
         EQ=00021.

         EQ=00022.
         EQ=00022.
         EQ=00022.
         EQ=00022.

 However,

         EQ=00014.

3. thermodynamic equation

         EQ=00023.
         EQ=00023.
         EQ=00023.
         EQ=00023.

 However,

         EQ=00015.

4. water vapor formula

         EQ=00024.
         EQ=00024.
         EQ=00024.
         EQ=00024.

 However,

         EQ=00016.