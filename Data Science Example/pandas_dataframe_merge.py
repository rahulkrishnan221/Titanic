staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR'},
                         {'Name': 'Sally', 'Role': 'Course liasion'},
                         {'Name': 'James', 'Role': 'Grader'}])
staff_df = staff_df.set_index('Name')
student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business'},
                           {'Name': 'Mike', 'School': 'Law'},
                           {'Name': 'Sally', 'School': 'Engineering'}])
student_df = student_df.set_index('Name')
print(staff_df.head())
print()
print(student_df.head())
#as it is outer it merge like set union
pd.merge(staff_df, student_df, how='outer', left_index=True, right_index=True)
#set intersection
pd.merge(staff_df, student_df, how='inner', left_index=True, right_index=True)
#shows only the left joint (indexes) combined with right
pd.merge(staff_df, student_df, how='left', left_index=True, right_index=True)
#shows only the right joint (indexes) combined with left
pd.merge(staff_df, student_df, how='right', left_index=True, right_index=True)
#It works with column also
#Here column name are based on Name
pd.merge(staff_df, student_df, how='left', left_on='Name', right_on='Name')
#if common value which is present in both is conflicting then it create location_x and location_y
staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR', 'Location': 'State Street'},
                         {'Name': 'Sally', 'Role': 'Course liasion', 'Location': 'Washington Avenue'},
                         {'Name': 'James', 'Role': 'Grader', 'Location': 'Washington Avenue'}])
student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business', 'Location': '1024 Billiard Avenue'},
                           {'Name': 'Mike', 'School': 'Law', 'Location': 'Fraternity House #22'},
                           {'Name': 'Sally', 'School': 'Engineering', 'Location': '512 Wilson Crescent'}])
pd.merge(staff_df, student_df, how='left', left_on='Name', right_on='Name')
#IF we have PRODUCT ID as index of left and PRODUCT ID is column of right
print(pd.merge(products, invoices, left_index=True, right_on='Product ID'))
#If we merge on both first and last name
pd.merge(staff_df, student_df, how='inner', left_on=['First Name','Last Name'], right_on=['First Name','Last Name'])
#Method chaining sample called python idioms or pandorable
df=(df.where(df["Quantity"]==0)).dropna().rename(columns={"Weight":"Weight(oz.)"})
#map example in which we pass the df in a function
#axis=1 says that to take all row
import numpy as np
def min_max(row):
    data = row[['POPESTIMATE2010',
                'POPESTIMATE2011',
                'POPESTIMATE2012',
                'POPESTIMATE2013',
                'POPESTIMATE2014',
                'POPESTIMATE2015']]
    return pd.Series({'min': np.min(data), 'max': np.max(data)})
    #OR::::
#   row['max'] = np.max(data)
#   row['min'] = np.min(data)
#   return row
df.apply(min_max, axis=1)
#using lambda
row=['POPESTIMATE2010',
                'POPESTIMATE2011',
                'POPESTIMATE2012',
                'POPESTIMATE2013',
                'POPESTIMATE2014',
                'POPESTIMATE2015']
df.apply(lambda x:np.max(x[row]))
#Group by return two object one the specified one and other is all info its like unique but faster and frame is arranged in order of group
#so 1 data for group and bundle of data for frame of that group
for group, frame in df.groupby('STNAME'):
    avg = np.average(frame['CENSUS2010POP'])
    print('Counties in state ' + group + ' have an average population of ' + str(avg))
#OTHER and slower approach
for state in df['STNAME'].unique():
    avg = np.average(df.where(df['STNAME']==state).dropna()['CENSUS2010POP'])
    print('Counties in state ' + state + ' have an average population of ' + str(avg))
#Using aggregate this length of code can be reduce
df.groupby('STNAME').agg({'CENSUS2010POP': np.average}) #so two column one STNAME AND other SENSUS
#can be used like this also
print(df.groupby('Category').apply(lambda df,a,b: sum(df[a] * df[b]), 'Weight (oz.)', 'Quantity'))
(df.set_index('STNAME').groupby(level=0)['CENSUS2010POP'].agg({'avg': np.average, 'sum': np.sum}))
(df.set_index('STNAME').groupby(level=0)['POPESTIMATE2010','POPESTIMATE2011'].agg({'avg': np.average, 'sum': np.sum})



#Putting in order for data low<medium<high
s = pd.Series(['Low', 'Low', 'High', 'Medium', 'Low', 'High', 'Low'])
s.astype('category', categories=['Low', 'Medium', 'High'], ordered=True)

df = pd.DataFrame(['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D'],
                  index=['excellent', 'excellent', 'excellent', 'good', 'good', 'good', 'ok', 'ok', 'ok', 'poor', 'poor'])
df.rename(columns={0: 'Grades'}, inplace=True)
grades = df['Grades'].astype('category',
                             categories=['D', 'D+', 'C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A', 'A+'],
                             ordered=True)
grades.head()


#Break the data into bins,halfs using cut it helps to categories using intervals
s = pd.Series([168, 180, 174, 190, 170, 185, 179, 181, 175, 169, 182, 177, 180, 171])
pd.cut(s, 3)
# You can also add labels for the sizes [Small < Medium < Large].
pd.cut(s, 3, labels=['Small', 'Medium', 'Large'])

#pivot table creation
pd.pivot_table(Bikes, index=['Manufacturer','Bike Type'])
#new index with column year and make value column name that column is filled with value kw
df.pivot_table(values='(kW)', index='YEAR', columns='Make', aggfunc=np.mean)
#can also perform list of function
df.pivot_table(values='(kW)', index='YEAR', columns='Make', aggfunc=[np.mean,np.min], margins=True)
