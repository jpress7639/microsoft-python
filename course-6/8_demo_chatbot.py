import spacy

nlp = spacy.load("en_core_web_sm")

def respond_to_user(user_input):
    # Process user input here 
    doc = nlp(user_input) # Process the user input with spaCy's NLP pipeline
    for token in doc: # Print each token and its part-of-speech tag
        print(token.text, token.pos_)

    if "hello" in user_input.lower() or "hi" in user_input.lower():
        response = "Hello! How can I help you today?"
    elif "how are you" in user_input.lower():
        response = "I'm doing well, thank you! How about you?"
    else: 
        response = "I'm still learning. Can you rephrase that?"  # default so response always exists
        for entity in doc.ents:
            if entity.label_ == "PERSON":
                response = f"Ah, you're talking about {entity.text}. What about them?"
            elif entity.label_ == "GPE":
                response = f"{entity.text} is an interesting place!"
            else: 
                response = "I'm still learning. Can you rephrase that?"

    return response

while True:
    user_input = input("You: ")
    response = respond_to_user(user_input)
    print("Chatbot:", response)

# spaCy's natural language processing pipeling:

# Tokenization - breaking down text into individual tokens (words, punctuation, etc.)
# Part-of-speech (POS) Tagging - identifying the grammatical parts of speech for each token in the text (e.g., noun, verb, adjective, etc.)
# Named Entity Recognition (NER) - identifying and classifying named entities in the text, such as names, organizations, dates, and more.

