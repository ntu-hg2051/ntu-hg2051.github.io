---
title: 'Week 2'
---

## Learning Objectives

* Data types: [`int`]{.py} [`float`]{.py} [`str`]{.py} [`list`]{.py} [`set`]{.py}
* Concepts: [assignment]{.py} [functions]{.py} [types-vs-tokens]{.nlp} [tokenization]{.nlp} [normalization]{.nlp} [frequency distributions]{.nlp} [unit tests]{.eng}
* Tools: [notebooks]{.eng} [NLTK]{.nlp}

(color key: [Python/Programming]{.py} [NLP/CL]{.nlp} [Software Engineering]{.eng})

## Reading

The readings for this week come from the official Python tutorial. The topic is "Using Python as a Calculator", but it is a good introduction to numbers, strings, and lists.

* [3.1 -- Using Python as a Calculator](https://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator)
  - [3.1.1 -- Numbers](https://docs.python.org/3/tutorial/introduction.html#numbers)
  - [3.1.2 -- Strings](https://docs.python.org/3/tutorial/introduction.html#strings)
  - [3.1.3 -- Lists](https://docs.python.org/3/tutorial/introduction.html#lists)

Additionally, please read the section on sets (only this section, *not*
the rest of the chapter):

* [5.4 -- Sets](https://docs.python.org/3/tutorial/datastructures.html#sets)

It helps to play with a Python interpreter while reading. Open up Visual
Studio Code's terminal and start Python (e.g., run `python3` or `py` at
the command prompt), then try out the examples for yourself.

## Testing Your Knowledge

There are two methods not mentioned in the tutorial:

- `str.split()` -- splits a string on whitespace and returns a list of substrings

  ```{.python .terminal}
  >>> "one two two".split()
  ['one', 'two', 'two']
  ```

- `list.count(x)` -- return the number of times that `x` occurs in a sequence (e.g., a list or a string)

  ```{.python .terminal}
  >>> ['one', 'two', 'two'].count('one')
  1
  >>> ['one', 'two', 'two'].count('two')
  2
  >>> 'one two two'.count('o')
  3
  ```

Given the following string:

```{.python .terminal}
s = ('There are seven days, there are seven days, '
     'there are seven days in a week. '
     'Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday')
```

Try to answer the following questions:

- How many times does the word "day" occur in the string?
- How many times do the tokens "day", "days", and "days," (note the comma) occur in the list of tokens (use `split()`)?
- How many tokens are there in total?
- Find the relative frequency of the token "are" (number of times it occurs over the count of all tokens)
- What is the set of unique words?
- What is the set of unique letters?
