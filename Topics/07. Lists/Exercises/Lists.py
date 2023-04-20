a = [1,2,3]
b = [4,5,6]
print (len(b))#Consulto la longitud de la lista
print (b[0])#Imprimo el indexado a 0 en la lista = 4
print (b[2] + a[0])#Imprimo la suma del indexado 2 en lista B, y el indexado 0 de lista A.

lista = [1,4,8,12,15]#Creo una lista con X valores.
suma = sum(lista)#Creo una variable con la "sum" de los valores dentro de "lista"
print("Max:", max(lista))
print("Sum is: ", suma)#Imprimo la suma.

def replace(s, old, new):#Argumentos s= string original, donde se buscará la substring old y se reemplazará por new. Old es la que se buscará para
    return s.replace(old, new)#En esta línea llamamos a replace en la string "s", y le damos los dos argumentos a cambiar.
s = "I love spom! Spom is my favorite food. Spom, spom, yum!"
assert(replace(s,"om","am")) == ("I love spam! Spam is my favorite food. Spam, spam, yum!")



def replace2(s, old, new):
    return new.join(s.split(old)) #Aquí es más díficil de ver. Si s es "Mississippi" y old es "i", el resultado de s.split(old) sería ["M", "ss", "ss", "pp", ""]. 
#La cadena se divide en cinco subcadenas, separadas por las cuatro ocurrencias de "i" en la cadena original.
#Luego usamos el método .join para unir todo eso en una string nueva, usando "new" como separador. Añadiendo ["M","new","ss","new","ss","new","pp","new" ""]
s = "I love spom! Spom is my favorite food. Spom, spom, yum!"
assert(replace2(s,"om","am") == "I love spam! Spam is my favorite food. Spam, spam, yum!")
print(replace2(s,"om","am"))

def replace3(s, old, new):#Poner anotaciones más tarde.
    words = s.split()
    count = len(words)
    indexes = range(count)
    for i in indexes:
        w = words[i]
        w = w.replace(old,new)
        words[i] = w
    return " ".join(words)