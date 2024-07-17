def main():
    book_path = "books/frenkenstein.txt"
    greetings(book_path)

    text = get_book_text(book_path)

    num_words = get_num_words(text)
    print_num_words(num_words)

    char_dict = get_num_letters(text)
    sorted_char_dict = sort_dict(char_dict)

    present_results(sorted_char_dict)

    closure()

def closure():
    print("--- End report ---")

def present_results(sorted_dict):
    for item in sorted_dict:
        print(f"The '{item}' character was found {sorted_dict[item]} times")

def sort_dict(mydict):
    mykeys = list(mydict.keys())
    mykeys.sort()
    return {i: mydict[i] for i in mykeys}
    
def print_num_words(num):
    print(f"{num} words found in the document")

def greetings(path):
    print(f"--- Begin report of {path} ---")

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_letters(text):
    letters = {}
    for letter in text.lower():
        if letter not in letters and letter.isalpha():
            letters[letter] = 1
        elif letter.isalpha():
            letters[letter] += 1
    return letters

main()