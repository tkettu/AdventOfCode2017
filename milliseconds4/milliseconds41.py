import sys


def check_duplicate(line):
    s = line.split()

    l = len(s)
    for i in range(l):
        j = i + 1
        while j < l:
            if s[i] == s[j]:
                return 0
            j += 1

    return 1

def passphrase(text):
    cs = 0
    while (True):
        line = text.readline()
        print(line)
        if line=='':
            break
        cs += check_duplicate(line)

    return cs



if __name__ == '__main__':
    file = 'input.txt'
    if len(sys.argv) > 1:
        file = sys.argv[1]

    nums = open(file)
    print(passphrase(nums))