def get_num_words(book_str):
    words_list = book_str.split()
    return len(words_list)

def char_analytics(book_str):
    char_dict = {}
    for char in book_str:
        char = char.lower() 
        if char not in char_dict:
            char_dict[f"{char}"] = 1
        else:
            char_dict[char] += 1
        # del char_dict[" "] # remove empty space as a character
    return char_dict

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):
    return dict["num"]

def report(char_dict):
    char_list = []
    for char in char_dict:
        char_list.append({"char": char, "num": char_dict[char]})
    char_list.sort(reverse=True, key=sort_on)
    return char_list