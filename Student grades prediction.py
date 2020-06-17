# Import data handling libraries
import pandas as pd
import numpy as np

# Import prediction models
from sklearn import linear_model
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR

# Import metrics systems
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.metrics import r2_score
 

# Import csv as dataframe
file = 'student-mat.csv'
data_df = pd.read_csv(file, sep=';')

# select data
df_new = data_df[['studytime', 'failures', 'absences', 'G1', 'G2', 'G3']]

target = 'G3'
X = np.array(df_new.drop([target], 1))
y = np.array(df_new[target])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

linear = linear_model.LinearRegression()
tree = DecisionTreeRegressor()
svr = SVR(kernel='rbf',C=8)

linear.fit(X_train, y_train)
tree.fit(X_train, y_train)
svr.fit(X_train, y_train)

linear_predict = pd.DataFrame(linear.predict(X_test))
tree_predict = pd.DataFrame(tree.predict(X_test))
svr_predict = pd.DataFrame(svr.predict(X_test))
y_real = pd.DataFrame(y_test)


new_df = pd.DataFrame() 

new_df[['y_real']] = y_real
new_df[['linear_predict']] = linear_predict
new_df[['tree_predict']] = tree_predict
new_df[['svr_predict']] = svr_predict

print(new_df.head())

print('linear score:{0}'.format(linear.score(X_test, y_test)))
print('tree score:{0}'.format(tree.score(X_test, y_test)))
print('svr score:{0}'.format(svr.score(X_test, y_test)))

err_lin = mean_squared_error(y_real, linear.predict(X_test))
err_tree = mean_squared_error(y_real, tree.predict(X_test))
err_svr = mean_squared_error(y_real, svr.predict(X_test))

print(err_lin, err_tree, err_svr)

'''
The decision tree model is best for this dataset
'''