from numpy import ndarray, iinfo, int32
from .core.scale import scale as scale_function


def scale(x: ndarray) -> ndarray:
    y = iinfo(int32)
    return scale_function(x.min(), x.max(), y.min, y.max, x).round().astype(int32)
