from cython cimport floating


cpdef floating[:, :] tensor(floating[:, :] coords):
    return coords
