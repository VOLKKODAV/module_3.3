def print_params(a=1, b='строка', c=True):  # *args **kwargs
    print(a, b, c)


print_params()


def print_params(a, b=28, c=1):
    print(a, b, c)


list_ = [1, 2, 3]
print_params(list_, b=25)


def print_params(a, b, c):
    print(a, b, c)


values_list = [1, 'suck', True]
values_dict = {'a': 7, 'b': False, 'c': 'dick'}
print_params(*values_list)
print_params(**values_dict)


def print_params(a, b, c):
    print(a, b, c)


values_list_2 = [8.5, 'dead']
print_params(*values_list_2, 42)