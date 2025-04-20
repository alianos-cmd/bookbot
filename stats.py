def count_words():
    with open("/home/alianos/projects/github.com/alianos-cmd/bookbot/books/frankenstein.txt") as f:
        text = f.read()
        split_text = text.split()
        words = len(split_text)
        print(f"{words} words found in the document")

def count_characters():
    with open("/home/alianos/projects/github.com/alianos-cmd/bookbot/books/frankenstein.txt") as f:
        text = f.read()
        characters = list(text.lower())
        character_list = {}
        #print(type(character_list))
        for character in characters:
            if character in character_list:
                character_list[character] += 1
            else:
                character_list[character] = 1

        return character_list


count_characters()