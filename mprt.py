import os
import sys
import requests
import re


def load_filenames(infile):
    files = list()
    with open(infile, 'r', encoding='ISO-8859-1') as f:
        for line in f:
            files.append(line.strip())
    return files


def load_data(infile):
    protein = str()
    with open(infile, 'r', encoding='ISO-8859-1') as f:
        for line in f:
            if line[0] != '>':
                protein += line.rstrip()
    return protein


def download_data(files):
    base_url = 'http://www.uniprot.org/uniprot/'
    for i in range(len(files)):
        outfile = files[i] + '.fasta'
        if os.path.exists(outfile):
            os.remove(outfile)
        file_url = base_url + files[i] + '.fasta'
        r = requests.get(file_url, stream = True)
        with open(outfile, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)


def find_motif(protein, pattern):
    positions = list()
    for i in range(len(protein) - 4):
        if re.match(pattern, protein[i:i+4]):
            positions.append(i+1)
    return positions

def write_data(outfile):
    # not used
    if os.path.exists(outfile):
        os.remove(outfile)
    
    f = open(outfile, 'a+')
    #f.write('')
    f.close()

def print_positions(name, positions):
    if positions:
        print(name)
        print(' '.join([str(i) for i in positions]))
    else:
        return


def main(argv):
    filenames = load_filenames(argv[0])
    download_data(filenames)
    pattern = 'N[^P][ST][^P]'
    for i in range(len(filenames)):
        positions = find_motif(load_data(filenames[i] + '.fasta'), pattern)
        print_positions(filenames[i], positions)


if __name__ == "__main__":
    main(sys.argv[1:])