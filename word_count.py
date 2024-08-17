def word_counter(text):
    words = text.split()
    return len(words)
text = input("Enter your text: ")
word_count = word_counter(text)
print("Word count: ", word_count)