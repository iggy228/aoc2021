import time


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


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


def isLocalMinimum(matrix, y, x):
    for a in range(-1, 2):
        for b in range(-1, 2):
            if 0 <= y + a < len(matrix) and 0 <= x + b < len(matrix[0]) and a != b:
                if matrix[y][x] >= matrix[y + a][x + b]:
                    return False
    return True


def solution1(matrix):
    sumOfMinimals = 0
    minimalsArr = []

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if isLocalMinimum(matrix, i, j):
                sumOfMinimals += matrix[i][j] + 1
                minimalsArr.append(Point(j, i))

    print('Solutions 1:', sumOfMinimals)
    return minimalsArr


def defineVisitedMatrix(matrix):
    visitedMatrix = []

    for line in matrix:
        visitedLine = []
        for nm in line:
            if nm == 9:
                visitedLine.append(True)
            else:
                visitedLine.append(False)
        visitedMatrix.append(visitedLine)
    return visitedMatrix


def BFS(visitedMatrix, point):
    queue = []
    area = 0

    queue.append(point)

    while queue:
        aPoint = queue.pop(0)

        if visitedMatrix[aPoint.y][aPoint.x] == False:
            area += 1

        visitedMatrix[aPoint.y][aPoint.x] = True

        if aPoint.y - 1 >= 0:
            if not visitedMatrix[aPoint.y - 1][aPoint.x]:
                queue.append(Point(aPoint.x, aPoint.y - 1))

        if aPoint.y + 1 < len(visitedMatrix):
            if not visitedMatrix[aPoint.y + 1][aPoint.x]:
                queue.append(Point(aPoint.x, aPoint.y + 1))

        if aPoint.x - 1 >= 0:
            if not visitedMatrix[aPoint.y][aPoint.x - 1]:
                queue.append(Point(aPoint.x - 1, aPoint.y))

        if aPoint.x + 1 < len(visitedMatrix[0]):
            if not visitedMatrix[aPoint.y][aPoint.x + 1]:
                queue.append(Point(aPoint.x + 1, aPoint.y))
    return area


def solution2(matrix, minimalsArr):
    visitedMatrix = defineVisitedMatrix(matrix)

    minimalsArea = []

    for minimal in minimalsArr:
        area = BFS(visitedMatrix, minimal)
        minimalsArea.append(area)

    minimalsArea.sort(reverse=True)

    print('Solution 2:', minimalsArea[0] * minimalsArea[1] * minimalsArea[2])


if __name__ == '__main__':
    t0 = time.time()
    file = open('files/day9.txt', 'r')

    matrix = fileToMatrix(file)
    print((time.time() - t0) * 1000, 'ms')
    minimalsArr = solution1(matrix)
    print((time.time() - t0) * 1000, 'ms')
    solution2(matrix, minimalsArr)
    print((time.time() - t0) * 1000, 'ms')
