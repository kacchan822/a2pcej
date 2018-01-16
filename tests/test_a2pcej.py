import unittest

from a2pcej import conv_ak, conv_al


class TestCommands(unittest.TestCase):
    """ test commands """

    def test_conv_ak(self):
        """ test conv_ak """
        vaild_values = [
            ('hoge', 'エイチ・オー・ジー・イー'),
            ('h0ge', 'エイチ・0・ジー・イー'),
            ('HogE', 'エイチ（大文字）・オー・ジー・イー（大文字）'),
            ('h0ge#', 'エイチ・0・ジー・イー・#'),
        ]
        for input_val, output_val in vaild_values:
            self.assertEqual(output_val, conv_ak(input_val))

    def test_conv_al(self):
        """ test conv_al """        
        vaild_values = [
            ('hoge', 'Hotel-Oscar-Golf-Echo'),
            ('h0ge', 'Hotel-0-Golf-Echo'),
            ('HogE', 'Hotel(CAPS)-Oscar-Golf-Echo(CAPS)'),
            ('h0ge#', 'Hotel-0-Golf-Echo-#'),
        ]
        for input_val, output_val in vaild_values:
            self.assertEqual(output_val, conv_al(input_val))
