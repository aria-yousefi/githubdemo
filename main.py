def encode(password):
    
    password_lst = []
    new_password = ""

    try:
        
        for i in password:
            password_lst.append(i)
        
        for digit in password_lst:
            digit = int(digit)
            digit += 3
            digit = str(digit)
            new_password += digit

        return new_password

        
    except TypeError as exc:
        print(exc)


def print_menu():
    print("Menu\n",
          "-------------\n",
          "1. Encode\n",
          "2. Decode\n",
          "3. Quit\n")



def main():
    
    quit_program = False

    while not quit_program:

        print_menu()

        menu_select = int(input("Please enter an option: "))

        if menu_select == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!\n")

        elif menu_select == 2:
            print(f"The encoded password is {encoded_password}, and the original password is {password}.")

        elif menu_select == 3:
            quit_program = True

if __name__ == "__main__":
    main()