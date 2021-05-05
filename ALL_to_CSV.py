# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 21:41:08 2021

@author: Home-PC
"""

# baigiamasis darbas.
# Parašyti skriptą, vizualizuojantį norimus duomenis apie namų ūkių biudžetus, būsto tipus, etc ...

import pandas as pd
import glob


dctu = {}  # žodynas namų ukių duomenims
dcta = {}  # žodynas asmenų duomenims
    
f_list_u = glob.glob('*i.txt')  # susirenkam namu ukiu .txt
f_list_u2 = glob.glob('*i.xls')  # susirenkam namu ukiu .xls
for i in f_list_u:
    df = pd.read_csv(i)
    dctu[int(i[4:8])] = df
for i in f_list_u2:
    df = pd.read_excel(i)
    dctu[int(i[4:8])] = df

f_list_a = glob.glob('*s.txt')  # susirenkam asmenu .txt
f_list_a2 = glob.glob('*s.xls')  # susirenkam asmenu .xls
for i in f_list_a:
    df = pd.read_csv(i)
    dcta[int(i[4:8])] = df
for i in f_list_a2:
    df = pd.read_excel(i)
    dcta[int(i[4:8])] = df
    
print(dctu.keys())
print(dcta.keys())
print(type(dcta[2019]))

r = list(dcta.keys())  # exportuojames visus failus i csv, kad greiciau dirbtumem.
for i in r:
    dcta[i].to_csv(str(i) + ' asmenys.csv', index=False)
    dctu[i].to_csv(str(i) + ' namu ukiai.csv', index=False)
    print(i)
