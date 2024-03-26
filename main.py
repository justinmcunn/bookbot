

def main():
    print('--- Begin report of books/frankenstein.txt ---')

    book = read_book('books/frankenstein.txt')

    num_words = get_number_of_words_in_book(book)
    print(f'{num_words} words found in the document')

    letter_count_dict = count_letters(book)

    letter_count_list = list(letter_count_dict.items())
    letter_count_list.sort(reverse=True, key=lambda a: a[1])

    for (k,v) in letter_count_list:
        if k.isalpha():
            print(f"The '{k}' character was found {v} times")
    print('--- End report ---')

def read_book(path):
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        return file_contents
    
def get_number_of_words_in_book(book):
    words = book.split()

    return len(words)

def count_letters(book):
    letter_dict = {}

    lowered_book = book.lower()

    for i in lowered_book:
        if i in letter_dict:
            letter_dict[i] += 1
        else:
            letter_dict[i] = 1
    
    return letter_dict

if __name__ == "__main__":
    main()