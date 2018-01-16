# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unittest

from a2pcej import conv_ak, conv_al


class TestCommands(unittest.TestCase):
    """ test commands """

    def test_conv_al(self):
        """ test conv_al """
        vaild_values = [
            ('examples', 'Echo-Xray-Alfa-Mike-Papa-Lima-Echo-Sierra'),
            ('Examples002', 'Echo(CAPS)-Xray-Alfa-Mike-Papa-Lima-Echo-Sierra-0-0-2'),
            ('hoge', 'Hotel-Oscar-Golf-Echo'),
            ('h0ge', 'Hotel-0-Golf-Echo'),
            ('HogE', 'Hotel(CAPS)-Oscar-Golf-Echo(CAPS)'),
            ('h0ge#', 'Hotel-0-Golf-Echo-#'),
        ]
        for input_value, expect_value in vaild_values:
            self.assertEqual(expect_value, conv_al(input_value))

    def test_conv_al_with_opt(self):
        """ test conv_al with options """
        vaild_values = [
            ('Examples003', 'Echo(CAPITAL), Xray, Alfa, Mike, Papa, Lima, Echo, Sierra, 0, 0, 3', {'delimiter': ', ', 'sign':'(CAPITAL)'}),
            ('Examples004', 'Echo(CAPS)-Xray-Alfa-Mike-Papa-Lima-Echo-Sierra-zero-zero-four', {'num': True}),
        ]
        for input_value, expect_value, option in vaild_values:
            self.assertEqual(expect_value, conv_al(input_value, **option))

    def test_conv_ak(self):
        """ test conv_ak """
        vaild_values = [
            ('examples', 'イー・エクス・エイ・エム・ピー・エル・イー・エス'),
            ('Examples002', 'イー（大文字）・エクス・エイ・エム・ピー・エル・イー・エス・0・0・2'),
            ('hoge', 'エイチ・オー・ジー・イー'),
            ('h0ge', 'エイチ・0・ジー・イー'),
            ('HogE', 'エイチ（大文字）・オー・ジー・イー（大文字）'),
            ('h0ge#', 'エイチ・0・ジー・イー・#'),
        ]
        for input_value, expect_value in vaild_values:
            self.assertEqual(expect_value, conv_ak(input_value))


    def test_conv_ak_with_opt(self):
        """ test conv_ak with options """
        vaild_values = [
            ('Examples003', 'イー(大)／エクス／エイ／エム／ピー／エル／イー／エス／0／0／3', {'delimiter': '／', 'sign':'(大)'}),
            ('Examples004', 'イー（大文字）・エクス・エイ・エム・ピー・エル・イー・エス・ゼロ・ゼロ・ヨン', {'num': True}),
        ]
        for input_value, expect_value, option in vaild_values:
            self.assertEqual(expect_value, conv_ak(input_value, **option))
