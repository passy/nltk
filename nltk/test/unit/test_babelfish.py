# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import unittest
from nltk.misc import babelfish

class BabelfishTest(unittest.TestCase):
    def test_greek(self):
        txt = 'Η Εταιρεία'
        translated_txt = babelfish.translate(txt, 'greek', 'english')
        self.assertEqual(translated_txt, 'The company')