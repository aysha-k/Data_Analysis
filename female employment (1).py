#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df=pd.read_csv(r"C:\Users\pc\Desktop\MLR2.csv")
df


# In[6]:


df.tail()


# In[7]:


df.head()


# In[10]:


df.info()
# df.isna().sum()


# In[28]:


df.set_index('Year', inplace=True)


# # Trends in Female Employment Rates

# In[38]:


plt.plot(df.index, df['PerFemEmploy'], label='Female Employment Rate')
plt.title('Trends in Female Employment Rates')
plt.xlabel('Year')
plt.ylabel('Percentage / Rate')
plt.xticks(df.index, rotation=45)
plt.tight_layout()
plt.show()


# Mean Percentage of Female Employment

# In[42]:


sector_data = df[['Agriculture', 'Industry', 'Services']]
mean = sector_data.mean()
mean


# # Relationship Between Female Employment in Different Sectors

# In[36]:


sns.pairplot(df[['Agriculture', 'Industry', 'Services']])
plt.show()


# Male-to-Female Ratios in Employment Over Time

# In[48]:


plt.bar(df.index, df['Ratio_MaletoFemale'], color='b', label='Male-to-Female Ratio')
plt.xlabel('Year')
plt.ylabel('Male-to-Female Ratio')
plt.xticks(rotation=45)
plt.show()


# # Distribution of Female Employment Between Wage and Non-Wage Sectors

# In[51]:


percentage_wage = df['Wage&Salaried'].mean()
percentage_non_wage = 100 - percentage_wage
labels = ['Wage Employment', 'Non-Wage Employment']
sizes = [percentage_wage, percentage_non_wage]
colors = ['lightblue', 'lightcoral']
plt.figure(figsize=(8, 6))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.show()


# # Correlation Heatmap of Female Employment Indicators Across Years

# In[52]:


sns.heatmap(df.corr(),annot=True,linewidth=4)


# In[ ]:





# In[ ]:




