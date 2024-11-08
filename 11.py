import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
titanic_df = pd.read_csv('D:\\Cars93.CSV')
print(titanic_df)
fig, ax = plt.subplots(figsize=(10, 4))
ax.scatter(titanic_df['Horsepower'], titanic_df['Price'])
ax.set_xlabel('Horsepower')
ax.set_ylabel('Price')
plt.title('Scatter plot of Price vs Horsepower')
plt.show()
titanic_df['Horsepower'].plot(kind='box')
plt.show()
q1 = titanic_df['Horsepower'].quantile(0.25)
q3 = titanic_df['Horsepower'].quantile(0.75)
iqr = q3-q1
upper_bound = q3+(1.5*iqr)
lower_bound = q1-(1.5*iqr)
age_arr = titanic_df['Horsepower']
outliers = age_arr[(age_arr <= lower_bound) | (age_arr >= upper_bound)]
print('The following are the outliers in the boxplot of age:\n',outliers)
titanic_df['Price'].plot(kind='hist')
plt.show()
upperIndex = titanic_df[titanic_df['Horsepower']>upper_bound].index
titanic_df.drop(upperIndex,inplace=True)
lowerIndex = titanic_df[titanic_df['Horsepower']<lower_bound].index
titanic_df.drop(lowerIndex,inplace=True)
print(titanic_df.info())
titanic_df = pd.read_csv('D:\\Cars93.csv')
fare_arr = titanic_df['Price']
upper_cap = np.percentile(fare_arr,1)
lower_cap = np.percentile(fare_arr,99)
outliers = fare_arr[(fare_arr < upper_cap) | (fare_arr > lower_cap)]
print('The following are the outliers in the boxplot of fare:\n',outliers)
for i in titanic_df['Price']:
    if i<lower_bound :
        titanic_df['Price'] = titanic_df['Price'].replace(i,lower_cap)
    elif i>upper_bound:
        titanic_df['Price'] = titanic_df['Price'].replace(i,upper_cap)
print(titanic_df.info())
titanic_df = pd.read_csv('D:\\Cars93.csv')
m = np.mean(titanic_df['Horsepower'])
print('mean:',m)
for i in titanic_df['Horsepower']:
    if i<lower_bound or i>upper_bound :
        titanic_df['Horsepower'] = titanic_df['Horsepower'].replace(i,m)
titanic_df = pd.read_csv('D:\\Cars93.csv')
q1 = titanic_df['Horsepower'].quantile(0.25)
q3 = titanic_df['Horsepower'].quantile(0.75)
iqr = q3-q1
upper_bound = q3+(1.5*iqr)
lower_bound = q1-(1.5*iqr)
m = titanic_df['Horsepower'].median()
print(m)
for i in titanic_df['Horsepower']:
    if i<lower_bound or i>upper_bound :
        titanic_df['Horsepower'] = titanic_df['Horsepower'].replace(i,m)
