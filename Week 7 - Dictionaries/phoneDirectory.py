def phone_book_program():
    phone_book = {}

    while True:
        print("\n--- PHONE BOOK MENU ---")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Search Contact")
        print("4. List Contacts")
        print("5. Exit")

        choice = input("Please enter the number of the action you want to perform (1-5) = ")

        if choice == "1":
            name = input("Name of the contact to add = ").strip().lower()
            phone = input("Phone number = ").strip()
            phone_book[name] = phone
            print(f"-> {name.capitalize()} successfully added to the phone book.")
        elif choice == "2":
            name = input("Name of the contact to delete: ").strip().lower()
            if name in phone_book:
                del phone_book[name]
                print(f"-> {name.capitalize()} deleted from the phone book.")
            else:
                print("Warning. No contact with this name was found in the phone book!")
        elif choice == "3":
            name = input("Name of the contact to search = ").strip().lower()

            if name in phone_book:
                print(f"-> Found: {name.capitalize()} - Number: {phone_book[name]}")
            else:
                print("No contact with this name is registered in the system.")
        elif choice == "4":
            if not phone_book:
                print("Your phone book is currently empty.")
            else:
                print("Registered Contacts")
                for name, phone in phone_book.items():
                    print(f"- {name.capitalize()}: {phone}")
        elif choice == "5":
            print("Exiting the phone book program. Have a nice day.")
            break
        else:
            print("Invalid. Please enter a number between 1 and 5.")

phone_book_program()