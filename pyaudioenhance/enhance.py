from pathlib import Path
from pydub import AudioSegment
from .core.enhance import enhance as enhance_function


def enhance(dtype: type, multiplier: int, filepath: Path) -> AudioSegment:
    audio = AudioSegment.from_file(filepath)
    audio = enhance_function(dtype, multiplier, audio)
    return audio
