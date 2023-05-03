import importlib

import mod_rec_m

for i in range(10):
    importlib.reload(mod_rec_m)

print('fim')
