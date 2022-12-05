ans = 0
for line in open("input.txt","r").readlines():
    segments = line.strip().split(",")
    seg1 = list(map(lambda x: int(x),segments[0].split("-")))
    seg2 = list(map(lambda x: int(x),segments[1].split("-")))
    if((seg1[0]<seg2[0])&(seg1[1]<seg2[0])):
        pass
    elif((seg2[0]<seg1[0])&(seg2[1]<seg1[0])):
        pass
    else:
        ans += 1

print(ans)