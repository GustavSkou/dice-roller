import pandas as pd
import matplotlib.pyplot as plt
from DiceRoller import DiceThrow

ones = []
twos = []
trees = []
fours = []
fives = []
sixes = []

fig, ax = plt.subplots()

side = input("how many sides does your dice have? ")
thro = input("how many times are you throwing your dice? ")
dice_sides = int(side)
times_thrown = int(thro)


D = DiceThrow(rolls=times_thrown, sides=dice_sides)
D.dice(dice_sides=dice_sides)
D.roll(times_rolled=times_thrown)
D.throw_dices()
D.in_row()
print(DiceThrow.lis_throws)
print(D.twos_in_row)
print(D.trees_in_row)
print(D.fours_in_row)

for x in DiceThrow.lis_throws:
    if x == 1:
        ones.append(x)
    elif x == 2:
        twos.append(x)
    elif x == 3:
        trees.append(x)
    elif x == 4:
        fours.append(x)
    elif x == 5:
        fives.append(x)
    elif x == 6:
        sixes.append(x)

data = [[1, len(ones), len(ones) / len(DiceThrow.lis_throws)],
        [2, len(twos), len(twos) / len(DiceThrow.lis_throws)],
        [3, len(trees), len(trees) / len(DiceThrow.lis_throws)],
        [4, len(fours), len(fours) / len(DiceThrow.lis_throws)],
        [5, len(fives), len(fives) / len(DiceThrow.lis_throws)],
        [6, len(sixes), len(sixes) / len(DiceThrow.lis_throws)]]

data_count = []
data_labels = []

for n in range(6):     # [list][item]
    data_count.append(data[0+n][1])
    data_labels.append(data[0+n][0])

# print(data)
# print(data_count)
# print(data_labels)

df = pd.DataFrame(data, columns=['side', 'count', 'pro'])
print(df)
fig1, ax1 = plt.subplots()
ax1.pie(data_count, labels=data_labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
