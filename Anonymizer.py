# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 15:04:56 2019

@author: Tripti Santani
"""

#Importing necessary libraries
from faker import Factory
from collections import defaultdict
from faker.generator import random
import pandas as pd

# Importing the dataset
df_GIST_syn_a_aev=pd.read_csv('~/Desktop/Datathon/Trial 1-GIST_syn_a_aev.csv', decimal = ',')

# Displaying top 5 rows to get the overview of the dataset
df_GIST_syn_a_aev.head()

disease=df_GIST_syn_a_aev['SOC_TXT']

faker  = Factory.create()
faker.random.seed(1)

# Anonymizing 'SOC_TXT' column of the Trial 1-GIST_syn_a_aev dataset
for row in range (0, 15075):
    disease_fake  = defaultdict(faker.word)
    df_GIST_syn_a_aev['SOC_TXT'][row]  = disease_fake['name']

df_columns=df_GIST_syn_a_aev.columns

#Anonymizing column names of the Trial 1-GIST_syn_a_aev dataset
df=[]
for row in df_columns:
    df_fake_columns  = defaultdict(faker.word)
    df.append(df_fake_columns['name'])
df_GIST_syn_a_aev.columns=df



