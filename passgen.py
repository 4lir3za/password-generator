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
}

PASSWORD_MAX_LEN = 4
PASSWORD_MIN_LEN = 30


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


def get_setting_from_user(settings):
    for option, default in settings.items():
        if option != 'length':
            settings[option] = get_yes_or_no_from_user(option, default)
        else:
            settings[option] = get_length_from_user(option, default)


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


def generat_password(finall_settings):
    finall_pw = ''
    choices = list(
        filter(lambda x: finall_settings[x] == True, finall_settings))

    password_length = finall_settings['length']
    for _ in range(password_length):
        finall_pw += generat_password_char(choices)
    print(f'generated password: {finall_pw}')


def main():
    clear_screen()
    get_setting_from_user(settings)
    print('-*-'*20)
    generat_password(settings)


main()
