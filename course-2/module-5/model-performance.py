# MODEL EVALUATION 

# Model evaluation is a crucial aspect of machine learning 
# it's the process of rigorously assessing how your machine learning model is doing its job

# BENEFITS OF MODEL EVALUATION

# helps where your model is underperforming or making systematic errors
# Avoid overfitting 
# Choose the best model
# It builds trust in the model

# Common evaluation metrics
# Accuracy - can be misleading though if the classes are inbalanced
# Precision tell you how many positive predictions made by your model were actually correct
# Recall - tells you how many of the positive cases your model was able to idenitfy 
# the F-1 score metric - strikes a balance between precision and recall

# NOTE: The F1-score is the harmonic mean of precision and recall, 
# making it a balanced metric that considers both false positives and false negatives. 
# It's a great choice when you need a single value to represent your model's overall performance.

# Confusion Matrix - a detailed report that shows the number of true positives, true negatives, false positives, and false negatives

# UNRAVELING THE CONFUSION MATRIX 

# serves as a powerful tool in this regard, providing a comprehensive framework 
# to figure out the intricacies of classification model performance

# Unraveling the Confusion Matrix: A Deep Dive into Classification Model Performance

# The confusion matrix would present a 2x2 table, with each of the rows representing the actual classes

# The first quadrant, True Positives (TP)
# shows instances where the model correctly predicts a positive outcome
# e.g. customers who were predicted to make a purchase and actually did make one

# True Negatives (TN)
# shows the instances where the model accurately predicts a negative outcome. 
# e.g. customers who were predicted to not make a purchase and they did not

# False Positives (FP) also referred to as Type I errors
# the model incorrectly predicts a positive outcome
# e.g. customers who were predicted to make a purchased and was incorrect

# False Negatives (FN) - Type II Errors
# represents instances where the model incorrectly predicts a negative outcome
# e.g. customers who surprisingly did make a purchase when looked over initially

# Key Metrics

# Accuracy 
# quantifies the overall proportion of correct predictions made by the model
# it can be deceptive in situations where classes are imbalanced

# Precision 
# shows you the positive predictions made by the model, 
# measuring the proportion of positive predictions that were accurate

# Recall 
# is also known as sensitivity
# It gauges the model's ability to identify all actual positive instances

# The F-1 Score 
# provides a balanced assessment of the model's performance
# particularly valuable when striking a balance between precision and recall is necessary, 
# as it penalizes extreme values in either metric

# NOTE: relevance of each metric is contingent upon the specific problem at hand 
# and the associated costs of different types of errors

# NOTE: it's always important to acknowledge its limitations. 
# It can oversimplify complexities of multi-class classification problems

# visualizing the confusion matrix as a heatmap, 
# where the intensity of color represents the frequency of predictions, 
# can help in identifying patterns and areas of confusion.

# the confusion matrix doesn't explicitly factor in the cost associated with different types of errors, 
# which can be a crucial consideration in certain applications
