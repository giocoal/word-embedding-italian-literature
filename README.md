# Distributional Semantics (word embedding with Word2Vec and CADE): the evolution of tópoi in the Italian literary tradition

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

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

The Greek term _tópoi_, in the singular _tòpos_, translated simply as "commonplace", identifies the repertoire of thematic and formal constants that constitute the morphological framework of the Western and Italian literary tradition.
Although the spectrum of narrative patterns that have characterized the literature produced in the Italian peninsula is broad and changing over time, _tòpos_ represent a form of imitatio that has never completely faded away, thus a useful tool for handing down the literary tradition.
Indeed, conventionality and recurrence allow _tòpos_ to traverse centuries and literary phases, yet lend themselves to the different formulations and interpretations of individual authors. Just think of the different visions of the locus amenous _tòpos_, the ideal place, which goes from 'natural earthly paradise' in classical literature to a grotesque and solitidune place in decadentism.

## Goals

The goals of our project were: 
1. to obtain corpora that were consistent with our research questions from a collection of texts obtained from two main sources 
2. to use distibutional semantics, and in particular algorithms from the word2vec family along with the CADE frameword in order to learn word embeddings from the generated and processed corpora 
3. and finally to Analyze some particularly long-lived _tòpos_, chosen arbitrarily, to be able to answer some research questions

The questions we asked ourselves were: 
1. How do the longest-lived literary _tòpos_ change in different historical periods ? and thus Does the historical-cultural context influence the recurring themes ? 
2. How do the canons proper to the different literary currents of Italian literature shape the representation of these common themes ?
3. Given some _tòpos_ and concepts peculiar to some of the greatest authors of Italian literature what are the correspondences in the works of other great authors ?

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/giocoal/word-embedding-italian-literature.svg?style=for-the-badge
[contributors-url]: https://github.com/giocoal/word-embedding-italian-literature/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/giocoal/word-embedding-italian-literature.svg?style=for-the-badge
[forks-url]: https://github.com/giocoal/word-embedding-italian-literature/network/members
[stars-shield]: https://img.shields.io/github/stars/giocoal/word-embedding-italian-literature.svg?style=for-the-badge
[stars-url]: https://github.com/giocoal/word-embedding-italian-literature/stargazers
[issues-shield]: https://img.shields.io/github/issues/giocoal/word-embedding-italian-literature.svg?style=for-the-badge
[issues-url]: https://github.com/giocoal/word-embedding-italian-literature/issues
[license-shield]: https://img.shields.io/github/license/giocoal/word-embedding-italian-literature.svg?style=for-the-badge
[license-url]: https://github.com/giocoal/word-embedding-italian-literature/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/giorgio-carbone-63154219b/
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com
