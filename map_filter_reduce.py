#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 17:01:25 2020

@author: liwenhuang

map, filter, and reduce notes
"""

"""
map map an interable with a function
"""
import math

def area(r):
    """return area of a circle with radius r"""
    return math.pi * (r**2)

radii = [2,5, 7.1, 0.3, 10]

# map takes a function, and iterable, output a map object, but we can use the list to turn it into a list
map(area, radii)
#<map at 0x7fea686d8390>

list(map(area, radii))
#[12.566370614359172,
# 78.53981633974483,
# 158.36768566746147,
# 0.2827433388230814,
# 314.1592653589793]

#here is a example mapping celsius to fahranheit
temps = [("Berlin",29), ("Cairo", 36), ("Los Angeles", 26), ("Beijing", 32), ("London", 22)]

c_2_f = lambda data: (data[0], (9/5)*data[1])

list(map(c_2_f, temps))
#[('Berlin', 52.2),
# ('Cairo', 64.8),
# ('Los Angeles', 46.800000000000004),
# ('Beijing', 57.6),
# ('London', 39.6)]

"""
filter function is structure similary, but only returning values when argument function is evaluated as true
"""
import statistics

data =[1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
avg = statistics.mean(data)

avg
#2.183333333333333
list(filter(lambda x: x > avg, data))
#[2.7, 4.1, 4.3]

#use filter to filter missing data
countries = ["", "Argentina", "", "Ecuador", "Venezuela"]

list(filter(None, countries)) 
# filter all values that are treated as False in boolean setting, these are 0 and empty emelents
# ['Argentina', 'Ecuador', 'Venezuela']


"""
reduce function compute nested loops until reaching the last value and return
"""
# use the reduce function for product of a list
from functools import reduce

data = [2, 3, 5, 7, 11, 13, 17]

multiplier = lambda x, y: x*y
reduce(multiplier, data)
#510510

# we can also specify a initial value for the reduce function
reduce(lambda x, y:x+y, data, 5) 

# in the employee data, the first name is the employee and the second is the boss
# use map reduce to report all the employees working under the same boss
EMPLOYEE_DATA = [
    "Alice, Carol",
    "Bob, Carol",
    "Elizabeth, Carol",
    "Gertrude, Fred",
    "Hilda, Fred",
    "David, Alice",
]

def list_employee(list_string):
    pair = list_string.split(",")
    employee, boss = pair[0].strip(), pair[1].strip()
    return (boss, employee)

employee_list = list(map(list_employee, EMPLOYEE_DATA))

def reducer(employee_dict, employee_entry):
    #print(employee_entry)
    k, v = employee_entry
    #print(k,v)
    if k not in employee_dict:
        employee_dict[k] = [v]
    else:
        employee_dict[k].append(v)
    
    return employee_dict
    
reduce(reducer, employee_list, {})
#{'Carol': ['Alice', 'Bob', 'Elizabeth'],
# 'Fred': ['Gertrude', 'Hilda'],
# 'Alice': ['David']}

#generate a list of all pairs of employees who have the same boss.
employee_dict = reduce(reducer, employee_list, {})


result = []
for boss, minions in employee_dict.items():
    while len(minions) > 1:
        current_minion = minions.pop()
        for minion in minions:
            result.append((minion, current_minion))


# use map -reduce to produce pairs with common friends
FRIEND_DATA = [
    "Alice, Bob",
    "Alice, Carol",
    "Carol, David",
    "Elizabeth, Fred",
    "Fred, David",
    "Elizabeth, Carol",
    "Gertrude, Bob",
    "Gertrude, Hilda",
    "Hilda, Carol",
]

from collections import defaultdict
# trick is to build the list of people sharing one common friend, as nodes that have 2 degrees of distance in a grph
friend_dict = defaultdict(set)
for line in FRIEND_DATA:
    first, second = line.split(',')
    first, second = first.strip(), second.strip()
    friend_dict[first].add(second)
    friend_dict[second].add(first)
    
friend_2_dict = defaultdict(set)
for host, friends in friend_dict.items():
    for friend in friends:
        friend_2_dict[host].update(friend_dict[friend])# this would add in all the 2nd connection
    friend_2_dict[host] -= {host}
    
#use the  friend_2_dict to produce all the combinations
#first get a sorted list of all the friends that have one common friend, filter when the list is shorter than 2
friend_2 = list(map(lambda item: sorted(list(item[1])), friend_2_dict.items()))

friend_2 = list(filter(lambda x:len(x)>1, friend_2))

result_comb = set()
for friend_list in friend_2:
    while len(friend_list) > 1:
        current_friend = friend_list.pop()
        for friend in friend_list:
            result_comb.add((current_friend, friend))

"""
reminder of how to use generator
"""
def nextSquare(): 
    i = 1; 
  
    # An Infinite loop to generate squares  
    while True: 
        yield i*i                 
        i += 1  # Next execution resumes  
                # from this point  

for num in nextSquare(): 
    if num > 100: 
         break    
    print(num) 