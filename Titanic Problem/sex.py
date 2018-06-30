import pandas as pd
import numpy as np
def sex(df):
    df['male']=np.where(np.logical_and(df['Sex']==0 ,df['Age_new']>18),1,0)
    df['female'] = np.where(np.logical_and(df['Sex'] == 1 , df['Age_new'] )> 18, 1, 0)

    return df
