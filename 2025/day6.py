with open(r'2025\inputs\day6input.txt', 'r') as file:
    input = file.read()

import re
import numpy as np

example = """123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   +  """

exampleops = example.split('\n')[-1]

def reducespace(string):
    string = re.sub(r'\s+', ' ', string).strip()
    return string

#print(reducespace(" 1   2   3      6               7      "))

def mat(string):
    rows = string.split('\n')
    for i,row in enumerate(rows):
        rownew = reducespace(row).split(" ")
        rows[i] = rownew
    return rows

def processcol(matrix, index, var=1) -> int:
    n_inputs = len(matrix)-1
    operator = matrix[n_inputs][index]
    if var == 1:
        values = [int(matrix[x][index]) for x in range(n_inputs)]
        if operator == '+':
            return sum(values)
        if operator == '*':
            return np.prod(values)

    #return values, n_inputs, operator, matrix



def iterate(string):
    sum = 0
    nvalues = len(mat(string)[0])
    for v in range(nvalues):
        sum += processcol(mat(string), v)
    return sum


#print(processcol(mat(example), 0))
#print(iterate(input))

def reassignoperators(string):
    rowlengthh = len(string)
    row = string.split('a')
    print(row)
    for x in range(rowlengthh):
        if row[x] == ' ':
            row[x] = row[x-1]
    return row


print(reassignoperators(exampleops))
exit()
#
# okay part 2 needs an entirely different way of thinking
def processmatrix(string):
    rows = string.split('\n')
    rowlength = len(rows[0])
    values = [int(rows[x][y]) for y in range(len(rows))]
    print(rows, rowlength, values)




print(processmatrix(example))