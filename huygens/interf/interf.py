
import ctypes as ct
import _ctypes as _ct

def c_pointer(dtype,obj):
  '''
  Produce a C like pointer to a given object of a given type.
  For example, the object returned by this function can be used if a function takes a parameter of type `int *` or `double *`, and these
  variables represent single objects passed by reference, and not arrays. For this latter case, see c_vector().

  Parameters
  ----------
  dtype : _ctypes.PyCSimpleType
    The data type of the vector to be constructed.
  obj : object
    The object to point to

  Returns
  -------
  ptr : LP_<dtype>
    A pointer to obj

  Raises
  ------
  TypeError
    if `size` is not an int or `dtype` is ctype's data type.
  ValueError
    if `size` is not a non-negative int.

  '''
  # check dtype is a valid ctype's c type
  try:
    if _ct._SimpleCData not in dtype.__mro__:
      raise TypeError('`dtype` must be a ctype\'s data type.')
  # dtype does not have attr __mro__
  except AttributeError:
    raise TypeError('`dtype` must be a ctype\'s data type.')
  return ct.pointer(dtype(obj))

def c_vector(dtype,size,data=None):
  '''
  Produce an object which can be passed to a library function as a pointer to an object.
  For example, the object returned by this function can be used if a function takes a parameter of type `int *` or `double *`, and these
  variables represent arrays, and not single objects passed by reference. For this latter case, see c_pointer().

  Once the function call has completed, the pointer returned by this function can be converted to a list or a numpy.ndarray.

  Parameters
  ----------
  dtype : _ctypes.PyCSimpleType
    The data type of the vector to be constructed.
  size : int
    The length of the vector.
    Must be non-negative.

  Returns
  -------
  vec : <dtype>_Array_<size>
    An array of size dtypes

  Raises
  ------
  TypeError
    if `size` is not an int or `dtype` is ctype's data type.
  ValueError
    if `size` is not a non-negative int.

  '''
  # check dtype is a valid ctype's c type
  try:
    if _ct._SimpleCData not in dtype.__mro__:
      raise TypeError('`dtype` must be a ctype\'s data type.')
  # dtype does not have attr __mro__
  except AttributeError:
    raise TypeError('`dtype` must be a ctype\'s data type.')

  try:
    # an array of size dtypes
    return (dtype*size)()
  # size is not an int
  except TypeError:
    raise TypeError('`size` must be a non-negative integer.')
  # size is negative
  except ValueError:
    raise ValueError('`size` must be a non-negative integer')

def c_matrix(dtype,nrow,ncol):
  '''
  Produce an object which can be passed to a library function as a pointer to a pointer to an object.
  For example, the objects returned by this function can be used if a function takes a parameter of type `int **` or `double **`, and these
  variables represent arrays, and not single objects passed by reference. For this latter case, see c_pointer().

  This function returns two objects, `tmp` and `act`. `tmp` is to be passed to the library function. Once the function call has completed,
  `tmp` can be safely deleted. `act` can then be used as the result of the library function's manipulations. It can be converted to a list of
  lists or a numpy.ndarray.

  Parameters
  ----------
  dtype : _ctypes.PyCSimpleType
    The data type of the matrix to be constructed.
  nrow,ncol : int
    The number of rows and columns in the matrix.
    Both must be non-negative.

  Returns
  -------
  tmp :  LP_<dtype>_Array_<nrow>
    `nrow` pointers to objects of type `dtype`.
    `tmp` is for passing to the library function, and can be deleted after the call.
  act :  <dtype>_Array_<ncol>_Array_<nrow>
    `nrow`-by-`ncol` array of objects of type `dtype`.
    `act` is for using the data once the library function has finished executing.

  Raises
  ------
  TypeError
    if `nrow` or `ncol` are not ints or `dtype` is ctype's data type.
  ValueError
    if `nrow` or `ncol` are not a non-negative ints.

  Examples
  --------
  >>> import numpy as np
  >>> imoprt ctypes as ct
  >>> from huygens.interf import c_matrix

  >>> tmp,act=c_matrix(ct.c_int,5,3)
  >>> library_function(tmp)
  >>> del tmp
  >>> act=np.ctypeslib.as_array(act)
  >>> print(act)

  '''

  # check dtype is a valid ctype's c type
  try:
    if _ct._SimpleCData not in dtype.__mro__:
      raise TypeError('`dtype` must be a ctype\'s data type.')
  # dtype does not have attr __mro__
  except AttributeError:
    raise TypeError('`dtype` must be a ctype\'s data type.')

  tmp=_c_2d_tmp(dtype,nrow)
  act=_c_2d(dtype,nrow,ncol)
  # set each pointer in tmp to point to each row in act
  # thus making the pointer to pointers
  for itr in range(nrow):
    tmp[itr]=act[itr]

  return tmp,act

def _c_2d(dtype,nrow,ncol):
  '''
  Produce a 2d array of objects of a given type.

  Parameters
  ----------
  dtype : _ctypes.PyCSimpleType
    The data type of the matrix to be constructed.
  nrow,ncol : int
    The number of rows and columns in the matrix.
    Both must be non-negative.

  Returns
  -------
  act :  <dtype>_Array_<ncol>_Array_<nrow>
    `nrow`-by-`ncol` array of objects of type `dtype`.

  Raises
  ------
  TypeError
    if `nrow` or `ncol` are not ints.
  ValueError
    if `nrow` or `ncol` are not a non-negative ints.

  '''
  try:
    # an array of nrow arrays of ncol dtypes
    return ((dtype*ncol)*nrow)()
  # size is not an int
  except TypeError:
    raise TypeError('`nrow` and `ncol` must be a non-negative integer.')
  # size is negative
  except ValueError:
    raise ValueError('`nrow` and `ncol` must be a non-negative integer')

def _c_2d_tmp(dtype,nrow):
  '''
  Produce an array of pointers to objects of a given type.

  Parameters
  ----------
  dtype : _ctypes.PyCSimpleType
    The data type of the matrix to be constructed.
  nrow : int
    The number of rows in the matrix.
    Must be non-negative.

  Returns
  -------
  tmp :  LP_<dtype>_Array_<nrow>
    `nrow` pointers to objects of type `dtype`.

  Raises
  ------
  TypeError
    if `nrow` is not an int.
  ValueError
    if `nrow` is not a non-negative int.

  '''
  try:
    # an array of nrow pointers to dtypes
    return (ct.POINTER(dtype)*nrow)()
  # size is not an int
  except TypeError:
    raise TypeError('`nrow` must be a non-negative integer.')
  # size is negative
  except ValueError:
    raise ValueError('`nrow` must be a non-negative integer')
