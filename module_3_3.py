def print_parasm(a = 1, b = 'Строка', c = True):
    print(a,b,c)
print_parasm()
values_list = [12,'str',False]
valuse_dict = {'a' : 20, 'b' : 'Стр' , 'c': True}
print_parasm(*values_list)
print_parasm(**valuse_dict)
values_list_2=['str',10]
print_parasm(*values_list_2)