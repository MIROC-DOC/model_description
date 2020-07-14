*** sample script for grads ***
* command to draw:
* gradsgt -blc draw.gs 
*
*** VAR ***
* surface air temperature
 var='t2' ; unit='degC' ; anom=273.15
*
*** EXP & DIR ***
 exp='ERA-interim'
*
 datdir='./dat'
 picdir='./pic'
'!if ! test -e 'picdir'; then mkdir 'picdir' ; fi'
*
*** SET COLOR ***
 colno=1
*label color(black)
 labelc=1
*label thickness
 labelt=6
*label size
 labels=0.15
*place colorbar
 cbxmin=2.0 ; cbxmax=9.0 ; cbymin=0.5 ; cbymax=0.75
*
*** MAP AREA ***
 latmin=-90 ; latmax=90 ; lonmin=0 ; lonmax=360
 if(latmin=-90&latmax=90) ; latlabs='S90|S60|S30|EQ|N30|N60|N90' ; endif
 if(lonmin=0&lonmax=360)  ; lonlabs='0|60E|120E|180|120W|60W|0'  ; endif
*
*** DRAW ***
 'reinit' 
  filen=''datdir'/'var'.ctl'
 'open 'filen''
*
  t=1 ; tmax=365
*
while(t<tmax+1)
 'c'
 'set grads off'
 'set display color white'
 'colorset.gs'
 'set grid off'
 'set parea 1.5 10.5 1.5 7'
*
 'set gxout shaded'
 'set t 't'' 
 'set xlopts 'labelc' 'labelt' 'labels''
 'set ylopts 'labelc' 'labelt' 'labels''
 'set lat 'latmin' 'latmax''
 'set lon 'lonmin' 'lonmax''
 'set xlab on'
 'set ylab on'
 'set xlabs 'lonlabs''
 'set ylabs 'latlabs''
*
 'set clevs  -50 -40 -30 -20 -10 -5 0 5 10 15 20 25 30 35'
 'd 'var'-'anom'' 
 'draw title 'var' ('unit'), day='t', 'exp''
 'cbarn'
*
  if(t<10)       ; 'printim 'picdir'/'var'-00't'_'exp'.png' ; endif
  if(t>9&t<100)  ; 'printim 'picdir'/'var'-0't'_'exp'.png'  ; endif
  if(t>99)       ; 'printim 'picdir'/'var'-'t'_'exp'.png'   ; endif
*
  t=t+1
*
endwhile
*
*** END GrADS ***
 'quit'
