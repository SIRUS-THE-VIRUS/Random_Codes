import random


class Enemy:
    life_comp = 2

    def damage_comp(self):

        self.life_comp -= 1

    def check_life(self):
        print("You have ", self.life_comp, "life remaining")
        return self.check_life()


class Player:
    life = 2

    def damage(self):
        self.life -= 1

    def check_life(self):
        print(player_1, " has ", self.life, " life remaining")
        return self.check_life()


def casefunc(user_object, computer_input):
    return{
        (1, 3): True,
        (2, 1): True,
        (3, 2): True,
        (3, 1): False,
        (1, 2): False,
        (2, 3): False,
    }.get((user_object, computer_input))


print("WELCOME TO LASHAWN/'s FIRST PYTHON GAME\n")
player_1 = input("Please enter player 1 name =====>>>> ")
print("\nWelcome ", player_1, "good luck")

enemy1 = Enemy()
player1 = Player()


while not(enemy1.life_comp <= 0) and not(player1.life <= 0):

    print("\nPlease choose below\n")
    print("=======================================")
    print("""1)rock
2)Paper
3)scissors""")
    print("=======================================")

    user_object = int(input())
    computer_input = random.randint(1, 3)
    if computer_input == user_object:
        continue
    if casefunc(user_object, computer_input) is True:
        print("Player 1 you won this round")
        enemy1.damage_comp()
    else:
        print("The enemy has won this round")
        player1.damage()

if enemy1.life_comp <= 0:
    print(player_1, "wins this game of rock paper scissors")
else:
    print("Nice try but Computer has won this game of rock paper scissors")