import os
from gensim.models import Word2Vec
import string

import multiprocessing
import time
import re

def simple_preproc(text):
    return text.translate(str.maketrans('', '', string.punctuation))

if __name__ == "__main__":
    # inserire path e definizione corpus da trattare
    path_source = "./data/Preprocessing/fasi_letterarie/frasi_NON_lemmatizzate_bigrammi/"
    path_save = "./data/Preprocessing/fasi_letterarie/Corpus_CADE_bigrammi/"
    nomi_dei_file = os.listdir(f"{path_source}")
    print(nomi_dei_file)
    st = time.time()
    # num_process = 6 # SET NUMERO DI CORE DA UTILIZZARE
    # with multiprocessing.Pool(processes=num_process) as pool:
    #    pool.map(training_W2V, nomi_dei_file)
    # pool.close()
    for file in nomi_dei_file:
        with open(path_source + file, encoding='utf-8') as read_file:
            sentences = [simple_preproc(k).lower().split() for k in read_file.readlines()]
            with open(path_save+'CADE_'+file, mode='w', encoding='utf-8') as f:
                for s in sentences:
                    for w in s:
                        f.write(w+" ")
                    f.write('\n')
    en = time.time()
    print("time taken = ", en-st)
    
    
                    