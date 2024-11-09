def print_params(a = 1, b = 'Строка', c = True):
    print(a,b,c)
print_params(b = 25)
print_params(c = [1, 2, 3])
values_list = [12,'str',False]
values_dict = {'a' : 20, 'b' : 'Стр' , 'c': True}
print_params(*values_list)
print_params(**values_dict)
values_list_2=['str',10]
print_params(*values_list_2)
