from random import randrange
from csv import reader
import os

list_path_img_tag = []
with open('imagemAWS/marfrig_sem_ocr.csv') as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv)
    for linha in leitor_csv:
      #  os.system(f'wget {linha[1]}')#img carcaça
        list_path_img_tag.append(linha[2])
       # os.system(f'wget {linha[2]}')#img tag

counter = 0
range_max = len(list_path_img_tag)-1
while counter < 500:
    counter += 1
    position = randrange(0, range_max)
    path_img = list_path_img_tag[position]
    os.system(f'wget {path_img}')