"""
Determines whether two (ASCII-only) strings are anagrams of each
other.

"""

import functools
import operator
import sys
import unicodedata
import unittest


CHAR_MAP = dict(
    zip("ETAOINSHRDLUCMFYWGPBVKXQJZ",
        [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
         47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
    )
)


def normalize(s: str) -> str:
    """
    Normalizes a string for comparison.

    """
    normalized = "".join(
        c for c in
        unicodedata.normalize("NFKD", s.upper())
        if unicodedata.category(c).startswith("L")
    )

    return normalized.encode("ascii", "ignore").decode("ascii")


def string_product(s: str) -> int:
    """
    Computes the product of a string.

    """
    return functools.reduce(
        operator.mul,
        (CHAR_MAP[c] for c in s if c in CHAR_MAP)
    )


def is_anagram(s1: str, s2: str) -> bool:
    """
    Determines whether two strings are anagrams of each other.

    """
    s1, s2 = normalize(s1), normalize(s2)
    if len(s1) != len(s2):
        return False
    return string_product(s1) == string_product(s2)


class AnagramTests(unittest.TestCase):
    def test_anagrams(self):
        for pair in (
                ("tar", "rat"),
                ("Stressed", "desserts"),
                ("School master", "the classroom"),
                ("the morse code", "Here come dots!"),
                ("über", "uber"),
                ("straße", "strasse"),  # Controversy!
        ):
            self.assertTrue(is_anagram(pair[0], pair[1]))

    def test_non_anagrams(self):
        for pair in (
                ("rate" "rat"),
                ("ban", "bann"),
                ("über", "ueber"),
                ("STRAẞE", "STRASSE"),  # CONTROVERSY!
        ):
            self.assertFalse(is_anagram(pair[0], pair[1]))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(unittest.main())
    s1, s2 = sys.argv[1:3]
    if is_anagram(s1, s2):
        print("Inputs are anagrams of each other")
    else:
        print("Inputs are not anagrams of each other")
