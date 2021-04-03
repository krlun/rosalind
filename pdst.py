import os
import sys
import numpy as np

def load_data(infile):
    genes = list()
    gene = str()
    with open(infile, 'r', encoding='ISO-8859-1') as f:
        line = f.readline()
        while True:
            line = f.readline()
            if not line:
                break
            if line[0] == '>':
                genes.append(gene)
                gene = str()
            else:
                gene += line.rstrip()
    genes.append(gene)
    return genes

def write_data(outfile):
    # not used
    if os.path.exists(outfile):
        os.remove(outfile)
    f = open(outfile, 'a+')
    #f.write('')
    f.close()

def calculate_p_distance(gene1, gene2):
    n = len(gene1)
    different = 0
    for i in range(n):
        if gene1[i] != gene2[i]:
            different += 1
    return different/n

def main(argv):
    genes = load_data(argv[0])
    n = len(genes)
    D = np.zeros((n, n))

    for i in range(n):
        for j in range(i, n):
            D[i, j] = calculate_p_distance(genes[i], genes[j])
            D[j, i] = D[i, j]
    
    for i in D:
        for j in i:
            print(j, end=' ')
        print()

if __name__ == "__main__":
    main(sys.argv[1:])