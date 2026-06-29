# Key Terms and Concepts in Machine Learning

# Machine learning allows computers to learn from data without explicit programming.

# Supervised Learning - when you give the machine labeled data 
# This means each data point is accompanied by a corresponding target or outcome for it to use.
# objective is to train a model capable of predicting the target for new, unseen data
# It provides feedback and corrections along the way and makes sure you are going in the right direction

# Unsupervised Learning - providing the machine with unlabeled data 
# The machine's task is to uncover patterns or structures within the data on its own. 
# Clustering - a common unsupervised learning task
# The goal of clustering is to group similar data points together.

# Features - represent the characteristics or attributes of your data 
# that the machine learning model utilizes to make predictions 

# Labels - denote the target or outcome you aim to predict 
# In classification problems - labels represent the different classes or categories 

# Models - a mathematical representation that encapsulates the patterns and relationships within your data

# Algorithms - step-by-step procedures that machine learning models employ to learn from data and generate predictions
# Linear regression, decision trees, logistic regression, random forests, or support vector machines 

# LINEAR REGRESSION: PREDICTING NUMERICAL VALUES 

# stands as a straightforward yet potent algorithm employed for predicting numerical values. 
# operates under the assumption of a linear relationship between the features and the target
# Example: Linear regression enables you to train a model that predicts the price of a new car given its mileage

# LOGISTIC REGRESSION: CLASSIFICATION TASKS 

# where the objective is to predict the category or class to which a data point belongs
# It estimates the probability that a data point falls into a specific class
# this probability is used to make a classification decision, setting a threshold
# Example: Logistic regression can be leveraged to train a model that classifies new emails as spam or not spam based on these features

# SCIKIT-LEARN: YOUR MACHINE LEARNING TOOLKIT

# a widely acclaimed Python library that offers a comprehensive suite of tools for constructing and evaluating machine learning models
# thoughtfully designed to be user-friendly, even for those new to machine learning

# The library streamlines the model design process by providing a consistent API for various algorithms, 
# allowing you to easily switch between different models and compare their performance

# It encompasses an extensive array of machine learning algorithms:
# including linear regression, logistic regression, decision trees, random forests, and support vector machines

# furnishing tools for gauging the performance of your models:
# tools include metrics like accuracy, precision, recall, MSE (Mean Squared Error), MAE (Mean Absolute Error), and R-squared

# Incorporates tools for cleaning and handling data:
# handling missing values, scaling features, and encoding categorical variables 

# MODEL EVALUATION: MEASURING SUCCESS
# Evaluating the performance of your machine learning models is paramount to ensuring their accuracy in making predictions.

# Classification Metrics:
# Accuracy - represents the proportion of correct predictions out of the total number of predictions
# However, can be misleading in imbalanced datasets where one class is much more prevalent 

# Precision -  focuses on the proportion of true positive predictions out of the total number of positive predictions
# NOTE: particularly relevant when the cost of false positives is high

# Recall - measures the proportion of true positive predictions out of the total number of actual positives
# NOTE: Crucial when the cost of false negatives is high

# Regression Metrics: 

# MSE (Mean Squared Error) - calculates the average squared difference between the predicted values and the actual values
# commonly used for regression problems and penalizes larger errors more severely
# NOTE: its sensitive to outliers 

# MAE (Mean Absolute Error) - computes the average absolute difference between the predicted values and the actual values
# less sensitive to outliers, a more robust metric when dealing with noisy data or outliers 

# R-squared - quantifies how well the model explains the variance in the target variable
# It ranges from 0 to 1, with higher values indicating a better fit
# NOTE: it's important to interpret it in conjunction with other metrics and consider the context of the problem