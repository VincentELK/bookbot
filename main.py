from stats import get_number_of_words
from stats import num_of_char
from stats import sort_dictionary

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = get_number_of_words(book_text)
    num_char = num_of_char(book_text)
    list_char_sorted = sort_dictionary(num_char)
    print(f"Found {num_words} total words")
    
    for dict_list in list_char_sorted:
        num = None
        char = ""
        for key in dict_list:
            if key == "char":
                char = dict_list[key]
        for key in dict_list:
            if key == "num":
                num = dict_list[key]           
        print(f"{char}: {num}")

def get_book_text(file_path):
   with open(file_path) as f:
       return f.read()

    




main()
         


