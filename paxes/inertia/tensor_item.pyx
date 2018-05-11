from cython cimport floating
import numpy


cpdef floating[:,:] tensor_item(floating[:] xyz):
    """Transform the input [x, y, z] into one item in the
        inertia tensor sum.

    Args:
        xyz (1D numpy.ndarray): [x, y, z]
    Outputs:
        3x3 2D numpy.ndarray
    """
    sqr = numpy.square
    x, y, z = xyz
    xy = -x*y
    xz = -x*z
    yz = -y*z
    xx = sqr(y) + sqr(z)
    yy = sqr(x) + sqr(z)
    zz = sqr(x) + sqr(y)

    return numpy.array(
        [
            [xx, xy, xz],
            [xy, yy, yz],
            [xz, yz, zz],
        ]
    )
