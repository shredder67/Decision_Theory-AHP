import json

def print_table(table):
    i = 1
    shift = '-'*(8*len(table[0]) + 3)
    print(shift)
    print('\t1',end='\t')
    for j in range(1, len(table[0])):
        print(j + 1,end='\t')
    print()
    print(shift)
    for row in table:
        print(i, ' |', end='\t')
        for v in row:
            print(v, end='\t')
        print()
        i += 1
    print(shift, end='\n\n')


with open('data.json', mode='r', encoding='utf-8') as json_file:
    # Read data from file and separate it
    content = json.load(json_file)
    data = content["data"]
    comp_matricies = content["comp_matricies"]
    keys = list(comp_matricies.keys())
    table = [list(data[i].values())[1:] for i in range(len(data))]

def normalize(vector):
    for i, v in enumerate(vector):
        vector[i] = v / sum(vector)
    return vector

def calc_W(matrix):
    V = []
    for row in matrix:
        V.append(1)
        for el in row:
            V[-1] *= el
        V[-1] = pow(V[-1], 1 / len(matrix))
    
    print(V)
    return normalize(V)
    

def main():
    print_table(table)
    print_table(comp_matricies[keys[0]])
    
    W = calc_W(comp_matricies[keys[0]])
    print(W)

if __name__ == "__main__":
    main()