import random

class DiceThrow:
    lis_throws = []
    times_in_row = []
    ones_in_row = []
    twos_in_row = []
    trees_in_row = []
    fours_in_row = []
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
        for item in DiceThrow.lis_throws:
            next = DiceThrow.lis_throws[DiceThrow.lis_throws.index(item)+1]
            next_over = DiceThrow.lis_throws[DiceThrow.lis_throws.index(item)+2]
            next_two_over = DiceThrow.lis_throws[DiceThrow.lis_throws.index(item) + 3]
            if item == DiceThrow.lis_throws[next] and DiceThrow.lis_throws[next] == DiceThrow.lis_throws[next_over] and DiceThrow.lis_throws[next_over] == DiceThrow.lis_throws[next_two_over]:
                DiceThrow.fours_in_row.append(4)
            elif item == DiceThrow.lis_throws[next] and DiceThrow.lis_throws[next] == DiceThrow.lis_throws[next_over]:
                DiceThrow.trees_in_row.append(3)
            elif item == DiceThrow.lis_throws[next]:
                DiceThrow.twos_in_row.append(2)
            else:
                pass
        DiceThrow.times_in_row.append(DiceThrow.twos_in_row)
        DiceThrow.times_in_row.append(DiceThrow.trees_in_row)
        DiceThrow.times_in_row.append(DiceThrow.fours_in_row)
