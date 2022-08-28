#!/usr/bin/env python
# -*- coding: utf-8 -*-

class PhonemeError(Exception):
    pass

class UnrecognizedSymbolsError(PhonemeError):
    def __init__(self, symbols, word):
        self.symbols = symbols
        self.partial_arpabet = word.translate_to_arpabet()
        super().__init__(f'Unrecognized phonetic symbols {symbols}')
