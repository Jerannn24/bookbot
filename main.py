from stats import *
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text

def main(argu):
    text = get_book_text(argu)
    nums = get_num_words(argu)
    dicti = get_num_huruf(argu)
    newList = get_new_dict(dicti)
    #print(nums)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count -----------")
    print(f"Found {nums} total words.")
    print("----------- Character Count -----------")
    for item in newList:
        print(f"{item['char']}: {item['num']}")
    
if len(sys.argv) == 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    argu = sys.argv[1]      
    main(argu)
