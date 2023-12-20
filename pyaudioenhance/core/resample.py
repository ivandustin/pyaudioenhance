from scipy.signal import resample as resample_function
from numpy import ndarray


def resample(multiplier: int, points: ndarray) -> ndarray:
    return resample_function(points, int(points.shape[-1] * multiplier))
