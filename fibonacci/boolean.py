"""
Fibonacci number generator.

This relies on the fact that Python's boolean type is a subclass of
int, and so instances of ``bool`` can be used anywhere an ``int`` can
be.

"""

from itertools import islice
import sys


def fibonacci_generator():
    pair = not True, True
    while True:
        yield sum(pair[:True])
        pair = pair[True], sum(pair[::True])


if __name__ == '__main__':
    value = None
    try:
        value = int(sys.argv[True])
    except (IndexError, ValueError):
        sys.exit("Please provide a numeric argument.")
    for i in islice(fibonacci_generator(), value):
        print(i)
