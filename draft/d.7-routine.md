## Computational Flow of Dynamical Core

In this section, calculations of dynamical component based on coding are summarized. `[module name(file name)]`

### Overview of Dynamical Core

1. Calculate dynamical term `[DYNTRM(dterm.F)]`

   1.1 Calculate volticity and divergence on wave space and get grid value. `[G2W, W2G(xdsphe.F)]`

   1.2 Diagnose stream function and potential velocity `[DYNTRM(dterm.F)]`

   1.3 Diagnose surface pressure advection, its tendency & vertical flow `[PSDOT(dgdyn.F)]`

   1.4 Calculate factor for hydrostatic eq. & interporation of temprature on Hybrid coord. `[CFACT(dcfct.F)]`

   1.5 Calculate virtual temprature `[VIRTMD(dvtmp.F)]`

   1.6 Calculate temperature advection `[GRTADV(dgdyn.F)]`

   1.7 Calculate momentum advection `[GRUADV(dgdyn.F)]`

   1.8 Spectral transform of tendency terms `[G2W(xdsphe.F)]`

2. Time integration of equation `DYNSTP(dstep.F)`

   2.1 Calculate tracer transport `[TRACEG(dtrcr.F)]`

   2.2 Time integration on wave space `[TINTGR(dintg.F)]`

   2.3 Time integration of tracer terms `[GTRACE(dtrcr.F)]`

   2.4 Time filter `[DADVNC(dadvn.F)]`

   2.5 Get horizontal wind of grid value from wave space `[W2G(xdsphe.F)]`

   2.6 Correction of pressure-level diffusion `[CORDIF(ddifc.F)]`

   2.7 Correction of horizontal friction heating `[CORFRC(ddifc.F)]`
