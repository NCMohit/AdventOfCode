crabs = []
file = open("input.txt","r")
for line in file.readlines():
    temp = line.strip().split(",")
    for crab in temp:
        crabs.append(int(crab))

min_cost = 999999999999999
for hole in range(min(crabs),max(crabs)+1):
    cost = 0
    for crab in crabs:
        shift = abs(hole-crab)
        cost += ((shift*(shift+1))/2)
    if(cost < min_cost):
        min_cost = cost

print("Min cost: ",min_cost)