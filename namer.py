#!/usr/bin/env python3

from nltk.corpus import words
from nltk.tag import pos_tag
from pathlib import Path
import nltk
import string
import json
import random
import sys
import os

# Ensure necessary NLTK data is downloaded
try:
    nltk.download('words')
    nltk.data.find('corpora/words')
except nltk.downloader.DownloadError:
    nltk.download('words')

try:
    nltk.download('averaged_perceptron_tagger_eng')
except nltk.downloader.DownloadError:
    nltk.data.find('taggers/averaged_perceptron_tagger')


def generate_wordlist():
    """Generates and saves JSON files for nouns and adjectives."""
    print('Generating new word files...')
    
    word_list = words.words()
    letter_array = list(string.ascii_lowercase)
    word_array_noun = {letter: [] for letter in letter_array}
    word_array_adjective = {letter: [] for letter in letter_array}

    # Process all words and tag them once
    tagged_words = pos_tag(word_list)

    for word, tag in tagged_words:
        if len(word) > 3 and word[0] in string.ascii_lowercase:
            # Check for adjectives
            if tag in ['JJ', 'JJR', 'JJS']:
                word_array_adjective[word[0]].append(word)
            # Check for nouns
            elif tag in ['NN', 'NNS', 'NNP', 'NNPS']:
                word_array_noun[word[0]].append(word)

    # Write outputs to files
    try:
        with open('nouns.json', 'w') as outfile:
            json.dump(word_array_noun, outfile)
        with open('adjectives.json', 'w') as outfile:
            json.dump(word_array_adjective, outfile)
        print("Word files generated successfully.")
    except IOError as e:
        print(f"Error writing to files: {e}", file=sys.stderr)
        return False

    return True


def get_random_word_pair():
    """Selects and prints a random adjective-noun pair."""
    # Load word lists from files
    try:
        with open('nouns.json', 'r') as json_file:
            word_array_noun = json.load(json_file)
        with open('adjectives.json', 'r') as json_file:
            word_array_adjective = json.load(json_file)
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error loading word files: {e}", file=sys.stderr)
        return

    # Select a random letter from a letter that has words
    available_letters = [
        l for l in string.ascii_lowercase 
        if word_array_adjective[l] and word_array_noun[l]
    ]

    if not available_letters:
        print("No words found for any letter.", file=sys.stderr)
        return

    letter = random.choice(available_letters)

    # Generate and return response
    adjective = random.choice(word_array_adjective[letter])
    noun = random.choice(word_array_noun[letter])
    
    response = [adjective.title(), noun.title()]
    print(' '.join(response))


def main():
    """Main function to run the script."""
    # Check if word files exist, if not, generate them
    if not (Path("nouns.json").is_file() and Path("adjectives.json").is_file()):
        if not generate_wordlist():
            sys.exit(1)
            
    get_random_word_pair()
    sys.exit(0)


if __name__ == "__main__":
    main()
