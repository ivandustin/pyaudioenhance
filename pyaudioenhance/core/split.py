from numpy import ndarray


def split(channels: int, samples: ndarray) -> ndarray:
    return samples.reshape((samples.size // channels, channels)).T
