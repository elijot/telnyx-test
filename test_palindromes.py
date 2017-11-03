# -*- coding: utf-8 -*-
# !/usr/bin/env python
import csv
import os
import unittest

from palindromes import ternary, is_palindrome, get_palindromes, save_csv, CSV_DELIMITER, QUOTE_CHAR


class PalindromesTest(unittest.TestCase):
    def test_ternary(self):
        expected_results = [
            {'number': 97, 'base': 2, 'repr': 1100001},
            {'number': 97, 'base': 3, 'repr': 10121},
            {'number': 97, 'base': 4, 'repr': 1201},
            {'number': 97, 'base': 5, 'repr': 342},
            {'number': 97, 'base': 6, 'repr': 241},
            {'number': 97, 'base': 7, 'repr': 166},
            {'number': 97, 'base': 8, 'repr': 141},
            {'number': 97, 'base': 9, 'repr': 117},
            {'number': 100, 'base': 2, 'repr': 1100100},
            {'number': 100, 'base': 3, 'repr': 10201},
            {'number': 100, 'base': 4, 'repr': 1210},
            {'number': 100, 'base': 5, 'repr': 400},
            {'number': 100, 'base': 6, 'repr': 244},
            {'number': 100, 'base': 7, 'repr': 202},
            {'number': 100, 'base': 8, 'repr': 144},
            {'number': 100, 'base': 9, 'repr': 121},
            {'number': 103, 'base': 2, 'repr': 1100111},
            {'number': 103, 'base': 3, 'repr': 10211},
            {'number': 103, 'base': 4, 'repr': 1213},
            {'number': 103, 'base': 5, 'repr': 403},
            {'number': 103, 'base': 6, 'repr': 251},
            {'number': 103, 'base': 7, 'repr': 205},
            {'number': 103, 'base': 8, 'repr': 147},
            {'number': 103, 'base': 9, 'repr': 124}
        ]
        for el in expected_results:
            self.assertEqual(str(el['repr']), ternary(el['number'], el['base']))

        # 0 case
        self.assertEqual(str(0), ternary(0, 2))

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome('1'))
        self.assertTrue(is_palindrome('101'))
        self.assertFalse(is_palindrome('100'))
        self.assertFalse(is_palindrome('10'))

    def test_get_palindromes(self):
        expected = [
            (1, 2),
            (2, 3),
            (3, 2),
            (4, 3),
            (5, 2),
            (6, 5),
            (7, 2),
            (8, 3),
            (9, 2),
            (10, 3),
            (11, 10),
            (12, 5),
            (13, 3),
            (14, 6),
            (15, 2),
            (16, 3),
            (17, 2),
            (18, 5),
            (19, 18),
            (20, 3)
        ]
        results = get_palindromes(start=1, end=20, start_base=2)
        for i, el in enumerate(results):
            self.assertEqual(el, expected[i])

        # should not be equal
        self.assertNotEqual([(2, 2)], get_palindromes(start=2, end=2, start_base=3))

        # should throw exception
        with self.assertRaises(ValueError):
            get_palindromes(1, 2, 1)

    def test_save_csv(self):
        results = [
            (1, 2),
            (2, 3),
            (3, 2)
        ]
        test_csv_file = 'save_csv.test.csv'
        if os.path.exists(test_csv_file):
            os.remove(test_csv_file)
        save_csv(results, test_csv_file)

        # validate if file exists
        self.assertTrue(os.path.exists(test_csv_file))

        # validate content
        saved_data = []
        with open(test_csv_file, 'r') as csvfile:
            row = csv.reader(csvfile, delimiter=CSV_DELIMITER, quotechar=QUOTE_CHAR)
            for r in row:
                saved_data.append(tuple(int(el) for el in r))
        self.assertEqual(saved_data, results)
