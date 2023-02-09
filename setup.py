#setup.py

from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize('file.pyx'))


#usges : python2/python3 setup.py build_ext --inplace
