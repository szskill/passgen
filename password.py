from string import ascii_letters, punctuation
from random import choice


def generate_password(length: int, symbols: bool) -> str:
    char_choices = [*ascii_letters]
    if symbols:
        char_choices.extend(punctuation)

    password = ''
    for i in range(length):
        password += choice(char_choices)

    return password
