# Define a function to read and process the text file
def count_unique_words(filename):
    # Create an empty dictionary to store word frequencies
    word_count = {}

    # Open the file in read mode
    with open(filename, 'r') as file:
        # Read each line in the file
        for line in file:
            # Split the line into words using space as a separator
            words = line.split()
            for word in words:
                # Remove punctuation and convert to lowercase to ensure accurate counting
                cleaned_word = word.strip('.,!?()[]{}":;')
                cleaned_word = cleaned_word.lower()

                # Update the word count in the dictionary
                if cleaned_word:
                    if cleaned_word in word_count:
                        word_count[cleaned_word] += 1
                    else:
                        word_count[cleaned_word] = 1

    return word_count

# Specify the path to your text file
file_path = 'new.txt'

# Call the function to count unique words and their occurrences
word_count = count_unique_words(file_path)

# Print the results
for word, count in word_count.items():
    print(f'{word}: {count}')
