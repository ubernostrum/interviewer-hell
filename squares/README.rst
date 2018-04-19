Detecting perfect squares
=========================

You can find this one on a number of interview-problem sites. Here's a
problem statement:

"Write a function which takes an integer as input, and returns true if
that integer is a perfect square, false otherwise. You may not use
your language's sqrt() function."

Some variations also disallow use of multiplication or exponentiation
operators.


The expected solution
---------------------

This is almost a pure shibboleth question; the interviewer is waiting
for you to regurgitate `Newton's method
<https://en.wikipedia.org/wiki/Newton%27s_method>`_.


The fun solution
----------------

The file ``odds.py`` in this directory implements square-detection in
a deliberately obfuscated way. It relies on the fact that the square
of a natural number, ``n``, is equal to the sum of the first ``n``
consecutive odd natural numbers. The approach, then, is to calculate a
series of sums of consecutive odd integers, and see if the given input
occurs among them. If the input ``n`` has not been found by the time
the sum exceeds ``n``, it returns false.

A second, less-obfuscated implementation is provided in the file
``odds.c``, to make it more clear what's going on, but the
Python solution should be preferred whenever possible.

The primary source of fun here is in showing off Python's lazy
iterables, and the useful functions in the ``itertools`` module. The
one-line ``is_square()`` function looks like it has no business
whatsoever accomplishing what it does, and offers an opportunity to
leave interviewers in a slightly dazed state after walking them
through what's happening.

An additional source of lecture material in this solution is the
ability to talk about the question not as a problem of numeric
calculation, but a problem of set membership. Many problems --
including a lot of fundamental ones in CS -- are or turn into
set-membership problems, and framing a question this way can often
yield useful insights into how to solve it.


Notes
-----

The solution given in Python would translate well to other languages
with lazy iterables and easy operations on them. It's likely to be a
one-liner in Haskell, for example.

For languages with fixed-size integral types, overflow is a
concern. Whatever type you're asked to check, use a wider type to
store your running sum in (i.e., the provided C implementation checks
an ``int`` and so uses a ``long`` for the running sum).
