# Python3 program to add two numbers

def Addition():
    global num1,num2
    num1 = 15
    num2 = 12

    # Adding two nos
    sum = num1 + num2
    return sum


# printing values (No Changes)

sum=Addition()
print("Sum of {0} and {1} is {2}" .format(num1, num2, sum))


