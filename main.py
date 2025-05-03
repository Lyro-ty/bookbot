from stats import word_count
from stats import character_count
from stats import alphabetize_dict

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = word_count(book_text)
    char_count = character_count(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    alphabetized_report = alphabetize_dict(char_count)
    for letter in alphabetized_report:
        print(f"{letter['char']}: {letter['num']}")
    print("============= END ===============")


main()