import paxes.inertia.tensor as I
import numpy


def test():
    answer = I(numpy.ones((2,3)))
    expect = numpy.ones(3)
    assert (answer == expect).all()
