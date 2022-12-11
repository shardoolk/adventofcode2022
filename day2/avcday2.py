# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 15:46:19 2022

@author: Shardool
"""

data  = open("inputday2.txt", "r").read().split("\n")

score  = 0
score2 = 0
for line in data:
    opp, me  = line.split()
    score += {'X' : 1, 'Y': 2, 'Z': 3}[me]
    score += {('A','X') : 3, ('A','Y') : 6,('A','Z') : 0,
              ('B','X') : 0, ('B','Y') : 3, ('B','Z') : 6, 
              ('C','X') : 6, ('C','Y') : 0, ('C','Z') : 3}[(opp,me)]
    score2 += {'X' : 0, 'Y': 3, 'Z': 6}[me]
    score2 += {('A','X') : 3, ('A','Y') : 1,('A','Z') : 2,
              ('B','X') : 1, ('B','Y') : 2, ('B','Z') : 3, 
              ('C','X') : 2, ('C','Y') : 3, ('C','Z') : 1}[(opp,me)]
    
print("Part1 : ",score)     
print("Part2 : ",score2)