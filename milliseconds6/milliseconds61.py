# Memory banks ([0, 2, 7, 0]) -> Distribute blocks
# Start with largest (i = 2), remove all, add one to next until everything distributed
import sys


def distribute(blocks):
    """Return number of cycles to redistribute until we reach state we've seen before"""

    cycles = 0
    states = []
    while blocks not in states:
        states.append(blocks[:])
        si = blocks.index(max(blocks))
        b = blocks[si]
        blocks[si] = 0
        blocks = distribute_index(blocks, b, si)
        cycles += 1
    return cycles


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


