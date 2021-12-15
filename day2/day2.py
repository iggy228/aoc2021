class SubmarineOperation:
    def __init__(self, operation, distance):
        self.operation = operation
        self.distance = distance



def stringToSubmatineOperation(a):
    strArr = a.split(' ')
    return SubmarineOperation(strArr[0], int(strArr[1]))


def loadFile(filename):
    file = open(filename, 'r')
    return list(map(stringToSubmatineOperation, file.readlines()))


def solution1(operations):
    horizontalDistance = 0
    verticalDistance = 0

    for operation in operations:
        if operation.operation == 'forward':
            horizontalDistance += operation.distance
        if operation.operation == 'up':
            verticalDistance -= operation.distance
        if operation.operation == 'down':
            verticalDistance += operation.distance

    print('1. Multiply of horizontal and vertical distance is:', horizontalDistance * verticalDistance)


def solution2(operations):
    horizontalDistance = 0
    verticalDistance = 0
    aim = 0

    for operation in operations:
        if operation.operation == 'forward':
            horizontalDistance += operation.distance
            verticalDistance += operation.distance * aim
        if operation.operation == 'up':
            aim -= operation.distance
        if operation.operation == 'down':
            aim += operation.distance

    print('2. Multiply of horizontal and vertical distance is:', horizontalDistance * verticalDistance)



submarineOperations = loadFile('day2.txt')

solution1(submarineOperations)
solution2(submarineOperations)
