# 3612020 = (301, -300)
# ero 325
# (301, 25)
#input = 361527
#


# 1024
# 962 = (16, -15)
# ero 62
# 962 + 31 = 993 -> (16,16)
# 993 + 31 = 1024 -> (-15,16)
import sys


def what_power(numb):
    a0 = 1
    p = 0
    while True:
        if numb <= a0:
            return p, a0-8*p, a0, numb - (a0 - 8*p), a0 - numb
        p += 1
        a0 = a0 + 8*p


if __name__ == '__main__':
    n = 1
    input = 361527
    if len(sys.argv) > 1:
        print(what_power(int(sys.argv[1])))
    else:
        print(what_power(input))