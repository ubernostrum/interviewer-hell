"""
Determines whether a string is a palindrome.

Requires the third-party 'regex' library; to obtain, 'pip install
regex'. See https://pypi.python.org/pypi/regex for details.

"""

import sys
import unicodedata
import unittest

import regex


def is_palindrome(s):
    """
    Determines whether a given string is a palindrome.

    """
    normalized = ''.join(
        c for c in 
        unicodedata.normalize('NFC', s.lower())
        if unicodedata.category(c).startswith('L')
    )
    graphemes = [
        g for g in regex.split(r'(\X)', normalized) if g
    ]
    return graphemes == graphemes[::-1]


class PalindromeTests(unittest.TestCase):
    def test_palindromes(self):
        for p in (
                'racecar',
                'tacocat',
                'Able was I, ere I saw Elba.',
                'A man, a plan, a canal: Panama!',
                'an\u0303a',
                'a\u00f1a',
                '\ufdfa',
        ):
            self.assertTrue(is_palindrome(p))

    def test_non_palindrome(self):
        for p in (
                'not',
                'Able was I, ere I saw Elbe.',
                unicodedata.normalize('NFKC', '\ufdfa'),
        ):
            self.assertFalse(is_palindrome(p))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(unittest.main())
    if is_palindrome(sys.argv[1]):
        print("Input is a palindrome.")
    else:
        print("Input is not a palindrome.")
