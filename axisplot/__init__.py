# -*- coding: utf-8 -*-
"""
AxisPlot extends the functionality of Matplotlib's imshow() function.

AxisPlot extends the functionality of Matplotlib's imshow() function by
appending up to four plots to the image, at the top, at the bottom, on the
left, and/or on the right. The additional plots contain the output of
operations that are performed along the two axes. Plots at the top and bottom
contain the output of operations performed along the vertical axis, while plots
on the left and right contain the output of operations that are performed along
the horizontal axis.

Classes:
    AxisPlot: The main, and only, class in this module.
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mp
import mpl_toolkits.axes_grid1 as mag1


class AxisPlot:
    """
    AxisPlot extends the functionality of Matplotlib's imshow() function.

    AxisPlot extends the functionality of Matplotlib's imshow() function by
    appending up to four plots to the image, at the top, at the bottom, on the
    left, and/or on the right. The additional plots contain the output of
    operations that are performed along the two axes. Plots at the top and
    bottom contain the output of operations performed along the vertical axis,
    while plots on the left and right contain the output of operations that are
    performed along the horizontal axis.

    Attributes:
        optop: Operation corresponding to the plot at the top of the image.
        topargs: Arguments to the top operation function.
        opbottom: Operation corresponding to the plot at the bottom.
        bottomargs: Arguments to the bottom operation function.
        opleft: Operation corresponding to the plot on the left.
        leftargs: Arguments to the left operation function.
        opright: Operation corresponding to the plot on the right.
        rightargs: Arguments to the right operation function.
        figsize: Size of the figure as (width, height) in inches.
        padtop: Padding between the top plot and the image.
        padbottom: Padding between the bottom plot and the image.
        padleft: Padding between the left plot and the image.
        padright: Padding between the right plot and the image.
        imshowkwargs: Keyword arguments to Matplotlib's imshow() function.
        heights: Heights of the appended plots.

    """

    def __init__(self, optop=None, topargs=None, opbottom=None,
                 bottomargs=None, opleft=None, leftargs=None, opright=None,
                 rightargs=None, figsize=None, padtop=0.0, padbottom=0.0,
                 padleft=0.0, padright=0.0, **imshowkwargs):
        """
        Initialise AxisPlot object.

        AxisPlot is initialised with the operations to perform along the two
        axes of the two-dimensional array that is to be plotted.

        Keyword arguments:
            optop: Operation corresponding to the plot at the top of the image.
            topargs: Arguments to the top operation function.
            opbottom: Operation corresponding to the plot at the bottom.
            bottomargs: Arguments to the bottom operation function.
            opleft: Operation corresponding to the plot on the left.
            leftargs: Arguments to the left operation function.
            opright: Operation corresponding to the plot on the right.
            rightargs: Arguments to the right operation function.
            figsize: Size of the figure as (width, height) in inches.
            padtop: Padding between the top plot and the image.
            padbottom: Padding between the bottom plot and the image.
            padleft: Padding between the left plot and the image.
            padright: Padding between the right plot and the image.
            imshowkwargs: Keyword arguments to Matplotlib's imshow() function.

        Returns:
            None.
        """
        self.optop = optop
        # if operations require arguments, store them
        if topargs is not None:
            self.topargs = self.__sanitise(topargs)
        else:
            self.topargs = None
        self.opbottom = opbottom
        if bottomargs is not None:
            self.bottomargs = self.__sanitise(bottomargs)
        else:
            self.bottomargs = None
        self.opleft = opleft
        if leftargs is not None:
            self.leftargs = self.__sanitise(leftargs)
        else:
            self.leftargs = None
        self.opright = opright
        if rightargs is not None:
            self.rightargs = self.__sanitise(rightargs)
        else:
            self.rightargs = None
        self.figsize = figsize
        self.padtop = padtop
        self.padbottom = padbottom
        self.padleft = padleft
        self.padright = padright
        self.imshowkwargs = imshowkwargs

        if figsize is None:
            figsize = mp.rcParams['figure.figsize']
        # figsize is (width, height)
        aspect_ratio = figsize[0] / figsize[1]

        default_height_frac = 0.2
        # heights is (y, x)
        self.heights = [figsize[0] * default_height_frac,
                        figsize[1] * aspect_ratio * default_height_frac]

        return

    def plot(self, X):
        """
        Plot input based on configuration.

        This function plots the input two-dimensional array using Matplotlib's
        imshow() function, and optionally appends additional plots based on how
        the axisplot object was instantiated.

        Arguments:
            X: Input two-dimensional array.

        Returns:
            A list of axes objects.
        """
        fig, ax = plt.subplots(figsize=self.figsize)
        ax.imshow(X, **self.imshowkwargs)
        divider = mag1.make_axes_locatable(ax)

        x = np.linspace(0, X.shape[1], X.shape[1])
        y = np.linspace(0, X.shape[0], X.shape[0])

        plot_axes = [ax]

        if self.optop:
            ax_top = divider.append_axes('top', self.heights[1],
                                         pad=self.padtop, sharex=ax)
            ax_top.xaxis.set_tick_params(labelbottom=False)
            if self.topargs is None:
                ax_top.plot(x, self.optop(X, axis=0))
            else:
                ax_top.plot(x, self.optop(**self.topargs, axis=0))
            ax_top.set_xlim(x.min(), x.max())
            plot_axes.append(ax_top)
        if self.opbottom:
            ax_bottom = divider.append_axes('bottom', self.heights[1],
                                            pad=self.padbottom, sharex=ax)
            # turn bottom labels off for the image
            ax.xaxis.set_tick_params(labelbottom=False)
            ax_bottom.xaxis.set_tick_params(labelbottom=True)
            if self.bottomargs is None:
                ax_bottom.plot(x, self.opbottom(X, axis=0))
            else:
                ax_bottom.plot(x, self.opbottom(**self.bottomargs, axis=0))
            ax_bottom.set_xlim(x.min(), x.max())
            plot_axes.append(ax_bottom)
        if self.opleft:
            ax_left = divider.append_axes('left', self.heights[0],
                                          pad=self.padleft, sharey=ax)
            # turn left labels off for the image
            ax.yaxis.set_tick_params(labelleft=False)
            ax_left.yaxis.set_tick_params(labelleft=True)
            if self.leftargs is None:
                ax_left.plot(self.opleft(X, axis=1), y)
            else:
                ax_left.plot(self.opleft(**self.leftargs, axis=1), y)
            ax_left.set_ylim(y.min(), y.max())
            plot_axes.append(ax_left)
        if self.opright:
            ax_right = divider.append_axes('right', self.heights[0],
                                           pad=self.padright, sharey=ax)
            ax_right.yaxis.set_tick_params(labelleft=False)
            if self.rightargs is None:
                ax_right.plot(self.opright(X, axis=1), y)
            else:
                ax_right.plot(self.opright(**self.rightargs, axis=1), y)
            ax_right.set_ylim(y.min(), y.max())
            plot_axes.append(ax_right)

        return plot_axes

    def __sanitise(self, args):
        """Sanitise arguments to operations."""
        # if 'axis' is specified as an argument, drop it
        if 'axis' in args:
            del args['axis']

        return args
