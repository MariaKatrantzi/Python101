# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 13:34:17 2021

@author: Maria Katrantzi
"""

# program that prints the unique items in a given list
def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(unique_list([1,2,3,3,3,3,4,5])) 

# program that simulates flipping a coin a random number of times
import random
def randgen(max):
    return random.randint(1,max)
    
def coinflip():
    coin = random.randint(1,2)
    if coin == 1:
        return "Heads"
    else:
        return "Tails"
def average(Heads, Tails):
    print("Heads: " + str(Heads))
    print("Tails: " + str(Tails))
    total = Heads + Tails
    print("Total: " + str(total))
    print("Heads: " + str((Heads/total)*100) + "%")
    print("Tails: " + str((Tails/total)*100) + "%")
    
def simulation():
    Heads = 0
    Tails = 0
    for i in range(randgen(100)):
        flip = coinflip()
        if flip == "Heads":
            Heads += 1
        else:
            Tails += 1
    average(Heads, Tails) 
simulation()