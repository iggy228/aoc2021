class BingoCard:
    def __init__(self):
        self.playboard = [
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
        ]

    def insertRow(self, row, position):
        self.playboard[position] = row

    def markNumber(self, number):
        for row in range(5):
            for position in range(5):
                if self.playboard[row][position] == number:
                    self.playboard[row][position] = -1

    def checkRow(self, row):
        for i in row:
            if i != -1:
                return False
        return True

    def checkColumn(self, column):
        for i in range(5):
            if self.playboard[i][column] != -1:
                return False
        return True

    # return True if was found bingo
    def checkBingo(self):
        for row in self.playboard:
            if(self.checkRow(row)):
                return True

        for i in range(5):
            if (self.checkColumn(i)):
                return True

        return False

    def sumUnmarkedNumers(self):
        unmarkedSum = 0
        for row in self.playboard:
            for number in row:
                if number != -1:
                    unmarkedSum += number
        return unmarkedSum

    def printPlayboard(self):
        print(self.playboard)



def loadNumbers(file):
    return list(map(int, file.readline().split(',')))


def loadBingos(file):
    bingosList = []

    while file.readline() == '\n':
        bingo = BingoCard()
        
        for i in range(5):
            bingoRow = list(map(int, file.readline().strip().split()))
            bingo.insertRow(bingoRow, i)

        bingosList.append(bingo)

    return bingosList


def solution1(numbersArr, bingosArr):
    for number in numbersArr:
        for bingo in bingosArr:
            bingo.markNumber(number)
            if (bingo.checkBingo()):
                print("Solution1: ", bingo.sumUnmarkedNumers() * number)
                return


def solution2(numbersArr, bingosArr):
    for number in numbersArr:
        i = 0
        while i < len(bingosArr):
            bingosArr[i].markNumber(number)
            if (bingosArr[i].checkBingo()):
                if len(bingosArr) > 1:
                    bingosArr.pop(i)
                    i -= 1
                else:
                    print("Solution2: ", bingosArr[0].sumUnmarkedNumers() * number)
                    return
            else:
                i += 1

def main():
    numbersArr = []
    bingosArr = []

    file = open('day4.txt')

    numbersArr = loadNumbers(file)

    bingosArr = loadBingos(file)

    # solution1(numbersArr, bingosArr)
    solution2(numbersArr, bingosArr)

if __name__ == '__main__':
    main()
