# Description of the program code

## The Basics of Reading Programs.

### Configuration Overview.

The AGCM program body has a hierarchical structure,
The files are maintained in multiple directories, each of which is divided into multiple files.
A single file (package) can contain ,
In addition, there are several program modules (subroutines and functions) in the package,
In some cases, there may be multiple entries in a module.

Example:

<span>**directory**</span>**dynamics: **
<span>**File**</span> **dadmn.F: **
\blanket* Package DADMN
.
<span>**File**</span> **dshpe.F: **
\blanket* Package DSPHE
<span>** Module DSETNM: **</span>̄
<span>**Module W2G**</span>
SUBROUTINE W2G
ENTRY G2W
ENTRY SPSTUP
<span>** Module DSETNM:**</span> SUBROUTINE DSETNM

### Directory Structure.

Currently, there are 9 directories as follows

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

That is, each of them is independent of the others in the same row,
The one on the left is used to call the one on the right, but the reverse is not allowed.

Several closely related routines in one file (package).
Particularly in the physical process, the replacement of one or a few files with
The use of parameterization is possible.

### Special Notes on the Program.

There are several modules that have multiple entries using the ENTRY statement.
 Its main purpose is the local storage of data.
 For example, in the case of the module W2G above, the variables PNM and DPNM are
 It is stored as a local variable in this module,
 Commonly used in     W2G, G2W and SPSTUP.
     W2G and G2W are used in many places, but this structure makes it possible for them to be used in various ways,
 This avoids the complexity of having to use     PNM and DPNM as arguments.
 The COMMON variable is usually used in such cases.
 Here, the COMMON variable is used as an inconvenience for management and debugging.
 We avoid this type of encapsulation structure as much as possible and instead use such an encapsulated structure.

Only two COMMONs are in use.

| Header0 | Header1 |
| ------- | ------- |
| COMMON /COMCON/ | Standard physical constants (earth radius, gas constant, etc.) |
| Anonymous COMMON | work area |

     COMCON contains the standard physical constants.
 This COMMON definition is in <span>`include/zccom.F`</span>,
 It is used to include as necessary.
 The value is set by calling the subroutine PCONST (<span>`admin/apcon.F`</span>).
 An unnamed COMMON block is used as a work area from many modules.
 It is used to reduce the overall memory consumption.
 Deleting all the relevant COMMON statements does not have a problem as it only affects the amount of memory.

For include file inclusion and conditional compilation
 It uses the     C preprocessor instruction.
 F`</span> instead of <span>`.f`</span>, so the file name is <span>`.
 As a conditional compilation,
 Using selection by     <span>`#ifdef`</span> and <span>`#ifndef`</span>.
 Files are imported from the <span>`inlcude`</span> directory,
 It is as follows.

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

FORTRAN 77 As a non-standard specification ,
 I'm using     NAMELIST reading,
 It seems to be able to be used in many processing systems without any problem.
 For the specifications of     NAMELIST, please refer to the manual of each system.

### Program Writing.

1. end-of-line comments are used in various explanations.
     `!" ` The end of the line below is a comment
     \0.1[1\].

All variables are declared. 2.
     IMPLICIT NONE (e.g., the <span>`u`</span> option for Sun) is set to
 It is a prerequisite for use.

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

 Here, the meaning of the input and output columns is as follows
     \In the meantime, I'm going to be in a position to take a look at some of the things I've done in the past.
         \begin{array}{ll}

 × x & whatever is in it
         \{array}


         \begin{array}{ll}
 O O & may be subject to change in the course of the event
           - & the value will not change
 × x & I can't guarantee what you'll find
         \{array}

 The important ones are M,O,I, where M,O and I are important, and C,D are a type of I.
 The use of     C, D, and I is not so neat.

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
 The following is     the part to be done only once on the first call

Sentence numbers are assigned to each block in the thousands,
 I'm guessing as structurally as possible.

### Naming Conventions.

The names of variables, entry names, etc. must be six characters or less.

2. variable name and type mapping

| Header0 | Header1 |
| ------- | ------- |
| A-G, P-Z | Floating point number (<span>`REAL*8`</span>) |
| H | String (<span>`CHARACTER`</span>) |
| I-N. | Integer (<span>`INTEGER`</span>) |
| O | Logical type (<span>`LOGICAL`</span>) |

 However, in the variables read by NAMELIST,
 This may not be met.

Conventions on the correspondence between variable names and contents

| Header0 | Header1 | Header2 |
| ------- | ------- | ------- |
| Prefix: | GA | The grid point state quantity ($t$) |
|  | GB | Grid point state quantity ($t-\Delta t$) |
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

For file names,
 The     first letter is unified to the first letter of the directory.
     (However, <span>`include`</span> is <span>`z`</span>.)
 Also, <span>`-admn`</span>(admin) indicates the main module in it.

<! -- end list -->!

The reason for the use of two characters here, not just `! I use two letters as well as `!
 Systems that use other end-of-line comment formats (e.g. HITAC VOS3)
 to ensure substitution for, and
     The reason for this is that Sun's CPP will malfunction if you use only `! is because Sun's CPP will malfunction if there is only `!
