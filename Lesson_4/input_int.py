import time

def input_int(message: str):
    while True:
        try:
            result = int(input(message))
        except ValueError:
            print('Вы ввели некорректное значение! Попробуйте ещё раз.')
            # Подождать 5 секунд
            time.sleep(5)
        else:
            return result


a = input_int('Введите первое число:')
b = input_int('Введите второе число:')

print(f'{a} + {b} = {a + b}')

raise Exception('Искусственная ошибка')