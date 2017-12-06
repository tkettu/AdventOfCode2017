import sys


def isAnagram(str1, str2):
    str1_list = list(str1)
    str1_list.sort()
    str2_list = list(str2)
    str2_list.sort()

    return (str1_list == str2_list)


def check_anagram(line):
    s = line.split()

    l = len(s)
    for i in range(l):
        j = i + 1
        while j < l:

            if isAnagram(s[i], s[j]):
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
        cs += check_anagram(line)

    return cs



if __name__ == '__main__':
    file = 'input.txt'
    if len(sys.argv) > 1:
        file = sys.argv[1]

    nums = open(file)
    print(passphrase(nums))