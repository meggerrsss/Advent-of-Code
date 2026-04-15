with open(r'2025\inputs\day5input.txt', 'r') as file:
    input = file.read()

import itertools
example = """3-5\n10-14\n16-20\n12-18\n\n1\n5\n8\n11\n17\n32"""

def freshlist(s):
    fresh,items = s.split("\n\n")
    fresh = fresh.split("\n")
    freshlist = set()
    for r in fresh:
        low,high = r.split('-')
        for num in range(int(low),int(high)+1):
            freshlist.add(num)
    #freshlistset = set(freshlist)
    #items = items.split("\n")
    return freshlist

def countfresh(s):
    freshset = freshlist(s)
    items = s.split("\n\n")[1]
    items = [int(x) for x in items.split("\n")]
    overlap = freshset.intersection(items)
    count = len(overlap)
    return count

#print(countfresh(example))
#print(countfresh(input))
##print(len(freshlist(input)))

### version 2
# iterate through items, check freshlist start / end if between, collect


def checkfresh(number, freshlistt):
    fresh = []
    for freshroster in freshlistt:
        length = freshroster.split('-')
        start,end = int(length[0]),int(length[1])
        if number >= start and number <= end:
            return True
    return False


def define(string):
    fresh,items = string.split("\n\n")
    fresh = fresh.split("\n")
    items = [int(i) for i in items.split("\n")]
    return items, fresh


def iterate(string):
    items, fresh = define(string)
    thefreshitems = []
    for i in items:
        #print(i)
        if checkfresh(int(i), fresh): thefreshitems.append(i)
    return len(thefreshitems)

#print(iterate(example))
#print(iterate(input))


# version 3, it is now april, and i have time at work

def freshitemrange(s):
    # just converting one line to a range
    f,l = s.split('-')
    r = range(int(f), int(l)+1)
    return [x for x in r]

def actuallyfresh(l):
    freshmasterlist = []
    for s in l:
        freshmasterlist.append(freshitemrange(s))
    freshmasterlist = list(itertools.chain.from_iterable(freshmasterlist))
    return set(freshmasterlist)

def ranges(l):
    return [(int(a), int(b)) for a, b in (s.split('-') for s in l)]

def countfreshfromrequests(inputt, overrideitem = '', overridefreshlist = ''):
    if overrideitem == '':
        items = define(inputt)[0]
    else:
        items = overrideitem
    if overridefreshlist == '':
        fresh = define(inputt)[1]
        fresh = ranges(fresh)
    else:
        fresh = overridefreshlist
    counted = 0
    for item in items:
        for f,l in fresh:
            if f <= item <= l:
                counted += 1
                break # this is important
    return counted

#items, fresh = define(input)
#print(countfreshfromrequests(input))

# version 4, by ranges instead i guess?

def compareranges(r1, r2):
    newrange = [0,0]
    if r1[1] < r2[0]-1:
        return("no overlap")
    elif r2[1] < r1[0]-1:
        return("no overlap")
    else:
        newrange[0] = min(r1[0],r2[0])
        newrange[1] = max(r1[1],r2[1])
    return newrange

#print(compareranges([3,5], [6,10]))
# no im' going back to version 3 for part 2


def p1(input):
    return countfreshfromrequests(input)

print(p1(example))
print(p1(input))


def findhighestfresh(freshlist):
    # freshlist is an output of ranges
    h = 0
    for item in freshlist:
        if item[1] > h: h = item[1]
    return h


def p2v1(input):
    items, fresh = define(input)
    highestitem = findhighestfresh(ranges(fresh))
    print(f"highest found to be {highestitem}")
    counted = countfreshfromrequests(input, overrideitem = range(0, highestitem+1))
    return counted

print(p2v1(example))
#print(p2v1(input))

# version 3.5
def mergeranges(ranges):
    ranges = sorted(ranges)
    merged = []
    for l, h in ranges:
        if not merged or l > merged[-1][1] + 1:
            merged.append([l, h])
        else:
            merged[-1][1] = max(merged[-1][1], h)
    return merged

def countfreshitemstotal(mranges):
    return sum(h - l + 1 for l, h in mranges)

def p2(input):
    items, fresh = define(input)
    theranges = ranges(fresh)
    mranges = mergeranges(theranges)
    s = countfreshitemstotal(mranges)
    return s


print(p2(input))
