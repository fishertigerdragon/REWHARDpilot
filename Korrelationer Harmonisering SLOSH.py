# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 09:15:53 2019

@author: mabr4821
"""

import os
import pandas as pd
import numpy as np

os.chdir('C:/Users/brafo/OneDrive/Skrivbord/Python')   
#ändrar min 'current working directory'
print(os.getcwd())   
#visar min working directory

# Läser in filen från Martin
data = pd.read_excel('SLOSH rådata harmonisering.xlsx')

data = data.drop(['tvåställig ssyk'], axis = 1)

data = data[data.r_7 == 2]

data = data.replace(['bortfall', 'kodas ej'], np.nan)

data.iloc[:, :13][data.iloc[:, :13]>4] = np.nan

data = data.apply(pd.to_numeric)

data.ssyk_7[data.ssyk_7 > 999] = data.ssyk_7[data.ssyk_7 > 999]/100

data.ssyk_7[data.ssyk_7 > 99] = data.ssyk_7[data.ssyk_7 > 99]/10

data['ssyk_7'] = data['ssyk_7'].apply(np.floor)

data = data.drop(['r_7', 'lopnr_slosh'], axis = 1)

data.columns = ['Loadtime', 'Interrup', 'Morework', 'Workfast','Workhard', 
                'Workeffo', 'Worktime', 'Workcntr', 'Workskil', 'Workinge',
                'Worklear', 'Workrepe', 'Workhow', 'Workwhat', 'SSYK']

data = data[['SSYK', 'Loadtime', 'Interrup', 'Morework', 'Workfast','Workhard', 
             'Workeffo', 'Worktime', 'Workcntr', 'Workskil', 'Workinge',
             'Worklear', 'Workrepe', 'Workhow', 'Workwhat']]

data.iloc[:, 1:] = 5-data.iloc[:, 1:]

# Tar fram mean för varje variabel med ssyk som nyckel
data2 = data.groupby('SSYK').mean()

# Ändrar namn på kolumnerna 
data2.columns = ['loadtime_mean', 'interrup_mean', 'morework_mean', 
                    'workfast_mean', 'workhard_mean', 'workeffo_mean', 
                    'worktime_mean', 'workcntr_mean', 'workskil_mean',
                    'workinge_mean', 'worklear_mean', 'workrepe_mean',
                    'workhow_mean', 'workwhat_mean']

# Merge data1 och data2 med SSYK som nyckel
data3 = pd.merge(data, data2, left_on='SSYK', right_index=True)

# Återställ index till default och drop indexkolumnen
data3 = data3.reset_index(drop=True)

# Spara ner dataframe till en excelfil
data3.to_excel('hej.xlsx')

#Räkna ut korrelationer mellan individvärden och mean
data3['Loadtime'].corr(data3['loadtime_mean'])

data3['Interrup'].corr(data3['interrup_mean'])

data3['Morework'].corr(data3['morework_mean'])

data3['Workfast'].corr(data3['workfast_mean'])

data3['Workhard'].corr(data3['workhard_mean'])

data3['Workeffo'].corr(data3['workeffo_mean'])

data3['Worktime'].corr(data3['worktime_mean'])

data3['Workcntr'].corr(data3['workcntr_mean'])

data3['Workskil'].corr(data3['workskil_mean'])

data3['Workinge'].corr(data3['workinge_mean'])

data3['Worklear'].corr(data3['worklear_mean'])

data3['Workrepe'].corr(data3['workrepe_mean'])

data3['Workhow'].corr(data3['workhow_mean'])

data3['Workwhat'].corr(data3['workwhat_mean'])

data3.count()