def main():
    book_path = "books/frankenstein.txt"
    file_contents = get_book_text(book_path)
    num_words = word_count(file_contents)
    print(f"words found in document; {num_words}")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(string):
    words = string.split()
    return len(words)



main()