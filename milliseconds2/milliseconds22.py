import sys


def evenly_divide(line):

    s = line.split()
    nums = [int(i) for i in s]
    l = len(nums)
    for i in range(l):
        j = i + 1
        while j < l:
            if nums[i]%nums[j] == 0:
                d = nums[i]/nums[j]
                return d
            elif nums[j]%nums[i] == 0:
                d = nums[j]/nums[i]
                return d
            j += 1

    return 0


def checksum(nums):
    cs = 0
    while (True):
        line = nums.readline()
        if line=='':
            break
        cs += evenly_divide(line)

    return cs



if __name__ == '__main__':
    file = 'test_input2.txt'
    if len(sys.argv) > 1:
        file = sys.argv[1]
    else:
        file = 'input2.txt'

    nums = open(file)
    print(checksum(nums))
