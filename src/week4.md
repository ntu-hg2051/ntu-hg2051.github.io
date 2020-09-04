---
title: 'Week 4'
---

## Learning Objectives

* Constants:
  [`True`]{.py}
  [`False`]{.py}
  [`None`]{.py}
* Data types:
  [`bool`]{.py}
  [`tuple`]{.py}
  [`dict`]{.py}
* Concepts:
  [mutability]{.eng}
  [side-effects]{.eng}
  [exceptions]{.py}
  [advanced functions]{.py}
  [text corpora]{.nlp}
  [conditional frequency distributions]{.nlp}
* Tools:
  [NLTK]{.nlp}

(color key: [Python/Programming]{.py} [NLP/CL]{.nlp} [Software Engineering]{.eng})

## Reading

### Constants

Python has several special constant values ("constant" meaning they have
predefined, unchangeable values). For present purposes, we only care
about `True`, `False`, and `None`. The [Dive Into
Python](https://diveintopython3.problemsolving.io) book has a good and
concise description of these:

* [DIP 2.2 -- Booleans](https://diveintopython3.problemsolving.io/native-datatypes.html#booleans)
* [DIP 2.8 -- None](https://diveintopython3.problemsolving.io/native-datatypes.html#none)

Another thing to add about `None` is that it is often used as a
placeholder for optional arguments and it is the return value of
function with no `return` statement or an empty `return` statement. For
example:

  ```python
  >>> def func(x=None):
  ...     print('this function prints', x, 'but returns None')
  ... 
  >>> x = func()
  this function prints None but returns None
  >>> print(x)
  None
  >>> x = func(5)
  this function prints 5 but returns None
  >>> print(x)
  None
  ```

### Data Types

The Python Tutorial has some good entries on `tuple` and `dict`:

* [PT 5.3 -- Tuples and Sequences](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)
* [PT 5.5 -- Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

In addition, `bool` is the type of the constants `True` and `False`. In
practice the explicit use of the `bool()` function is rarely necessary
as it is implicit in an `if` statement, but it can be useful in
interactive sessions for determining the boolean value of objects:

```python
>>> bool()           # bool of nothing is False
False
>>> bool(True)       # these are almost tautological...
True
>>> bool(False)
False
>>> bool(0)          # 0 is the only False-valued integer
False
>>> bool(-1)         # all other integers are True
True
>>> bool(99999)
True
>>> bool('')         # the empty string is the only False string
False
>>> bool('foo')      # all others are True
True
>>> bool('False')    # even deceptive ones
True
>>> bool([])         # empty containers (list, tuple, set, dict, etc.) are False
False
>>> bool([1, 2, 3])  # all others are True
True
>>> bool([[]])       # even if their contents would be False
True
```

### Functions

For further topics on functions, see the Python Tutorial's section on
default and keyword arguments:

* [PT 4.7.1 -- Default Argument Values](https://docs.python.org/3/tutorial/controlflow.html#default-argument-values)
* [PT 4.7.2 -- Keyword Arguments](https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments)

### Text Corpora

The NLTK provides interfaces to a variety of common and freely-available
corpora. Read chapter 2 section 1 of the NLTK book to get an overview.
You don't need to follow all the code examples, but try to be able to
answer questions like these:

- What is a text corpus?
- What kinds of corpora does the NLTK provide?
- What are things you can do with a text corpus?
- What is the difference between an annotated and unannotated corpus?
- How might some text corpus structures be more or less appropriate for certain NLP tasks?

You don't have to read all the section in 2.1. Focus on these for now:

* [NLTK 2.1 -- Accessing Text Corpora](http://www.nltk.org/book/ch02.html#accessing-text-corpora)
  - [NLTK 2.1.1 -- Gutenberg Corpus](http://www.nltk.org/book/ch02.html#gutenberg-corpus)
  - [NLTK 2.1.3 -- Brown Corpus](http://www.nltk.org/book/ch02.html#brown-corpus)
  - [NLTK 2.1.6 -- Annotated Text Corpora](http://www.nltk.org/book/ch02.html#annotated-text-corpora)
  - [NLTK 2.1.7 -- Corpora in Other Languages](http://www.nltk.org/book/ch02.html#corpora-in-other-languages)
  - [NLTK 2.1.8 -- Text Corpus Structure](http://www.nltk.org/book/ch02.html#text-corpus-structure)

### Conditional Frequency Distribution

Earlier we discussed frequency distribution and used the NLTK's
`FreqDist` class. Now we will introduce conditional frequency
distributions. Please read the following:

* [NLTK 2.2 -- Conditional Frequency Distributions](http://www.nltk.org/book/ch02.html#conditional-frequency-distributions)
  - [NLTK 2.2.1 -- Conditions and Events](http://www.nltk.org/book/ch02.html#conditions-and-events)
  - [NLTK 2.2.2 -- Counting Words by Genre](http://www.nltk.org/book/ch02.html#counting-words-by-genre)
  - [NLTK 2.2.3 -- Plotting and Tabulating Distributions](http://www.nltk.org/book/ch02.html#plotting-and-tabulating-distributions)

## Testing Your Knowledge

### Dictionaries

Get a feel for Python's `dict` type by creating and inspecting some
dictionaries. Use `help(dict)` in Python to browse the available methods
(ignore the ones that start with `__` for now). Try to read a list of
words and create a dictionary mapping each letter to the set of words
starting with the letter. For example:

```python
>>> def letter_lookup(words):
...     # your code here
>>> d = letter_lookup('python programming provides endless possibilities'.split())
>>> d['p']
{'python', 'provides', 'programming', 'possibilities'}
>>> d['e']
{'endless'}
```

### Text Corpora and Conditional Frequencies

* Use the NLTK's Brown corpus and `ConditionalFreqDist` class to find
  what are the most frequent words for each genre of the Browne corpus.
* Try again but first filter out stopwords.
