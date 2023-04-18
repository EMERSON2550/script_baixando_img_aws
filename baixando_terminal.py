from csv import reader
import os

cont  = 0
with open('marfrig_sem_ocr.csv') as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv)
    for linha in leitor_csv:
        if cont < 500:
            cont = cont + 1
        else:
            break
        #os.system(f'wget {linha[1]}')#img carcaça
        os.system(f'wget {linha[2]}')#img tag
    

