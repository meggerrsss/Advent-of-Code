with open(r'2025\inputs\day5input.txt', 'r') as file:
    input = file.read()

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

print(countfresh(example))
#print(countfresh(input))
print(len(freshlist(input)))

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

print(iterate(example))
print(iterate(input))