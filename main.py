from stats import get_num_words, get_char_count, sort_chars_count
import sys


def get_book_text(filepath):
    file_contents=""
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def report_count_format(char_count):
    list = sort_chars_count(char_count)

    for item in list:
        char = item["char"]
        count = item["count"]
        
        if char.isalpha():
            print(f"{char}: {count}")

def print_book_report(book_url):
    book_content = get_book_text(book_url)
    words = get_num_words(book_content)
    char_count = get_char_count(book_content)

    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {book_url}...")
    print(f"----------- Word Count ----------")
    print(f"Found {words} total words")
    print(f"--------- Character Count -------")
    report_count_format(char_count)
    print(f"============= END ===============")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_url = sys.argv[1]
    print_book_report(book_url)

main()    