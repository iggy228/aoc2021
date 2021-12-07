def string_to_arr(str):
    return list(map(int, str.strip().split(',')))


def arr_to_count_arr(arr, countArr):
    for i in arr:
        countArr[i] += 1


def solution(arr, period):
    fishCountArr = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    arr_to_count_arr(arr, fishCountArr)

    for _ in range(period):
        newFishCountArr = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(len(fishCountArr)):
            if i == 0:
                newFishCountArr[6] += fishCountArr[0]
                newFishCountArr[8] += fishCountArr[0]
            else:
                newFishCountArr[i - 1] += fishCountArr[i]

        fishCountArr = newFishCountArr

    print('Solution after', period, ':', sum(fishCountArr))


if __name__ == '__main__':
    lineStr = open('files/day6.txt').readline()
    arr = string_to_arr(lineStr)

    solution(arr, 80)
    solution(arr, 256)
