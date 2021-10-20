"""
File: class_reviews.py
Name:黃稚程 mike
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your program should be case-insensitive.
If the user input -1 for class name, your program would output
the maximum, minimum, and average among all the inputs.
"""
EXIT = '-1'


def main():
    """
    This function will individually calculate max, min, average of score of the two class, SC001 and SC101.
    """
    a = input("Which class? ")
    a = a.upper()
    Max001 = 0
    Min001 = 101
    Total001 = 0
    number001 = 0
    Max101 = 0
    Min101 = 101
    Total101 = 0
    number101 = 0
    while a != EXIT:
        b = int(input("Score: "))
        if a == "SC001":
            number001 += 1
            Total001 += b
            if b >= Max001:
                Max001 = b
            if b < Min001:
                Min001 = b
        if a == "SC101":
            number101 += 1
            Total101 += b
            if b >= Max101:
                Max101 = b
            if b < Min101:
                Min101 = b
        a = input("Which class? ")
        a = a.upper()
    if number001 == 0 and number101 == 0:
        print("No class scores were entered")
    else:
        if number001 != 0:
            print("==========================SC001==========================")
            print("Max (001): "+str(Max001))
            print("Min (001): "+str(Min001))
            avg001 = Total001 / number001
            print("Avg (001): "+str(avg001))
        else:
            print("==========================SC001==========================")
            print("No score for SC001")
        if number101 != 0:
            print("==========================SC101==========================")
            print("Max (101): " + str(Max101))
            print("Min (101): "+str(Min101))
            avg101 = Total101 / number101
            print("Avg (101): " + str(avg101))
        else:
            print("==========================SC101==========================")
            print("No score for SC101")




#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
