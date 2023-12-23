from pyaudioenhance.core.scale import scale


def test():
    assert scale(0, 10, 0, 100, 5) == 50
    assert scale(-10, 10, -100, 100, 0) == 0
    assert scale(0, 1, 0, 100, 0.5) == 50
    assert scale(10, 0, 100, 0, 5) == 50
