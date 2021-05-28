'''
Every non-negative integer n has a binary representation.  For example, 5 can be represented as "101" in binary, 11 as "1011" in binary, and so on.  Note that except for n = 0, there are no leading zeroes in any binary representation.

The complement of a binary representation is the number in binary you get when changing every 1 to a 0 and 0 to a 1.  For example, the complement of "101" in binary is "010" in binary.

For a given number n in base-10, return the complement of it's binary representation as a base-10 integer.
'''
import math

n = int(input("Enter the Integer value(n): "))

def complement():
    n_bin = bin(n)
    print('n in Binary form:',n_bin)
    n_bin_cmpl = ''
    for digit in n_bin.split('b')[1]:
            n_bin_cmpl += '0' if digit=='1' else '1'
    
    print('n Binary complement: ',n_bin_cmpl)

    n_int = 0
    i =0
    for digit in n_bin_cmpl[::-1]:
        n_int += int(digit)*math.pow(2,i)
        i+=1

    return(int(n_int))
                

if n>0 and (type(n) is int):
    print('n in integer form:',complement())
else:
    print("You need to enter a positive Integer")

