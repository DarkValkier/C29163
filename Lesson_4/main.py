a = 6
b = 'dfgdfgs'

try:
    print(a / b)
except ZeroDivisionError:
    print('На ноль делить нельзя!')
except Exception as error:
    print('Что-то пошло не так:', error)
else:
    pass
finally:
    pass
