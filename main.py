# The entry point to our program and any code that doesn't fit elsewhere.

import sys

from stats import get_num_words, get_num_chars

def get_book_text(path_to_file):
    print(f"Analyzing book found at {path_to_file}")

    # Get File Contents.
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents

def main():
    print("============ BOOKBOT ============")

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(sys.argv[1])
    num_words = get_num_words(book_text)
    num_chars = get_num_chars(book_text)

    print("============= END ===============")

main()
