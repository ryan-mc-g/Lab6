# Ryan McGlinn


# encodes unencoded password
def encode(password):
    encoded_password = ''               # initialize encoded password string
    listed_password = list(password)    # convert password str to list of ints
    for i in listed_password:
        i = int(i) + 3                  # add 3 to each num in list
        if i >= 10:
            i -= 10                     # - 10 if num + 3 is 2 digits
        encoded_password += str(i)      # insert each num into encoded password string
    return encoded_password


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
