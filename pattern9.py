#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *

#mixed 7th and 8th to print diamond

for i in range(1, 6):

    # prints spaces before the stars to center the pyramid
    for j in range(5 - i):
        print(" ", end=" ")

    # prints odd number of stars in each row 
    for j in range(2 * i - 1):
        print("*", end=" ")
    print()
for i in range(4, 0, -1):

    # prints spaces before the stars to center the pyramid
    for j in range(5 - i):
        print(" ", end=" ")

    # prints odd number of stars in each row 
    for j in range(2 * i - 1):
        print("*", end=" ")
    print()