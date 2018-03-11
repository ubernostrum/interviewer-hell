Anagram detector
================

We've all run into this one. The usual problem statement is something
like:

"Write a function which takes two strings as input, and returns true
if they're anagrams of each other, false otherwise."

In theory, this is one of those problems that's supposed to also test
how well you explore the scope. Generally, anagrams ignore whitespace,
punctuation and differences in case, but you're supposed to ask about
it anyway to prove how diligent you are.


The expected solution
---------------------

Some interviewers will use this question as a proxy for "Have you read
*Programming Pearls*", since Chapter 2 deals with an anagram-finding
problem. The solution presented there is to sort the letters of a word
into alphabetical order -- so that, for example, ``"stressed"`` and
``"desserts"`` each sort into ``"deerssst"``. Then simply compare the
sorted values to determine whether the inputs are
anagrams. *Programming Pearls* presents this in the context of
searching a large list of words for all anagrams of a given input
word, and uses binary search on a list of words sorted in this
fashion. This is an acceptable solution.

In the Python standard library, you can also use
``collections.Counter`` as a histogram data structure, feeding strings
into instances of ``Counter`` to determine what letters are in them
and how many occurrences there are of each letter. Which leads to an
easy implementation (presuming some suitable normalization done before
invoking ``is_anagram()``)::

    from collections import Counter

    def is_anagram(s1, s2):
        return Counter(s1) == Counter(s2)

This is also an acceptable solution.


The fun solution
----------------

The file ``primes.py`` in this directory uses the same *principle* --
creating a unique signature for each word, based on which letters it
contains and how many times each letter occurs -- but takes a numeric,
rather than string-oriented, approach.

The ``is_anagram()`` function there maps each uppercase ASCII letter
to a prime number, which allows a string to be converted into a list
of primes which are then multiplied together. Anagram detection occurs
by checking whether the prime products of the two strings are
equal. Because prime factorization is unique, this will only occur
when the two lists of primes are identical (and thus when the two
input strings contain identical letters).

This solution also engages in a bit of Unicode geekery. It normalizes
the input strings to a decomposed form, discards any code points which
are not letters, and then round-trips to ASCII and back to eliminate
anything outside the ASCII range.

Finally, for sake of superficial efficiency, primes are not assigned
to ASCII letters in ascending order; instead the most common English
letters are assigned the lowest-valued primes.

A fun followup discussion is how the German letter "ß" should be
handled in a fully Unicode-aware followup question, especially in
light of the normalization to uppercase used in this
implementation. Historically, this letter did not have an uppercase
form, and in many modern programming languages it still uppercases to
"SS", which means that ``"straße"`` and ``"strasse"`` will be treated
as anagrams (since both normalize to ``"STRASSE"``). Bonus points if
you launch into a discussion of case folding as the proper
pre-normalization technique.

Credit goes to `this tweet from Fermat's Library
<https://twitter.com/fermatslibrary/status/958700402647674880>`_ for
reminding me of this approach. I do not, however, recall where I first
saw it.


Notes
-----

This solution works well in languages like Python which either do not
have multiple differently-sized integral types, or which offer an
integral type which does not make the programmer worry about
overflow. In languages with only fixed-size integral types, overflow
is a concern; the five-character input string ``"ZZZZZ"`` will
overflow a 32-bit integer, while the ten-character input string
"``ZZZZZZZZZZ"`` will overflow a 64-bit integer. If you are forced to
use a language like this for your interview, just go with the
*Programming Pearls* approach of sorting the letters, and revenge
yourself on the company some other way.
