import random


def roll_dice():
    dice_rand = random.randint(1, 6)
    print(f"The dice were rolled, and it landed on {dice_rand}")


roll_dice()
