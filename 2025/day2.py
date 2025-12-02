with open(r'2025\inputs\day2input.txt', 'r') as file:
    input = file.read()

import textwrap

example = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

def repeat(n:int, style = '') -> bool:
    stringnum = str(n)
    #if not len(i) % 2 == 0: return False
    if style == 'twice':
        duration = int(len(stringnum)/2)
        parts = textwrap.wrap(stringnum, duration)
        #print(f"{duration} parts out of twice split into {parts}")
        repeated = all(x == parts[0] for x in parts)
        return repeated
    else:
        testuptolength = int(len(stringnum)/2)
        truth = False
        for duration in range(testuptolength):
            parts = textwrap.wrap(stringnum, duration+1)
            repeated = all(x == parts[0] for x in parts)
            if repeated: truth = True
            #print(f"{duration+1} parts out of {testuptolength} split into {parts}, returns {repeated}")
        return truth

def findinvalids(id:str) -> list:
    first,last = [int(t) for t in id.split('-')]
    invalids = [x for x in range(first,last+1) if repeat(x)]
    #print(id, invalids)
    return invalids


def suminvalids(listid:str) -> int:
    val = 0
    for id in listid.split(","):
        invalids = findinvalids(id)
        val += sum(invalids)
        #print(id, val)
    return val

print(f"example {suminvalids(example)}")
print(f"final {suminvalids(input)}")
