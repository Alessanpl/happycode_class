# encoding: utf-8

"""
Problema: Dado um diretório com diversos arquivos do tipo 
.pdf, .xlxs e .docx, separá-los por tipo em diretórios diferentes

Passos do algoritmo:

1. Criar os três diretórios chamados pdf, xlxs e docx
2. Varrer diretório Todos e para cada arquivo verificar o tipo:
   Se pdf -> copiar para diretório pdf
   Se xlxs -> copiar para diretório xlxl
   Se docx -> copiar para diretório docx

"""

pasta = "/Users/Alessanpl/Downloads/Todos/"

# Criar os três diretórios

import os
import shutil

os.makedirs(pasta + 'pdf', exist_ok=True)
os.makedirs(pasta + 'xlsx', exist_ok=True)
os.makedirs(pasta + 'docx', exist_ok=True)

# Varrer o diretório Todos e copiar os arquivos para os respectivos diretórios

diretorio = os.listdir(pasta)

for arquivo in diretorio:
    if os.path.isfile(pasta + arquivo) and arquivo.endswith('pdf'):
        shutil.move(pasta + arquivo, pasta + 'pdf/' + arquivo)

    if os.path.isfile(pasta + arquivo) and arquivo.endswith('xlsx'):
        shutil.move(pasta + arquivo, pasta + 'xlsx/' + arquivo)  
        
    if os.path.isfile(pasta + arquivo) and arquivo.endswith('docx'):
        shutil.move(pasta + arquivo, pasta + 'docx/' + arquivo)  
