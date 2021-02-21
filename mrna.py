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


def main(argv):
    data = load_data(argv[0])
    print(calc_transition_transversion_ratio(data))



if __name__ == "__main__":
    main(sys.argv[1:])