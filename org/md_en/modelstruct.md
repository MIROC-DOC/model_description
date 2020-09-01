# Model Configuration.

## Composition Overview.

The AGCM programs are organized in a hierarchical structure, and are managed in several directories, each of which is divided into several files. Each file (package) contains several program modules (subroutines and functions), and in some cases, each module has several entries.

Example:

<span>**directory**</span>**dynamics: **
<span>**File**</span>**dadmn.F: **DADMN.F: ** PACKAGE DADMN
.
<span>**File**</span> **dshpe.F: ** dshpe.F: ** PACKAGE DSPHE
<span>**Module DSETNM: **</span> ̄ <span>**Module W2G**</span> SUBROUTINE W2G
ENTRY G2W
ENTRY SPSTUP
<span>** Module DSETNM:**</span> SUBROUTINE DSETNM

Currently, there are 10 directories as follows

| Header0 | Header1 |
| ------- | ------- |
| admin | Modules related to the structure of the entire model (coordinates, time, constants, etc.) |
| dynamics | Modules related to mechanical processes |
| physics | Modules involved in physical processes |
| io | Modules for data input/output |
| util | General-purpose operation libraries |
| sysdep | system dependent module |
| include | Headers included     by <span>`#include`</span> |
| nonstd | Non-standard plug-in modules |
|  | test module |
| shalo | Module for     single layer barotropic shallow water models (under test) |

Note that the files containing the main routines are located directly under <span>`src/`</span>.

These dependencies are as follows.

| Header0 | Header1 | Header2 | Header3 | Header4 |
| ------- | ------- | ------- | ------- | ------- |
| MAIN | \- Replica Hermes Handbags |  |  |  |
|  | \- Dynamics |  |  |  |
|  | \- Physical properties |  |  |  |
|  |  | \- I'm not sure how to describe it. |  |  |
|  |  |  | \- You can't even tell me how to do it. |  |
|  |  |  |  | \- I'm sure you'll be able to find out more about it in the next few days. |

That is, they are independent of each other, and the one on the left is used to call the one on the right, but not the other way around.

The package contains several closely related routines in a single file. Particularly for the physical processes, it is possible to replace the parameterization by replacing one or a few files.

## Special note on the program.

There are several modules with multiple entries using the ENTRY statement. Its main purpose is to store data locally. For example, in the case of the above mentioned module W2G, variables such as PNM and DPNM are stored as local variables in this module and are commonly used in W2G, G2W, and SPSTUP. Although W2G and G2W are used in many places, this structure avoids the complexity of having to use PNM and DPNM as arguments. Common variables are usually used in such a case. Here, we avoid the COMMON variables as much as possible due to their inconvenience in management and debugging, and use this encapsulation structure instead.

Only two COMMONs are in use.

| Header0 | Header1 |
| ------- | ------- |
| COMMON /COMCON/ | Standard physical constants (earth radius, gas constant, etc.) |
| COMMON /COMWRK/ | work area |

COMCON contains the standard definition of physical constants. This COMMON definition is included in <span>`include/zccom.F`</span>, and is included as necessary. The value is set by calling the subroutine PCONST (<span>`admin/apcon.F`</span>). COMWRK is used as a work area by many modules. It is used to reduce the overall memory consumption and it is not a problem to remove all the corresponding COMMON statements.

The C preprocessor instruction is used for include file inclusion and conditional compilation. F`</span> instead of <span>`.f`</span>. F`&lt;/span&gt;. As a conditional compilation, the selection by <span>`#ifdef`</span> and <span>`#ifndef`</span> is used. The files are fetched from the <span>`inlcude`</span> directory and are as follows.

| Header0 | Header1 |
| ------- | ------- |
| Array size parameter statements | zcdim.F |
|  | zpdim.F |
|  | zidim.F |
|  | zsdim.F |
|  | zhdim.F |
|  | zradim.F |
|  | zwdim.F |
| COMMON definition (physical constants) | zccom.F |
| Statement function definition (saturation ratio humidity) | zqsat.F |

Although the specification of FORTRAN 77 is not in the standard, it uses the NAMELIST reading method, it seems to be usable by most of the systems. For the specification of NAMELIST, please refer to the manual of each system.

## Program Writing.

End-of-line comments are used in various descriptions. `!" ` The comments are at the end of the line below.

All variables are declared. It is assumed that the IMPLICIT NONE (e.g. the <span>`-u`</span> option in Sun's case) is used.

Each entry's argument is accompanied by a continuation line column to explain the function.

| Header0 | Header1 | Header2 | Header3 | Header4 |
| ------- | ------- | ------- | ------- | ------- |
| symbol | meaning | input | Outputs | function |
| O | output | ×impossibility | circle (e.g. of friends) | Generate values |
| M | modify | circle (e.g. of friends) | circle (e.g. of friends) | Processing the input values and outputting them |
| I | input | circle (e.g. of friends) | - | Input value ('variable') |
| C | constant | circle (e.g. of friends) | - | Input value ('constant') |
| D | dimension | circle (e.g. of friends) | - | Variables that determine the size of the matching array |
| W | work | ×impossibility | ×impossibility | work area |
| U | undefined | ×impossibility | ×impossibility | dummy |

where the meaning of the input and output columns is as follows \The entry of a certain type of event in the event of a certain type of event.
     \begin{array}{ll}

 × x & whatever is in it
     \{array}
 \A lot of people could be in a position to be in a position to do something about it     .
     \begin{array}{ll}
 O O & may be subject to change in the course of the event
       - & the value will not change
 × x & I can't guarantee what you'll find
     \{array}
      \The important ones are M,O,I, where the key ones are M,O,I and C,D are a type of I. The use of C,D and I is not so neat. The usage of C,D,I is not so correct.

The contents of each file are as follows.

` *" PACKAGE PSAVE save/load data (real memory version) `
:̄ Package Name
`*" [HIS] 93/11/10(numaguti) AGCM5.3`
Change log
`        SUBROUTINE PGSAVE     !" Internal Data Save `
: Module Declaration
`*    [PARAM]`
The following, parameter statements are (included) followed by
`    * [MODIFY] `
: Declarations of input and output variables
`    * [OUTPUT] `
: the following, output variable declarations
`    * [INPUT] `
: The following, Declarations of Input Variables
`    * [ENTRY OUTPUT] `
: Declare output variables in the entry...
`    * [INTERNAL WORK] `
: Declarations of internal work variables
`*    [INTERNAL SAVE]`
Declarations of internal variables (which should be kept after RETURN)
`*    [INTERNAL PARAM]`
Declarations of internal parameters (to be read by NAMELIST, etc.)
`*    [ONCE]`
The following is the part to be done only once on the first call

Sentence numbers are assigned to each block in the thousands, and are applied as structurally as possible.

## Naming Rules.

The names of variables, entry names, etc. must be six characters or less.

Variable name and type mapping

| Header0 | Header1 |
| ------- | ------- |
| A-G, P-Z | Floating point number (<span>`REAL*8`</span>) |
| H | String (<span>`CHARACTER`</span>) |
| I-N. | Integer (<span>`INTEGER`</span>) |
| O | Logical type (<span>`LOGICAL`</span>) |

However, this may not be the case for variables read by NAMELIST.

Conventions on the Correspondence between Variable Names and Contents

| Header0 | Header1 | Header2 |
| ------- | ------- | ------- |
| Prefix: | GA | The grid point state quantity ($u,v,T,p_S,q,T_g$) |
|  | GB | Grid point state quantity (${\mathcal F}_x,{\mathcal F}_y,Q,S,Q_g$) |
|  | GD | Grid State Quantity (for common use) |
|  | GT | Time differential term of the grid state quantity |
|  | WD | Spectral representation of state quantities |
|  | WT | Spectral representation of the time differential term of the state quantity |
|  | I | Longitude index |
|  | J | Index of latitude |
|  | K | Index for vertical level |
|  | IJ | An index of all the latitudes and longitudes in one place |
|  | NM. | Index of the spectrum |
|  | NM. | NAMELIST Name |
|  | COM | COMMON Name |
| Tangent: | U | east-west wind |
|  | V | north-south wind |
|  | T | temperature |
|  | PS | surface pressure |
|  | Q | Specific humidity, various tracers |
|  | QL | cloud liquidity |
|  | FLX,FLUX | flux density |
|  | MTX | Matrices for implicit solutions |
|  | MAX | data length |
|  | DIM | Size of the array region |

As for the file names, the first letter is the first letter of the directory (although <span>`include`</span> is <span>`z`</span>). Also, <span>`-admn`</span>(admin) indicates the main module in it.

This COMMON is actually ungrammatical. The size of the common block by the COMMON statement must be the same (an unnamed common block is acceptable). We are going to change this in the near future.

The reason for using two characters here, not just `! The reason for using two characters and not just `! ` to ensure substitution for systems with other end-of-line comment formats (e.g., HITAC VOS3), and because Sun's CPP will malfunction if there is only
