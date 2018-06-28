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


df['Child']=df['Age']
x1=df.where(df['Child']<16)
x1['Child'].fillna(0,inplace=True)
y1=x1.where(x1['Child']<2)
y1['Child'].fillna(1,inplace=True)
df['Child']=y1['Child']

titles = set()
for name in df['Name']:
    titles.add(name.split(',')[1].split('.')[0].strip())
df['Title']=df['Name'].map(lambda name:name.split(',')[1].split('.')[0].strip())
"""
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

replacement = {
    'Don': 0,
    'Rev': 0,
    'Jonkheer': 0,
    'Capt': 0,
    'Mr': 1,
    'Dr': 2,
    'Col': 3,
    'Major': 3,
    'Master': 4,
    'Miss': 5,
    'Mrs': 6,
    'Mme': 7,
    'Ms': 7,
    'Mlle': 7,
    'Sir': 7,
    'Lady': 7,
    'the Countess': 7,
    'Dona':8
}
df['Title']=df.Title.map(replacement)
df['Cabin'].fillna('U', inplace=True)
df['Cabin'] = df['Cabin'].apply(lambda x: x[0])

df['Cabin'] = df['Cabin'].apply(lambda x: replacement1.get(x))
df["Sex"]=df["Sex"].replace(to_replace="male",value=0)
df["Sex"]=df["Sex"].replace(to_replace="female",value=1)
df["Embarked"]=df["Embarked"].replace(to_replace=['C','S','Q'],value=[1,2,3])
df.loc[829,"Embarked"]=1
df.loc[61,"Embarked"]=1
df['Age'].fillna(23.826033707865168, inplace=True)
X=df[['Pclass','Fare','Sex','SibSp','Parch','Embarked','Age','Title','Child','Cabin']]
y=df['Survived']

knn=KNeighborsClassifier(n_neighbors=3)
knn.fit(X,y)

df1=pd.read_csv("test.csv")
df1['Cabin'].fillna('U', inplace=True)
df1['Cabin'] = df1['Cabin'].apply(lambda x: x[0])

df1['Cabin'] = df1['Cabin'].apply(lambda x: replacement1.get(x))
df1['Child']=df1['Age']
x4=df.where(df1['Child']<16)
x4['Child'].fillna(0,inplace=True)
y4=x4.where(x4['Child']<2)
y4['Child'].fillna(1,inplace=True)
df1['Child']=y4['Child']
titles = set() ###
for name in df1['Name']:
    titles.add(name.split(',')[1].split('.')[0].strip())
df1['Title']=df1['Name'].map(lambda name:name.split(',')[1].split('.')[0].strip())
df1['Title']=df1.Title.map(replacement)
df1["Sex"]=df1["Sex"].replace(to_replace="male",value=0)
df1["Sex"]=df1["Sex"].replace(to_replace="female",value=1)
df1["Embarked"]=df1["Embarked"].replace(to_replace=['C','S','Q'],value=[1,2,3])
df1['Age'].fillna(24.10191846522782, inplace=True)
test=df1[['Pclass','Fare','Sex','SibSp','Parch','Embarked','Age','Title','Child','Cabin']]
test.loc[152,"Fare"]=10
p=knn.predict(test)


random_forest = RandomForestClassifier(n_estimators=100)
random_forest.fit(X, y)
klu = random_forest.predict(test)







ids=df1['PassengerId'].values
submission_file=open('submission.csv','w')
open_file_object= csv.writer(submission_file)
open_file_object.writerow(["PassengerId","Survived"])
open_file_object.writerows(zip(ids, klu))#here change klu to p to print  values and change back to klu to print random forest prediction values
submission_file.close()

"""
=======
print(p)

>>>>>>> d2a4a42ce1fdc00f2b59c2687073833f22ba9a8e
for i in range(0,df1["Pclass"].count()):
    prediction=knn.predict([[test.loc[i]["Pclass"],test.loc[i]["Fare"],test.loc[i]["Sex"],test.loc[i]["SibSp"],test.loc[i]["Parch"]]])
    print(test.loc[i]["Pclass"],test.loc[i]["Fare"],test.loc[i]["Sex"],test.loc[i]["SibSp"],test.loc[i]["Parch"],prediction)
"""