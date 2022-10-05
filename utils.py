class InRow:
    lis = [1, 3, 4, 2, 2, 2, 5]
    in_row = []
    times_in_row = []
    times_in_times_in_row = 1

    @staticmethod
    def check_times_in_row(num):
        InRow.in_row.append(num)

        if len(InRow.in_row) < 2:
            pass
        else:
            for item in InRow.in_row:
                next_num = InRow.in_row.index(item) + 1
                if next_num > len(InRow.in_row) - 1:
                    break
                if item == InRow.in_row[next_num]:
                    if InRow.times_in_times_in_row > 0:
                        InRow.times_in_row.append(InRow.times_in_times_in_row)
                        print(InRow.in_row)
                        print(InRow.times_in_times_in_row)
                        print("her")
                    else:
                        InRow.times_in_row.append(1)
                        # in_row.pop(in_row.index(item))
                        InRow.times_in_times_in_row += 1
                else:
                    InRow.in_row.pop(InRow.in_row.index(item))
                    InRow.times_in_times_in_row = 0


R = InRow
for num in R.lis:
    R.check_times_in_row(num)
print(R.times_in_row)
