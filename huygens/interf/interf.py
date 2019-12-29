
import ctypes as ct
import _ctypes as _ct

def c_vector(dtype,size):
  '''
  Produce an object which can be passed to a library function as a pointer to an object.
  For example, the object returned by this function can be used if a function takes a parameter of type `int *` or `double *`.

  Parameters
  ----------
  dtype : _ctypes.PyCSimpleType
    The data type of the vector to be constructed.
  size : int
    The length of the vector.
    Must be non-negative.

  Returns
  -------
  vec : __main__.<dtype>_Array_<size>
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
  act :  __main__.<dtype>_Array_<ncol>_Array_<nrow>
    `nrow`-by-`ncol` array of objects of type `dtype`.

  Raises
  ------
  TypeError
    if `nrow` or `ncol` is not an int.
  ValueError
    if `nrow` or `ncol` is not a non-negative int.

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
  tmp :  __main__.LP_<dtype>_Array_<nrow>
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
