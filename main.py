def main():  
    book_path = "books/book.txt"
    file_contents = get_book_text(book_path)
    if file_contents == None:
        return None
    num_words = word_count(file_contents)
    letter_count = count_letters(file_contents)
    sorted_dict_list = sort_dict_list(dictToList(letter_count))
    print_report(sorted_dict_list, book_path, num_words)
    #print(sorted_dict_list)


def get_book_text(path): # Open given book file path and return the file as a string
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError:
            print("File not found.\nThe program expects a book.txt file located in the 'bookbot/books' directory.")
            return None

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

def print_report(sortedList, bookPath, wordCount):
    print(f"--- Begin report of {bookPath} ---\n{wordCount} words found in the document.\n\n")

    for i in range(0, len(sortedList)):
        singleDict = sortedList[i]
        singleChar = singleDict['character']
        singleCount = singleDict['count']
        print(f"The '{singleChar}' character was found {singleCount} times.")
    print("--- End report ---")



main()