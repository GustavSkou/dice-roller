import pandas as pd
import matplotlib.pyplot as plt
from DiceRoller import DiceThrow

def check_times_in_row(num):
    in_row.append(num)
    if len(in_row) < 2:
        pass
    else:
        for item in in_row:
            next_num = in_row.index(item) + 1
            if next_num > len(in_row)-1:
                break
            if item == in_row[next_num]:
                times_in_row.append(1)
                in_row.pop(in_row.index(item))
            else:
                in_row.pop(in_row.index(item))



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
D.dice(
    dice_sides=dice_sides
)
D.roll(
    times_rolled=times_thrown
)
D.throw_dices()

print(DiceThrow.lis_throws)
#DiceThrow.lis_throws.sort()
# print(lis_throws_sorted)

in_row = []
times_in_row = []

for x in DiceThrow.lis_throws:
    check_times_in_row(x)

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
print(len(times_in_row))
fig1, ax1 = plt.subplots()
ax1.pie(data_count, labels=data_labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
