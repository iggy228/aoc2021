import math
import time


def fileToArray(file):
    arr = []
    for line in file:
        arr.append(line.strip('\n'))
    return arr


def findCorruptChar(line):
    stack = []

    for i in line:
        if i == '(' or i == '[' or i == '{' or i == '<':
            stack.append(i)
        if i == ')':
            if stack.pop() != '(':
                return 3
        if i == ']':
            if stack.pop() != '[':
                return 57
        if i == '}':
            if stack.pop() != '{':
                return 1197
        if i == '>':
            if stack.pop() != '<':
                return 25137
    return 0


def countBrackets(line):
    stack = []
    points = 0

    for i in line:
        if i == '(' or i == '[' or i == '{' or i == '<':
            stack.append(i)
        if i == ')':
            stack.pop()
        if i == ']':
            stack.pop()
        if i == '}':
            stack.pop()
        if i == '>':
            stack.pop()

    for i in range(len(stack) - 1, -1, -1):
        points *= 5
        if stack[i] == '(':
            points += 1
        if stack[i] == '[':
            points += 2
        if stack[i] == '{':
            points += 3
        if stack[i] == '<':
            points += 4
    return points


def solution1(arr):
    allPoints = 0

    for i in range(len(arr)):
        points = findCorruptChar(arr[i])
        if points > 0:
            allPoints += points
            arr[i] = ''

    print('Solution 1:', allPoints)


def solution2(arr):
    allPoints = []

    for i in arr:
        if i != '':
            allPoints.append(countBrackets(i))

    allPoints.sort()

    print('Solution 2:', allPoints[len(allPoints) - math.ceil(len(allPoints) / 2)])


if __name__ == '__main__':
    t0 = time.time()
    file = open('files/day10.txt')

    arr = fileToArray(file)
    print((time.time() - t0) * 1000, 'ms')

    solution1(arr)
    print((time.time() - t0) * 1000, 'ms')

    solution2(arr)
    print((time.time() - t0) * 1000, 'ms')
