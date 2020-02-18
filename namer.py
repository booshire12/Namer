#!/usr/bin/env python3

from nltk.corpus import words
from nltk.tag import pos_tag
from pathlib import Path
import nltk
import string
import json
import random
import os

def generate_wordlist():
    # Generate Lists of Nouns and Adjectives
    word_list = words.words()
    letter_array = list(string.ascii_lowercase)
    word_array_noun = dict()
    word_array_adjective = dict()

    for letter in letter_array:
        word_array_noun[letter] = []
        word_array_adjective[letter] = []
        
        for word in word_list:
            if word.startswith(letter) and len(word) > 3:
                if pos_tag([word])[0][1] in ['JJ', 'JJR', 'JJS']:
                    word_array_adjective[letter].append(word)
                elif pos_tag([word])[0][1] in ['NN', 'NNS', 'NNP', 'NNPS']:
                    word_array_noun[letter].append(word)

    # Write outputs to files
    with open('nouns.json', 'w') as outfile:
        json.dump(word_array_noun, outfile)
    with open('adjectives.json', 'w') as outfile:
        json.dump(word_array_adjective, outfile)
    
    return(True)


# Generate word files if they do not exist
if not Path("nouns.json").is_file() or not Path("adjectives.json").is_file():
    print('Generating new word files')
    generate_wordlist()

# Import word lists generated from generate_wordlist.py
noun_file = open('nouns.json', 'r')
adjective_file = open('adjectives.json', 'r')

with open('nouns.json') as json_file:
    word_array_noun = json.load(json_file)

with open('adjectives.json') as json_file:
    word_array_adjective = json.load(json_file)


# Select random letter
letter_array = list(string.ascii_lowercase)
letter = random.choice(letter_array)

response = [
    random.choice(word_array_adjective[letter]),
    random.choice(word_array_noun[letter]),
]

print(' '.join(response))
