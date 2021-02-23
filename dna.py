import os
import sys
import requests
import re


def load_data(infile):

    with open(infile, 'r', encoding='ISO-8859-1') as f:
        dna = f.readline().rstrip()
    return dna

def write_data(outfile):
    # not used
    if os.path.exists(outfile):
        os.remove(outfile)
    
    f = open(outfile, 'a+')
    #f.write('')
    f.close()

def count_nucleotides(dna):
    A = 0
    C = 0
    G = 0
    T = 0
    for i in dna:
        if i == 'A':
            A += 1
        elif i == 'C':
            C += 1
        elif i == 'G':
            G += 1
        else:
            T += 1
    print(str(A) + ' ' + str(C) + ' ' + str(G) + ' ' + str(T))


def main(argv):
    dna = load_data(argv[0])
    count_nucleotides(dna)


if __name__ == "__main__":
    main(sys.argv[1:])