'''
Given an integer num, repeatedly add all its digits until the result has only
one digit, and return it.
'''
def add_digits(arg):
    total=0
    for digit in str(arg):
        total+=int(digit)
    if len(str(total))>1:
        add_digits(total)
    else:
        print(total)

num = int(input('Enter a number:'))
add_digits(num)

#When we try to return 'total' and print it from the function it's showing
#'None', ask Why is it happening

'''
This is the other way using 'WHILE' loop

n = int(input("Enter number: "))
temp = n

if len(str(num))<2:
            return num
else:
    temp = num
    while len(str(temp))>1:
        total = 0
        for digit in str(temp):
            total+=int(digit)
        if len(str(total))>1:
            temp = total
        else:
            return total
            break
'''




        
