# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 15:02:03 2022

@author: Shardool
"""

data  = open("avc1.txt", "r").read().split("\n\n")

calorie = []
for line in data:
    calorie.append(sum([int(r) for r in line.splitlines()]))
    
   
print("part 1: ",  max(calorie))

calorie.sort(reverse = True)

print("part 2: ", sum(calorie[:3]))