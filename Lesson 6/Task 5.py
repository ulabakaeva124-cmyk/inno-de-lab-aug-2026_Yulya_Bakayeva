#guess the number
import random
number = random.randint(1,20)
counter = 0
while counter < 5:
    print(f'Я загадал число от 1 до 20. У тебя {5 - counter} попыток.')
    counter += 1
    attempt = int(input(f'Попытка {counter}. Введите число: '))
    if attempt == number:
        print(f'Ты угадал! Отличная работа')
        break
    elif attempt > number:
            print(f'Слишком много! Осталось попыток: {5 - counter}')
    else:
        print(f'Слишком мало! Осталось попыток: {5 - counter}')
else:
    print('Попытки закончились!')
