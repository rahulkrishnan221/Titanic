import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV, cross_val_score
import csv as csv

train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')
features = ['Age', 'SibSp','Parch','Fare','male','embarked_Q','embarked_S','Pclass_2', 'Pclass_3']