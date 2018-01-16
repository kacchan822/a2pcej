import unittest

from a2pcej.phonetics import A2pcej


class TestPhonetics(unittest.TestCase):
    """ test class of phonetics.py """

    def test_phonetics(self):
        """ test method for phonetics """
        langs = ['en', 'ja']
        for lang in langs:
            alphabet_dict = A2pcej.phonetics['alphabet_'+lang]
            number_dict = A2pcej.phonetics['number_'+lang]
            self.assertTrue('A' in alphabet_dict.keys())
            self.assertTrue('Z' in  alphabet_dict.keys())
            self.assertTrue('0' in number_dict.keys())
            self.assertTrue('9' in  number_dict.keys())
