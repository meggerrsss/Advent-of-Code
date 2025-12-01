with open(r'2025\inputs\day1input.txt', 'r') as file:
    input = file.read()

def value(input, start=0):
    try: inlist = input.split('\n')
    except AttributeError: inlist = input
    st = start
    crosses = 0
    zeros = 0
    for item in inlist:
        dir = item[0]
        amt = int(item[1:])
        print (start, dir, amt)
        if dir == 'L':
            if start <= amt:
                crosses += (amt-start)//100 +1
                if start == 0: crosses -= 1 # cursed
            start -= amt
            start = start%100
            if start == 0: zeros += 1
            print(start, crosses)
        elif dir == 'R':
            if start + amt >= 100:
                crosses += (amt+start)//100
            start += amt%100
            start = start%100
            if start == 0: zeros += 1
            print(start, crosses)

    str = f"starting at {st}, ending at {start}, hitting zero {zeros}, crossing zero {crosses}"
    return str

print(value(input, start = 50))

test = ['L68','L30','R48','L5','R60','L55','L1','L99','R14','L82']
print(value(test,start = 50))