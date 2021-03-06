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

 - TAB00000:0.0
     admin

 - TAB00000:0.1
 Modules related to the structure of the entire model (coordinates, time, constants, etc.)

 - TAB00000:1.0
     dynamics

 - TAB00000:1.1
 Modules related to mechanical processes

 - TAB00000:2.0
     physics

 - TAB00000:2.1
 Modules involved in physical processes

 - TAB00000:3.0
     io

 - TAB00000:3.1
 Modules for data input/output

 - TAB00000:4.0
     util

 - TAB00000:4.1
 General-purpose operation libraries

 - TAB00000:5.0
     sysdep

 - TAB00000:5.1
 system dependent module

 - TAB00000:6.0
     include

 - TAB00000:6.1
 Headers included     by <span>`#include`</span>

 - TAB00000:7.0
     nonstd

 - TAB00000:7.1
 Non-standard plug-in modules

 - TAB00000: 8.0
     special

 - TAB00000:8.1
 test module

 - TAB00000:9.0
     shalo

 - TAB00000:9.1
 Module for     single layer barotropic shallow water models (under test)

Note that the files containing the main routines are located directly under <span>`src/`</span>.

These dependencies are as follows.

 - TAB00001:0.0
     MAIN

 - TAB00001:0.1
     \- Replica Hermes Handbags

 - TAB00001:0.2

 - TAB00001:1.0

 - TAB00001:1.1
     \- Dynamics

 - TAB00001:1.2

 - TAB00001:2.0

 - TAB00001:2.1
     \- Physical properties

 - TAB00001:2.2

 - TAB00001:3.0

 - TAB00001:3.1

 - TAB00001:3.2
     \- I'm not sure how to describe it.

 - TAB00001:3.3

 - TAB00001:4.0

 - TAB00001:4.1

 - TAB00001:4.2

 - TAB00001:4.3
     \- You can't even tell me how to do it.

 - TAB00001:4.4

 - TAB00001:5.0

 - TAB00001:5.1

 - TAB00001:5.2

 - TAB00001:5.3

 - TAB00001:5.4
     \- I'm sure you'll be able to find out more about it in the next few days.

That is, they are independent of each other, and the one on the left is used to call the one on the right, but not the other way around.

The package contains several closely related routines in a single file. Particularly for the physical processes, it is possible to replace the parameterization by replacing one or a few files.

## Special note on the program.

There are several modules with multiple entries using the ENTRY statement. Its main purpose is to store data locally. For example, in the case of the above mentioned module W2G, variables such as PNM and DPNM are stored as local variables in this module and are commonly used in W2G, G2W, and SPSTUP. Although W2G and G2W are used in many places, this structure avoids the complexity of having to use PNM and DPNM as arguments. Common variables are usually used in such a case. Here, we avoid the COMMON variables as much as possible due to their inconvenience in management and debugging, and use this encapsulation structure instead.

Only two COMMONs are in use.

 - TAB00002:0.0
     COMMON /COMCON/

 - TAB00002:0.1
 Standard physical constants (earth radius, gas constant, etc.)

 - TAB00002:1.0
     COMMON /COMWRK/

 - TAB00002:1.1
 work area

COMCON contains the standard definition of physical constants. This COMMON definition is included in <span>`include/zccom.F`</span>, and is included as necessary. The value is set by calling the subroutine PCONST (<span>`admin/apcon.F`</span>). COMWRK is used as a work area by many modules. It is used to reduce the overall memory consumption and it is not a problem to remove all the corresponding COMMON statements.

The C preprocessor instruction is used for include file inclusion and conditional compilation. F`</span> instead of <span>`.f`</span>. F`&lt;/span&gt;. As a conditional compilation, the selection by <span>`#ifdef`</span> and <span>`#ifndef`</span> is used. The files are fetched from the <span>`inlcude`</span> directory and are as follows.

 - TAB00003:0.0
 Array size parameter statements

 - TAB00003:0.1
     zcdim.F

 - TAB00003:1.0

 - TAB00003:1.1
     zpdim.F

 - TAB00003:2.0

 - TAB00003:2.1
     zidim.F

 - TAB00003:3.0

 - TAB00003:3.1
     zsdim.F

 - TAB00003:4.0

 - TAB00003:4.1
     zhdim.F

 - TAB00003:5.0

 - TAB00003:5.1
     zradim.F

 - TAB00003:6.0

 - TAB00003:6.1
     zwdim.F

 - TAB00003:7.0
     COMMON definition (physical constants)

 - TAB00003:7.1
     zccom.F

 - TAB00003:8.0
 Statement function definition (saturation ratio humidity)

 - TAB00003:8.1
     zqsat.F

Although the specification of FORTRAN 77 is not in the standard, it uses the NAMELIST reading method, it seems to be usable by most of the systems. For the specification of NAMELIST, please refer to the manual of each system.

## Program Writing.

End-of-line comments are used in various descriptions. `!" ` The comments are at the end of the line below.

All variables are declared. It is assumed that the IMPLICIT NONE (e.g. the <span>`-u`</span> option in Sun's case) is used.

Each entry's argument is accompanied by a continuation line column to explain the function.

 - TAB00004:0.0
 symbol

 - TAB00004:0.1
 meaning

 - TAB00004:0.2
 input

 - TAB00004:0.3
 Outputs

 - TAB00004:0.4
 function

 - TAB00004:1.0
     O

 - TAB00004:1.1
     output

 - TAB00004:1.2
     ×impossibility

 - TAB00004:1.3
 circle (e.g. of friends)

 - TAB00004:1.4
 Generate values

 - TAB00004:2.0
     M

 - TAB00004:2.1
     modify

 - TAB00004:2.2
 circle (e.g. of friends)

 - TAB00004:2.3
 circle (e.g. of friends)

 - TAB00004:2.4
 Processing the input values and outputting them

 - TAB00004:3.0
     I

 - TAB00004:3.1
     input

 - TAB00004:3.2
 circle (e.g. of friends)

 - TAB00004:3.3
     -

 - TAB00004:3.4
 Input value ('variable')

 - TAB00004:4.0
     C

 - TAB00004:4.1
     constant

 - TAB00004:4.2
 circle (e.g. of friends)

 - TAB00004:4.3
     -

 - TAB00004:4.4
 Input value ('constant')

 - TAB00004:5.0
     D

 - TAB00004:5.1
     dimension

 - TAB00004:5.2
 circle (e.g. of friends)

 - TAB00004:5.3
     -

 - TAB00004:5.4
 Variables that determine the size of the matching array

 - TAB00004:6.0
     W

 - TAB00004:6.1
     work

 - TAB00004:6.2
     ×impossibility

 - TAB00004:6.3
     ×impossibility

 - TAB00004:6.4
 work area

 - TAB00004:7.0
     U

 - TAB00004:7.1
     undefined

 - TAB00004:7.2
     ×impossibility

 - TAB00004:7.3
     ×impossibility

 - TAB00004:7.4
 dummy

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

 - TAB00005:0.0
     A-G, P-Z

 - TAB00005:0.1
 Floating point number (<span>`REAL*8`</span>)

 - TAB00005:1.0
     H

 - TAB00005:1.1
 String (<span>`CHARACTER`</span>)

 - TAB00005:2.0
     I-N.

 - TAB00005:2.1
 Integer (<span>`INTEGER`</span>)

 - TAB00005:3.0
     O

 - TAB00005:3.1
 Logical type (<span>`LOGICAL`</span>)

However, this may not be the case for variables read by NAMELIST.

Conventions on the Correspondence between Variable Names and Contents

 - TAB00006:0.0
 Prefix:

 - TAB00006:0.1
     GA

 - TAB00006:0.2
 The grid point state quantity (TERM00000)

 - TAB00006:1.0

 - TAB00006:1.1
     GB

 - TAB00006:1.2
 Grid point state quantity (TERM00001)

 - TAB00006:2.0

 - TAB00006:2.1
     GD

 - TAB00006:2.2
 Grid State Quantity (for common use)

 - TAB00006:3.0

 - TAB00006:3.1
     GT

 - TAB00006:3.2
 Time differential term of the grid state quantity

 - TAB00006:4.0

 - TAB00006:4.1
     WD

 - TAB00006:4.2
 Spectral representation of state quantities

 - TAB00006:5.0

 - TAB00006:5.1
     WT

 - TAB00006:5.2
 Spectral representation of the time differential term of the state quantity

 - TAB00006:6.0

 - TAB00006:6.1
     I

 - TAB00006:6.2
 Longitude index

 - TAB00006:7.0

 - TAB00006:7.1
     J

 - TAB00006:7.2
 Index of latitude

 - TAB00006:8.0

 - TAB00006:8.1
     K

 - TAB00006:8.2
 Index for vertical level

 - TAB00006:9.0

 - TAB00006:9.1
     IJ

 - TAB00006:9.2
 An index of all the latitudes and longitudes in one place

 - TAB00006:10.0

 - TAB00006:10.1
     NM.

 - TAB00006:10.2
 Index of the spectrum

 - TAB00006:11.0

 - TAB00006:11.1
     NM.

 - TAB00006:11.2
     NAMELIST Name

 - TAB00006:12.0

 - TAB00006:12.1
     COM

 - TAB00006:12.2
     COMMON Name

 - TAB00006:13.0
 Tangent:

 - TAB00006:13.1
     U

 - TAB00006:13.2
 east-west wind

 - TAB00006:14.0

 - TAB00006:14.1
     V

 - TAB00006:14.2
 north-south wind

 - TAB00006:15.0

 - TAB00006:15.1
     T

 - TAB00006:15.2
 temperature

 - TAB00006:16.0

 - TAB00006:16.1
     PS

 - TAB00006:16.2
 surface pressure

 - TAB00006:17.0

 - TAB00006:17.1
     Q

 - TAB00006:17.2
 Specific humidity, various tracers

 - TAB00006:18.0

 - TAB00006:18.1
     QL

 - TAB00006:18.2
 cloud liquidity

 - TAB00006:19.0

 - TAB00006:19.1
     FLX,FLUX

 - TAB00006:19.2
 flux density

 - TAB00006:20.0

 - TAB00006:20.1
     MTX

 - TAB00006:20.2
 Matrices for implicit solutions

 - TAB00006:21.0

 - TAB00006:21.1
     MAX

 - TAB00006:21.2
 data length

 - TAB00006:22.0

 - TAB00006:22.1
     DIM

 - TAB00006:22.2
 Size of the array region

As for the file names, the first letter is the first letter of the directory (although <span>`include`</span> is <span>`z`</span>). Also, <span>`-admn`</span>(admin) indicates the main module in it.

This COMMON is actually ungrammatical. The size of the common block by the COMMON statement must be the same (an unnamed common block is acceptable). We are going to change this in the near future.

The reason for using two characters here, not just `! The reason for using two characters and not just `! ` to ensure substitution for systems with other end-of-line comment formats (e.g., HITAC VOS3), and because Sun's CPP will malfunction if there is only