from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from pathlib import Path
from numpy import dtype
from .enhance import enhance as enhance_function


def enhance():
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("directory", type=Path)
    parser.add_argument("--multiplier", type=int, default=10, help="Sample multiplier")
    parser.add_argument("--format", type=str, default="mp3", help="Output format")
    parser.add_argument("--bitrate", type=str, default="320k", help="Output bitrate")
    parser.add_argument("--dtype", type=dtype, default="int32", help="Output bit width")
    args = parser.parse_args()
    outdir = args.directory.parent / f"{args.directory.name}-enhanced"
    outdir.mkdir(exist_ok=True)
    suffix = f".{args.format}"
    filepaths = args.directory.glob("*")
    for filepath in filepaths:
        audio = enhance_function(args.dtype, args.multiplier, filepath)
        outpath = outdir / filepath.name
        outpath = outpath.with_suffix(suffix)
        audio.export(outpath, format=args.format, bitrate=args.bitrate)
