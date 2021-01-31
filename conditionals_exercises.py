# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 00:33:29 2021

@author: Maria Katrantzi
"""
# program to convert temperatures to and from Celcius, Fahrenheit
temp = input("Input the  temperature you like to convert? (e.g., 45F, 102C etc.) : ")
if len(temp)>1:
    degree = int(temp[:-1])
i_convention = temp[-1]

if i_convention.upper() == "C":
  result = round((9 * degree) / 5 + 32)
  o_convention = "Fahrenheit"
  print("The temperature in", o_convention, "is", result, "degrees.")
elif i_convention.upper() == "F":
  result = round((degree - 32) * 5 / 9)
  o_convention = "Celsius"
  print("The temperature in", o_convention, "is", result, "degrees.")
else:
  print("Input proper convention.")
  
# program to count the number of even and odd numbers from a series of numbers
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) # Declaring the tuple
count_odd = 0
count_even = 0
for x in numbers:
        if x % 2 == 0:
    	     count_even+=1
        else:
    	     count_odd+=1
print("Number of even numbers :",count_even)
print("Number of odd numbers :",count_odd)