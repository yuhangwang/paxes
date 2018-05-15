from paxes.inertia import tensor
import numpy
from pytest import approx


def test():
    xyz = numpy.array(
        [
            [1.0, 1.0, 1.0],
            [1.0, 2.0, 3.0],
        ]
    )

    print(xyz.shape)
    answer = numpy.asarray(tensor(xyz))
    expect = numpy.array(
        [
            [15.0, -3.0, -4.0],
            [-3.0, 12.0, -7.0],
            [-4.0, -7.0, 7.0],
        ]
    )
    print("answer = ", answer)
    assert answer == approx(expect)
