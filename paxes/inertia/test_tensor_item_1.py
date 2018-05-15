from paxes.inertia import tensor_item
import numpy
from pytest import approx


def test():
    xyz = numpy.array([1.0, 1.0, 1.0])
    answer = tensor_item(xyz)
    expect = numpy.array(
        [
            [2.0, -1.0, -1.0],
            [-1.0, 2.0, -1.0],
            [-1.0, -1.0, 2.0],
        ]
    )
    assert answer == approx(expect)
