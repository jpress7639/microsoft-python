# CLASSIFICATION 

# predicting which group or category new information belongs to, 
# based ​on its characteristics or features.

# Logistic regression is a particularly popular algorithm for handling binary classifications.

# Sigmoid function - at the heart of logistic regression 
# This function takes a linear combination of your data's features and transforms 
# it into a probability value, a number between 0 and 1.
# often visualized as an S-curve that starts near 0 (representing low probabilities) and ends near 1 (signalling high probabilities)


# Build a Model Step-by-step
# Gather and clean your data - handling any missing data, transforming non-numerical data into numbers 
# Split the data into two sets, one for training, and the other for testing 
# select the most relevant features, charactertistics that will help your model make accurate predictions

# NOTE: Feature selection is crucial 
# 1) helps the model's performance by focusing its learning on the most informative aspects of teh data
# 2) it can significantly reduce the risk of overfitting or underfitting 

# Feed your training data into the logistics algorithm 

# Logistic Regression is adaptable 
# with modifications, it can handle situations where you have more than two possible outcomes or classes

# One common technique is the one vs rest strategy
# you essentially train multiple binary logistic regression models
# Each model focuses on distinguishing one specific class from all the others 
# whichever model gives the highest probability wins 
# - the new data is then classfied as belonging to the class that the winning model was trained to recognize