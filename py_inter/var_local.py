# variables -> local & nonlocal
# print(globals())
# def out(x):
#     a = x
#     print(locals())

#     def dent():
#         print(dent.__code__.co_freevars)
#         return a
#     return dent 

# in_1 = out(10)
# in_2 = out(20)
# print(in_1(), in_2())

def concatena(value_init):
    value_fin = value_init

    def interna(value_conc):
        nonlocal value_fin
        value_fin += value_conc
        return value_fin
    return interna

x = concatena('a')
print(x('b'))
print(x('c'))
print(x('d'))

