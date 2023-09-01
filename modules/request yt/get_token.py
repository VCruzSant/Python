from pathlib import Path

token = 'Bearer '

TOKEN_PATH = Path(__file__).parent / 'token.txt'

with open(TOKEN_PATH, 'r', encoding='utf8') as file:
    token += file.read()
