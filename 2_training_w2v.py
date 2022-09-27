import os
from gensim.models import Word2Vec
import string

import multiprocessing
import time
import re

# La funzione seguente addestra un numero n di modelli per ciascuno dei corpus a disposizione

def training_W2V(file_name, #file .txt con frasi PROCESSATE, nome con cui salvare il modello  
                 n_mod,
                 path_source,
                 path_save,
                 workers,
                 epochs = 6): # numero di modelli da addestrare
        
        file_name_no_ext = file_name.replace(".txt","")                      
          
        print(f"{file_name_no_ext}: LOADING") 
        
        with open((path_source + file_name), encoding='utf-8') as read_file:
            nome_file_sentences = [simple_preproc(k).lower().split() for k in read_file.readlines()]
        
        for k in range(n_mod):
            try:
                with open(path_save + file_name_no_ext + "_" + str(k) + ".model", "r") as file:
                    nome_modello = file_name_no_ext + "_" + str(k)
                    print(f"{nome_modello}: GIÀ ALLENATO")
                    pass
            except FileNotFoundError:
                model = Word2Vec(sentences = nome_file_sentences,
                        #window = 5, default value
                        min_count=10, #not consider word with absolute frequency <10 
                        vector_size=300, #vector size 
                        sg = 1, #skipgram algorithm
                        hs = 0,
                        negative = 5, #negative sampling with 5 noise words
                        workers = workers, #faster process
                        epochs = epochs #6 iterations
                        )
                model.save(path_save + file_name_no_ext + "_" + str(k) + ".model")
            finally:
                pass
    
# La funzione seguente serve per caricare le sentences salvate nelle cartelle condivise
def simple_preproc(text):
    return text.translate(str.maketrans('', '', string.punctuation))

if __name__ == "__main__":
    # inserire path e definizione corpus da trattare
    path_source = "./data/Preprocessing/autori/frasi_NON_lemmatizzate_bigrammi/"
    path_save = "./data/Models/autori/frasi_NON_lemmatizzate_bigrammi/w2v/"
    nomi_dei_file = os.listdir(f"{path_source}")
    print(nomi_dei_file)
    st = time.time()
    
    #num_process = 6 # SET NUMERO DI CORE DA UTILIZZARE
    #with multiprocessing.Pool(processes=num_process) as pool:
    #    pool.map(training_W2V, nomi_dei_file)
    #pool.close()
    
    # Definisco parametri di training
    cores = multiprocessing.cpu_count()
    workers = cores - 1
    n_mod = 5
    epochs = 6
    
    for _ in nomi_dei_file:
        training_W2V(_, 
                     n_mod=n_mod, 
                     path_source=path_source,
                     path_save=path_save,
                     workers=workers,
                     epochs=epochs)
    en = time.time()
    print("time taken = ", en-st)