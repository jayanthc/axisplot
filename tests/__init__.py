import unittest
import numpy as np
import matplotlib.pyplot as plt
import axesplot


class TestAxesPlot(unittest.TestCase):
    def test(self):
        # generate some data
        dim_x = 512
        dim_y = 256
        x = np.linspace(0, 2 * np.pi, dim_x)
        X = np.random.normal(size=(dim_y, dim_x)) + np.sin(x)
        # create axesplot with mean along the y-axis at the top, and sum along
        # the x-axis on the right
        axesplot.AxesPlot(X, np.mean, np.sum, cmap='plasma')
        plt.show()
