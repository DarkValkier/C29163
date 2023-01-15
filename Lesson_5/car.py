class OutOfFuel(Exception):
    def __init__(self, message='Not enough fuel to continue driving'):
        Exception.__init__(self, message)


class Car:
    fuel = 0
    fuel_rate = 0.1
    traveled = 0

    def __init__(self, fuel=0, fuel_rate=0.1):
        self.fuel = max(fuel, 0)
        self.fuel_rate = fuel_rate
        self.traveled = 0

    def go(self, distance):
        fuel_required = distance * self.fuel_rate
        if self.fuel < fuel_required:
            # Если топлива не хватает
            raise OutOfFuel()
            pass
        else:
            # Если топлива достаточно
            pass
