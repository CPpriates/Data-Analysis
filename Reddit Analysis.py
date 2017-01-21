"""Nico Salafranca nms6dz"""
import pandas as pd
import math
import numpy as np
import collections

f = open('hw6-output-Salafranca-Nicolas.txt', 'w')
df = pd.read_table('pizza_requests.txt')

txtlist = []
for i in df.requests:
    txtlist.append(i)
txtlist

#1
print("Problem 1", file=f)
requestlist = []
for line in txtlist:
    if line.count("requester_received_pizza, true") == 1 or line.count("requester_received_pizza, false"):
        requestlist.append(line)
len(requestlist)

successcount = 0 
for i in requestlist:
    if i.count("true"):
        successcount += 1
successcount 
"""1397"""
print(successcount, file=f)
#2
print("Problem 2", file=f)
subred = []
for line in txtlist:
    if line.count("requester_number_of_subreddits_at_request"):
        subred.append(line.split(',')[1])
subred = list(map(int, subred))
np.mean(subred)
"""17.969846587903369"""
print("mean = ", np.mean(subred), file=f)

subs = []
for line in txtlist:
    if line.count("  "):
        subs.append(line)
subs
for i in subs:
    if i.count("request_text") or i.count("request_text_edit_aware") or i.count("request_title"):
        subs.remove(i)
subs
unnn = np.unique(subs)
len(unnn)
print("Distinct sub", len(unnn), file=f)

#3
print('Problem 3', file=f)
agelist = []
for line in txtlist:
    if line.count("requester_account_age_in_days_at_request") == 1:
        agelist.append(line)

age = []
for i in agelist:
    age.append(i.split(',')[1])
age

age2 = list(map(float, age))
sum(age2)/len(age2)
"""252.90525101719555"""
print(sum(age2)/len(age2), file=f)
#4 
print('Problem 4', file=f)
m = 252.90525101719555
big = []
small = []
for i in age2:
    if i < m:
        small.append(i)
    elif i > m:
        big.append(i)
        
p1 = len(small)/len(age2)
p2 = len(big)/len(age2)
n1 = len(small)
n2 = len(big)
p11 = (p1*(1-p1))/n1
p22 = (p2*(1-p2))/n2
z = [(p1 - p2) - 1.96*math.sqrt(p11 + p22),(p1 - p2) + 1.96*math.sqrt(p11 + p22)]
"""[0.21996123385322788, 0.27201548982866236]"""
print(z, file=f)
#5
print('Problem 5', file=f)
users = []
for lines in txtlist:
    if lines.count("requester_username") == 1:
        users.append(lines)

usernum = []
for i in users:
    usernum.append(i.split(',')[1])
usernum       

print([item for item, count in collections.Counter(usernum).items() if count > 1])
"""No duplicates"""
print("No Duplicates", file=f)

#6
print('Problem 6', file=f)
upvote = []
for line in txtlist:
    if line.count("number_of_upvotes_of_request_at_retrieval") == 1:
        upvote.append(line)

upvotect = []
for i in upvote:
    upvotect.append(i.split(',')[1])
upvotect

up = list(map(int, upvotect))
np.mean(up)
"""6.3921706929994713"""
print(np.mean(up), file=f)
#7
print('Problem 7', file=f)
str = "request_text"
list1 = []
for line in txtlist:
    if line.count(str) == 1:
        list1.append(line)

list2 = []
for i in list1:
    if i.count("request_text_edit_aware")==1:
        list2.append(i)
list2

list3 = np.setdiff1d(list1, list2)
list4 = list(list3)

studct = 0
for i in list4:
    if i.count("student") > 0:
        studct += 1

studct/len(list4)*100
"""7.836023943406493"""
print(studct/len(list4)*100, file=f)