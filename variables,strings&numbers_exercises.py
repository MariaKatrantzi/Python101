# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 13:23:39 2021

@author: Maria Katrantzi
"""

#Variables
# Example1:
message = "Hello Python world!" 
print(message) 
# Output:
# Hello Python world! 

# A variable holds a value. You can change the value of a variable at any point.
# Example2:
message = "Hello Python world!" 
print(message)  
message = "Python is my favorite language!" 
print(message) 
# Output: 
# Hello Python world! Python is my favorite language! 

# Example3:
message = "Thank you for sharing Python with the world, Guido!" 
#print(mesage) 
# Output: 
# --------------------------------------------------------------------------- NameError                                 Traceback (most recent call last) /home/ehmatthes/development_resources/project_notes/intro_programming/notebooks/<ipython-input-12-7966723379c3> in <module>()       1 message = "Thank you for sharing Python with the world, Guido!" ----> 2 print(mesage)  NameError: name 'mesage' is not defined

message = "Thank you for sharing Python with the world, Guido!" 
print(message) 
# Output: 
# Thank you for sharing Python with the world, Guido!

#Variable Assignment
# Excersise1:
message="Introduction to Python"
print(message)

# Excersise2:
message="Intro to Python!"
print(message)
message=("Variables")
print(message)

#Changing case
#Example 1:
first_name = 'eric'  
print(first_name) 
print(first_name.title()) 
# Output: 
# eric Eric

#Example 2:
first_name = 'eric'  
print(first_name)  
print(first_name.title()) 
print(first_name.upper()) 

#Combining strings(concatenation)
first_name = 'ada' 
last_name = 'lovelace'  
full_name = first_name + ' ' + last_name  
print(full_name.title()) 
# Output: 
# Ada Lovelace

first_name = 'ada' 
last_name = 'lovelace' 
full_name = first_name + ' ' + last_name  
message = full_name.title() + ' ' + "was considered the world's first computer programmer." 
print(message) 
# Output: 
# Ada Lovelace was considered the world's first computer programmer.

#Whitespace
print("Hello everyone!") 
# Output: 
# Hello everyone!

print("\tHello everyone!") 
# Output: 
# 	Hello everyone!

print("Hello \teveryone!") 
# Output: 
# Hello 	everyone!

# The combination "\n" makes a newline appear in a string. You can use newlines anywhere you like in a string.
print("Hello everyone!") 
# Output: 
# Hello everyone!

print("\nHello everyone!") 
# Output: 
# Hello everyone!

print("Hello \neveryone!") 
# Output: 
# Hello  everyone!

print("\n\n\nHello everyone!") 
# Output: 
#   Hello everyone!

name = ' eric '  
print(name.lstrip()) 
print(name.rstrip()) 
print(name.strip()) 
# Output: 
# eric   eric eric

# It's hard to see exactly what is happening, so maybe the following will make it a little more clear:
name = ' eric '  
print('-' + name.lstrip() + '-') 
print('-' + name.rstrip() + '-') 
print('-' + name.strip() + '-') 
# Output: 
# -eric - - eric- -eric-

#Integers
print(3+2) 
# Output: 
# 5

print(3-2) 
# Output: 
# 1

print(3*2) 
# Output: 
# 6

print(3/2) 
# Output: 
# 1.5 

print(3**2) 
# Output: 
# 9 

# You can use parenthesis to modify the standard order of operations.
standard_order = 2+3*4 
print(standard_order) 
# Output: 
# 14 

my_order = (2+3)*4 
print(my_order) 
# Output: 
# 20 

#Floating numbers
print(0.1+0.1) 
# Output: 
# 0.2 

# However, sometimes you will get an answer with an unexpectly long decimal part:
print(0.1+0.2) 
# Output: 
# 0.30000000000000004 

# This happens because of the way computers represent numbers internally; this has nothing to do with Python itself. Basically, we are used to working in powers of ten, where one tenth plus two tenths is just three tenths. But computers work in powers of two. So your computer has to represent 0.1 in a power of two, and then 0.2 as a power of two, and express their sum as a power of two. There is no exact representation for 0.3 in powers of two, and we see that in the answer to 0.1+0.2.
# Python tries to hide this kind of stuff when possible. Don't worry about it much for now; just don't be surprised by it, and know that we will learn to clean up our results a little later on.
# You can also get the same kind of result with other operations.
print(3*0.1) 
# Output: 
# 0.30000000000000004 