# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 13:46:18 2022

@author: Shardool
"""

data =  open("inputday4.txt", "r").read().split("\n")
contains = 0
count = 0 
count1 = 0
for line in data:
    a, b = line.split(',')
    a1, a2 = a.split('-')
    b1, b2 = b.split('-')
    a1 = int(a1)
    b1 = int(b1)
    a2 = int(a2)
    b2 = int(b2)
    
    
    #part 1
    if(a1 <= b1 and a2 >= b2):
        count += 1
    elif(b1 <= a1 and b2 >= a2):
        count += 1
    #part 2    
    if(a1 <= b1 and a2>= b1):
        count1 += 1
    elif(b1 <= a1 and b2 >=a1):
        count1 += 1

print("Part 1 solution: ", count)
print("Part 2 solution: ", count1)   
    
#     elf1,elf2 =  line.split(',') 
#     start1,end1 = elf1.split('-')
#     start2,end2 = elf2.split('-')
    
#     # cast to integer
#     start1 = int(start1)
#     start2 = int(start2)
#     end1 = int(end1)
#     end2 = int(end2)
    
#     # check if elf 1's range contains elf 2's range
#     # if(start1 <= start2 and end1 >= end2):
#     #     contains = contains + 1
#     # # check if elf 2's range contains elf 1's range
#     # elif(start2 <= start1 and end2 >= end1):
#     #     contains = contains + 1
    
#     # check if elf1's range overlaps before elf 2's range
#     if(start1 <= start2 and end1 >= start2):
#        contains = contains + 1
#    # check if elf2's range overlaps before elf 1's range
#     elif(start2 <= start1 and end2 >= start1):
#        contains = contains + 1
# # print answer
# print(contains)