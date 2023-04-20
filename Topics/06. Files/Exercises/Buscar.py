import pathlib

path = str(pathlib.Path(__file__).parent.absolute())

search = input("Introduce el texto a buscar: ")
fhand = open(path + '/text.txt')
for line in fhand:
    line = line.rstrip(search)
    if not search in line:
        continue
    print(line)

fhand.close()