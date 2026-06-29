# SCIKIT-LEARN DOCUMENTATION 

# contains a lot of knowledge crafted by experts in the field
# provides in-depth explanation of various machine learning algorithms

# It breaks down complex algorithms into easily understandable components, 
# providing clear explanations of their inner workings

# By studying the documentation, you gain insights into the mathematical foundations of each algorithm, 
# the types of problems they are best suited for, and the key parameters that influence their behavior

# STEP BY STEP GUIDE TO ALGORITHMS AND PARAMETERS 
# Designed to be accessible, tutorials, examples, and API references
#  https://scikit-learn.org/

# User guide - foundational guide to machine learning - overview of key concepts, best practices, and common pitfalls

# API reference - becomes your technical dictionary, offers detailed documentation for class, function, and method

# Examples - is where you can practice, 
# houses a rich collection of code examples that showcase how to apply various machine learning algorithms and techniques to real-world problems

# Tutorials - available for a more hands-on and interactive learning experience 

# Choose your machine learning task - identify the problem you want to solve 
# Are you dealing with classification, regression, clustering, or another type of task?

# Explore available algorithms - head to the API reference section to explore availabke algorithms

# Understand algorithm parameters 
# - each algorithm in the API reference section comes with a detailed description of its parameters

# Experiment with different parameters
# documentation includes examples that demonstrate how to use different algorithms 
# you can use these examples as a starting point and modify the hyperparameters

# Evaluate model performance: 
# once you've trained your model - you must evaluate its performance using appropriate metrics

# CODE EXAMPLE
# in this example, you used the Scikit-learn documentation 
# to better understand the DecisionTreeClassifier class and its parameters

# You loaded the Iris dataset,
# a dataset for classification tasks and then split it into training and testing sets

# Next, you made predictions on the test data, and finally evaluated the model's accuracy
# using the accuracy_score metric

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the Iris dataset
iris = load_iris()
x = iris.data
y = iris.target

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Create a decision tree classifier
clf = DecisionTreeClassifier()

# Train the classifier
clf.fit(x_train, y_train)

# Make predictions on the test set
y_pred = clf.predict(x_test) 

# Evaluate the model's accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)