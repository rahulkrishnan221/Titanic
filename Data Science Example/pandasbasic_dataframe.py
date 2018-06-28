#dataframes can be made from series or dictionary
import pandas as pd
purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})
df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])
df.head()
#here we have three column as Name,Item Purchased,Cost   and indexes as Store 1 Store 1 Store 2
#Output for
df['Store 2']
#Name                  Vinod
#Item Purchased    Bird Seed
#Cost                      5
#Name: Store 2, dtype: object

#for checking type
type(df.loc['Store 2'])
#if we need to get the column item with indexes
df['Name']  #df['column Name']
#if we want to select item from particular indices and from particular column
df.loc['Store 1','Name']  
# OR
df.loc['Store']['Name']
# for transpose but original not affected
df.T 
#for accessing column using loc and transpose
df.T.loc['Name']
#for slicing
df.loc[:,['Name', 'Cost']]
#for droping the column or row label
df.drop("Store 1") #to make changes we need to store in df=df.drop()
copy_df = df.copy()
copy_df = copy_df.drop('Store 1')
#for deleting without assigning so column deleted
del df['Name']
#Remember if any of the column is copied to new dataframe if any changed meant to that data frame affect orginally so to avoid that use .copy
costs = df['Cost']
costs+=2
# read csv using pandas
df=pd.read_csv('olympics.csv')
#in this it is ignoring index column 0 and ignore the first row(skip rows upto)
df = pd.read_csv('olympics.csv', index_col = 0, skiprows=1)
#get list of all columns
df.columns
#Rename the column it take value as dict present and new one :::inplace will help to make change to original df also if set true
 df.rename(columns={"Name":"New Name"},inplace=True)
 #Sample with slicing
 for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold' + col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver' + col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze' + col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#' + col[1:]}, inplace=True) 

df.head()
#it has a layer of boolean mask over it as it return boolean value if fails
xd=df['Gold'] >0 #here it has boolean value and count give 147
xd.count()
#It count
#where is used when the condition is false it add NaN
only_gold = df.where(df['Gold'] > 0) #So with NaN count give 100 and normally df has 147 value
only_gold = only_gold.dropna()    #it remove the row which have NaN
df[(df['Gold.1'] > 0) & (df['Gold'] == 0)] #also we can perform and ,or operation  and store in new in dfr
#print both name and cost >3
df['Name'][df['Cost']>3]

#df.index take all the index and here storing it in country column
df['country'] = df.index
#If setting index gold as new index from gold column
df= df.set_index('Gold')
#reset index to  0......n form
df = df.reset_index()
#returns all unique value in column
df['SUMLEV'].unique()
columns_to_keep = ['STNAME',
                   'CTYNAME',
                   'BIRTHS2010',
                   'BIRTHS2011',
                   'BIRTHS2012',
                   'BIRTHS2013',
                   'BIRTHS2014',
                   'BIRTHS2015',
                   'POPESTIMATE2010',
                   'POPESTIMATE2011',
                   'POPESTIMATE2012',
                   'POPESTIMATE2013',
                   'POPESTIMATE2014',
                   'POPESTIMATE2015']
#it stores the stated column in df and remove all other
df = df[columns_to_keep]
#:::::::::::::::::::making dual index
df = df.set_index(['STNAME', 'CTYNAME'])
#then for query
df.loc['Michigan', 'Washtenaw County']
#multiple query
df.loc[ [('Michigan', 'Washtenaw County'),
         ('Michigan', 'Wayne County')] ]
#Helps to name the index
df.index.names = ['Location', 'Name']
#while using append indexes are as name value of column as data
df = df.append(pd.Series(data={'Cost': 3.00, 'Item Purchased': 'Kitty Food'}, name=('Store 2', 'Kevyn')))
#any case for append keyword it is mandatory to use name and data
df = df.append(pd.Series(data={'Cost': 3.00, 'Item Purchased': 'Kitty Food','Name':'Test'}, name='store2'))
#na_values : scalar, str, list-like, or dict, default None
#Additional strings to recognize as NA/NaN. If dict passed, specific per-column NA values. By default the following values are interpreted as NaN: ‘’, ‘#N/A’, ‘#N/A N/A’, ‘#NA’, ‘-1.#IND’, ‘-1.#QNAN’, ‘-NaN’, ‘-nan’, ‘1.#IND’, ‘1.#QNAN’, ‘N/A’, ‘NA’, ‘NULL’, ‘NaN’, ‘n/a’, ‘nan’, ‘null’.
pd.read_csv('hello.csv',na_values="Na",na_filter=True)
#na_filter : boolean, default True
#Detect missing value markers (empty strings and the value of na_values). 
#In data without any NAs, passing na_filter=False can improve the performance of reading a large file

#sorting the index
df = df.sort_index()
#this is used to fill the missing values
#DataFrame.fillna(value=None, method=None, axis=None, inplace=False, limit=None, downcast=None, **kwargs)[source]
#value : scalar, dict, Series, or DataFrame
#Value to use to fill holes (e.g. 0), alternately a dict/Series/DataFrame of values specifying which value to use for each index (for a Series) or column (for a DataFrame). (values not in the dict/Series/DataFrame will not be filled). This value cannot be a list.
#method : {‘backfill’, ‘bfill’, ‘pad’, ‘ffill’, None}, default None
#method to use for filling holes in reindexed Series pad / ffill: propagate last valid observation forward to next valid backfill / bfill: use NEXT valid observation to fill gap
df.fillna(0)

 values = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
df.fillna(value=values)
#for maximum
df.["Summer"].max()