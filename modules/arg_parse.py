# argsparse.ArgumentParser para argumentos mais complexos
# https://docs.python.org/3/howto/argparse.html
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument(
    '-v', '--verbose',
    help='Mostra o help',
    # type=str,
    metavar='Value',
    # valor padrão:
    # default='helow world',
    required=True,
    # Recebe mais de um valor:
    # nargs='+',
    # Recebe mais de um argumento, o type deve ser list:
    action='append',
)

parser.add_argument(
    '-x', '--value_x',
    help='Mostra logs',
    action='store_true'
)
args = parser.parse_args()
print(args.verbose)

if args.verbose is None:
    print('Você não passou o verbo')
else:
    print(f'Seu verbo é: {args.verbose}')

print(args.value_x)
