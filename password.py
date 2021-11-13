from string import ascii_letters, punctuation, digits
from random import choice


def generate_password(length: int, symbols: bool, numbers: int) -> str:
    char_choices = [*ascii_letters]
    if symbols:
        char_choices.extend(punctuation)
    if numbers:
        char_choices.extend(digits)

    password = ''
    for i in range(length):
        password += choice(char_choices)

    return password
