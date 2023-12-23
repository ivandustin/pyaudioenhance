from numpy import ndarray, iinfo, int32
from .core.scale import scale as scale_function


def scale(n: ndarray) -> ndarray:
    y = iinfo(int32)
    return scale_function(n.min(), n.max(), y.min, y.max, n).round().astype(int32)
