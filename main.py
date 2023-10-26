# Ryan McGlinn


# encodes unencoded password
def encode(password):
    """
    Ryan McGlinn
    """
    encoded_password = ''               # initialize encoded password string
    listed_password = list(password)    # convert password str to list of ints
    for i in listed_password:
        i = int(i) + 3                  # add 3 to each num in list
        if i >= 10:
            i -= 10                     # - 10 if num + 3 is 2 digits
        encoded_password += str(i)      # insert each num into encoded password string
    return encoded_password

def decode(password):
    """
    Ethan Van
    """
    decoded_password = ''
    for i in password: # For each digit
        i = (10 + int(i) - 3) % 10 # Add 10 then subtract 3. Get the remainder of 10
        decoded_password = decoded_password + str(i)
    return decoded_password

if __name__ == '__main__':
    user_menu_choice = None
    while user_menu_choice != 3:        # loop menu
        print('Menu')
        print('-' * 13)
        print('1. Encode\n'
              '2. Decode\n'
              '3. Quit')
        # get menu choice from user
        user_menu_choice = int(input('Please enter an option: '))
        if user_menu_choice == 1:
            # get unencoded password from user
            user_password = str(input('Please enter your password to encode: '))
            encoded_password = encode(user_password)
            print('Your password has been encoded and stored!')
        elif user_menu_choice == 2:
            # get stored encoded and decoded password
            decoded_password = decode(encoded_password)
            print(f'The encoded password is {encoded_password}, and the original password is {decoded_password}.')
