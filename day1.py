def openFile(filename):
    file = open(filename, 'r')

    return list(map(int, file.readlines()))


def measurement(arr):
    curDeep = 0
    measurement = 0

    for deep in arr:
        if curDeep == 0:
            curDeep = deep
        else:
            if deep > curDeep:
                measurement += 1
            curDeep = deep

    print('First part: ', measurement)


def slicingMeasurment(arr):
    prevMeasurment = arr[0] + arr[1] + arr[2]
    measurement = 0

    for i in range(3, len(arr)):  
        curMeasurment = prevMeasurment + arr[i] - arr[i - 3]

        if (curMeasurment > prevMeasurment):
            measurement += 1
        prevMeasurment = curMeasurment

    print('Second part: ', measurement)

arr = openFile('files/day1.txt')

measurement(arr)

slicingMeasurment(arr)
