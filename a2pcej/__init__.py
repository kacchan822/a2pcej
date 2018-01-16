# -*- coding: utf-8 -*-
"""a2pcej, convert Alphabet to Phonetic Code in English and Japanease.

    This module convert each alphabet letters to phonetic code,
    and also convert each alphabet letterts to katakana.
"""
from __future__ import absolute_import, unicode_literals
import argparse
import sys

from .a2pcej import A2pcej, conv_ak, conv_al
from .phonetics import Phonetics

__all__ = ['A2pcej', 'Phonetics', 'conv_al', 'conv_ak']
if sys.version_info[0] == 2:
    __all__ = [n.encode('ascii') for n in __all__]


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
