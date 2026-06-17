# DETECTING AND REMOVING OUTLIERS 

# Outliers - data points that significantly deviate from the rest of your dataset

# CAUSES
# Measurement errors 
# Typo or incorrect entries 
# Genuine anomalies 

# Z-scores rely on standard deviations are great at identifying outliers 
# IQR - interquartile range - is a measure of how spread out the middle of your data is 

# to find the IQR
# calculate the first quartile, Q1
# the third quartile, Q3
# and the IQR

# OPTIONS TO HANDLE THEM 

# you can trim them - but be cautious, it could be valuable information 

# winzoring - replace them with less extreme values
# imputation - replace them with a estimated value or calculated value (mean or median)

# Perform sensitivity analysis. 
# ​Try running your analysis with and without the outlier ​to see how much they influence the results. 

