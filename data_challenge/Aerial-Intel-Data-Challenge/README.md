# AI-Data-Challenge
Data Challenge for Aerial Intelligence

For the data Challenge, my first step was to determine what sort of approach to use to analyze the given data. Because the outcome we are interested in (Winter Wheat yield) is a continuous variable, and we have several features to use in predicting Winter Wheat Yield, this problem can be approached using multiple variable linear regression.

Because I have recently completed an exercise using Octave/MatLab wherein we implemented linear regression, I took the basic code from that exercise and adapted it for use with this dataset. This is found in "ai3.m". 

In this approach, I first read in the data, selected the relevant features (ignoring those mentioned in the challenge context information). The data needed to be split into a training, cross validation, and test set, so it made sense to me to use the 2013 data as the training set, and then use half of 2014 for cross validation and half for the test set.

The next step was to implement linear regression. To do this, I need to minimize the cost of theta for each feature. I decided to use gradient descent to minimize the cost of theta ("gradientDescent.m"). Consequently, I first normalized the features by subtracting the mean of each feature and dividing by the standard deviation of that feature ("featureNormalize.m"). Next, I found the cost of theta, and used arbitrary values for alpha and the number of iterations to run gradient descent. This is one of the things that I would do differently if given more time. Gradient descent was chosen primiarly because of my familiarity with the method, but if I were more familiar with other cost-minimizing functions, I would choose one of those instead.

After attempting to approach the problem in this manner, I ran into an issue wherein theta was not properly computing, and returning NaN values. After seeking out the bug for a bit, I decided to turn to Python instead Octave/MatLab, and use a module that already has a linear regression function, rather than using my own. I followed the tutorial from DataQuest that demonstrates participating in Kaggle competitions, and used my dataset instead of their example. This is the "ai.py" file in the repository.

The python method successfully reads in and summarizes the data, and performs linear regression. At this point, because Parth asked me only to spend a couple of hours on the challenge I decided to stop. The next step that I would take is to figure out how to compute the accuracy of the model, and then test it on the remainder of the dataset. Because I only used one year of data for the python exercise, I would also redo this analysis using subsets of both datasets.

I definitely learned during this project that choosing an approach that you're more familiar with (Octave, Gradient Descent) may not necessarily be faster or easier than an approach that you are less comfortable with (Python, Pandas/NumPy).

Thanks!

-Stephen

