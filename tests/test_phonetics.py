# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unittest
import pytest  # Added for exception testing

from a2pcej.phonetics import Phonetics


class TestPhonetics(unittest.TestCase):  # unittest.TestCase can be kept or changed to object
    """ test class of phonetics.py """

    def setUp(self):
        """Setup method to create a Phonetics instance"""
        self.phonetics = Phonetics()

    def test_get_phonetics_basic_structure(self):
        """ Test that get_phonetics returns dicts with expected keys for supported languages """
        langs = ['en', 'ja']
        for lang in langs:
            phonetic_info = self.phonetics.get_phonetics(lang)
            self.assertIn('alphabet', phonetic_info)
            self.assertIn('number', phonetic_info)
            self.assertIn('delimiter', phonetic_info)
            self.assertIn('sign', phonetic_info)

            alphabet_dict = phonetic_info['alphabet']
            number_dict = phonetic_info['number']
            self.assertTrue('A' in alphabet_dict.keys())
            self.assertTrue('Z' in alphabet_dict.keys())
            self.assertTrue('0' in number_dict.keys())
            self.assertTrue('9' in number_dict.keys())

    def test_get_phonetics_default_values(self):
        """ Test get_phonetics returns correct default delimiter and sign """
        en_phonetics = self.phonetics.get_phonetics('en')
        self.assertEqual(en_phonetics['delimiter'], '-')
        self.assertEqual(en_phonetics['sign'], '(CAPS)')

        ja_phonetics = self.phonetics.get_phonetics('ja')
        self.assertEqual(ja_phonetics['delimiter'], '・')
        self.assertEqual(ja_phonetics['sign'], '（大文字）')

    def test_get_phonetics_unsupported_language(self):
        """ Test get_phonetics raises KeyError for unsupported language """
        with pytest.raises(KeyError) as excinfo:
            self.phonetics.get_phonetics('fr')
        self.assertIn("'fr' not found in DEFAULTS", str(excinfo.value))

    def test_get_alphabet_dict_unsupported_language(self):
        """ Test get_alphabet_dict raises KeyError for unsupported language """
        with pytest.raises(KeyError) as excinfo:
            self.phonetics.get_alphabet_dict('fr')
        self.assertIn("'fr' not found in ALPHABET", str(excinfo.value))

    def test_get_number_dict_unsupported_language(self):
        """ Test get_number_dict raises KeyError for unsupported language """
        with pytest.raises(KeyError) as excinfo:
            self.phonetics.get_number_dict('fr')
        self.assertIn("'fr' not found in NUMBER", str(excinfo.value))
