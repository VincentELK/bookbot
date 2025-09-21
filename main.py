def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = get_number_of_words(book_text)
    print(f"{num_words} words found in the document")

def get_book_text(file_path):
   with open(file_path) as f:
       return f.read()

    


def get_number_of_words(text):
     return len(text.split())

main()
         


