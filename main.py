from stats import get_num_words, get_occurence_words, get_sorted_list
import sys


def get_book_test(file_path):
    try:
        with open(file_path) as f:
            file_contents = f.read()
            return file_contents
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return ""


def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


def main():
    if len(sys.argv) != 2:
        print("Please provide a file path")
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    if not sys.argv[1].endswith(".txt"):
        print("Please provide a .txt file")
        sys.exit(1)
    book = get_book_test(sys.argv[1])
    num_words = get_num_words(book)
    occurence_words = get_occurence_words(book)
    sorted_list = get_sorted_list(occurence_words)
    print_report(sys.argv[1], num_words, sorted_list)


main()
