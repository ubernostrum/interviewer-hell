Palindrome detector
===================

Apparently a lot of companies nowadays have palindrome detection as a
core part of their business, because I've seen this problem more often
than any other in early-stage screens.

Problem statement:

"Write a function which takes a string as input, and returns true if
that string is a palindrome, false otherwise."

This is one of those "prove you're diligent by asking questions about
scope" problems where you're supposed to "wonder" whether whitespaces,
case differences and punctuation matter. They do, always, but you have
to ask to get the full marks.


The expected solution
---------------------

Check whether the string is the same when read forwards or
backwards. Either normalize it to a single case and to remove
punctuation/whitespace, or ignore case and skip non-letter characters
while reading.

Bonus points sometimes go to "clever" solutions like using two
pointers -- one starting at each end -- and walking them toward the
middle of the string, comparing as you go, but these solutions are
uncommon in languages that don't do lots of manual
exposing/manipulating of memory.

Assuming you have the normalization figured out, you can one-line this
in Python::

    is_palindrome = lambda s: s == s[::-1]


The fun solution
----------------

The file ``is_palindrome.py`` in this directory uses the same eventual
technique as the one-line solution above. However, it is written in a
way that lets you lecture your interviewer about Unicode and the true
complexities of palindrome detection. Which, in the cutthroat world of
modern palindromes-as-a-service software, proves your qualifications.

Here are a few of the potential issues:

* First you can talk about the difficulties involved in doing this
  with a string type that only exposes bytes (as the "just use UTF-8"
  people favor), because anything outside the ASCII range is going to
  require multiple bytes to encode. This creates traps where a string
  that is a palindrome when considered as Unicode code points is not a
  palindrome when considered as bytes.

* Then you can step up a level to languages which expose strings as
  sequences of code points. This solves some issues, but now you have
  to deal with composed versus decomposed forms in many common Latin
  scripts, which gives an opportunity to talk about normalization. The
  code point approach still isn't perfect, though, as there are plenty
  of strings which are visually palindromes, but are not palindromes
  when considered as sequences of code points, even after
  normalization. Many non-Latin scripts are this way; Korean is
  probably the ultimate torture test for a palindrome detector.

* And then you bring out the big gun: graphemes. All the issues
  discussed above are due to the mismatch between how humans visually
  regard the rendered string, and how computers store it and expose it
  to a programmer for use. The Unicode abstraction for the visual
  thing we actually care about here is the grapheme, and a palindrome
  is a string which consists of the same sequence of graphemes when
  read in either direction.

The solution given here uses `a third-party regex module for Python
<https://pypi.python.org/pypi/regex>`_ , which provides an
implementation of the Unicode grapheme-matching metacharacter in order
to split the input string at grapheme boundaries.

Also, for bonus points, explain why you used normalization form NFC
instead of NFKC. Studying the test suite may be illuminating.


Notes
-----

Languages which natively understand graphemes have a major advantage
here. For example, in Swift the building block of strings is the
``Character`` type, which is a grapheme cluster rather than a code
point. If you choose one of these languages, you can still deliver the
Unicode lecture, and then explain how you've chosen a language which
deals with these problems for you.
