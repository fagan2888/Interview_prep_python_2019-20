"""
Created on Fri Jan 17 07:48:50 2020

@author: liwenhuang
"""

# overlapping meetings
meetings = [[8, 9], [10, 12], [8.5, 10.5], [7, 8], [7.5, 8.5]]
n = len(meetings)

for i in range(1, n):
    x, y = meetings[0], meetings[i]
    a, b = x[0], x[1]
    c, d = y[0], y[1]
    if a<c<b or a<d<b:
        print('yes')
    else:
        print('no')

# moving average
mylist = [1, 2, 3, 4, 5, 6, 7]

moving_sum = 0
cul_arr = []
for i in range(len(mylist)):
    moving_sum += mylist[i]
    cul_arr.append(mylist[i])
    if len(cul_arr) == 3:
        print(moving_sum/3)
        moving_sum -= cul_arr.pop(0)


# rank customers
customers = ['Mary $2', 'Sam $2', 'Sam $2', 'Joe $1', 'Joe $3']
customer_list = []
for i in range(5):
    a_record = customers[i].split(' ')
    name, amt = a_record[0], a_record[1].strip('$')
    customer_list.append([name, amt])

customer_dict = {}
for i in range(5):
    name, amt = customer_list[i][0], float(customer_list[i][1])
    if name not in customer_dict:
        customer_dict[name] = amt
    else:
         customer_dict[name] += amt

# this dose not sort the name
for name, amt in sorted(customer_dict.items(), key = lambda item: item[1], reverse = True):
    print(name + ': $' + str(amt))

# use default dictionary
from collections import defaultdict
cust_rank_dict2 = defaultdict(list)
for name, amt in customer_dict.items():
    cust_rank_dict2[amt].append(name)
    cust_rank_dict2[amt].sort()

# print out
for amt, names in sorted(cust_rank_dict.items(), key = lambda item: item[0], reverse = True):
    for name in names:
        print(name + ': $' + str(amt))

# sort names so that customer with equal amount would be ranked by names as well
cust_rank_dict = {}
for name, amt in customer_dict.items():
    if amt not in cust_rank_dict:
        cust_rank_dict[amt] = [name]
    else:
        cust_rank_dict[amt].append(name)
        cust_rank_dict[amt].sort()
