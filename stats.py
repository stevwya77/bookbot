""" 
    This file contains functions for analyzing the text 
"""


# read and split text in file, print word count
def get_num_words(filepath):
    # read contents of book
    with open(filepath) as f:
        contents = f.read()
        # separate words, get count
        words = contents.split()
        num_words = len(words)
        return words


# set word to lowercase, store in dictionary, return counts per character
def get_char_dict(words):
    char_count = {}
    for word in words:
        word = word.lower()
        for char in word:
            if char not in char_count:
                char_count[char] = 0    
            char_count[char] += 1
    return char_count

def list_of_dict(char_count):
    list_dict = []
    for char, count in char_count.items():
        new_dict = {}
        new_dict[char] = count
        list_dict.append(new_dict)
    return list_dict

def sort_on(list_dict):
    for idx in list_dict:
        return list_dict[idx]
