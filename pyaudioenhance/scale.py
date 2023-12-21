from numpy import ndarray, iinfo, abs, longdouble
from .core.scale import scale as scale_function


def scale(dtype: type, x: ndarray) -> ndarray:
    info = iinfo(dtype)
    return (
        scale_function(
            abs([info.min, info.max], dtype=longdouble).max(),
            abs(x, dtype=longdouble).max(),
            x,
        )
        .round()
        .clip(info.min, info.max)
        .astype(dtype)
    )
