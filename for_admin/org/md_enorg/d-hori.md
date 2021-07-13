## Horizontal discretization

The horizontal discretization is based on the spectral transformation method (Bourke, 1988). The differential terms for longitude and latitude are evaluated by the orthogonal function expansion, while the non-linear terms are calculated on the grid.

### Spectral Expansion.

As an expansion function, the spherical harmonic functions TERM00229 and TERM00229, which are eigenfunction of Laplacian on a sphere, are used. However, TERM00230 is used. TERM00231 satisfies the following equation,

     EQ=00039.

Using the Legendre jury function TERM00232 it is written as follows.

     EQ=00040.

However, it is TERM00233.

The expansion by spherical harmonic functions is ,

     EQ=00041.

When I write ,

     EQ=00042.

The inverse of that is ,

     EQ=00056.
     EQ=00056.

The formula is expressed as To evaluate by replacing the integral with a sum, we use the Gauss trapezoidal formula for the TERM00236 integral and the Gauss-Legendre integral formula for the TERM00237 integral. TERM00238 is the Gauss latitude and TERM00239 is the Gauss load. Also, TERM00240 is a grid of evenly spaced Gauss loads.

Using spectral expansion, the grid point values of the terms containing the derivatives can be calculated as follows.

     EQ=00043.

     EQ=00044.

Furthermore, the grid point values of TERM00245 and TERM00245 can be obtained from the spectral components of TERM00243 and TERM00244 as follows

     EQ=00045.

     EQ=00046.

The derivative appearing in the advection term of the equation is calculated as

     EQ=00057.
     EQ=00057.
     EQ=00057.

     EQ=00058.
     EQ=00058.
     EQ=00058.

Furthermore,

     EQ=00047.

to be used for the evaluation of the TERM00248 section.

### Horizontal Diffusion Term

The horizontal diffusion term is entered in the form TERM00249 as follows.

     EQ=00048.

     EQ=00049.

     EQ=00050.

     EQ=00051.

This horizontal diffusion term has strong implications for computational stability. In order to represent selective horizontal diffusion on small scales, 4 TERM00251 16 is used as TERM00250. Here, the extra term for vorticity and divergence diffusion indicates that the term of rigid body rotation in TERM00252 does not decay.

### Spectral representation of equations

1. a series of equations

         EQ=00059.
         EQ=00059.

 Here,

         EQ=00052.

2. equation of motion

         EQ=00060.
         EQ=00060.
         EQ=00060.

         EQ=00061.
         EQ=00061.
         EQ=00061.
         EQ=00061.

 However,

         EQ=00053.

3. thermodynamic equation

         EQ=00062.
         EQ=00062.
         EQ=00062.
         EQ=00062.

 However,

         EQ=00054.

4. water vapor formula

         EQ=00063.
         EQ=00063.
         EQ=00063.
         EQ=00063.

 However,

         EQ=00055.