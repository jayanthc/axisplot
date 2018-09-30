AxisPlot
========

AxisPlot extends the functionality of Matplotlib's `imshow()` function by
appending up to four plots to the image, at the top, bottom, left, and/or
right. The additional plots contain the output of operations that are performed
along the two axes. Plots at the top and bottom contain the output of
operations performed along the vertical axis, while plots on the left and right
contain the output of operations that are performed along the horizontal axis.
For example, the screenshot below shows an AxisPlot with the mean of the image
computed along the vertical axis, shown at the top, and the sum of the image
computed along the horizontal axis, shown on the right.

.. class:: no-web

    .. image:: https://github.com/jayanthc/axisplot/blob/master/examples/example.png
        :alt: AxisPlot screenshot
        :height: 1088px
        :width: 1280px
        :scale: 60%
        :align: center


Usage
-----

.. code:: python

    import numpy as np
    import matplotlib.pyplot as plt
    import axisplot as ap

    # generate some data
    dim_x = 512
    dim_y = 256
    x = np.linspace(0, 2 * np.pi, dim_x)
    X = np.random.normal(size=(dim_y, dim_x)) + np.sin(x)
    # create axisplot with mean along the y-axis at the top, and sum along the
    # x-axis on the right
    axisplot = ap.AxisPlot(optop=np.mean, opright=np.sum, cmap='plasma')
    axisplot.plot(X)
    # another example, using an operation (percentile) that takes arguments
    # axisplot = ap.AxisPlot(optop=np.percentile, topargs={'a': X, 'q': 95})
    # _, ax_top, _, _ = axisplot.plot(X)
    plt.show()

Installation
------------

Development mode:

::

    cd <axisplot-directory>
    pip install -e .

Unit Testing
------------

::

    cd <axisplot-directory>
    python -m unittest

License
-------

AxisPlot is distributed under WTFPLv2.


----
