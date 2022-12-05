ascii = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

ans = 0
for line in open("input.txt","r").readlines():
    line = line.strip()
    half = int(len(line)/2)
    front = line[:half]
    back = line[half:]
    for letter in front:
        if(letter in back):
            ans += ascii.index(letter) + 1
            break

print(ans)