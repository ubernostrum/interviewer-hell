"""
Determines whether a given integer is a perfect square, without using
sqrt() or multiplication.

This works because the square of an integer, n, is the sum of the
first n consecutive odd integers. Various itertools functions are used
to generate a lazy iterable of odd integers and a running sum of them,
until either the given integer is found as a sum or at least n odd
integers have been consumed.

"""

from itertools import accumulate, count, takewhile
import sys
import unittest


is_square = lambda n: n in takewhile(lambda x: x <= n, accumulate(filter(lambda n: n & 1, count())))


class SquareTests(unittest.TestCase):
    def test_squares(self):
        for i in range(1, 101):
            if i in (1, 4, 9, 16, 25, 36, 49, 64, 81, 100):
                assert is_square(i)
            else:
                assert not is_square(i)


if __name__ == '__main__':
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

        
