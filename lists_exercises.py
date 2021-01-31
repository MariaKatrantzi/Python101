# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 00:15:35 2020

@author: Maria Katrantzi
"""
# program to remove duplicates from a list
a = [10,20,30,20,10,50,60,40,80,50,40]

dup_items = set()
uniq_items = []
for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)

print(dup_items)
print(uniq_items)

dup_items=[10, 20, 30, 50, 60, 40, 80]
uniq_items=[10, 20, 30, 50, 60, 40, 80]

# program to get the difference between two lists
list1 = [1, 2, 3, 4]
list2 = [1, 2]
print(list(set(list1) - set(list2)))

# program to find the index of an item in a specified list
num =[10, 30, 4, -6]
print(num.index(30))

# program to get unique values from a list
my_list = [10, 20, 30, 40, 20, 50, 60, 40]
print("Original List : ",my_list)
my_set = set(my_list)
my_new_list = list(my_set)
print("List of unique numbers : ",my_new_list)

# program to convert a list to a tuple
listx = [5, 10, 7, 4, 15, 3]
print(listx)
#use the tuple() function built-in Python, passing as parameter the list
tuplex = tuple(listx)
print(tuplex)

# program to find the length of a tuple
tuplex = tuple("w3resource")
print(tuplex)
#use the len() function to known the length of tuple
print(len(tuplex))