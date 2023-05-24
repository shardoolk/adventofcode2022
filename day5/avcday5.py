# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 00:17:43 2022

@author: Shardool
"""

levels, instructions =  open("inputday5.txt", "r").read().split("\n\n")


for line in instructions:
    quantity, origin, destination = [int(i) for i in instructions.split(" ") if i.isnumeric()]
    
    