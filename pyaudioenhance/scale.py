from numpy import ndarray, iinfo
from .core.scale import scale as scale_function


def scale(dtype: type, x: ndarray) -> ndarray:
    info = iinfo(dtype)
    return scale_function(info.max, x.max(), x).clip(info.min, info.max).astype(dtype)
