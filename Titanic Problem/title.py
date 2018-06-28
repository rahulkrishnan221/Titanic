
# coding: utf-8

# In[104]:


import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
df=pd.read_csv("train.csv")


# In[105]:


t=df['Name']


# In[106]:


titles = set()
for name in df['Name']:
    titles.add(name.split(',')[1].split('.')[0].strip())


# In[107]:


print(titles)


# In[108]:


Title_Dictionary = {
    "Capt": "Officer",
    "Col": "Officer",
    "Major": "Officer",
    "Jonkheer": "Other",
    "Don": "Other",
    "Sir" : "Other",
    "Dr": "Officer",
    "Rev": "Other",
    "the Countess":"Other",
    "Mme": "Mirs",
    "Mlle": "Miss",
    "Ms": "Mirs",
    "Mr" : "Mr",
    "Mrs" : "Mirs",
    "Miss" : "Miss",
    "Master" : "Master",
    "Lady" : "Other"
}


# In[109]:


df['Title']=df['Name'].map(lambda name:name.split(',')[1].split('.')[0].strip())


# In[110]:


df


# In[116]:


df['Title']=df.Title.map(Title_Dictionary)


# In[119]:


df2=df1[df1['Title'].str.contains("Mrs")]


# In[139]:



# In[82]:





# In[83]:


#df3.Age.fillna(35.653543)


# In[117]:


df3=df[['Age','Title']]
print(df3)


# In[118]:





# In[40]:





# In[38]:





# In[51]:




