import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
df=pd.read_csv("train.csv")

df.plot(x='Fare',y='Pclass',kind='scatter')
plt.show()
"""
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
df.loc[df["Fare"]<=50,"Fare"]=0
df.loc[df["Fare"]>50,"Fare"]=1
X=df[['Pclass','Fare','Sex','SibSp','Parch']]
y=df['Survived']
X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=0)
knn=KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train,y_train)
print(knn.score(X_test,y_test))