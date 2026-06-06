'''
Docstring for transliterate.py
* this file contains functions to transliterate text from one script to another
* this function acesses the words.jsonl file to get the transliteration mappings
* if the word is not found in the words.jsonl file, it will return the original word
* the return will be in string format
'''




import json

def transliterate(word):

    # open the Words.jsonl file 
    with open(r"Words.jsonl" , 'r') as file:
        word_data  = {}
        for line in file:
            data  = json.loads(line)
            word_data.update(data)

    transliterated_words = []
    for w in word:
        if w in word_data:
            transliterated_words.append(word_data[w])
        else:
            transliterated_words.append(w)

    return ' '.join(transliterated_words)