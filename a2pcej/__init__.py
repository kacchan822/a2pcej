# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from sys import version_info
from .a2pcej import *
"""a2pcej, convert Alphabet to Phonetic Code in English and Japanease.

    This module convert each alphabet letters to phonetic code,
    and also convert each alphabet letterts to katakana.
"""
__all__ = ['conv_al', 'conv_ak']
if version_info[0] == 2:
    __all__ = [n.encode('ascii') for n in __all__]
