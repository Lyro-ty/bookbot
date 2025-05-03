#counts the words in the book
def word_count(book_text):
    book_words = book_text.split()
    return len(book_words)


#text to string then counts characters
def character_count(book_text):
    convert_caps = book_text.lower()
    letters_in_book = {}
    for letter in convert_caps:
        if letter in letters_in_book:
            letters_in_book[letter] += 1
        else:
            letters_in_book[letter] = 1
    return letters_in_book
            