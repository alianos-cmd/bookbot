
def count_words(book):
    with open(book) as f:
        text = f.read()
        split_text = text.split()
        words = len(split_text)
        return words

def count_characters(book):
    with open(book) as f:
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

def sort(characters):
    sorted_list = []
    for character in characters:
        char_dict = {"letter": character, "count": characters[character]}
        sorted_list.append(char_dict)
    return sorted_list
    
def sort_on(dict):
    return dict["count"]