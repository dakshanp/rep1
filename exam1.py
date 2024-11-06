import pandas as pd
import missingno as msno
titanic_df=pd.read_csv('D:\\Book6.csv',encoding='latin1')
print(titanic_df)
print(titanic_df.info())
print(titanic_df.isnull())
print(titanic_df.isnull().sum())
df=titanic_df.dropna(axis=0)
print(df.isnull().sum())
df.info()
print(titanic_df.columns)
df=titanic_df.drop(['fare'],axis=1)
print(df.isnull().sum())
print(titanic_df['fare'].unique)
titanic_df['fare']=titanic_df['fare'].fillna('C')
print(titanic_df['fare'].isnull().sum())
print(titanic_df)
mean=titanic_df['age'].mean()
print(mean)
titanic_df['age']=titanic_df['age'].fillna(mean)
print(titanic_df['age'])
titanic_df=pd.read_csv('D:\\Book6.csv',encoding='latin1')
mode=titanic_df['fare'].mode()[0]
print(mode)
titanic_df['fare']=titanic_df['fare'].fillna(mode)
print(titanic_df['fare'])
titanic_df['age']=titanic_df['age'].fillna(titanic_df['age'].median())
print(titanic_df['age'])
titanic_df=pd.read_csv('D:\\Book6.csv',encoding='latin1')
print(titanic_df)
new_df=titanic_df.ffill
print(new_df)
new_df=titanic_df.ffill(limit=1)
print(new_df)
new_df=titanic_df.bfill
print(new_df)
