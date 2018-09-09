AxesPlot
========

AxesPlot extends the functionality of Matplotlib's `imshow()` function by
appending two plots to the image, at the top or bottom, and on the left or
right. The additional plots contain the output of operations that are performed
along the two axes. For example, the screenshot below shows an AxesPlot with
the mean of the image computed along the vertical axis, shown at the top, and
the sum of the image computed along the horizontal axis, shown on the right.

.. class:: no-web

    .. image:: https://github.com/jayanthc/axesplot/blob/master/examples/example.png
        :alt: AxesPlot screenshot
        :height: 1088px
        :width: 1280px
        :scale: 60%
        :align: center


Usage
-----

.. code:: python

    import numpy as np
    import axesplot

    # generate some data
    dim_x = 512
    dim_y = 256
    x = np.linspace(0, 2 * np.pi, dim_x)
    X = np.random.normal(size=(dim_y, dim_x)) + np.sin(x)
    # create axesplot with mean along the y-axis at the top, and sum along the
    # x-axis on the right
    axesplot.AxesPlot(X, np.mean, np.sum, cmap='plasma')

Installation
------------

Development mode:

::

    cd <axesplot-directory>
    pip install -e .

Unit Testinig
------------

::

    cd <axesplot-directory>
    python -m unittest

License
-------

AxesPlot is distributed under WTFPLv2.


----
