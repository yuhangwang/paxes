from paxes.inertia.tensor_item cimport tensor_item
from paxes.inertia.tensor_item import tensor_item
from cython cimport floating
import numpy


cpdef floating[:,:] p(floating[:] xs):
    print(numpy.asarray(xs))
    return numpy.array([xs])

cpdef floating[:, :] tensor(floating[:, :] coords):
    """Return the moment of inertia tensor

    Args:
        coords (2D numpy.ndarray): input coordinates (Nx3)
            one point per row.
    """
    n_points = numpy.shape(coords)[0]
    return numpy.add.reduce(
        list(map(tensor_item, [coords[i, :] for i in range(n_points)])),
        axis=0)
