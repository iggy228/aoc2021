# time complexity O(n2)
def solution1(input_arr):
    max_number = max(input_arr)
    min_number = min(input_arr)
    solution = 9999999999999999999

    for i in range(min_number, max_number + 1):
        fuelCount = 0
        for nm in input_arr:
            fuelCount += abs(nm - i)
        if fuelCount < solution:
            solution = fuelCount

    print(solution)


# time complexity O(n2)
def solution2(input_arr):
    max_number = max(input_arr)
    min_number = min(input_arr)
    solution = 9999999999999999999

    for i in range(min_number, max_number + 1):
        fuelCount = 0
        for nm in input_arr:
            fuelCount += (abs(nm - i) * (abs(nm - i) + 1)) / 2
        if fuelCount < solution:
            solution = fuelCount

    print(solution)


if __name__ == '__main__':
    input_arr = list(map(int, open('day7.txt').readline().strip().split(',')))

    solution1(input_arr)
    solution2(input_arr)
