import os
from gensim.models import Word2Vec
from cade.cade import CADE

import multiprocessing
import time
import re

def training_CADE(file_names, #lista contenente i corpus usati per creare la compass, numero di slices da addestrare
                  n_mod,
                  path_source,
                  path_compass,
                  path_save,
                  workers): 
# LA LISTA TEXT CHE VIENE PASSATA COME VARIABILE DEVE CONTENERE I CORPUS NELLO STESSO ORDINE CON CUI SONO STATI USATI PER
# CREARE LA COMPASS. IO AVEVO PASSATO I NOMI SENZA ESTENSIONE .TXT PER FACILITARMI IL SALVATAGGIO
    aligner = CADE(min_count=10,  
                  size=300,
                  sg = 1, 
                  #hs = 0,
                  ns = 5, 
                  workers = workers,
                  siter = 6)
    
    for k in range(n_mod):
        print(f"ALLENANDO ALIGNER numero {k}")
        aligner.train_compass(path_compass, overwrite=True)
        for file_name in file_names:
            print(f"{file_name}: ALLENANDO modello {k}!")
            model_slice = aligner.train_slice((path_source + file_name)) #per trainare le slice ho bisogno del nome esatto del file .txt con cui ho creato il compasso
            file_name_no_ext = file_name.replace(".txt","") 
            model_slice.save(path_save + file_name_no_ext + '_cade_' + str(k) + '.model') #qui posso salvare il modello con un nome a piacere
        
        
if __name__ == "__main__":
    # inserire path e definizione corpus da trattare
    path_source = "./data/Preprocessing/autori/Corpus_CADE_bigrammi/"
    path_compass = "./data/Preprocessing/autori/compass_autori_bigrammi.txt"
    path_save = "./data/Models/autori/frasi_NON_lemmatizzate_bigrammi/CADE/"
    nomi_dei_file = os.listdir(f"{path_source}")
    print(nomi_dei_file)
    st = time.time()
    
    #num_process = 6 # SET NUMERO DI CORE DA UTILIZZARE
    #with multiprocessing.Pool(processes=num_process) as pool:
    #    pool.map(training_W2V, nomi_dei_file)
    #pool.close()
    
    # Definisco parametri di training
    cores = multiprocessing.cpu_count()
    #workers = cores - 1
    workers = 4
    n_mod = 5
    
    training_CADE(nomi_dei_file,
                n_mod=n_mod, 
                path_source=path_source,
                path_compass=path_compass,
                path_save=path_save,
                workers=workers)
    en = time.time()
    print("time taken = ", en-st)