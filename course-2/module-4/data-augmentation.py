# DATA AUGMENTATION 
# a technique where we create new, slightly altered versions of our existing data.

# Two common challenges in machine learing 
# Overfitting - when a model learns not just the key patterns in the data, but also the noise or random fluctuations that are specific to the training set.
# Underfitting - when your model is too simple to capture the underlying patterns in new data.

# an overfit model might perform exceptionally well on ​the data it was trained on, but it'll falter when faced with new, unseen data.
# Data augmentation helps us combat overfitting by essentially increasing the size and diversity of our training data.

# Synthetic data - created using various techniques that can generate new, artificial examples that resemble real-world data.

# TEXT AUGMENTATION 
# Synonym replacement - swap out certain words in our text with its synonym 
# "The dog is happy" -> "The canine is joyful"
# NOTE: crucial that the same message is placed

# Back translation - take original text, translate it into another language, and then translate it back 
# useful if you want to introduce paraphrasing-like variations into your data 

# Random insertion or deletion - randomly add or remove words as long as it doesn't take away its meaning 
# teaches the model to be resilient to minor errors and variations 
# NOTE: important to implement safeguards to lead to incorrect or nonsensical sentences 

# Over-augmentation - or too many variations in your data
# it can introduce noise or dilute meaningful patterns

# Search pre-trained word embeddings like sentence transformers 
# to find semantically similar ​words for replacement, 
# adding a layer of meaningfulness to the augmentations.  

# Sentence shuffling - allows you to change the order of sentences within a paragraph or document, 
# ​challenging the model to understand context even when the sequence is altered

# BEST PRACTICES FOR DATA AUGMENTATION 

# you don't have access to an endless supply of images?
# images don't quite capture the full spectrum of variations you might encounter in the real world?
# it's a clever way to stretch your existing dataset
# the transformations, like rotations, flips, crops, and color adjustments - teaching your model to see the world from different angles

# it does have challenges 
# it can introduce bias into your model or lead to overfitting (falter on data outside what it was trained on)

# Importance of Data Augmentation 
# model solely on images of dogs in ideal conditions – 
# well-lit, centered, and facing the camera – 
# it might excel at recognizing dogs in similar scenarios

# Real world is rarely so accomodating 
# The dogs could be partially obscured by objects, in shadows, or captured at odd angles 
# the model's performance can suffer significantly when faced with such variations

# Key principles of effective data augmentation 

# 1. Maintain realistic transformations - staying true to the real-world context of your data 
# Your augmentation should mimic the natural variations you'd expect to see

# 2. Preserve label consistency 
# ensuring the core meaning of your data remains unchanged 

# 3. Balance Augmentation intensity - finding the sweet spot
# too little augmentation might not offer enough variety for your model to learn from 
# while excessive augmentation could lead to overfitting 

# 4. Consider Domain-Specific Augmentations - your augmentations should reflect unique characteristics
# understanding the specific nuances of your domain can lead to more targeted and effective augmentations 

# 5. Start simple, then iterate - a gradual approach to augmentation 
# begin with basic transformation
# as you gain confidence and observe your model's performance - you can experiement with more complex techniques like color jittering (randomly adjusting brightness, contrast, etc.) or adding noise

# Addressing bias and overfitting 
# Data augmentations can inadvertenly introduce bias if transformations disproportionately affect certain classes or groups 
# e.g. if your dataset contains more images of dogs than cats, you might end up with more random crops of dogs - biasing the model towards that class

# Overfitting can occur when the model becomes too familiar with the augmented versions of the training data 

# Real-world scenarios 

# Character Recognition in Historical Documents:
# a model tasked with transcribing these fragile documents. 
# Data augmentation can significantly aid this process

# Speech Recognition in Noisy Environments: 
# bustling city streets to crowded cafes, speech recognition systems often encounter a cacophony of background noise
# Data augmentation can help it filter out the distractions.

