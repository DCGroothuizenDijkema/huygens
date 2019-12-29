
import ctypes as ct
import _ctypes as _ct

def c_vector(dtype,size):

  try:
    if _ct._SimpleCData not in dtype.__mro__:
      raise TypeError('`dtype` must be a ctypes data type.')
  except AttributeError:
    raise TypeError('`dtype` must be a ctypes data type.')

  try:
    return (dtype*size)()
  except TypeError:
    raise TypeError('`size` must be a non-negative integer.')
  except ValueError:
    raise ValueError('`size` must be a non-negative integer')

def c_matrix(dtype,nrow,ncol):

  try:
    if _ct._SimpleCData not in dtype.__mro__:
      raise TypeError('`dtype` must be a ctypes data type.')
  except AttributeError:
    raise TypeError('`dtype` must be a ctypes data type.')

  tmp=_c_2d_tmp(dtype,nrow)
  act=_c_2d(dtype,nrow,ncol)
  for itr in range(nrow):
    tmp[itr]=act[itr]

  return tmp,act

def _c_2d(dtype,nrow,ncol):

  try:
    return ((dtype*ncol)*nrow)()
  except TypeError:
    raise TypeError('`nrow` and `ncol` must be a non-negative integer.')
  except ValueError:
    raise ValueError('`nrow` and `ncol` must be a non-negative integer')

def _c_2d_tmp(dtype,nrow):

  try:
    return (ct.POINTER(dtype)*nrow)()
  except TypeError:
    raise TypeError('`nrow` and `ncol` must be a non-negative integer.')
  except ValueError:
    raise ValueError('`nrow` and `ncol` must be a non-negative integer')
