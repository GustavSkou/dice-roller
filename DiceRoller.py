import random

class DiceThrow:
    lis_throws = []

    def __init__(self, sides, rolls):
        self.sides = sides
        self.rolls = rolls

    def roll(self, times_rolled):
        self.rolls = times_rolled

    def dice(self, dice_sides):
        self.sides = dice_sides

    def throw_dices(self):
        for x in range(self.rolls):
            ran_side = random.uniform(1, self.sides+1)
            int_ran_side = int(ran_side)
            DiceThrow.lis_throws.append(int_ran_side)
