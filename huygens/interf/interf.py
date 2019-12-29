
import ctypes as ct

def c_vector(dtype,size):
  return (dtype*size)()

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
