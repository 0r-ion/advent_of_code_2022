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

    #lose
    if you == "X":
        score += 0
        if enemy == "A":
            score += 3
        elif enemy == "B":
            score += 1
        elif enemy == "C":
            score += 2
    #tie
    elif you == "Y":
        score += 3
        if enemy == "A":
            score += 1
        elif enemy == "B":
            score += 2
        elif enemy == "C":
            score += 3

    #win
    elif you == "Z":
        score += 6
        if enemy == "A":
            score += 2
        elif enemy == "B":
            score += 3
        elif enemy == "C":
            score += 1
    return score
    


def main():
    total = 0
    file = open("2\data.txt","r")
    for line in file:
        oppo = line[0]
        youy = line [2]
        total += scoreOfRound(oppo, youy)
    print(total )

if __name__ == __name__=='__main__':
    main()