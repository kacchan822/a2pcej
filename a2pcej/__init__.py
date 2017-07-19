# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from sys import version_info, exit
import argparse
from .a2pcej import *
"""a2pcej, convert Alphabet to Phonetic Code in English and Japanease.

    This module convert each alphabet letters to phonetic code,
    and also convert each alphabet letterts to katakana.
"""
__all__ = ['conv_al', 'conv_ak']
if version_info[0] == 2:
    __all__ = [n.encode('ascii') for n in __all__]


def main():
    p = argparse.ArgumentParser()
    p.add_argument('-m', '--mode', choices=['en', 'ja'], required=True)
    p.add_argument('-d', '--delimiter')
    p.add_argument('-nd', '--nodelimiter', action='store_true')
    p.add_argument('-s', '--sign')
    p.add_argument('-ns', '--nosign', action='store_true')
    p.add_argument('-n', '--num', action='store_true')
    p.add_argument('letters', nargs='+', type=str)

    args = p.parse_args()

    if args.mode == 'en':
        cmd = conv_al
    else:
        cmd = conv_ak

    if args.delimiter is None and not args.nodelimiter:
        if args.mode == 'en':
            delimiter = '-'
        else:
            delimiter = '・'
    elif args.nodelimiter:
        delimiter = ''
    else:
        delimiter = args.delimiter

    if args.sign is None and not args.nosign:
        if args.mode == 'en':
            sign = '(CAPS)'
        else:
            sign = '（大文字）'
    elif args.nosign:
        sign = ''
    else:
        sign = args.sign

    for s in args.letters:
        print(cmd(s, delimiter=delimiter, sign=sign, num=args.num))


if __name__ == '__main__':
    exit(main())
