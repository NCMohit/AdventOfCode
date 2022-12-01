import math, sys
matrix = []

file = open("input.txt","r")
for line in file.readlines():
    row = []
    temp = line.strip()
    for i in temp:
        row.append(int(i))
    matrix.append(row)

node_cost = {(0,0):0}
visited = []
visited_temp = [[0,0]]

while(len(visited_temp) != 0 ):
    chosen_node = None
    chosen_node_cost = math.inf
    for node in visited_temp:
        if(node_cost[(node[0],node[1])]<chosen_node_cost):
            chosen_node = node
            chosen_node_cost = node_cost[(node[0],node[1])]
    visited.append(chosen_node)
    visited_temp.remove(chosen_node)
    neighbors = []
    if(chosen_node[0] != 0):
        if([chosen_node[0]-1,chosen_node[1]] not in visited+visited_temp):
            visited_temp.append([chosen_node[0]-1,chosen_node[1]])
            neighbors.append([chosen_node[0]-1,chosen_node[1]])
    if(chosen_node[0] != (len(matrix)-1) ):
        if([chosen_node[0]+1,chosen_node[1]] not in visited+visited_temp):
            visited_temp.append([chosen_node[0]+1,chosen_node[1]])
            neighbors.append([chosen_node[0]+1,chosen_node[1]])
    if(chosen_node[1] != 0):
        if([chosen_node[0],chosen_node[1]-1] not in visited+visited_temp):
            visited_temp.append([chosen_node[0],chosen_node[1]-1])
            neighbors.append([chosen_node[0],chosen_node[1]-1])
    if(chosen_node[1] != (len(matrix[0])-1) ):
        if([chosen_node[0],chosen_node[1]+1] not in visited+visited_temp):
            visited_temp.append([chosen_node[0],chosen_node[1]+1])
            neighbors.append([chosen_node[0],chosen_node[1]+1])
    for node in neighbors:
        if((node[0],node[1]) in node_cost.keys()):
            temp = chosen_node_cost + matrix[node[0]][node[1]]
            if(temp < node_cost[(node[0],node[1])]):
                node_cost[(node[0],node[1])] = temp
        else:
            node_cost[(node[0],node[1])] = chosen_node_cost + matrix[node[0]][node[1]]

print(node_cost[len(matrix)-1,len(matrix[0])-1])