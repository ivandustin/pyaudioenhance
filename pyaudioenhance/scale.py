from numpy import ndarray, iinfo
from .core.scale import scale as scale_function


def scale(dtype: type, x: ndarray) -> ndarray:
    m = iinfo(dtype).max
    n = x.max()
    y = scale_function(m, n, x)
    return y.astype(dtype)
