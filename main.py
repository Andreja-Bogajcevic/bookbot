def main():
    path_to_book = "./books/frankenstein.txt"

    with open(path_to_book) as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        char_dict = count_chars(file_contents)

        sorted_chars = sorted(char_dict.items(), key=lambda e: e[1], reverse=True)

        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document \n")
        for item in sorted_chars:
            print(f"The '{item[0]}' character was found {item[1]} times")


def count_words(text):
    count = 0

    for word in text.split():
        count += 1

    return count

def count_chars(text):
    dict = {}

    filter_string = "qwertyuiopasdfghjklzxcvbnm"
    for char in text.lower():
        if char in filter_string:
            if char in dict:
                dict[char] += 1
            else:
                dict[char] = 1


    return dict

main()