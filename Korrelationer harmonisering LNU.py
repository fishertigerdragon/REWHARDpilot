# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 07:15:41 2019

@author: brafo
"""

import os
import pandas as pd
import numpy as np

os.chdir('C:/Users/brafo/OneDrive/Skrivbord/Python')   
#ändrar min 'current working directory'
print(os.getcwd())   
#visar min working directory

# Läser in filen från Martin
data = pd.read_excel('exempel lnu.xlsx')

data = data.drop(['Unnamed: 0'], axis = 1)

data.rename(columns={'z1': 'Lopnr', 'z18': 'SSYK'}, inplace=True)

data.replace(regex=True, inplace=True, to_replace=r'\D', value=r'')

data['z626'] = data['z626'].astype(str).str[:1]
data['z626'] = data['z626'].replace('n', np.nan)

data = data.apply(pd.to_numeric)

data.SSYK[data.SSYK > 999] = data.SSYK[data.SSYK > 999]/100

data.SSYK[data.SSYK > 99] = data.SSYK[data.SSYK > 99]/10

data['SSYK'] = data['SSYK'].apply(np.floor)

data = data[['Lopnr', 'SSYK', 'z670', 'z671', 'z672', 'z673', 'z674', 'z680', 'z681',  
           'z682','z616', 'z624', 'z626', 'z647', 'z651', 'z652', 'z653', 'z654',
           'z655', 'z656', 'z625', 'z621', 'z622']]

data.iloc[:, 2:20] = data.iloc[:, 2:20].replace(9, np.nan)
data.z625 = data.z625.replace(99, np.nan)
data.iloc[:, 21:] = data.iloc[:, 21:].replace(9999, np.nan)

data.z680 = data.z680.replace(8, np.nan) 
data.z681 = data.z681.replace(8, np.nan)

data.loc[data.z624==2, ['z625']] = 0

data.z624 = 3 - data.z624
data.z647 = 3 - data.z647
data.z651 = 3 - data.z651
data.z652 = 3 - data.z652
data.z670 = 3 - data.z670
data.z671 = 3 - data.z671
data.z672 = 3 - data.z672

data.z653 = 6 - data.z653
data.z654 = 6 - data.z654
data.z655 = 6 - data.z655
data.z656 = 6 - data.z656
data.z680 = 6 - data.z680
data.z681 = 6 - data.z681
data.z682 = 6 - data.z682

data = data.drop('Lopnr', axis = 1)

data2 = data.groupby('SSYK').mean()

# Ändrar namn på kolumnerna 
data2.columns = ['z670_mean', 'z671_mean', 'z672_mean', 
                    'z673_mean', 'z674_mean', 'z680_mean', 
                    'z681_mean', 'z682_mean', 'z616_mean',
                    'z624_mean', 'z626_mean', 'z647_mean',
                    'z651_mean', 'z652_mean', 'z653_mean', 
                    'z654_mean', 'z655_mean', 
                    'z656_mean', 'z625_mean', 'z621_mean', 
                    'z622_mean']

# Merge data1 och data2 med SSYK som nyckel
data3 = pd.merge(data, data2, left_on='SSYK', right_index=True)

# Återställ index till default och drop indexkolumnen
data3 = data3.reset_index(drop=True)

data3['z656'].corr(data3['z656_mean'])


