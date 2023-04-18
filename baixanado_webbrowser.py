from csv import reader
import webbrowser


with open('imagemAWS/img.test.csv') as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv)
    for linha in leitor_csv:
        webbrowser.open(linha[1])
        webbrowser.open(linha[2])



