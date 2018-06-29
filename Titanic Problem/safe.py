import pandas as pd
import csv as csv
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

df=pd.read_csv("train.csv")

df['Cabin'].fillna('U', inplace=True)
df['Cabin'] = df['Cabin'].apply(lambda x: x[0])
df['Cabin'].unique()


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



df["Sex"]=df["Sex"].replace(to_replace="male",value=0)
df["Sex"]=df["Sex"].replace(to_replace="female",value=1)
df["Embarked"]=df["Embarked"].replace(to_replace=['C','S','Q'],value=[1,2,3])
df.loc[829,"Embarked"]=2
df.loc[61,"Embarked"]=2


X=df[['Pclass','Fare','Sex','SibSp','Parch','Embarked','Age_new']]
y=df['Survived']
#X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=0)




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

df1.loc[152,"Fare"]=10


df1["Sex"]=df1["Sex"].replace(to_replace="male",value=0)
df1["Sex"]=df1["Sex"].replace(to_replace="female",value=1)
df1["Embarked"]=df1["Embarked"].replace(to_replace=['C','S','Q'],value=[1,2,3])



test=df1[['Pclass','Fare','Sex','SibSp','Parch','Embarked','Age_new']]



random_forest = RandomForestClassifier(n_estimators=100)
random_forest.fit(X, y)
#print(random_forest.score(X_test,y_test))
klu = random_forest.predict(test)








ids=df1['PassengerId'].values
submission_file=open('submission.csv','w')
open_file_object= csv.writer(submission_file)
open_file_object.writerow(["PassengerId","Survived"])
open_file_object.writerows(zip(ids, klu))#here change klu to p to print  values and change back to klu to print random forest prediction values
submission_file.close()
