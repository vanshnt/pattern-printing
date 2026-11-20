# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

 # outer loop prints 5 rows
for i in range(5):
    #inner loop prints numbers upto current row number
    for j in range(1, i+2):
        print(j, end = " ")
    print()