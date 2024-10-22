
first = int(input('Введите число: '))
second = int(input('Введите 2-ое число: '))
third = int(input('Введите 3-е число: '))
if first==second==third:
    print('Все', 3, 'числа равны между собой')
elif first==second or second==third or first==third :
    print(2,'числа равны между собой')
else:
    print(0,'равных чисел')
