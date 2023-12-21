from numpy import array, iinfo, int16, int32
from pyaudioenhance.scale import scale


def test():
    info16 = iinfo(int16)
    info32 = iinfo(int32)
    actual = scale(int16, array([info32.min, info32.max]))
    expected = array([info16.min, info16.max])
    assert (actual == expected).all()
