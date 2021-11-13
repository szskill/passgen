from enum import Enum
from string import punctuation
from typing import List


class Weaknesses(Enum):
    LESS_THAN_8_CHARS = 'Less than 8 characters'
    NO_LOWERCASE_LETTERS = 'No lowercase letters'
    NO_UPPERCASE_LETTERS = 'No uppercase letters'
    NO_NUMBERS = 'No numbers'
    NO_SYMBOLS = 'No symbols'


def find_weaknesses(password: str) -> List[Weaknesses]:
    weaknesses = []

    lowercase_letter_found = False
    uppercase_letter_found = False
    number_found = False
    symbol_found = False

    if len(password) < 8:
        weaknesses.append(Weaknesses.LESS_THAN_8_CHARS)

    for letter in password:
        if letter.islower():
            lowercase_letter_found = True
        elif letter.isupper():
            uppercase_letter_found = True
        elif letter.isnumeric():
            number_found = True
        elif letter in punctuation:
            symbol_found = True

    if not lowercase_letter_found:
        weaknesses.append(Weaknesses.NO_LOWERCASE_LETTERS)
    if not uppercase_letter_found:
        weaknesses.append(Weaknesses.NO_UPPERCASE_LETTERS)
    if not number_found:
        weaknesses.append(Weaknesses.NO_NUMBERS)
    if not symbol_found:
        weaknesses.append(Weaknesses.NO_SYMBOLS)

    return weaknesses
