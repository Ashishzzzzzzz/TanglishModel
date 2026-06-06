'''
Docstring for transliterate.py
* this file contains functions to transliterate text from one script to another
* this function acesses the words.jsonl file to get the transliteration mappings
* if the word is not found in the words.jsonl file, it will return the original word
* the return will be in string format
'''



import json

def transliterate(text_list):

# load the words.jsonl file
    with open('words.jsonl', 'r') as f:
        mapping = json.load(f)

    # transliterate each word in the list
    transliterated_words = []
    for word in text_list:
        if word in mapping:
            transliterated_words.append(mapping[word])
        else:
            transliterated_words.append(word)

    return transliterated_words
