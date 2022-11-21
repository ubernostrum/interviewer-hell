FizzBuzz
========

The ancient and immortal source of evil.

FizzBuzz was originally proposed as a way to weed out people with CS
degrees -- even postgraduate CS degrees from good schools -- who
couldn't put together a ``for`` loop. It kicked off a new era of
inhumane phone-screen trickery, and the only unsolved question about
it today is whether mocking solutions outnumber genuine ones.

The problem statement:

"Write a program that prints the numbers from 1 to 100. But for
multiples of three print 'Fizz' instead of the number and for the
multiples of five print 'Buzz'. For numbers which are multiples of
both three and five print 'FizzBuzz'."


The expected solution
---------------------

Really, anything that proves you can write a ``for`` loop and some
``if`` statements. Here's some Python::

    for i in range(1, 101):
        result = ""
	if i % 3 == 0:
	    result += "Fizz"
	if i % 5 == 0:
	    result += "Buzz"
	print(result or i)


The fun solutions
-----------------

A lot of people have taken cracks at FizzBuzz over the
years. Solutions show off language features like pattern matching, or
bring in trendy buzzwords like `machine learning
<http://joelgrus.com/2016/05/23/fizz-buzz-in-tensorflow/>`_.

I thought about taking a stab at an "enterprise" pattern-heavy
FizzBuzz, but `it's already been done
<https://github.com/EnterpriseQualityCoding/FizzBuzzEnterpriseEdition>`_
and far better than I could manage. Seriously, go look at that
link. It's written in Java and uses pretty much every idea from
*Design Patterns* except for Kitchen Sink, and probably someone's
added a pull request for that. My attempt in Python at a
Strategy/dependency-injection approach got to about ten classes before
I got tired of writing it and decided to just link a proper
implementation in this README.

So there are two solutions presented here, of slightly lower fun value.

In the file ``unrolled.py`` is a highly-optimized implementation of
FizzBuzz, transpiled from a solution in C with
``-funroll-loops``. It's perfect for the speed freak in your
interviewing life.

In the file ``fizzbuzz.py`` is an implementation that uses Python's
``itertools`` module to construct a lazy infinite iterable that yields
correct values, then slices off the first 100. It is a fully general
FizzBuzz solver, and you can invoke its ``make_fizzbuzz()`` function
with a dictionary mapping integers to the strings which should be
printed on multiples of those integers.

Also, since an original justification of FizzBuzz was to test whether
candidates could write a ``for`` loop and ``if`` statements, both
solutions presented here avoid not only the ``for`` keyword, but all
of Python's control-flow keywords.