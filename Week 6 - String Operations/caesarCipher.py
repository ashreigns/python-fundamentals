def caesar_cipher(text, shift_amount):
    cipher_text = ""

    for char in text:
        if char.isupper():
            # ord(char) - ord('A') finds the position of the letter in the alphabet (A=0, B=1, Z=25)
            # shift_amount shifts it forward by the specified number
            # % 26 ensures that when it reaches the end of the alphabet (past Z), it wraps back to the beginning
            # + ord('A') converts it back to the ASCII number value that the computer understands
            new_ascii = (ord(char) - ord('A') + shift_amount) % 26 + ord('A')
            # The chr() function converts the ASCII number back into a character
            cipher_text = cipher_text + chr(new_ascii)
        elif char.islower():
            # We perform the same operations basing them on the lowercase 'a'
            new_ascii = (ord(char) - ord('a') + shift_amount) % 26 + ord('a')
            cipher_text = cipher_text + chr(new_ascii)
        else:
            cipher_text = cipher_text + char

    return cipher_text

user_text = input("Enter the text you want to encrypt = ")
number = int(input("How many letters should it be shifted (Enter a number) = "))

result = caesar_cipher(user_text, number)

print(f"Encrypted text = {result}")