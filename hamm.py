import os
import sys

def load_data(infile):
    with open(infile, 'r', encoding='ISO-8859-1') as f:
        dna1 = f.readline().rstrip()
        dna2 = f.readline().rstrip()
    return dna1, dna2

def write_data(outfile):
    # not used
    if os.path.exists(outfile):
        os.remove(outfile)
    f = open(outfile, 'a+')
    #f.write('')
    f.close()

def hamming(dna1, dna2):
    count = 0
    for i in range(len(dna1)):
        if dna1[i] != dna2[i]:
            count += 1
    return count

def main(argv):
    dna1, dna2 = load_data(argv[0])
    print(hamming(dna1, dna2))

if __name__ == "__main__":
    main(sys.argv[1:])