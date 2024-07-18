import random

def password_generator():
    pass_1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
                '-', '_', ',', ';', '.', ':', '!', '?', '…', '^', '`', '+', '"', '*', '#', '¶', 'Ç', '%', 'ç', '&', '/',
                '(', ')', '=', '[', ']', '|', '{', '}', 'à', 'ä', 'ö', 'é', '¨', '$', '£', '<', '>', '«', '@', '§', 'æ',
              '¢', '≤', '≥', '¥', '≈', '©', '~', '√', 'è', 'ü', '“', '±', '≠', '¿', '´', 'µ', '~', '∞', 'Ò', 'Ô', 'Ú',
              '∏', 'ÿ', '˚', '◊', '•']
    password = ""
    inp = input("Choose the length of your password (integer) : ")
    for x in range(int(inp)): 
        password = password + random.choices(pass_1)[0]
    
    pass_len = len(password)
    print(f"\nYour new password is :\n\n {password}\n")
    print(f"{pass_len} characters")
    save_to_file(password)
    return password

def save_to_file(password):
    save = input("Do you want to save this password ? (y/n) : ")
    if save == "y":
        file_path = "/Output/File/Path/"
        file_name = input("Enter the name of the file to save : ")
        if not file_name.endswith(".txt"):
            file_name = file_name + ".txt"
        try:
            with open(file_path + file_name, "w") as file:
                file.write(str(password))
            print(f"Password saved in file {file_name}")
            another_action()
        except IOError:
            print("Error : An error occurred while saving the file.")
    elif save == "n":
        another_action()
    else:
        print("Error : Incorrect choice. Please enter 'y' for yes or 'n' for no.")
        save_to_file(password)


def another_action():
    choice = input("Do you want to generate a new password ? (y/n) : ")
    if choice == "y":
        password_generator()
    elif choice == 'n':
        print("\nSee you soon !")
    else:
        print("Error : Incorrect choice. Please enter 'y' for yes or 'n' for no.")
        another_action()


password_generator()

