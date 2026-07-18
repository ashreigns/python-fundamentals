def convert_letters(text):
    vowels = "aeıioöuüAEIİOÖUÜ"
    new_text = ""

    for char in text:
        if char in vowels:
            # converts the character to uppercase and appends it to the new variable
            new_text = new_text + char.upper()
        else:
            # converts the character to lowercase and appends it to the new variable
            new_text = new_text + char.lower()
    return new_text

user_text = input("Please enter some text = ")

result = convert_letters(user_text)

print(f"Converted text = {result}")