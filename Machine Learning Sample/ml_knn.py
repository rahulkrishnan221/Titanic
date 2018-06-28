import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from matplotlib import cm
from sklearn.neighbors import KNeighborsClassifier

fruits=pd.read_table('fruit_data_with_colors.txt')
lookup_fruit_name=dict(zip(fruits['fruit_label'].unique(),fruits['fruit_name'].unique()))
X=fruits[['mass','width','height']]
y=fruits['fruit_label']

# default is 75% and 25% split
X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=0)

#Visualizing
#Scatter plot
#cmap=cm.get_cmap('gnuplot')
#scatter=pd.scatter_mattrix(X_train,c=y_train,marker='o',s=40, hist_kwds={'bins':15}, figsize=(9,9), cmap=cmap)


#3D plot
"""from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.scatter(X_train['mass'], X_train['width'], X_train['height'], c = y_train, marker = 'o', s=100)
ax.set_xlabel('mass')
ax.set_ylabel('width')
ax.set_zlabel('height')
plt.show() """


knn=KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train,y_train)
accracy=knn.score(X_test,y_test)
fruit_prediction=knn.predict([[20,4.3,5.5]])
print(lookup_fruit_name[fruit_prediction[0]])

#visualiziing knn
"""
from adspy_shared_utilities import plot_fruit_knn

plot_fruit_knn(X_train, y_train, 5, 'uniform')

#How sensitive is k-NN classification accuracy to the choice of the 'k' parameter?

k_range = range(1,20)
scores = []

for k in k_range:
    knn = KNeighborsClassifier(n_neighbors = k)
    knn.fit(X_train, y_train)
    scores.append(knn.score(X_test, y_test))

plt.figure()
plt.xlabel('k')
plt.ylabel('accuracy')
plt.scatter(k_range, scores)
plt.xticks([0,5,10,15,20]);

How sensitive is k-NN classification accuracy to the train/test split proportion?
t = [0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2]

knn = KNeighborsClassifier(n_neighbors = 5)

plt.figure()

for s in t:

    scores = []
    for i in range(1,1000):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1-s)
        knn.fit(X_train, y_train)
        scores.append(knn.score(X_test, y_test))
    plt.plot(s, np.mean(scores), 'bo')

plt.xlabel('Training set proportion (%)')
plt.ylabel('accuracy')
"""
