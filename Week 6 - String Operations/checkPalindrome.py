def is_palindrome(sentence):
    # .lower() converts all letters in the sentence to lowercase
    # .replace(" ", "") removes all spaces in the sentence and joins the letters together
    clean_sentence = sentence.lower().replace(" ", "")
    # We reverse the string using the slicing method
    # In Python, [::-1] means read the text backwards from the very end to the beginning
    reversed_sentence = clean_sentence[::-1]
    if clean_sentence == reversed_sentence:
        return True  # If they are the same, return True (meaning it is a palindrome)
    else:
        return False  # If they are different, return False (meaning it is not a palindrome)

print("*-*-*-* Palindrome Sentence Checker *-*-*-*")
user_text = input("Please enter the sentence you want to check = ")

result = is_palindrome(user_text)

if result == True:
    print("The sentence you entered is a palindrome.")
else:
    print("The sentence you entered is not a palindrome.")