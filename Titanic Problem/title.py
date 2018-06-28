
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




# In[108]:


Title_Dictionary = {
    "Mr" : "Mr",
    "Mrs" : "Mirs",
    "Miss" : "Miss",
    "Master" : "Master",
}


# In[109]:


df['Title']=df['Name'].map(lambda name:name.split(',')[1].split('.')[0].strip())


# In[110]:

check_copy=df[['Age','Title']].copy()
check_copy=check_copy.dropna()
c=0
ct=0
for i,j in check_copy.iterrows():
    if(j["Title"]=="Miss"):
        c=c+j["Age"]
        ct+=1
        
print(c/ct)
df["Age"]=df["Age"].fillna(1000)
lt=df["Title"].values.tolist()
la=df["Age"].values.tolist()
print(len(lt),len(la))
fl=[]
for i,j in zip(la,lt):
    if i==1000:
        if j=="Master":
            fl.append(4.65)
        elif j=="Mrs":
            fl.append(35.89)
        elif j=="Miss":
            fl.append(21.77)
        elif j=="Mr":
            fl.append(32.3)
    else:
        fl.append(i)
df["Age_new"]=pd.DataFrame({'col':fl})
print(df)
# In[116]:


#df['Title']=df.Title.map(Title_Dictionary)


# In[119]:


df2=df[df['Title'].str.contains("Mrs")]


# In[139]:



# In[82]:





# In[83]:


#df3.Age.fillna(35.653543)


# In[117]:


df3=df[['Age','Title']]


# In[118]:





# In[40]:





# In[38]:





# In[51]:




