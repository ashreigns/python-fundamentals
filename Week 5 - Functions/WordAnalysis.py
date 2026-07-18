def analyze_sentence(sentence):
    # The .split() function splits the sentence by spaces and creates a list of words
    # For example, it turns "Today weather is good" into ["Today", "weather", "is", "good"]
    word_list = sentence.split()
    # The len() function counts how many elements (words) are in this list
    word_count = len(word_list)
    # We open an empty list to store the character count of each word
    char_counts = []
    # We take each word in the word list one by one
    for word in word_list:
        # len(word) counts how many letters that word consists of (e.g., 4 for "good")
        char_count = len(word)
        # We append the character count we found into the list we opened above
        char_counts.append(char_count)
    # When the function finishes, we return both results down below
    return word_count, char_counts

user_sentence = input("Please write a sentence = ")
# Since the function returns two pieces of data, we receive them with two separate variables
count, characters = analyze_sentence(user_sentence)

print(f"Number of words in the sentence = {count}")
print(f"Character counts of the words in the sentence = {characters}")