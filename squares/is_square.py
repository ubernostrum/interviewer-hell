"""
Determines whether a given integer is a perfect square, without using
sqrt() or multiplication.

"""

import sys
import typing
import unittest
from itertools import accumulate, count, takewhile

is_square: typing.Callable[[int], bool] = (
    lambda n: n == 0
    or n > 0
    and n in takewhile(lambda x: x <= n, accumulate(filter(lambda n: n & 1, count())))
)


class SquareTests(unittest.TestCase):
    def test_squares(self):
        for i in range(1, 101):
            if i in (1, 4, 9, 16, 25, 36, 49, 64, 81, 100):
                assert is_square(i)
            else:
                assert not is_square(i)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(unittest.main())
    value = None
    try:
        value = int(sys.argv[1])
    except TypeError:
        sys.exit("Please provide a numeric argument.")
    if is_square(value):
        print("{} is a square.".format(value))
    else:
        print("{} is not a square.".format(value))
