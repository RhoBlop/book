def main():
    path_to_book = "/home/thisnow/workspace/projects/bootdev/bookbot/books/frankenstein.txt"

    with open(path_to_book, mode="r", encoding="utf-8") as f:
        content = f.read()
        num_words = count_words(content)
        num_per_char = count_chars_dict(content)

        print(f" --- Begin Report of {path_to_book.split("/")[-1]} ---")
        print(f"{num_words} words found in the document")
        for char in sorted(num_per_char.keys()):
            if char.isalpha():
                print(repr(f"The {char} character was found {num_per_char[char]} times"))
                
        print("--- End Report ---")

def count_words(string):
    return len(string.split())

def count_chars_dict(string):
    chars_dict = {}
    for char in string:
        char = char.lower()
        chars_dict[char] = chars_dict.get(char, 0) + 1

    return chars_dict
    
if __name__ == "__main__":
    main()