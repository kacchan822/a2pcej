# -*- coding: utf-8 -*-
"""a2pcej, convert Alphabet to Phonetic Code in English and Japanease.

    This module convert each alphabet letters to phonetic code,
    and also convert each alphabet letterts to katakana.

    IMPORTANT: In current version, supported with Python 3.x.

    Simple example of usage as below...

    Import module.
    >>> from ak2pc import *

    Convert 'exsamples' to Ponetic code.
    >>> conv_al('examples')
    'ECHO, X―RAY, ALFA, MIKE, PAPA, LIMA, ECHO, SIERRA,'

    Convert 'exsamples' to Katakana.
    >>> conv_ak('examples')
    'イー・エクス・エイ・エム・ピー・エル・イー・エス'

    Non alphabet letters are not convert(default), and Upper case lattters
    has (CAPS) or (大文字) flag(default).
    >>> conv_al('Examples002')
    'Echo(CAPS)-Xray-Alfa-Mike-Papa-Lima-Echo-Sierra-0-0-2'
    >>> conv_ak('Examples002')
    'イー（大文字）・エクス・エイ・エム・ピー・エル・イー・エス・0・0・2'

    You can change delimiter and Upper case letters flag.
    >>> conv_al('Examples003', '//', '(CAPITAL)')
    'Echo(CAPITAL)//Xray//Alfa//Mike//Papa//Lima//Echo//Sierra//0//0//3/'
    >>> conv_ak('Examples003', '//', '(CAPITAL)')
    'イー(CAPITAL)//エクス//エイ//エム//ピー//エル//イー//エス//0//0//3/'

    If you would like to convert numbers to phonetic code,
    set num_cnv_flag=True .
    >>> conv_al('Examples002', num_cnv_flag=True)
    'Echo(CAPS)-Xray-Alfa-Mike-Papa-Lima-Echo-Sierra-zero-zero-two'
    >>> conv_ak('Examples002', num_cnv_flag=True)
    'イー（大文字）・エクス・エイ・エム・ピー・エル・イー・エス・ゼロ・ゼロ・ニイ'
"""
from .a2pcej import *
