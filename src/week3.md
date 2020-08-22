---
title: 'Week 3'
---

## Learning Objectives

* Data types:
  [`str`]{.py}
  [`list`]{.py}
  [`set`]{.py}
* Concepts:
  [comparisons]{.py}
  [conditionals]{.py}
  [loops]{.py}
  [comprehensions]{.py}
  [functions]{.py}
  [filtering]{.nlp}
  [stopwords]{.nlp}
  [efficiency]{.eng}
* Tools:
  [NLTK]{.nlp}

(color key: [Python/Programming]{.py} [NLP/CL]{.nlp} [Software Engineering]{.eng})

## Reading

### Control Flow

The Python tutorial has a good and concise explanation of Python's basic
control-flow mechanisms:

* [3.2 -- First Steps Towards Programming](https://docs.python.org/3/tutorial/introduction.html#first-steps-towards-programming)
* [4 -- More Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html)
  - [4.1 -- `if` Statements](https://docs.python.org/3/tutorial/controlflow.html#if-statements)
  - [4.2 -- `for` Statements](https://docs.python.org/3/tutorial/controlflow.html#for-statements)
  - [4.3 -- The `range()` Function](https://docs.python.org/3/tutorial/controlflow.html#the-range-function)
  - [4.4 -- `break` and `continue` Statements, and `else` Clauses on Loops](https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops)
  - [4.5 -- `pass` Statements](https://docs.python.org/3/tutorial/controlflow.html#pass-statements)

### Functions

This section on defining functions extends what we talked about in class
in Week 2):

* [4.6 -- Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)

### Strings Methods

For now we will cover a subset of the available [string
methods](https://docs.python.org/3/library/stdtypes.html#string-methods):

  - [str.startswith()](https://docs.python.org/3/library/stdtypes.html#str.startswith)
  - [str.endswith()](https://docs.python.org/3/library/stdtypes.html#str.endswith)
  - [str.isalpha()](https://docs.python.org/3/library/stdtypes.html#str.isalpha)
  - [str.isdigit()](https://docs.python.org/3/library/stdtypes.html#str.isdigit)
  - [str.split()](https://docs.python.org/3/library/stdtypes.html#str.split)
  - [str.splitlines()](https://docs.python.org/3/library/stdtypes.html#str.splitlines)
  - [str.join()](https://docs.python.org/3/library/stdtypes.html#str.join)
  - [str.lower()](https://docs.python.org/3/library/stdtypes.html#str.lower)
  - [str.replace()](https://docs.python.org/3/library/stdtypes.html#str.replace)
  - [str.strip()](https://docs.python.org/3/library/stdtypes.html#str.strip)

### List Methods and Other Uses

Lists also have a number of useful methods and :

* [5.1 -- More on Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
 - [5.1.1 -- Using Lists as Stacks](https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-stacks)
 - [5.1.3 -- List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
* [5.2 -- The `del` statement](https://docs.python.org/3/tutorial/datastructures.html#the-del-statement)

### The `in` Operator

Many kinds of "containers" in Python (which include strings, lists,
sets, and other structures) work with Python's `in` operator. For most
containers, an `x in y` operation returns `True` if `x` is one of the
elements contained in `y`. For strings, it returns `True` if `x` is a
subsequence of the elements of `y`:

```python
>>> my_list = [1, 2, 3]
>>> 2 in my_list           # check for an individual element
True
>>> [1, 2] in my_list      # this does not work
False
>>> [1, 2] in [[1, 2], 3]  # unless the list actually has [1, 2] as an element
True
>>> my_str = '123'
>>> '2' in my_str          # a single character is just a string with one character
True
>>> '12' in my_str         # `in` with strings checks for substrings
True
>>> '12' in '1 2 3'        # subsequences must be exact (spaces count)
False

```

**Question:** How might you check for the presence of subsequences in lists? (hint: consider the methods or operations in the reading [above](#list-methods-and-other-uses))

### Stopwords

Finally, also read this section of the NLTK book, but just the part
about "stopwords" (just a few sentences and code blocks):

* [NLTK 4.1 -- Wordlist Corpora](http://www.nltk.org/book/ch02.html#wordlist-corpora)

## Testing Your Knowledge

Ensure you have the NLTK's 'gutenberg' and 'stopwords' corpora
downloaded by importing `nltk` and running the following two commands in
Python (after `>>>`):

```python
>>> import nltk
>>> nltk.download('gutenberg')
[nltk_data] Downloading package gutenberg to
[nltk_data]     /home/goodmami/nltk_data...
[nltk_data]   Package gutenberg is already up-to-date!
True
>>> nltk.download('stopwords')
[nltk_data] Downloading package stopwords to
[nltk_data]     /home/goodmami/nltk_data...
[nltk_data]   Package stopwords is already up-to-date!
True
```

You can find the available corpora like this:

```python
>>> nltk.corpus.gutenberg.fileids()
['austen-emma.txt', 'austen-persuasion.txt', 'austen-sense.txt', 'bible-kjv.txt', 'blake-poems.txt', 'bryant-stories.txt', 'burgess-busterbrown.txt', 'carroll-alice.txt', 'chesterton-ball.txt', 'chesterton-brown.txt', 'chesterton-thursday.txt', 'edgeworth-parents.txt', 'melville-moby_dick.txt', 'milton-paradise.txt', 'shakespeare-caesar.txt', 'shakespeare-hamlet.txt', 'shakespeare-macbeth.txt', 'whitman-leaves.txt']
```

Then get the NLTK's "raw" (string) version of one of these as follows
(here I get "Moby Dick"):

```python
>>> moby_dick = nltk.corpus.gutenberg.raw('melville-moby_dick.txt')
```

Now `moby_dick` is a big string containing the entire book. Use this
string and the string methods in your reading to answer the following
questions:

* How many lines are in the file?
* Is each line exactly one complete sentence?
* How many tokens are in the file?
* What is the average number of tokens per line?

Also use list or set comprensions to filter tokens to answer the
following questions:

* How many unique, case-normalized tokens are in the book?
* What proportion of the case-normalized tokens are, or are not, stopwords?
* What is the set of tokens in the book that begin with "whale"?
* What is the set of tokens in the book that begin with "whale" and are all alphabetic characters?
