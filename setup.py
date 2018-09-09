from setuptools import setup

setup(name='axesplot',
      version='1.0',
      description='Matplotlib imshow() Functionality Extension',
      url='http://github.com/jayanthc/axesplot',
      author='Jayanth Chennamangalam',
      license='WTFPLv2',
      packages=['axesplot'],
      install_requires=[
          'numpy',
          'matplotlib'
      ],
      zip_safe=False)
