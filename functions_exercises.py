# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 22:28:40 2021

@author: Maria Katrantzi
"""

# program to find the max of two numbers
def max_of_two(x, y):
    if x > y:
        return x
    return y
print(max_of_two(3,9))

# program to find the max of three numbers
def max_of_three( x, y, z ):
    return max_of_two( x, max_of_two( y, z ) )
print(max_of_three(3, 6, -5))

# program to calculate the factorial of a number 
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Input a number to compute the factiorial : "))
print(factorial(n))

# program to check whether a number is in a given range
def test_range(n):
    if n in range(3,9):
        print( "%s is in the range"%str(n))
    else :
        print("The number is outside the given range.")
test_range(5)