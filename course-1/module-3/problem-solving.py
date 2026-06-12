# decomposition, is fundamental to tackling any challenging task, whether it's writing a novel, designing a building, or coding a software application.
# it's taking code and breaking it down into step by step to solve for errors
# Functions are the perfect tool for implementing decomposition in code. 

# Embracing Modularity and Testability

def is_valid_tweet_length(tweet_text):
    """Validates the tweet length."""
    if not tweet_text:
        return False # Tweet text cannot be empty
    if len(tweet_text) > 280:
        return False # Tweet text is too long (over 280 characters)
    return True

def are_valid_media_files(media_files):
    """Validates the media files (basic check)."""
    if media_files is None:
        return True  # No media is fine
    elif isinstance(media_files, list):
        return True  # A list of media files is fine for this basic check
    else:
        return False # Anything else is not a valid format
    
# this approach improved maintainability, testability, and reusabikity 

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * (9/5)) + 32
    return fahrenheit 

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) / (5/9)
    return celsius

def convert_temperature(temperature: int, unit: str):
    if unit == "F":
        converted_c = fahrenheit_to_celsius(temperature)
        print(f"{temperature}°F is equal to {converted_c}°C")
        return converted_c
    elif unit == "C":
        converted_f = celsius_to_fahrenheit(temperature)
        print(f"{temperature}°C is equal to {converted_f}°F")
        return converted_f
    else:
        print("Please give a unit of temperature, either in C or F")


