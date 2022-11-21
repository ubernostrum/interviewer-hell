Generating Fibonacci numbers
============================

The problem statement here is to generate `Fibonacci numbers
<https://en.wikipedia.org/wiki/Fibonacci_number>`_, providing a
function which either calculates the nth Fibonacci number, or prints
the first n numbers in the Fibonacci sequence.


The expected solution
---------------------

Varies depending on the interviewer's goals.

Some will use this as a FizzBuzz-esque test of basic programming
constructs, to see whether you can write a ``for`` loop or use
recursion.

Some will use it to see if you understand and can talk about taking
advantage of tail-call optimization, or as a jumping-off point into
topics like memoization, and possibly into asking for an
implementation of an LRU cache.

In some extreme cases it may be used as a linear-algebra shibboleth,
since calculating Fibonacci numbers via matrix exponentiation (``O(log
n)`` time) is faster than the iterative solution (``O(n)`` time) and
*much* faster than the recursive solution (``O(n^2)`` time).


The fun solution
----------------

The file ``fibonacci_generator.py`` in this directory implements a
Fibonacci sequence generator via the iterative algorithm, but uses no
explicit arithmetic operators and no integer literals.

The implementation abuses a historical quirk of the language. Python
originally lacked a boolean type, and most Python programmers used
integer ``0`` and ``1``, following the convention of C. When the
``bool`` type was added (in Python 2.3), it was implemented as a
subclass of ``int``, and its two instances, ``False`` and ``True``,
have integer values ``0`` and ``1``, respectively. As a result, it's
legal to use them in any expression which calls for an integer, since
they *are* instances of ``int``.

The use of a ``while True:`` loop in the generator body helps add to
the confusion, by being the only place where a ``bool`` is used for
its conventional purpose, and the ``True:`` in the loop statement
nicely mirrors the ``:True`` slice in the following line. The
``sum()`` built-in is used for style points (avoiding arithmetic
operators, and slightly obfuscating the in-place calculation) but also
as a sneaky way of "upcasting" from ``bool`` to plain ``int``, which
would otherwise have to be achieved via some method more likely to
rouse suspicion (such as doubled negation).
