# -*- coding: utf-8 -*-
"""SongClassification-LogisticRegressionClassifier.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ASJ5INfQNqbSqnoGZwxusEtsIBIhCVU1
"""

#load Libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import OneHotEncoder

#load dataset by uploading
data = pd.read_excel(r'/content/dataset.xlsx')
data.head(10)

#Drop predicting column "Genre" from input dataset
X= data.drop(columns=['Genre'])
X.head()

#Drop predicting column "Genre" from input dataset
X= data.drop(columns=['Genre'])
X.head()

#Column to Predict "DISORDER"
y = data['Genre'].values
y[0:5]

#Obtain column names of columns with object data types(non - numerical) 
nominal_cols = X.columns[X.dtypes==object].tolist()
nominal_cols

#Hot encode above columns
hot_encoder = OneHotEncoder()

data_hot = hot_encoder.fit_transform(X[nominal_cols]).toarray()
data_hot

#Column to Predict "Genre"
y = data['Genre'].values
y[0:5]

#Obtain column names of columns with object data types(non - numerical) 
nominal_cols = X.columns[X.dtypes==object].tolist()
nominal_cols

#Obtain column names of columns with object data types(non - numerical) 
nominal_cols = X.columns[X.dtypes==object].tolist()
nominal_cols

#Generating labels for columns
dataLabels = hot_encoder.get_feature_names(nominal_cols)
dataLabels

#converting the encoded array into a dataframe
X = pd.DataFrame(data_hot, columns=dataLabels)
X.head(5)

#Split data into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 45, stratify =y)

# Create Logistic Regression classifier
clf = LogisticRegression(random_state=0).fit(X_train, y_train)

#Input values to predict the output
(X_test)[0:5]

#Pass input values to prediction model
clf.predict(X_test)
clf.predict_proba(X_test)

#Accuracy of model
clf.score(X_test, y_test)