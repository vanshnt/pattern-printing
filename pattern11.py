# *
# * *
# *   *
# *     *
# * * * * *


for i in range(5):
    for j in range(i+1):
        if i == 4 or j == 0 or i == j:
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()