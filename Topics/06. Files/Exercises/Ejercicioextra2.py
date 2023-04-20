import pathlib

path = str(pathlib.Path(__file__).parent.absolute())

totalines = 0 # Empezamos con la variable a valor 0
notatotal = 0 # Empezamos con la variable a valor 0
with open(path + "//newnotas.txt", "r") as f:
    for line in f: #Por cada línea en el archivo:
        nota = int(line) # Hago casting para cambiar el tipo de string a entero.
        notatotal += nota # variable que incrementa por cada loop. (+=)
        print (notatotal) # Imprimo para ver que hace el loop bien.
        totalines += 1 # Otra variable que incrementa por cada loop. Contando las veces del loop.
notamedia = notatotal / totalines # Operación sencilla para sacar la media.
print("La nota media es de: ", notamedia) # Print con una string para dar formato y la variable que nos da el resultado.