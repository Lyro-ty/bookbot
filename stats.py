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
            

#sort function
def sort_on(num):
    return num["num"]

#return sorted list/counts convert to list
def alphabetize_dict(letters_in_book):
    letter_report = []
    for letter in letters_in_book:
        if letter.isalpha():
            letter_report.append({"char": letter, "num": letters_in_book[letter]})
    letter_report.sort(reverse=True, key=sort_on)
    return letter_report