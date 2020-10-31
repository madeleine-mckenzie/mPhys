# Matplotlib imports:

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D #for 3d plots
from matplotlib.font_manager import FontProperties #for the pdf fonts

from matplotlib.ticker import MultipleLocator, FormatStrFormatter, AutoMinorLocator, AutoLocator, MaxNLocator
from mpl_toolkits.axes_grid1.anchored_artists import AnchoredSizeBar

import matplotlib.gridspec as gridspec
from matplotlib.colorbar import Colorbar

from scipy import optimize

from matplotlib import rcParams
rcParams['font.family'] = 'serif'
rcParams['font.size'] = 14
#plt.rcParams['axes.labelweight'] = 'bold'
rcParams["axes.edgecolor"] = 'black'
rcParams["legend.edgecolor"] = '0.8'

plt.rcParams['mathtext.fontset'] = 'dejavuserif'
plt.rcParams['text.latex.preamble']=[r"\usepackage{amsmath}"]

import matplotlib.colors as mcolors

from array_manager import get_arrays_ts4

import numpy as np

from matplotlib import colors

import matplotlib.ticker as ticker

from make_summary import write_rotation

from scipy.stats import kde

from scipy import stats


new_col = 'xkcd:periwinkle'
old_col = 'xkcd:rosy pink'


def fmt(x, pos):
    if x == 0:
        return r'0'
    a, b = '{:.1e}'.format(x).split('e')
    b = int(b)
    return r'${} \times 10^{{{}}}$'.format(a, b)


def plot_tout_4(data_array, timeStepArray):

    gal, gas, new, old = get_arrays_ts4(data_array, 0)

    fig, ax = plt.subplots(2, 4, sharex=True, sharey=True)
    fig.set_size_inches(15 , 7)
    ax_lims = 2000

    font = FontProperties()
    font.set_weight('bold')

    ax[0,0].scatter(gas[:,0], gas[:,1], c='dimgrey', s=0.1)
    ax[0,0].scatter(old[:,0], old[:,1], c='red', s=0.1)
    ax[0,0].text(-0.8* ax_lims, 0.8* ax_lims, 'T = %.2g  yrs' %timeStepArray[0], weight = 'bold')
    ax[0,0].set_xlim(-ax_lims,ax_lims)
    ax[0,0].set_ylim(-ax_lims,ax_lims)
    ax[0,0].set_ylabel("Y (pc)")
    ax[0,0].xaxis.set_minor_locator(AutoMinorLocator())
    ax[0,0].yaxis.set_minor_locator(AutoMinorLocator())

    ax[1,0].scatter(gas[:,0], gas[:,2], c='dimgrey', s=0.05)
    ax[1,0].scatter(old[:,0], old[:,2], c='red', s=0.05)
    ax[1,0].set_xlim(-ax_lims,ax_lims)
    ax[1,0].set_ylim(-ax_lims,ax_lims)
    ax[1,0].set_xlabel("X (pc)")
    ax[1,0].set_ylabel("Z (pc)")
    ax[1,0].xaxis.set_minor_locator(AutoMinorLocator())
    ax[1,0].yaxis.set_minor_locator(AutoMinorLocator())

    gal, gas, new, old = get_arrays_ts4(data_array, 1)

    #for plot labels
    gs= ax[0,1].scatter(gas[:,0], gas[:,1], c='dimgrey', s=0.05)
    gc=ax[0,1].scatter(old[:,0], old[:,1], c='red', s=0.05)
    ns=ax[0,1].scatter(new[:,0], new[:,1], c='cyan', s=1)
    ax[0,1].text(-0.8* ax_lims, 0.8* ax_lims, 'T = %.2g  yrs' %timeStepArray[1], weight = 'bold')
    ax[0,1].set_xlim(-ax_lims,ax_lims)
    ax[0,1].set_ylim(-ax_lims,ax_lims)

    ax[1,1].scatter(gas[:,0], gas[:,2], c='dimgrey', s=0.05)
    ax[1,1].scatter(old[:,0], old[:,2], c='red', s=0.05)
    ax[1,1].scatter(new[:,0], new[:,2], c='cyan', s=1)
    ax[1,1].set_xlim(-ax_lims,ax_lims)
    ax[1,1].set_ylim(-ax_lims,ax_lims)
    ax[1,1].set_xlabel("X (pc)")
    ax[1,1].xaxis.set_minor_locator(AutoMinorLocator())
    ax[1,1].yaxis.set_minor_locator(AutoMinorLocator())

    gal, gas, new, old = get_arrays_ts4(data_array, 2)

    ax[0,2].scatter(gas[:,0], gas[:,1], c='dimgrey', s=0.05)
    ax[0,2].scatter(old[:,0], old[:,1], c='red', s=0.05)
    ax[0,2].scatter(new[:,0], new[:,1], c='cyan', s=1)
    ax[0,2].text(-0.8* ax_lims, 0.8* ax_lims, 'T = %.2g  yrs' %timeStepArray[2],  weight = 'bold')
    ax[0,2].set_xlim(-ax_lims,ax_lims)
    ax[0,2].set_ylim(-ax_lims,ax_lims)
    ax[0,2].xaxis.set_minor_locator(AutoMinorLocator())
    ax[0,2].yaxis.set_minor_locator(AutoMinorLocator())

    ax[1,2].scatter(gas[:,0], gas[:,2], c='dimgrey',s=0.05)
    ax[1,2].scatter(old[:,0], old[:,2], c='red', s=0.05)
    ax[1,2].scatter(new[:,0], new[:,2], c='cyan', s=1)
    ax[1,2].set_xlim(-ax_lims,ax_lims)
    ax[1,2].set_ylim(-ax_lims,ax_lims)
    ax[1,2].set_xlabel("X (pc)")
    ax[1,2].xaxis.set_minor_locator(AutoMinorLocator())
    ax[1,2].yaxis.set_minor_locator(AutoMinorLocator())

    gal, gas, new, old = get_arrays_ts4(data_array, 3)

    ax[0,3].scatter(gas[:,0], gas[:,1], c='dimgrey', s=0.05)
    ax[0,3].scatter(old[:,0], old[:,1], c='red', s=0.05)
    ax[0,3].scatter(new[:,0], new[:,1], c='cyan', s=1)
    ax[0,3].text(-0.8*ax_lims, 0.8*ax_lims, 'T = %.2g  yrs' %timeStepArray[3],  weight = 'bold')
    ax[0,3].set_xlim(-ax_lims,ax_lims)
    ax[0,3].set_ylim(-ax_lims,ax_lims)
    ax[0,3].xaxis.set_minor_locator(AutoMinorLocator())
    ax[0,3].yaxis.set_minor_locator(AutoMinorLocator())


    ax[1,3].scatter(gas[:,0], gas[:,2], c='dimgrey',s=0.05)
    ax[1,3].scatter(old[:,0], old[:,2], c='red', s=0.05)
    ax[1,3].scatter(new[:,0], new[:,2], c='cyan', s=1)
    ax[1,3].set_xlim(-ax_lims,ax_lims)
    ax[1,3].set_ylim(-ax_lims,ax_lims)
    ax[1,3].set_xlabel("X (pc)")
    ax[1,3].xaxis.set_minor_locator(AutoMinorLocator())
    ax[1,3].yaxis.set_minor_locator(AutoMinorLocator())

    ax[0,0].tick_params(direction='in', axis='both', which='both', bottom=True,top=True, left=True, right=True)
    ax[0,1].tick_params(direction='in', axis='both', which='both', bottom=True,top=True, left=True, right=True)
    ax[0,2].tick_params(direction='in', axis='both', which='both', bottom=True,top=True, left=True, right=True)
    ax[0,3].tick_params(direction='in', axis='both', which='both', bottom=True,top=True, left=True, right=True)
    ax[1,0].tick_params(direction='in', axis='both', which='both', bottom=True,top=True, left=True, right=True)
    ax[1,1].tick_params(direction='in', axis='both', which='both', bottom=True,top=True, left=True, right=True)
    ax[1,2].tick_params(direction='in', axis='both', which='both', bottom=True,top=True, left=True, right=True)
    ax[1,3].tick_params(direction='in', axis='both', which='both', bottom=True,top=True, left=True, right=True)
    plt.legend((gs, gc, ns), ('Gas', 'GC stars', 'New stars'), markerscale=10)
    plt.tight_layout()
    plt.savefig("spacial_positions")
    plt.close()

    del gal, gas, old, new

# Using bins of 80
def los_curve(old, new, bins):

    fig, ax = plt.subplots(3,2)
    fig.set_size_inches(12, 15)
    gamma = 0.4

    ax[0,0].hist2d(old['x_scale'], old['vy'], bins=[bins, bins], norm=mcolors.PowerNorm(gamma), range=([-50,50],[-50,50]))
    ax[0,0].set_xlim(-50,50)
    ax[0,0].set_ylim(-50,50)
    ax[0,0].set_xlabel("X position (pc)")
    ax[0,0].set_ylabel("Vy (km/s)")

    ax[0,1].hist2d(new['x_scale'], new['vy'],bins=[bins, bins], norm=mcolors.PowerNorm(gamma), range=([-50,50],[-50,50]))
    ax[0,1].set_xlim(-50,50)
    ax[0,1].set_ylim(-50,50)
    ax[0,1].set_xlabel("X position (pc)")
    ax[0,1].set_ylabel("Vy (km/s)")


    ax[1,0].hist2d(old['x_scale'], old['vz'], bins=[bins, bins], norm=mcolors.PowerNorm(gamma), range=([-50,50],[-50,50]))
    ax[1,0].set_xlim(-50,50)
    ax[1,0].set_ylim(-50,50)
    ax[1,0].set_xlabel("X position (pc)")
    ax[1,0].set_ylabel("Vz (km/s)")

    ax[1,1].hist2d(new['x_scale'], new['vz'],bins=[bins, bins], norm=mcolors.PowerNorm(gamma), range=([-50,50],[-50,50]))
    ax[1,1].set_xlim(-50,50)
    ax[1,1].set_ylim(-50,50)
    ax[1,1].set_xlabel("X position (pc)")
    ax[1,1].set_ylabel("Vz (km/s)")

    ax[2,0].hist2d(old['y_scale'], old['vx'], bins=[bins, bins], norm=mcolors.PowerNorm(gamma), range=([-50,50],[-50,50]))
    ax[2,0].set_xlim(-50,50)
    ax[2,0].set_ylim(-50,50)
    ax[2,0].set_xlabel("Y position (pc)")
    ax[2,0].set_ylabel("Vx (km/s)")

    ax[2,1].hist2d(new['y_scale'], new['vx'],bins=[bins, bins], norm=mcolors.PowerNorm(gamma), range=([-50,50],[-50,50]))
    ax[2,1].set_xlim(-50,50)
    ax[2,1].set_ylim(-50,50)
    ax[2,1].set_xlabel("Y position (pc)")
    ax[2,1].set_ylabel("Vx (km/s)")

    plt.tight_layout()
    print('should have plotted rotation')
    plt.savefig("rotation_hist")
    plt.close()

def final_ts_plot(gal,gas, new, old, bins, rang):
    '''
    gal_count, xedges, yedges = np.histogram2d(gal['x'], gal['y'], bins=[bins, bins],range=([-rang,rang],[-rang,rang]))
    gas_count, xedges, yedges = np.histogram2d(gas['x'], gas['y'], bins=[bins, bins],range=([-rang,rang],[-rang,rang]))
    new_count, xedges, yedges = np.histogram2d(new['x'], new['y'], bins=[bins, bins],range=([-rang,rang],[-rang,rang]))
    old_count, xedges, yedges = np.histogram2d(old['x'], old['y'], bins=[bins, bins],range=([-rang,rang],[-rang,rang]))
    gal_max = np.amax(gal_count)
    gas_max = np.amax(gas_count)
    new_max = np.amax(new_count)
    old_max = np.amax(old_count)
    '''
    # For normalising the histograms
    gal_max = np.amax(gal.mass)
    gas_max = np.amax(gas.mass)
    new_max = np.amax(new.mass)
    old_max = np.amax(old.mass)

    # Get maximum value to use as the upper bound
    all_max = max(gal_max, gas_max, new_max, old_max)


    fig, ax = plt.subplots(2,2, sharey=True, sharex=True)
    fig.set_size_inches(8, 8)
    gamma = 0.3
    cm = plt.cm.get_cmap('magma_r')

    ax[1,0].hist2d(gas['x'], gas['y'], bins=[bins, bins], norm=mcolors.PowerNorm(gamma), vmin=0, vmax=all_max, range=([-rang,rang],[-rang,rang]), cmap=cm)
    ax[1,0].set_xlim(-rang,rang)
    ax[1,0].set_ylim(-rang,rang)
    ax[1,0].set_xlabel("X (pc)")
    ax[1,0].set_ylabel("Y (pc)")
    ax[1,0].xaxis.set_minor_locator(AutoMinorLocator())
    ax[1,0].yaxis.set_minor_locator(AutoMinorLocator())

    ax[1,1].hist2d(gal['x'], gal['y'], bins=[bins, bins], norm=mcolors.PowerNorm(gamma), vmin=0, vmax=all_max, range=([-rang,rang],[-rang,rang]), cmap=cm)
    ax[1,1].set_xlim(-rang,rang)
    ax[1,1].set_ylim(-rang,rang)
    ax[1,1].set_xlabel("X (pc)")
    ax[1,1].xaxis.set_minor_locator(AutoMinorLocator())
    ax[1,1].yaxis.set_minor_locator(AutoMinorLocator())

    ax[0,0].hist2d(old['x'], old['y'], bins=[bins, bins], norm=mcolors.PowerNorm(gamma), vmin=0, vmax=all_max, range=([-rang,rang],[-rang,rang]), cmap=cm)
    ax[0,0].set_xlim(-rang,rang)
    ax[0,0].set_ylim(-rang,rang)
    ax[0,0].set_ylabel("Y (pc)")
    ax[0,0].xaxis.set_minor_locator(AutoMinorLocator())
    ax[0,0].yaxis.set_minor_locator(AutoMinorLocator())


    ax[0,1].hist2d(new['x'], new['y'], bins=[bins, bins], norm=mcolors.PowerNorm(gamma), vmin=0, vmax=all_max, range=([-rang,rang],[-rang,rang]), cmap=cm)
    ax[0,1].set_xlim(-rang,rang)
    ax[0,1].set_ylim(-rang,rang)
    ax[0,1].set_xlabel("X (pc)")
    ax[0,1].xaxis.set_minor_locator(AutoMinorLocator())
    ax[0,1].yaxis.set_minor_locator(AutoMinorLocator())

    ax[0,0].tick_params(direction='in', axis='both', which='both', bottom=True,top=True, left=True, right=True)
    ax[0,1].tick_params(direction='in', axis='both', which='both', bottom=True,top=True, left=True, right=True)
    ax[1,0].tick_params(direction='in', axis='both', which='both', bottom=True,top=True, left=True, right=True)
    ax[1,1].tick_params(direction='in', axis='both', which='both', bottom=True,top=True, left=True, right=True)


    ax[0,0].yaxis.set_major_locator(MaxNLocator(nbins='auto', prune='lower')) # added
    ax[1,0].xaxis.set_major_locator(MaxNLocator(nbins='auto',prune='upper')) # added
    plt.subplots_adjust(wspace=0, hspace=0)

    props = dict(facecolor='white',alpha=0.9)
    ax[0,0].text(-1200, 1100, '1G', bbox=props)
    ax[0,1].text(-1200, 1100, '2G', bbox=props)
    ax[1,0].text(-1200, 1100, 'Gas', bbox=props)
    ax[1,1].text(-1200, 1100, 'Disk Stars', bbox=props)

    #plt.tight_layout()
    plt.savefig("final_time_step", bbox_inches='tight', dpi = 300)
    plt.close()

def final_ts_plot_scale(gal, gas, new, old, bins, rang):

    # Calculate histogram bins then use imshow()
    # Weighted by mass
    gal_count, xedges, yedges = np.histogram2d(gal['x_scale'], gal['y_scale'], bins=[bins, bins],range=([-rang,rang],[-rang,rang]), weights=gal['mass'])
    gas_count, xedges, yedges = np.histogram2d(gas['x_scale'], gas['y_scale'], bins=[bins, bins],range=([-rang,rang],[-rang,rang]), weights=gas['mass'])
    new_count, xedges, yedges = np.histogram2d(new['x_scale'], new['y_scale'], bins=[bins, bins],range=([-rang,rang],[-rang,rang]), weights=new['mass'])
    old_count, xedges, yedges = np.histogram2d(old['x_scale'], old['y_scale'], bins=[bins, bins],range=([-rang,rang],[-rang,rang]), weights=old['mass'])


    fig = plt.figure()
    gs = gridspec.GridSpec(2, 4, width_ratios=[1,1, 0.05, 0.05])
    cbax = plt.subplot(gs[:,3])
    ax0 = plt.subplot(gs[1,0]) # bottom left
    ax1 = plt.subplot(gs[1,1], sharey=ax0) # bottom right
    ax2 = plt.subplot(gs[0,0], sharex=ax0) # top left
    ax3 = plt.subplot(gs[0,1], sharex=ax1, sharey=ax2) # top right
    fig.set_size_inches(6, 6.05)

    plt.setp(ax1.get_yticklabels(), visible=False)
    plt.setp(ax2.get_xticklabels(), visible=False)
    plt.setp(ax3.get_yticklabels(), visible=False)
    plt.setp(ax3.get_xticklabels(), visible=False)

    gamma = 0.5
    #gamma = 0.4
    cmap = plt.cm.get_cmap('magma_r')

    gal_max = np.amax(gal_count)
    gas_max = np.amax(gas_count)
    new_max = np.amax(new_count)
    old_max = np.amax(old_count)

    all_max = max(gal_max, gas_max, new_max, old_max)

    props = dict(facecolor='white',alpha=0.9)
    vmin = 1e2
    #vmin = 1e3
    shading = 'quadric'


    im = ax0.imshow(gal_count.T, cmap=cmap, origin='lower', vmin=vmin, vmax=all_max, norm=mcolors.PowerNorm(gamma), interpolation=shading)
    ax0.set_xlabel("X (pc)")
    ax0.set_ylabel("Y (pc)")
    ax0.xaxis.set_minor_locator(AutoMinorLocator())
    ax0.yaxis.set_minor_locator(AutoMinorLocator())
    ax0.text(5, 50, 'Disk Stars', bbox=props)

    ax1.imshow(gas_count.T, cmap=cmap, origin='lower', vmin=vmin, vmax=all_max, norm=mcolors.PowerNorm(gamma), interpolation=shading)
    ax1.set_xlabel("X (pc)")
    ax1.xaxis.set_minor_locator(AutoMinorLocator())
    ax1.yaxis.set_minor_locator(AutoMinorLocator())
    ax1.text(5, 50, 'Gas', bbox=props)

    ax2.imshow(old_count.T, cmap=cmap, origin='lower', vmin=vmin, vmax=all_max, norm=mcolors.PowerNorm(gamma), interpolation=shading)
    ax2.set_ylabel("Y (pc)")
    ax2.xaxis.set_minor_locator(AutoMinorLocator())
    ax2.yaxis.set_minor_locator(AutoMinorLocator())
    ax2.text(5, 50, '1G', bbox=props)


    ax3.imshow(new_count.T, cmap=cmap, origin='lower', vmin=vmin, vmax=all_max, norm=mcolors.PowerNorm(gamma), interpolation=shading)
    ax3.xaxis.set_minor_locator(AutoMinorLocator())
    ax3.yaxis.set_minor_locator(AutoMinorLocator())
    ax3.text(5, 50, '2G', bbox=props)

    ax0.tick_params(direction='in', axis='both', which='both', bottom=True,top=True, left=True, right=True)
    ax1.tick_params(direction='in', axis='both', which='both', bottom=True,top=True, left=True, right=True)
    ax2.tick_params(direction='in', axis='both', which='both', bottom=True,top=True, left=True, right=True)
    ax3.tick_params(direction='in', axis='both', which='both', bottom=True,top=True, left=True, right=True)
    gs.update(left=0.05, right=0.95, bottom=0.08, top=0.93, wspace=0.0, hspace=0.0)

    cb = Colorbar(ax = cbax, mappable = im , format=ticker.FuncFormatter(fmt))
    #cb = Colorbar(ax = cbax, mappable = im)
    cb.set_label(r'M$_\odot$pc$^{-2}$', labelpad=10)
    plt.savefig("final_time_step_zoom", bbox_inches='tight', dpi = 300)
    plt.close()

def final_GC(new, old, bins, rang):

    # Calculate histogram bins then use imshow()
    # Weighted by mass
    #gal_count, xedges, yedges = np.histogram2d(new['y_scale'], new['z_scale'], bins=[bins, bins],range=([-rang,rang],[-rang,rang]), weights=new['mass'])
    old_xz, xedges, yedges = np.histogram2d(old['x_scale'], old['z_scale'], bins=[bins, bins],range=([-rang,rang],[-rang,rang]), weights=old['mass'])
    new_xz, xedges, yedges = np.histogram2d(new['x_scale'], new['z_scale'], bins=[bins, bins],range=([-rang,rang],[-rang,rang]), weights=new['mass'])
    new_xy, xedges, yedges = np.histogram2d(new['x_scale'], new['y_scale'], bins=[bins, bins],range=([-rang,rang],[-rang,rang]), weights=new['mass'])
    #old_count, xedges, yedges = np.histogram2d(new['z_scale'], new['x_scale'], bins=[bins, bins],range=([-rang,rang],[-rang,rang]), weights=new['mass'])
    old_xy, xedges, yedges = np.histogram2d(old['x_scale'], old['y_scale'], bins=[bins, bins],range=([-rang,rang],[-rang,rang]), weights=old['mass'])


    fig = plt.figure()
    gs = gridspec.GridSpec(2, 4, width_ratios=[1,1, 0.05, 0.05])
    cbax = plt.subplot(gs[:,3])
    '''
    ax0 = plt.subplot(gs[1,0]) # bottom left
    ax1 = plt.subplot(gs[1,1], sharey=ax0) # bottom right
    ax2 = plt.subplot(gs[0,0], sharex=ax0) # top left
    ax3 = plt.subplot(gs[0,1], sharex=ax1, sharey=ax2) # top right
    '''
    ax0 = plt.subplot(gs[1,0]) # bottom left
    ax1 = plt.subplot(gs[1,1]) # bottom right
    ax2 = plt.subplot(gs[0,0]) # top left
    ax3 = plt.subplot(gs[0,1]) # top right
    fig.set_size_inches(6, 6.05)

    plt.setp(ax1.get_yticklabels(), visible=False)
    plt.setp(ax2.get_xticklabels(), visible=False)
    plt.setp(ax3.get_yticklabels(), visible=False)
    plt.setp(ax3.get_xticklabels(), visible=False)

    gamma = 0.5
    #gamma = 0.4
    cmap = plt.cm.get_cmap('magma_r')

    gal_max = np.amax(old_xz)
    gas_max = np.amax(new_xz)
    new_max = np.amax(new_xy)
    old_max = np.amax(old_xy)

    all_max = max(gal_max, gas_max, new_max, old_max)

    props = dict(facecolor='white',alpha=0.9)
    vmin = 0
    #vmin = 1e3
    shading = 'quadric'


    im = ax0.imshow(old_xz.T, cmap=cmap, origin='lower', vmin=vmin, vmax=all_max, norm=mcolors.PowerNorm(gamma), interpolation=shading)
    ax0.set_xlabel("X (pc)")
    ax0.set_ylabel("Z (pc)")
    ax0.xaxis.set_minor_locator(AutoMinorLocator())
    ax0.yaxis.set_minor_locator(AutoMinorLocator())
    #ax0.text(5, 50, 'Disk Stars', bbox=props)

    #ax1.imshow(new_xz.T, cmap=cmap, origin='lower', vmin=vmin, vmax=all_max, norm=mcolors.PowerNorm(gamma), interpolation=shading)
    #ax1.scatter(new['x_scale'], new['z_scale'])
    ax1.imshow(new_xz.T, cmap=cmap, origin='lower', vmin=vmin, vmax=all_max, norm=mcolors.PowerNorm(gamma), interpolation=shading)
    ax1.set_xlabel("X (pc)")
    ax1.xaxis.set_minor_locator(AutoMinorLocator())
    ax1.yaxis.set_minor_locator(AutoMinorLocator())
    #ax1.text(5, 50, 'Gas', bbox=props)

    ax2.imshow(old_xy.T, cmap=cmap, origin='lower', vmin=vmin, vmax=all_max, norm=mcolors.PowerNorm(gamma), interpolation=shading)
    ax2.set_ylabel("Y (pc)")
    ax2.xaxis.set_minor_locator(AutoMinorLocator())
    ax2.yaxis.set_minor_locator(AutoMinorLocator())
    ax2.text(5, 52, '1G', bbox=props)


    ax3.imshow(new_xy.T, cmap=cmap, origin='lower', vmin=vmin, vmax=all_max, norm=mcolors.PowerNorm(gamma), interpolation=shading)
    ax3.xaxis.set_minor_locator(AutoMinorLocator())
    ax3.yaxis.set_minor_locator(AutoMinorLocator())
    ax3.text(5, 52, '2G', bbox=props)

    ax0.tick_params(direction='in', axis='both', which='both', bottom=True,top=True, left=True, right=True)
    ax1.tick_params(direction='in', axis='both', which='both', bottom=True,top=True, left=True, right=True)
    ax2.tick_params(direction='in', axis='both', which='both', bottom=True,top=True, left=True, right=True)
    ax3.tick_params(direction='in', axis='both', which='both', bottom=True,top=True, left=True, right=True)
    gs.update(left=0.05, right=0.95, bottom=0.08, top=0.93, wspace=0.0, hspace=0.0)

    cb = Colorbar(ax = cbax, mappable = im , format=ticker.FuncFormatter(fmt))
    #cb = Colorbar(ax = cbax, mappable = im)
    cb.set_label(r'M$_\odot$pc$^{-2}$', labelpad=10)
    plt.savefig("final_time_step_GC", bbox_inches='tight', dpi = 300)
    plt.close()


def final_ts_plot_all(gal, gas, new, old, bins, rang, iwas_x, iwas_y):

    # Calculate histogram bins then use imshow()
    # Weighted by mass
    gal_count, xedges, yedges = np.histogram2d(gal['x'], gal['y'], bins=[bins, bins],range=([-rang,rang],[-rang,rang]), weights=gal['mass'])
    gas_count, xedges, yedges = np.histogram2d(gas['x'], gas['y'], bins=[bins, bins],range=([-rang,rang],[-rang,rang]), weights=gas['mass'])
    new_count, xedges, yedges = np.histogram2d(new['x'], new['y'], bins=[bins, bins],range=([-rang,rang],[-rang,rang]), weights=new['mass'])
    old_count, xedges, yedges = np.histogram2d(old['x'], old['y'], bins=[bins, bins],range=([-rang,rang],[-rang,rang]), weights=old['mass'])


    fig = plt.figure()
    gs = gridspec.GridSpec(2, 4, width_ratios=[1,1, 0.05, 0.05])
    cbax = plt.subplot(gs[:,3])
    ax0 = plt.subplot(gs[1,0]) # bottom left
    ax1 = plt.subplot(gs[1,1], sharey=ax0) # bottom right
    ax2 = plt.subplot(gs[0,0], sharex=ax0) # top left
    ax3 = plt.subplot(gs[0,1], sharex=ax1, sharey=ax2) # top right
    fig.set_size_inches(6, 6.05)

    plt.setp(ax1.get_yticklabels(), visible=False)
    plt.setp(ax2.get_xticklabels(), visible=False)
    plt.setp(ax3.get_yticklabels(), visible=False)
    plt.setp(ax3.get_xticklabels(), visible=False)

    gamma = 0.2
    cmap = plt.cm.get_cmap('magma_r')
    shading = 'quadric'

    gal_max = np.amax(gal_count)
    gas_max = np.amax(gas_count)
    new_max = np.amax(new_count)
    old_max = np.amax(old_count)

    all_max = max(gal_max, gas_max, new_max, old_max)

    props = dict(facecolor='white',alpha=0.9)


    im = ax0.imshow(gal_count.T, cmap=cmap, origin='lower', vmin=0, vmax=all_max, norm=mcolors.PowerNorm(gamma), interpolation=shading)
    ax0.scatter(iwas_x, iwas_y, s=500, facecolors='none', edgecolors='k', zorder=5)
    ax0.set_xlabel("X (pc)")
    ax0.set_ylabel("Y (pc)")
    ax0.xaxis.set_minor_locator(AutoMinorLocator())
    ax0.yaxis.set_minor_locator(AutoMinorLocator())
    ax0.text(100, 1800, 'Disc Stars', bbox=props)

    ax1.imshow(gas_count.T, cmap=cmap, origin='lower', vmin=0, vmax=all_max, norm=mcolors.PowerNorm(gamma), interpolation=shading)
    ax1.scatter(iwas_x, iwas_y, s=500, facecolors='none', edgecolors='k', zorder=5)
    ax1.set_xlabel("X (pc)")
    ax1.xaxis.set_minor_locator(AutoMinorLocator())
    ax1.yaxis.set_minor_locator(AutoMinorLocator())
    ax1.text(100, 1800, 'Gas', bbox=props)

    ax2.imshow(old_count.T, cmap=cmap, origin='lower', vmin=0, vmax=all_max, norm=mcolors.PowerNorm(gamma), interpolation=shading)
    ax2.scatter(iwas_x, iwas_y, s=500, facecolors='none', edgecolors='k', zorder=5)
    ax2.set_ylabel("Y (pc)")
    ax2.xaxis.set_minor_locator(AutoMinorLocator())
    ax2.yaxis.set_minor_locator(AutoMinorLocator())
    ax2.text(100, 1800, '1G', bbox=props)


    ax3.imshow(new_count.T, cmap=cmap, origin='lower', vmin=0, vmax=all_max, norm=mcolors.PowerNorm(gamma), interpolation=shading)
    ax3.scatter(iwas_x, iwas_y, s=500, facecolors='none', edgecolors='k', zorder=5)
    ax3.xaxis.set_minor_locator(AutoMinorLocator())
    ax3.yaxis.set_minor_locator(AutoMinorLocator())
    ax3.text(100, 1800, '2G', bbox=props)

    ax0.tick_params(direction='in', axis='both', which='both', bottom=True,top=True, left=True, right=True)
    ax1.tick_params(direction='in', axis='both', which='both', bottom=True,top=True, left=True, right=True)
    ax2.tick_params(direction='in', axis='both', which='both', bottom=True,top=True, left=True, right=True)
    ax3.tick_params(direction='in', axis='both', which='both', bottom=True,top=True, left=True, right=True)
    gs.update(left=0.05, right=0.95, bottom=0.08, top=0.93, wspace=0.0, hspace=0.0)

    cb = Colorbar(ax = cbax, mappable = im , format=ticker.FuncFormatter(fmt))
    cb.set_label(r'M$_\odot$pc$^{-2}$', labelpad=10)
    plt.savefig("final_time_step_all", bbox_inches='tight', dpi = 300)
    plt.close()


def binned_rotation(x, old_rot, new_rot):

    fig, ax = plt.subplots(1,3)
    fig.set_size_inches(15, 5)

    ax[0].plot(x, old_rot[0], 'k')
    old = ax[0].scatter(x, old_rot[0], color='red')

    ax[0].plot(x, new_rot[0], 'k')
    new = ax[0].scatter(x, new_rot[0], color='blue')

    ax[0].set_xlabel("X (pc)")
    ax[0].set_ylabel("Vy (kms$^{-1}$)")
    ax[0].xaxis.set_minor_locator(AutoMinorLocator())
    ax[0].yaxis.set_minor_locator(AutoMinorLocator())

    ax[1].scatter(x, old_rot[1], color='red')
    ax[1].plot(x, old_rot[1], 'k')

    ax[1].scatter(x, new_rot[1], color='blue')
    ax[1].plot(x, new_rot[1], 'k')

    ax[1].set_xlabel("X (pc)")
    ax[1].set_ylabel("Vz (kms$^{-1}$)")
    ax[1].xaxis.set_minor_locator(AutoMinorLocator())
    ax[1].yaxis.set_minor_locator(AutoMinorLocator())

    ax[2].scatter(x, old_rot[2], color='red')
    ax[2].plot(x, old_rot[2], 'k')

    ax[2].scatter(x, new_rot[2], color='blue')
    ax[2].plot(x, new_rot[2], 'k')

    ax[2].set_xlabel("Y (pc)")
    ax[2].set_ylabel("V$_x$ (kms$^{-1}$)")
    ax[2].xaxis.set_minor_locator(AutoMinorLocator())
    ax[2].yaxis.set_minor_locator(AutoMinorLocator())

    ax[0].tick_params(direction='in', axis='both', which='both', bottom=True,top=True, left=True, right=True)
    ax[1].tick_params(direction='in', axis='both', which='both', bottom=True,top=True, left=True, right=True)
    ax[2].tick_params(direction='in', axis='both', which='both', bottom=True,top=True, left=True, right=True)

    plt.legend((old, new), ('Old stars', 'New stars'), markerscale=1)
    plt.tight_layout()
    plt.savefig("binned_rotation_all")
    plt.close()

def position_3d(arr, iwas):
    '''
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.quiver(arr['x_scale'], arr['y_scale'],arr['z_scale'],arr['vx_scale'], arr['vy_scale'], arr['vz_scale'],length=1, normalize=False)
    ax.scatter(iwas[0], iwas[1],iwas[2])
    ax.set_xlim(-50,50)
    ax.set_ylim(-50,50)
    ax.set_zlim(-50,50)
    ax.set_xlabel("X (pc)")
    ax.set_ylabel("Y (pc)")
    ax.set_zlabel("Z (pc)")
    '''
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(arr[arr['r']<=50]['x_scale'], arr[arr['r']<=50]['y_scale'],arr[arr['r']<=50]['z_scale'])
    ax.scatter(iwas[0], iwas[1],iwas[2])
    ax.set_xlim(-50,50)
    ax.set_ylim(-50,50)
    ax.set_zlim(-50,50)
    ax.set_xlabel("X (pc)")
    ax.set_ylabel("Y (pc)")
    ax.set_zlabel("Z (pc)")

    plt.show()
    plt.close()

def plot_mass_ratio_new(new, old, f_en, mass):

    rang = 25
    bins = rang*2


    new_count, xedges, yedges = np.histogram2d(new['x_scale'], new['y_scale'], bins=[bins, bins],range=([-rang,rang],[-rang,rang]), weights=new['mass'])
    old_count, xedges, yedges = np.histogram2d(old['x_scale'], old['y_scale'], bins=[bins, bins],range=([-rang,rang],[-rang,rang]), weights=old['mass'])


    fig = plt.figure()
    gs = gridspec.GridSpec(ncols=3, nrows=2, width_ratios=[1,1, 0.05], height_ratios=[1,0.5])
    cbax = plt.subplot(gs[:,2])
    ax0 = plt.subplot(gs[0,0]) # top left
    ax1 = plt.subplot(gs[0,1], sharey=ax0) # top right
    ax2 = plt.subplot(gs[1,0:2]) # bottom row

    fig.set_size_inches(8, 6)

    plt.setp(ax1.get_yticklabels(), visible=False) # Dont want to see top right y labels


    gamma = 0.3
    cmap = plt.cm.get_cmap('binary')

    # Normalise the histogram
    new_max = np.amax(new_count)
    old_max = np.amax(old_count)

    all_max = max(new_max, old_max)

    props = dict( facecolor='white',alpha=0.9)


    im = ax0.imshow(old_count.T, cmap=cmap, origin='lower', vmin=0, vmax=all_max, norm=mcolors.PowerNorm(gamma))
    #im = ax0.quiver(old.x_scale,old.y_scale,old.vx_scale,old.vy_scale)
    ax0.set_xlabel("X (pc)")
    ax0.set_ylabel("Y (pc)")
    ax0.set_xlim([-rang, rang])
    ax0.set_ylim([-rang, rang])
    ax0.xaxis.set_label_position('top')
    ax0.xaxis.set_minor_locator(AutoMinorLocator())
    ax0.yaxis.set_minor_locator(AutoMinorLocator())
    ax0.text(2, 25, '1G', bbox=props)

    ax1.imshow(new_count.T, cmap=cmap, origin='lower', vmin=0, vmax=all_max, norm=mcolors.PowerNorm(gamma))
    #ax1.quiver(new.x_scale,new.y_scale,new.vx_scale,new.vy_scale)
    ax1.set_xlim([-rang, rang])
    ax1.set_ylim([-rang, rang])
    ax1.set_xlabel("X (pc)")
    ax1.xaxis.set_label_position('top')
    ax1.xaxis.set_minor_locator(AutoMinorLocator())
    ax1.yaxis.set_minor_locator(AutoMinorLocator())
    ax1.text(2, 25, '2G', bbox=props)


    #plt.plot(x, mass, 'k')
    #ax.scatter(x, mass, color='lightsteelblue')
    ax2.scatter(f_en, mass, color='black')

    ax2.set_xlabel("Radius (pc)")
    ax2.set_ylabel("f$_{enritched}$")
    ax2.xaxis.set_minor_locator(AutoMinorLocator())
    ax2.yaxis.set_minor_locator(AutoMinorLocator())
    #plt.tight_layout()
    ax0.tick_params(direction='in', axis='both', which='both', bottom=True,top=True, left=True, right=True)
    ax1.tick_params(direction='in', axis='both', which='both', bottom=True,top=True, left=True, right=True)
    ax2.tick_params(direction='in', axis='both', which='both', bottom=True,top=True, left=True, right=True)

    #gs.update(wspace=0.0)
    cb = Colorbar(ax = cbax, mappable = im , format=ticker.FuncFormatter(fmt))


    plt.savefig("mass_ratio_new")
    plt.close()

def plot_mass_ratio_new_2(new, old, f_en, mass):

    rang = 25
    bins = rang*2


    new_count, xedges, yedges = np.histogram2d(new['x_scale'], new['y_scale'], bins=[bins, bins],range=([-rang,rang],[-rang,rang]), weights=new['mass'])
    old_count, xedges, yedges = np.histogram2d(old['x_scale'], old['y_scale'], bins=[bins, bins],range=([-rang,rang],[-rang,rang]), weights=old['mass'])


    fig = plt.figure()
    gs = gridspec.GridSpec(ncols=3, nrows=2, width_ratios=[1,1, 0.05], height_ratios=[1,0.5])
    cbax = plt.subplot(gs[:,2])
    ax0 = plt.subplot(gs[0,0]) # top left
    ax1 = plt.subplot(gs[0,1], sharey=ax0) # top right
    ax2 = plt.subplot(gs[1,0:2]) # bottom row

    fig.set_size_inches(8, 6)

    plt.setp(ax1.get_yticklabels(), visible=False) # Dont want to see top right y labels


    gamma = 0.3
    cmap = plt.cm.get_cmap('binary')

    # Normalise the histogram
    new_max = np.amax(new_count)
    old_max = np.amax(old_count)

    all_max = max(new_max, old_max)

    props = dict( facecolor='white',alpha=0.9)


    #im = ax0.imshow(old_count.T, cmap=cmap, origin='lower', vmin=0, vmax=all_max, norm=mcolors.PowerNorm(gamma))
    im = ax0.quiver(old.x_scale,old.y_scale,old.vx_scale,old.vy_scale)
    ax0.set_xlabel("X (pc)")
    ax0.set_ylabel("Y (pc)")
    ax0.set_xlim([-rang, rang])
    ax0.set_ylim([-rang, rang])
    ax0.xaxis.set_label_position('top')
    ax0.xaxis.set_minor_locator(AutoMinorLocator())
    ax0.yaxis.set_minor_locator(AutoMinorLocator())
    ax0.text(2, 25, '1G', bbox=props)

    #ax1.imshow(new_count.T, cmap=cmap, origin='lower', vmin=0, vmax=all_max, norm=mcolors.PowerNorm(gamma))
    ax1.quiver(new.x_scale,new.y_scale,new.vx_scale,new.vy_scale)
    ax1.set_xlim([-rang, rang])
    ax1.set_ylim([-rang, rang])
    ax1.set_xlabel("X (pc)")
    ax1.xaxis.set_label_position('top')
    ax1.xaxis.set_minor_locator(AutoMinorLocator())
    ax1.yaxis.set_minor_locator(AutoMinorLocator())
    ax1.text(2, 25, '2G', bbox=props)


    #plt.plot(x, mass, 'k')
    #ax.scatter(x, mass, color='lightsteelblue')
    ax2.scatter(f_en, mass, color='black')

    ax2.set_xlabel("Radius (pc)")
    ax2.set_ylabel("f$_{enritched}$")
    ax2.xaxis.set_minor_locator(AutoMinorLocator())
    ax2.yaxis.set_minor_locator(AutoMinorLocator())
    #plt.tight_layout()
    ax0.tick_params(direction='in', axis='both', which='both', bottom=True,top=True, left=True, right=True)
    ax1.tick_params(direction='in', axis='both', which='both', bottom=True,top=True, left=True, right=True)
    ax2.tick_params(direction='in', axis='both', which='both', bottom=True,top=True, left=True, right=True)

    #gs.update(wspace=0.0)
    cb = Colorbar(ax = cbax, mappable = im , format=ticker.FuncFormatter(fmt))


    plt.savefig("mass_ratio_new_2")
    plt.close()

def plot_mass_ratio(x, mass):
    fig, ax = plt.subplots(1,1)

    fig.set_size_inches(6, 4)

    plt.plot(x, mass, 'k')
    #plt.plot(x, mass+std)
    #ax.scatter(x, mass, color='lightsteelblue')
    ax.scatter(x, mass, color='black')


    ax.set_xlabel("Radius (pc)")
    ax.set_ylabel("f$_{enritched}$")
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    plt.tight_layout()
    ax.tick_params(direction='in', axis='both', which='both', bottom=True,top=True, left=True, right=True)

    plt.savefig("mass_ratio")
    plt.close()


def plot_total_orbit(time):
    ''' Not the one I'm using for the paper'''
    fig, ax = plt.subplots(1,1)
    fig.set_size_inches(15, 12)

    dwarf     = ax.plot(time['time'], time['dwarf'])
    gas       = ax.plot(time['time'], time['gas'])
    new_stars = ax.plot(time['time'], time['new_stars'])
    gc        = ax.plot(time['time'], time['GC'], 'g')
    total_gc  = ax.plot(time['time'], time['total_gc'])
    total_agb = ax.plot(time['time'], time['total_AGB'])
    gc_agb    = ax.plot(time['time'], time['GC_AGB'])



    plt.legend((dwarf[0], gas[0], new_stars[0], gc[0], total_gc[0], total_agb[0],gc_agb[0] ), ('dwarf stars', 'gas', 'new stars', 'GC stars', 'total GC stars', 'total AGB', 'gc AGB'), markerscale=10)
    ax.tick_params(direction='in', axis='both', which='both', bottom=True,top=True, left=True, right=True)
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    plt.yscale("log")
    ax.set_xlabel("Time (Myr)")
    ax.set_ylabel("Mass ($M_{\odot}$)")
    ax.set_ylim(top=1e7)
    plt.savefig('orbit_masses.png')
    plt.close()

def plot_orbit_gc(time):
    ''' Time evolution plot I'm using in the paper'''
    fig, ax = plt.subplots(1,1, constrained_layout=True)
    #fig, ax = plt.subplots(1,1)
    fig.set_size_inches(8, 5)

    # Plot from least to most important
    ax.plot(time['time'], time['dwarf'], color='xkcd:pea', label = 'Disc Stars', linewidth=0.75)
    ax.plot(time['time'], time['GC_AGB'], color='xkcd:orchid', linestyle=':', dashes=(1, 2.5), label = 'AGB gas')
    ax.plot(time['time'], (time.gas-time['GC_AGB']), color='xkcd:peach', linestyle=':', dashes=(1, 1), label = 'ISM')


    ax.plot(time['time'], time['total_gc'],color='xkcd:dark seafoam', label= 'Total GC',linewidth=1.25)
    ax.plot(time['time'], time['new_stars'], color=new_col, linestyle='--', dashes=(4, 1), label = '2G', linewidth=1)
    ax.plot(time['time'], time['GC'], color=old_col, linestyle='--', dashes=(7, 3), label = '1G', linewidth=1)


    #plt.legend((new_stars[0], gc[0], total_gc[0],gc_agb[0], gas[0], gal[0] ), ('2P', '1P', 'Total GC', 'AGB gas', 'ISM', 'Dwarf'), markerscale=20)
    #ax.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,ncol=3, mode="expand", borderaxespad=0., edgecolor='0', fancybox=False, frameon=True)
    ax.legend(ncol=2, borderaxespad=0., edgecolor='0', fancybox=False, frameon=True)
    ax.tick_params(direction='in', axis='both', which='both', bottom=True,top=True, left=True, right=True)
    plt.yscale("log")
    ax.set_xlabel("Time (Myr)")
    ax.set_ylabel(r"Mass ($M_{\odot}$)")
    ax.set_ylim(bottom=1e3)
    ax.set_xlim(left=0, right=375)
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    #plt.tight_layout
    plt.savefig('orbit_gc_mass.png',bbox='tight', dpi = 300)


def plot_gc_pos(x, y, z):

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax_bounds = 500
    ax.plot(x, y, z, 'k')
    ax.scatter(x[0], y[0], z[0], color = 'blue')
    ax.set_xlim(-ax_bounds,ax_bounds)
    ax.set_ylim(-ax_bounds,ax_bounds)
    ax.set_zlim(-ax_bounds,ax_bounds)
    ax.set_xlabel("X (pc)")
    ax.set_ylabel("Y (pc)")
    ax.set_zlabel("Z (pc)")

    #plt.show()



def plot_gc_pos_2D(x, y, x_dot, y_dot, time, dwarf_x, dwarf_y):

    fig, ax = plt.subplots(constrained_layout=True)
    #fig.set_size_inches(8 , 6)
    bounds = 1000
    gc_path = ax.plot(x, y, 'k', label='Path')

    cm = plt.cm.get_cmap('gist_rainbow')
    first_ts = np.load('gas_init.npy')


    ax.hist2d(first_ts[:,0], first_ts[:,1], bins=[300, 300], norm=mcolors.PowerNorm(0.3), cmap=plt.cm.get_cmap('binary'), range=([-bounds,bounds],[-bounds,bounds]))
    start = ax.scatter(x[0], y[0], color='red', marker='*', s =200, label='Start Pos.', zorder=5)

    dots = ax.scatter(x_dot, y_dot, c=time, cmap=cm)
    ax.set_xlabel("X (pc)")
    ax.set_ylabel("Y (pc)")
    ax.set_xlim(-bounds,bounds)
    ax.set_ylim(-bounds,bounds)
    ax.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,ncol=2, mode="expand", borderaxespad=0., edgecolor='0', fancybox=False, frameon=True)
    #plt.legend((start, gc_path[0]), ('GC Start Position', 'GC path'))
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())



    cbar = plt.colorbar(dots)
    cbar.set_label('Time (yr)')

    ax.tick_params(direction='in', axis='both', which='both', bottom=True,top=True, left=True, right=True)
    ax.axis('equal')
    #plt.tight_layout()
    plt.savefig('orbit_positions_cm', bbox_inches='tight', dpi = 300)
    #plt.show()

def full_orbit(x, y, x_dot, y_dot, time, gas, ns_1, ns_2):

    #fig, ax = plt.subplots(constrained_layout=True)
    fig, ax = plt.subplots()
    #fig.set_size_inches(6 , 5)
    bounds = 1000


    cm = plt.cm.get_cmap('rainbow_r')
    cmap_g = plt.cm.get_cmap('Greys')
    cmap_1 = plt.cm.get_cmap('RdPu')
    cmap_2 = plt.cm.get_cmap('YlGn')
    #first_ts = np.load('gas_init.npy')

    size = 0.08

    #ax.hist2d(first_ts[:,0], first_ts[:,1], bins=[300, 300], norm=mcolors.PowerNorm(0.3), cmap=plt.cm.get_cmap('binary'), range=([-bounds,bounds],[-bounds,bounds]))
    from scipy.ndimage import gaussian_filter
    gas_hist, xedges, yedges = np.histogram2d(gas.x, gas.y, bins=bounds*2 ,range=([-bounds,bounds],[-bounds,bounds]), weights=gas.mass)
    #ns_1_hist, xedges, yedges = np.histogram2d(ns_1.x, ns_1.y, bins=bounds*2 ,range=([-bounds,bounds],[-bounds,bounds]), weights=ns_1.mass)
    #ns_2_hist, xedges, yedges = np.histogram2d(ns_2.x, ns_2.y, bins=bounds*2 ,range=([-bounds,bounds],[-bounds,bounds]), weights=ns_2.mass)

    smoothing_sigma = 5
    gamma = 0.3

    gas_hist = gaussian_filter(gas_hist, sigma=smoothing_sigma)

    #ns_1_hist = gaussian_filter(ns_1_hist, sigma=smoothing_sigma)
    #ns_2_hist = gaussian_filter(ns_2_hist, sigma=smoothing_sigma)
    #nbins = 20
    #k = kde.gaussian_kde(ns_1_hist.T)
    #xi, yi = np.mgrid[x.min():x.max():nbins*1j, y.min():y.max():nbins*1j]
    #zi = k(np.vstack([xi.flatten(), yi.flatten()]))

    ax.imshow(gas_hist.T, cmap=cmap_g, origin='lower',  norm=mcolors.PowerNorm(gamma), extent=[-bounds, bounds, -bounds, bounds])
    #ax.pcolormesh(xi, yi, zi.reshape(xi.shape), shading='gouraud', cmap=cmap_1)

    #k = kde.gaussian_kde(ns_2_hist.T)
    #xi, yi = np.mgrid[x.min():x.max():nbins*1j, y.min():y.max():nbins*1j]
    #i = k(np.vstack([xi.flatten(), yi.flatten()]))
    #ax.pcolormesh(xi, yi, zi.reshape(xi.shape), shading='gouraud', cmap=cmap_2)

    #masked_1 = np.ma.masked_where(ns_1_hist == 0, ns_1_hist)
    #masked_2 = np.ma.masked_where(ns_2_hist == 0, ns_2_hist)

    #ax.imshow(masked_1.T, cmap=cmap_1, origin='lower', norm=mcolors.PowerNorm(gamma), extent=[-bounds, bounds, -bounds, bounds])
    #ax.imshow(masked_2.T, cmap=cmap_2, origin='lower', norm=mcolors.PowerNorm(gamma), extent=[-bounds, bounds, -bounds, bounds])

    #ax.scatter(gas, gas_y, marker=',', s=size, color='xkcd:slate grey', label='Gas', alpha = 0.1, zorder = 0)
    ax.scatter(np.NaN, np.NaN, marker=',', color='xkcd:slate grey', label='Gas')
    #ax.scatter(np.NaN, np.NaN, marker=',', s=size,color='xkcd:candy pink', label='Ex-situ')
    #ax.scatter(np.NaN, np.NaN, marker=',', s=size,color='xkcd:mint green',label='In-situ')
    #ax.scatter(ns_1_x, ns_1_y, marker=',', s=size,color='xkcd:candy pink', label='Ex-situ', alpha = 0.5, zorder = 1)
    #ax.scatter(ns_2_x, ns_2_y, marker=',', s=size, color='xkcd:mint green',label='In-situ', alpha = 0.5, zorder = 2)
    ax.plot(x, y, 'k', label='Path', zorder= 4)
    ax.scatter(x[0], y[0], color='red', marker='*', s =200, label='Start', zorder=5)
    #ax.plot(np.NaN, np.NaN, '-', color='none', label=' ')


    handles, labels = ax.get_legend_handles_labels()
    # sort both labels and handles by labels
    #labels, handles = zip(*sorted(zip(labels, handles), key=lambda t: t[0]))
    #ax.legend(handles, labels)
    #print(labels)
    #order = [2,0,4,1,3,5]
    #plt.legend([handles[idx] for idx in order],[labels[idx] for idx in order]

    dots = ax.scatter(x_dot, y_dot, c=time, cmap=cm, zorder = 6)
    ax.set_xlabel("X (pc)")
    ax.set_ylabel("Y (pc)")
    ax.set_xlim(-bounds,bounds)
    ax.set_ylim(-bounds,bounds)
    leg = ax.legend( bbox_to_anchor=(0., 1.02, 1., .052), mode="expand", borderaxespad=0., loc=3, ncol=3, edgecolor='0', fancybox=False, frameon=True)
    #ax.legend()
    #leg = ax.legend([handles[idx] for idx in order],[labels[idx] for idx in order], bbox_to_anchor=(0., 1.02, 1., .102), loc=3,ncol=3, mode="expand", borderaxespad=0., edgecolor='0', fancybox=False, frameon=True)
    #plt.legend((start, gc_path[0]), ('GC Start Position', 'GC path'))
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    #leg.legendHandles[0]._sizes = [40]
    #leg.legendHandles[2]._sizes = [40]
    #leg.legendHandles[4]._sizes = [40]


    cbar = plt.colorbar(dots)
    cbar.set_label('Time (Myr)')
    ax.yaxis.set_major_locator(MaxNLocator(nbins='auto', prune='lower'))
    ax.tick_params(direction='in', axis='both', which='both', bottom=True,top=True, left=True, right=True)
    #ax.axis('equal')
    #plt.tight_layout()
    #plt.show()
    plt.savefig('orbit_all', bbox_inches='tight', dpi = 300)

def star_formation_plots(ism, gas, time):
    fig, ax = plt.subplots(1,1)
    fig.set_size_inches(15, 12)
    ism_mass,= ax.semilogy(time, ism)
    gs_mass,= ax.semilogy(time, gas)
    ax.set_xlabel("Time (yrs)")
    ax.set_ylabel("Mass (Msun)")
    ax.set_title("AGB vs ISM masses")
    ax.tick_params(direction='in', axis='both', which='both', bottom=True,top=True, left=True, right=True)
    ax.legend((gs_mass, ism_mass), ('Mass from AGB', 'Mass from ISM'))
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    plt.savefig('SFR.png')

def star_formation_rate_plots(ism_rate, gas_rate, time):
    fig, ax = plt.subplots(1,1)
    fig.set_size_inches(15, 12)
    ism_rate, = ax.semilogy(time, ism_rate)
    gs_rate, = ax.semilogy(time, gas_rate)
    ax.set_xlabel("Time (yrs)")
    ax.set_ylabel("Star formation rate (Msun/yr)")
    ax.set_title("Star formation rate")
    ax.tick_params(direction='in', axis='both', which='both', bottom=True,top=True, left=True, right=True)
    ax.legend((gs_rate, ism_rate), ('Mass of gas accreted onto GC', 'Mass from ISM'))
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    plt.savefig('sf_rate.png')


def basic_rot_plot(x,y,rot_arr, old):
    fig, ax = plt.subplots(1,1)

    fig.set_size_inches(6 , 5)
    bounds = 10
    bin_size = 20

    h = ax.hist2d(old.x_scale, old.y_scale, bins=[bin_size, bin_size], norm=mcolors.PowerNorm(0.8), cmap=plt.cm.get_cmap('binary'), range=([-bounds,bounds],[-bounds,bounds]), weights=old.mass)
    cbar = plt.colorbar(h[3])

    cbar.ax.set_ylabel('particle count')
    ax.scatter(x, y, c='black')
    fg = ax.quiver(x,y,rot_arr.gc_vx,rot_arr.gc_vy, color='red')
    sg = ax.quiver(x,y,rot_arr.ns_vx,rot_arr.ns_vy, color='blue')


    ax.set_xlabel("X (pc)")
    ax.set_ylabel("Y (pc)")
    ax.set_xlim(-bounds,bounds)
    ax.set_ylim(-bounds,bounds)

    plt.legend((fg, sg), ('1P', '2P'))
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.tick_params(direction='in', axis='both', which='both', bottom=True,top=True, left=True, right=True)
    ax.axis('equal')
    plt.savefig('polar_pos_rotation', bbox_inches='tight')



def rot_theta_plot(theta, rot_arr):
    fig, ax = plt.subplots(3,2, sharex=True, sharey=True)
    fig.set_size_inches(12, 15)

    ax[0,0].errorbar(theta, rot_arr.gc_vx, yerr=rot_arr.gc_vx_std)
    ax[0,0].set_ylabel("Vx (km/s)")

    ax[1,0].errorbar(theta, rot_arr.gc_vy, yerr=rot_arr.gc_vy_std)
    ax[1,0].set_ylabel("Vy (km/s)")

    ax[2,0].errorbar(theta, rot_arr.gc_vz, yerr=rot_arr.gc_vz_std)
    ax[2,0].set_ylabel("Vz (km/s)")
    ax[2,0].set_xlabel("Theta (deg)")

    ax[0,1].errorbar(theta, rot_arr.ns_vx, yerr=rot_arr.ns_vx_std)
    ax[1,1].errorbar(theta, rot_arr.ns_vy, yerr=rot_arr.ns_vy_std)
    ax[2,1].errorbar(theta, rot_arr.ns_vz, yerr=rot_arr.ns_vz_std)
    ax[2,1].set_xlabel("Theta (deg)")


def rot_theta__overlay_plot_gridspec(theta, rot_arr):

    # Use graphics grid to put legend into its own axis

    fig = plt.figure()
    gs = gridspec.GridSpec(4, 1, hight_ratios=[0.05,1, 1, 1])
    leg = plt.subplot(gs[0])
    ax0 = plt.subplot(gs[1]) # Vx
    ax1 = plt.subplot(gs[2], sharex=ax0) # Vy
    ax2 = plt.subplot(gs[3], sharex=ax0) # Vz
    fig.set_size_inches(6, 9)

    # Hide axis for the top two plots
    plt.setp(ax0.get_xticklabels(), visible=False)
    plt.setp(ax1.get_xticklabels(), visible=False)

    fig, ax = plt.subplots(3,1, sharex=True, sharey=True)
    fig.set_size_inches(6, 9)

    fg = ax[0].scatter(theta, rot_arr.gc_vx, color=old_col, marker='s')
    ax[0].fill_between(theta, rot_arr.gc_vx - rot_arr.gc_vx_std, rot_arr.gc_vx + rot_arr.gc_vx_std, color='r', alpha=0.2)

    ax[0].set_ylabel("$V_x$ (km$s^{-1})$")

    ax[1].scatter(theta, rot_arr.gc_vy, color=old_col, marker='s')
    ax[1].fill_between(theta, rot_arr.gc_vy - rot_arr.gc_vy_std, rot_arr.gc_vy + rot_arr.gc_vy_std, color='r', alpha=0.2)
    ax[1].set_ylabel("$V_y$ (km$s^{-1}$)")

    ax[2].scatter(theta, rot_arr.gc_vz, color=old_col, marker='s')
    ax[2].fill_between(theta, rot_arr.gc_vz - rot_arr.gc_vz_std, rot_arr.gc_vz + rot_arr.gc_vz_std, color='r', alpha=0.2)
    ax[2].set_ylabel("$V_z$ (km$s^{-1}$)")

    sg = ax[0].scatter(theta, rot_arr.ns_vx, color=new_col, marker='D')
    ax[0].fill_between(theta, rot_arr.ns_vx - rot_arr.ns_vx_std, rot_arr.ns_vx + rot_arr.ns_vx_std, color='b', alpha=0.2)
    ax[1].scatter(theta, rot_arr.ns_vy, color=new_col, marker='D')
    ax[1].fill_between(theta, rot_arr.ns_vy - rot_arr.ns_vy_std, rot_arr.ns_vy + rot_arr.ns_vy_std, color='b', alpha=0.2)
    ax[2].scatter(theta, rot_arr.ns_vz, color=new_col, marker='D')
    ax[2].fill_between(theta, rot_arr.ns_vz - rot_arr.ns_vz_std, rot_arr.ns_vz + rot_arr.ns_vz_std, color='b', alpha=0.2)
    ax[2].set_xlabel(r"$\theta$ (deg)")

    plt.legend((fg, sg), ('1G', '2G'))
    ax[0].xaxis.set_minor_locator(AutoMinorLocator())
    ax[0].yaxis.set_minor_locator(AutoMinorLocator())

    ax[1].xaxis.set_minor_locator(AutoMinorLocator())
    ax[1].yaxis.set_minor_locator(AutoMinorLocator())

    ax[1].xaxis.set_minor_locator(AutoMinorLocator())
    ax[1].yaxis.set_minor_locator(AutoMinorLocator())

    ax[0].tick_params(direction='in', axis='both', which='both', bottom=True,top=True, left=True, right=True)
    ax[1].tick_params(direction='in', axis='both', which='both', bottom=True,top=True, left=True, right=True)
    ax[2].tick_params(direction='in', axis='both', which='both', bottom=True,top=True, left=True, right=True)

    plt.subplots_adjust(wspace=0, hspace=0)
    plt.savefig('polar_rotation', bbox_inches='tight')
    plt.tight_layout()

    #plt.show()

def sine_fit(x, a, b, c, d):
    return a * np.sin(b * x +c)+d




def rot_theta__overlay_plot(theta, rot_arr):

    # Use graphics grid to put legend into its own axis
    params_gcx, params_covariance = optimize.curve_fit(sine_fit, theta, rot_arr.gc_vx, p0=[10, 0.017, 0, 0])
    params_gcy, params_covariance = optimize.curve_fit(sine_fit, theta, rot_arr.gc_vy, p0=[10, 0.017, 0, 0])
    params_gcz, params_covariance = optimize.curve_fit(sine_fit, theta, rot_arr.gc_vz, p0=[1, 0.017, 0, 0])

    params_nsx, params_covariance = optimize.curve_fit(sine_fit, theta, rot_arr.ns_vx, p0=[10, 0.017, 0, 0])
    params_nsy, params_covariance = optimize.curve_fit(sine_fit, theta, rot_arr.ns_vy, p0=[10, 0.017, 0, 0])
    params_nsz, params_covariance = optimize.curve_fit(sine_fit, theta, rot_arr.ns_vz, p0=[1, 0.017, 0, 0])

    fig, ax = plt.subplots(3,1, sharex=True, sharey=True)
    fig.set_size_inches(6, 9)

    ax[0].scatter(theta, rot_arr.gc_vx, color=old_col, marker='s', label='1G')
    # Add this to put the 1 sigma axis back in label=r'1 $\sigma$'
    ax[0].fill_between(theta, rot_arr.gc_vx - rot_arr.gc_vx_std, rot_arr.gc_vx + rot_arr.gc_vx_std, color='r', alpha=0.2)
    ax[0].plot(theta, sine_fit(theta, params_gcx[0], params_gcx[1], params_gcx[2], params_gcx[3]), color='r', alpha=0.5, zorder=-2)
    ax[0].set_ylabel("$V_x$ (km$s^{-1})$")


    ax[1].scatter(theta, rot_arr.gc_vy, color=old_col, marker='s', label='1G')
    ax[1].fill_between(theta, rot_arr.gc_vy - rot_arr.gc_vy_std, rot_arr.gc_vy + rot_arr.gc_vy_std, color='r', alpha=0.2)
    ax[1].plot(theta, sine_fit(theta, params_gcy[0], params_gcy[1], params_gcy[2], params_gcy[3]), color='r', alpha=0.5, zorder=-2)
    ax[1].set_ylabel("$V_y$ (km$s^{-1}$)")



    ax[2].scatter(theta, rot_arr.gc_vz, color=old_col, marker='s', label='1G')
    ax[2].fill_between(theta, rot_arr.gc_vz - rot_arr.gc_vz_std, rot_arr.gc_vz + rot_arr.gc_vz_std, color='r', alpha=0.2)
    ax[2].plot(theta, sine_fit(theta, params_gcz[0], params_gcz[1], params_gcz[2], params_gcz[3]), color='r', alpha=0.5, zorder=-2)
    ax[2].set_ylabel("$V_z$ (km$s^{-1}$)")



    ax[0].scatter(theta, rot_arr.ns_vx, color=new_col, marker='D', label='2G')
    ax[0].fill_between(theta, rot_arr.ns_vx - rot_arr.ns_vx_std, rot_arr.ns_vx + rot_arr.ns_vx_std, color='b', alpha=0.2)
    ax[0].plot(theta, sine_fit(theta, params_nsx[0], params_nsx[1], params_nsx[2], params_nsx[3]), color='b', alpha=0.5, zorder=-1)
    ax[1].scatter(theta, rot_arr.ns_vy, color=new_col, marker='D', label='2G')
    ax[1].fill_between(theta, rot_arr.ns_vy - rot_arr.ns_vy_std, rot_arr.ns_vy + rot_arr.ns_vy_std, color='b', alpha=0.2)
    ax[1].plot(theta, sine_fit(theta, params_nsy[0], params_nsy[1], params_nsy[2], params_nsy[3]), color='b', alpha=0.5, zorder=-2)
    ax[2].scatter(theta, rot_arr.ns_vz, color=new_col, marker='D', label='2G')
    ax[2].fill_between(theta, rot_arr.ns_vz - rot_arr.ns_vz_std, rot_arr.ns_vz + rot_arr.ns_vz_std, color='b', alpha=0.2)
    ax[2].plot(theta, sine_fit(theta, params_nsz[0], params_nsz[1], params_nsz[2], params_nsz[3]), color='b', alpha=0.5, zorder=-2)
    ax[2].xaxis.set_ticks(np.arange(0, 721, 90))
    ax[2].set_xlabel(r"$\theta$ (deg)")

    # Want it on top of the top axis
    ax[0].legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,ncol=2, mode="expand", borderaxespad=0., edgecolor='0', fancybox=False, frameon=True)
    ax[0].xaxis.set_minor_locator(AutoMinorLocator())
    ax[0].yaxis.set_minor_locator(AutoMinorLocator())

    ax[1].xaxis.set_minor_locator(AutoMinorLocator())
    ax[1].yaxis.set_minor_locator(AutoMinorLocator())

    ax[1].xaxis.set_minor_locator(AutoMinorLocator())
    ax[1].yaxis.set_minor_locator(AutoMinorLocator())

    ax[0].tick_params(direction='in', axis='both', which='both', bottom=True,top=True, left=True, right=True)
    ax[1].tick_params(direction='in', axis='both', which='both', bottom=True,top=True, left=True, right=True)
    ax[2].tick_params(direction='in', axis='both', which='both', bottom=True,top=True, left=True, right=True)

    ax[0].set_xlim(left = 0,right = 720)

    plt.subplots_adjust(wspace=0, hspace=0)
    plt.savefig('polar_rotation', bbox_inches='tight', dpi = 300)
    #plt.tight_layout()

    write_rotation(params_gcx[0], params_gcy[0], params_gcz[0], params_nsx[0], params_nsy[0], params_nsz[0])







def xyz_vel_plot(x,y,z, vx, vy,vz):
    fig, ax = plt.subplots(2,1, sharex=True, sharey=True)
    fig.set_size_inches(3.5, 6)
    ax[0].quiver(x,y, vx, vy, scale=None)
    ax[0].vlines(0, -20,20, color='red', linewidth=0.5)
    ax[0].hlines(0, -20,20, color='red', linewidth=0.5)
    ax[1].vlines(0, -20,20, color='red', linewidth=0.5)
    ax[1].hlines(0, -20,20, color='red', linewidth=0.5)

    ax[1].quiver(x,z, vx, vz)
    #ax[0].scatter(0,0, color="red")
    ax[0].tick_params(direction='in', axis='both', which='both', bottom=True,top=True, left=True, right=True)
    ax[1].tick_params(direction='in', axis='both', which='both', bottom=True,top=True, left=True, right=True)
    ax[1].set_xlabel("X (pc)")
    ax[0].set_ylabel("Y (pc)")
    ax[1].set_ylabel("Z (pc)")
    ax[0].set_xlim([-20,20])
    ax[0].set_ylim([-20,20])
    ax[1].set_ylim([-20,20])
    ax[0].xaxis.set_minor_locator(AutoMinorLocator())
    ax[0].yaxis.set_minor_locator(AutoMinorLocator())

    ax[1].xaxis.set_minor_locator(AutoMinorLocator())
    ax[1].yaxis.set_minor_locator(AutoMinorLocator())
    plt.subplots_adjust(wspace=0, hspace=0)

    plt.savefig('new_stars_quiver', bbox_inches='tight', dpi=300)
    #plt.show()


def cumulative_hist(old_r, new_r):

    n_bins = 100

    fig, ax = plt.subplots(1,1)
    fig.set_size_inches(6 , 4)


    ax.hist(old_r, n_bins, density=True, histtype='step',
                           cumulative=True, label='1G', color='red')

    ax.hist(new_r, n_bins, density=True, histtype='step',
                            cumulative=True, label='2G', color='blue')


    ax.legend(loc='upper left')
    ax.set_xlabel("Radius (pc)")
    ax.set_ylabel("Normalised Count")
    #ax.set_xlim(right=20)
    ax.tick_params(direction='in', axis='both', which='both', bottom=True,top=True, left=True, right=True)
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    plt.savefig('cum_dist_plot', bbox_inches='tight')

def init_state(gal, gas, bins, rang):
    # Calculate histogram bins then use imshow()
    # Weighted by mass
    gal_county, xedges, yedges = np.histogram2d(gal[:,0], gal[:,1], bins=[bins, bins],range=([-rang,rang],[-rang,rang]), weights=gal[:,8])
    gas_county, xedges, yedges = np.histogram2d(gas[:,0], gas[:,1], bins=[bins, bins],range=([-rang,rang],[-rang,rang]), weights=gas[:,8])
    gal_countz, xedges, yedges = np.histogram2d(gal[:,0], gal[:,2], bins=[bins, bins],range=([-rang,rang],[-rang,rang]), weights=gal[:,8])
    gas_countz, xedges, yedges = np.histogram2d(gas[:,0], gas[:,2], bins=[bins, bins],range=([-rang,rang],[-rang,rang]), weights=gas[:,8])


    fig = plt.figure()
    gs = gridspec.GridSpec(2, 4, width_ratios=[1,1, 0.05, 0.05])
    cbax = plt.subplot(gs[:,3])
    ax0 = plt.subplot(gs[1,0]) # bottom left
    ax1 = plt.subplot(gs[1,1], sharey=ax0) # bottom right
    ax2 = plt.subplot(gs[0,0], sharex=ax0) # top left
    ax3 = plt.subplot(gs[0,1], sharex=ax1, sharey=ax2) # top right
    fig.set_size_inches(6, 6.05)

    plt.setp(ax1.get_yticklabels(), visible=False)
    plt.setp(ax2.get_xticklabels(), visible=False)
    plt.setp(ax3.get_yticklabels(), visible=False)
    plt.setp(ax3.get_xticklabels(), visible=False)

    gamma = 0.2
    cmap = plt.cm.get_cmap('magma_r')
    shading = 'quadric'

    gal_max = np.amax(gal_county)
    gas_max = np.amax(gas_county)
    new_max = np.amax(gal_countz)
    old_max = np.amax(gas_countz)

    all_max = max(gal_max, gas_max, new_max, old_max)

    props = dict(facecolor='white',alpha=0.9)


    im = ax0.imshow(gal_countz.T, cmap=cmap, origin='lower', vmin=0, vmax=all_max, norm=mcolors.PowerNorm(gamma), interpolation=shading)

    ax0.set_xlabel("X (pc)")
    ax0.set_ylabel("Z (pc)")
    ax0.xaxis.set_minor_locator(AutoMinorLocator())
    ax0.yaxis.set_minor_locator(AutoMinorLocator())
    #ax0.text(100, 1800, 'Disc Stars', bbox=props)

    ax1.imshow(gas_countz.T, cmap=cmap, origin='lower', vmin=0, vmax=all_max, norm=mcolors.PowerNorm(gamma), interpolation=shading)

    ax1.set_xlabel("X (pc)")
    ax1.xaxis.set_minor_locator(AutoMinorLocator())
    ax1.yaxis.set_minor_locator(AutoMinorLocator())
    #ax1.text(100, 1800, 'Gas', bbox=props)

    ax2.imshow(gal_county.T, cmap=cmap, origin='lower', vmin=0, vmax=all_max, norm=mcolors.PowerNorm(gamma), interpolation=shading)

    ax2.set_ylabel("Y (pc)")
    ax2.xaxis.set_minor_locator(AutoMinorLocator())
    ax2.yaxis.set_minor_locator(AutoMinorLocator())
    ax2.text(200, 3500, 'Disc stars', bbox=props)


    ax3.imshow(gas_county.T, cmap=cmap, origin='lower', vmin=0, vmax=all_max, norm=mcolors.PowerNorm(gamma), interpolation=shading)

    ax3.xaxis.set_minor_locator(AutoMinorLocator())
    ax3.yaxis.set_minor_locator(AutoMinorLocator())
    ax3.text(200, 3500, 'Gas', bbox=props)

    ax0.tick_params(direction='in', axis='both', which='both', bottom=True,top=True, left=True, right=True)
    ax1.tick_params(direction='in', axis='both', which='both', bottom=True,top=True, left=True, right=True)
    ax2.tick_params(direction='in', axis='both', which='both', bottom=True,top=True, left=True, right=True)
    ax3.tick_params(direction='in', axis='both', which='both', bottom=True,top=True, left=True, right=True)
    gs.update(left=0.05, right=0.95, bottom=0.08, top=0.93, wspace=0.0, hspace=0.0)

    cb = Colorbar(ax = cbax, mappable = im , format=ticker.FuncFormatter(fmt))
    cb.set_label(r'M$_\odot$pc$^{-2}$', labelpad=10)
    plt.savefig("initial_time_step_xy", bbox_inches='tight', dpi = 300)
    plt.close()


def init_state_old(gal, gas, bins, rang):
    # Calculate histogram bins then use imshow()
    # Weighted by mass

    gal_count, xedges, yedges = np.histogram2d(gal[:,0], gal[:,1], bins=[bins, bins],range=([-rang,rang],[-rang,rang]), weights=gal[:,8])
    gas_count, xedges, yedges = np.histogram2d(gas[:,0], gas[:,1], bins=[bins, bins],range=([-rang,rang],[-rang,rang]), weights=gas[:,8])

    fig = plt.figure()
    gs = gridspec.GridSpec(2, 3, width_ratios=[1, 0.05, 0.05])
    cbax = plt.subplot(gs[:,2])
    ax0 = plt.subplot(gs[1,0]) # bottom left

    ax2 = plt.subplot(gs[0,0], sharex=ax0) # top left

    fig.set_size_inches(6, 9)


    plt.setp(ax2.get_xticklabels(), visible=False)

    gamma = 0.3
    cmap = plt.cm.get_cmap('binary')

    gal_max = np.amax(gal_count)
    gas_max = np.amax(gas_count)

    all_max = max(gal_max, gas_max)

    props = dict(facecolor='white',alpha=0.9)


    im = ax0.imshow(gal_count.T, cmap=cmap, origin='lower', vmin=0, vmax=all_max, norm=mcolors.PowerNorm(gamma), interpolation='bilinear')
    ax0.set_xlabel("X (pc)")
    ax0.set_ylabel("Y (pc)")
    ax0.xaxis.set_minor_locator(AutoMinorLocator())
    ax0.yaxis.set_minor_locator(AutoMinorLocator())
    ax0.text(100, 1300, 'Disk Stars', bbox=props)

    ax2.imshow(gas_count.T, cmap=cmap, origin='lower', vmin=0, vmax=all_max, norm=mcolors.PowerNorm(gamma), interpolation='bilinear')
    ax2.set_ylabel("Y (pc)")
    ax2.xaxis.set_minor_locator(AutoMinorLocator())
    ax2.yaxis.set_minor_locator(AutoMinorLocator())
    ax2.text(100, 1300, 'Gas', bbox=props)



    ax0.tick_params(direction='in', axis='both', which='both', bottom=True,top=True, left=True, right=True)

    ax2.tick_params(direction='in', axis='both', which='both', bottom=True,top=True, left=True, right=True)

    gs.update(left=0.05, right=0.95, bottom=0.08, top=0.93, wspace=0.0, hspace=0.0)

    cb = Colorbar(ax = cbax, mappable = im , format=ticker.FuncFormatter(fmt))
    cb.set_label(r'M$_\odot$pc$^{-2}$', labelpad=10)
    plt.savefig("Initial_time_step", bbox_inches='tight', dpi = 300)
    plt.close()

def init_basic(gal, gas):
    fig, ax = plt.subplots(1,1)
    fig.set_size_inches(6 , 4)

    plt.scatter(gal[:,0], gal[:,1])
    plt.scatter(gas[:,0], gas[:,1])
    #plt.show()

def basic_ns_scatter(x1,y1, x2, y2):
    fig, ax = plt.subplots(1,1)
    fig.set_size_inches(6 , 4)

    plt.scatter(x2, y2, s=0.1)
    plt.scatter(x1, y1, s=0.1)


    plt.savefig('basic_ns_scatter', dpi = 300)

def original_loc(gas_x,gas_y, ns_1_x, ns_1_y, ns_2_x, ns_2_y):

    #gs = gridspec.GridSpec(2, 1, width_ratios=[1, 0.05, 0.05])
    #cbax = plt.subplot(gs[1])
    #ax0 = plt.subplot(gs[2]) # bottom left

    fig, ax = plt.subplots(1,1)
    fig.set_size_inches(6 , 6)

    size = 0.08


    ax.scatter(gas_x, gas_y, marker=',', s=size, color='xkcd:slate grey', label='Gas', alpha = 0.2)
    ax.scatter(ns_1_x, ns_1_y, marker=',', s=size,color='xkcd:candy pink', label='ID 1', alpha = 0.5)
    ax.scatter(ns_2_x, ns_2_y, marker=',', s=size, color='xkcd:mint green',label='ID 2', alpha = 0.5)

    ax.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,ncol=3, mode="expand", borderaxespad=0., edgecolor='0', fancybox=False, frameon=True, markerscale=20)

    ax.tick_params(direction='in', axis='both', which='both', bottom=True,top=True, left=True, right=True)
    ax.set_xlabel("X (pc)")
    ax.set_ylabel("Y (pc)")
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())


    plt.savefig('original_loc_all',bbox_inches='tight', dpi = 300)


def init_metal_grad(gas, id1, id2):

    fig, ax = plt.subplots(1,1)

    plt.hist(gas, bins=100, histtype='stepfilled', label = 'Total 2G', color = 'xkcd:midnight purple', facecolor='xkcd:midnight purple', alpha=0.2)
    plt.hist(id1, bins=100, histtype='step', label='Ex-situ', color='xkcd:candy pink')
    plt.hist(id2, bins=100, histtype='step', label='In-situ', color='xkcd:mint green')

    ax.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,ncol=3, mode="expand", borderaxespad=0., edgecolor='0', fancybox=False, frameon=True)


    ax.tick_params(direction='in', axis='both', which='both', bottom=True,top=True, left=True, right=True)
    ax.set_xlabel("Radius (pc)")
    ax.set_ylabel("Number of particles")
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())




    plt.savefig('init_metal_gradient',bbox_inches='tight', dpi = 300)

def init_metal_grad_kde(gas, id1, id2):

    fig, ax = plt.subplots(1,1)
    fig.set_size_inches(6,4)

    #plt.hist(gas, bins=100, histtype='stepfilled', label = 'Total 2G', color = 'xkcd:midnight purple', facecolor='xkcd:midnight purple', alpha=0.2)
    #plt.hist(id1, bins=100, histtype='step', label='Ex-situ', color='xkcd:candy pink')
    #plt.hist(id2, bins=100, histtype='step', label='In-situ', color='xkcd:mint green')
    #plt.hist([id1, id2], bins=100, histtype='step',stacked=True, density = True, label='In-situ')
    id1_ratio = id1.size/gas.size
    id2_ratio = id2.size/gas.size

    # previous colours: 'xkcd:candy pink', 'xkcd:mint green', xkcd:midnight purple'

    kde = stats.gaussian_kde(id1)
    id1_linspace = np.linspace(0, gas.max(), 1000)
    ax.plot(id1_linspace, kde(id1_linspace)*id1_ratio,label='Ex-situ', color='#495867')

    kde = stats.gaussian_kde(id2)
    id2_linspace = np.linspace(0, gas.max(), 1000)
    ax.plot(id2_linspace, kde(id2_linspace)*id2_ratio,label='In-situ', color='#C18C5D')


    '''
    kde = stats.gaussian_kde(gas)
    gas_linspace = np.linspace(0, 1500, 1000)
    # This wont work as you are weighting the ex and in lines equally when that's a lie
    ax.plot(gas_linspace, kde(id2_linspace)+ kde(id1_linspace),label = 'Total 2G', color='xkcd:midnight purple')
    '''

    kde = stats.gaussian_kde(gas)
    gas_linspace = np.linspace(0, gas.max(), 1000)
    # This wont work as you are weighting the ex and in lines equally when that's a lie
    ax.fill_between(gas_linspace, kde(gas_linspace), label = 'Total 2G', color='#ECC8AF', alpha = 0.2)



    ax.tick_params(direction='in', axis='both', which='both', bottom=True,top=True, left=True, right=True)
    ax.set_xlabel("Radius (pc)")
    ax.set_ylabel("Probability Density")
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.set_xlim(left=0, right=gas.max())
    ax.set_ylim(bottom=0)

    ax.legend(fancybox=False, frameon=False)
    plt.savefig('init_metal_gradient_kde',bbox_inches='tight', dpi = 300)

def interp_1G_2G_old(new, old, bins, rang):

    # Calculate histogram bins then use imshow()
    # Weighted by mass
    '''
    gal_count, xedges, yedges = np.histogram2d(old.x_scale, old.z_scale, bins=[bins, bins],range=([-rang,rang],[-rang,rang]), weights=old.mass)
    gas_count, xedges, yedges = np.histogram2d(new.x_scale, new.z_scale, bins=[bins, bins],range=([-rang,rang],[-rang,rang]), weights=new.mass)
    new_count, xedges, yedges = np.histogram2d(new.x_scale, new.y_scale, bins=[bins, bins],range=([-rang,rang],[-rang,rang]), weights=new.mass)
    old_count, xedges, yedges = np.histogram2d(old.x_scale, old.y_scale, bins=[bins, bins],range=([-rang,rang],[-rang,rang]), weights=old.mass)
    '''
    from scipy import stats


    xmin = old.x_scale.min()
    xmax = old.x_scale.max()
    ymin = old.y_scale.min()
    ymax = old.y_scale.max()

    X, Y = np.mgrid[xmin:xmax:100j, ymin:ymax:100j]
    positions = np.vstack([X.ravel(), Y.ravel()])

    values = np.vstack([old.x_scale, old.y_scale])

    positions = np.vstack([X.ravel(), Y.ravel()])

    kernel = stats.gaussian_kde(values)
    Z = np.reshape(kernel(positions).T, X.shape)


    fig = plt.figure()
    gs = gridspec.GridSpec(2, 4, width_ratios=[1,1, 0.05, 0.05])
    cbax = plt.subplot(gs[:,3])
    ax0 = plt.subplot(gs[1,0]) # bottom left
    ax1 = plt.subplot(gs[1,1], sharey=ax0) # bottom right
    ax2 = plt.subplot(gs[0,0], sharex=ax0) # top left
    ax3 = plt.subplot(gs[0,1], sharex=ax1, sharey=ax2) # top right
    fig.set_size_inches(6, 6.05)

    plt.setp(ax1.get_yticklabels(), visible=False)
    plt.setp(ax2.get_xticklabels(), visible=False)
    plt.setp(ax3.get_yticklabels(), visible=False)
    plt.setp(ax3.get_xticklabels(), visible=False)

    gamma = 0.3
    cmap = plt.cm.get_cmap('twilight')
    '''
    gal_max = np.amax(gal_count)
    gas_max = np.amax(gas_count)
    new_max = np.amax(new_count)
    old_max = np.amax(old_count)

    all_max = max(gal_max, gas_max, new_max, old_max)
    '''
    props = dict(facecolor='white',alpha=0.9)


    im = ax0.imshow(np.rot90(Z), cmap=cmap, extent=[xmin, xmax, ymin, ymax])
    ax0.set_xlabel("X (pc)")
    ax0.set_ylabel("Y (pc)")
    ax0.xaxis.set_minor_locator(AutoMinorLocator())
    ax0.yaxis.set_minor_locator(AutoMinorLocator())
    #ax0.text(1, 40, 'Disk Stars', bbox=props)

    #ax1.pcolormesh(new.x_scale, new.z_scale,new.vy_scale.reshape(new.shape), cmap=cmap)
    ax1.set_xlabel("X (pc)")
    ax1.xaxis.set_minor_locator(AutoMinorLocator())
    ax1.yaxis.set_minor_locator(AutoMinorLocator())
    #ax1.text(1, 40, 'Gas', bbox=props)

    #ax2.pcolormesh(old.x_scale, old.y_scale, old.v.reshape(old.shape), cmap=cmap)
    ax2.set_ylabel("Y (pc)")
    ax2.xaxis.set_minor_locator(AutoMinorLocator())
    ax2.yaxis.set_minor_locator(AutoMinorLocator())
    #ax2.text(1, 40, '1G', bbox=props)


    #ax3.pcolormesh(new.x_scale, new.y_scale, new.v.reshape(new.shape), cmap=cmap)
    ax3.xaxis.set_minor_locator(AutoMinorLocator())
    ax3.yaxis.set_minor_locator(AutoMinorLocator())
    #ax3.text(1, 40, '2G', bbox=props)

    ax0.tick_params(direction='in', axis='both', which='both', bottom=True,top=True, left=True, right=True)
    ax1.tick_params(direction='in', axis='both', which='both', bottom=True,top=True, left=True, right=True)
    ax2.tick_params(direction='in', axis='both', which='both', bottom=True,top=True, left=True, right=True)
    ax3.tick_params(direction='in', axis='both', which='both', bottom=True,top=True, left=True, right=True)
    gs.update(left=0.05, right=0.95, bottom=0.08, top=0.93, wspace=0.0, hspace=0.0)

    cb = Colorbar(ax = cbax, mappable = im , format=ticker.FuncFormatter(fmt))
    cb.set_label(r'M$_\odot$pc$^{-2}$', labelpad=10)
    plt.savefig("1G_2G_XY", bbox_inches='tight', dpi = 300)
    plt.close()

def kd_interp(x,y):
    nbins=60
    k = kde.gaussian_kde([x,y])
    xi, yi = np.mgrid[x.min():x.max():nbins*1j, y.min():y.max():nbins*1j]
    zi = k(np.vstack([xi.flatten(), yi.flatten()]))
    return xi, yi, zi


def interp_1G_2G(new, old, bins, rang):

    # Calculate histogram bins then use imshow()
    # Weighted by mass
    '''
    gal_count, xedges, yedges = np.histogram2d(old.x_scale, old.z_scale, bins=[bins, bins],range=([-rang,rang],[-rang,rang]), weights=old.mass)
    gas_count, xedges, yedges = np.histogram2d(new.x_scale, new.z_scale, bins=[bins, bins],range=([-rang,rang],[-rang,rang]), weights=new.mass)
    new_count, xedges, yedges = np.histogram2d(new.x_scale, new.y_scale, bins=[bins, bins],range=([-rang,rang],[-rang,rang]), weights=new.mass)
    old_count, xedges, yedges = np.histogram2d(old.x_scale, old.y_scale, bins=[bins, bins],range=([-rang,rang],[-rang,rang]), weights=old.mass)
    '''

    '''
    x = new.x_scale
    y = new.y_scale

    nbins=120
    k = kde.gaussian_kde([x,y])
    xi, yi = np.mgrid[x.min():x.max():nbins*1j, y.min():y.max():nbins*1j]
    zi = k(np.vstack([xi.flatten(), yi.flatten()]))
    '''

    fig = plt.figure()
    gs = gridspec.GridSpec(2, 4, width_ratios=[1,1, 0.05, 0.05])
    cbax = plt.subplot(gs[:,3])
    ax0 = plt.subplot(gs[1,0]) # bottom left
    ax1 = plt.subplot(gs[1,1], sharey=ax0) # bottom right
    ax2 = plt.subplot(gs[0,0], sharex=ax0) # top left
    ax3 = plt.subplot(gs[0,1], sharex=ax1, sharey=ax2) # top right
    fig.set_size_inches(6, 6.05)

    plt.setp(ax1.get_yticklabels(), visible=False)
    plt.setp(ax2.get_xticklabels(), visible=False)
    plt.setp(ax3.get_yticklabels(), visible=False)
    plt.setp(ax3.get_xticklabels(), visible=False)

    gamma = 0.8
    cmap = plt.cm.get_cmap('magma_r')
    '''
    gal_max = np.amax(gal_count)
    gas_max = np.amax(gas_count)
    new_max = np.amax(new_count)
    old_max = np.amax(old_count)

    all_max = max(gal_max, gas_max, new_max, old_max)
    '''
    props = dict(facecolor='white',alpha=0.9)

    rang = 30
    gamma = 0.8

    xi, yi, zi = kd_interp(old.x_scale, old.z_scale)
    xj, yj, zj = kd_interp(new.x_scale, new.z_scale)
    xk, yk, zk = kd_interp(old.x_scale, old.y_scale)
    xl, yl, zl = kd_interp(new.x_scale, new.y_scale)

    gal_max = np.amax(zi)
    gas_max = np.amax(zj)
    new_max = np.amax(zk)
    old_max = np.amax(zl)

    all_max = max(gal_max, gas_max, new_max, old_max)

    im = ax0.pcolormesh(xi, yi, zi.reshape(xi.shape), v_max= all_max, shading='gouraud', norm=mcolors.PowerNorm(gamma), cmap = cmap)
    #im = ax0.hist2d(x, y, bins = 200, weights = old.mass, range=([-rang,rang],[-rang,rang]),  norm=mcolors.PowerNorm(gamma))
    ax0.set_xlabel("X (pc)")
    ax0.set_ylabel("Y (pc)")
    ax0.xaxis.set_minor_locator(AutoMinorLocator())
    ax0.yaxis.set_minor_locator(AutoMinorLocator())
    #ax0.text(1, 40, 'Disk Stars', bbox=props)



    ax1.pcolormesh(xi, yi, zi.reshape(xi.shape),  shading='gouraud', norm=mcolors.PowerNorm(gamma), cmap = cmap)
    ax1.set_xlabel("X (pc)")
    ax1.xaxis.set_minor_locator(AutoMinorLocator())
    ax1.yaxis.set_minor_locator(AutoMinorLocator())
    #ax1.text(1, 40, 'Gas', bbox=props)



    ax2.pcolormesh(xi, yi, zi.reshape(xi.shape),  shading='gouraud', norm=mcolors.PowerNorm(gamma), cmap = cmap)
    ax2.set_ylabel("Y (pc)")
    ax2.xaxis.set_minor_locator(AutoMinorLocator())
    ax2.yaxis.set_minor_locator(AutoMinorLocator())
    #ax2.text(1, 40, '1G', bbox=props)


    ax3.pcolormesh(xi, yi, zi.reshape(xi.shape),  shading='gouraud', norm=mcolors.PowerNorm(gamma), cmap = cmap)
    ax3.xaxis.set_minor_locator(AutoMinorLocator())
    ax3.yaxis.set_minor_locator(AutoMinorLocator())
    #ax3.text(1, 40, '2G', bbox=props)

    ax0.tick_params(direction='in', axis='both', which='both', bottom=True,top=True, left=True, right=True)
    ax1.tick_params(direction='in', axis='both', which='both', bottom=True,top=True, left=True, right=True)
    ax2.tick_params(direction='in', axis='both', which='both', bottom=True,top=True, left=True, right=True)
    ax3.tick_params(direction='in', axis='both', which='both', bottom=True,top=True, left=True, right=True)
    gs.update(left=0.05, right=0.95, bottom=0.08, top=0.93, wspace=0.0, hspace=0.0)

    #cb = Colorbar(ax = cbax, mappable = im , format=ticker.FuncFormatter(fmt))
    cb = Colorbar(ax = cbax, mappable = im )
    cb.set_label(r'M$_\odot$pc$^{-2}$', labelpad=10)
    plt.savefig("1G_2G_XY", bbox_inches='tight', dpi = 300)
    plt.close()
