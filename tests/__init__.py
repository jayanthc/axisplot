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
        axesplot.AxesPlot(X, np.mean, np.sum, cmap='plasma')
        plt.show()
