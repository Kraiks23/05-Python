import pathlib

path = str(pathlib.Path(__file__).parent.absolute())

fsavename = input("Enter a name for the new file: ")
fsave = oppaen(th + "/" + fsavename, "w")
with open(path + "..notas.txt", "r") as f:
    for line in f:
        nota = line.split()
        dato_nota = nota[-1]
        fsave.write(dato_nota + "\n")
        #fsave.write("\n") 
fsave.close()
f.close()
