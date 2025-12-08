import os

year = '2025'
folder = rf'.\{year}'

files = os.listdir(rf'.\{year}')
days = [f.split('.')[0][3:] for f in files if f[0]=='d']
highestday = max([int(g) for g in days])
print(highestday)

nextday = highestday+1

newscr = os.path.join(folder,f'day{nextday}.py')
newinp = os.path.join(folder,'inputs',f'day{nextday}input.txt')

with open(newscr, "w") as file:
    file.write(rf"with open(r'{year}\inputs\day{nextday}input.txt', 'r') as file:")
    file.write("\n")
    file.write(r"    input = file.read()")

with open(newinp, "w") as file:
    file.write("")