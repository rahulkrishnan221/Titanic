#Timestamp
pd.Timestamp('9/1/2016 10:05AM')
#period Period('2016-03-05', 'D')
pd.Period('3/5/2016')
t1 = pd.Series(list('abc'), [pd.Timestamp('2016-09-01'), pd.Timestamp('2016-09-02'), pd.Timestamp('2016-09-03')])
#way to have two column as a and b
d1 = ['2 June 2013', 'Aug 29, 2014', '2015-06-26', '7/12/16']
ts3 = pd.DataFrame(np.random.randint(10, 100, (4,2)), index=d1, columns=list('ab'))
#help for making date look clean and well
ts3.index = pd.to_datetime(ts3.index)
#diff
pd.to_datetime('4.7.12', dayfirst=True)
#using range
dates = pd.date_range('10-01-2016', periods=9, freq='2W-SUN')
#finding difference in value
df.diff()
#here resample changes to monday date
df.resample('M').mean()
#get the value
df['2017']
#same
df['2016-12']
#slicing
df['2016-12':]
#changing the value to weeks
df.asfreq('W', method='ffill')
