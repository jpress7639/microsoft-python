# Image augmentation techniques

# Image augmentation - a technique used to artificially expand the size and diversity of an image dataset
# It achieves this by generating modified versions of existing images, 
# introducing subtle or substantial alterations that simulate variations in real-world conditions

# Rotation - By rotating an image from a certain angle, 
# we create a new image that shows the object from a different viewpoint

# Imagine you're training a model to recognize cars
# If your dataset only contains images of cars facing forward, 
# the model might struggle to identify a car viewed from the side

# Flipping 
# mirroring an image horizontally or vertically.
# introduces variations that can improve the model's ability to recognize objects regardless of their orientation

# Cropping 
# selecting a portion of an image and discarding the rest

# First, it can help focus the model's attention on the most relevant part of the image, 
# reducing the influence of background noise

# Second, it can simulate different zoom levels, 
# teaching the model to recognize objects at various scales.

# Brightness adjustments
# Altering the brightness of an image can also be beneficial
# By adjusting the brightness of your training images, 
# you expose the model to a wider range of lighting conditions, 
# making it more robust to changes in illumination

# Augmenting the training data with images of varying brightness can help the model perform well in different lighting conditions.

# Real-world examples:
# Medical field - We can create synthetic medical images to train AI models, making them better at spotting diseases and helping doctors develop new treatments
# Self-driving cars - By creating synthetic images of different driving scenarios, we're training the AI behind these cars to handle all sorts of situations, making them safer and more reliable on the road.

# NOTE: Limitations and considerations
# Using too many augmentation techniques can lead to the creation of images that deviate significantly from reality, potentially confusing the model during training
# t's essential to strike a delicate balance, ensuring that the augmented images remain realistic and representative of the real-world scenarios the model is intended to encounter.