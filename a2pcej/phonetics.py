# -*- coding: utf-8 -*-
"""convert Alphabet to Phonetic Code in English and Japanease."""
from __future__ import unicode_literals


def make_alphabet_dict(p_list):
    return {chr(65 + k): v for k, v in enumerate(p_list) if k < 25}


def make_num_dict(p_list):
    return {str(k): v for k, v in enumerate(p_list) if k < 10}


class A2pcej:
    alphabet_en = [
        'Alfa', 'Bravo', 'Charlie', 'Delta', 'Echo', 'Foxtrot', 'Golf',
        'Hotel', 'India', 'Juliett', 'Kilo', 'Lima', 'Mike', 'November',
        'Oscar', 'Papa', 'Quebec', 'Romeo', 'Sierra', 'Tango', 'Uniform',
        'Victor', 'Whiskey', 'Xray', 'Yankee', 'Zulu'
    ]
    alphabet_ja = [
        'エイ', 'ビー', 'シー', 'ディー', 'イー', 'エフ', 'ジー',
        'エイチ', 'アイ', 'ジェイ', 'ケイ', 'エル', 'エム', 'エヌ',
        'オー', 'ピー', 'キュー', 'アール', 'エス', 'ティー', 'ユー',
        'ヴィー', 'ダブリュー', 'エクス', 'ワイ', 'ゼット',
    ]
    number_en = [
        'zero', 'one', 'two', 'three', 'four', 'five',
        'six', 'seven', 'eight', 'nine',
    ]
    number_ja = [
        'ゼロ', 'イチ', 'ニイ', 'サン', 'ヨン', 'ゴウ',
        'ロク', 'シチ', 'ハチ', 'キュウ',
    ]

    phonetics = {
        'alphabet_en': make_alphabet_dict(alphabet_en),
        'alphabet_ja': make_alphabet_dict(alphabet_ja),
        "number_en": make_num_dict(number_en),
        "number_ja": make_num_dict(number_ja),
    }
