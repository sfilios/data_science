import pandas
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import KFold


wheat = pandas.read_csv("wheat-2013-supervised.csv")
#show details about the data
print(wheat.describe())
#show the first 5 rows of data
print (wheat.head(5))

#only used some of the parameters, just trying to make a 'quick and dirty' algorithm that displays something
#I would go back and add the rest of the parameters if I had more time

predictors = ["apparentTemperatureMax", "apparentTemperatureMax", "cloudCover", "dewPoint", "humidity"]

#initialize algorithm class
alg=LinearRegression()

#split the dataset into groups for testing and cross validation. Assign those rows.
kf = KFold(wheat.shape[0], n_folds=3, random_state=1)

#initialize list for predictions
predictions = []
for train, test in kf:
	#training set selected as features given in predictors
	train_predictors = (wheat[predictors].iloc[train,:])
   # Using Wheat Yield from the training set to train the algorithm, so set that to train_target
   	train_target = wheat["Yield"].iloc[train]
   # Actually train the algorithm with this function.
	alg.fit(train_predictors, train_target)
   # Extrapolate the model to make predictions on the test set
	test_predictions = alg.predict(wheat[predictors].iloc[test,:])
	predictions.append(test_predictions)
	
predictions = np.concatenate(predictions, axis=0)

print predictions[1:10]
# Didn't figure out how to compare predictions accuracy
