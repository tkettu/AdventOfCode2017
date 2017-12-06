import sys


def nums_to_array(nums):
    a = []
    while True:
        line = nums.readline()
        if line=='':
            break
        a.append(int(line))
    return a

def solve_maze(nums):

    maze = nums_to_array(nums)

    ni = 0
    s, e = 0, (len(maze) - 1)
    steps = 0

    if (e < 20):
        print(maze)
    while True:
        if (ni< s) | (ni > e):
            break
        c = maze[ni]

        maze[ni] += -1 if (c > 2) else 1
        ni = ni + c

        steps += 1

    if (e < 20):
        print(maze)
    print(steps)


if __name__ == '__main__':
    file = 'test_input.txt'
    if len(sys.argv) > 1:
        file = 'input.txt'


    nums = open(file)
    solve_maze(nums)
