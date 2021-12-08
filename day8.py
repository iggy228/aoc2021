def fileToArrays(file):
    leftSideArr = []
    rightSideArr = []

    for line in file:
        leftSide, rightSide = line.strip().split('|')
        leftSideArr.append(leftSide.strip().split())
        rightSideArr.append(rightSide.strip().split())

    return leftSideArr, rightSideArr


# O(n) if right side will be always 4 numbers else O(n2)
def solution1(rightSideArr):
    count = 0
    for line in rightSideArr:
        for i in line:
            if len(i) == 2 or len(i) == 4 or len(i) == 3 or len(i) == 7:
                count += 1
    print('Solution 1:', count)


def decifreNumbers(leftSide):
    digits = ['', '', '', '', '', '', '', '', '', '']

    fiveLengthDigits = []
    sixLengthDigits = []

    # categorizing numbers
    for i in leftSide:
        if len(i) == 2:
            digits[1] = i
        if len(i) == 3:
            digits[7] = i
        if len(i) == 4:
            digits[4] = i
        if len(i) == 7:
            digits[8] = i
        if len(i) == 6:
            sixLengthDigits.append(i)
        if len(i) == 5:
            fiveLengthDigits.append(i)

    # final decisioning for six length digits by length by legth of set
    for i in sixLengthDigits:
        if len(set(i) - set(digits[1])) == 5:
            digits[6] = i
        elif len(set(i) - set(digits[4])) == 2:
            digits[9] = i
        else:
            digits[0] = i

    # final decisioning for five length digits by length of set
    for i in fiveLengthDigits:

        if len(set(i) - set(digits[1])) == 3:
            digits[3] = i
        elif len(set(i) - set(digits[4])) == 3:
            digits[2] = i
        else:
            digits[5] = i

    return digits


def solution2(leftSideArr, rightSideArr):
    sumOfAllNumbers = 0

    for i in range(len(leftSideArr)):
        digits = decifreNumbers(leftSideArr[i])

        numbers = ''
        for code in rightSideArr[i]:
            for j in range(len(digits)):
                if set(code) == set(digits[j]):
                    numbers += str(j)
        sumOfAllNumbers += int(numbers)

    print('Solution 2:', sumOfAllNumbers)


if __name__ == '__main__':
    file = open('files/day8.txt')

    leftSideArr, rightSideArr = fileToArrays(file)

    solution1(rightSideArr)
    solution2(leftSideArr, rightSideArr)
