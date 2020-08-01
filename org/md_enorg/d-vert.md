## Vertical discretization

According to Arakawa and Suarez (1983),
Discretize the basic equations vertically by differences.
The scheme has the following characteristics.

 - Save the total integrated mass

 - Save the total integrated energy

 - Preserving angular momentum for global integration

 - Conservation of total mass-integrated potential temperature

 - The hydrostatic pressure equation comes down to local (the altitude of the lower level is independent of the temperature of the upper level)

 - Constant in the horizontal direction, for a given temperature distribution,
 The hydrostatic pressure equation becomes accurate and the barometric gradient force becomes zero.

 - Isothermal atmosphere stays isothermal forever

### How to take a level.

Number the layers from bottom to top.
Assume that the physical quantity of TERM00000 and TERM00000 is defined at the integer level (layer).
On the other hand, TERM00001 is defined at the half-integer level.
First, the value of TERM00002 at a half-integer level
TERM00003,TERM00003
Define the .
However, level TERM00004 is the lower end (TERM00005),
Level TERM00006 should be the upper end (TERM00007).

Value of TERM00008 in integer level
TERM00009,TERM00009
is obtained from the following equation.

     EQ=00000.     --- (1)

Furthermore,

     EQ=00001.    --- (2)

.

### Vertical discretization representation.

The discretized representation of each equation is as follows.

1. continuity formula, vertical velocity

         EQ=00002.     --- (3)

         EQ=00003.     --- (4)

         EQ=00004.     --- (5)

2. hydrostatic pressure formula

         EQ=00010.     --- (6)
         EQ=00010.

         EQ=00011.    --- (7)
         EQ=00011.

 Here,

         EQ=00012.    --- (8)
         EQ=00012.    --- (9)

3. equation of motion

         EQ=00005.     --- (10)

         EQ=00006.     --- (11)

 Here,

         EQ=00013.
         EQ=00013.    --- (12)

         EQ=00014.
         EQ=00014.    --- (13)

         EQ=00015.
         EQ=00015.    --- (14)

         EQ=00007.     --- (15)

4. thermodynamic equation

         EQ=00016.
         EQ=00016.
         EQ=00016.    --- (16)

 Here,

         EQ=00017.
         EQ=00017.
         EQ=00017.
         EQ=00017.
         EQ=00017.
         EQ=00017.
         EQ=00017.    --- (17)

         EQ=00018.    --- (18)
         EQ=00018.    --- (19)

         EQ=00019.    --- (20)
         EQ=00019.    --- (21)

5. water vapor formula

         EQ=00008.     --- (22)

         EQ=00009.     --- (23)