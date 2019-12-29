
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
  tmp=_c_2d_tmp(dtype,nrow)
  act=_c_2d(dtype,nrow,ncol)
  for itr in range(nrow):
    tmp[itr]=act[itr]

  return tmp,act

def _c_2d(dtype,nrow,ncol):
  return ((dtype*ncol)*nrow)()

def _c_2d_tmp(dtype,nrow):
  return (ct.POINTER(dtype)*nrow)()
