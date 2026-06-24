# MACHINE LEARNING 

# It's a subset of AI that allows computers to learn from data without being explicity programmed

# revolves around the development of algorithm
# allow computers to analyze data, identify patterns, and make predictions or decisions

# Supervised Learning - the algorithm is provided with labeled data 
# learns to map inputs to outputs, allowing it to make decisions

# e.g. Image Recognition, Spam Filtering, and Predictive Modeling 

# Unsupervised Learning - presenting the algorithm with unlabeled data
# algorithm's task is to disover hidden patterns, structures, or relationships in the data

# Customer segmentation, Anomaly Detection, Dimensionality Reduction 

# Reinforcement Learning - has an agent learn by interacting with an environment, taking actions to maximize rewards

# Game playing, Robotics, Personalized Recommendations

# Healthcare, it's being used to aid in early disease detection, find things in X-Ray, MRI Imaging to detect things that are not caught by the naked eye
# Finance, predict stock market trends, detect fraudulent transactions
# Commerce, it powers personalized product recommendations, targeted advertising, chatbots

# Siri and Alexa - leverage machine learning to understand and respond to your voice

# HOW MACHINE LEARNING WORKS 
# We feed the machine learning model a massive amount of labeled data, for example, pictures ​of cats and dogs with the correct labels.
# The model analyzes this data, identifies patterns, and learns to distinguish between the two.

# The model optimizes its guesses based on its performance.
# The more data it's trained on, the more accurate its predictions become. 

# KEY TERMINOLOGY IN MACHINE LEARNING

# Features: The Descriptive Attributes 
# Features serve as the descriptive attributes that characterize the data we work with
# They represent the individual pieces of information that provide insights into the patterns and relationships within the data

# Selection and engineering of features play a pivotal role in the success of a machine learning model

# Labels: The Target Outcome
# labels represent the target outcome or the value you aim to predict

# serve as the ground truth or the desired output for a given set of features

# play a critical role in supervised learning, 
# where the model learns from labeled examples to make predictions on unseen data

# Models: The Mathematical Representation

# can be conceptualized as a mathematical representation of the relationship 
# between features and labels

# It encapsulates the knowledge and patterns extracted from the training data, 
# enabling it to make predictions or decisions on new, unseen data

# A model acts as a bridge between the input features and the desired output labels.

# TYPES OF MODELS:

# Linear regression: Models the relationship between features and a continuous label using a linear equation.

# Decision trees: create a tree-like structure of decisions based on feature values, 
# leading to a predicted label. 
# Easy to interpret and visualize

# Support Vector Machines (SVMs)
# find the best boundary (hyperplane) to separate data points into different classes
# SVMs are effective in high-dimensional spaces and can handle complex relationships between features

# Neural Networks: Mimic the human brain's structure with interconnected layers of artificial neurons. 
# They're capable of learning highly complex patterns and are 
# widely used in image recognition, natural language processing, and other challenging tasks.

# Algorithms: The Learning Process 

# They power machine learning.
# Algos provide instructions and procedures that guide the model's learning process
# also define how the model extracts patterns from the data, adjusts its internal parameters, and makes predictions.
# Different algorithms use different strategies to achieve their learning objectives

# For instance, a decision tree algorithm recursively partitions the data based on feature values to create a tree-like structure for decision-making. 
# This process continues until the tree reaches a certain depth or the data points within each leaf node are sufficiently similar in terms of their labels.

# In contrast, a neural network algorithm utilizes interconnected layers of artificial neurons to learn complex patterns and representations from the data.
# Each neuron receives inputs from other neurons, performs a weighted sum of these inputs, applies an activation function, and passes the output to the next layer. 

# Overfitting: When Models Learn Too Much 

# where the model becomes excessively specialized in the training data, 
# hindering its ability to generalize to new, unseen data

# To mitigate overfitting: 

# Regularization - adds a penalty term to the model's loss function 
# discouraging it from assigning excessive importance to any single feature or combination of features
# This helps to prevent the model from becoming overly complex and fitting the training data too closely

# Early Stopping - halts the training process when the model's performance on a separate validation set starts to deteriorate

# Cross-validation - a technique that involves dividing the available data into multiple subsets or "folds."
# The model is then trained on a combination of these folds, while its performance is evaluated on the remaining, unseen fold. 
# cross-validation provides a more robust estimate of how well the model is likely to perform on new, unseen data

# IN THE REAL WORLD

# Finance - how do you spot fraud detection?
# formerly a rule-based systems were essentially a set of if-then statements 
# manual reviews were incredibly time-consuming and slow

# Supervised learning algorithm are now trained on vast historical transaction data
# learning to identify patterns and anomalies that indicate fraud
# The algorithm also keeps learning with new transactions

# Customer Experience - supervised learning to predict your next purchase
# Purchase history and demographics

# Unsupervised learning - discovers hidden patterns in customer data, grouping those with similar preferences
# this allows platforms to target rcommendations and and promotions more effectively 

# Self-driving cars - combination of supervised, unsupervised, and even reinforcement learning 
# Supervised learning helps the car recognize objects and understand traffic rules 

# Unsupervised learning helps identify different or new situations by group similar ones together
# Reinforcemnt learning is used to train decision-making system

