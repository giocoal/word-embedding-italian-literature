import simplemma  # altro pacchetto per lemmatizzare
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from gensim.models import Phrases
import unicodedata  # Pulizia dei caratteri speciali
import random
from collections import Counter
import it_core_news_lg
import spacy  # altro pacchetto per lemmatizzare
from nltk.corpus import wordnet
import string
import sys
import io
import nltk  # Natural Language Processing package

import os
import multiprocessing
import time

# Stopwords

from gensim.parsing.preprocessing import remove_stopwords
from nltk.corpus import stopwords
# nltk.download('stopwords')
stops = set(stopwords.words('italian'))
nltk_stopwords = nltk.corpus.stopwords.words('italian')
# Valutare di aggiungere eventuali forme arcariche delle stopwords italiane, o se c'è necessità di estendere questa lista

# Bigrammi

# Per dividere il testo in frasi in base ai punti
# nltk.download('punkt')

# Per tokenizzare

# Per il discorso lemmatizzazione dobbiamo valutare come muoverci con l'italiano

# Lemmatization
# nltk.download('averaged_perceptron_tagger')
# nltk.download('wordnet')
# nltk.download('omw-1.4')
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


# Contatore parole uniche

# Per esplorare risultati


def preprocessing(file_name,
                  path_source="./data/Corpora/altro/italia_liberale_split_1/",
                  path_save="./data/Preprocessing/periodi_storici/"):
    try:
        with open(path_save + file_name, "r", encoding='utf-8') as file:
            print(f"{file_name}: GIÀ PROCESSATO")
            pass
    except FileNotFoundError:
        print(f"{file_name}: PROCESSANDO !")
        output = ""
        with open((path_source + file_name), encoding='utf-8') as f:
            for line in f:
                #print("ok")
                if not line.isspace():  # Rimuovo linee vuote
                    output += line

        # Divido il testo in frasi, basandomi sui punti
        output_sentences = nltk.tokenize.sent_tokenize(output)

        # Valutare se è necessario eliminare delle righe all'inizio o alla fine dei .txt se presentano licenze,...
        # output_sentences = output_sentences[:-]

        filtered_sentences = []
        # 'Pulisco' ogni frase, una alla volta
        for sentence in output_sentences:
            #print("ok1")
            # Metto tutto in lower case
            lower_sentence = sentence.lower()
            # Rimuovo caratteri non alfa numerici
            noalfa_sentence = [w for w in word_tokenize(
                lower_sentence) if (w.isalpha() == True)]
            # Rimuovo le stopwords e le parole di un solo carattere che potrebbero non essere incluse nella lista delle stopwords
            filtered_sentence = [w for w in noalfa_sentence if (
                (w not in stops) and (len(w) > 1))]
            # Ricostruisco la lista con le frasi 'pulite'
            if filtered_sentence:
                filtered_sentences.append(filtered_sentence)

        savesentencesnl(file_name, filtered_sentences, path_save)
        print(f"{file_name}: DONE!")
        # return filtered_sentences
    finally:
        pass


def savesentencesnl(filename, sentences, path_save):
    #os.chdir('/content/drive/MyDrive/Magistrale/Secondo semestre/DS/Progetto/Sentences_nl')
    with open((path_save + filename), 'w', encoding='utf-8') as fp:
        for sentence in sentences:
            fp.write(str(sentence) + '\n')


if __name__ == "__main__":
    # inserire path e definizione corpus da ttrattare
    path_source = "./data/Corpora/altro/italia_liberale_split_1/"
    # path_save = "./data/Preprocessing/autori/frasi_NON_lemmatizzate/"
    nomi_dei_file = os.listdir(f"{path_source}")
    print(nomi_dei_file)

    # multiprocessing
    # os.chdir(path)
    st = time.time()
    num_process = 6
    with multiprocessing.Pool(processes=num_process) as pool:
        pool.map(preprocessing, nomi_dei_file)
    pool.close()
    en = time.time()
    print("time taken = ", en-st)
    #frasi = preprocessing("Luigi Pirandello.txt")
    #savesentencesnl("Luigi Pirandello", frasi)
