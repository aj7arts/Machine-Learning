# -*- coding: utf-8 -*-
"""ML_Prac_03

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nFaaXIkEw6LF_ghjGu9xx5U7DPu2h4TF
"""

import pandas as pd

iris_data = pd.read_csv('Iris.csv')

iris_data.head()

iris_data.info()

from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
iris_data['Species'] = encoder.fit_transform(iris_data['Species'])

iris_data.head(150)

import matplotlib.pyplot as plt

plt.pie(iris_data['Species'].value_counts(),labels=['Setosa','Versicolor','Virginica'],autopct='%0.2f')
plt.show()

x = iris_data.drop('Species',axis=1)
y = iris_data['Species']

print(x)

print(y)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=2)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression(max_iter = 1000)
model.fit(x_train,y_train)

pred_train = model.predict(x_train)

from sklearn.metrics import confusion_matrix,accuracy_score
accuracy_score(y_train,pred_train)

pred_test = model.predict(x_test)

accuracy_score(y_test,pred_test)

confusion_matrix(y_test,pred_test)