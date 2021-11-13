from random import choice
from string import ascii_letters, punctuation
from argparse import ArgumentParser


def generate_password(symbols: bool) -> str:
    char_choices = [*ascii_letters]
    if symbols:
        char_choices.extend(punctuation)

    password = ''
    for i in range(args.length):
        password += choice(char_choices)

    return password


parser = ArgumentParser(description='Generates passwords.')
parser.add_argument('--length', '-l', type=int, default=12,
                    help='The length of the password to generate.')
parser.add_argument('--symbols', '-s', default=False, action='store_true',
                    help='Whether to place symbols in the password.')

args = parser.parse_args()

print(generate_password(args.symbols))
