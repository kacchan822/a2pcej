# -*- coding: utf-8 -*-
""" Convert Alphabet to Phonetic Code in English and Japanease."""
from __future__ import absolute_import, unicode_literals
from .phonetics import Phonetics


class A2pcej:
    """ A2pcej """
    def __init__(self, lang='ja', delimiter=None, sign=None, num=False):
        self.lang = lang
        self.num = num
        self.phonetics = Phonetics()
        try:
            # Ensure self.lang is used, not the potentially None 'lang' from init
            self.phonetic_dict = self.phonetics.get_phonetics(self.lang) 
        except KeyError:
            raise ValueError(f"Language '{self.lang}' is not supported.")

        self.delimiter = delimiter if delimiter is not None else self.phonetic_dict['delimiter']
        self.sign = sign if sign is not None else self.phonetic_dict['sign']

    def __converter__(self, letter):
        if letter.upper() in self.phonetic_dict['alphabet'].keys():
            phonetic_code = self.phonetic_dict['alphabet'][letter.upper()]
            if letter.isupper():
                phonetic_code += self.sign
        elif (letter.isdigit() and self.num):
            phonetic_code = self.phonetic_dict['number'][letter]
        else:
            phonetic_code = letter
        return phonetic_code

    def convert(self, letters):
        """ convert """
        converted_letters = []
        for letter in letters:
            converted_letters.append(self.__converter(letter))
        return self.delimiter.join(converted_letters)


def conv_al(letters, delimiter='-', sign='(CAPS)', num=False):
    """ Convert Alphabet to Phonetic Code in English. """
    converter = A2pcej(
        lang='en',
        delimiter=delimiter,
        sign=sign,
        num=num
    )
    return converter.convert(letters)


def conv_ak(letters, delimiter='・', sign='（大文字）', num=False):
    """ Convert Alphabet to Phonetic Code in Japanease. """
    converter = A2pcej(
        lang='ja',
        delimiter=delimiter,
        sign=sign,
        num=num
    )
    return converter.convert(letters)
