from Lesson_2.character import Character


class Vampire(Character):
    def __init__(self, name, health=100, damage=1, defence=0):
        Character.__init__(self, name, health, damage, defence)

    def attack(self, target):
        target.take_damage(self.damage)
        self.health += self.damage * 0.1
