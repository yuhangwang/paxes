import paxes.inertia.tensor_item as item
import numpy


def test():
    xyz = numpy.array([1.0, 1.0, 1.0])
    answer = item.tensor_item(xyz)
    expect = numpy.array(
        [
            [2.0, -1.0, -1.0],
            [-1.0, 2.0, -1.0],
            [-1.0, -1.0, 2.0],
        ]
    )
    assert (answer == expect).all()
