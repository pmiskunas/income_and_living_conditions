# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 21:41:08 2021

@author: Home-PC
"""

# baigiamasis darbas.
# Parašyti skriptą, vizualizuojantį norimus duomenis apie namų ūkių biudžetus, būsto tipus, etc ...

import pandas as pd
import glob
import os

dctu = {}  # žodynas namų ukių duomenims
dcta = {}  # žodynas asmenų duomenims

cwd = os.getcwd()  # getting current folder path
folder = '\data_files\\'
path_read = cwd + folder
print(path_read)

f_list_u = glob.glob(str(path_read + '*i.csv'))  # susirenkam namu ukiu .csv
f_list_u2 = glob.glob(str(path_read + '*i.xls'))  # susirenkam namu ukiu .xls

for i in f_list_u:
    x = f_list_u.index(i)
    year = [int(n) for n in f_list_u[x].split() if n.isdigit()]
    df = pd.read_csv(i)
    dctu[year[0]] = df
for i in f_list_u2:
    x = f_list_u2.index(i)
    year = [int(n) for n in f_list_u2[x].split() if n.isdigit()]
    df = pd.read_excel(i)
    dctu[year[0]] = df
print(f'{len(dctu.keys())} files for income was read')

f_list_a = glob.glob(str(path_read + '*s.csv'))  # susirenkam asmenu .csv
f_list_a2 = glob.glob(str(path_read + '*s.xls'))  # susirenkam asmenu .xls
for i in f_list_a:
    x = f_list_a.index(i)
    year = [int(n) for n in f_list_a[x].split() if n.isdigit()]
    df = pd.read_csv(i)
    dcta[year[0]] = df
for i in f_list_a2:
    x = f_list_a2.index(i)
    year = [int(n) for n in f_list_a2[x].split() if n.isdigit()]
    df = pd.read_excel(i)
    dcta[year[0]] = df
print(f'{len(dcta.keys())} files for living conditions was read')

cwd = os.getcwd()  # getting current folder path
nf = 'output_csv\\'  # new folder name
path = os.path.join(cwd, nf)
try:
    os.mkdir(path)  # making new folder if doesn't exist
except Exception:
    pass

r = list(dcta.keys())  # exportuojames visus failus i csv, kad greiciau dirbtumem.
for i in r:
    dcta[i].to_csv(path + '\\' + str(i) + ' asmenys.csv', index=False)
    dctu[i].to_csv(path + '\\' + str(i) + ' namu ukiai.csv', index=False)
    print(f' .csv files for {i} year was created')

print(f'All .csv files was created in this directory: \n {path}')
