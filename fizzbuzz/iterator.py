"""
Solves FizzBuzz by creating an infinite lazy iterator yielding correct
values, then slicing off as much as is desired.

"""

import functools
import itertools
import operator


make_fizzbuzz = lambda mod_map, start: map(
    lambda tup: functools.reduce(operator.add, tup[1]) or tup[0],
    enumerate(
        zip(
            *map(
                lambda tup: itertools.cycle([""] * (tup[0] - 1) + [tup[1]]),
                mod_map.items()
            )
        ), start
    )
)


# Implement the "standard" FizzBuzz: print "Fizz" on multiples of 3,
# "Buzz" on multiples of 5, "FizzBuzz" on multiples of both 3 and 5,
# number otherwise for numbers 1-100.
if __name__ == '__main__':
    print("\n".join(map(str, itertools.islice(
        make_fizzbuzz({
            3: 'Fizz',
            5: 'Buzz',
        }, 1),
        100))))
