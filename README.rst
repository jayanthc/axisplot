AxesPlot
========

AxesPlot extends the functionality of Matplotlib's `imshow()` function by
appending two plots to the image, at the top or bottom, and on the left or
right.

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
