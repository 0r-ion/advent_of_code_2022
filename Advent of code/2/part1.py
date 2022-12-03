class points():
    def __init__(self) -> None:
        self.rock = 1
        self.paper = 2
        self.scissors = 3
        self.win = 6
        self.loss = 0
        self.tie = 3

def scoreOfRound(enemy, you)->int:
    score = 0

    #points from pick

    if you == "X":
        score += 1
    elif you == "Y":
        score += 2
    elif you == "Z":
        score += 3
    
    #points from winning

    if enemy == "A":
        if you == "X":
            score += 3
        elif you == "Y":
            score += 6
        elif you == "Z":
            score += 0

    elif enemy == "B":
        if you == "X":
            score += 0
        elif you == "Y":
            score += 3
        elif you == "Z":
            score += 6

    elif enemy == "C":
        if you == "X":
            score += 6
        elif you == "Y":
            score += 0
        elif you == "Z":
            score += 3
    return score
        


def main():
    total = 0
    file = open("data.txt","r")
    for line in file:
        oppo = line[0]
        youy = line [2]
        total += scoreOfRound(oppo, youy)
        # print(line[2])
        # print(f"{line[0]} <-e y-> {line[2]}")
    print(total )

if __name__ == __name__=='__main__':
    main()