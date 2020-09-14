---
title: 'Week 5'
---

## Learning Objectives

* Concepts:
  [lexical resources]{.nlp}
  [Swadesh lists]{.nlp}
  [pronouncing dictionaries]{.nlp}
  [wordnets]{.nlp}

(color key: [Python/Programming]{.py} [NLP/CL]{.nlp} [Software Engineering]{.eng})

## Reading

* [NLTK 2.4 -- Lexical Resources](http://www.nltk.org/book/ch02.html#lexical-resources)
* [NLTK 2.5 -- WordNet](http://www.nltk.org/book/ch02.html#wordnet)
  ([How To](http://www.nltk.org/howto/wordnet.html))

## Additional Links

* [Peter Norvig's Spelling Corrector](https://norvig.com/spell-correct.html) -- demonstrates something cool you can do with just a little bit of Python
* [ARPABET](https://en.wikipedia.org/wiki/ARPABET) -- the phonemic transcription system used by the CMU Pronouncing Dictionary
* WordNet
  - Documentation of relations: <https://globalwordnet.github.io/gwadoc>
  - Browse the modern English WordNet: <https://en-word.net/>
  - The Open Multilingual Wordnet: <http://compling.hss.ntu.edu.sg/omw/>

## Testing Your Knowledge

* Use the `nltk.corpus.words` wordlist to estimate the following for
  several text corpora:

  - what percentage of the text's vocabularly are not in the wordlist?
  - what percentage of the wordlist are present in the text?

* Use the ARPABET transcriptions in the `nltk.corpus.cmudict` corpus to
  devise a function for identifying rhyming words (how they are
  identified is up to you). What are the largest clusters of rhyming
  words?

* Use `nltk.corpus.wordnet` to explore word relations.
  - What are the **hyponyms** of *student*?
  - Use the `lowest_common_hypernyms()` method on synsets to find what is the shared hypernym of *student* and *professor*. How about *professor* and *lecturer*?
