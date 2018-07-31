# coding: utf-8
import unittest

import six

import matcher


class TestMatcher(unittest.TestCase):
    def test_positive(self):
        got = matcher.find_include_japanese_column(u"a as あ")
        self.assertEqual(got, [u"あ"])

    def test_pre_any_spaces(self):
        got = matcher.find_include_japanese_column(u"a as       あ")
        self.assertEqual(got, [u"あ"])

    def test_kanji(self):
        got = matcher.find_include_japanese_column(u"kanji as 漢字")
        self.assertEqual(got, [u"漢字"])

    def test_itaiji(self):
        got = matcher.find_include_japanese_column(u"itaiji as 髙")
        self.assertEqual(got, [u"髙"])

    def test_kisyuizonmoji(self):
        got = matcher.find_include_japanese_column(u"kisyuizonmoji as ①㊀㎆")
        self.assertEqual(got, [u"①㊀㎆"])

    def test_no_as(self):
        got = matcher.find_include_japanese_column(u"てすと")
        self.assertEqual(got, [])

    def test_multi_columns(self):
        got = matcher.find_include_japanese_column(u"a as あ, i as い")
        self.assertEqual(got, [u"あ", u"い"])

    def test_in_ascii_head(self):
        got = matcher.find_include_japanese_column(u"sum(a) as aの合計")
        self.assertEqual(got, [u"aの合計"])

    def test_in_ascii_middle(self):
        got = matcher.find_include_japanese_column(u"average(a) as 中間のaの平均")
        self.assertEqual(got, [u"中間のaの平均"])

    def test_in_ascii_tail(self):
        got = matcher.find_include_japanese_column(u"max(a) as 最大のa")
        self.assertEqual(got, [u"最大のa"])

    def test_as_upper(self):
        got = matcher.find_include_japanese_column(u"a AS あ")
        self.assertEqual(got, [u"あ"])

    def test_as_camel(self):
        got = matcher.find_include_japanese_column(u"a As あ")
        self.assertEqual(got, [u"あ"])

    def test_as_inverse_camel(self):
        got = matcher.find_include_japanese_column(u"a aS あ")
        self.assertEqual(got, [u"あ"])

