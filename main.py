def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def word_count(book_text):
    book_words = book_text.split()
    return len(book_words)


def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = word_count(book_text)
    print(f"{num_words} words found in the document")


main()