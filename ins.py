import os
import sys
import numpy as np
import pandas as pd


def load_data(infile):
    array = list()
    with open(infile, 'r', encoding='ISO-8859-1') as f:
        for line in f:
            line = line.strip()
            array.append(line)

    data = array[1].split()
    for i in range(int(array[0])):
        data[i] = int(data[i])

    return int(array[0]), data

def insertion_sort(n, A):
    count = 0
    for i in range(1, n):
        k = i
        while k > 0 and A[k] < A[k-1]:
            count += 1
            A[k], A[k-1] = A[k-1], A[k]
            k -= 1
    return A, count



def write_data(outfile):
    # not used
    if os.path.exists(outfile):
        os.remove(outfile)
    
    f = open(outfile, 'a+')
    #f.write('')
    f.close()

def main(argv):
    n, data = load_data(argv[0])
    data, count = insertion_sort(n, data)
    print(count)



if __name__ == "__main__":
    main(sys.argv[1:])