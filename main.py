"""
    Main function call for Bookbot, a python program
    which analyzes the contents of novels and prints 
    statistical reports.
"""
import sys
from stats import get_num_words, get_char_dict, list_of_dict, sort_on


if len(sys.argv) != 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)
filepath = sys.argv[1]



def main():
    words = get_num_words(filepath)
    word_count = len(words)
    count_dict = get_char_dict(words)
    list_dict = list_of_dict(count_dict)
    list_dict.sort(reverse=True, key=sort_on)
    print(f"============ BOOKBOT ============\nAnalyzing book found at {filepath}...\n----------- Word Count ----------\nFound {word_count} total words\n--------- Character Count -------")
    for idx in list_dict:
        for key in idx:
            if key.isalpha():
                print(f"{key}: {idx[key]}\n")
    print("============= END ===============")

if __name__ == "__main__" :
    main()
