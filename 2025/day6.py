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


#print(reassignoperators(exampleops))
#
# okay part 2 needs an entirely different way of thinking

# coming back to part 2 months later
def processmatrix(input):
    # converting the full worksheet into individual problems
    lines = input.split('\n')
    firstline = reducespace(lines[0])
    numproblems = len(firstline.split(' '))
    linelength = max([len(t) for t in lines])
    if (linelength+1) % numproblems == 0:
        problemlength = int((linelength+1)/numproblems)
    else: raise ValueError("this is bad")
    problemstartpoints = [x for x in range(0,linelength,problemlength)]
    numlines = len(lines)
    # everything above is just defining math to make this easier

    problems = ['']*numproblems
    for problemnumber in range(numproblems):
        for linenumber, line in enumerate(lines):
            line = line + ' '
            #print("prob", problemnumber, "line", linenumber, line)
            st = problemstartpoints[problemnumber]
            en = st + problemlength
            toadd = line[st:en]
            problems[problemnumber] += toadd

    d = {"all lines" : lines, "first line" : firstline, "number of problems" : numproblems,
         "longest line length": linelength, "problem length" : problemlength, "problem starts" : problemstartpoints,
         "number of lines" : numlines}
    return problems, d

def packcolumns(lines):
    width = max(len(s) for s in lines)
    padded = [s.rjust(width) for s in lines]

    result = []
    for col in range(width):
        digits = [row[col] for row in padded if row[col] != ' ']
        result.append(int(''.join(digits)))

    return result


def convertproblemtoints(input):
    p,d = processmatrix(input)
    problem = p[0]
    stripped = reducespace(problem)
    mathtype = stripped[-1]
    mathspot = problem.find(mathtype)
    numbers = problem[0:mathspot]
    problemlength = d['problem length']
    numlines = d['number of lines']
    splitted = [numbers[(n*problemlength):(n*problemlength)+(problemlength-1)] for n in range(0,numlines)]
    # there are a lot of assumptions about problemlength being the same here lol


    return problem, mathtype, numbers, problemlength, splitted


#print(example)
#print(processmatrix(example)[0])

print(convertproblemtoints(example))