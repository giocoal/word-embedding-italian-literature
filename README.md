# Distributional Semantics (Word2Vec and CADE): the evolution of tópoi in the Italian literary tradition

## Requirements
* python 3.7+
* multiprocessing
* Pandas
* Numpy
* cade
  * [Info & Download](https://federicobianchi.io/cade/)
* gensim
* smart_open
* spacy
  * it_core_news_lg: `python -m spacy download it_core_news_lg`
* simplemma
* nltk

## Introduction 

The Greek term topoi, in the singular topos, translated simply as "commonplace", identifies the repertoire of thematic and formal constants that constitute the morphological framework of the Western and Italian literary tradition.
Although the spectrum of narrative patterns that have characterized the literature produced in the Italian peninsula is broad and changing over time, topos represent a form of imitatio that has never completely faded away, thus a useful tool for handing down the literary tradition.
Indeed, conventionality and recurrence allow topos to traverse centuries and literary phases, yet lend themselves to the different formulations and interpretations of individual authors. Just think of the different visions of the locus amenous topoi, the ideal place, which goes from 'natural earthly paradise' in classical literature to a grotesque and solitidune place in decadentism.

## Goals

The goals of our project were: 
1. to obtain corpora that were consistent with our research questions from a collection of texts obtained from two main sources 
2. to use distibutional semantics, and in particular algorithms from the word2vec family along with the CADE frameword in order to learn word embeddings from the generated and processed corpora 
3. and finally to Analyze some particularly long-lived topoi, chosen arbitrarily, to be able to answer some research questions

The questions we asked ourselves were: 
1. How do the longest-lived literary topoi change in different historical periods ? and thus Does the historical-cultural context influence the recurring themes ? 
2. How do the canons proper to the different literary currents of Italian literature shape the representation of these common themes ? and finally 
3. Given some topoi and concepts peculiar to some of the greatest authors of Italian literature what are the correspondences in the works of other great authors ?
