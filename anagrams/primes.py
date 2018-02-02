"""
Determines whether two (ASCII-only) strings are anagrams of each
other.

This works by assigning each ASCII letter in a string to a prime
number, and determining the resulting product for the
string. Comparing the products for two strings indicates whether they
are anagrams. Per the fundamental theorem of arithmetic, prime
factorization of a composite number is unique, so only two strings
whose sets of letters are identical will yield the same product.

"""

import functools
import operator
import sys
import unicodedata
import unittest


CHAR_MAP = dict(
    # Assign primes to letters, with lowest-valued primes assigned to
    # most-common letters in English.
    zip('ETAOINSHRDLUCMFYWGPBVKXQJZ',
        [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
         47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
    )
)


def normalize(s):
    """
    Normalizes a string for comparison.

    This first applies Unicode normalization to form NFKD, to
    decompose any composed forms in the string, then strips non-letter
    characters and round-trips to ASCII and back ignoring invalid
    characters. The result will consist only of uppercase ASCII
    letters.

    """
    normalized = ''.join(
        c for c in
        unicodedata.normalize('NFKD', s.upper())
        if unicodedata.category(c).startswith('L')
    )

    return normalized.encode('ascii', 'ignore').decode('ascii')


def string_product(s):
    """
    Computes the "product" of a string.

    The string in question should already be normalized to uppercase
    ASCII, letters only.

    """
    return functools.reduce(
        operator.mul,
        (CHAR_MAP[c] for c in s if c in CHAR_MAP)
    )


def is_anagram(s1, s2):
    """
    Determines whether two strings are anagrams of each other.

    The strings will be normalized to uppercase ASCII, and non-letter
    characters ignored. The only shortcut applied here is a length
    comparison; otherwise, comparison occurs via prime-number product
    of the strings.

    """
    s1, s2 = normalize(s1), normalize(s2)
    if len(s1) != len(s2):
        return False
    return string_product(s1) == string_product(s2)


class AnagramTests(unittest.TestCase):
    def test_anagrams(self):
        for pair in (
                ('tar', 'rat'),
                ('Stressed', 'desserts'),
                ('School master', 'the classroom'),
                ('the morse code', 'Here come dots!'),
                ('über', 'uber'),
                ('straße', 'strasse'),  # Controversy!
        ):
            self.assertTrue(is_anagram(pair[0], pair[1]))

    def test_non_anagrams(self):
        for pair in (
                ('rate' 'rat'),
                ('ban', 'bann'),
                ('über', 'ueber'),
                ('STRAẞE', 'STRASSE'),  # CONTROVERSY!
        ):
            self.assertFalse(is_anagram(pair[0], pair[1]))


if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit(unittest.main())
    s1, s2 = sys.argv[1:3]
    if is_anagram(s1, s2):
        print("Inputs are anagrams of each other")
    else:
        print("Inputs are not anagrams of each other")
