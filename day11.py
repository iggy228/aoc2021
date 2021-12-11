import time

t0 = time.time()


def fileToMatrix(file):
    matrix = []

    for line in file:
        matrixLine = []
        line.strip()
        for nm in line:
            if nm != '\n':
                matrixLine.append(int(nm))
        matrix.append(matrixLine)
    return matrix


def defineFlashesMatrix(rowCount, columnCount):
    matrix = []

    for _ in range(rowCount):
        matrixLine = []
        for __ in range(columnCount):
            matrixLine.append(False)
        matrix.append(matrixLine)
    return matrix


def resetFlashesMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = False


def trueFlashesMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if not matrix[i][j]:
                return False
    return True


def octopusBFS(matrix, flashesMatrix, y, x):
    queue = []
    count = 0

    queue.append([y, x])

    while queue:
        curPos = queue.pop(0)

        if matrix[curPos[0]][curPos[1]] != 9:
            if not flashesMatrix[curPos[0]][curPos[1]]:
                matrix[curPos[0]][curPos[1]] += 1
        else:
            if not flashesMatrix[curPos[0]][curPos[1]]:
                count += 1
                matrix[curPos[0]][curPos[1]] = 0
                flashesMatrix[curPos[0]][curPos[1]] = True
                for a in range(-1, 2):
                    for b in range(-1, 2):
                        if 0 <= curPos[0] + a < len(matrix) and 0 <= curPos[1] + b < len(matrix[0]) and (a != 0 or b != 0):
                            queue.append([curPos[0] + a, curPos[1] + b])

    return count


def solution(matrix, flashesMatrix):
    flashesCount = 0
    found = False
    period = 1

    while not found:

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                flashesCount += octopusBFS(matrix, flashesMatrix, i, j)

        if period == 100:
            print('Solution 1:', flashesCount)
            print((time.time() - t0) * 1000, 'ms')
        if trueFlashesMatrix(flashesMatrix):
            print('Solution 2:', period)
            found = True

        resetFlashesMatrix(flashesMatrix)
        period += 1


if __name__ == '__main__':
    file = open('files/day11.txt')

    matrix = fileToMatrix(file)
    flashesMatrix = defineFlashesMatrix(len(matrix), len(matrix[0]))
    print((time.time() - t0) * 1000, 'ms')
    solution(matrix, flashesMatrix)
    print((time.time() - t0) * 1000, 'ms')

