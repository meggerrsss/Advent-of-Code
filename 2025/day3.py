with open(r'2025\inputs\day3input.txt', 'r') as file:
    input = file.read()

import itertools

example = "987654321111111\n811111111111119\n234234234234278\n818181911112111"
#joltages

ie = '987654321111111'
fulllen = len(input.split('\n')[0])

def bitGen(n, x):
    return [''.join(i) for i in itertools.product('01', repeat=n) if sum([int(t) for t in ''.join(i)]) <= x]

def enable(n, x):
    # n is length, x is allowed enabled bits
    startlist = bitGen(n, x)
    #filt = [z for z in startlist if sum([int(y) for y in z]) <= x]
    return startlist

fulloptions = enable(100,12)
print(fulloptions)

def largest2(num):
    length = len(num)
    largest = 0
    for f,first in enumerate(num):
        following = num[f+1:]
        for g,second in enumerate(following):
            compressed = int(first+second)
            if largest < compressed: largest = compressed
    return largest

def largestn(num, n):
    length = len(num)
    enablecombos = enable(length, n)
    #print(enablecombos)
    sums = []
    for combo in enablecombos:
        compress = ''
        for spot,value in enumerate(combo):
            #print(spot, value)
            if value == '1':
                compress += num[spot]
        #print(compress)
        sums.append(compress)

    sumsnum = [int(n) for n in sums if n != '']
    return max(sumsnum)

def bankssum(lst, n):
    banks = lst.split('\n')
    sum = 0
    for item in banks:
        sum += largestn(item, n)
    return sum


print(bankssum(example, 12))
print(bankssum(input, 12))
