import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

import seaborn as sns
import matplotlib.pyplot as plt

from sklearn import linear_model
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor

# import the data
file = 'Consumo_cerveja.csv'
data = pd.read_csv(file)

#data cleaning
data.columns = data.columns.str.replace(' ', '_')
data.columns = data.columns.str.replace('[)(]', '')

data = data.dropna(axis=0) 

data['Temperatura_Media_C'] = data['Temperatura_Media_C'].str.replace(',', '.').astype('float')
data['Temperatura_Minima_C'] = data['Temperatura_Minima_C'].str.replace(',', '.').astype('float')
data['Temperatura_Maxima_C'] = data['Temperatura_Maxima_C'].str.replace(',', '.').astype('float')
data['Precipitacao_mm'] = data['Precipitacao_mm'].str.replace(',', '.').astype('float')
data['Final_de_Semana'] = data['Final_de_Semana'].astype('int')

print(data['Precipitacao_mm'].describe(include='all'))
data = data.drop(['Data', 'Temperatura_Minima_C', 'Temperatura_Media_C'], axis=1)

# EDA
sns.regplot(x=data['Temperatura_Media_C'], y=data['Consumo_de_cerveja_litros'])
plt.show()

sns.regplot(x=data['Temperatura_Minima_C'], y=data['Consumo_de_cerveja_litros'])
plt.show()

sns.regplot(x=data['Temperatura_Maxima_C'], y=data['Consumo_de_cerveja_litros'])
plt.show()

plt.hist(data['Precipitacao_mm'])
plt.xlabel('Precipitation')
plt.ylabel('Days')
plt.show()

sns.violinplot(x='Final_de_Semana', y='Consumo_de_cerveja_litros', data=data)
plt.show()

# model development
target = 'Consumo_de_cerveja_litros'
X = np.array(data.drop([target], 1))
y = np.array(data[target])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

linear = linear_model.LinearRegression()
tree = DecisionTreeRegressor()
svr = SVR(kernel='rbf', C=8)

linear.fit(X_train, y_train)
svr.fit(X_train, y_train)
tree.fit(X_train, y_train)

linear_predict = linear.predict(X_test)
tree_predict = tree.predict(X_test)
svr_predict = svr.predict(X_test)

results = pd.DataFrame()
results['consumption_test'] = y_test
results['consumption_linear'] = linear_predict
results['consumption_svr'] = svr_predict
results['consumption_tree'] = tree_predict

print('linear score:{0}'.format(linear.score(X_test, y_test)))
print('tree score:{0}'.format(tree.score(X_test, y_test)))
print('svr score:{0}'.format(svr.score(X_test, y_test)))

print(results.head(15))



