import os
import sys

def load_data(infile):
    data = list()
    first = True
    with open(infile, 'r', encoding='ISO-8859-1') as file:
        for line in file:
            if line[0] == '>':
                if first:
                    string = ''
                    first = False
                else:
                    data.append(string)
                    string = ''
            else:
                string = string + line.strip()
        data.append(string)
    return data

def write_data(outfile):
    # not used
    if os.path.exists(outfile):
        os.remove(outfile)
    
    f = open(outfile, 'a+')
    #f.write('')
    f.close()

def transition(a, b):
    if a == 'A' and b == 'G' or a == 'C' and b == 'T':
        return True
    elif b == 'A' and a == 'G' or b == 'C' and a == 'T':
        return True
    else:
        return False

def transversion(a, b):
    if a == 'A' and b == 'C' or a == 'A' and b == 'T' or a == 'G' and b == 'C' or a == 'G' and b == 'T':
        return True
    elif b == 'A' and a == 'C' or b == 'A' and a == 'T' or b == 'G' and a == 'C' or b == 'G' and a == 'T':
        return True
    else:
        return False

def calc_transition_transversion_ratio(data):
    transitions = 0
    transversions = 0
    for i in range(len(data[0])):
        if transition(data[0][i], data[1][i]):
            transitions += 1
        elif transversion(data[0][i], data[1][i]):
            transversions += 1
    return transitions/transversions

def main(argv):
    data = load_data(argv[0])
    print(calc_transition_transversion_ratio(data))



if __name__ == "__main__":
    main(sys.argv[1:])