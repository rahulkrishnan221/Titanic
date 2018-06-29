import pandas as pd
import csv as csv
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt


df=pd.read_csv("train.csv")



#1
df['Cabin'].fillna('U', inplace=True)
df['Cabin'] = df['Cabin'].apply(lambda x: x[0])
df['Cabin'].unique()

#2
df['Child']=df['Age']
x1=df.where(df['Child']<16)
x1['Child'].fillna(0,inplace=True)
y1=x1.where(x1['Child']<2)
y1['Child'].fillna(1,inplace=True)
df['Child']=y1['Child']



#3
titles = set()
for name in df['Name']:
    titles.add(name.split(',')[1].split('.')[0].strip())
df['Title']=df['Name'].map(lambda name:name.split(',')[1].split('.')[0].strip())
df["Age"]=df["Age"].fillna(1000)
lt=df["Title"].values.tolist()
la=df["Age"].values.tolist()
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


#4
replacement1 = {
    'T': 0,
    'U': 1,
    'A': 2,
    'G': 3,
    'C': 4,
    'F': 5,
    'B': 6,
    'E': 7,
    'D': 8
}


#5
replacement = {
    'Don': 1,
    'Rev': 2,
    'Jonkheer': 3,
    'Capt': 4,
    'Mr': 5,
    'Dr': 6,
    'Col': 7,
    'Major': 8,
    'Master': 9,
    'Miss': 10,
    'Mrs': 11,
    'Mme': 12,
    'Ms': 13,
    'Mlle': 15,
    'Sir': 14,
    'Lady': 16,
    'the Countess': 17,
    'Dona':18
}


#5
df['Title']=df.Title.map(replacement)



#6
df['Cabin'].fillna('U', inplace=True)
df['Cabin'] = df['Cabin'].apply(lambda x: x[0])
df['Cabin'] = df['Cabin'].apply(lambda x: replacement1.get(x))


#7
df["Sex"]=df["Sex"].replace(to_replace="male",value=0)
df["Sex"]=df["Sex"].replace(to_replace="female",value=1)


#8
df["Embarked"]=df["Embarked"].replace(to_replace=['C','S','Q'],value=[1,2,3])
df.loc[829,"Embarked"]=1
df.loc[61,"Embarked"]=1


#9
df['SibSp'].fillna(8, inplace=True)


replacement3 = {
    6: 0,
    4: 0,
    5: 1,
    0: 2,
    2: 3,
    1: 4,
    3: 5
}
df['Parch'] = df['Parch'].apply(lambda x: replacement3.get(x))
replacement4= {
    5: 0,
    8: 0,
    4: 1,
    3: 2,
    0: 3,
    2: 4,
    1: 5
}

df['SibSp'] = df['SibSp'].apply(lambda x: replacement4.get(x))



#10
from sklearn.preprocessing import StandardScaler
df['Fare'] = StandardScaler().fit_transform(df['Fare'].values.reshape(-1, 1))
df['Age_new'] = StandardScaler().fit_transform(df['Age_new'].values.reshape(-1, 1))
df['Parch'] = StandardScaler().fit_transform(df['Parch'].values.reshape(-1, 1))
df['SibSp'] = StandardScaler().fit_transform(df['SibSp'].values.reshape(-1, 1))
df['Pclass'] = StandardScaler().fit_transform(df['Pclass'].values.reshape(-1, 1))
df['Title'] = StandardScaler().fit_transform(df['Title'].values.reshape(-1, 1))
df['Cabin'] = StandardScaler().fit_transform(df['Cabin'].values.reshape(-1, 1))



#11

X=df[['Pclass','Fare','Sex','SibSp','Parch','Age_new','Title','Child','Cabin']]
y=df['Survived']





#12
df1=pd.read_csv("test.csv")



#13
df1['Cabin'].fillna('U', inplace=True)
df1['Cabin'] = df1['Cabin'].apply(lambda x: x[0])
df1['Cabin'] = df1['Cabin'].apply(lambda x: replacement1.get(x))




#14
df1['Child']=df1['Age']
x4=df.where(df1['Child']<16)
x4['Child'].fillna(0,inplace=True)
y4=x4.where(x4['Child']<2)
y4['Child'].fillna(1,inplace=True)
df1['Child']=y4['Child']


#15
titles = set() ###
for name in df1['Name']:
    titles.add(name.split(',')[1].split('.')[0].strip())
df1['Title']=df1['Name'].map(lambda name:name.split(',')[1].split('.')[0].strip())

df1["Age"]=df1["Age"].fillna(1000)
lt1=df1["Title"].values.tolist()
la1=df1["Age"].values.tolist()
fl1=[]
for i,j in zip(la1,lt1):
    if i==1000:
        if j=="Master":
            fl1.append(7.4)
        elif j=="Mrs":
            fl1.append(38.9)
        elif j=="Miss":
            fl1.append(21.77)
        elif j=="Mr":
            fl1.append(31)
        elif j=="Ms":
        	fl1.append(28)
    else:
        fl1.append(i)
df1["Age_new"]=pd.DataFrame({'col':fl1})


#16
df1['Title']=df1.Title.map(replacement)



#17
df1["Sex"]=df1["Sex"].replace(to_replace="male",value=0)
df1["Sex"]=df1["Sex"].replace(to_replace="female",value=1)
df1["Embarked"]=df1["Embarked"].replace(to_replace=['C','S','Q'],value=[1,2,3])




#18
replacement33 = {
    9: 0,
    6: 0,
    4: 0,
    5: 1,
    0: 2,
    2: 3,
    1: 4,
    3: 5
}
df1['Parch'] = df1['Parch'].apply(lambda x: replacement33.get(x))



replacement44= {
    5: 0,
    8: 0,
    4: 1,
    3: 2,
    0: 3,
    2: 4,
    1: 5
}

df1['SibSp'] = df1['SibSp'].apply(lambda x: replacement44.get(x))




#19
df1.loc[152,"Fare"]=10.0



#20
df1['Fare'] = StandardScaler().fit_transform(df1['Fare'].values.reshape(-1, 1))
df1['Age_new'] = StandardScaler().fit_transform(df1['Age_new'].values.reshape(-1, 1))
df1['Parch'] = StandardScaler().fit_transform(df1['Parch'].values.reshape(-1, 1))
df1['SibSp'] = StandardScaler().fit_transform(df1['SibSp'].values.reshape(-1, 1))
df1['Pclass'] = StandardScaler().fit_transform(df1['Pclass'].values.reshape(-1, 1))
df1['Title'] = StandardScaler().fit_transform(df1['Title'].values.reshape(-1, 1))
df1['Cabin'] = StandardScaler().fit_transform(df1['Cabin'].values.reshape(-1, 1))


#21
test=df1[['Pclass','Fare','Sex','SibSp','Parch','Age_new','Title','Child','Cabin']]



#22
random_forest = RandomForestClassifier(n_estimators=100)
random_forest.fit(X, y)
klu = random_forest.predict(test)






#23
ids=df1['PassengerId'].values
submission_file=open('submission.csv','w')
open_file_object= csv.writer(submission_file)
open_file_object.writerow(["PassengerId","Survived"])
open_file_object.writerows(zip(ids, klu))#here change klu to p to print  values and change back to klu to print random forest prediction values
submission_file.close()

