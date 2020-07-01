# Load Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from pandas.plotting import scatter_matrix


# Load dataset
url = "https://raw.githubusercontent.com/callxpert/datasets/master/iris.data.txt"
names=['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset=pd.read_csv(url,names=names)

# Shape
# print(dataset.shape)
# print(dataset.head(20))

# class distribution
# print(dataset.groupby('class').size())

# box and whisker plots
# dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
# plt.show()


# Histogram
# dataset.hist()
# plt.show()

# Scatter Plot
# scatter_matrix(dataset)
# plt.show()

array = dataset.values
X = array[:,0:4]
Y = array[:,4]
x_train, x_test, y_train, y_test = model_selection.train_test_split(X,Y,test_size=0.2,random_state=7)

# KNN algorithm
model = KNeighborsClassifier()
# Support vector machine
# model = SVC()
# Randomforest
# model = RandomForestClassifier(n_estimators=5)
# Logistic Regression
# model = LogisticRegression()
model.fit(x_train,y_train)
predictions = model.predict(x_test)
print(accuracy_score(y_test,predictions))