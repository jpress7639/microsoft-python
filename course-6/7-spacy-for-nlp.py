# spaCy for NLP: Entity recognition and text classification

# you'll discover how spaCy can automatically pull out key bits of information ​from text, like names, places, dates, and more

# spaCy - an open-source library for advanced Natural Language Processing in Python.
# It comes pre-loaded with various language models and supports tasks like tokenization, part-of-speech tagging, named entity recognition, and text classification.

# NER Model - Named Entity Recognition (NER) is a key feature of spaCy that allows you to identify and classify entities in text, such as names, organizations, dates, and more.
# Text Classification - spaCy also supports text classification, which allows you to categorize text into predefined categories based on its content. This can be useful for tasks like sentiment analysis, topic categorization, and spam detection.

# Steps in the NER Model
# install spaCy using pip
# pip install spacy
# download a language model, for example, the English model
# python -m spacy download en_core_web_sm

# Example usage
# import spacy
# nlp = spacy.load("en_core_web_sm")
# text = "Apple is looking at buying U.K. startup for $1 billion"
# doc = nlp(text)

# Named Entity Recognition
# for ent in doc.ents:
#     print(ent.text, ent.label_)

# Text Classification (if the model supports it) - where spaCy takes a piece of text and puts it in a defined category 
# for token in doc:
#     print(token.text, token.pos_, token.dep_)
