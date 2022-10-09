import random
from itertools import groupby

random.seed()


class DiceThrow:
    lis_throws = []
    times_in_row = 0
    ones_times_in_row = 0
    twos_times_in_row = 0
    trees_times_in_row = 0
    fours_times_in_row = 0
    fives_times_in_row = 0
    over_fives_times_in_row = 0

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

    @staticmethod
    def in_row():
        lis = DiceThrow.lis_throws
        grouped_lis = [[k, sum(1 for i in g)] for k, g in groupby(lis)]
        for x in range(len(grouped_lis)):
            DiceThrow.times_in_row = grouped_lis[x][1]
            if DiceThrow.times_in_row == 1:
                DiceThrow.ones_times_in_row = DiceThrow.ones_times_in_row + 1
            elif DiceThrow.times_in_row == 2:
                DiceThrow.twos_times_in_row = DiceThrow.twos_times_in_row + 1
            elif DiceThrow.times_in_row == 3:
                DiceThrow.trees_times_in_row = DiceThrow.trees_times_in_row + 1
            elif DiceThrow.times_in_row == 4:
                DiceThrow.fours_times_in_row = DiceThrow.fours_times_in_row + 1
            elif DiceThrow.times_in_row == 5:
                DiceThrow.fives_times_in_row = DiceThrow.fives_times_in_row + 1
            elif DiceThrow.times_in_row > 5:
                DiceThrow.over_fives_times_in_row = DiceThrow.over_fives_times_in_row + 1

