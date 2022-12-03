from character import Character

player1 = Character('Vasya', damage=2)
player2 = Character('Petya', health=50)

print(player1)
print(player2)

player1.attack(player2)

print(player1)
print(player2)