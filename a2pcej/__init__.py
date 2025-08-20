"""a2pcej, convert Alphabet to Phonetic Code in English and Japanese.

    This module convert each alphabet letters to phonetic code,
    and also convert each alphabet letters to katakana.
"""
import argparse

from .a2pcej import A2pcej, conv_ak, conv_al
from .phonetics import Phonetics

try:
    from ._version import __version__
except ImportError:
    # fallback for development without setuptools_scm
    __version__ = "unknown"

__all__ = ['A2pcej', 'Phonetics', 'conv_al', 'conv_ak', '__version__']


def create_parser():
    """ commandline argparser """
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--mode', choices=['en', 'ja'], required=True)
    parser.add_argument('-d', '--delimiter')
    parser.add_argument('-nd', '--nodelimiter', action='store_true')
    parser.add_argument('-s', '--sign')
    parser.add_argument('-ns', '--nosign', action='store_true')
    parser.add_argument('-n', '--num', action='store_true')
    parser.add_argument('letters', nargs='+', type=str)
    return parser


def main():
    """ called cmdline """
    parser = create_parser()
    args = parser.parse_args()

    converter = A2pcej(
        lang=args.mode,
        delimiter=args.delimiter if not args.nodelimiter else '',
        sign=args.sign if not args.nosign  else '',
        num=args.num
    )

    for letters in args.letters:
        print(converter.convert(letters))
