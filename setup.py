from setuptools import setup

setup(name='axisplot',
      version='1.0',
      description='Matplotlib imshow() Functionality Extension',
      url='http://github.com/jayanthc/axisplot',
      author='Jayanth Chennamangalam',
      license='WTFPLv2',
      packages=['axisplot'],
      install_requires=[
          'numpy',
          'matplotlib'
      ],
      zip_safe=False)
