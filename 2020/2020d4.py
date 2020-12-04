f = open('2020/inputs/2020d4input.txt', 'r')
inp = f.read()
f.close() 
linp = inp.split("\n\n")

def inn(st,key): # is the necessary value IN the string
  st = st.replace(":"," ")
  st = st.replace("\n"," ")
  return key in st.split(" ")

needed = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]

def countvalues(st,need = needed): # how many necessary values are in the string
  v = [inn(st,k) for k in need]
  return sum(v)

def numvalid(li): #counting how many people have valid passports
  counter = 0
  for person in li:
    if countvalues(person) == len(needed):
      counter += 1
  return counter
#print(numvalid(linp))


#part two aka shit should have used dictionaries
def dictify(st):
  st = st.replace("\n"," ").split(" ")
  d = {}
  for element in st:
    key = element[0:3]
    value = element[4:]
    d[key] = value
  return d

def people(li):
  s = [dictify(x) for x in li]
  return s

colorkey = ['a','b','c','d','e','f','0','1','2','3','4','5','6','7','8','9']

def validcolour(st):
  coldig = [x in colorkey for x in st[1:]]
  if st[0] == "#" and sum(coldig) ==6:
    return True 
  else: return False

def extravalid(person, need = needed): #a person is a dictionary
  r = [element in person.keys() for element in need]
  #if sum(r) < len(need):
  #  return False
  x = [0] * len(need)
  if 'byr' in person.keys():
     x[0] = int(person['byr']) <= 2002 + int(person['byr']) >= 1920
  if 'iyr' in person.keys():
     x[1] = int(person['iyr']) <= 2020 + int(person['iyr']) >= 2010
  if 'eyr' in person.keys():
     x[2] = int(person['iyr']) <= 2030 + int(person['iyr']) >= 2020
  if 'hgt' in person.keys():
    units = person['hgt'][-2:]
    value = int(person['hgt'][:-2])
    if units == 'cm' and value >=150 and value <= 193:
      x[3] = True 
    elif units == 'in' and value >=59 and value <= 76:
      x[3] = True 
  if 'hcl' in person.keys():
    x[4] = validcolour(person['hcl'])
  return r , x

print(linp[0])
print(extravalid(dictify(linp[0])))
