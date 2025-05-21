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

    DEFAULTS = {
        'en': {
            'delimiter': '-',
            'sign': '(CAPS)',
        },
        'ja': {
            'delimiter': '・',
            'sign': '（大文字）',
        },
    }

    def get_phonetics(self, lang):
        """ create phonetic code list for lang """
        if lang not in self.DEFAULTS:
            raise KeyError(f"Language '{lang}' not found in DEFAULTS.")
        defaults = self.DEFAULTS[lang]
        phonetics = {
            'alphabet': self.get_alphabet_dict(lang),
            'number': self.get_number_dict(lang),
            'delimiter': defaults['delimiter'],
            'sign': defaults['sign'],
        }
        return phonetics

    def get_alphabet_dict(self, lang):
        if lang not in self.ALPHABET:
            raise KeyError(f"Language '{lang}' not found in ALPHABET.")
        phonetics = self.ALPHABET[lang]
        return {chr(65 + k): v for k, v in enumerate(phonetics) if k < 26}

    def get_number_dict(self, lang):
        if lang not in self.NUMBER:
            raise KeyError(f"Language '{lang}' not found in NUMBER.")
        phonetics = self.NUMBER[lang]
        return {str(k): v for k, v in enumerate(phonetics) if k < 10}
