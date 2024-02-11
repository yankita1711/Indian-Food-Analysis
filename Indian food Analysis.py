#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import plotly.express as px
from plotly.offline import init_notebook_mode
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from wordcloud import WordCloud,ImageColorGenerator


# In[3]:


pip install wordcloud


# In[2]:


data=pd.read_csv("indian_food.csv")


# In[3]:


data


# In[4]:


data.head()


# In[6]:


data.columns


# In[7]:


data.info()


# In[8]:


data.isnull().any()


# In[9]:


data.isnull().sum()


# In[10]:


data=data.replace(-1,np.nan)
data=data.replace('-1',np.nan)


# In[11]:


data.head()


# In[12]:


data.isnull().sum()


# In[13]:


data.shape


# In[17]:


pie_data=data.diet.value_counts().reset_index()


# In[20]:


pie_data.columns=['diet','count']
fig=px.pie(pie_data,values='count',names='diet',title='Proportion of Vegetarian and Non-vegetarian Dishes',color_discrete_sequence=['green','red'])
fig.show()


# In[ ]:




