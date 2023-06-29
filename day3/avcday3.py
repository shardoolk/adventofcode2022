# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 22:34:50 2022

@author: Shardool
"""

datad3  = open("inputday3.txt", "r").read().split("\n")


def getVal(x):
    return ord(x) - ord('a') + 1 if x.islower() else ord(x) - ord('A') + 27

count = 0
for line in datad3:
    m = len(line) // 2
    x = (set(line[:m]) & set(line[m:])).pop()
    count += getVal(x)
   
   
# sol = ', '.join(str(i) for i in sol)

# count = 0
# for i in range(len(sol)):
#     count +=  ord(sol[i]) - ord('a') + 1 if sol[i].islower() else ord(sol[i]) - ord('A') + 27

count2 = 0

for i in range(0, len(datad3),3):
    line1, line2, line3 = datad3[i:i+3]
    common = (set(line1) & set(line2) & set(line3)).pop()
    count2 += getVal(common)
    
    