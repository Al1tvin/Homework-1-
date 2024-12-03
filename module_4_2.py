def test_function():
    def inner_function():
        print('Я в области видимости test_function')

    inner_function()
    print(inner_function)

test_function()
test_function()() # Вызов внутренней функции через внешнюю
inner_function()  # Не можем вызвать inner_function т.к. она находится в локальной области test_function
