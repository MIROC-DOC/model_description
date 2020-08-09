# Description of the program code

## The Basics of Reading Programs.

### Configuration Overview.

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

### Directory Structure.

Currently, there are 9 directories as follows

 - TAB00005:0.0
     admin

 - TAB00005:0.1
 Modules related to the structure of the entire model (coordinates, time, constants, etc.)

 - TAB00005:1.0
     dynamics

 - TAB00005:1.1
 Modules related to mechanical processes

 - TAB00005:2.0
     physics

 - TAB00005:2.1
 Modules involved in physical processes

 - TAB00005:3.0
     io

 - TAB00005:3.1
 Modules for data input/output

 - TAB00005:4.0
     util

 - TAB00005:4.1
 General-purpose operation libraries

 - TAB00005:5.0
     sysdep

 - TAB00005:5.1
 system dependent module

 - TAB00005:6.0
     include

 - TAB00005:6.1
 Headers included     by <span>`#include`</span>

 - TAB00005:7.0
     nonstd

 - TAB00005:7.1
 Non-standard plug-in modules

 - TAB00005:8.0
     special

 - TAB00005:8.1
 test module

Note that the files containing the main routines are located directly under <span>`src/`</span>.

These dependencies are as follows.

 - TAB00006:0.0
     MAIN

 - TAB00006:0.1
     \- Replica Hermes Handbags

 - TAB00006:0.2

 - TAB00006:1.0

 - TAB00006:1.1
     \- Dynamics

 - TAB00006:1.2

 - TAB00006:2.0

 - TAB00006:2.1
     \- Physical properties

 - TAB00006:2.2

 - TAB00006:3.0

 - TAB00006:3.1

 - TAB00006:3.2
     \- I'm not sure how to describe it.

 - TAB00006:3.3

 - TAB00006:4.0

 - TAB00006:4.1

 - TAB00006:4.2

 - TAB00006:4.3
     \- You can't even tell me how to do it.

 - TAB00006:4.4

 - TAB00006:5.0

 - TAB00006:5.1

 - TAB00006:5.2

 - TAB00006:5.3

 - TAB00006:5.4
     \- I'm sure you'll be able to find out more about it in the next few days.

That is, they are independent of each other, and the one on the left is used to call the one on the right, but not the other way around.

The package contains several closely related routines in a single file. Particularly for the physical processes, it is possible to replace the parameterization by replacing one or a few files.

### Special Notes on the Program.

There are several modules that have multiple entries using ENTRY statement. Its main purpose is to keep the data local. For example, in the case of the above mentioned module W2G, variables such as PNM and DPNM are stored as local variables in this module and are commonly used in W2G, G2W, and SPSTUP. Although W2G and G2W are used in many places, this structure avoids the complexity of having to use PNM and DPNM as arguments. Common variables are usually used in such a case. Here, we avoid the COMMON variables as much as possible due to their inconvenience in management and debugging, and use this encapsulation structure instead.

Only two COMMONs are in use.

       - TAB00007:0.0
         COMMON /COMCON/

       - TAB00007:0.1
 Standard physical constants (earth radius, gas constant, etc.)

       - TAB00007:1.0
 Anonymous COMMON

       - TAB00007:1.1
 work area

     COMCON contains the standard definition of physical constants. This COMMON definition is included in <span>`include/zccom.F`</span>, and is included as necessary. The value is set by calling the subroutine PCONST (<span>`admin/apcon.F`</span>). An unnamed COMMON block is used as a work area by many modules. It is used to reduce the overall memory consumption. Removing all the corresponding COMMON statements does not have a problem as it only affects the amount of memory.

The C preprocessor instruction is used for include file inclusion and conditional compilation. F`</span> instead of <span>`.f`</span>. F`&lt;/span&gt;. As a conditional compilation, the selection by <span>`#ifdef`</span> and <span>`#ifndef`</span> is used. The files are fetched from the <span>`inlcude`</span> directory and are as follows.

       - TAB00008:0.0
 Array size parameter statements

       - TAB00008:0.1
         zcdim.F

       - TAB00008:1.0

       - TAB00008:1.1
         zpdim.F

       - TAB00008:2.0

       - TAB00008:2.1
         zidim.F

       - TAB00008:3.0

       - TAB00008:3.1
         zsdim.F

       - TAB00008:4.0

       - TAB00008:4.1
         zhdim.F

       - TAB00008:5.0

       - TAB00008:5.1
         zradim.F

       - TAB00008:6.0

       - TAB00008:6.1
         zwdim.F

       - TAB00008:7.0
         COMMON definition (physical constants)

       - TAB00008:7.1
         zccom.F

       - TAB00008:8.0
 Statement function definition (saturation ratio humidity)

       - TAB00008:8.1
         zqsat.F

Although the specification of FORTRAN 77 is not in the standard, we use the NAMELIST reading method, it seems to be usable in many systems. For the specification of NAMELIST, please refer to the manual of each system.

### Program Writing.

1. end-of-line comments are used for various explanations. `!" The following comments are at the end of the line

All variables are declared. It is assumed that the IMPLICIT NONE (e.g. <span>`-u`</span> option in Sun's case) is used.

Each entry's argument is accompanied by a continuation line column to explain the function.

       - TAB00009:0.0
 symbol

       - TAB00009:0.1
 meaning

       - TAB00009:0.2
 input

       - TAB00009:0.3
 Outputs

       - TAB00009:0.4
 function

       - TAB00009:1.0
         O

       - TAB00009:1.1
         output

       - TAB00009:1.2
         ×impossibility

       - TAB00009:1.3
 circle (e.g. of friends)

       - TAB00009:1.4
 Generate values

       - TAB00009:2.0
         M

       - TAB00009:2.1
         modify

       - TAB00009:2.2
 circle (e.g. of friends)

       - TAB00009:2.3
 circle (e.g. of friends)

       - TAB00009:2.4
 Processing the input values and outputting them

       - TAB00009:3.0
         I

       - TAB00009:3.1
         input

       - TAB00009:3.2
 circle (e.g. of friends)

       - TAB00009:3.3
         -

       - TAB00009:3.4
 Input value ('variable')

       - TAB00009:4.0
         C

       - TAB00009:4.1
         constant

       - TAB00009:4.2
 circle (e.g. of friends)

       - TAB00009:4.3
         -

       - TAB00009:4.4
 Input value ('constant')

       - TAB00009:5.0
         D

       - TAB00009:5.1
         dimension

       - TAB00009:5.2
 circle (e.g. of friends)

       - TAB00009:5.3
         -

       - TAB00009:5.4
 Variables that determine the size of the matching array

       - TAB00009:6.0
         W

       - TAB00009:6.1
         work

       - TAB00009:6.2
         ×impossibility

       - TAB00009:6.3
         ×impossibility

       - TAB00009:6.4
 work area

       - TAB00009:7.0
         U

       - TAB00009:7.1
         undefined

       - TAB00009:7.2
         ×impossibility

       - TAB00009:7.3
         ×impossibility

       - TAB00009:7.4
 dummy

 where the meaning of the input and output columns is as follows \The entry of a certain type of event in the event of a certain type of event.
         \begin{array}{ll}

 × x & whatever is in it
         \{array}
 \A lot of people could be in a position to be in a position to do something about it         .
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
 The following is     the part to be done only once on the first call

Sentence numbers are assigned to each block in the thousands, and are applied as structurally as possible.

### Naming Conventions.

The names of variables, entry names, etc. must be six characters or less.

2. variable name and type mapping

       - TAB00010:0.0
         A-G, P-Z

       - TAB00010:0.1
 Floating point number (<span>`REAL*8`</span>)

       - TAB00010:1.0
         H

       - TAB00010:1.1
 String (<span>`CHARACTER`</span>)

       - TAB00010:2.0
         I-N.

       - TAB00010:2.1
 Integer (<span>`INTEGER`</span>)

       - TAB00010:3.0
         O

       - TAB00010:3.1
 Logical type (<span>`LOGICAL`</span>)

 However, this may not be the case for variables read by NAMELIST.

Conventions on the correspondence between variable names and contents

       - TAB00011:0.0
 Prefix:

       - TAB00011:0.1
         GA

       - TAB00011:0.2
 Grid State Quantity (TERM01202)

       - TAB00011:1.0

       - TAB00011:1.1
         GB

       - TAB00011:1.2
 Grid State Quantity (TERM01203)

       - TAB00011:2.0

       - TAB00011:2.1
         GD

       - TAB00011:2.2
 Grid State Quantity (for common use)

       - TAB00011:3.0

       - TAB00011:3.1
         GT

       - TAB00011:3.2
 Time differential term of the grid state quantity

       - TAB00011:4.0

       - TAB00011:4.1
         WD

       - TAB00011:4.2
 Spectral representation of state quantities

       - TAB00011:5.0

       - TAB00011:5.1
         WT

       - TAB00011:5.2
 Spectral representation of the time differential term of the state quantity

       - TAB00011:6.0

       - TAB00011:6.1
         I

       - TAB00011:6.2
 Longitude index

       - TAB00011:7.0

       - TAB00011:7.1
         J

       - TAB00011:7.2
 Index of latitude

       - TAB00011:8.0

       - TAB00011:8.1
         K

       - TAB00011:8.2
 Index for vertical level

       - TAB00011:9.0

       - TAB00011:9.1
         IJ

       - TAB00011:9.2
 An index of all the latitudes and longitudes in one place

       - TAB00011:10.0

       - TAB00011:10.1
         NM.

       - TAB00011:10.2
 Index of the spectrum

       - TAB00011:11.0

       - TAB00011:11.1
         NM.

       - TAB00011:11.2
         NAMELIST Name

       - TAB00011:12.0

       - TAB00011:12.1
         COM

       - TAB00011:12.2
         COMMON Name

       - TAB00011:13.0
 Tangent:

       - TAB00011:13.1
         U

       - TAB00011:13.2
 east-west wind

       - TAB00011:14.0

       - TAB00011:14.1
         V

       - TAB00011:14.2
 north-south wind

       - TAB00011:15.0

       - TAB00011:15.1
         T

       - TAB00011:15.2
 temperature

       - TAB00011:16.0

       - TAB00011:16.1
         PS

       - TAB00011:16.2
 surface pressure

       - TAB00011:17.0

       - TAB00011:17.1
         Q

       - TAB00011:17.2
 Specific humidity, various tracers

       - TAB00011:18.0

       - TAB00011:18.1
         QL

       - TAB00011:18.2
 cloud liquidity

       - TAB00011:19.0

       - TAB00011:19.1
         FLX,FLUX

       - TAB00011:19.2
 flux density

       - TAB00011:20.0

       - TAB00011:20.1
         MTX

       - TAB00011:20.2
 Matrices for implicit solutions

       - TAB00011:21.0

       - TAB00011:21.1
         MAX

       - TAB00011:21.2
 data length

       - TAB00011:22.0

       - TAB00011:22.1
         DIM

       - TAB00011:22.2
 Size of the array region

As for the file names, the first letter is the first letter of the directory (although <span>`include`</span> is <span>`z`</span>). Also, <span>`-admn`</span>(admin) indicates the main module in it.

<! -- end list -->!

The reason for using two characters here, not just `! The reason for using two characters and not just `! ` to ensure substitution for systems with other end-of-line comment formats (e.g., HITAC VOS3), and because Sun's CPP will malfunction if there is only