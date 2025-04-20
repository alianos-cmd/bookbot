def main():
    with open("/home/alianos/projects/github.com/alianos-cmd/bookbot/books/frankenstein.txt") as f:
        text = f.read()
        print(text)

from stats import count_words
from stats import count_characters

counted_characters = count_characters()

# main()
count_words()
print(counted_characters)