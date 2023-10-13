import re
# ^ -> começa com | $ -> termina com
NUM_OR_NOT_REGEX = re.compile(r'^[0-9.]$')


def isNumOrNot(string: str):
    return bool(NUM_OR_NOT_REGEX.search(string))


def isEmpty(string: str):
    return bool(string == '')
