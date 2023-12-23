from pathlib import Path
from pydub import AudioSegment
from .core.enhance import enhance as enhance_function


def enhance(multiplier: int, filepath: Path) -> AudioSegment:
    audio = AudioSegment.from_file(filepath)
    audio = enhance_function(multiplier, audio)
    return audio
