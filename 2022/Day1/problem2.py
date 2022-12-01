calories = []
file = open("input.txt","r")
reindeer = []
for line in file.readlines():
    if(line == "\n"):
        calories.append(sum(reindeer))
        reindeer = []
    else:
        reindeer.append(int(line.strip()))

calories.append(sum(reindeer))

calories.sort()
print(sum(calories[-3:]))