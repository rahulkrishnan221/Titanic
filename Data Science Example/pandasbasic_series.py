import pandas as pd
animals=["Liom","Tiger"]
#Series in pandas is amix of list of dict which have index and column in hich it contain values
pd.Series(animals)  #also it can process numpy array
#if it has string missing data it give None object and if integer then NaN float64 type dtype is always object
animals=["Tiger","Lion",None]
pd.Series(animals)
a=[1,2,3,None]
pd.Series(a)
#None is similar to NaN but they are not exact or numerically similar
#if series is created from dictionary object then the index is the keys
sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}
s = pd.Series(sports)
#with list we can have index
s = pd.Series(['Tiger', 'Bear', 'Moose'], index=['India', 'America', 'Canada'])
#in this it stores the value whose indexes are given other are elemenated if index is present but values are missing then it store as NaN as value
sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}
s = pd.Series(sports, index=['Golf', 'Sumo', 'Hockey'])

#Query
sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}
s = pd.Series(sports)
#by index number
s.iloc[3]
#by index key as loc is a attribute
s.loc['Golf']
s[3] #south korea
s['Golf'] #Scotland
 #iTs bit confusing when we have integer in a list and key as a integer so at that case better use loc and iloc
 #to itterate and get value we case iterate like list using for each 
 total = 0 #slow
for item in s:
    total+=item
print(total)
 #faster approach beacuse of vectorixzation
 import numpy as np

total = np.sum(s)
print(total)

#to get first five element
s.head()
#iteration
for label, value in s.iteritems():
    s.set_value(label, value+2)
#Jupiter feature for finding time
%%timeit -n 100
#iterating through loc is bit slow because it modify the value and add value if not exist
#also element can be added like this
s.loc['Animal']='Gorilla'
#here we are having same indexes for multiple value but when we append to old one it will not get appended
#but cricket_loving_countries will get the value and all_countries also get the all value 
original_sports = pd.Series({'Archery': 'Bhutan',
                             'Golf': 'Scotland',
                             'Sumo': 'Japan',
                             'Taekwondo': 'South Korea'})
cricket_loving_countries = pd.Series(['Australia',
                                      'Barbados',
                                      'Pakistan',
                                      'England'], 
                                   index=['Cricket',
                                          'Cricket',
                                          'Cricket',
                                          'Cricket'])
all_countries = original_sports.append(cricket_loving_countries)