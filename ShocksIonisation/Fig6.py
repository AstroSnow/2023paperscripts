#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 15:23:28 2022

@author: ben
"""
import pipreadmods as PIPpy
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.transforms as mtransforms

#fname='../Data/'
#fname='../simdata/nleveltest_rad/Data/'
#fname='../simdata/nleveltest_rad_thick_st'
#fname='../simdata/upc_time10/' ;xmin=0.075;xmax=0.08; T0=6220.0
#fname='../simdata/isca_midc_ltest/Data/' ;xmin=0.052;xmax=0.074
fname='../simdata/CorrectedSims/upt10_conv/'

ds1=PIPpy.pipread(fname,1)
ds10=PIPpy.pipread(fname,10)
ds100=PIPpy.pipread('../simdata/CorrectedSims/upt100_conv/',10)
dsm=PIPpy.pipread('../simdata/MHD_ref/',50)

fig, axs = plt.subplots(4, 3,dpi=300)
fig.set_size_inches(12,12)
#fig.tight_layout(pad=2.0)
#plt.subplots_adjust(wspace=0.3)
lthick=2.5

#axs[0,0].plot(ds['xgrid']/ds['time'],ds['vx_n']-ds['vx_p'],label='vx_n-vx_p',color='k',linewidth=lthick)
axs[0,0].plot(ds1['xgrid']/ds1['time'],ds1['vx_n'],label='vx_n',color='r',linewidth=lthick)
axs[0,0].plot(ds1['xgrid']/ds1['time'],ds1['vx_p'],label='vx_p',color='b',linewidth=lthick)
axs[0,0].set_xscale('log')
axs[0,0].set_xlim([0.001,4])
axs[0,0].set_ylim([-1.6,0.2])
#axs[0,0].set_ylim([-0.16,0.16])
#axs[0,0].legend()
#axs[0,0].set_xlabel('$x/t$')
axs[0,0].set_ylabel('$v_x$')

T1=ds1['pr_p'][-1]/ds1['ro_p'][-1]*5.0/6.0
T1m=dsm['pr_p'][-1]/dsm['ro_p'][-1]*5.0/3.0
Tmhd=dsm['pr_p'][750]/dsm['ro_p'][750]*5.0/3.0/T1m
axs[1,0].plot(ds1['xgrid']/ds1['time'],ds1['pr_p']/ds1['ro_p']*5.0/6.0/T1,label='T_p',color='b',linewidth=lthick)
axs[1,0].plot(ds1['xgrid']/ds1['time'],ds1['pr_n']/ds1['ro_n']*5.0/3.0/T1,label='T_n',color='r',linewidth=lthick)
axs[1,0].plot([-1,4],[Tmhd,Tmhd],'k--',label='T (MHD)',linewidth=lthick)
#axs[0,1].set_yscale('log')
axs[1,0].set_xscale('log')
axs[1,0].set_xlim([0.001,4])#axs[0,1].set_xlim([0.01,2.0])
axs[1,0].set_ylim([0,17])
#axs[0,1].legend()
#axs[0,1].set_xlabel('$x_s$')
axs[1,0].set_ylabel('$T/T_0$')

axs[2,0].plot(ds1['xgrid']/ds1['time'],ds1['ion_loss'],label='P_n',color='k',linewidth=lthick)
#axs[1,1].plot(xs,ds['pr_p'],label='P_p',color='b',linewidth=lthick)
#axs[1,1].plot(xs,ds['pr_p']+ds['pr_n'],label='P_p+P_n',color='g',linewidth=lthick)
axs[2,0].set_xscale('log')
axs[2,0].set_xlim([0.001,4])
axs[2,0].set_ylim([-0.0005,0.002])
#axs[1,1].legend()
#axs[0,2].set_xlabel('$x_s$')
axs[2,0].set_ylabel('loss rate')


axs[3,0].plot(ds1['xgrid']/ds1['time'],ds1['ion'],label='ion',linewidth=lthick)
axs[3,0].plot(ds1['xgrid']/ds1['time'],ds1['rec'],label='rec',linewidth=lthick)
axs[3,0].plot(ds1['xgrid']/ds1['time'],ds1['ion_rad'],label='ion_rad',linewidth=lthick)
axs[3,0].plot(ds1['xgrid']/ds1['time'],ds1['rec_rad'],label='rec_rad',linewidth=lthick)
axs[3,0].set_yscale('log')
axs[3,0].set_xscale('log')
axs[3,0].set_xlim([0.001,4])
axs[3,0].set_ylim([1.0e-12,1.0e3])
#axs[0,3].legend()
axs[3,0].set_xlabel('$x/t$')
axs[3,0].set_ylabel('$\Gamma$')


##############################################################################################
axs[0,1].plot(ds10['xgrid']/ds10['time'],ds10['vx_n'],label='vx_n',color='r',linewidth=lthick)
axs[0,1].plot(ds10['xgrid']/ds10['time'],ds10['vx_p'],label='vx_p',color='b',linewidth=lthick)
axs[0,1].set_xscale('log')
axs[0,1].set_xlim([0.001,4])
axs[0,1].set_ylim([-1.6,0.2])
#axs[0,0].set_ylim([-0.16,0.16])
#axs[1,0].legend()
#axs[1,0].set_xlabel('$x/t$')
#axs[0,1].set_ylabel('$v_x$')

T1=ds10['pr_p'][-1]/ds10['ro_p'][-1]*5.0/6.0
T1m=dsm['pr_p'][-1]/dsm['ro_p'][-1]*5.0/3.0
Tmhd=dsm['pr_p'][750]/dsm['ro_p'][750]*5.0/3.0/T1m
axs[1,1].plot(ds10['xgrid']/ds10['time'],ds10['pr_p']/ds10['ro_p']*5.0/6.0/T1,label='T_p',color='b',linewidth=lthick)
axs[1,1].plot(ds10['xgrid']/ds10['time'],ds10['pr_n']/ds10['ro_n']*5.0/3.0/T1,label='T_n',color='r',linewidth=lthick)
axs[1,1].plot([-1,4],[Tmhd,Tmhd],'k--',label='T (MHD)',linewidth=lthick)
#axs[0,1].set_yscale('log')
axs[1,1].set_xscale('log')
axs[1,1].set_xlim([0.001,4])#axs[0,1].set_xlim([0.01,2.0])
axs[1,1].set_ylim([0,17])
#axs[1,1].legend()
#axs[1,1].set_xlabel('$x_s$')
#axs[1,1].set_ylabel('Temperature [kK]')

axs[2,1].plot(ds10['xgrid']/ds10['time'],ds10['ion_loss'],label='P_n',color='k',linewidth=lthick)
#axs[1,1].plot(xs,ds['pr_p'],label='P_p',color='b',linewidth=lthick)
#axs[1,1].plot(xs,ds['pr_p']+ds['pr_n'],label='P_p+P_n',color='g',linewidth=lthick)
axs[2,1].set_xscale('log')
axs[2,1].set_xlim([0.001,4])
axs[2,1].set_ylim([-0.0005,0.002])
#axs[0,0].set_ylim([-0.16,0.16])
#axs[1,1].legend()
#axs[1,2].set_xlabel('$x_s$')
#axs[2,1].set_ylabel('loss rate')


axs[3,1].plot(ds10['xgrid']/ds10['time'],ds10['ion'],label='ion',linewidth=lthick)
axs[3,1].plot(ds10['xgrid']/ds10['time'],ds10['rec'],label='rec',linewidth=lthick)
axs[3,1].plot(ds10['xgrid']/ds10['time'],ds10['ion_rad'],label='ion_rad',linewidth=lthick)
axs[3,1].plot(ds10['xgrid']/ds10['time'],ds10['rec_rad'],label='rec_rad',linewidth=lthick)
axs[3,1].set_yscale('log')
axs[3,1].set_xscale('log')
axs[3,1].set_xlim([0.001,4])
#axs[0,3].legend()
axs[3,1].set_xlabel('$x/t$')
axs[3,1].set_ylim([1.0e-12,1.0e3])
#axs[3,1].set_ylabel('$\Gamma$')

##############################################################################################
axs[0,2].plot(ds100['xgrid']/ds100['time'],ds100['vx_n'],label='vx_n',color='r',linewidth=lthick)
axs[0,2].plot(ds100['xgrid']/ds100['time'],ds100['vx_p'],label='vx_p',color='b',linewidth=lthick)
axs[0,2].set_xscale('log')
axs[0,2].set_xlim([0.001,4])
axs[0,2].set_ylim([-1.6,0.2])
#axs[0,0].set_ylim([-0.16,0.16])
axs[0,2].legend()
#axs[0,2].set_xlabel('$x/t$')
#axs[0,2].set_ylabel('$v_x$')

T1=ds100['pr_p'][-1]/ds100['ro_p'][-1]*5.0/6.0
T1m=dsm['pr_p'][-1]/dsm['ro_p'][-1]*5.0/3.0
Tmhd=dsm['pr_p'][750]/dsm['ro_p'][750]*5.0/3.0/T1m
axs[1,2].plot(ds100['xgrid']/ds100['time'],ds100['pr_p']/ds100['ro_p']*5.0/6.0/T1,label='T_p',color='b',linewidth=lthick)
axs[1,2].plot(ds100['xgrid']/ds100['time'],ds100['pr_n']/ds100['ro_n']*5.0/3.0/T1,label='T_n',color='r',linewidth=lthick)
axs[1,2].plot([-1,4],[Tmhd,Tmhd],'k--',label='T (MHD)',linewidth=lthick)
#axs20,1].set_yscale('log')
axs[1,2].set_xscale('log')
axs[1,2].set_xlim([0.001,4])#axs[0,1].set_xlim([0.01,2.0])
axs[1,2].set_ylim([0,17])
axs[1,2].legend()
#axs[1,2].set_xlabel('$x/t$')
#axs[1,2].set_ylabel('Temperature [kK]')

axs[2,2].plot(ds100['xgrid']/ds100['time'],ds100['ion_loss'],label='$\phi_I-\phi_R$',color='k',linewidth=lthick)
#axs[1,1].plot(xs,ds['pr_p'],label='P_p',color='b',linewidth=lthick)
#axs[1,1].plot(xs,ds['pr_p']+ds['pr_n'],label='P_p+P_n',color='g',linewidth=lthick)
axs[2,2].set_xscale('log')
axs[2,2].set_xlim([0.001,4])
axs[2,2].set_ylim([-0.0005,0.002])
#axs[0,0].set_ylim([-0.16,0.16])
axs[2,2].legend()
#axs[2,2].set_xlabel('$x/t$')
#axs[2,2].set_ylabel('loss rate')


axs[3,2].plot(ds100['xgrid']/ds100['time'],ds100['ion'],label='$\Gamma_{ion,col}$',linewidth=lthick)
axs[3,2].plot(ds100['xgrid']/ds100['time'],ds100['rec'],label='$\Gamma_{rec,col}$',linewidth=lthick)
axs[3,2].plot(ds100['xgrid']/ds100['time'],ds100['ion_rad'],label='$\Gamma_{ion,rad}$',linewidth=lthick)
axs[3,2].plot(ds100['xgrid']/ds100['time'],ds100['rec_rad'],label='$\Gamma_{rec,rad}$',linewidth=lthick)
axs[3,2].set_yscale('log')
axs[3,2].set_xscale('log')
axs[3,2].set_xlim([0.001,4])
axs[3,2].set_ylim([1.0e-12,1.0e3])
axs[3,2].legend(handlelength=1)
#leg.handlelength=0.1
axs[3,2].set_xlabel('$x/t$')
#axs[3,2].set_ylabel('$\Gamma$')

#
#Some plot fixes
fig.tight_layout()
#plt.subplots_adjust(wspace=0.3)

trans = mtransforms.ScaledTranslation(-15/72, 10/72, fig.dpi_scale_trans)
axs[0,0].text(1.0, 0.0, 'a', transform=axs[0,0].transAxes + trans,
        fontsize='medium', verticalalignment='bottom', fontfamily='serif',
        bbox=dict(facecolor='0.7', edgecolor='none', pad=3.0))
trans = mtransforms.ScaledTranslation(-15/72, 10/72, fig.dpi_scale_trans)
axs[0,1].text(1.0, 0.0, 'b', transform=axs[0,1].transAxes + trans,
        fontsize='medium', verticalalignment='bottom', fontfamily='serif',
        bbox=dict(facecolor='0.7', edgecolor='none', pad=3.0))
trans = mtransforms.ScaledTranslation(-15/72, 10/72, fig.dpi_scale_trans)
axs[0,2].text(1.0, 0.0, 'c', transform=axs[0,2].transAxes + trans,
        fontsize='medium', verticalalignment='bottom', fontfamily='serif',
        bbox=dict(facecolor='0.7', edgecolor='none', pad=3.0))

trans = mtransforms.ScaledTranslation(10/72, 10/72, fig.dpi_scale_trans)
axs[1,0].text(0.0, 0.0, 'd', transform=axs[1,0].transAxes + trans,
        fontsize='medium', verticalalignment='bottom', fontfamily='serif',
        bbox=dict(facecolor='0.7', edgecolor='none', pad=3.0))
trans = mtransforms.ScaledTranslation(10/72, 10/72, fig.dpi_scale_trans)
axs[1,1].text(0.0, 0.0, 'e', transform=axs[1,1].transAxes + trans,
        fontsize='medium', verticalalignment='bottom', fontfamily='serif',
        bbox=dict(facecolor='0.7', edgecolor='none', pad=3.0))
trans = mtransforms.ScaledTranslation(10/72, 10/72, fig.dpi_scale_trans)
axs[1,2].text(0.0, 0.0, 'f', transform=axs[1,2].transAxes + trans,
        fontsize='medium', verticalalignment='bottom', fontfamily='serif',
        bbox=dict(facecolor='0.7', edgecolor='none', pad=3.0))

trans = mtransforms.ScaledTranslation(10/72, -15/72, fig.dpi_scale_trans)
axs[2,0].text(0.0, 1.0, 'g', transform=axs[2,0].transAxes + trans,
        fontsize='medium', verticalalignment='bottom', fontfamily='serif',
        bbox=dict(facecolor='0.7', edgecolor='none', pad=3.0))
trans = mtransforms.ScaledTranslation(10/72, -15/72, fig.dpi_scale_trans)
axs[2,1].text(0.0, 1.0, 'h', transform=axs[2,1].transAxes + trans,
        fontsize='medium', verticalalignment='bottom', fontfamily='serif',
        bbox=dict(facecolor='0.7', edgecolor='none', pad=3.0))
trans = mtransforms.ScaledTranslation(10/72, -15/72, fig.dpi_scale_trans)
axs[2,2].text(0.0, 1.0, 'i', transform=axs[2,2].transAxes + trans,
        fontsize='medium', verticalalignment='bottom', fontfamily='serif',
        bbox=dict(facecolor='0.7', edgecolor='none', pad=3.0))

trans = mtransforms.ScaledTranslation(-15/72, 10/72, fig.dpi_scale_trans)
axs[3,0].text(1.0, 0.0, 'j', transform=axs[3,0].transAxes + trans,
        fontsize='medium', verticalalignment='bottom', fontfamily='serif',
        bbox=dict(facecolor='0.7', edgecolor='none', pad=3.0))
trans = mtransforms.ScaledTranslation(-15/72, 10/72, fig.dpi_scale_trans)
axs[3,1].text(1.0, 0.0, 'k', transform=axs[3,1].transAxes + trans,
        fontsize='medium', verticalalignment='bottom', fontfamily='serif',
        bbox=dict(facecolor='0.7', edgecolor='none', pad=3.0))
trans = mtransforms.ScaledTranslation(-15/72, 10/72, fig.dpi_scale_trans)
axs[3,2].text(1.0, 0.0, 'l', transform=axs[3,2].transAxes + trans,
        fontsize='medium', verticalalignment='bottom', fontfamily='serif',
        bbox=dict(facecolor='0.7', edgecolor='none', pad=3.0))

plt.savefig('timeseries_plot_upcor.png',dpi=300)
