# A file that contains functions for analyzing the text.

def sort_on(items):
    return items["num"]

def get_num_words(file_contents):
    print("----------- Word Count ----------")

    # Split text into set of words.
    words = file_contents.split()
    count = len(words)

    # Output Message.
    print(f"Found {count} total words")

    return count

def get_num_chars(file_contents):
    print("--------- Character Count -------")

    # Variables.
    chars = []

    # Make file contents lower case.
    contents = file_contents.lower()

    # Loop through Ascii characters.
    for i in range(33, 96):
        # Get number of times character is used in text.
        chars.append({"name": chr(i).lower(), "num": contents.count(chr(i).lower())})

    # Order Dictonary Set.
    chars.sort(reverse=True, key=sort_on)

    # Output Message.
    for i in range(0, len(chars)):
         print(f"{chars[i]["name"]}: {chars[i]["num"]}")

    return chars
