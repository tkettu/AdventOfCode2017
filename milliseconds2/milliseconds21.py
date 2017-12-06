import sys


def difference_bw_largest_adn_smallest(line):

    s = line.split()
    nums = [int(i) for i in s]
    ma, mi = max(nums), min(nums)
    return (ma - mi)


def checksum(nums):
    cs = 0
    while (True):
        line = nums.readline()
        #print(line)
        if line=='':
            break
        cs += difference_bw_largest_adn_smallest(line)

    return cs



if __name__ == '__main__':
    file = 'test_input.txt'
    if len(sys.argv) > 1:
        file = sys.argv[1]

    nums = open(file)
    print(checksum(nums))
