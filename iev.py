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

def calc_offspring_dominant_phenotype(data):
    return 1*data[0]*2 + 1*data[1]*2 + 1*data[2]*2 + 0.75*data[3]*2 + 0.5*data[4]*2 + 0*data[5]*2


def main(argv):
    data = load_data(argv[0])
    print(data)
    print(calc_offspring_dominant_phenotype(data))


if __name__ == "__main__":
    main(sys.argv[1:])