def fileToSet(file):
    pointsSet = set()

    line = file.readline()

    while line != '\n':
        point = tuple(map(int, line.strip().split(',')))
        pointsSet.add(point)

        line = file.readline()
    return pointsSet


def fileToArr(file):
    arr = []

    for line in file:
        _, res = line.strip().split('fold along ')
        dir, pos = res.strip().split('=')

        arr.append([dir, int(pos)])
    return arr


def fold(points, instruction):
    newSet = set()

    for point in points:
        if instruction[0] == 'x':
            if point[0] > instruction[1]:
                newPoint = list(point)
                x = newPoint[0] - 2 * (newPoint[0] - instruction[1])
                newPoint[0] = x
                newSet.add(tuple(newPoint))
            else:
                newSet.add(point)
        if instruction[0] == 'y':
            if point[1] > instruction[1]:
                newPoint = list(point)
                y = newPoint[1] - 2 * (newPoint[1] - instruction[1])
                newPoint[1] = y
                newSet.add(tuple(newPoint))
            else:
                newSet.add(point)
    return newSet


def printPoints(points):
    matrix = [[' ' for col in range(200)] for row in range(7)]

    for point in points:
        matrix[point[1]][point[0]] = '#'

    for row in matrix:
        for column in row:
            print(column, sep='', end='')
        print()


def solution(points, instructions):
    printLength = True

    for instruction in instructions:
        points = fold(points, instruction)

        if printLength:
            print('Solution 1:', len(points))
            printLength = False

    printPoints(points)


if __name__ == '__main__':
    file = open('day13.txt')

    pointsSet = fileToSet(file)
    instructions = fileToArr(file)

    solution(pointsSet, instructions)