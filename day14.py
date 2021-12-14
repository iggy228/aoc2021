# return two maps
import time


def fileToHashMaps(file):
    keyValMap = {}

    for line in file:
        key, val = line.strip().split('->')
        keyValMap[key.strip()] = val.strip()

    return keyValMap


def defineCountMap(string):
    map = {}
    for i in range(len(string) - 1):
        if map.get(string[i: i + 2]) is None:
            map[string[i: i + 2]] = 1
        else:
            map[string[i: i + 2]] += 1
    return map


def defineLettersMap(string):
    map = {}
    for i in string:
        if map.get(i) is None:
            map[i] = 1
        else:
            map[i] += 1
    return map


def findSmallestAndlargest(lettersMap):
    smallest = None
    largest = 0

    for val in lettersMap:
        if smallest is None:
            smallest = lettersMap[val]
        if largest < lettersMap[val]:
            largest = lettersMap[val]
        if smallest > lettersMap[val]:
            smallest = lettersMap[val]

    return smallest, largest


def solution(string, valMap, period):
    pairsMap = defineCountMap(string)
    lettersMap = defineLettersMap(string)

    for _ in range(period):
        newCountMap = {}

        for val in pairsMap:
            letter = valMap[val]

            if lettersMap.get(letter) is None:
                lettersMap[letter] = pairsMap[val]
            else:
                lettersMap[letter] += pairsMap[val]

            if newCountMap.get(val[0] + letter) is None:
                newCountMap[val[0] + letter] = pairsMap[val]
            else:
                newCountMap[val[0] + letter] += pairsMap[val]

            if newCountMap.get(letter + val[1]) is None:
                newCountMap[letter + val[1]] = pairsMap[val]
            else:
                newCountMap[letter + val[1]] += pairsMap[val]

        pairsMap = newCountMap

    smallest, largest = findSmallestAndlargest(lettersMap)
    print(lettersMap)
    print('Solution:', largest - smallest)


if __name__ == '__main__':
    t0 = time.time()
    file = open('files/day14.txt')

    string = file.readline().strip('\n')
    file.readline()

    valMap = fileToHashMaps(file)
    print((time.time() - t0) * 1000, 'ms')

    print('Period 10')
    solution(string, valMap, 10)
    print((time.time() - t0) * 1000, 'ms')

    print('Period 40')
    solution(string, valMap, 40)
    print((time.time() - t0) * 1000, 'ms')

    print('Period 100')
    solution(string, valMap, 100)
    print((time.time() - t0) * 1000, 'ms')

    print('Period 1000')
    solution(string, valMap, 100)
    print((time.time() - t0) * 1000, 'ms')
