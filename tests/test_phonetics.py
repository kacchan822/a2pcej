# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unittest

from a2pcej.phonetics import Phonetics


class TestPhonetics(unittest.TestCase):
    """ test class of phonetics.py """

    def test_phonetics(self):
        """ test method for phonetics """
        langs = ['en', 'ja']
        for lang in langs:
            alphabet_dict = Phonetics().get_phonetics(lang)['alphabet']
            number_dict = Phonetics().get_phonetics(lang)['number']
            self.assertTrue('A' in alphabet_dict.keys())
            self.assertTrue('Z' in  alphabet_dict.keys())
            self.assertTrue('0' in number_dict.keys())
            self.assertTrue('9' in  number_dict.keys())
