import pandas as pd
def rich(df):
  df.loc[(df.Title=="Master") & (df.Pclass <=2 ),"rich_master"]=1
  df.loc[(df.Title=="Master") & (df.SibSp <=2),"master_freesib"]=1
  df["rich_master"]=df["rich_master"].fillna(0)
  df["master_freesib"]=df["master_freesib"].fillna(0)
  return df