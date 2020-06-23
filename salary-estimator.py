import pandas
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score

# Load training dataset
url = "https://raw.githubusercontent.com/callxpert/datasets/master/data-scientist-salaries.cc"
names = ['Years-experience', 'Salary']
dataset = pandas.read_csv(url, names=names)

# Mean, min, max etc
# print(dataset.describe())

# Visualize
# dataset.plot()
# plt.show()

# Setup Training/Testing
X = dataset[['Years-experience']]
y = dataset['Salary']
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=101)

# Training
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train,y_train)

# Testing
predictions = model.predict(X_test)
print(accuracy_score(y_test, predictions))

# Predict
print(model.predict([[6.3]]))