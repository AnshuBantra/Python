# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 13:13:52 2023

Kaggle Datasets

@author: Anshu Bantra
"""

# ! pip install opendatasets

# import opendatasets as od

# od.download(r'https://www.kaggle.com/datasets/amaanansari09/most-streamed-songs-all-time/Streams.csv')

# od.download(
#     "https://www.kaggle.com/datasets/muratkokludataset/acoustic-extinguisher-fire-dataset")

#%%
import os

print(os.getcwd())

#%%

import pandas as pd
df = pd.read_csv(r'./most-streamed-songs-all-time/Streams.csv')

#%%
print(df.head())

#%%

word = 'Python'
for char in word:
    print(char)
    
    
    
    
    
    