from pydub import AudioSegment
from numpy import array, stack
from .resample import resample
from .unsplit import unsplit
from ..scale import scale
from .split import split


def enhance(multiplier: int, audio: AudioSegment) -> AudioSegment:
    samples = audio.get_array_of_samples()
    samples = array(samples)
    samples = split(audio.channels, samples)
    samples = stack([resample(multiplier, samples[i]) for i in range(audio.channels)])
    samples = unsplit(samples)
    samples = scale(samples)
    return AudioSegment(
        samples.tobytes(),
        frame_rate=audio.frame_rate * multiplier,
        sample_width=samples.itemsize,
        channels=audio.channels,
    )
