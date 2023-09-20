#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 11:33:51 2022

@author: ben
"""
import pipreadmods as PIPpy
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.transforms as mtransforms
import matplotlib

matplotlib.rcParams.update({'font.size': 10})

#fname='../Data/'
#fname='../simdata/nleveltest_rad/Data/'
#fname='../simdata/nleveltest_rad_thick_st'
#fname='../simdata/T_6220_long/Data/' ;xmin=0.075;xmax=0.08; T0=6220.0
#fname='../simdata/isca_midc_ltest/Data/' ;xmin=0.052;xmax=0.074
fname='../simdata/CorrectedSims/uptestisca/' ;xmin=0.1451;xmax=0.1466; T0=6220.0; etime=60

ds=PIPpy.pipread(fname,30)
dsm=PIPpy.pipread('../simdata/MHD_ref/',50)

#nntot=ds['nexcite1']+ds['nexcite2']+ds['nexcite3']+ds['nexcite4']+ds['nexcite5']

#ndif=ds['ro_n']-nntot

#############################################################
#Temperature
T1=ds['pr_p'][-1]/ds['ro_p'][-1]*5.0/6.0
T1m=dsm['pr_p'][-1]/dsm['ro_p'][-1]*5.0/3.0

Tmhd=dsm['pr_p'][750]/dsm['ro_p'][750]*5.0/3.0/T1m#/1000.0

#############################################################
#Estimate the shock frame
b=np.argmin(np.gradient(ds['vx_p'])) #plasma shock location
vs=ds['xgrid'][b]/ds['time'] #plasma shock velocity
xs=ds['xgrid']/ds['time']-vs #shock grid
bn=np.argmin(np.gradient(ds['vx_n'])) #neutral shock location
vsn=ds['xgrid'][bn]/ds['time'] #neutral shock velocity

############################################################
#Frictional heating
fheat=0.5*ds['ac']*ds['ro_p']*ds['ro_n']*(np.abs(ds['vx_n']-ds['vx_p'])+np.abs(ds['vy_n']-ds['vy_p']))**2
#Thermal damping
tdamp=3.0/2.0*ds['ac']*ds['ro_p']*ds['ro_n']*(ds['pr_n']/ds['ro_n']-ds['pr_p']/ds['ro_p']/2.0)

#Ionisation heating 
Hp=0.5*((ds['rec']+ds['rec_rad'])*ds['ro_p']*(ds['vx_p']**2+ds['vy_p']**2) 
        -2.0*(ds['ion']+ds['ion_rad'])*ds['ro_n']*(ds['vx_p']*ds['vx_n']+ds['vy_p']*ds['vy_n']) +
        (ds['ion']+ds['ion_rad'])*ds['ro_n']*(ds['vx_n']**2+ds['vy_n']**2))
Hn=0.5*((ds['rec']+ds['rec_rad'])*ds['ro_p']*(ds['vx_p']**2+ds['vy_p']**2) 
        -2.0*(ds['rec']+ds['rec_rad'])*ds['ro_n']*(ds['vx_p']*ds['vx_n']+ds['vy_p']*ds['vy_n']) +
        (ds['ion']+ds['ion_rad'])*ds['ro_n']*(ds['vx_n']**2+ds['vy_n']**2))
tdampion=((ds['ion']+ds['ion_rad'])*ds['pr_n']-0.5*(ds['rec']+ds['rec_rad'])*ds['pr_p'])/(5.0/3.0-1.0)

fig, axs = plt.subplots(4, 1,dpi=300)
fig.set_size_inches(6, 12)
lthick=2.5

axs[0].plot(xs,fheat,label='$H_f$',color='k',linewidth=lthick)
axs[0].plot(xs,tdamp,label='$T_{damp}$',color='r',linewidth=lthick)
axs[0].plot(xs,-tdamp,label='$-T_{damp}$',color='b',linewidth=lthick)
#axs[0].plot(xs,ds['pr_n']/ds['ro_n']*5.0/3.0*T0/T1/1000.0,label='T_n',color='r',linewidth=lthick)
#axs[0].plot([-1,1],[Tmhd,Tmhd],'k--',label='T (MHD)',linewidth=lthick)
axs[0].set_yscale('log')
#axs[0,1].set_xscale('log')
axs[0].set_xlim([xmin-vs,xmax-vs])#
#axs[0].set_ylim([1.0e-6,1.0e-1])
axs[0].set_ylim([1.0e-8,1.0e0])
axs[0].legend()
#axs[0].set_xlabel('$x_s$')
axs[0].set_ylabel('$H_f, T_{damp}$')

"""axs[1].plot(xs,Hn,label='$H_n$',color='k',linewidth=lthick)
axs[1].plot(xs,-Hp,label='$-H_p$',color='g',linewidth=lthick)
axs[1].plot(xs,Hn+Hp,label='$H_n+H_p$',color='y',linewidth=lthick)
axs[1].plot(xs,tdampion,label='$T_{damp,ion}$',color='r',linewidth=lthick)
axs[1].plot(xs,-tdampion,label='$-T_{damp,ion}$',color='b',linewidth=lthick)"""
hnp=axs[1].plot(xs,Hn,label='$H_n$',color='k',linewidth=lthick)
hnn=axs[1].plot(xs,-Hn,label='_nolegend_',color='k',linewidth=lthick,linestyle='--')
hpp=axs[1].plot(xs,Hp,label='$H_p$',color='g',linewidth=lthick)
hpn=axs[1].plot(xs,-Hp,label='_nolegend_',color='g',linewidth=lthick,linestyle='--')
ht=axs[1].plot(xs,Hn+Hp,label='$H_n+H_p$',color='y',linewidth=lthick)
htn=axs[1].plot(xs,-(Hn+Hp),label='_nolegend_',color='y',linewidth=lthick)
tdi=axs[1].plot(xs,tdampion,label='$T_{damp,ion}$',color='r',linewidth=lthick)
tdin=axs[1].plot(xs,-tdampion,label='_nolegend_',color='r',linewidth=lthick,linestyle='--')
#axs[0].plot(xs,ds['pr_n']/ds['ro_n']*5.0/3.0*T0/T1/1000.0,label='T_n',color='r',linewidth=lthick)
#axs[0].plot([-1,1],[Tmhd,Tmhd],'k--',label='T (MHD)',linewidth=lthick)
axs[1].set_yscale('log')
#axs[0,1].set_xscale('log')
axs[1].set_xlim([xmin-vs,xmax-vs])#
axs[1].set_ylim([1.0e-8,1.0e0])
#axs[1].set_ylim([1.0e-6,1.0e-1])
axs[1].legend(loc='upper right')
#axs[1].set_xlabel('$x_s$')
axs[1].set_ylabel('$H_n,H_p, T_{damp,ion}$')

axs[2].plot(xs,ds['ion_loss'],label='P_n',color='k',linewidth=lthick)
#axs[1,1].plot(xs,ds['pr_p'],label='P_p',color='b',linewidth=lthick)
#axs[1,1].plot(xs,ds['pr_p']+ds['pr_n'],label='P_p+P_n',color='g',linewidth=lthick)
axs[2].set_yscale('log')
axs[2].set_xlim([xmin-vs,xmax-vs])
#axs[2].set_ylim([1.0e-6,1.0e-1])
axs[2].set_ylim([1.0e-8,1.0e0])
#axs[1,1].legend()
#axs[2].set_xlabel('$x_s$')
axs[2].set_ylabel('loss rate')

axs[3].plot(xs,ds['pr_p']/ds['ro_p']*5.0/6.0/T1,label='T_p',color='b',linewidth=lthick)
axs[3].plot(xs,ds['pr_n']/ds['ro_n']*5.0/3.0/T1,label='T_n',color='r',linewidth=lthick)
axs[3].plot([-1,1],[Tmhd,Tmhd],'k--',label='T (MHD)',linewidth=lthick)
#axs[0,1].set_yscale('log')
#axs[0,1].set_xscale('log')
axs[3].set_xlim([xmin-vs,xmax-vs])#axs[0,1].set_xlim([0.01,2.0])
axs[3].legend()
axs[3].set_xlabel('$x_s$')
axs[3].set_ylabel('T/$T_0$')


trans = mtransforms.ScaledTranslation(5/72, -5/72, fig.dpi_scale_trans)
axs[0].text(0.0, 1.0, 'a', transform=axs[0].transAxes + trans,
        fontsize='medium', verticalalignment='top', fontfamily='serif',
        bbox=dict(facecolor='0.7', edgecolor='none', pad=3.0))
trans = mtransforms.ScaledTranslation(5/72, -5/72, fig.dpi_scale_trans)
axs[1].text(0.0, 1.0, 'b', transform=axs[1].transAxes + trans,
        fontsize='medium', verticalalignment='top', fontfamily='serif',
        bbox=dict(facecolor='0.7', edgecolor='none', pad=3.0))
trans = mtransforms.ScaledTranslation(5/72, -5/72, fig.dpi_scale_trans)
axs[2].text(0.0, 1.0, 'c', transform=axs[2].transAxes + trans,
        fontsize='medium', verticalalignment='top', fontfamily='serif',
        bbox=dict(facecolor='0.7', edgecolor='none', pad=3.0))
trans = mtransforms.ScaledTranslation(5/72, -5/72, fig.dpi_scale_trans)
axs[3].text(0.0, 1.0, 'd', transform=axs[3].transAxes + trans,
        fontsize='medium', verticalalignment='top', fontfamily='serif',
        bbox=dict(facecolor='0.7', edgecolor='none', pad=3.0))

plt.savefig('heatterms_plot_upcor.png',dpi=300)


