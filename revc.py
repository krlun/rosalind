import os
import sys


def load_data(infile):
    with open(infile, 'r', encoding='ISO-8859-1') as f:
        dna = f.readline().rstrip()
    return list(dna)

def write_data(outfile):
    # not used
    if os.path.exists(outfile):
        os.remove(outfile)
    
    f = open(outfile, 'a+')
    #f.write('')
    f.close()

def complementary_dna_string(dna):
    cdna = list()
    for i in dna[::-1]:
        if i == 'C':
            cdna.append('G')
        elif i == 'G':
            cdna.append('C')
        elif i == 'A':
            cdna.append('T')
        else:
            cdna.append('A')
    return cdna



def main(argv):
    dna = load_data(argv[0])
    cdna = complementary_dna_string(dna)
    print(''.join(cdna))




if __name__ == "__main__":
    main(sys.argv[1:])