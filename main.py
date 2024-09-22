from collections import Counter

# Open and read the file
with open('books/frankenstein.txt', 'r') as file:
    content = file.read()

# Split the content into words
words = content.split()

# Count the number of words
word_count = len(words)

# Print the word count
print(f"The number of words in the book is: {word_count}")


# Use Counter to count the frequency of each character
character_count = Counter(content)


# Print the character count
for char, count in character_count.items():
    print(f"'{char}': {count}")
    