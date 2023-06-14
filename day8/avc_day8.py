#### advent of code 2022 day 8 trees height

tree_data = open("day_8_input.txt").readlines()
forest = [[int(x) for x in row.strip()] for row in tree_data]
rows = len(forest)
columns = len(forest[0])

edges = 2*rows + 2*(columns-2) 

scores = []

visible_trees = edges
for row in range(1,rows-1):
    for cols in range(1,columns-1):
        tree = forest[row][cols]
        
        left = [forest[row][cols-i] for i in range(1,cols+1)]
        right = [forest[row][cols+i] for i in range(1,columns-cols)]
        top = [forest[row-i][cols] for i in range(1,row+1)]
        down = [forest[row+i][cols] for i in range(1,rows-row)]
        
        #### Part 1
        if max(left) < tree or max(right) < tree or max(top) < tree or max(down) < tree:
            visible_trees +=1
            
        #### Part 2
        score = 1
        
        for lst in (left,right,top,down):
            tracker = 0
            for i in range(len(lst)):
                if lst[i] < tree:
                    tracker += 1
                elif lst[i] >= tree:
                    tracker+= 1
                    break
                       
            score *= tracker
            scores.append(score)
            
            
print("Part 1 soln: ", visible_trees)  

print("Part 2 soln: ", max(scores))