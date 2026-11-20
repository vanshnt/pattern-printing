#          *
#        * *
#      * * *
#    * * * *
#  * * * * *



# outer loop prints 5 rows
for i in range(1, 6):
    # prints spaces 
    for j in range(5 - i):
        print("", end="  ")

    # prints stars according to the current row number
    for j in range(i):
        print("*", end=" ")
    print()