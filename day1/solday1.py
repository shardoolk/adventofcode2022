
data  = open("avc1.txt", "r").read().split("\n\n")

calorie = []
for line in data:
    calorie.append(sum([int(r) for r in line.splitlines()]))
    
   
print("part 1: ",  max(calorie))

calorie.sort(reverse = True)

print("part 2: ", sum(calorie[:3]))