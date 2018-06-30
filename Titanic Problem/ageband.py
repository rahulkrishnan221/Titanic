def age_band(df):
    df['Child']=df["Age_new"].map(lambda s:1 if 0<=s<18 else 0 )
    df['Mid']=df['Age_new'].map(lambda s:1 if 18<=s<=35 else 0)
    df['Old']=df['Age_new'].map(lambda s:1 if s>35 else 0)
    return df