import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV, cross_val_score
import csv as csv

df = pd.read_csv('train.csv')
df['Child']=df['Age']
x1=df.where(df['Child']<16)
x1['Child'].fillna(0,inplace=True)
y1=x1.where(x1['Child']<2)
y1['Child'].fillna(1,inplace=True)
df['Child']=y1['Child']
print(df['Child'])



