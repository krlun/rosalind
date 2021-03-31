import os
import sys
from typing import Sequence

def load_data(infile):
    with open(infile, 'r', encoding='ISO-8859-1') as f:
        data = f.readline().split()
    return int(data[0]), int(data[1])

def write_data(outfile):
    # not used
    if os.path.exists(outfile):
        os.remove(outfile)
    f = open(outfile, 'a+')
    #f.write('')
    f.close()

def rabbits(n, m):
    sequence = [1, 1]
    for i in range(2, n):
        if i < m:
            sequence.append(sequence[-1] + sequence[-2])
        elif (i == m) or (i == m + 1):
            sequence.append(sequence[-1] + sequence[-2] - 1)
        else:
            sequence.append(sequence[-1] + sequence[-2] - sequence[-(m+1)])
    return sequence[-1]

def main(argv):
    n, m = load_data(argv[0])
    print(rabbits(n, m))

if __name__ == "__main__":
    main(sys.argv[1:])