import os
import sys


def load_data(infile):
    genes = dict()
    gene = str()
    first = True
    with open(infile, 'r', encoding='ISO-8859-1') as f:
        line = f.readline()
        gene_name = line[1:].rstrip()
        while True:
            line = f.readline()
            if not line:
                break
            if line[0] == '>':
                genes[gene_name] = gene
                gene_name = line[1:].rstrip()
                gene = str()
            else:
                gene += line.rstrip()
    genes[gene_name] = gene
    return genes

def create_adjaceny_list(genes):
    adjacency_list = list()
    for key_i in genes.keys():
        for key_j in genes.keys():
            # print(key_i, key_j)
            if key_i != key_j:
                # print(key_i, key_j)
                # print(genes[key_i][-3:])
                if genes[key_i][-3:] == genes[key_j][0:3]:
                    adjacency_list.append(str(key_i) + ' ' + str(key_j))
    return adjacency_list

def write_data(outfile):
    # not used
    if os.path.exists(outfile):
        os.remove(outfile)
    f = open(outfile, 'a+')
    #f.write('')
    f.close()

def main(argv):
    genes = load_data(argv[0])
    adjacency_list = create_adjaceny_list(genes)
    for item in adjacency_list:
        print(item)


if __name__ == "__main__":
    main(sys.argv[1:])