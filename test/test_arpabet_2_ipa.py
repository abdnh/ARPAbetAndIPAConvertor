import unittest
from arpabetandipaconvertor.arpabet2phoneticalphabet import ARPAbet2PhoneticAlphabetConvertor
from arpabetandipaconvertor.excepts import PhonemeError


class TestIPAToARPAbet(unittest.TestCase):

    def setUp(self):
        self._arpabet_convertor = ARPAbet2PhoneticAlphabetConvertor()

    def test_convertor_ipa(self):
        #单音节
        f = self._arpabet_convertor.convert_to_american_phonetic_alphabet('F AW1 N D')
        self.assertEqual(f, 'faʊnd')

        # ri'trai  双音节
        f = self._arpabet_convertor.convert_to_american_phonetic_alphabet('R IY0 T R AY1')
        self.assertEqual(f, 'riˈtraɪ')

        # ˈɛniˌwʌn, -wən 三音节
        f = self._arpabet_convertor.convert_to_american_phonetic_alphabet('EH1 N IY0 W AH2 N')
        self.assertEqual(f, 'ˈɛniˌwʌn')

        #kʊd 单音节
        f = self._arpabet_convertor.convert_to_american_phonetic_alphabet('K UH1 D')
        self.assertEqual(f, 'kʊd')

        # 双音节
        f = self._arpabet_convertor.convert_to_american_phonetic_alphabet("W IY1 L K IY0 N S N")
        self.assertEqual(f, 'ˈwilkinsn')

        # 边缘测试：重音标识不对
        with self.assertRaises(PhonemeError) as cm:
            f = self._arpabet_convertor.convert_to_american_phonetic_alphabet("W IY1 L K IY4 N S N")
        the_exception =cm.exception
        self.assertEqual(str(the_exception), 'IY The accent mark is incorrect, marked as 4')

        # 边缘测试：ARPAbet不对
        with self.assertRaises(PhonemeError) as cm:
            f = self._arpabet_convertor.convert_to_american_phonetic_alphabet("W IY1 L K IG N S N")
        the_exception =cm.exception
        self.assertEqual(str(the_exception), 'IG Can\'t match the appropriate phonetic symbol')


        # 边缘测试：重音标识位置不对
        with self.assertRaises(PhonemeError) as cm:
            f = self._arpabet_convertor.convert_to_american_phonetic_alphabet("W IY1 L K IY N1 S N")
        the_exception =cm.exception
        self.assertEqual(str(the_exception), 'N1 The accent mark is in the wrong place - the current N is not a vowel')

        # 边缘测试：标记重音的ARPAbet不对
        with self.assertRaises(PhonemeError) as cm:
            f = self._arpabet_convertor.convert_to_american_phonetic_alphabet("W IY1 L K IY X1 S N")
        the_exception =cm.exception
        self.assertEqual(str(the_exception), 'X Can\'t match the appropriate phonetic symbol')


