#!/usr/bin/env python
# -*- coding: utf-8 -*-

class PhonemeError(Exception):
    pass

class UnrecognizedSymbolsError(PhonemeError):
    def __init__(self, symbols):
        self.symbols = symbols
        super().__init__('Unrecognized phonetic symbols %s' % symbols)
