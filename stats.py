def get_num_words(book_file):
    with open(book_file) as f:
        contents = f.read()
        words = contents.split()
        num_words = len(words)
    return num_words

def char_count(book_file):
    with open(book_file) as f:
        contents = f.read()
        l_string = contents.lower()
        char_count = {}
        for char in l_string:
            char_count[char] = 0
        for char in l_string:
            char_count[char] += 1

    return char_count

def sort_on(dict):
    return dict["num"]

def sorted_list(dict):
    sorted_list = []
    for key, value in dict.items():
        sorted_list.append(
            {
                "char" : key,
                "num" : value
             }
            )
        sorted_list.sort(reverse=True,key=sort_on)
    return sorted_list




