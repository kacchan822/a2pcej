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
    converted_letters = ''
    for i in list(letters):
        if i.upper() in phonetic_dict.keys():
            converted_letters += phonetic_dict[i.upper()]
            if i.isupper():
                converted_letters += sign
        elif (i.isdigit() and num):
            converted_letters += phonetic_num_dict[i]
        else:
            converted_letters += i
        converted_letters += delimiter
    return converted_letters[:-1]


def conv_al(letters, delimiter='-', sign='(CAPS)', num=False):
    return _converter('alphabet_en', letters, delimiter, sign, num)


def conv_ak(letters, delimiter='・', sign='（大文字）', num=False):
    return _converter('alphabet_kana', letters, delimiter, sign, num)
