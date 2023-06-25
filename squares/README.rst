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

I haven't seen this one for a while, and when I did it was a pure
shibboleth question, where the interviewer wanted to hear about
`Newton's method <https://en.wikipedia.org/wiki/Newton%27s_method>`_
for approximating a square root.

But more recently, this apparently has become popular as a test to see
if someone will think to use binary search to quickly work through the
space of possible square roots of the input. Here's a simple Python
implementation::

    def is_square(n):
        lower, upper = 0, n

        while lower <= upper:
            candidate = (lower + upper) // 2
            check = candidate ** 2
            if check == n:
                return True
            lower, upper = (lower, candidate - 1) if check > n else (candidate + 1, upper)
            
        return False


The fun solution
----------------

The file ``is_square.py`` in this directory implements
square-detection in a deliberately obfuscated way. It relies on the
fact that the square of a natural number, ``n``, is equal to the sum
of the first ``n`` consecutive odd natural numbers. The approach,
then, is to calculate a series of sums of consecutive odd integers,
and see if the given input occurs among them. If the input has not
been found by the time the sum exceeds the input, it returns false.

A C# implementation using a similar iterator-based approach is
provided in teh file ``SquareDetector.cs``.

The primary source of fun here is in showing off Python's lazy
iterables, and the useful functions in the ``itertools`` module. The
``is_square()`` function looks like it has no business whatsoever
accomplishing what it does, and offers an opportunity to leave
interviewers in a slightly dazed state after walking them through
what's happening.

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
store your running sum in (i.e., the provided C# implementation checks
an ``int`` and so uses a ``long`` for the running sum).
