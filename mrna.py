import os
import sys

def load_data(infile):
    with open(infile, 'r', encoding='ISO-8859-1') as f:
        data = f.readline().strip()
    return data

def write_data(outfile):
    # not used
    if os.path.exists(outfile):
        os.remove(outfile)
    
    f = open(outfile, 'a+')
    #f.write('')
    f.close()


def main(argv):
    data = load_data(argv[0])
    print(data)
    number_of_codons_for_aa = {'F':2, 'L':6, 'S':6, 'Y':2, 'C':2, 'W':1, 'P':4, 'H':2, 'Q':2, 'R':6, 'I':3, 'M':1, 'T':4, 'N':2, 'K':2, 'V':4, 'A':4, 'D':2, 'E':2, 'G':4, 'Stop':3}
    number_of_possibilities = 1
    for aa in range(len(data)):
        number_of_possibilities *= number_of_codons_for_aa[data[aa]]
        number_of_possibilities %= 1000000
    number_of_possibilities *= number_of_codons_for_aa['Stop']
    number_of_possibilities %= 1000000
    print(number_of_possibilities)


if __name__ == "__main__":
    main(sys.argv[1:])