people = {
    'name': 'vini',
    'surname': 'sant'
}

data = {
    'years_o': 19,
    'hight': 1.85,
}

# (a, b), (c, d) = people.items()
# print(a, b, c, d)

# for key, value in people.items():
#     print(key, value)

complete_people = {**people, **data}


def show_named_args(*args, **kwargs):
    print(f'não nomeado: {args}')

    for key, value in kwargs.items():
        print(key, value)

show_named_args(19, **complete_people)

