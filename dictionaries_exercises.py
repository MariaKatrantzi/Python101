# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 16:51:50 2021

@author: Maria Katrantzi
"""

# program to check whether a given key already exists in a dictionary
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(x):
  if x in d:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
is_key_present(5)
is_key_present(9)

# program to iterate over dictonaries using for loops. Print keys and values of dictionary
d = {'x': 10, 'y': 20, 'z': 30} 
for dict_key, dict_value in d.items():
    print(dict_key,'->',dict_value)
    
# program to print a dictionary where the keys are numbers between 1 and 15 (both included)
# and the values are square of keys
d=dict()
for x in range(1,16):
    d[x]=x**2
print(d)  

# program to multiply all the items in a dictionary 
my_dict = {'data1':100,'data2':-54,'data3':247}
result=1
for key in my_dict:    
    result=result * my_dict[key]
print(result)

# program to add a key to a dictionary
d = {0:10, 1:20}
print(d)
d.update({2:30})
print(d)

# program to remove a key from a dictionary
myDict = {'a':1,'b':2,'c':3,'d':4}
print(myDict)
if 'a' in myDict: 
    del myDict['a']
print(myDict)

# program to check if a dictionary is empty or not 
my_dict = {}
if not bool(my_dict):
    print("Dictionary is empty")
    
# program to remove duplicates from a dictionary
student_data = {'id1': 
   {'name': ['Sara'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id2': 
  {'name': ['David'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id3': 
    {'name': ['Sara'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id4': 
   {'name': ['Surya'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
}
result = {}
for key,value in student_data.items():
    if value not in result.values():
        result[key] = value
print(result)
    
# program to match key values in two dictionaries
x = {'key1': 1, 'key2': 3, 'key3': 2}
y = {'key1': 1, 'key2': 2}
for (key, value) in set(x.items()) & set(y.items()):
    print('%s: %s is present in both x and y' % (key, value))