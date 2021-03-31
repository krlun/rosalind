import os
import sys

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

def rabbits(n, k):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return rabbits(n-1, k) + k*rabbits(n-2, k)

def main(argv):
    n, k = load_data(argv[0])
    print(rabbits(n, k))

if __name__ == "__main__":
    main(sys.argv[1:])