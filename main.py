from collections import Counter as c

def text_opener(book_path):
    with open(book_path) as f:
        file_contents = f.read()
        return file_contents

def word_count(file_contents):
    words = len(file_contents.split())
    return words

def each_word_count(file_contents):
    l = list()
    for i in file_contents:
        i = i.lower()
        l.append(i)
    count = c(l)
    return count

def report(file_contents, word_count):
    print("--- Begin report of books/frankenstein.txt ---")
    print(str(word_count) + " words found in the document\n\n")
    for i in file_contents:
        print("The \'" + str(i) + "\' character was found " + str(file_contents[i]) +" times" )
    print("--- End report ---")

def main():
    book_path = 'books/frankenstein.txt'
    file_contents = text_opener(book_path)
    print(file_contents)
    word_count1 = word_count(file_contents)
    print("The following book contains " + str(word_count1) + " words\n")
    unique_word_count = each_word_count(file_contents)
    report(unique_word_count, word_count1)


if __name__ == '__main__':
    main()

