###Advent of code 2022 day7 solution 
from collections import defaultdict
console_data = open("day_7_input.txt").read().strip()

file_size = defaultdict(int)
path = []

console_data = console_data.split("\n")
for line in console_data:
    if line.startswith("$ cd"):
        last_dict = line.split()[2]
        if last_dict == "/":
            path.append("/")
        elif last_dict == "..":
            last = path.pop()
        else:
            path.append(f"{path[-1]}{'/' if path[-1] != '/' else ''}{last_dict}") 
    if line[0].isnumeric():
        for p in path:
            file_size[p] = file_size[p] + int(line.split()[0]) 
                
            
#print(path)
#print(file_size)            
#print(file_size.values())
print(f"Part 1: {sum(s for s in file_size.values() if s <= 100_000)}")
print(f"Part 2: {min(s for s in file_size.values() if s >= 30_000_000 - (70_000_000 - file_size['/']))}")