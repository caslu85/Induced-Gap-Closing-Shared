#%%
##### LOADER FOR JSON FILES #####
%matplotlib qt

import json, numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 12})

file_path = '.'

def doplt( d, *args, ax=None, **kwargs ) :
    ''' make plot of dictionary-ized data d
    '''
    data = d['data']
    x = d['x']
    y = d['y']
    clabel = d['clabel']
    xlabel = d['xlabel']
    ylabel = d['ylabel']

    # fig, _ = plt.subplots(1,1)
    if ax is None :
        _, ax = plt.subplots(1,1)
    im = ax.pcolormesh( x, y, data, *args, **kwargs )
    cbar = ax.figure.colorbar( im, ax=ax )

    im.set_edgecolor('face')
    cbar.set_label( clabel )
    ax.set_xlabel( xlabel )
    ax.set_ylabel( ylabel )
    return im, cbar

def load_json( name ) :
    ''' load name.json
    returns: loaded dictionary
    '''
    s_file = f'{file_path}/{name}.json'
    with open( s_file ) as fp :
        data = json.load( fp )
    return data

#%% local
fig, ax = plt.subplots( 3, 2 )
local = ( 'fig6al', 'fig6ar', 'fig6bl', 'fig6br', 'fig6cl', 'fig6cr' )
for a, s in zip( ax.flatten(), local ) :
    d = load_json( s )
    doplt( d, ax=a, vmax=0.3 )
fig.tight_layout()

#%% nonlocal 
fig, ax = plt.subplots( 3, 2 )
local = ( 'fig5al', 'fig5ar', 'fig5bl', 'fig5br', 'fig5cl', 'fig5cr' )
for a, s in zip( ax.flatten(), local ) :
    d = load_json( s )
    doplt( d, ax=a, cmap='bwr', vmin=-0.04, vmax=0.04 )
fig.tight_layout()

#%%