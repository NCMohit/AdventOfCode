ascii = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

ans = 0
temp = []
for line in open("input.txt","r").readlines():
    if(len(temp)==3):
        for x in temp[0]:
            if(x in temp[1]):
                if(x in temp[2]):
                    ans += ascii.index(x) + 1
                    break
        temp = []
    line = line.strip()
    temp.append(set(line))

for x in temp[0]:
    if(x in temp[1]):
        if(x in temp[2]):
            ans += ascii.index(x) + 1

print(ans)