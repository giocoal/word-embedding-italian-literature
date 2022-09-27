# ---- PACCHETTI E OPERAZIONI PRELIMINARI ----

from re import I
import nltk  # Natural Language Processing package
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from gensim.models import Phrases # Bigrammi
from gensim.models.phrases import Phraser
import unicodedata  # Pulizia dei caratteri speciali
import random
from collections import Counter
from nltk.corpus import wordnet
import string
import sys
import io


import os
import multiprocessing
import time

# Stopwords

from gensim.parsing.preprocessing import remove_stopwords
from nltk.corpus import stopwords
nltk.download('stopwords')
stops = set(stopwords.words('italian'))
nltk_stopwords = nltk.corpus.stopwords.words('italian')

# Per dividere il testo in frasi in base ai punti
nltk.download('punkt')

# Lemmatization
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('omw-1.4')
lemmatizer = WordNetLemmatizer()

# Position tag
def get_wordnet_pos(word):
    """Map POS tag to first character lemmatize() accepts"""
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}

    return tag_dict.get(tag, wordnet.NOUN)




# ---- FUNZIONI ----

def simple_preproc(text):  # Pre-preprocessing per la costruzione dei bigrammi
    return text.translate(str.maketrans('', '', string.punctuation))

# Generazione dei bigrammi
def build_phrases(sentences): # La funzione vuole in input le frasi già processate
    phrases = Phrases(sentences,
                      min_count=5,
                      threshold=10,
                      progress_per=1000)
    return Phraser(phrases)

# Ricostruzione delle frasi con i bigrammi
def sentence_to_bi_grams(phrases_model, sentence):
    return ' '.join(phrases_model[sentence])

def savesentencesnl(filename, sentences, path_save):
    #os.chdir('/content/drive/MyDrive/Magistrale/Secondo semestre/DS/Progetto/Sentences_nl')
    with open((path_save + filename), 'w', encoding='utf-8') as fp:
        for sentence in sentences:
            fp.write(str(sentence) + '\n')

def preprocessing_w_bigrams(file_name, 
            path_source = './data/Corpora/periodi_storici/', 
            path_save='./data/Preprocessing/periodi_storici/frasi_NON_lemmatizzate_bigrammi/',
            path_totBigrams = './data/Preprocessing/periodi_storici/'):
    try:
        with open(path_save + file_name, "r", encoding='utf-8') as file:
            print(f"{file_name}: GIÀ PROCESSATO")
            pass
    except FileNotFoundError:
        print(f"{file_name}: PROCESSANDO !")
        output = ""
        with open((path_source + file_name), encoding='utf-8') as f:
            for line in f:
                if not line.isspace():  # Rimuovo linee vuote
                    output += line
        # Divido il testo in frasi, basandomi sui punti
        output_sentences = nltk.tokenize.sent_tokenize(output)
        filtered_sentences = []
        # 'Pulisco' ogni frase, una alla volta
        for sentence in output_sentences:
            # Metto tutto in lower case
            lower_sentence = sentence.lower()
            # Rimuovo caratteri non alfa numerici
            noalfa_sentence = [w for w in word_tokenize(
                lower_sentence) if (w.isalpha() == True)]
            # Rimuovo le stopwords e le parole di un solo carattere che potrebbero non essere incluse nella lista delle stopwords
            filtered_sentence = [w for w in noalfa_sentence if (
                (w not in stops) and (len(w) > 1))]
            phrases_model = Phraser.load(path_totBigrams + 'full_bigrams_model.pkl')
            bigram_sentence = sentence_to_bi_grams(phrases_model, filtered_sentence)
            bigram_sentence = bigram_sentence.split() # Rimetto tutto in token
            # Ricostruisco la lista con le frasi 'pulite'
            if bigram_sentence:
                filtered_sentences.append(bigram_sentence)
            # Ricostruisco la lista con le frasi 'pulite'

        savesentencesnl(file_name, filtered_sentences, path_save)
        print(f"{file_name}: DONE!")
        # return filtered_sentences
    finally:
            pass



# --- MAIN ---

if __name__ == "__main__":
    #os.chdir('C:/Users/marco/OneDrive - Università degli Studi di Milano-Bicocca/data/Corpora/fasi_letterarie/')
    # inserire path e definizione corpus da trattare
    path_source = "./data/Corpora/periodi_storici/"
    path_save = "./data/Preprocessing/periodi_storici/frasi_NON_lemmatizzate_bigrammi/"
    path_totCorpus = './data/Corpora/altro/total_corpus/'
    path_save_big_mod = './data/Preprocessing/periodi_storici/'
    nomi_dei_file = os.listdir(f"{path_source}")

    # Unione dei corpus
    with open(path_totCorpus + 'total_corpus_periodi_storici.txt', 'w', encoding='utf-8') as outfile:
        for fname in nomi_dei_file:
            with open(path_source + fname, encoding='utf-8') as infile:
                outfile.write(infile.read())

    # Eseguo il simple pre-processing sull'intero corpus
    with open(path_totCorpus + 'total_corpus_periodi_storici.txt', encoding='utf-8') as read_file:
        sentences = [simple_preproc(k).lower().split() for k in read_file.readlines()]
    phrases_model = build_phrases(sentences)
    phrases_model.save(path_save_big_mod + 'full_bigrams_model.pkl')

    # multiprocessing
    # os.chdir(path)
    st = time.time()
    cores = multiprocessing.cpu_count()
    num_process = cores - 1
    with multiprocessing.Pool(processes=num_process) as pool:
        pool.map(preprocessing_w_bigrams, nomi_dei_file)
    pool.close()
    en = time.time()
    print("time taken = ", en-st)