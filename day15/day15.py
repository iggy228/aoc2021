import time

allPath = 0
lowest = None


def fileToMatrix(file):
    matrix = []

    for line in file:
        matrixLine = []
        line = line.strip('\n')
        for digit in line:
            matrixLine.append(int(digit))
        matrix.append(matrixLine)

    return matrix


def calculatePath(matrix, visited):
    global lowest
    sum = 0

    for i in visited:
        sum += matrix[i[0]][i[1]]
    if lowest is None:
        lowest = sum
    if lowest > sum:
        lowest = sum


def findLowestPointPathDFS(matrix, cur, visited):
    if cur == (len(matrix) - 1, len(matrix[0]) - 1):
        global allPath
        allPath += 1
        calculatePath(matrix, visited)
        return
    visited.add(cur)

    if cur[0] - 1 >= 0:
        if (cur[0] - 1, cur[1]) not in visited:
            findLowestPointPathDFS(matrix, (cur[0] - 1, cur[1]), visited.copy())
    if cur[0] + 1 < len(matrix):
        if (cur[0] + 1, cur[1]) not in visited:
            findLowestPointPathDFS(matrix, (cur[0] + 1, cur[1]), visited.copy())
    if cur[1] - 1 >= 0:
        if (cur[0], cur[1] - 1) not in visited:
            findLowestPointPathDFS(matrix, (cur[0], cur[1] - 1), visited.copy())
    if cur[1] + 1 < len(matrix[0]):
        if (cur[0], cur[1] + 1) not in visited:
            findLowestPointPathDFS(matrix, (cur[0], cur[1] + 1), visited.copy())


def solution1(matrix):
    findLowestPointPathDFS(matrix, (0, 0), set())
    # print(lowest)
    print(allPath)


if __name__ == '__main__':
    t0 = time.time()
    file = open('day15.txt')

    matrix = fileToMatrix(file)
    print((time.time() - t0) * 1000, 'ms')
    solution1(matrix)
    print((time.time() - t0) * 1000, 'ms')
    # solution2(graph)
    # print((time.time() - t0) * 1000, 'ms')
