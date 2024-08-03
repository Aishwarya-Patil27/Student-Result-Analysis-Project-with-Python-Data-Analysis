#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# pip install numpy
# pip install pandas
# pip install matplotlib
# pip install seaborn


# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[9]:


df = pd.read_csv(r'C:\Users\aishw\Documents\Prep\Projects\Python project for data analaysis (student)\student_scores.csv')
print(df.head())


# In[10]:


df.describe() 


# In[28]:


df.info()


# In[12]:


df.isnull().sum()


# # drop unamed column

# In[27]:


df.head()


# In[26]:


df = df.drop("Unnamed: 0", axis=1)
print(df.head())


# # change weekly study hours columns

# In[29]:


df["WklyStudyHours"] = df["WklyStudyHours"].str.replace ("5-Oct","5-10")
df.head()


# # gender distribution

# In[58]:


plt.figure(figsize=(5,5))
ax = sns.countplot(data = df, x ="Gender")
ax.bar_label(ax.containers[0])
plt.title("Gender Distributuion")
plt.show()


# # from the above chart we have analysed that :
# #the number of females in the data is more than that of males

# In[38]:


gb = df.groupby("ParentEduc").agg({"MathScore" : 'mean',"ReadingScore":"mean","WritingScore":"mean"})
print(gb)


# In[43]:


plt.figure(figsize=(4,4))
sns.heatmap(gb,annot = True)
plt.title("Relationship between Parent's Education and Stduent's score")
plt.show()


# In[ ]:


#from the above chart we have concluded that the education of the parents have a good impact on their studies


# In[41]:


gb1 = df.groupby("ParentMaritalStatus").agg({"MathScore" : 'mean',"ReadingScore":"mean","WritingScore":"mean"})
print(gb1)


# In[45]:


plt.figure(figsize=(4,4))
sns.heatmap(gb1,annot = True)
plt.title("Relationship between Parent's Marital Status and Stduent's score")
plt.show()


# In[ ]:


#from the above chart we have concluded that there is no impact on the students score due to their parent's marital status


# In[46]:


sns.boxplot(data=df,x = "MathScore")
plt.show()


# In[47]:


sns.boxplot(data=df,x = "ReadingScore")
plt.show()


# In[48]:


sns.boxplot(data=df,x = "WritingScore")
plt.show()


# In[49]:


print(df["EthnicGroup"].unique())


# # Distribution of Ethnic Groups

# In[57]:


groupA = df.loc[(df['EthnicGroup'] == "group A")].count()
groupB = df.loc[(df['EthnicGroup'] == "group B")].count()
groupC = df.loc[(df['EthnicGroup'] == "group C")].count()
groupD = df.loc[(df['EthnicGroup'] == "group D")].count()
groupE = df.loc[(df['EthnicGroup'] == "group E")].count()
l = ["group A","group B","group C","group D","group E"]
mlist = [groupA["EthnicGroup"],groupB["EthnicGroup"],groupC["EthnicGroup"],groupD["EthnicGroup"],groupE["EthnicGroup"]]
plt.pie(mlist, labels = l,autopct = "%1.2f%%")
print(mlist)
plt.title("Distribution of Ethnic Groups")
plt.show()


# In[55]:


ax = sns.countplot(data = df, x = "EthnicGroup")
ax.bar_label(ax.containers[0])


# In[ ]:




