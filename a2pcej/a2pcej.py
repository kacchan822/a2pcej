# -*- coding: utf-8 -*-
"""convert Alphabet to Phonetic Code in English and Japanease."""
from __future__ import absolute_import, unicode_literals
from sys import version_info
from .phonetics import A2pcej


def _converter(phonetics, letters, delimiter, sign, num):
    if version_info[0] == 2:
        letters = letters.decode('utf-8')
    phonetic_dict = A2pcej.phonetics[phonetics]
    phonetic_num_dict = A2pcej.phonetics['number_' + phonetics.split('_')[1]]
    converted_letters = []
    for i in list(letters):
        if i.upper() in phonetic_dict.keys():
            i_phonetic = phonetic_dict[i.upper()]
            if i.isupper():
                i_phonetic += sign
            converted_letters.append(i_phonetic)
        elif (i.isdigit() and num):
            converted_letters.append(phonetic_num_dict[i])
        else:
            converted_letters.append(i)
    return delimiter.join(converted_letters)


def conv_al(letters, delimiter='-', sign='(CAPS)', num=False):
    return _converter('alphabet_en', letters, delimiter, sign, num)


def conv_ak(letters, delimiter='・', sign='（大文字）', num=False):
    return _converter('alphabet_ja', letters, delimiter, sign, num)
