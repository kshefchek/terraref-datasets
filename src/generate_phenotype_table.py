#!/usr/bin/env python
# coding: utf-8

# ### Phenotype Table for Initial Set of Training Data

# In[1]:


import datetime
import pandas as pd
import numpy as np


# #### Import dataset downloaded from betydb in R

# In[2]:


df_0 = pd.read_csv('../data/raw/mac_season_4.csv')
df_0.head()


# In[3]:


df_0.columns


# In[4]:


df_1 = df_0.drop(labels=['Unnamed: 0', 'checked', 'citation_id', 'city', 'scientificname', 'commonname', 'genus',
                        'species_id', 'author', 'citation_year', 'trait_description', 'units', 'n', 'statname',
                        'stat', 'access_level', 'view_url', 'edit_url'], axis=1)

df_1.head()


# In[5]:


timestamp = datetime.datetime.now().replace(microsecond=0).isoformat()
output_filename = f'pheno-table_{timestamp}.csv'.replace(':', '')
df_1.to_csv(f'../data/processed/{output_filename}', index=False)


# In[ ]:




