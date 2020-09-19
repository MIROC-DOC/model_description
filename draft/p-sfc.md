# Surface (地表)
## 本章でとりあげる or 関連するプログラム
**contents** are just quoted by the programs.

| module name      | file name            | contents                          | subroutines |
|:-----------------|:---------------------|:------------------------------------------------|
| `MODULE:[PLAND]` | `./physics/pglnd.F ` | land surface                                    |
| `MODULE:[POCEN]` | `./physics/pgocn.F`  | mixed layer/fixed SST ocean                     |
| `MODULE:[PGRIV]` | `./physics/pgriv.F ` | |river routing submodel                         |
| `MODULE:[PGSFC]` | `./physics/pgsfc.F ` | surface driver                                  |
| `MODULE:[PSFCL]` | `./physics/psfcl.F`  | surface bulk transfer coefficient               |
| `MODULE:[PSFCM]` | `./physics/psfcm.F`  | surface fluxes                                  |

### SUBROUTINES

#### `MODULE:[PLAND]` (./physics/pglnd.F)

| routine name | contents                           |
|:-------------|:-----------------------------------|
| `LAND`       | land driver                        |
| `LNDSLV`     | surface temperature                |
| `LNDSUB`     | land surface                       |
| `LNDIMP`     | change in underground values       |
| `GRWNML`     | file of surface parameter          |
| `PGPGET`     | set surface parameters             |
| `LSETCO`     | coordinates of submodel            |
| `SETGLV`     | set land vartical coordinates      |
| `SETGL`      | vertical coordinates               |
| `LRSTRT`     | read land initial values           |
| `LCHKV`      | valid range monitor                |
| `SETDTL`     | land time step (dummy for matsiro) |


#### `MODULE:[POCEN]` (./physics/pgocn.F)

| routine name  | contents                               |
|:--------------|:---------------------------------------|
| `OCEAN`       | mixed layer ocean driver               |
| `OCNSLV`      | surface temperature                    |
| `OCNSUB`      | mixed layer ocean                      |
| `ICEADJ`      | ice/temp. adjustment                   |
| `OSETCO`      | --                                     |
| `SEAALB`      | sea surface albedo                     |
| `SEAZ0F`      | roughness of ocean (flux dependent)    |
| `TICEMG`      | merge two different ice data, and etc. |
| `TICEMG2`     | --                                     |
| `ORSTRT`      | read physical initial value            |
| `OCHKV`       | valid range monitor                    |
| `OCEAN_DUMMY` | --                                     |


#### `MODULE:[PGRIV]` (./physics/pgriv.F)

| routine name | contents          |
|:-------------|:------------------|
| `RIVER`      | river routing     |
| `RIVDST`     | river destination |



#### `MODULE:[PGSFC]` (./physics/pgsfc.F)

| routine name | contents       |
|:-------------|:---------------|
| `SURFCE`     | surface driver |
| `RADSFC`     | --             |


#### `MODULE:[PSFCL]` (./physics/psfcl.F)

| routine name | contents                  |
|:-------------|:--------------------------|
| `BLKCOF`     | bulk transfer coefficient |

## Surface fluxes (地表フラックス)

### Basic information
`MODULE:[PSFCM]` (./physics/psfcm.F)

| routine name | contents     |
|:-------------|:-------------|
| `SFCFLX`     | surface flux |

 `[HIS]
07/10/04 Suzuki Tatsuo: use ocean velocity for CPL by H.Tatebe`
