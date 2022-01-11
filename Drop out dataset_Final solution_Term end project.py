#!/usr/bin/env python
# coding: utf-8

# In[105]:


import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[106]:


df=pd.read_csv("C:\\Users\\aashi\\Documents\\dropout.csv.csv")


# In[107]:


df.head()
#this dataset focuses upon the dropout rate across all states in India based upon the schooling stages,
#more specefically for boys and girls seperately and the total as well.


# In[108]:


df.tail()


# In[109]:


df.isnull()


# In[110]:


df.describe()


# In[111]:


df['State_UT'].unique()


# In[112]:


df.dtypes


# In[113]:


df = df[df['State_UT']=='Goa']


# In[114]:


df.head()


# In[116]:


df.info()


# In[117]:


df = df[df['State_UT']=='Goa']


# In[118]:


df.head()


# In[119]:


df=pd.read_csv("C:\\Users\\aashi\\Documents\\dropout.csv.csv")


# In[120]:


df = df[df['State_UT']=='Goa']


# In[121]:


df.head()


# In[122]:


df=df.replace('NR',0)
df=df.replace('@',0)


# In[123]:


df.head()


# In[163]:


primary_boys=df['Primary_Total'].values.astype(np.float32)


# In[125]:


df.dtypes


# In[127]:


df=pd.read_csv("C:\\Users\\aashi\\Documents\\dropout.csv.csv")


# In[128]:


df.head()


# In[164]:


df=df.replace('NR',0)
df=df.replace('@',0)
df=df.replace('Uppe_r_Primary',0)
#replacing the null values with 0 to make the whole data set into numeric values


# In[130]:


df.head()


# In[131]:


df.dtypes


# In[132]:


df["Primary_Boys"] = df["Primary_Boys"].astype(float).astype(int)
df["Primary_Girls"] = df["Primary_Girls"].astype(float).astype(int)
df["Primary_Total"] = df["Primary_Total"].astype(float).astype(int)
df["Upper Primary_Boys"] = df["Upper Primary_Boys"].astype(float).astype(int)
df["Upper Primary_Girls"] = df["Upper Primary_Girls"].astype(float).astype(int)
df["Upper Primary_Total"] = df["Upper Primary_Total"].astype(float).astype(int)
df["Secondary _Boys"] = df["Secondary _Boys"].astype(float).astype(int)
df["Secondary _Girls"] = df["Secondary _Girls"].astype(float).astype(int)
df["Secondary _Total"] = df["Secondary _Total"].astype(float).astype(int)
df["HrSecondary_Boys"] = df["HrSecondary_Boys"].astype(float).astype(int)
df["HrSecondary_Girls"] = df["HrSecondary_Girls"].astype(float).astype(int)
df["HrSecondary_Total"] = df["HrSecondary_Total"].astype(float).astype(int)

#converting float values to numeric for making the graphs


# In[133]:


df.dtypes


# In[166]:


_=sns.barplot(x='Primary_Boys', y='Primary_Girls', data=df)
#this represents that on an average, as many girls dropout as many do boys at Primary School level


# In[134]:


df.shape


# In[137]:


sns.pairplot(df)


# In[175]:


import altair as alt


# In[178]:


alt.Chart(df).mark_circle().encode(
x='Primary_Boys:Q',
y='Primary_Total:Q',
color='State_UT:N',
).interactive()
#there is a positive correlation between the two


# In[142]:


x=df


# In[143]:


df.iloc[0:3]
#a function to see individual state data


# In[148]:


sns.boxplot(x='year', y='Upper Primary_Total', data=df)
#this represents year wise data w.r.t each school level
#here, the median value for all three years falls between 2.5-5.


# In[149]:


sns.boxplot(x='year', y='Primary_Total', data=df)


# In[150]:


sns.boxplot(x='year', y='Secondary _Total', data=df)


# In[151]:


sns.boxplot(x='year', y='HrSecondary_Total', data=df)


# In[152]:


dropout= pd.crosstab(df.year, df.State_UT)


# In[153]:


dropout
#an year wise tabulation w.r.t each state


# In[154]:


sns.heatmap(dropout)
#heat map of the same which represents higher drop out rates in most states and lower in Tripura in 2012-13 which increased in 2014-15


# In[179]:


df['Primary_Total'].mean()
#mean drop out rate of Primary school stage in total


# In[182]:


df['HrSecondary_Total'].mean()
#mean drop out rate of Higher Secondary school stage in total


# In[183]:


df['Secondary _Total'].mean()
#mean drop out rate of Secondary school stage in total
#the highest so far. Most children drop out from Secondary school.


# In[162]:


sns.set_style('whitegrid')
_=sns.lineplot(data=df, x='year', y= 'HrSecondary_Total', estimator= np.mean, hue='State_UT')
#This represents that in 2014-15, children in Higher secondary in state of Chhattisgrah dropped out the most and the numbers declined for Odisha.

