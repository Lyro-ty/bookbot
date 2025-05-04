import sys
from stats import word_count
from stats import character_count
from stats import alphabetize_dict



def get_book_text(filepath):
    with (open(filepath)) as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    num_words = word_count(book_text)
    char_count = character_count(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    alphabetized_report = alphabetize_dict(char_count)
    for letter in alphabetized_report:
        print(f"{letter['char']}: {letter['num']}")
    print("============= END ===============")


main()