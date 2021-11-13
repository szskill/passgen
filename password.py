from string import ascii_lowercase, ascii_uppercase, punctuation, digits
from random import choice


def generate_password(length: int = 8, upper_case: bool = True, lower_case: bool = True,
                      numbers: bool = True, symbols: bool = True) -> str:
    password = ''
    last_time_character_type = 'symbol'

    while len(password) < length:
        if last_time_character_type == 'symbol':
            if upper_case:
                password += choice(ascii_uppercase)
            last_time_character_type = 'upper case'
        elif last_time_character_type == 'upper case':
            if lower_case:
                password += choice(ascii_lowercase)
            last_time_character_type = 'lower case'
        elif last_time_character_type == 'lower case':
            if numbers:
                password += choice(digits)
            last_time_character_type = 'number'
        elif last_time_character_type == 'number':
            if symbols:
                password += choice(punctuation)
            last_time_character_type = 'symbol'

    password_characters_list = list(password)
    password = ''
    while password_characters_list:
        random_character = choice(password_characters_list)
        password += random_character
        del password_characters_list[password_characters_list.index(random_character)]

    return password
