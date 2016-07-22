# -*- coding: utf-8 -*-
"""convert Alphabet to Phonetic Code in English and Japanease."""


class A2pcej:
    alphabet_en = {
        'A': 'Alfa',
        'B': 'Bravo',
        'C': 'Charlie',
        'D': 'Delta',
        'E': 'Echo',
        'F': 'Foxtrot',
        'G': 'Golf',
        'H': 'Hotel',
        'I': 'India',
        'J': 'Juliett',
        'K': 'Kilo',
        'L': 'Lima',
        'M': 'Mike',
        'N': 'November',
        'O': 'Oscar',
        'P': 'Papa',
        'Q': 'Quebec',
        'R': 'Romeo',
        'S': 'Sierra',
        'T': 'Tango',
        'U': 'Uniform',
        'V': 'Victor',
        'W': 'Whiskey',
        'X': 'Xray',
        'Y': 'Yankee',
        'Z': 'Zulu',
    }
    alphabet_kana = {
        'A': 'エイ',
        'B': 'ビー',
        'C': 'シー',
        'D': 'ディー',
        'E': 'イー',
        'F': 'エフ',
        'G': 'ジー',
        'H': 'エイチ',
        'I': 'アイ',
        'J': 'ジェイ',
        'K': 'ケイ',
        'L': 'エル',
        'M': 'エム',
        'N': 'エヌ',
        'O': 'オー',
        'P': 'ピー',
        'Q': 'キュー',
        'R': 'アール',
        'S': 'エス',
        'T': 'ティー',
        'U': 'ユー',
        'V': 'ヴィー',
        'W': 'ダブリュー',
        'X': 'エクス',
        'Y': 'ワイ',
        'Z': 'ゼット',
    }
    number_en = {
        "0": "zero",
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine",
    }
    number_kana = {
        "0": "ゼロ",
        "1": "イチ",
        "2": "ニイ",
        "3": "サン",
        "4": "ヨン",
        "5": "ゴウ",
        "6": "ロク",
        "7": "シチ",
        "8": "ハチ",
        "9": "キュウ（数字）",
    }
    phonetics = {
        'alphabet_en': alphabet_en,
        'alphabet_kana': alphabet_kana,
        "number_en": number_en,
        "number_kana": number_kana,
    }


def _converter(use_phonetics, letters, delimiter, upper_sign, num_cnv_flag):
    phonetic_dict = A2pcej.phonetics[use_phonetics]
    phonetic_num_dict = A2pcej.phonetics['number_' + use_phonetics.split('_')[1]]
    converted_letters = ''
    for i in list(letters):
        if i.upper() in phonetic_dict.keys():
            converted_letters += phonetic_dict[i.upper()]
            if i.isupper():
                converted_letters += upper_sign
        elif (i.isdigit() and num_cnv_flag ):
            converted_letters += phonetic_num_dict[i]
        else:
            converted_letters += i
        converted_letters += delimiter
    return converted_letters[:-1]


def conv_al(letters, delimiter='-', upper_sign='(CAPS)', num_cnv_flag=False):
    return _converter('alphabet_en', letters, delimiter, upper_sign, num_cnv_flag)


def conv_ak(letters, delimiter='・', upper_sign='（大文字）', num_cnv_flag=False):
    return _converter('alphabet_kana', letters, delimiter, upper_sign, num_cnv_flag)
