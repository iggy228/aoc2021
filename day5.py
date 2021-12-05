def open_file_as_two_array(filename):
    file = open(filename)
    lines = file.readlines()
    firstPoints = []
    secondsPoints = []
    for line in lines:
        point1, point2 = line.split('->')
        firstPoints.append(list(map(int, point1.strip().split(','))))
        secondsPoints.append(list(map(int, point2.strip().split(','))))
    return firstPoints, secondsPoints


def define_grid(size):
    grid = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(0)
        grid.append(row)
    return grid


def save_line(grid, start_point, end_point):
    increment = 1
    if start_point[0] > end_point[0]:
        increment = -1

    for i in range(start_point[0], end_point[0] + increment, increment):
        grid[start_point[1]][i] += 1


def save_column(grid, start_point, end_point):
    increment = 1
    if start_point[1] > end_point[1]:
        increment = -1

    for i in range(start_point[1], end_point[1] + increment, increment):
        grid[i][start_point[0]] += 1


def save_diagonal(grid, start_point, end_point):
    start_nm = 0
    end_nm = 1
    isDown = 1

    startY = 0

    if start_point[0] < end_point[0]:
        start_nm = start_point[0]
        end_nm += end_point[0]
        startY = start_point[1]
        if start_point[1] > end_point[1]:
            isDown = -1
    else:
        start_nm = end_point[0]
        end_nm += start_point[0]
        startY = end_point[1]
        if end_point[1] > start_point[1]:
            isDown = -1

    for i in range(start_nm, end_nm):
        grid[startY][i] += 1
        startY += (1 * isDown)


def count_intersection(grid):
    count = 0
    for row in grid:
        for number in row:
            if number > 1:
                count += 1
    return count


def solution1(grid, start_points, end_points):
    for i in range(len(start_points)):
        if start_points[i][0] == end_points[i][0]:
            save_column(grid, start_points[i], end_points[i])
        if start_points[i][1] == end_points[i][1]:
            save_line(grid, start_points[i], end_points[i])

    print(count_intersection(grid))


def solution2(grid, start_points, end_points):
    for i in range(len(start_points)):
        if abs(start_points[i][0] - end_points[i][0]) == abs(start_points[i][1] - end_points[i][1]):
            save_diagonal(grid, start_points[i], end_points[i])

    print(count_intersection(grid))


if __name__ == '__main__':
    start_points, end_points = open_file_as_two_array('files/day5.txt')
    grid = define_grid(1000)

    solution1(grid, start_points, end_points)
    solution2(grid, start_points, end_points)
