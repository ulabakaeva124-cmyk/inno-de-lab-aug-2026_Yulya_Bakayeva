#calculator
while True:
    number_1 = input('Введите первое число: ')
    if number_1.isdigit():
        number_1 = float(number_1)
        break
    else:
        print('Введите корректные данные!')
while True:
    number_2 = input('Введите второе число: ')
    if number_2.isdigit():
        number_2 = float(number_2)
        break
    else:
        print('Введите корректные данные!')
while True:
    operation = input('Выберите оператор (*, /, +, -): ')
    if operation in ('*', '/', '+', '-'):
        if operation == '/' and number_2 == 0:
            print('Ошибка!')
            continue
        break
    else:
        print('Введите корректные данные!')
if operation == '*':
    result = number_1 * number_2
elif operation == '/':
    result = number_1 / number_2
elif operation == '+':
    result = number_1 + number_2
elif operation == '-':
    result = number_1 - number_2
print(f'Результат: {number_1} {operation} {number_2} = {result}')
