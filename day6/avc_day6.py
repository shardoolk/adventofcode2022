### Advent of code2022
# Day 6 solution 

###Take in the input 
signal = open("day6input.txt").read()

## A function which finds the message depending of the size provided by the question
def message_loc(size):
    for i,char in enumerate(signal):
        setOFsignal = set(signal[i:i+size]) ## set does not allow for duplicates hence if the length matches 
        #we arrive at our solution
        if len(setOFsignal) == size:
            return i+size 
        

print("Solution Part 1:", message_loc(4))
print("Solution Part 2:", message_loc(14))