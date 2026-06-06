'''
Docstring for clean.py
* this file contains functions to clean the data using regex and other string manipulation techniques.
* here the clean_text() function is defined which takes a string as input and returns a cleaned version of the string.
* the returned will be in lowercase and in list format
* All special characters and numbers will be removed from the string to provide a cleaner version of the text for further processing.
'''

import re

def clean_text(text):
    # Convert the text to lowercase
    text = text.lower()
    
    # Remove special characters and numbers using regex
    cleaned_text = re.sub(r'[^a-z\s]', '', text)
    
    # Split the cleaned text into a list of words
    word_list = cleaned_text.split()
    
    return word_list