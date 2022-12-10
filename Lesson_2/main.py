from character import Character

player1 = Character('Vasya', damage=2)
player2 = Character('Petya', health=50)

print(player1)
print(player2)

while player1.health > 0 and player2.health > 0:
    player1.attack(player2)
    player2.attack(player1)

    print(player1)
    print(player2)