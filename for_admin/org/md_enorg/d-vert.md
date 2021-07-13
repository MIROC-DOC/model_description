## Vertical discretization

Following Arakawa and Suarez (1983), the basic equations are discretized vertically by differences. This scheme has the following characteristics.

 - Save the total integrated mass

 - Save the total integrated energy

 - Preserving angular momentum for global integration

 - Conservation of total mass-integrated potential temperature

 - The hydrostatic pressure equation comes down to local (the altitude of the lower level is independent of the temperature of the upper level)

 - For a given temperature distribution, constant in the horizontal direction, the hydrostatic pressure equation becomes accurate and the barometric gradient force becomes zero.

 - Isothermal atmosphere stays isothermal forever

### How to take a level.

Number the layers from the bottom to the top. We assume that the physical quantity in TERM00210 and TERM00210 is defined in terms of integer levels (layers). On the other hand, TERM00211 is defined at the half-integer level (level). First, define the value of TERM00212 at a half-integer level TERM00213,TERM00213. However, the level TERM00214 is the lower end (TERM00215) and the level TERM00216 is the upper end (TERM00217).

The value of TERM00218 at the integer level TERM00219,TERM00219 is calculated by the following formula.

     EQ=00019.

Furthermore,

     EQ=00020.

.

### Vertical discretization representation.

The discretized representation of each equation is as follows.

1. continuity formula, vertical velocity

         EQ=00021.

         EQ=00022.

         EQ=00023.

2. hydrostatic pressure formula

         EQ=00029.
         EQ=00029.

         EQ=00030.
         EQ=00030.

 Here,

         EQ=00031.
         EQ=00031.

3. equation of motion

         EQ=00024.

         EQ=00025.

 Here,

         EQ=00032.
         EQ=00032.

         EQ=00033.
         EQ=00033.

         EQ=00034.
         EQ=00034.

         EQ=00026.

4. thermodynamic equation

         EQ=00035.
         EQ=00035.
         EQ=00035.

 Here,

         EQ=00036.
         EQ=00036.
         EQ=00036.
         EQ=00036.
         EQ=00036.
         EQ=00036.
         EQ=00036.

         EQ=00037.
         EQ=00037.

         EQ=00038.
         EQ=00038.

5. water vapor formula

         EQ=00027.

         EQ=00028.