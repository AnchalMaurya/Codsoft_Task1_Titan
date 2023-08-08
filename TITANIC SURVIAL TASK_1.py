#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


df=pd.read_csv('Titanic.csv')
df.head(10)


# In[3]:


df.Age.mean()


# In[4]:


df.Age.mode()


# In[5]:


df.Pclass.value_counts


# In[6]:


df.Survived.value_counts


# In[7]:


df.Sex.value_counts


# In[8]:


df.iloc[0]


# In[9]:


df.loc[20:30,['PassengerId','Age']]


# In[10]:


df.info


# In[11]:


len(df[df['Age']<25])


# In[12]:


df_lt_25=df[df['Age']<25]
df.sort_values(['Age'],ascending=False)


# In[13]:


df['Fare'].max()


# In[14]:


df['Fare'].min()


# In[15]:


df['Name'].apply(lambda x:x.startswith('B'))


# In[16]:


df[df['Name'].apply(lambda x:x.startswith('B'))]


# In[17]:


len(df[df['Name'].apply(lambda x:x.startswith('B'))])


# In[18]:


df['Name'][0].startswith('B')


# In[19]:


df['Name'][0]


# In[20]:


df['SW_B']=df['Name'].apply(lambda x:x.startswith('B'))


# In[21]:


df[(df['Age']<25)& (df['Sex']=='male')]


# In[22]:


len(df[(df['Age']<25)& (df['Sex']=='male')])


# In[23]:


df[df['Ticket'].isin(['17463','237736'])]


# In[ ]:




