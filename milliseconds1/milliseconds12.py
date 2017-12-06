import sys

# aoc ms (day) 1.2
def capthcha(input):
    s = 0
    sper2 = int(len(input)/2)
    for i in range(len(input)):
        nro = input[i]
        s += int(nro) if (nro==ring_next_half(input,sper2, i)) else 0
    return s


def ring_next_half(s, sper2, i):
    return (s[i+sper2] if i < sper2  else s[i - sper2])


if __name__=='__main__':
    text = '1111'
    if len(sys.argv) > 1:
        text = sys.argv[1]
    else:
        text = open('input.txt').read()

    print(capthcha(text))

