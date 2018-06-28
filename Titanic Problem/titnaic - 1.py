import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
df=pd.read_csv("train.csv")

df["Sex"]=df["Sex"].replace(to_replace="male",value=0)
df["Sex"]=df["Sex"].replace(to_replace="female",value=1)
df["Embarked"]=df["Embarked"].replace(to_replace=['C','S','Q'],value=[1,2,3])
X=df[['Pclass','Fare','Sex','SibSp','Parch']]
y=df['Survived']
X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=0)
knn=KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train,y_train)
print(knn.score(X_test,y_test))
print(df['Sex'].count())