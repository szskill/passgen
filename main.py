from password import generate_password
from argparse import ArgumentParser
from weaknesses import find_weaknesses

parser = ArgumentParser(description='Generates passwords.')
parser.add_argument('--length', '-l', type=int, default=12,
                    help='The length of the password to generate.')
parser.add_argument('--symbols', '-s', default=False, action='store_true',
                    help='Whether to place symbols in the password.')
parser.add_argument('--show-weaknesses', '-w', default=False, action='store_true',
                    help='Whether to show weaknesses of the password.')

args = parser.parse_args()

password = generate_password(args.length, args.symbols)
print(password)

if args.show_weaknesses:
    print()  # newline

    weaknesses = find_weaknesses(password)
    for weakness in weaknesses:
        print(f'Weakness: {weakness.value}.')
