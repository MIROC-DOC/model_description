## Computational flow of dynamical core

In this section, calculations of dynamical component based on coding are summarized. `[module name(file name)]`

### Overview of dynamical core

1. calculate dynamical term `[DYNTRM(dterm.F)]`

   1.1 calculate volticity and divergence on wave space and get grid value. `[G2W, W2G(xdsphe.F)]`

   1.2 diagnose stream function and potential velocity `[DYNTRM(dterm.F)]`

   1.3 diagnose surface pressure advection, its tendency & vertical flow `[PSDOT(dgdyn.F)]`

   1.4 calculate factor for hydrostatic eq. & interporation of temprature on Hybrid coord. `[CFACT(dcfct.F)]`

   1.5 calculate vartual temprature `[VIRTMD(dvtmp.F)]`

   1.6 calculate temperature advection `[GRTADV(dgdyn.F)]`

   1.7 calculate momentum advection `[GRUADV(dgdyn.F)]`

   1.8 spectral transform of tendency terms `[G2W(xdsphe.F)]`

2. Time integration of equation `DYNSTP(dstep.F)`

   2.1 calculate tracer transport `[TRACEG(dtrcr.F)]`

   2.2 time integration on wave space `[TINTGR(dintg.F)]`

   2.3 time integration of tracer terms `[GTRACE(dtrcr.F)]`

   2.4 time filter `[DADVNC(dadvn.F)]`

   2.5 get horizontal wind of grid value from wave space `[W2G(xdsphe.F)]`

   2.6 correction of pressure-level diffusion `[CORDIF(ddifc.F)]`

   2.7 correction of horizontal friction heating `[CORFRC(ddifc.F)]`
