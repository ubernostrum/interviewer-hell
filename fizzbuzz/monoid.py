"""
FizzBuzz via monoid.

This file requires Python 3.12 or newer to run.

Based on this idea:

https://techhub.social/@fabianveal/111025513014174674

"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol, Self


class Monoid[T](Protocol):
    def mempty(self) -> Self: ...
    def mappend(self, other: Self) -> Self: ...


@dataclass
class String(Monoid[str]):
    value: str

    def mempty(self) -> String:
        return String("")

    def mappend(self, other: String) -> String:
        return String(self.value + other.value)

    def __add__(self, other: String) -> String:
        return self.mappend(other)


def mwhen[M: Monoid](condition: bool, monoid: M) -> M:
    return monoid if condition else monoid.mempty()


def fizzbuzz(n: int) -> String:
    _f = mwhen(n % 3 == 0, String("Fizz")) + mwhen(n % 5 == 0, String("Buzz"))
    return _f + mwhen(_f == String(""), String(str(n)))


if __name__ == "__main__":
    list(map(lambda i: print(fizzbuzz(i).value), range(1, 101)))
