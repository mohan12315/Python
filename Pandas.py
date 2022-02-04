#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


sports1 = pd.Series([1,2,3,4],index=["cricket","football","basketball","golf"])
sports1


# In[3]:


sports1["basketball"]


# In[4]:


sports2 = pd.Series([11,13,5,6],index=["cricket","football","baseball","golf"])
sports2


# In[5]:


sports1+sports2


# In[7]:


df1 = pd.DataFrame(np.random.rand(8,5),index='A B C D E F G H'.split(),columns = 'score1 score2 score3 score4 score5'.split())
df1


# In[8]:


df1[['score1','score2','score3']]


# In[9]:


df1['score1']


# In[10]:


df1["score6"] = df1['score1'] + df1['score2']
df1


# In[12]:


df1.drop('E')
df1


# In[13]:


df1.drop("score1",axis=1)


# In[14]:


df1.drop('A',axis=0)


# In[15]:


df2 = {'ID':[10,11,12,13,14],'Name':['mohan','ravi','aman','dara','venky'],'Profit':[30,15,20,17,25]}
df=pd.DataFrame(df2)
df


# In[16]:


df.drop('ID',axis=1)


# In[17]:


df.drop(3)


# In[18]:


df['Name']


# In[20]:


df[['Name','ID']]


# In[23]:


df = pd.read_csv("DimCity.csv")


# In[ ]:


df.head()


# In[ ]:


df.tail()

