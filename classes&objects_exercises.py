# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 17:00:35 2021

@author: Maria Katrantzi
"""

# program that computes the area of a rectangle
class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def rectangle_area(self):
        return self.length*self.width
    
newRectangle = Rectangle(12, 10)
print(newRectangle.rectangle_area())

# program that accepts a string from the user and prints it in upper case
class IOString():
    def __init__(self):
        self.str1 = ""

    def get_String(self):
        self.str1 = input("Input String: ")

    def print_String(self):
        print(self.str1.upper())

str1 = IOString()
str1.get_String()
str1.print_String()

# program that gives users the ability to select a password's strength and length, 
# then generate a random password for them
import random
import string
class passgen:
	#initialize lists using string library
	def __init__(self, password = "", alphabet=list(string.ascii_letters), alphnum=(list(string.ascii_letters)+list(string.digits)), printable=(list(string.ascii_letters)+list(string.digits) + ['!', '@', '#', '$', '%', '^', '&', '*', "(", ')']) ): 
		self.alphabet = alphabet 
		self.alphnum = alphnum
		self.printable = printable
		self.password = password
	def weak(self, length):
		password = ""
		for i in range(length):
			password += random.choice(self.alphabet)
		self.password = password
		return password
	def fair(self, length):
		password = ""
		for i in range(length):
			password += random.choice(self.alphnum)
		self.password = password
		return password
	def strong(self, length):
		password = ""
		for i in range(length):
			password += random.choice(self.printable)
		self.password = password
		return password
	def choose(self):
		length = int(input('Enter Desired Password Length: ')) #allows user to pick password length
		strength = int(input('Select Desired Password Strength:\n 1: Weak\n 2: Fair\n 3: Strong\n Selection: ')) #allows user to pick password strength
		if strength == 1: #checks what the user picked for strength then calls appropriate method
			self.weak(length)
		elif strength == 2:
			self.fair(length)
		elif strength == 3:
			self.strong(length)
		else: # if they entered something invalid tell them they can't
			print('invalid selection')
			self.choose() # run the function again. this is optional and can be replaced with an end of program

a = passgen()
a.choose()
print(a.password)
