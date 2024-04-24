def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    print(f"Word count: {count_words(text)}")
    print(count_letters(text))


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

main()
