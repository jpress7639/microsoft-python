# INTEPRETING EVALUATION METRICS IN CONTEXT

# They allow us to measure and understand how well our models are performing
# They also provide insights into the model's strengths and weaknesses

# Contextualizing Specific Problems and Assigning Relevant Metrics

# Choosing the right evaluation metrics begins by understanding the 
# specific problem you're trying to solve and the business goals you're aiming to achieve

# Example: if you're building a customer churn prediction model, 
# your KPIs might include customer retention rate, customer lifetime value, and revenue

# Next, gain a deeper understanding of the data you're working with when assigning metrics. 
# Is your data labeled or unlabeled? Is it balanced or imbalanced? What are the features and target variables? 

# Understanding the data will help you identify potential challenges and choose appropriate metrics.

# For example, if your dataset is imbalanced, you might need to consider metrics to class imbalance, 
# such as precision, recall, and F1-score. 

# Then determine the type of model you're building. 
# Are you building a classification model, a regression model, or something else? 
# NOTE: Classification models typically use metrics like accuracy, precision, recall, and F1-score.
# NOTE: Regression models use metrics like MSE and RMSE. 

# You also need to assess the potential consequences of false positives and false negatives.
# Are there any trade-offs between different metrics? 
# Understanding the risks and trade-offs will help you choose metrics that align with your business priorities.

# Example: in a fraud detection model, the cost of a false negative (missing a fraudulent transaction)
# might be much higher than the cost of a false positive (flagging a legitimate transaction as fraudulent)

# Based on your understanding of the problem, business goals, data, model type, and potential risks, select the metrics that best capture the desired outcomes. 
# It's often helpful to choose a combination of metrics that provide a comprehensive view of the model's performance. 

# Finally, you must continuously monitor the performance of your model using the chosen metrics and iterate on your model development process to improve its performance. 
# This might involve experimenting with different algorithms, feature engineering techniques, or hyperparameter tuning. 

# Identifying and Interpreting Evaluation Metrics

# Selecting the appropriate evaluation metrics requires you to have a deep understanding of the problem at hand and the desired outcomes of solving that problem. 
# It's not a one-size-fits-all scenario. 

# Accuracy - the most straightforward metric - represents the proportion of correct predictions made by the model.
# can be misleading in imbalanced datasets where one class is significantly more prevalent than others
# Formula: Accuracy = (Number of Correct Predctions) / (Total Number of Correct Predictions)


# Precision - focuses on the accuracy of positive predictions
# measuring how many of the identified positive cases were actually correct
# It is important in scenarios where the cost of false positives is high
# Formula: Precision = (True Positives) / (True Positives + False Positives)

# Recall - also known as sensitivity - measures the model's ability to identify all actual positive cases
# quantifies how many of the actual positive cases were correctly predicted by the model
# NOTE: High recall is critical in situations where missing positive cases is unacceptable

# Formula: Recall = (True Positives) / (True Positives + False Negatives)

# F-1 Score - the harmonic mean of precision and recall, providing a balanced measure of the model's performance
# It is particularly useful when you need to consider both precision and recall
# as it penalizes models that perform well in one metric at the expense of the other

# Formula: F1-Score = 2 * (Precision * Recall) / (Precision + Recall)

# ROC-AUC - Receiver Operating Characteristic Area Under the Curve
# evaluates the model's ability to distinguish between positive and negative classes 
# across different classification thresholds
# It plots the true positive rate against the false positive rate at various threshold settings
# A higher ROC-AUC indicates better discrimination, meaning the model is better at separating the two classes.
# NOTE: This metric is particularly useful when you need to assess the overall performance of 
# a model across different operating points, allowing you to choose the optimal threshold based on your specific needs.

# NOTE: The ROC-AUC doesn't have a single, straightforward formula in the same way that Accuracy or Precision do.

# MSE (Mean Squared error) or RMSE (Root Mean Squared Error)
# measure the average squared difference between the predicted and actual values in regression problems
# Lower MSE and RMSE values indicate better model fit, as the predictions are closer to the actual values

# MSE Formula: MSE = (1 / N) * Sum( (actual_value - predicted_value)2 )
# for all data points - where N represents the number of data points.

# RMSE Formula:  RMSE = Square Root ((1 / N) * Sum( (actual_value - predicted_value)2 )) 
# for all data points

# However, the resulting MSE value is in "squared" units (like "dollars squared" for sales figures), which isn't very intuitive for a human to understand.
# which is where RMSE becomes useful - it takes the square root of the MSE, transforms it back the original units of what you're trying to predict
# a much more relatable sense 

# Evaluation metrics are more than just numbers; they are important pieces to machine learning.
# By understanding their significance, contextually interpreting them, 
# and choosing the most relevant metrics for your specific problem, 
# you can build models that not only perform well technically but also deliver real-world value. 

# A low false positive rate shows how to avoid inconveniencing legitimate customers, account lockouts, 
# and even loss of business. The careful calibration is necessary for the model's sensitivity 
# so you can avoid unnecessary disruptions for people that are actual users