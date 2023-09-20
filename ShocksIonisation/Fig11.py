#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 14:53:51 2022

@author: ben
"""

import pipreadmods as PIPpy
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#fname='../simdata/T_6220_long/Data/' ;xmin=0.0748;xmax=0.08 ;sname='shocksub2_plot_upc.png'; etime=30;T0=6220
#fname='../simdata/isca_midc_ltest/Data/' ;xmin=0.052;xmax=0.074 ;sname='shocksub2_plot_midc.png'; etime=40; T0=5030
#fname='../simdata/isca_lowc_long/Data/' ;xmin=0.04;xmax=0.1 ;sname='shocksub2_plot_lowc.png'; etime=21; T0=5180
#fname='../simdata/T_5300_n_7.5e16/' ;xmin=0.05;xmax=0.08 ;sname='shocksub2_plot_T5300.png'; etime=40;T0=5300
matplotlib.rcParams.update({'font.size': 18})

#ds=PIPpy.pipread(fname,etime)
dsm=PIPpy.pipread('../simdata/MHD_ref/',50)


#Mid-upper chromosphere cases
nelements=7
tprearr=np.empty(nelements)
tpostarr=np.empty(nelements)
tmaxarr=np.empty(nelements)
rarr=np.empty(nelements)
xnarr=np.empty(nelements)
xnparr=np.empty(nelements)
tref=np.empty(nelements)
ionprearr=np.empty(nelements)
recprearr=np.empty(nelements)
ionradprearr=np.empty(nelements)
recradprearr=np.empty(nelements)
ionposarr=np.empty(nelements)
recposarr=np.empty(nelements)
ionradposarr=np.empty(nelements)
recradposarr=np.empty(nelements)
for i in range(0,nelements):
    if i==0:
        fname='../simdata/CorrectedSims/T5000_n7.5e16_t100000/' ;xmin=0.08;xmax=0.12; etime=10;T0=5000
    if i==1:
        fname='../simdata/CorrectedSims/T5400_n7.5e16_t10000/' ;xmin=0.1;xmax=0.15; etime=10;T0=5400
    if i==2:
        fname='../simdata/CorrectedSims/T5600_n7.5e16_t100000/' ;xmin=0.101;xmax=0.105; etime=10;T0=5600
    if i==3:
        fname='../simdata/CorrectedSims/T5800_n7.5e16_t10000/' ;xmin=0.14;xmax=0.147; etime=10;T0=5800
    if i==4:
        fname='../simdata/CorrectedSims/T6000_n7.5e16_t10000/' ;xmin=0.14;xmax=0.15; etime=10;T0=6000
    if i==5:
        fname='../simdata/CorrectedSims/uptestisca/' ;xmin=0.145;xmax=0.1462; etime=50;T0=6220

    
    ds=PIPpy.pipread(fname,etime)
    T1=ds['pr_p'][-1]/ds['ro_p'][-1]*5.0/6.0
    T=ds['pr_p']/ds['ro_p']*5.0/6.0
    tpost=np.interp(xmin,ds['xgrid']/ds['time'],T*T0/T1)
    tpre=np.interp(xmax,ds['xgrid']/ds['time'],T*T0/T1)
    tmax=np.max(T[100:-1]*T0/T1)
    ropost=np.interp(xmin,ds['xgrid']/ds['time'],ds['ro_p']+ds['ro_n'])
    ropre=np.interp(xmax,ds['xgrid']/ds['time'],ds['ro_p']+ds['ro_n'])
    xn=ds['ro_n']/(ds['ro_p']+ds['ro_n'])
    xnparr[i]=np.interp(xmin,ds['xgrid']/ds['time'],xn)
    ionprearr[i]=np.interp(xmax,ds['xgrid']/ds['time'],ds['ion'])
    recprearr[i]=np.interp(xmax,ds['xgrid']/ds['time'],ds['rec'])
    ionradprearr[i]=np.interp(xmax,ds['xgrid']/ds['time'],ds['ion_rad'])
    recradprearr[i]=np.interp(xmax,ds['xgrid']/ds['time'],ds['rec_rad'])
    ionposarr[i]=np.interp(xmin,ds['xgrid']/ds['time'],ds['ion'])
    recposarr[i]=np.interp(xmin,ds['xgrid']/ds['time'],ds['rec'])
    ionradposarr[i]=np.interp(xmin,ds['xgrid']/ds['time'],ds['ion_rad'])
    recradposarr[i]=np.interp(xmin,ds['xgrid']/ds['time'],ds['rec_rad'])

    print(tpre,tpost,tmax,ropost/ropre,xn[-1])
    tprearr[i]=tpre
    tpostarr[i]=tpost
    tmaxarr[i]=tmax
    rarr[i]=ropost/ropre
    xnarr[i]=xn[-1]
    tref[i]=T0
    
###############################################################################
"""#Mid-lower chromosphere cases
nelements2=3
tprearr2=np.empty(nelements2)
tpostarr2=np.empty(nelements2)
tmaxarr2=np.empty(nelements2)
rarr2=np.empty(nelements2)
xnarr2=np.empty(nelements2)
xnparr2=np.empty(nelements2)
tref2=np.empty(nelements2)
ionprearr2=np.empty(nelements2)
recprearr2=np.empty(nelements2)
ionradprearr2=np.empty(nelements2)
recradprearr2=np.empty(nelements2)
ionposarr2=np.empty(nelements2)
recposarr2=np.empty(nelements2)
ionradposarr2=np.empty(nelements2)
recradposarr2=np.empty(nelements2)
for i in range(0,nelements2):
    if i==0:
        fname='../simdata/CorrectedSims/lowisca/';xmin=0.06;xmax=0.12; T0=5180.0; etime=50
    if i==1:
        fname='../simdata/CorrectedSims/T5500_n6.5e18_t100000/' ;xmin=0.07;xmax=0.13; etime=10;T0=5500
    if i==2:
        fname='../simdata/CorrectedSims/T6000_n6.5e18_t100000/' ;xmin=0.05;xmax=0.09; etime=10;T0=6000
#    if i==3:
#        fname='../simdata/CorrectedSims/T6000_n7.5e16_t10000/' ;xmin=0.14;xmax=0.15; etime=10;T0=6000
#    if i==4:
#        fname='../simdata/CorrectedSims/uptestisca/' ;xmin=0.145;xmax=0.1462; etime=50;T0=6220

    
    ds=PIPpy.pipread(fname,etime)
    T1=ds['pr_p'][-1]/ds['ro_p'][-1]*5.0/6.0
    T=ds['pr_p']/ds['ro_p']*5.0/6.0
    tpost=np.interp(xmin,ds['xgrid']/ds['time'],T*T0/T1)
    tpre=np.interp(xmax,ds['xgrid']/ds['time'],T*T0/T1)
    tmax=np.max(T[100:-1]*T0/T1)
    ropost=np.interp(xmin,ds['xgrid']/ds['time'],ds['ro_p']+ds['ro_n'])
    ropre=np.interp(xmax,ds['xgrid']/ds['time'],ds['ro_p']+ds['ro_n'])
    xn=ds['ro_n']/(ds['ro_p']+ds['ro_n'])
    xnparr2[i]=np.interp(xmin,ds['xgrid']/ds['time'],xn)
    ionprearr2[i]=np.interp(xmax,ds['xgrid']/ds['time'],ds['ion'])
    recprearr2[i]=np.interp(xmax,ds['xgrid']/ds['time'],ds['rec'])
    ionradprearr2[i]=np.interp(xmax,ds['xgrid']/ds['time'],ds['ion_rad'])
    recradprearr2[i]=np.interp(xmax,ds['xgrid']/ds['time'],ds['rec_rad'])
    ionposarr2[i]=np.interp(xmin,ds['xgrid']/ds['time'],ds['ion'])
    recposarr2[i]=np.interp(xmin,ds['xgrid']/ds['time'],ds['rec'])
    ionradposarr2[i]=np.interp(xmin,ds['xgrid']/ds['time'],ds['ion_rad'])
    recradposarr2[i]=np.interp(xmin,ds['xgrid']/ds['time'],ds['rec_rad'])

    print(tpre,tpost,tmax,ropost/ropre,xn[-1])
    tprearr2[i]=tpre
    tpostarr2[i]=tpost
    tmaxarr2[i]=tmax
    rarr2[i]=ropost/ropre
    xnarr2[i]=xn[-1]
    tref2[i]=T0
"""

##############################################################################
#MHD data
dsm=PIPpy.pipread('../simdata/MHD_ref/',50)
T1m=dsm['pr_p'][-1]/dsm['ro_p'][-1]*5.0/3.0
Tm=dsm['pr_p']/dsm['ro_p']*5.0/3.0
tpost=np.interp(0.05,dsm['xgrid']/dsm['time'],Tm*T0/T1m)
tpre=np.interp(0.25,dsm['xgrid']/dsm['time'],Tm*T0/T1m)
tmax=np.max(Tm*T0/T1m)
ropost=np.interp(0.05,dsm['xgrid']/dsm['time'],dsm['ro_p'])
ropre=np.interp(0.25,dsm['xgrid']/dsm['time'],dsm['ro_p'])

tprem=tpre
tpostm=tpost
tmaxm=tmax
rm=ropost/ropre
xnm=0.0
trefm=T0
#xn=np.array([0.87,0.9986,0.9997,0.999992])
#xi=1.0-xn

#mhdtjump=27772.766819280467/5526.754752598247

#tpre=np.array([6158.830514202272,5237.838535379454,4894.209028189453,4927.655727575849])
#tpost=np.array([8394.621226583751,7862.661566436549,7936.2773700190355,9048.333527801136])
#tmax=np.array([24222.73214722533,16817.874630670856,17006.501840154626,17835.3943491788])

#comp=np.array([4.464929983051906,6.053326213145618,5.983905519969008,5.806633285098448])

fig, axs = plt.subplots(1, 1,dpi=300)
fig.set_size_inches(9.7, 6)
lthick=4.5

"""line1=plt.plot(np.log10(1.0-xnarr),tpostarr/tprearr,'-*r')
line2=plt.plot(np.log10(1.0-xnarr),tmaxarr/tprearr,'-*b')
line3=plt.plot(np.log10(1.0-xnarr),rarr,'-*g')"""

line1=plt.plot(tref,tpostarr/tprearr,'-*r',label='$T^d/T^u$',linewidth=lthick,markersize=12)
line2=plt.plot(tref,tmaxarr/tprearr,'-*b',label='$T_{max}/T^u$',linewidth=lthick,markersize=12)
line3=plt.plot(tref,rarr,'-*g',label='$\\rho^d/\\rho^u$',linewidth=lthick,markersize=12)
line4=plt.plot([5000,6250],[tpostm/tprem,tpostm/tprem],'r--',linewidth=lthick,markersize=12)#,label='$T^d/T^u$ (MHD)'
#axs=plt.plot([5000,6500],[tmaxm/tprem,tmaxm/tprem],'b--')
line5=plt.plot([5000,6250],[rm,rm],'g--',linewidth=lthick,markersize=12)#,label='$\\rho^d/\\rho^u$ (MHD)'
axs.legend(loc='upper right')
axs.set_ylim([1,5.5])
#axs[1,1].set_xscale('log')
#axs[1,1].set_yscale('log')
#axs[1,1].set_xlim([xmin-vs,xmax-vs])
axs.set_xlabel('$Temperature [K]$')
axs.set_ylabel('$T_{jump}, \\rho_{jump}$')
#line1=plt.plot(tref2,tpostarr2/tprearr2,'sr',linewidth=lthick,markersize=12)
#line2=plt.plot(tref2,tmaxarr2/tprearr2,'sb',linewidth=lthick,markersize=12)
#line3=plt.plot(tref2,rarr2,'sg',linewidth=lthick,markersize=12)
plt.savefig('tcompcor_plot',dpi=300)


###########################################
fig, axs = plt.subplots(1, 1,dpi=300)
fig.set_size_inches(9.7, 6)
lthick=4.5

ax2=axs.twinx()

"""line1=plt.plot(np.log10(1.0-xnarr),tpostarr/tprearr,'-*r')
line2=plt.plot(np.log10(1.0-xnarr),tmaxarr/tprearr,'-*b')
line3=plt.plot(np.log10(1.0-xnarr),rarr,'-*g')"""

axs.plot(tref,ionradprearr/ionprearr,'-*',color='#ff7f00',label='$\Gamma_{I,rad}/\Gamma_{I,col} (preshock)$',linewidth=lthick,markersize=12)
axs.plot(tref,ionradposarr/ionposarr,'-*',color='#377eb8',label='$\Gamma_{I,rad}/\Gamma_{I,col} (postshock)$',linewidth=lthick,markersize=12)
ax2.plot(tref,1.0-xnarr,'-*',color='#4daf4a',label='$\\xi_i (preshock)$',linewidth=lthick,markersize=12)
ax2.plot(tref,1.0-xnparr,'-*',color='#f781bf',label='$\\xi_i (postshock)$',linewidth=lthick,markersize=12)
#line2=plt.plot(tref,tmaxarr/tprearr,'-*b',label='$T_{max}/T^u$',linewidth=lthick)
#line3=plt.plot(tref,rarr,'-*g',label='$\\rho^d/\\rho^u$',linewidth=lthick)
#line4=plt.plot([5000,6500],[tpostm/tprem,tpostm/tprem],'r--',linewidth=lthick)#,label='$T^d/T^u$ (MHD)'
#axs=plt.plot([5000,6500],[tmaxm/tprem,tmaxm/tprem],'b--')
#line5=plt.plot([5000,6500],[rm,rm],'g--',linewidth=lthick)#,label='$\\rho^d/\\rho^u$ (MHD)'
ax2.legend(loc='lower right')
#axs.legend(loc=[0.5,0.02])
axs.legend(loc='lower left')
#axs[1,1].set_xscale('log')
axs.set_yscale('log')
ax2.set_yscale('log')
axs.set_ylim([1.0e-6,1.0e5])
ax2.set_ylim([1.0e-5,1.1e0])
axs.set_xlabel('$Temperature [K]$')
axs.set_ylabel('$\Gamma_{I,rad}/\Gamma_{I,col}$')
ax2.set_ylabel('$\\xi_i$')
plt.savefig('tcompcor_ion_plot',dpi=300)

#print(xi)