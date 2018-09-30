# -*- coding: <encoding name> -*-
import unittest
import numpy as np
import matplotlib.pyplot as plt
import axisplot as ap


class TestAxisPlot(unittest.TestCase):
    def test_default(self):
        # generate some data
        dim_x = 512
        dim_y = 256
        x = np.linspace(0, 2 * np.pi, dim_x)
        X = np.random.normal(size=(dim_y, dim_x)) + np.sin(x)
        # create axisplot with mean along the y-axis at the top, and sum along
        # the x-axis on the right
        axisplot = ap.AxisPlot(optop=np.mean, opright=np.sum, cmap='plasma')
        ax, ax_top, ax_right = axisplot.plot(X)
        ax.set_xlabel('x label')
        ax.set_ylabel('y label')
        ax_top.set_title('test_default')
        plt.show()

    def test_all_plots(self):
        # generate some data
        dim_x = 512
        dim_y = 256
        x = np.linspace(0, 2 * np.pi, dim_x)
        X = np.random.normal(size=(dim_y, dim_x)) + np.sin(x)
        # create axisplot with mean along the y-axis at the top, sum along the
        # y-axis at the bottom, mean along the x-axis on the left, and sum
        # along the x-axis on the right
        axisplot = ap.AxisPlot(optop=np.mean, opbottom=np.sum, opleft=np.mean,
                               opright=np.sum, cmap='viridis')
        _, ax_top, _, _, _ = axisplot.plot(X)
        ax_top.set_title('test_all_plots')
        plt.show()

    def test_multiple_plots(self):
        # generate some data
        dim_x = 512
        dim_y = 256
        x = np.linspace(0, 2 * np.pi, dim_x)
        X = np.random.normal(size=(dim_y, dim_x)) + np.sin(x)
        # create axisplot
        axisplot = ap.AxisPlot(optop=np.mean, opright=np.sum)
        _, ax_top, _ = axisplot.plot(X)
        ax_top.set_title('test_multiple_plots 0')
        # create another axisplot with the same settings
        X = np.random.normal(size=(dim_y, dim_x)) + np.cos(x)
        _, ax_top, _ = axisplot.plot(X)
        ax_top.set_title('test_multiple_plots 1')
        plt.show()

    def test_axislabels(self):
        # generate some data
        dim_x = 512
        dim_y = 256
        x = np.linspace(0, 2 * np.pi, dim_x)
        X = np.random.normal(size=(dim_y, dim_x)) + np.sin(x)
        # create axisplot and update some tick labels
        axisplot = ap.AxisPlot(optop=np.mean, opright=np.sum)
        ax, ax_top, ax_right = axisplot.plot(X)
        ticks = ax.get_xticks()
        labels = ax.get_xticklabels()
        ax.set_xticklabels(map(lambda x: '{:.1f}'.format(x), ticks / 100))
        ax_right.set_xticklabels([])
        ax_top.set_title('test_axislabels')
        plt.show()

    def test_opargs(self):
        # generate some data
        dim_x = 512
        dim_y = 256
        x = np.linspace(0, 2 * np.pi, dim_x)
        X = np.random.normal(size=(dim_y, dim_x)) + np.sin(x)
        # create axisplot with operations that take arguments
        axisplot = ap.AxisPlot(optop=np.percentile,
                               topargs={'a': X, 'q': 95, 'axis': 50},
                               opright=np.sum,
                               opbottom=np.percentile,
                               bottomargs={'a': X, 'q': 5})
        _, ax_top, _, _ = axisplot.plot(X)
        ax_top.set_title('test_opargs')
        plt.show()
