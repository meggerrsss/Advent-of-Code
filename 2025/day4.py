with open(r'2025\inputs\day4input.txt', 'r') as file:
    input = file.read()


example = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

# 4 in a row causes a problem
# nope i misinterpreted this. 8 AROUND it

def maxinrow(line):
    sections = []
    count = 1
    for ind,spot in enumerate(line):
        cap = len(line)
        if ind+1 < cap:
            if line[ind+1] == spot and ind+1 <= cap:
                count += 1
            elif line[ind+1] != spot:
                sections.append(count)
                count = 1
        if ind+1 == cap:
            if line[ind] == line[ind-1]:
                #count += 1
                sections.append(count)
            else:
                sections.append(1)
    return sections

def doable(row, tolerance):
    if max(maxinrow(row)) >= tolerance: return False
    else: return True


examplematrix = example.split('\n')
inputmatrix = input.split('\n')

def friendsindex(matrix, i, j, nrows, ncols):
    if i == 0: # top edge
        if j == 0: # top left corner
            friends = [[i+1,j  ], [i  ,j+1], [i+1,j+1]]
        elif j == ncols-1: # top right corner
            friends = [[i+1,j  ], [i  ,j-1], [i+1,j-1]]
        else: # top edge
            friends = [[i  ,j-1],           [i  ,j+1],
                       [i+1,j-1], [i+1,j  ],[i+1,j+1]]
    elif i == nrows-1: # bottom edge
        if j == 0: # bottom left corner
            friends = [[i-1,j  ], [i  ,j+1], [i-1,j+1]]
        elif j == ncols-1: # bottom right corner
            friends = [[i-1,j  ], [i  ,j-1], [i-1,j-1]]
        else: # bottom edge
            friends = [[i-1,j-1], [i-1,j  ],[i-1,j+1],
                       [i  ,j-1],           [i  ,j+1]]
    else: # middle
        friends = [[i-1,j-1], [i-1,j  ],[i-1,j+1],
                   [i  ,j-1],           [i  ,j+1],
                   [i+1,j-1], [i+1,j  ],[i+1,j+1]]
        for x,y in friends:
            if x<0 or x>nrows-1:
                friends.remove([x,y])
            if y<0 or y>ncols-1:
                friends.remove([x,y])
    return friends

def countfriends(matrix, i, j, nrows, ncols, bad="@"):
    friends = friendsindex(matrix, i, j, nrows, ncols)
    count = 0
    for friendx,friendy in friends:
        if matrix[friendx][friendy] == bad:
            count+=1
    return count


def comfy(matrix, tolerance, good="@"):
    nrows,ncols = len(matrix), len(matrix[1])
    extractable = []
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if countfriends(matrix,i,j,nrows,ncols) < tolerance and matrix[i][j]==good:
                extractable.append([i,j])
    return extractable

#print(len(comfy(examplematrix,4)))
#print(len(comfy(inputmatrix, tolerance = 4)))

def removecomfy(matrix, tolerance, new='.'):
    extractable = comfy(matrix,tolerance)
    #print(f"removed {len(extractable)} rolls")
    for i,j in extractable:
        matrix[i] = str(matrix[i][:j] + new + matrix[i][j + 1:])
    return matrix

def iterate(matrix,tolerance,removed = 0):
    extractable = comfy(matrix,tolerance)
    while len(extractable) > 0:
        extractable = comfy(matrix,tolerance)
        removed = removed+len(extractable)
        matrix = removecomfy(matrix, tolerance)
        iterate(matrix, tolerance, removed = removed)
    return matrix,removed

#print(iterate(examplematrix, 4))



extractable = comfy(inputmatrix,4)
removed = 0
while len(extractable) > 0:
    inputmatrix = removecomfy(inputmatrix,4)
    removed += len(extractable)
    extractable = comfy(inputmatrix,4)
    print(removed)