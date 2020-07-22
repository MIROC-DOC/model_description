## Vertical discretization

According to Arakawa and Suarez (1983),
The basic equations are discretized vertically by differences.
This scheme has the following features.

  - Conservation of the total domain-integrated mass

  - Save the total integrated energy

  - Preserving angular momentum for global integration

  - Conservation of total mass-integrated potential temperature

  - The hydrostatic pressure equation comes down to local (the altitude of the lower level is independent of the temperature of the upper level)

  - Constant in the horizontal direction, for a given temperature distribution,
    The hydrostatic pressure equation becomes accurate and the barometric gradient force becomes zero.

  - The isothermal atmosphere stays at the isothermal level indefinitely

### How to take a level.

Number the layers from the bottom to the top.
Assume that the physical quantity of TERM00000 and TERM00000 is defined in terms of integer levels (layers).
On the other hand, TERM00001 is defined by the half-integer level (level).
First, let the value of TERM00002 at the half-integer level be
TERM00003,TERM00003
is defined.
except that level TERM00004 is the lower end (TERM00005),
Level TERM00006 should be the uppermost (TERM00007).

The value of TERM00008 for an integer level
TERM00009,TERM00009
is found by the following formula.

> EQ=00000.
> <span id="Bear definition" label="Bear definition">\blindness\.0000

Furthermore,

> EQ=00001.
> <span id="sigma thickness" label="sigma thickness">Sigma thickness\[sigma thickness]</span>

.

### vertical discretization representation.

The discretized representation of each equation is as follows.

The equation of continuity, vertical velocity

    > EQ=00002.

    > EQ=00003.

    > EQ=00004.

2. hydrostatic pressure equation

    > EQ=00010.  
    > EQ=00010.

    > EQ=00011.  
    > EQ=00011.

    Here ,

    > <span id="Hydrostatic pressure coefficient" label="Hydrostatic pressure coefficient">Are you sure you can't take a look at it?
    > EQ=00012.  
    > EQ=00012.

3. equation of motion

    > EQ=00005.
    > <span id="Vorticity After All" label="Vorticity After All">\\\.com\.} </span>.

    > EQ=00006.

    Here,

    > EQ=00013.  
    > EQ=00013.

    > EQ=00014.  
    > EQ=00014.

    > <span id="Hatchetkappa" label="Hatchetkappa">\\blade\.com\blade\bladeCoCoCoCo.} </span>.
    > EQ=00015.  
    > EQ=00015.

    > EQ=00007.

4. thermodynamic equation

    > EQ=00016.  
    > EQ=00016.  
    > EQ=00016.

    Where ,

    > EQ=00017.  
    > EQ=00017.  
    > EQ=00017.  
    > EQ=00017.  
    > EQ=00017.  
    > EQ=00017.  
    > EQ=00017.

    > EQ=00018.  
    > EQ=00018.

    > <span id="Temperature Interpolation Factor" label="Temperature Interpolation Factor">\\BackBackBacklash\.com
    > EQ=00019.  
    > EQ=00019.

5. water vapor formula

    > EQ=00008.
    > <span id="q eventually" label="q eventually" label="q eventually">\\blana[q eventually]</span>

    > EQ=00009.
