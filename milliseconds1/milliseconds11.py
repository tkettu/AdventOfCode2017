import sys

# aoc ms (day) 1.1
def capthcha(input):
    s = 0
    for i in range(len(input)):
        nro = input[i]
        s += int(nro) if (nro==ring_next(input,i)) else 0
    return s


def ring_next(s, i):
    return (s[i+1] if i < len(s) - 1 else s[0])


if __name__=='__main__':
    text = '1111'
    if len(sys.argv) > 1:
        text = sys.argv[1]
    else:
        text = open('input.txt').read()

    print(capthcha(text))

