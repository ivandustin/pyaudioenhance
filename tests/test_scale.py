from numpy import array, array_equal
from pyaudioenhance.scale import scale


def test():
    input = array([-1, -0.5, 0, 0.5, 1])
    expected = array([-2147483648, -1073741824, 0, 1073741823, 2147483647])
    actual = scale(input)
    assert array_equal(expected, actual)
