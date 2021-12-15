import time
from collections import defaultdict

pathsCount = 0
paths2Count = 0


def fileToGraph(file):
    gdict = defaultdict(list)

    for line in file:
        l, r = line.strip().split('-')
        gdict[l].append(r)
        gdict[r].append(l)

    return gdict


def findAllValidPathsDFS(graph, cur, visited):
    if cur == 'end':
        global pathsCount
        pathsCount += 1
        return
    visited.append(cur)

    for neighbour in graph[cur]:
        if neighbour.islower():
            if neighbour not in visited:
                findAllValidPathsDFS(graph, neighbour, visited.copy())
        else:
            findAllValidPathsDFS(graph, neighbour, visited.copy())



def findAllValidPathsDFS2(graph, cur, visited, twiceVisited):
    if cur == 'end':
        global paths2Count
        paths2Count += 1
        return

    visited.append(cur)

    for neighbour in graph[cur]:
        if neighbour.islower():
            if neighbour in visited:
                if twiceVisited == '' and neighbour != 'start':
                    findAllValidPathsDFS2(graph, neighbour, visited.copy(), neighbour)
            else:
                findAllValidPathsDFS2(graph, neighbour, visited.copy(), twiceVisited)
        else:
            findAllValidPathsDFS2(graph, neighbour, visited.copy(), twiceVisited)


def solution1(graph):
    findAllValidPathsDFS(graph, 'start', [])

    print('Solution 1:', pathsCount)


def solution2(graph):
    findAllValidPathsDFS2(graph, 'start', [], '')

    print('Solution 2:', paths2Count)


if __name__ == '__main__':
    t0 = time.time()
    file = open('day12.txt')

    graph = fileToGraph(file)
    print((time.time() - t0) * 1000, 'ms')
    solution1(graph)
    print((time.time() - t0) * 1000, 'ms')
    solution2(graph)
    print((time.time() - t0) * 1000, 'ms')
