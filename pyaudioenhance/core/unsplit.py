from numpy import ndarray


def unsplit(array: ndarray) -> ndarray:
    return array.T.flatten()
