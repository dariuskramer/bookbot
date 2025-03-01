import sys

from stats import count_words, count_unique_chars, sort_chars

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

def main(filepath: str):
    contents = get_book_text(filepath)
    count = count_words(contents)
    unique_chars = count_unique_chars(contents)
    sorted_chars = sort_chars(unique_chars)
    printable_chars = [c for c in sorted_chars if c['character'].isalpha()]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")

    for char in printable_chars:
        print(f"{char['character']}: {char['count']}")

    print("============= END ===============")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    main(sys.argv[1])
