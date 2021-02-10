# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 00:55:19 2021

@author: Maria Katrantzi
"""

# calculator
operator = input("enter operator:")
first_number = input("enter first number:")
second_number = input("enter second number:")
output=""
if (operator=="+"):
    output=int(first_number) + int(second_number)
    print(output)
elif(operator=="-"):
    output=int(first_number) - int(second_number)
    print(output)
elif(operator=="*"):
    output=int(first_number) * int(second_number)
    print(output)
elif(operator=="/"):
    output=int(first_number) / int(second_number)
    print(output)
    
# password validation
x = True
while x: 
    p= input("Input your password:") 
    if (len(p)<6 or len(p)>12):
        print("Invalid Password")
    else:
        print("Valid Password")
        x=False
    
# fizzbuzz challenge
for i in range(0,100):
	if i % 3 == 0 and i % 5 == 0:
		print(str(i) + ': fizz-buzz')
	elif i % 3 == 0:
		print(str(i) + ": Fizz")
	elif i % 5 == 0:
		print(str(i) + ": Buzz")
	else:
		print(i)
        
# time table
for i in range(11):
    for j in range(11):
        print(i*j)
        
# This is a classic "roll the dice" program. 
# We will be using the random module for this,since we want to randomize the numberswe get from the dice. 
# We set two variables (min and max) , lowest and highest number of the dice. 
# We then use a while loop, so that the user can roll the dice again. 
# The roll_again can be set to any value, but here it's set to "yes" or "y", 
# but you can also add other variations to it. s
import random
min = 1
max = 6

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print("Rolling the dices...")
    print("The values are....")
    print(random.randint(min, max))
    print(random.randint(min, max))

    roll_again = input("Roll the dices again?")