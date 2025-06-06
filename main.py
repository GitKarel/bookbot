import sys
from stats import get_num_words, get_usecount_characters,sorted_character_count_list

# function to return the book contents depending on the file_+path
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


#Function input the request to read the file
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    #book_name = 'frankenstein' -- Removed hardcoded
    path_to_file = sys.argv[1] 

    book_text = get_book_text(path_to_file)
    num_words = get_num_words(book_text)
    character_dictionary = get_usecount_characters(book_text)
    sorted_character_list = sorted_character_count_list(character_dictionary)
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {path_to_file}...')
    print('----------- Word Count ----------')
    print(f'Found {num_words} total words')
    print('--------- Character Count -------')
    for dic in sorted_character_list:
        if dic["char"].isalpha():
                print(f'{dic["char"]}: {dic["count"]}')

    #print(character_dictionary)
    print('============= END ===============')
    #print(book_text)

#Call main
if __name__ == '__main__':
  main()