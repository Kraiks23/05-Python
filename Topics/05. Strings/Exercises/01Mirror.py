def mirror(word):
    inverted_word = word
    index = len(word) - 1
    while index >= 0:
        inverted_word += word[index]
        index -= 1
    return inverted_word

assert(mirror("good") == "gooddoog")
assert(mirror("Python") == "PythonnohtyP")
assert(mirror("") == "")
assert(mirror("a") == "aa")

word = input("Ingresa una palabra: ")
result = mirror(word)
print ("La versión espejo de tu palabra es:", result)