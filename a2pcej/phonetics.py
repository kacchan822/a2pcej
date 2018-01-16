# -*- coding: utf-8 -*-
""" Phonetic Code in English and Japanease. """
from __future__ import unicode_literals


class Phonetics:
    """ Phonetics """
    ALPHABET = {
        'en': [
            'Alfa',
            'Bravo',
            'Charlie',
            'Delta',
            'Echo',
            'Foxtrot',
            'Golf',
            'Hotel',
            'India',
            'Juliett',
            'Kilo',
            'Lima',
            'Mike',
            'November',
            'Oscar',
            'Papa',
            'Quebec',
            'Romeo',
            'Sierra',
            'Tango',
            'Uniform',
            'Victor',
            'Whiskey',
            'Xray',
            'Yankee',
            'Zulu'
        ],
        'ja': [
            'エイ',
            'ビー',
            'シー',
            'ディー',
            'イー',
            'エフ',
            'ジー',
            'エイチ',
            'アイ',
            'ジェイ',
            'ケイ',
            'エル',
            'エム',
            'エヌ',
            'オー',
            'ピー',
            'キュー',
            'アール',
            'エス',
            'ティー',
            'ユー',
            'ヴィー',
            'ダブリュー',
            'エクス',
            'ワイ',
            'ゼット'
        ],
    }

    NUMBER = {
        'en': [
            'zero',
            'one',
            'two',
            'three',
            'four',
            'five',
            'six',
            'seven',
            'eight',
            'nine'
        ],
        'ja':  [
            'ゼロ',
            'イチ',
            'ニイ',
            'サン',
            'ヨン',
            'ゴウ',
            'ロク',
            'シチ',
            'ハチ',
            'キュウ'
        ],
    }

    def get_phonetics(self, lang):
        """ create phonetic code list for lang """
        phonetics = {
            'alphabet': self.get_alphabet_dict(lang),
            'number': self.get_number_dict(lang),
        }
        return phonetics

    def get_alphabet_dict(self, lang):
        phonetics = self.ALPHABET.get(lang)
        return {chr(65 + k): v for k, v in enumerate(phonetics) if k < 26}

    def get_number_dict(self, lang):
        phonetics = self.NUMBER.get(lang)
        return {str(k): v for k, v in enumerate(phonetics) if k < 10}
