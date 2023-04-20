import pathlib

path = str(pathlib.Path(__file__).parent.absolute())

fname = input('Enter the file name: ')
try:
    fopen = open(path + '/' + fname, 'r')
except:
    print('File ', fname, ' not found')
    quit()

ext = pathlib.Path(fname).suffix #.suffix Mantiene la extensión del archivo, el "sufijo"
fsavename = pathlib.Path(fname).stem + 'Unnumbered' + ext 

fsave = open(path + "/" + fsavename, "w")
for line in fopen: #El siguiente bucle se repite todo el rato por cada línea dentro del archivo fopen.
    line = line[5:]# La función [5:] ignora los 5 primeros caracteres de la linea.
    fsave.write(line)#Esta función escribe la línea anterior en el archivo fsave.
fopen.close()#Esto cierra el archivo.   
fsave.close()# Esto cierra el otro archivo.














