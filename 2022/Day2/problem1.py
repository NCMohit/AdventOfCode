moves = []

def check_results(opponent, move):
    if(opponent == "A"):
        if(move == "X"):
            return 3
        if(move == "Y"):
            return 6
        if(move == "Z"):
            return 0
    elif(opponent == "B"):
        if(move == "X"):
            return 0
        elif(move == "Y"):
            return 3
        elif(move == "Z"):
            return 6
    elif(opponent == "C"):
        if(move == "X"):
            return 6
        elif(move == "Y"):
            return 0
        elif(move == "Z"):
            return 3

move_score = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

score = 0
for line in open("input.txt","r").readlines():
    move = line.strip().split(" ")
    score += move_score[move[1]] + check_results(move[0],move[1])

print(score)