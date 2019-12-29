
import ctypes as ct
import _ctypes as _ct

def c_vector(dtype,size):

  # check dtype is a valid ctype's c type
  try:
    if _ct._SimpleCData not in dtype.__mro__:
      raise TypeError('`dtype` must be a ctypes data type.')
  # dtype does not have attr __mro__
  except AttributeError:
    raise TypeError('`dtype` must be a ctypes data type.')

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
      raise TypeError('`dtype` must be a ctypes data type.')
  # dtype does not have attr __mro__
  except AttributeError:
    raise TypeError('`dtype` must be a ctypes data type.')

  tmp=_c_2d_tmp(dtype,nrow)
  act=_c_2d(dtype,nrow,ncol)
  # set each pointer in tmp to point to each row in act
  # thus making the pointer to pointers
  for itr in range(nrow):
    tmp[itr]=act[itr]

  return tmp,act

def _c_2d(dtype,nrow,ncol):

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

  try:
    # an array of nrow pointers to dtypes
    return (ct.POINTER(dtype)*nrow)()
  # size is not an int
  except TypeError:
    raise TypeError('`nrow` must be a non-negative integer.')
  # size is negative
  except ValueError:
    raise ValueError('`nrow` must be a non-negative integer')
