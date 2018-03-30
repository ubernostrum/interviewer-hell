"""
Solves FizzBuzz by creating an infinite lazy iterator yielding correct
values, then slicing off as much as is desired.

"""

from functools import reduce
from itertools import cycle, islice
from operator import add


make_fizzbuzz = lambda mod_map, start: map(
    lambda tup: reduce(add, tup[1]) or tup[0],
    enumerate(zip(*map(
        lambda tup: cycle([""] * (tup[0] - 1) + [tup[1]]),
        mod_map.items()
    )), start))


print("\n".join(map(str, islice(
    make_fizzbuzz({
        3: 'Fizz',
        5: 'Buzz',
    }, 1), 100))))
