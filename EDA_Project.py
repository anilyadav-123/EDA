#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set(color_codes=True)


# In[4]:


df = pd.read_csv("C:/Talent Battle/Future Focus Internship Batch/DS1_EDA/Dataset/data.csv")
df.head(5)


# In[6]:


df.tail(5)


# In[8]:


df.dtypes


# In[10]:


df = df.drop(['Market Category','Vehicle Style','Engine Fuel Type','Popularity','Number of Doors','Vehicle Size'],axis=1)
df.head(5)


# In[12]:


df = df.rename(columns={"Engine HP":"HP","Engine Cylinders":"Cylinders","Transmission Type":"Transmission","Driven_Wheels":"Drive Mode","highway MPG":"MPG-H","city mpg":"MPG-C","MSRP":"Price"})
df.head(5)


# In[14]:


df.shape


# In[16]:


duplicate_rows_df = df[df.duplicated()]
print("No of Duplicate Rows:",duplicate_rows_df.shape)


# In[18]:


df.count()


# In[20]:


df = df.drop_duplicates()


# In[22]:


df.count()


# In[24]:


print(df.is_null().sum())


# In[26]:


print(df.isnull().sum())


# In[28]:


df=df.dropna()
df.count()


# In[30]:


print(df.isnull().sum())


# In[33]:


sns.boxplot(x=df['HP'])


# In[35]:


df.Make.value_counts().nlargest(40).plot(kind='bar',figsize=(10,5))
plt.title("Number of cars by making production")
plt.ylabel("No. of cars")
plt.xlabel("Make of Cars")


# In[37]:


plt.figure(figsize=(10,5))
data = df.corr()
sns.heatmap(data,cmap="BrBG",annot=True)
data


# In[40]:


fig,axis = plt.subplots(figsize=(10,6))
axis.scatter(df['Cylinders'],df['Price'])
axis.set_xlabel('Cylinders')
axis.set_ylabel('Price')
plt.show()

