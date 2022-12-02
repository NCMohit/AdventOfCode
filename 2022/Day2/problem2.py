moves = []

def check_results(opponent, move):
    if(opponent == "A"):
        if(move == "X"):
            return 3
        if(move == "Y"):
            return 1
        if(move == "Z"):
            return 2
    elif(opponent == "B"):
        if(move == "X"):
            return 1
        elif(move == "Y"):
            return 2
        elif(move == "Z"):
            return 3
    elif(opponent == "C"):
        if(move == "X"):
            return 2
        elif(move == "Y"):
            return 3
        elif(move == "Z"):
            return 1

round_score = {
    "X": 0,
    "Y": 3,
    "Z": 6
}

score = 0
for line in open("input.txt","r").readlines():
    move = line.strip().split(" ")
    score += check_results(move[0],move[1]) + round_score[move[1]]

print(score)