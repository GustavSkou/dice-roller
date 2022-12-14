import pandas as pd
import matplotlib.pyplot as plt
from DiceRoller import DiceThrow

ones = 0
twos = 0
trees = 0
fours = 0
fives = 0
sixes = 0

over = ">5"

side = input("how many sides does your dice have? ")
thro = input("how many times are you throwing your dice? ")
dice_sides = int(side)
times_thrown = int(thro)

D = DiceThrow(rolls=times_thrown, sides=dice_sides)
D.dice(dice_sides=dice_sides)
D.roll(times_rolled=times_thrown)
D.throw_dices()
D.in_row()

for x in DiceThrow.lis_throws:
    if x == 1:
        ones = ones + 1
    elif x == 2:
        twos = twos + 1
    elif x == 3:
        trees = trees + 1
    elif x == 4:
        fours = fours + 1
    elif x == 5:
        fives = fives + 1
    elif x == 6:
        sixes = sixes + 1

data = [["1", ones, ones / len(DiceThrow.lis_throws) * 100, "1", DiceThrow.ones_times_in_row, DiceThrow.ones_times_in_row / len(DiceThrow.lis_throws) * 100],
        ["2", twos, twos / len(DiceThrow.lis_throws) * 100, "2", DiceThrow.twos_times_in_row, DiceThrow.twos_times_in_row / len(DiceThrow.lis_throws) * 100],
        ["3", trees, trees / len(DiceThrow.lis_throws) * 100, "3", DiceThrow.trees_times_in_row, DiceThrow.trees_times_in_row / len(DiceThrow.lis_throws) * 100],
        ["4", fours, fours / len(DiceThrow.lis_throws) * 100, "4", DiceThrow.fours_times_in_row, DiceThrow.fours_times_in_row / len(DiceThrow.lis_throws) * 100],
        ["5", fives, fives / len(DiceThrow.lis_throws) * 100, "5", DiceThrow.fives_times_in_row, DiceThrow.fives_times_in_row / len(DiceThrow.lis_throws) * 100],
        ["6", sixes, sixes / len(DiceThrow.lis_throws) * 100, ">5", DiceThrow.over_fives_times_in_row, DiceThrow.over_fives_times_in_row / len(DiceThrow.lis_throws) * 100],
        ["",
         ones + twos + trees + fours + fives + sixes,
         ones / len(DiceThrow.lis_throws) + twos / len(DiceThrow.lis_throws) + trees / len(DiceThrow.lis_throws) + fours / len(DiceThrow.lis_throws) + fives / len(DiceThrow.lis_throws) + sixes / len(DiceThrow.lis_throws),
         "",
         DiceThrow.ones_times_in_row + DiceThrow.twos_times_in_row + DiceThrow.trees_times_in_row + DiceThrow.fours_times_in_row + DiceThrow.fives_times_in_row,
         ""]]

df = pd.DataFrame(data, columns=['Side', 'Count', 'pro', 'In row', 'count', 'pro'])
print(df)

# creating pie chart for rolls
data_count = []
data_labels = []
for n in range(6):  # [list][item]
    data_count.append(data[n][1])
    data_labels.append(data[n][0])

fig1, ax1 = plt.subplots()
ax1.pie(data_count, labels=data_labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')

# Creating chart for in row rolls
data_count2 = []
data_labels2 = []
for n in range(6):  #    [list][item]
    data_count2.append(data[n][4])
    data_labels2.append(data[n][3])

fig2, ax2 = plt.subplots()
ax2.bar(data_labels2, data_count2)

plt.show()
