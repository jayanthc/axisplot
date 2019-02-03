# -*- coding: <encoding name> -*-
import unittest
import numpy as np
import matplotlib.pyplot as plt
import axisplot as ap


class TestAxisPlot(unittest.TestCase):
    def setUp(self):
        # generate some data
        # set up dimensions
        self.dim_x = 512
        self.dim_y = 256
        # generate a random normal
        self.data = np.random.normal(loc=0.0,
                                     scale=1.0,
                                     size=(self.dim_y, self.dim_x))
        # add a sine wave on top of it
        self.x = np.linspace(0, 2 * np.pi, self.dim_x)
        self.data += np.sin(self.x)

    def test_0_default(self):
        # create axisplot with mean along the y-axis at the top, and sum along
        # the x-axis on the right
        axisplot = ap.AxisPlot(optop=np.mean, opright=np.sum, cmap='plasma')
        ax, ax_top, ax_right = axisplot.plot(self.data)
        ax.set_xlabel('x label')
        ax.set_ylabel('y label')
        ax_top.set_title('test_0_default')
        plt.show()

    def test_1_all_plots(self):
        # create axisplot with mean along the y-axis at the top, sum along the
        # y-axis at the bottom, mean along the x-axis on the left, and sum
        # along the x-axis on the right
        axisplot = ap.AxisPlot(optop=np.mean, opbottom=np.sum, opleft=np.mean,
                               opright=np.sum, cmap='viridis')
        _, ax_top, _, _, _ = axisplot.plot(self.data)
        ax_top.set_title('test_1_all_plots')
        plt.show()

    def test_2_multiple_plots(self):
        # create axisplot
        axisplot = ap.AxisPlot(optop=np.mean, opright=np.sum)
        _, ax_top, _ = axisplot.plot(self.data)
        ax_top.set_title('test_2_multiple_plots 0')

        # create another axisplot with the same settings
        # generate a (different) random normal
        data = np.random.normal(loc=1.0,
                                scale=2.0,
                                size=(self.dim_y, self.dim_x))
        # add a sine wave on top of it
        data += np.sin(self.x)
        _, ax_top, _ = axisplot.plot(data)
        ax_top.set_title('test_2_multiple_plots 1')
        plt.show()

    def test_3_axislabels(self):
        # create axisplot and update some tick labels
        axisplot = ap.AxisPlot(optop=np.mean, opright=np.sum)
        ax, ax_top, ax_right = axisplot.plot(self.data)
        ticks = ax.get_xticks()
        labels = ax.get_xticklabels()
        ax.set_xticklabels(map(lambda x: '{:.1f}'.format(x), ticks / 100))
        ax_right.set_xticklabels([])
        ax_top.set_title('test_3_axislabels')
        plt.show()

    def test_4_opargs(self):
        # create axisplot with operations that take arguments
        axisplot = ap.AxisPlot(optop=np.percentile,
                               topargs={'a': self.data, 'q': 95, 'axis': 50},
                               opright=np.sum,
                               opbottom=np.percentile,
                               bottomargs={'a': self.data, 'q': 5})
        _, ax_top, _, _ = axisplot.plot(self.data)
        ax_top.set_title('test_4_opargs')
        plt.show()
