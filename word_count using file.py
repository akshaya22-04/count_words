def word_counter(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            words = text.split()
            return len(words)
    except FileNotFoundError:
        print("File not found.")
        return None
file_path = input("Enter the file path:")
word_count = word_counter(file_path)
if word_count is not None:
    print("Word count:", word_count)