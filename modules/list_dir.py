# os.listdir para navegar em caminhos
# \C:\codando 1\Python\modules
import os

path = os.path.abspath('.')
print(path)

for iten in os.listdir(path):
    path_complete = os.path.join(path, iten)
    print(path_complete)
    print(iten)

    if not os.path.isdir(path_complete):
        continue

    for folder in os.listdir(path_complete):
        print(' ', folder)
