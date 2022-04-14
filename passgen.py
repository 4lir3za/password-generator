import random
import string
import os

settings = {
    'lower': True,
    'upper': True,
    'symbol': True,
    'number': True,
    'space': False,
    'length': 8,
    'multi': 1,
}

PASSWORD_MIN_LEN = 4
PASSWORD_MAX_LEN = 30
MIN_MULTI = 1
MAX_MULTI = 10


def clear_screen():
    os.system('cls')


def get_yes_or_no_from_user(option, default):
    while True:
        user_input = input(
            f'include {option}? (Default is {default}) ' '(y :YES - n :NO - enter :Set Default): ')

        if user_input == '':
            return default

        if user_input in ['y', 'n']:
            return user_input == 'y'
        print('Invalid Input')


def get_length_from_user(option, default, pw_min_len=PASSWORD_MIN_LEN, pw_max_len=PASSWORD_MAX_LEN):
    while True:
        user_input = input(
            f'(Default {option} is {default}) ' '---enter to set default length---' 'if you want to change Please Enter length your password: ')
        if user_input == '':
            return default
        if user_input.isdigit():
            user_input = int(user_input)
            if pw_min_len <= user_input <= pw_max_len:
                return user_input
            print(
                f'Please Enter a number between {pw_min_len} and {pw_max_len}')
            continue
        print('Please Enter numberic')


def get_total_multiple_pw(option, default, min_multi=MIN_MULTI, max_multi=MAX_MULTI):
    while True:
        user_input = input(
            f'(Default {option} is {default})- ''enter: set default *** enter a number ')

        if user_input == '':
            return default
        if user_input.isdigit():
            user_input = int(user_input)
            if 1 <= user_input <= 10:
                return user_input
            print(
                f'Please Enter a number between {min_multi} and {max_multi}  ')
            continue
        print("Please Enter a number.Please Try Again ")


def generate_password_with_default_settings(finall_settings):
    while True:
        user_input = input(
            'Do you want generate password with default settings? (y: yes n: no enter: yes) ')
        if user_input in ['y', 'n', '']:
            if user_input == 'y' or user_input == '':
                return generat_password(finall_settings)
            else:
                get_setting_from_user(settings)
                print('-*-'*20)
                return generate_password_loop(settings)
                
        print("Please choose(y: yes n: no enter: yes)")


def get_setting_from_user(settings):
    for option, default in settings.items():
        if option != 'length' and option != 'multi':
            settings[option] = get_yes_or_no_from_user(option, default)
        elif option == 'length':
            settings[option] = get_length_from_user(option, default)
        elif option == 'multi':
            settings[option] = get_total_multiple_pw(option, default)


def ascii_upper_case():
    return random.choice(string.ascii_uppercase)


def ascii_lower_case():
    return random.choice(string.ascii_lowercase)


def ascii_number():
    return random.choice(string.digits)


def ascii_symbol():
    return random.choice(string.punctuation)


def generat_password_char(choices):
    rand_choice = random.choice(choices)
    if rand_choice == 'upper':
        return ascii_upper_case()
    if rand_choice == 'lower':
        return ascii_lower_case()
    if rand_choice == 'number':
        return ascii_number()
    if rand_choice == 'symbol':
        return ascii_symbol()
    if rand_choice == 'space':
        return ' '


def generate_password_loop(settings):
    while True:
        generat_password(settings)

        user_input = input(
            'if you want generate passwords again (type-> y or press enter key) else: type-> n ')
        if user_input in ['y', 'n', '']:
            if user_input == 'y' or user_input == '':
                continue
            return
        print('please choose (type-> y or press enter key else: type-> n) ')


def generat_password(finall_settings):
    password_length = finall_settings['length']
    password_multi = finall_settings['multi']
    finall_pw = []
    choices = list(
        filter(lambda x: finall_settings[x] == True, ['lower', 'upper', 'symbol', 'number', 'space']))

    for _ in range(password_multi):
        password = ''
        for _ in range(password_length):
            password += generat_password_char(choices)
        finall_pw.append(password)
    print('generatde passwords:')
    for i, it in enumerate(finall_pw):
        print(i+1, it)


def main():
    clear_screen()
    generate_password_with_default_settings(settings)


main()
