from car import Car, OutOfFuel

car1 = Car(fuel=0)

try:
    car1.go(30)
    car1.go(100)
    car1.go(int(input('Введите расстояние')))
except OutOfFuel:
    print('Топливо закончилось. Движение невозможно.')

print(f'fuel = {car1.fuel}')
print(f'traveled = {car1.traveled}')