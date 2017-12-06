
import sys

def distribute(blocks):

    states = []
    same_block = []
    li = 0
    #while blocks not in states:
    while blocks not in states:
        states.append(blocks[:])
        si = blocks.index(max(blocks))
        b = blocks[si]
        blocks[si] = 0
        blocks = distribute_index(blocks, b, si)
        same_block = blocks

    cycles = 0
    li = len(states) - 1

    while True:
        cycles += 1
        bb = states[li - cycles]
        if bb == same_block:
            break

    return cycles + 1


def distribute_index(blocks, b, si):
    while b > 0:
        si = ring_next_index(blocks, si)
        blocks[si] += 1
        b -= 1
    return blocks


def ring_next_index(s, i):
    return (i+1 if i < len(s) - 1 else 0)

if __name__=='__main__':
    blocks_test = [0, 2, 7, 0]
    if len(sys.argv) > 1:
        file =  'input.txt'
        blocks = open(file).read().split('\t')
        blocksi = [int(i) for i in blocks]
        print(distribute(blocksi))
    else:
        print(distribute(blocks_test))


