import pandas as pd
def femparch(df):
    df.loc[(df.Parch==0)&(df.Title=="Mrs")&(df.SibSp==1),"female_alive1"]=1
    df["female_alive1"]=df["female_alive1"].fillna(0)
    return df