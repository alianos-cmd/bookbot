
import sys
import os


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book = sys.argv[1]

if not os.path.exists(book):
    print(f"Error: The file '{book}' does not exist.")
    sys.exit(1)



from stats import count_words
from stats import count_characters
from stats import sort
from stats import count_words, count_characters, sort, sort_on


counted_characters = count_characters(book)
word_count = count_words(book)
characters = count_characters(book)         # Call with book passed here
unsorted = sort(characters)                 # Since sort needs characters
unsorted.sort(reverse=True, key=sort_on)


def print_report(word_count, unsorted):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for char_dict in unsorted:
        letter = char_dict["letter"]
        if letter.isalpha(): 
            count = char_dict["count"]
            print(f"{letter}: {count}")

    print("============= END ===============")

# main()
#count_words()
#print(counted_characters)
#print(unsorted)
print_report(word_count, unsorted)