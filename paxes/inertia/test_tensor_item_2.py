import paxes.inertia.tensor_item as item
import numpy


def test():
    xyz = numpy.array([1.0, 2.0, 3.0])
    answer = item.tensor_item(xyz)
    expect = numpy.array(
        [
            [13.0, -2.0, -3.0],
            [-2.0, 10.0, -6.0],
            [-3.0, -6.0, 5.0],
        ]
    )
    print(numpy.asarray(answer))
    assert (answer == expect).all()
