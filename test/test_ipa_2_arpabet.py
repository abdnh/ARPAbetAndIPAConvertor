import unittest
from arpabetandipaconvertor.phoneticarphabet2arpabet import PhoneticAlphabet2ARPAbetConvertor
from arpabetandipaconvertor.excepts import PhonemeError


class TestIPAToARPAbet(unittest.TestCase):

    def setUp(self):
        self._ipa_convertor = PhoneticAlphabet2ARPAbetConvertor()

    def test_convertor(self):
        # 单音节及()
        f = self._ipa_convertor.convert('faʊ(hh)nd')
        self.assertEqual(f, ('F AW1 N D', ''))

        # ri'trai 双音节
        f = self._ipa_convertor.convert('riˈtraɪ')
        self.assertEqual(f, ('R IY0 T R AY1', ''))

        # ˈɛniˌwʌn, -wən 三音节
        f = self._ipa_convertor.convert('ˈɛniˌwʌn, -wən')
        self.assertEqual(f, ('EH1 N IY0 W AH2 N', ''))

        #kʊd
        f = self._ipa_convertor.convert('kʊd')
        self.assertEqual(f, ('K UH1 D', ''))

        # wilkinsn 双音节
        f = self._ipa_convertor.convert("'wilkinsn")
        self.assertEqual(f, ('W IY1 L K IY0 N S N', ''))

        # 边缘测试 重音标识位置不对
        with self.assertRaises(PhonemeError) as cm:
            f = self._ipa_convertor.convert("wilkins'n")
        the_exception = cm.exception
        self.assertEqual(str(the_exception), 'ns\' Inappropriate accent mark - \' has no vowel in the previous syllable!')

        # 边缘测试 重音标识隔断完整的音符
        with self.assertRaises(PhonemeError) as cm:
            f = self._ipa_convertor.convert("wilkins'n")
        the_exception = cm.exception
        self.assertEqual(str(the_exception), 'ns\' Inappropriate accent mark - \' has no vowel in the previous syllable!')

        # 边缘测试 重音标识不对，并没有元音
        f = self._ipa_convertor.convert("wilkia'ʊsn")
        self.assertEqual(f, ('W IY0 L K IY0 <a>0 UH1 S N', '<a>'))

        # 边缘测试 最后一个音节美音找完整
        f = self._ipa_convertor.convert("wilki'sna")
        self.assertEqual(f, ('W IY0 L K IY0 S N <a>1', '<a>'))

        # 边缘测试 中间一个不完整的音节连带到做好匹配不到合适的音标
        f = self._ipa_convertor.convert("wilki'san")
        self.assertEqual(f, ('W IY0 L K IY0 S <an>1', '<an>'))






