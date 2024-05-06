def main():
    book_path = "books/frankenstein.txt"
    file_contents = get_book_text(book_path)
    num_words = word_count(file_contents)
    letter_count = count_letters(file_contents)
    #print(f"Words found in document: {num_words}. Letter counts: {letter_count}")
    
    print(f"word count: {num_words}, character dictionary: {letter_count}")
    
    
    

def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(string):
    words = string.split()
    return len(words)

def count_letters(string):
    lowered_string = string.lower()
    string_words = list(lowered_string)
    wordcount_dictionary = {}
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for b in letters:
        letterCounter = 0
        for i in range(0, len(string_words)):
            if b == string_words[i]:
                letterCounter += 1
        wordcount_dictionary[b] = letterCounter
        
    return wordcount_dictionary





main()