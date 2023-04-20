def remove_letter(letter, string):
    result = ""
    for char in string:
        if char != letter:
            result += char
    return result

assert(remove_letter("a", "apple") == "pple")
assert(remove_letter("a", "banana") == "bnn")
assert(remove_letter("z", "banana") == "banana")
assert(remove_letter("i", "Mississippi") == "Msssspp")
assert(remove_letter("b", "") == "")
assert(remove_letter("b", "c") == "c")

resultado = remove_letter("a", "apple")
print(resultado)  
prueba2 = remove_letter("L", "Lost ark")
print(prueba2)
