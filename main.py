def main():  
    book_path = "books/frankenstein.txt"
    file_contents = get_book_text(book_path)
    num_words = word_count(file_contents)
    letter_count = count_letters(file_contents)
    sorted_dict_list = sort_dict_list(dictToList(letter_count))
    print(sorted_dict_list)
    #print(f"Words found in document: {num_words}. Letter counts: {letter_count}")

def get_book_text(path): # Open given book file path and return the file as a string
    with open(path) as f:
        return f.read()

def word_count(string):  # Function counts numer of words in document
    words = string.split()
    return len(words)

def count_letters(string):  # Function counts instances of each letter in document and adds them to a list.
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

def dictToList(entryDict):  # loop through char count dictionary and append to a list of dictionaries
    dict_list = []
    for a, b in entryDict.items():
        count_dict = {"character" : a, "count" : b}
        dict_list.append(count_dict)
    return dict_list

def sort_on(entryDict):  # returns the value of 'count' key in given dictionary list
    return entryDict["count"]

def sort_dict_list(dictList): # sorts dict list is descending order
    dictList.sort(reverse=True, key=sort_on)
    return dictList



main()