import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mp
import mpl_toolkits.axes_grid1 as mag1


class AxesPlot:
    def __init__(self, X, op1, op2, figsize=None, positions=('top', 'right'),
                 heights=None, pads=None, labeltop=False, labelbottom=False,
                 labelleft=False, labelright=False, cmap=None, norm=None,
                 aspect=None, interpolation=None, alpha=None, vmin=None,
                 vmax=None, origin=None, extent=None, shape=None, filternorm=1,
                 filterrad=4.0, imlim=None, resample=None, url=None, data=None,
                 **kwargs):
        if figsize is None:
            figsize = mp.rcParams['figure.figsize']
        # figsize is (width, height)
        aspect_ratio = figsize[0] / figsize[1]

        fig, ax = plt.subplots(figsize=figsize)
        divider = mag1.make_axes_locatable(ax)

        # guess appropriate heights for the axes plots
        default_height_frac = 0.2
        if heights is None:
            # heights is (y, x)
            heights = [figsize[0] * default_height_frac,
                       figsize[1] * aspect_ratio * default_height_frac]

        if pads is None:
            pads = (0.0, 0.0)

        ax_x = divider.append_axes(positions[0], heights[1], pad=pads[0],
                                   sharex=ax)
        ax_y = divider.append_axes(positions[1], heights[0], pad=pads[1],
                                   sharey=ax)
        ax_x.xaxis.set_tick_params(labelbottom=labelbottom)
        ax_y.yaxis.set_tick_params(labelleft=labeltop)

        ax.imshow(X, cmap=cmap, norm=norm, aspect=aspect,
                  interpolation=interpolation, alpha=alpha, vmin=vmin,
                  vmax=vmax, origin=origin, extent=extent, shape=shape,
                  filternorm=filternorm, filterrad=filterrad, imlim=imlim,
                  resample=resample, url=url, data=data, **kwargs)

        x = np.linspace(0, X.shape[1], X.shape[1])
        y = np.linspace(0, X.shape[0], X.shape[0])

        ax_x.plot(x, op1(X, axis=0))
        ax_y.plot(op2(X, axis=1), y)

        ax_x.set_xlim(x.min(), x.max())
        ax_y.set_ylim(y.min(), y.max())

        return
