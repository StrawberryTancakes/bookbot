from stats import get_num_words
from stats import char_count
from stats import sorted_list
import sys
def main(filepath):
    if len(filepath) != 2:
          print("Usage: python3 main.py <path_to_book>")
          sys.exit(1)
    wordcount = (get_num_words(filepath[1]))
    # print(char_count(filepath))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {wordcount} total words")
    char_list = (sorted_list(char_count(filepath[1])))
    for item in char_list:
            if item["char"].isalpha():
                 print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")

main(sys.argv)



