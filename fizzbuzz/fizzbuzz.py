"""
Solves FizzBuzz.

"""

from functools import reduce
from itertools import cycle, islice
from operator import add
import typing


make_fizzbuzz: typing.Callable[[dict, int], typing.Iterable[str]] = (
    lambda mod_map, start: map(
        lambda t: reduce(add, t[1]) or t[0],
        enumerate(zip(*map(
            lambda t: cycle([str()] * (t[0] - 1) + [t[1]]),
            mod_map.items()
        )), start))
)


print("\n".join(map(str, islice(
    make_fizzbuzz({
        3: "Fizz",
        5: "Buzz",
    }, 1), 100))))
