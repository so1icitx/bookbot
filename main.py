from stats import book_len,count_char,sort_d
import sys



if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(file_path):
    with open(file_path) as f:
        file_conts = f.read()
        return file_conts

def main():
    book = book_len(get_book_text(sys.argv[1]))
    book_length = len(book)
    print(f'Found {book_length} total words')
    ud = count_char(book)
    od = sort_d(ud)
    for dict in od:
        if dict['char'].isalpha():
            print(f'{dict['char']}: {dict['num']}')
        

main()
