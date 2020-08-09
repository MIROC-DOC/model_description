## Solving the diffuse balance equation for atmospheric and surface systems

### Basic Solutions.

Some of the terms in the radiation, vertical diffusion, and boundary layer and surface processes are treated as implicit terms, and the time integration is performed at the end of the calculation. As the time-varying term for the vector quantity <span>q</span>, we divide it into two terms, TERM01072 for the Euler method and TERM01073 for the implicit method.

     EQ=00428.

Although this is difficult to solve in the general case, it can be approximated by linearizing TERM01074.

     EQ=00429.

and linearize it using the matrix TERM01075 as where ,

     EQ=00430.

but if you write TERM01076 Then write TERM01076,

     EQ=00431.

It is easy to solve in principle by matrix operations.

### Fundamental Equations.

The equations for radiation, vertical diffusion, and ground boundary layer/surface processes are basically expressed as follows.

     EQ=00479.
     EQ=00479.
     EQ=00479.
     EQ=00479.
     EQ=00479.

where TERM01077 and TERM01077 are the vertical energy flux densities of the vertical diffusion fluxes of TERM01078 and TERM01078, respectively. TERM01079 is the vertical upward energy flux density of the vertical diffuse flux density of TERM01078 and TERM01078, respectively.

The atmosphere is discretized using the TERM01080 coordinate system. Wind speed, temperature, etc. are defined by the layer TERM01081. The flux is defined by the layer boundary TERM01082. TERM01083 increases from the lower levels to the upper levels. Also, TERM01084 and TERM01085 are defined in the upper levels. The TERM01086 coordinates can be considered to be the same as those of TERM01088 except for the difference by a constant (TERM01087) factor, as long as we consider a one-dimensional vertical process. Here,

     EQ=00432.

     EQ=00433.

And write .

### implicit time difference

For terms that can be linearized, such as the vertical diffusion term, we use the implicit method. Although the diffusion coefficients depend on the forecast variables, we only obtain the coefficients first and do not solve them iteratively. However, in order to improve the stability of the method, the time step is treated differently (see below).

For example, the discretized equation of TERM01089 (178) is

     EQ=00434.

Here, TERM01090 is a time step. Since TERM01091 etc. is a function of TERM01092, we can linearize its dependence on

     EQ=00435.

Thus, if you put TERM01093,

     EQ=00436.

Namely,

     EQ=00437.

It can be written in the following matrix form

     EQ=00438.

     EQ=00439.

This can be solved by methods such as LU decomposition. Since TERM01094 is usually a triple diagonal, it can be solved easily. After solving the problem, the consistent fluxes are calculated using (534). The same is true for TERM01095.

### implicit time difference coupling

Temperature, specific humidity, and ground temperature are not as simple as those in the previous section.

     EQ=00480.
     EQ=00480.

     EQ=00440.

     EQ=00441.

Note that TERM01096 and TERM01097 in the above equations are taken from TERM01098 and TERM01099. This is because the flux at the earth's surface is as follows.

     EQ=00442.

     EQ=00443.

     EQ=00444.

Assuming that the surface skin temperature is set to TERM01102, TERM01103, TERM01104 (saturated specific humidity), and TERM01105 are all dependent on TERM01106. All of these values depend on the TERM01106. Also, all of the values of TERM01107 depend on the TERM01109.

As with (538), rewriting (539), (540) and (541) using the matrices TERM01110 and TERM01110, in TERM01111 (for TERM01112 and TERM01112) or TERM01113 (for TERM01114),

     EQ=00481.
     EQ=00481.

     EQ=00445.

     EQ=00446.

However,

     EQ=00447.

     EQ=00448.

     EQ=00449.

In case of TERM01115 (for TERM01116 and TERM01116) or TERM01117 (for TERM01118),

     EQ=00482.
     EQ=00482.
     EQ=00482.

     EQ=00450.

     EQ=00483.
     EQ=00483.
     EQ=00483.

However,

     EQ=00451.

     EQ=00452.

     EQ=00453.

However, (553) is a condition for the balance of the ground surface

     EQ=00454.

Note that we have treated the case of TERM01119 in the soil temperature equation, which is not included in the table of (541).

Taking these, (545), (546), (547), (551), (552), and (553) together, we can solve the equations for the TERM01120 unknowns since we have the same number of equations. In practice, the LU decomposition can be used to solve this problem.

After solving the problem, the consistent fluxes should be obtained as in (534).

### Solving the Coupling Formula for Time Difference

(551), etc., can be written as follows.

     EQ=00455.

Here, the terms TERM01121 and TERM01121 are associated with surface fluxes, and the other terms are associated with vertical diffusion. If we reverse the upside-down matrix, we get the following results.

     EQ=00456.

For the sake of brevity, we shall now refer to this document as TERM01122. The following discussion will not lose its generality.

     EQ=00457.

Let us consider the equation for TERM01123 and TERM01123 (which corresponds to the case where flux exchange at the surface is not considered), which is solved by the LU decomposition.

     EQ=00458.

LU. Take it apart,

     EQ=00459.

Now..,

     EQ=00460.

for TERM01124 (which can be easily solved by starting from TERM01125), and then,

     EQ=00461.

for TERM01126, starting from TERM01127, and solving in sequence.

For TERM01128 and TERM01128, the LU decomposition is

     EQ=00462.

Now..,

     EQ=00463.

However, comparing this with (563), we see the following relationship.

     EQ=00464.

With this,

     EQ=00465.

The result is That is, ,

     EQ=00466.

Note that TERM01129 and TERM01130 can be obtained by the LU decomposition with the equation (561) of TERM01131, i.e., without considering the surface flux term. The physical meaning of these terms is that in the flux exchange process with the ground surface, the entire atmosphere has a heat capacity TERM01132, and can be regarded as a layer whose flux TERM01133 is supplied from above.

In (545) and (551), (546) and (552), (547) and (553), respectively, the equation corresponding to (569) is obtained, which is as follows.

     EQ=00467.

     EQ=00468.

     EQ=00469.

Therefore, by concatenating the above three expressions, we can solve for the unknown variables TERM01134 and TERM01134. Once these are solved, we can then solve for (568) as TERM01135 and TERM01135. After that, we can apply a consistent flux to the obtained temperatures and

     EQ=00484.
     EQ=00484.

and compute it as Although we have shown that TERM01136 is a general matrix, it is simpler since it is actually a triple-diagonal matrix.

In the program, `MODULE:[VFTND1(pimtx.F)]` for the atmospheric part and `MODULE:[GNDHT1(pggnd.F)]` for the underground part, the first half of the LU decomposition method (where TERM01137 is obtained) is performed, and in `MODULE:[ SLVSFC(pgslv.F)]`, the equation of TERM01138 is solved, and TERM01139 and TERM01139 are obtained. Then, in `MODULE:[GNDHT2(pggnd.F)]`, we perform the latter half of the LU decomposition method, solve for the temperature coefficient of variation for the ground, and correct the fluxes so that the convergence of the two equations agrees with each other. In `MODULE:[VFTND2(pimtx.F)]`, the temperature coefficient of variation is solved for the atmosphere, and the fluxes are corrected with `MODULE:[FLXCOR(pimtx.F)]`.

### Combined expression for time difference

The concatenation formula for TERM01140 and TERM01140 is solved three times with different conditions as follows.

Solve for surface wetness TERM01141 as 1. Surface temperature is a variable.

2. the solution is based on the surface moisture content obtained by `MODULE:[GNDBET]`. The surface temperature is a variable.

3. the solution is given by the surface moisture content obtained by `MODULE:[GNDBET]`. In the case of snow melting, etc., the surface temperature is fixed at the freezing point.

The first calculation is performed to estimate the possible evaporation rate (TERM01142). (When the surface wetness is small, diagnosing the possible evaporation rate as TERM01144 using TERM01143 obtained from the model energy balance will result in an unrealistically large value.) The possible evaporation rate is defined as,

     EQ=00485.

It becomes The subscript TERM01145 means, after correction, that this is a consistent flux for the temperature etc. obtained.

In the second and subsequent calculations ,

The value of evaporation (TERM01146) multiplied by the value of possible evaporation determined in the first calculation is the value of evaporation (TERM01147).

         EQ=00470.

2. evaporation rate TERM01148 is

         EQ=00471.

 The energy balance is again rebalanced as required by

There are two ways of calculating the evaporation rate, i.e., (1) and (2) (the standard method is used in this case). The third calculation is performed in order to fix the surface temperature at the freezing point, etc. during snow and ice melt or sea ice formation in the mixed layer oceans in order to solve the energy balance. The amount of energy used for the phase change of water is diagnostically determined and is used to calculate the amount of snowmelt later.

The concrete form of the coupling formula is as follows.

     EQ=00486.
     EQ=00486.

Here, TERM01150, TERM01150, and TERM01151 and TERM01151 are components of the matrices and vectors obtained by the first half of the LU decomposition method. When the ground surface is covered with snow or ice, the sublimation latent heat TERM01153 is used instead of the latent heat TERM01152. TERM01154 is the latent heat of the melting of water. However, in the second calculation, if the first method is used to estimate evaporation, the result will be as follows.

     EQ=00487.
     EQ=00487.

In the third calculation, the concatenation equation for a fixed surface temperature is

     EQ=00488.
     EQ=00488.

Here, TERM01155 is the rate of change to the temperature to be fixed,

     EQ=00472.

The value of TERM01156 is 273.15 K for snow and ice melt, and 271.15 K for sea ice formation. When the second method of evaporation calculation is used, TERM01158 is used instead of TERM01157, and the differential term of TERM01159 is set to zero. In this case, the differential term of TERM01159 is set to zero,

     EQ=00489.
     EQ=00489.

TERM01160, which is calculated by TERM01160, is the surface energy balance and is the energy used for the water phase change.

### implicit Treatment of Time Steps in Time Differences

Although the implicit method is used for the time difference of the vertical diffusion term, the diffusion coefficients are generally nonlinear, and the explicit evaluation of these coefficients may lead to numerical instability problems. In order to improve the stability, we follow Kalnay and Kanamitsu (19?) in treating the time step as in Kalnay and Kanamitsu (19?). In order to improve the stability, we follow Kalnay and Kanamitsu (19?) in treating the time step.

For simplicity, we will take the following ordinary differential equations as an example.

     EQ=00473.

The coefficient TERM01161 expresses the nonlinearity. Evaluating only the coefficients explicitly and making them implicitly differential, we obtain the following equation.

     EQ=00474.

However, consider the value of TERM01162 two steps ahead, TERM01163,

     EQ=00475.

     EQ=00476.

and (586). In general, (585) and (586) are known to be more stable than (584).

By rewriting (585) and (586) into a form for determining the rate of change over time, we obtain the following.

     EQ=00477.

     EQ=00478.

In other words, the time step in determining the rate of change is twice the time integration step.