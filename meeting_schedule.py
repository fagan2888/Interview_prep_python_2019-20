#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 10:16:53 2020

@author: liwenhuang
meeting scheduler - https://www.hackerrank.com/contests/amazon/challenges/meeting-schedules/problem

a pretty dumb solution that is accepted 
"""

m=list(map(int, input().split()))
m, k = m[0], m[1]
time_slots = []
#format the input
for _ in range(m):
    time_slots.append(list(map(int, input().split())))
#print(time_slots)
hours = [[0]*60 for _ in range(24)]


time_slots = [
[7, 45, 7, 47],
[3, 28, 3, 30],
[9, 50, 9, 51],
[15, 44, 15, 45],
[22, 8, 22, 9],
[20, 42, 20, 43],
[18, 20, 18, 21],
[7, 34, 7, 35],
[8, 36, 8, 37],
[9, 43, 9, 45]
]
k = 30



def find_slots(time_slots, k):
    #this function print out the first 0 starting from h, m
    def find_0(s_h, s_m):
        # search in the first hour
        for i in range(s_m, 60):
            if hours[s_h][i] == 0:
                return [s_h, i]
#        for m in range(start_m, 24):
#            if hours[start_h][m] == 0:
#                return [start_h, m]
        # search in the next hour  
        for h in range(s_h+1, 24):
            for m in range(60):
                if hours[h][m] == 0:
                    return[h,m]
    #this function print out the first 1 starting from h, m
    def find_1(s_h, s_m):
        # search in the first hour
        for i in range(s_m, 60):
            if hours[s_h][i] == 1:
                return[s_h, i]
        # search in the next hour  
        for h in range(s_h+1, 24):
            for m in range(60):
                if hours[h][m] == 1:
                    return[h,m]
    #this func determind whether a time slot is longer than k
    def duration(slot):
        start = slot[0]
        end = slot[1]
        if end:
            duration =  (end[0] - start[0])*60 + (end[1] - start[1])
        else:
            duration =  (23 - start[0])*60 + (60- start[1])
        #if duration >= k: print('yes')
        return duration
    
    #this function take in the start hh, mm, and end hh, mm, mark all the minute in this durations 1
    def mark_1(s_h, s_m, e_h, e_m):
        # duration within one hour
        if s_h == e_h:
            for i in range(s_m, e_m):
                hours[s_h][i] =1    
        # duration span different hours, note e_h always > s_h
        else:
            for i in range(s_m, 60):
                hours[s_h][i] = 1
            for i in range(s_h+1, e_h):
                for j in range(60):
                    hours[i][j] = 1
            for i in range(0, e_m):
                hours[e_h][i] = 1
        
    
    #mark all the busy slots with 1
    for time_slot in time_slots: 
        #print(time_slot)              
        s_h, s_m, e_h, e_m = time_slot[0], time_slot[1], time_slot[2], time_slot[3]
        mark_1(s_h, s_m, e_h, e_m)

    slots = [[find_0(0, 0), find_1(0, 0)]]
    #after this, the next pair will use the [1] of the current pair as
    while slots[-1][1]: # this does not account for the last openning til the mid-night
        pair = slots[-1]
        new_input = pair[1]
        new_h, new_m = new_input[0], new_input[1]
        if not find_0(new_h, new_m): # consider situation when all the mins til midnight are not available
            break
        new_pair = [find_0(new_h, new_m)]
        new_pair.append(find_1(new_pair[0][0], new_pair[0][1]))
        slots.append(new_pair)
    #process the last slot
    slots[-1][1] = [23, 60]
       
    #filter the slot that last longer than k
    potential_slots = list(filter(lambda x:duration(x) >= k, slots))
    
    if potential_slots[-1][1] == [23, 60]:
        potential_slots[-1][1] = [0, 0]
    return potential_slots


#three layers of lists 
result = find_slots(time_slots, k)

# second layer is the one line
for slots in result:
    # first layer is the start point and end point in [hh, mm], [hh, mm] form
    new_slots = []
    for slot in slots:
        new_slot = list(map(lambda num:"{:02d}".format(num), slot))
        #print(" ".join(new_slot))
        new_slots.append(" ".join(new_slot))
    print(" ".join(new_slots))
    

#test7_path = "https://hr-testcases-us-east-1.s3.amazonaws.com/255/input07.txt?AWSAccessKeyId=AKIAJ4WZFDFQTZRGO3QA&Expires=1582083661&Signature=osSAGg%2B%2FjVg4SkvhzL7SrqOkdiQ%3D&response-content-type=text%2Fplain"
#
#from urllib.request import urlopen
#import sys
#
#file = urlopen(test7_path)
#test7 = str(file.read(), 'utf-8')
#datapoints = list(map(int, test7.split()))
#datapoints = datapoints[2:]
#time_slots = []
#time_slot = []
#while datapoints:
#    current_num = datapoints.pop(0)
#    time_slot.append(current_num)
#    if len(time_slot) == 4:
#        time_slots.append(time_slot)
#        time_slot = []
    
    
    



            




