
'''
===================================
Interfacing with Compiled Libraries
===================================

Functions
=========

  c_vector -- Produce a ctype's object to pass as a C pointer (a vector)
  c_matrix -- Produce a ctype's object to pass as a C pointer to a pointer (a matrix)
'''

from .interf import *

__all__=[s for s in dir() if not s.startswith('_')]
