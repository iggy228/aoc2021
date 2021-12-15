def loadFile(filename):
    file = open(filename, 'r')
    return file.readlines()


def countZerosAndOnes(arr, i):
    countOfZeros = 0
    countOfOnes = 0

    for record in arr:
        if record[i] == '0':
            countOfZeros += 1
        else:
            countOfOnes += 1

    return countOfZeros, countOfOnes

def solution1(arr):
    gammaRate = ''
    epsilonRate = ''

    for i in range(len(arr[0]) - 1):
        countOfZeros, countOfOnes = countZerosAndOnes(arr, i)

        if countOfZeros > countOfOnes:
            gammaRate += '0'
            epsilonRate += '1'
        if countOfZeros < countOfOnes:
            gammaRate += '1'
            epsilonRate += '0'

    print("Solution1:", int(gammaRate, 2) * int(epsilonRate, 2))


def selectOxygenRate(arr):
    oxygenRate = arr.copy()

    for i in range(len(arr[0]) - 1):
        countOfZeros, countOfOnes = countZerosAndOnes(oxygenRate, i)

        if len(oxygenRate) > 1:
            if countOfZeros > countOfOnes:
                oxygenRate = list(filter(lambda x: x[i] == '0',oxygenRate))
            elif countOfOnes > countOfZeros:
                oxygenRate = list(filter(lambda x: x[i] == '1',oxygenRate))
            else:
                oxygenRate = list(filter(lambda x: x[i] == '1',oxygenRate))
        else:
            return int(oxygenRate[0], 2)

    return int(oxygenRate[0], 2)


def selectCoRate(arr):
    co2Rate = arr.copy()

    for i in range(len(arr[0]) - 1):
        countOfZeros, countOfOnes = countZerosAndOnes(co2Rate, i)

        if len(co2Rate) > 1:
            if countOfZeros > countOfOnes:
                co2Rate = list(filter(lambda x: x[i] == '1',co2Rate))
            elif countOfOnes > countOfZeros:
                co2Rate = list(filter(lambda x: x[i] == '0',co2Rate))
            else:
                co2Rate = list(filter(lambda x: x[i] == '0',co2Rate))
        else:
            return int(co2Rate[0], 2)
    return int(co2Rate[0], 2)


def solution2(arr):
    oxygenRate = selectOxygenRate(arr)
    co2Rate = selectCoRate(arr)

    print('Solution2:', oxygenRate * co2Rate)



inputArr = loadFile('day3.txt')

solution1(inputArr)

solution2(inputArr)