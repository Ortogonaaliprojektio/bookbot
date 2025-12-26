from stats import *
import sys
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    print("============ BOOKBOT ============")
    if len(sys.argv)==1: 
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_to_analyze=sys.argv[1]
    print("Analyzing book found at "+book_to_analyze+"...")
    frankenstein=get_book_text(book_to_analyze)
    print("----------- Word Count ----------")
    print(f"Found {wordCount(frankenstein)} total words")
    print("--------- Character Count -------")
    character_map=sortedDictionary(charCount(frankenstein))
    for line in character_map:
        if line["char"].isalpha():
            print(f"{line["char"]}: {line["num"]}")
    print("============= END ===============")
main()