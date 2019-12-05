#advent 2019 day 2 
#input formatting
inp = "3,225,1,225,6,6,1100,1,238,225,104,0,1101,72,36,225,1101,87,26,225,2,144,13,224,101,-1872,224,224,4,224,102,8,223,223,1001,224,2,224,1,223,224,223,1102,66,61,225,1102,25,49,224,101,-1225,224,224,4,224,1002,223,8,223,1001,224,5,224,1,223,224,223,1101,35,77,224,101,-112,224,224,4,224,102,8,223,223,1001,224,2,224,1,223,224,223,1002,195,30,224,1001,224,-2550,224,4,224,1002,223,8,223,1001,224,1,224,1,224,223,223,1102,30,44,225,1102,24,21,225,1,170,117,224,101,-46,224,224,4,224,1002,223,8,223,101,5,224,224,1,224,223,223,1102,63,26,225,102,74,114,224,1001,224,-3256,224,4,224,102,8,223,223,1001,224,3,224,1,224,223,223,1101,58,22,225,101,13,17,224,101,-100,224,224,4,224,1002,223,8,223,101,6,224,224,1,224,223,223,1101,85,18,225,1001,44,7,224,101,-68,224,224,4,224,102,8,223,223,1001,224,5,224,1,223,224,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,7,677,226,224,102,2,223,223,1005,224,329,101,1,223,223,8,677,226,224,1002,223,2,223,1005,224,344,1001,223,1,223,1107,677,677,224,102,2,223,223,1005,224,359,1001,223,1,223,1107,226,677,224,102,2,223,223,1005,224,374,101,1,223,223,7,226,677,224,102,2,223,223,1005,224,389,101,1,223,223,8,226,677,224,1002,223,2,223,1005,224,404,101,1,223,223,1008,226,677,224,1002,223,2,223,1005,224,419,1001,223,1,223,107,677,677,224,102,2,223,223,1005,224,434,101,1,223,223,1108,677,226,224,1002,223,2,223,1006,224,449,101,1,223,223,1108,677,677,224,102,2,223,223,1006,224,464,101,1,223,223,1007,677,226,224,102,2,223,223,1006,224,479,101,1,223,223,1008,226,226,224,102,2,223,223,1006,224,494,101,1,223,223,108,226,226,224,1002,223,2,223,1006,224,509,101,1,223,223,107,226,226,224,102,2,223,223,1006,224,524,101,1,223,223,1107,677,226,224,102,2,223,223,1005,224,539,1001,223,1,223,108,226,677,224,1002,223,2,223,1005,224,554,101,1,223,223,1007,226,226,224,102,2,223,223,1005,224,569,101,1,223,223,8,226,226,224,102,2,223,223,1006,224,584,101,1,223,223,1008,677,677,224,1002,223,2,223,1005,224,599,1001,223,1,223,107,226,677,224,1002,223,2,223,1005,224,614,1001,223,1,223,1108,226,677,224,102,2,223,223,1006,224,629,101,1,223,223,7,677,677,224,1002,223,2,223,1005,224,644,1001,223,1,223,108,677,677,224,102,2,223,223,1005,224,659,101,1,223,223,1007,677,677,224,102,2,223,223,1006,224,674,101,1,223,223,4,223,99,226"
inputs = [1]
#a = inputs.pop(0)
#print(a,inputs)
#print("the 225th input is "+str(inp[225]))

import math 

def form(st): # changing string list to list of int
    linp = str.split(st,",")
    for i in range(0, len(linp)): 
        linp[i] = int(linp[i]) 
    return(linp)


def pieces(n):
    de = n % 100 # cents, referring to the actual instruction from now on
    c = ((n - de) % 1000) / 100 # position or immediate of 1st parameter
    b = ((n - c*100 - de) % 10000) / 1000 # position or immediate of 2nd parameter
    a = (n - 1000*b - 100*c - de) / 10000 # position or immediate of 3rd parameter
    return (int(a),int(b),int(c),int(de))


def heaviside(a,b,c): #a = 0 or 1
    return b*(1-a)+c*a
    

def thing3(li,d=0): 
    li = form(li)
    i = 0
    while i < len(li):
        p = pieces(li[i]) #p[3] is true instruction, p[2,1,0] are pos/imm values of parm 1,2,3 resp. p() = (a,b,c,de)
        if p[3] == 99:
            break
        elif p[3] == 1:
            if d: 
                print("intcode is",(li[i:i+4]))
                print("pieces are",p,str(p[3])+" means add")
                #print(li[li[i+1]],li[li[i+2]])
            if li[i+1]<0 and li[i+2]>=0:
                li[li[i+3]] = li[i+1] + heaviside(p[1],li[li[i+2]],li[i+2]) 
            elif li[i+2]<0 and li[i+1]>=0:
                li[li[i+3]] = heaviside(p[2],li[li[i+1]],li[i+1]) + li[i+2] 
            elif li[i+2]<0 and li[i+1]<0:
                li[li[i+3]] = li[i+1] + li[i+2] 
            else:
                li[li[i+3]] = heaviside(p[2],li[li[i+1]],li[i+1]) + heaviside(p[1],li[li[i+2]],li[i+2]) 
            i += 4
        elif p[3] == 2:
            if d: 
                print("intcode is",(li[i:i+4]))
                print("pieces are",p,str(p[3])+" means multiply")
                print(li[li[i+1]],li[li[i+2]])
            li[li[i+3]] = heaviside(p[2],li[li[i+1]],li[i+1]) * heaviside(p[1],li[li[i+2]],li[i+2])
            i += 4
        elif li[i] == 3: # not p[3] because it's not allowed to be immediate mode
            if d: 
                print("intcode is",(li[i:i+2]))
                print("pieces are",p,str(p[3])+" means store new input")
            if inputs:
                li[li[i+1]] = int(inputs.pop(0))
                print(li[li[i+1]],type(li[li[i+1]]))
            else:
                li[li[i+1]] = input("gimme a number: ")
            i += 2
        elif p[3] == 4:
            print("pieces are",p,str(p[3])+" means output value")
            i += 2
        else: 
            return str(p[3])+" means no correct instruction"
    if d: print(li)
    return li[0]

#day 2 tests
t0="1,9,10,3,2,3,11,0,99,30,40,50" #3500
assert(thing3(t0)==3500)
t1="1,0,0,0,99" #2 
assert(thing3(t1)==2)
t2="2,3,0,3,99" #2
assert(thing3(t2)==2)
t3="2,4,4,5,99,0" #2
assert(thing3(t3)==2)
t4="1,1,1,4,99,5,6,0,99" #30
assert(thing3(t4)==30)
d2test = "1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,5,19,23,2,9,23,27,1,6,27,31,1,31,9,35,2,35,10,39,1,5,39,43,2,43,9,47,1,5,47,51,1,51,5,55,1,55,9,59,2,59,13,63,1,63,9,67,1,9,67,71,2,71,10,75,1,75,6,79,2,10,79,83,1,5,83,87,2,87,10,91,1,91,5,95,1,6,95,99,2,99,13,103,1,103,6,107,1,107,5,111,2,6,111,115,1,115,13,119,1,119,2,123,1,5,123,0,99,2,0,14,0"
assert(thing3(d2test)==3101844)
d2testl = "1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,6,19,2,19,6,23,1,23,5,27,1,9,27,31,1,31,10,35,2,35,9,39,1,5,39,43,2,43,9,47,1,5,47,51,2,51,13,55,1,55,10,59,1,59,10,63,2,9,63,67,1,67,5,71,2,13,71,75,1,75,10,79,1,79,6,83,2,13,83,87,1,87,6,91,1,6,91,95,1,10,95,99,2,99,6,103,1,103,5,107,2,6,107,111,1,10,111,115,1,115,5,119,2,6,119,123,1,123,5,127,2,127,6,131,1,131,5,135,1,2,135,139,1,139,13,0,99,2,0,14,0"
assert(thing3(d2testl)==3058646)
d2testg = "1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,2,19,9,23,1,23,5,27,2,6,27,31,1,31,5,35,1,35,5,39,2,39,6,43,2,43,10,47,1,47,6,51,1,51,6,55,2,55,6,59,1,10,59,63,1,5,63,67,2,10,67,71,1,6,71,75,1,5,75,79,1,10,79,83,2,83,10,87,1,87,9,91,1,91,10,95,2,6,95,99,1,5,99,103,1,103,13,107,1,107,10,111,2,9,111,115,1,115,6,119,2,13,119,123,1,123,6,127,1,5,127,131,2,6,131,135,2,6,135,139,1,139,5,143,1,143,10,147,1,147,2,151,1,151,13,0,99,2,0,14,0"
assert(thing3(d2testg)==4576384)

u0="1002,4,3,4,33" #1002
assert(thing3(u0)==1002)
u1="1101,100,-1,4,0" # 

print(thing3(u1,1))
#print(thing3(inp,1))

