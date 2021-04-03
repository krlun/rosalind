import os
import sys

def load_data(infile):
    with open(infile, 'r', encoding='ISO-8859-1') as f:
        n = int(f.readline().rstrip())
        nodes = [False]*n
        adjacency_list = dict()
        for i in range(n):
            adjacency_list[i] = set()
        for line in f:
            line = line.rstrip().split()
            key = int(line[0]) - 1
            value = int(line[1]) - 1
            adjacency_list[key].add(value)
            key, value = value, key
            adjacency_list[key].add(value)
    return nodes, adjacency_list

def write_data(outfile):
    # not used
    if os.path.exists(outfile):
        os.remove(outfile)
    f = open(outfile, 'a+')
    #f.write('')
    f.close()

def DFS(adjacency_list, nodes, k):
    nodes[k] = True
    for i in adjacency_list[k]:
        if nodes[i] == False:
            DFS(adjacency_list, nodes, i)
    return None

def main(argv):
    nodes, adjacency_list = load_data(argv[0])
    component_count = 0
    for i in range(len(nodes)):
        if nodes[i] == False:
            DFS(adjacency_list, nodes, i)
            component_count += 1
    print(component_count - 1)

if __name__ == "__main__":
    main(sys.argv[1:])