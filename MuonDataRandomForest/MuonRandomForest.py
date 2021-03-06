#===================================================================================
# This is an example of how to create a random forest
# From http://www.agcross.com/2015/02/random-forests-in-python-with-scikit-learn/
#===================================================================================

# Import Random Forest and Scikit's example dataset
from sklearn.ensemble import RandomForestClassifier as RFC
from sklearn.datasets import load_iris

# Import necessary packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import timeit

# Start program timer
start = timeit.default_timer()

#===================================================================================
#///////// Load Dataset ////////////////////////////////////////////////////////////
#===================================================================================

# Create dataframe from iris dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

#===================================================================================
#////// Train and Test Random Forest ///////////////////////////////////////////////
#===================================================================================

# Create a random uniform distribution between 0 and 1
# Assign 75% to be a training subset
df['is_train'] = np.random.uniform(0, 1, len(df)) <= 0.75

# decompress an array of the assigned categories (species)
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

# Explicitly create train and test sets
# Then create the model's input variables as 'features'
train = df[df['is_train']==True]
test = df[df['is_train']==False]
features = df.columns[0:4]

# input the model parameters (# of jobs and # of trees)
forest = RFC(n_jobs=2, n_estimators=50)

# recompress the array that contains category names
y, _ = pd.factorize(train['species'])

# fit the model to the training data and use it to predict
# the category for each of the points in the test data
forest.fit(train[features], y)
preds = iris.target_names[forest.predict(test[features])]
print pd.crosstab(index=test['species'], columns=preds, rownames=['actual'], colnames=['preds'])

# Stop the timer and get the run time of creating the 
# Random Forest
stop = timeit.default_timer()
print "The runtime of training and testing the random forest is: "  
print stop - start

#===================================================================================
#////// Plots //////////////////////////////////////////////////////////////////////
#===================================================================================

# Sort the most important features (variables)
importances = forest.feature_importances_
indicies = np.argsort(importances)

# Plot the most important features
plt.figure(1)
plt.title('Feature Importances')
plt.barh(range(len(indicies)), importances[indicies], color='b', align='center')
plt.yticks(range(len(indicies)), features[indicies])
plt.xlabel('Relative Importance')
plt.savefig('FeatureImportance.png')

