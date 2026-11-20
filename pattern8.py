# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *


# outer loop prints rows
for i in range(5, 0, -1):

    # prints spaces before the stars to center the pyramid
    for j in range(5 - i):
        print(" ", end=" ")

    # prints odd number of stars in each row 
    for j in range(2 * i - 1):
        print("*", end=" ")
    print()