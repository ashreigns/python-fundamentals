def count_letters(text):
    tally_sheet = {} # here we created an empty dictionary

    # We take each character in the text one by one
    for character in text:
        # We skip spaces so we don't count them as letters
        if character == " ":
            continue
        # If this letter has been added to the dictionary before (exists in our tally)
        if character in tally_sheet:
            tally_sheet[character] = tally_sheet[character] + 1
        # If we are seeing this letter for the first time (not in our tally)
        else:
            tally_sheet[character] = 1
    return tally_sheet

user_text = input("Please enter some text = ")

result = count_letters(user_text)

print(f"Statistical result of the text = {result}")