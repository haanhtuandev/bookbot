from stats import num_of_string, character_frequency, print_report
import sys

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents



def main():
    args = sys.argv
    

    if len(args)<2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path=args[1]
        text = get_book_text(path)
        word_count = num_of_string(text)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        print_report(character_frequency(text))
        print("============= END ===============")


    


main()