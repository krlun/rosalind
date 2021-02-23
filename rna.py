import os
import sys
import copy


def load_data(infile):

    with open(infile, 'r', encoding='ISO-8859-1') as f:
        dna = f.readline().rstrip()
    # return list(dna)
    return dna

def write_data(outfile):
    # not used
    if os.path.exists(outfile):
        os.remove(outfile)
    
    f = open(outfile, 'a+')
    #f.write('')
    f.close()

def dna_to_rna(dna):
    rna = dna.copy()
    for i in range(len(dna)):
        if dna[i] == 'T':
            rna[i] = 'U'
    return ''.join(rna)


def main(argv):
    dna = load_data(argv[0])
    rna = dna.replace('T', 'U')
    # rna = dna_to_rna(dna)
    print(rna)


if __name__ == "__main__":
    main(sys.argv[1:])