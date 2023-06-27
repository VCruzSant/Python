from contextlib import contextmanager

@contextmanager
def my_open(path_file, mode):
    try:
        print('opening file')
        file = open(path_file, mode, encoding='utf8')
        # função geradora:
        yield file 
        # tem uma pause
        
    except Exception as e:
        print('unknown error')
    finally:
        print('closing file')
        file.close

with my_open('context_manager_lib.txt', 'w') as file:
    file.write('line 1\n')
    file.write('line 2\n')
    file.write('line 3\n')
    print('with', file)