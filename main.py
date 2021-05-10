# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 20:21:01 2021

@author: Home-PC
"""

#  #baigiamasis darbas.
#  Parašyti skriptą, vizualizuojantį norimus duomenis apie namų ūkių biudžetus, būsto tipus, etc ...

import matplotlib.pyplot as plt
import pandas as pd
import glob
import numpy as np
import os


dctu = {}   # žodynas namų ukių duomenims (metai : dataframe)
dcta = {}   # žodynas asmenų duomenims (metai : dataframe)

cwd = os.getcwd()  # getting current folder path
nf = 'output_csv\\'  # new folder name
path = os.path.join(cwd, nf)

f_list_u = glob.glob(str(path + '*i.csv')) #susirenkam namu ukiu .csv
for i in f_list_u:
    df = pd.read_csv(i)
    dctu[int(i[-19:-15])] = df

f_list_a = glob.glob(str(path +'*s.csv')) #susirenkam asmenu .csv
for i in f_list_a:
    df = pd.read_csv(i)
    dcta[int(i[-16:-12])] = df
    
years = list(dcta.keys()) #sukurtas sąrašas nagrinėjamų metų (objektai int tipo)

# padarom nauja dictionary su joinintom lentelem per namų ūkio ID. (metai : dataframe)
dctall = {}
for y in years:
    dctall[y] = pd.merge(dctu[y], dcta[y], on = 'HB030') # padarom left join dviems lentelems (ir praeinam per metus)

avg_inc_1 = []  #average income in Vilnius
avg_inc_2 = []  #average income in Kaunas
avg_inc_3 = []  #average income in Klaipeda
avg_inc_4 = []  #average income in Šiauliai
avg_inc_5 = []  #average income in Panevėžys
avg_inc_6 = []  #average income in Kiti miestai
avg_inc_7 = []  #average income in Kaimai

income_sl = {'Vilnius':avg_inc_1, 'Kaunas':avg_inc_2, 'Klaipeda':avg_inc_3, 'Šiauliai':avg_inc_4,'Panevėžys':avg_inc_5, 'Kiti miestai':avg_inc_6, 'Kaimai':avg_inc_7} #SL - sluoksniai per kuriuos kerpu duomenis
for y in years:
    income = dctall[y].groupby(['SL_y'])['HY010'].mean() #miestuose ir kaime Namų ūkio pajamos
    # key_list = income.keys().tolist()
    inc = income.to_dict()    
    for key, value in inc.items():
        if key == 1:            
            if y <2015: 
                avg_inc_1.append(value/3.4528)  
            else:
                avg_inc_1.append(value)
        if key == 2:
            if y <2015:
                avg_inc_2.append(value/3.4528)     
            else:
                avg_inc_2.append(value)
        if key == 3:
            if y <2015:
                avg_inc_3.append(value/3.4528)     
            else:
                avg_inc_3.append(value)
        if key == 4:            
            if y <2015: 
                avg_inc_4.append(value/3.4528)  
            else:
                avg_inc_4.append(value)
        if key == 5:
            if y <2015:
                avg_inc_5.append(value/3.4528)     
            else:
                avg_inc_5.append(value)
        if key == 6:
            if y <2015:
                avg_inc_6.append(value/3.4528)     
            else:
                avg_inc_6.append(value)                
        if key == 7:
            if y <2015:
                avg_inc_7.append(value/3.4528)     
            else:
                avg_inc_7.append(value)                   

# o čia labai gudriai su mažai kodo - atspausdinam grafikus:
fig, ((ax, ax2),(ax3, ax4)) = plt.subplots(2,2)
for key, value in income_sl.items():
       ax.plot(years, value, label = key, linewidth=2)
ax.legend()       
ax.set_title('Metinės namų ūkių pajamos miestuose ir kaime')
ax.set_ylabel('Bendrosios namų ūkio pajamos per metus, EUR')


fc = 'whitesmoke'
ax.set_facecolor(fc)
ax2.set_facecolor(fc)
ax3.set_facecolor(fc)
fig.canvas.set_window_title('Metinės pajamos')
fig. tight_layout()


# ============== paskaičiuoti iš dviejų lentelių iš kelių susideda namų ūkis. ir kokios metines pajamos vienam žmogui namų ūkyje
for y in years:
    a = dctall[y].groupby(['HB030'])['PB030'].count()
    a.name = 'num_pers'
    dctall[y] = pd.merge(dctall[y], a, on = 'HB030') # pridedam column kiek zmoniu gyvena vienam namų ūkyje
    dctall[y]['inc_pers'] = dctall[y]['HY010'] / dctall[y]['num_pers'] # income per person 1 namų ūkyje
    
# print(dctall[2012].head(10)[['HB030', 'PB030', 'HY010', 'num_pers', 'inc_pers']])

avg_incp_1 = []  #average income in Vilnius
avg_incp_2 = []  #average income in Kaunas
avg_incp_3 = []  #average income in Klaipeda
avg_incp_4 = []  #average income in Šiauliai
avg_incp_5 = []  #average income in Panevėžys
avg_incp_6 = []  #average income in Kiti miestai
avg_incp_7 = []  #average income in Kaimai

incomep_sl = {'Vilnius':avg_incp_1, 'Kaunas':avg_incp_2, 'Klaipeda':avg_incp_3, 'Šiauliai':avg_incp_4,'Panevėžys':avg_incp_5, 'Kiti miestai':avg_incp_6, 'Kaimai':avg_incp_7} #SL - sluoksniai per kuriuos kerpu duomenis
for y in years:
    incomep = dctall[y].groupby(['SL_y'])['inc_pers'].mean() #miestuose ir kaime Namų ūkio pajamos
    inc = incomep.to_dict()    
    for key, value in inc.items():
        if key == 1:            
            if y <2015: 
                avg_incp_1.append(value/3.4528)  
            else:
                avg_incp_1.append(value)
        if key == 2:
            if y <2015:
                avg_incp_2.append(value/3.4528)     
            else:
                avg_incp_2.append(value)
        if key == 3:
            if y <2015:
                avg_incp_3.append(value/3.4528)     
            else:
                avg_incp_3.append(value)
        if key == 4:            
            if y <2015: 
                avg_incp_4.append(value/3.4528)  
            else:
                avg_incp_4.append(value)
        if key == 5:
            if y <2015:
                avg_incp_5.append(value/3.4528)     
            else:
                avg_incp_5.append(value)
        if key == 6:
            if y <2015:
                avg_incp_6.append(value/3.4528)     
            else:
                avg_incp_6.append(value)                
        if key == 7:
            if y <2015:
                avg_incp_7.append(value/3.4528)     
            else:
                avg_incp_7.append(value)                  

for key, value in incomep_sl.items():
       ax2.plot(years, value, label = key, linewidth=2)

ax2.legend()
ax2.set_title('Metinės namų ūkių pajamos vienam asmeniui miestuose ir kaime')
ax2.set_ylabel('Metinės namų ūkių pajamos vienam asmeniui, EUR')

# pasidarom issilavinimo kategorijas:
dctall[2019].loc[dctall[2019]['PE040'] == 0, 'edu_c'] = 0
dctall[2019].loc[dctall[2019]['PE040'] == 100, 'edu_c'] = 100
dctall[2019].loc[dctall[2019]['PE040'] == 200, 'edu_c'] = 200
dctall[2019].loc[(dctall[2019]['PE040'] >= 300) & (dctall[2019]['PE040'] < 400), 'edu_c'] = 300
dctall[2019].loc[dctall[2019]['PE040'] == 400, 'edu_c'] = 400
dctall[2019].loc[dctall[2019]['PE040'] == 450, 'edu_c'] = 400
dctall[2019].loc[dctall[2019]['PE040'] == 600, 'edu_c'] = 600
dctall[2019].loc[dctall[2019]['PE040'] == 700, 'edu_c'] = 700
dctall[2019].loc[dctall[2019]['PE040'] == 800, 'edu_c'] = 800
# print(dctall[2019].head(50))


df_miest_19 = dctall[2019][dctall[2019]['M_K_x'] == 1] #dataframe'as vien tik miesto
df_kaim_19 =  dctall[2019][dctall[2019]['M_K_x'] == 2] #dataframe'as vien tik kaimo
df_miest_10 = dctall[2010][dctall[2010]['M_K_x'] == 1] #dataframe'as vien tik miesto
df_kaim_10 =  dctall[2010][dctall[2010]['M_K_x'] == 2] #dataframe'as vien tik kaimo

tul_m_19 = df_miest_19.groupby(['HH091', 'edu_c'])['HB030'].count().unstack(fill_value=0).stack() #grupuojam TULIKAI, išsilavinimas, skaičiuojam namų ūkius, MIESTE _19 metais
tul_k_19 = df_kaim_19.groupby(['HH091', 'edu_c'])['HB030'].count().unstack(fill_value=0).stack() #grupuojam TULIKAI, išsilavinimas, skaičiuojam namų ūkius, KAIME _19 metais

tul_m_10 = df_miest_10.groupby(['HH091', 'PE040'])['HB030'].count().unstack(fill_value=0).stack()
tul_k_10 = df_kaim_10.groupby(['HH091', 'PE040'])['HB030'].count().unstack(fill_value=0).stack()

tul_mdct_19 = tul_m_19.to_dict()
keys_values = tul_mdct_19.items()
tul_m_edu_19 = {str(key): int(value) for key, value in keys_values}

tul_kdct_19 = tul_k_19.to_dict()
keys_values = tul_kdct_19.items()
tul_k_edu_19 = {str(key): int(value) for key, value in keys_values}

tul_m_edu1_19 = []
tul_m_edu2_19 = []
tul_m_edu3_19 = []
tul_k_edu1_19 = []
tul_k_edu2_19 = []
tul_k_edu3_19 = []
for key, value in tul_m_edu_19.items():
    if '1,' in key:
        tul_m_edu1_19.append(value)
    if '2,' in key:
        tul_m_edu2_19.append(value)
    if '3,' in key:
        tul_m_edu3_19.append(value)
        
for key, value in tul_k_edu_19.items():
    if '1,' in key:
        tul_k_edu1_19.append(value)
    if '2,' in key:
        tul_k_edu2_19.append(value)
    if '3,' in key:
        tul_k_edu3_19.append(value)

tul_mdct_10 = tul_m_10.to_dict()
keys_values = tul_mdct_10.items()
tul_m_edu_10 = {str(key): int(value) for key, value in keys_values}

tul_kdct_10 = tul_k_10.to_dict()
keys_values = tul_kdct_10.items()
tul_k_edu_10 = {str(key): int(value) for key, value in keys_values}

tul_m_edu1_10 = []
tul_m_edu2_10 = []
tul_m_edu3_10 = []
tul_k_edu1_10 = []
tul_k_edu2_10 = []
tul_k_edu3_10 = []
for key, value in tul_m_edu_10.items():
    if '1,' in key:
        tul_m_edu1_10.append(value)
    if '2,' in key:
        tul_m_edu2_10.append(value)
    if '3,' in key:
        tul_m_edu3_10.append(value)
        
for key, value in tul_k_edu_10.items():
    if '1,' in key:
        tul_k_edu1_10.append(value)
    if '2,' in key:
        tul_k_edu2_10.append(value)
    if '3,' in key:
        tul_k_edu3_10.append(value)

tul_edux = ['Ikimokyklinis','Pradinis','Pagrindinis','Vidurinis','Profesinis','Bakalauras','Magistras','Daktaras']
tul_edux2 = ['Ikimokyklinis','Pradinis','Pagrindinis','Vidurinis','Profesinis','Bakalauras\nMagistras','Daktaras']

fig, ((bx1,bx3),(bx2,bx4))=plt.subplots(2,2)
fig.canvas.set_window_title('Tualetų su nutekamuoju vandeniu skaičius pagal išsilavinimą')
width = 0.5 
x = np.arange(len(tul_edux))
rects1 = bx1.bar(x , tul_m_edu1_19, width, label = 'Naudojasi tik vienas namų ūkis')
rects2 = bx1.bar(x + width/3, tul_m_edu2_19, width, label = 'Naudojasi keli namų ūkiai')
rects3 = bx1.bar(x - width/3, tul_m_edu3_19, width, label = 'Būste nėra tualeto su nutekamuoju vandeniu')
bx1.set_title('2019 metais mieste')
bx1.set_xticks(x)
bx1.set_xticklabels(tul_edux, rotation = 45)
bx1.legend()
bx1.set_ylabel('Būstų skaičius')
bx1.set_xlabel('Išsilavinimas')
bx1.set_facecolor(fc)
bx1.tick_params(axis="x",direction="in", pad=-55)

rects1 = bx2.bar(x , tul_k_edu1_19, width, label = 'Naudojasi tik vienas namų ūkis')
rects2 = bx2.bar(x + width/3, tul_k_edu2_19, width, label = 'Naudojasi keli namų ūkiai')
rects3 = bx2.bar(x - width/3, tul_k_edu3_19, width, label = 'Būste nėra tualeto su nutekamuoju vandeniu')
bx2.set_title('2019 metais kaime')
bx2.set_xticks(x)
bx2.set_xticklabels(tul_edux, rotation = 45)
bx2.legend()
bx2.set_ylabel('Būstų skaičius')
bx2.set_xlabel('Išsilavinimas')
bx2.set_facecolor(fc)
bx2.tick_params(axis="x",direction="in", pad=-55)

x2 = np.arange(len(tul_edux2))
rects1 = bx3.bar(x2 , tul_m_edu1_10, width, label='Naudojasi tik vienas namų ūkis')
rects2 = bx3.bar(x2 + width/3, tul_m_edu2_10, width, label='Naudojasi keli namų ūkiai')
rects3 = bx3.bar(x2 - width/3, tul_m_edu3_10, width, label='Būste nėra tualeto su nutekamuoju vandeniu')
bx3.set_title('2010 metais mieste')
bx3.set_xticks(x2)
bx3.set_xticklabels(tul_edux2, rotation = 45)
bx3.legend()
bx3.set_ylabel('Būstų skaičius')
bx3.set_xlabel('Išsilavinimas')
bx3.set_facecolor(fc)
bx3.tick_params(axis="x",direction="in", pad=-55)

rects1 = bx4.bar(x2 , tul_k_edu1_10, width, label = 'Naudojasi tik vienas namų ūkis')
rects2 = bx4.bar(x2 + width/3, tul_k_edu2_10, width, label = 'Naudojasi keli namų ūkiai')
rects3 = bx4.bar(x2 - width/3, tul_k_edu3_10, width, label = 'Būste nėra tualeto su nutekamuoju vandeniu')
bx4.set_title('2010 metais kaime')
bx4.set_xticks(x2)
bx4.set_xticklabels(tul_edux2, rotation = 45)
bx4.legend()
bx4.set_ylabel('Būstų skaičius')
bx4.set_xlabel('Išsilavinimas')
bx4.set_facecolor(fc)
bx4.tick_params(axis="x",direction="in", pad=-55)

fig.suptitle("Tualetų su nutekamuoju vandeniu skaičius pagal išsilavinimą", fontsize = 14)
# fig. tight_layout()


# =============== busto islaikymo ir metiniu pajamu santykis miestuose ir kaime
# imam HY010 - Bendrosios namų ūkio pajamos ir HH070 - komunaliniai per mėn - bet imsim per metus

for y in years:
    dctall[y]['K/P'] = ((dctall[y]['HH070']* 12) / dctall[y]['HY010']) * 100 # komunalinės išlaidos procentais nuo pajamų
       
avg_kp_1 = []  #average utility cost in Vilnius
avg_kp_2 = []  #average utility cost in Kaunas
avg_kp_3 = []  #average utility cost in Klaipeda
avg_kp_4 = []  #average utility cost in Šiauliai
avg_kp_5 = []  #average utility cost in Panevėžys
avg_kp_6 = []  #average utility cost in Kiti miestai
avg_kp_7 = []  #average utility cost in Kaimai

kp_sl = {'Vilnius':avg_kp_1, 'Kaunas':avg_kp_2, 'Klaipeda':avg_kp_3, 'Šiauliai':avg_kp_4,'Panevėžys':avg_kp_5, 'Kiti miestai':avg_kp_6, 'Kaimai':avg_kp_7} #SL - sluoksniai per kuriuos kerpu duomenis
for y in years:
    df_kom = dctall[y][dctall[y]['HY010'] > 0] #dataframe'as kur pajamos daugiau už 0 
    kp_df = df_kom.groupby(['SL_y'])['K/P'].mean() #miestuose ir kaime komunalinės išlaidos procentai nuo pajamų
    kp_dict = kp_df.to_dict()    
    for key, value in kp_dict.items():
        if key == 1:            
            avg_kp_1.append(value)
        if key == 2:
            avg_kp_2.append(value)
        if key == 3:
            avg_kp_3.append(value)
        if key == 4:            
            avg_kp_4.append(value)
        if key == 5:
            avg_kp_5.append(value)
        if key == 6:
            avg_kp_6.append(value)                
        if key == 7:
            avg_kp_7.append(value)                  

for key, value in kp_sl.items():
    ax3.plot(years, value, label = key, linewidth=2)
ax3.legend()
ax3.set_title('Komunalinės išlaidos miestuose ir kaime')
ax3.set_ylabel('Komunalinės išlaidos, % nuo pajamų')


# =============== metinės namų ūkio pajamos (vienam žmogui?) pagal PL040 - užimtumo statusas

       
avg_sal_1 = []  #Savarankiškai dirbantis ir turintis samdomų darbuotojų
avg_sal_2 = []  #Savarankiškai dirbantis be samdomų darbuotojų
avg_sal_3 = []  #Samdomas darbuotojas
avg_sal_4 = []  #Dirbantis be atlyginimo šeimos versle, asmeniniame žemės ukyje 

sal_sl = {'Savarankiškai dirbantis ir turintis samdomų darbuotojų':avg_sal_1, 'Savarankiškai dirbantis be samdomų darbuotojų':avg_sal_2, 'Samdomas darbuotojas':avg_sal_3, 'Dirbantis be atlyginimo šeimos versle, asmeniniame žemės ukyje':avg_sal_4} #sl - sluoksniai per kuriuos kerpu duomenis
for y in years:
    dctall[y]['sal'] = (dctall[y]['PY010N'] + dctall[y]['PY050N']) # samdomo ir savarankiško darbo pajamos per metus

for y in years:
    sal_df = dctall[y].groupby(['PL040'])['sal'].mean() #metinės pajamos pagal užimtumo statusą
    sal_dict = sal_df.to_dict()    
    for key, value in sal_dict.items():
        if key == 1:
            if y <2015:
                avg_sal_1.append(value/3.4528)
            else:
                avg_sal_1.append(value)
        if key == 2:
            if y <2015: 
                avg_sal_2.append(value/3.4528)
            else:
                avg_sal_2.append(value)
        if key == 3:
            if y <2015: 
                avg_sal_3.append(value/3.4528)
            else:
                avg_sal_3.append(value)
        if key == 4:            
            if y <2015: 
                avg_sal_4.append(value/3.4528)
            else:
                avg_sal_4.append(value)
                

for key, value in sal_sl.items():
    ax4.plot(years, value, label = key, linewidth=2)
ax4.legend()
ax4.set_title('Metinės pajamos, atskaičius mokesčius, pagal užimtumo statusą')
ax4.set_ylabel('Metinės asmens pajamos, EUR')
ax4.set_facecolor(fc)

ax4.set_xticks(years)
ax4.set_xticklabels(years)
ax3.set_xticks(years)
ax3.set_xticklabels(years)
ax2.set_xticks(years)
ax2.set_xticklabels(years)    
ax.set_xticks(years)
ax.set_xticklabels(years)

plt.show()
