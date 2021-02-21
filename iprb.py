import os
import sys
from math import factorial


def load_data(infile):
    data = list()
    with open(infile, 'r', encoding='ISO-8859-1') as file:
        data = [int(i) for i in file.readline().strip().split()]

    return data

def write_data(outfile):
    # not used
    if os.path.exists(outfile):
        os.remove(outfile)
    
    f = open(outfile, 'a+')
    #f.write('')
    f.close()

def binom(n, k):
    return factorial(n) // factorial(k) // factorial(n - k)

def dominant_allele(d):
    dominant = binom(d[0], 2) + d[0]*d[1] + d[0]*d[2] + 0.5*d[1]*d[2] + .75*binom(d[1], 2)
    print(sum(d))
    return dominant/binom(sum(d), 2)

def main(argv):
    data = load_data(argv[0])
    print(dominant_allele(data))

    print(data)



if __name__ == "__main__":
    main(sys.argv[1:])