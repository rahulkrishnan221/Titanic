import pandas as pd
import csv as csv
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

df=pd.read_csv("train.csv")
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

"""

df['Title']=df.Title.map(replacement)

from sklearn.preprocessing import StandardScaler
df['Fare'] = StandardScaler().fit_transform(df['Fare'].values.reshape(-1, 1))
df['Age_new'] = StandardScaler().fit_transform(df['Age_new'].values.reshape(-1, 1))
df['Parch'] = StandardScaler().fit_transform(df['Parch'].values.reshape(-1, 1))
df['SibSp'] = StandardScaler().fit_transform(df['SibSp'].values.reshape(-1, 1))
df['Pclass'] = StandardScaler().fit_transform(df['Pclass'].values.reshape(-1, 1))
df['Title'] = StandardScaler().fit_transform(df['Title'].values.reshape(-1, 1))
df['Cabin'] = StandardScaler().fit_transform(df['Cabin'].values.reshape(-1, 1))

df.plot(x='Pclass',y='Survived',kind='scatter')
plt.show()
print(df.columns)
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.scatter(df['Fare'], df['Pclass'], df['Age'], c = df['Survived'], marker = 'o', s=100)
ax.set_xlabel('Fare')
ax.set_ylabel('Class')
ax.set_zlabel('Age')
plt.show()
"""
"""print(df["Sex"])
xd=df[(df["Survived"]==1 )& (df["Sex"]=="female")]
print(xd.count())
print(df["Pclass"][df["Fare"]>500])"""
df["Sex"]=df["Sex"].replace(to_replace="male",value=0)
df["Sex"]=df["Sex"].replace(to_replace="female",value=1)
df["Embarked"]=df["Embarked"].replace(to_replace=['C','S','Q'],value=[1,2,3])
df['familia']=df['SibSp']+df['Parch']
df.loc[829,"Embarked"]=2
df.loc[61,"Embarked"]=2
df['Title_rating']=df.Title.map(replacement)
df.loc[(df.Title=="Master") & (df.Pclass <=2 ),"rich_master"]=1
df.loc[(df.Title=="Master") & (df.SibSp <=2),"master_freesib"]=1
df.loc[(df.Parch==0)&(df.Title=="Mrs")&(df.SibSp==1),"female_alive1"]=1
df["female_alive1"]=df["female_alive1"].fillna(0)
df["rich_master"]=df["rich_master"].fillna(0)
df["master_freesib"]=df["master_freesib"].fillna(0)
df["Cabin"]=df["Cabin"].fillna(0)
df.loc[df["Cabin"]!=0,"Cabin"]=1
X=df[['Pclass','Fare','Sex','Embarked','Age_new','Title_rating','rich_master','master_freesib','female_alive1','familia',"Cabin"]]
y=df['Survived']
#X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=0)
#knn=KNeighborsClassifier(n_neighbors=3)
#knn.fit(X,y)

df1=pd.read_csv("test.csv")

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
            fl1.append(32)
        elif j=="Ms":
        	fl1.append(28)
    else:
        fl1.append(i)
df1["Age_new"]=pd.DataFrame({'col':fl1})

df1['Title_rating']=df1.Title.map(replacement)

df1["Sex"]=df1["Sex"].replace(to_replace="male",value=0)
df1["Sex"]=df1["Sex"].replace(to_replace="female",value=1)
df1["Embarked"]=df1["Embarked"].replace(to_replace=['C','S','Q'],value=[1,2,3])
df1['familia']=df1['SibSp']+df1['Parch']
df1.loc[(df1.Title=="Master") & (df1.Pclass <=2 ),"rich_master"]=1
df1.loc[(df1.Title=="Master") & (df1.SibSp <=2),"master_freesib"]=1
df1["rich_master"]=df1["rich_master"].fillna(0)
df1["master_freesib"]=df1["master_freesib"].fillna(0)
df1.loc[(df1.Parch==0)&(df1.Title=="Mrs")&(df1.SibSp==1),"female_alive1"]=1
df1["female_alive1"]=df1["female_alive1"].fillna(0)
df1.loc[df1["Cabin"]!=0,"Cabin"]=1
test=df1[['Pclass','Fare','Sex','Embarked','Age_new','Title_rating','rich_master','master_freesib','female_alive1','familia',"Cabin"]]
test.loc[152,"Fare"]=10
#p=knn.predict(test)
X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=0)
random_forest = RandomForestClassifier(n_estimators=1000)
random_forest.fit(X_train, y_train)
print(random_forest.score(X_test,y_test))
klu = random_forest.predict(test)








ids=df1['PassengerId'].values
submission_file=open('submission1000.csv','w')
open_file_object= csv.writer(submission_file)
open_file_object.writerow(["PassengerId","Survived"])
#for i,j in zip(ids,klu):
#	print(i,j)
open_file_object.writerows(zip(ids, klu))#here change klu to p to print  values and change back to klu to print random forest prediction values
submission_file.close()
