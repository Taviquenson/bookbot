import sys
from stats import get_num_words, char_analytics, report

def get_book_text(path_to_book):
    with open(path_to_book) as f:
        # f is a file object
        file_contents = f.read()
        return file_contents
 
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_book = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    book_text = get_book_text(path_to_book)
    num_words = get_num_words(book_text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    char_dict = char_analytics(book_text)
    sorted_char_list = report(char_dict)
    for entry in sorted_char_list:
        if entry["char"].isalpha():
            print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")

main()