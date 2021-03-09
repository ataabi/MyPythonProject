import os
import os.path

def criarnome(max):
    import string
    from random import randint

    letters = string.ascii_letters
    alphdic = {}
    for n, l in enumerate(letters):
        alphdic[n+1] = l

    cx = alphdic[randint(1,52)]
    for c in range(1,max):
        c = alphdic[randint(1,52)]
        cx += c
    return cx


def criararquivo(type='txt',caracteres=8,diretorio=''):
    nome = criarnome(caracteres)
    a = open(f'{diretorio}{nome}.{type}', 'wt+')
    a.close()


def listar(diretorio,tipo='txt'):
    from os import walk
    for pasta in walk(diretorio):
        for lista in pasta:
            for n, arquivos in enumerate(lista):
                if len(arquivos) >= 3 :
                    if tipo == 0 :
                        print(arquivos, '\n')
                    else:
                        if tipo in arquivos:
                            print(arquivos,'\n')


def returnlist(diretorio,tipo='txt'):
    from os import walk
    listaarq = []
    for pasta in walk(diretorio):
        for lista in pasta:
            for arquivos in lista:
                if len(arquivos) >= 3 :
                    if tipo == 0 :
                        listaarq.append(arquivos)
                    else:
                        if tipo in arquivos:
                            listaarq.append(arquivos)
    return listaarq


def nameswap(diretorio,nome,tipo):
    for n, c in enumerate(returnlist(diretorio)):
        print(c)
        os.renames(f'{diretorio}{c}',f'{diretorio}{nome}{n}.{tipo}')



diretorio = ''
diretorio2 = ''

def trocarnome(diretorio,tipo):
    tipo = "mp4"
    for directory , subdirectory, filelist in os.walk(diretorio):
        for c in subdirectory:
            print(c)
        for arquivo in filelist:
            print(arquivo)
            novo = arquivo
            os.renames(f'{directory}/{arquivo}',f'{directory}/{novo}.{tipo}')
            print(f'{directory}/{novo}.{tipo}')


