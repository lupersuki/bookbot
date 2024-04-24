def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    letter_count = count_letters(text)
    sorted_count = sorted(letter_count.items(), key=lambda item: item[1], reverse=True)

    print(f"--- Begin report of {book_path} ---")
    print(f"{count_words(text)} words found in the document")
    for letter, count in sorted_count:
        if letter.isalpha():
            print(f"The '{letter}' character was found {count} times")

    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = (len(text.split()))
    return words

def count_letters(text):
    letters_dict = {}
    for letter in text:
        lowered = letter.lower()
        if lowered not in letters_dict:
            letters_dict[lowered] = 1
        letters_dict[lowered] += 1
    return letters_dict

def sort_on(dict):
    return dict["num"]

main()
