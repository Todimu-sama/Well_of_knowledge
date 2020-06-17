# import data handling libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# import data visualisation libraries
import seaborn as sns
import matplotlib.pyplot as plt

# import machine learning prediction libraries
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

# import model evaluation metrics
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.model_selection import cross_val_score

# importing data sets
tit_tr = pd.read_csv('train_clean.csv')
tit_te = pd.read_csv('test_clean.csv')

print(tit_tr.dtypes)

# some exploratory dat a analysis
print('{0} rows'.format(tit_tr.shape[0]))
print(tit_tr['Survived'].value_counts())

sns.countplot(x='Sex', data=tit_tr, palette='hls', hue='Survived')
plt.show()

sns.countplot(x='Embarked', data=tit_tr, palette='hls', hue='Survived')
plt.show()

sns.countplot(x='Pclass', data=tit_tr, palette='hls', hue='Survived')
plt.show()

sns.countplot(x='Title', data=tit_tr, palette='hls', hue='Survived')
plt.show()

# pre processing the data
tit_tr['Sex'] =  tit_tr['Sex'].astype('category')
tit_tr['Sex'] = tit_tr['Sex'].cat.codes

cat = ['Embarked', 'Title']

for var in cat:
    tit_tr = pd.concat([tit_tr, pd.get_dummies(tit_tr[var], prefix=var)], axis=1)
    del tit_tr[var]
    
tit_tr = tit_tr.drop(['Cabin', 'Name', 'Ticket', 'PassengerId'], axis=1)

# train test split
target = 'Survived'
X = np.array(tit_tr.drop([target], 1))
print(X)
y = np.array(tit_tr[target])

X_train, X_value, y_train, y_value = train_test_split(X, y, test_size=0.2, random_state=4)

# train models
rf = RandomForestClassifier(random_state=42)
tree = DecisionTreeRegressor()
svr = SVC(kernel='rbf', C=8)
lr = LogisticRegression()

# fit and train models
rf.fit(X_train, y_train)
tree.fit(X_train, y_train)
svr.fit(X_train, y_train)
lr.fit(X_train, y_train)

a = rf.predict(X_value)
b = tree.predict(X_value)
c = svr.predict(X_value)
d = lr.predict(X_value)

b = b.astype('int')

# out of sample evaluation
print('random forest accuracy:',accuracy_score(y_value, rf.predict(X_value)))
print('decision tree accuracy',accuracy_score(y_value, b))
print('svr accuracy', accuracy_score(y_value, c))
print('Logistic regression accuracy', accuracy_score(y_value, d))

# preprocessing the test data 
tit_te['Sex'] =  tit_te['Sex'].astype('category')
tit_te['Sex'] = tit_te['Sex'].cat.codes

cat = ['Embarked', 'Title']

for var in cat:
    tit_te = pd.concat([tit_te, pd.get_dummies(tit_te[var], prefix=var)], axis=1)
    del tit_te[var]
    
tit_te = tit_te.drop(['Cabin', 'Name', 'Ticket', 'PassengerId'], axis=1)

# train test split
target = 'Survived'
X = np.array(tit_te.drop([target], 1))

yhat_rf = rf.predict(X).astype('int')
yhat_tree = tree.predict(X).astype('int')
yhat_svr = svr.predict(X).astype('int')
yhat_lr = lr.predict(X).astype('int')

new_df = pd.DataFrame()

new_df['yhat_rf'] = yhat_rf
new_df['yhat_tree'] = yhat_tree
new_df['yhat_svr'] = yhat_svr
new_df['yhat_lr'] = yhat_lr

print(new_df.head(15))
