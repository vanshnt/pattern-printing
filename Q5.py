# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# running outer loop to print 5 rows
for i in range(6):
# inner loop prints the current row number i times
    for j in range(i):
        print(i, end = " ")
    print()