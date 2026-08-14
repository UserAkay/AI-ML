def count_word_occurrences(filename, word):
    try:
        with open(filename, "r") as file:
            content = file.read()
            word = word.lower()
            count = content.lower().split().count(word)
            print(f"The word '{word}' appears {count} times in '{filename}'.")
    except FileNotFoundError:
        print(f"File '{filename}' not found!")


filename = input("Enter the file name: ")
word = input("Enter the word to count: ")
count_word_occurrences(filename, word)
