class Student:
    name = ''
    birth_year = 2000
    group = ''
    avg_mark = 0

    def __init__(self, name, birth_year=2000, group=1, avg_mark=0):
        self.name = name
        self.birth_year = birth_year
        self.group = group
        self.defence = avg_mark

    def __str__(self):
        return f' == {self.name} ==\n' \
            f' Год рождения: {self.birth_year}\n' \
            f' Группа: {self.group}\n' \
            f' Средний балл: {self.avg_mark}\n'

    def get_age(self):
        # Посчитать и вернуть возраст студента на основе его года рождения
        return