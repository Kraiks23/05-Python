def analyze_text(text):
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    text = "".join(char for char in text if char is not punctuation)
    words = text.split()
    total_words = len(words)
    words_with_e = sum("e" in word for word in words)
    percentage_with_e = (words_with_e / total_words)*100
    analysis = "Your text contains {} words, of which {} ({:.1f}%) contain an 'e'.".format(total_words, words_with_e, percentage_with_e)
    return analysis

                 

text = """En un lugar de la Mancha, de cuyo nombre no quiero 
acordarme, no ha mucho tiempo que vivía un hidalgo de los de 
lanza en astillero, adarga antigua, rocín flaco y galgo corredor. 
Una olla de algo más vaca que carnero, salpicón las más noches, 
duelos y quebrantos los sábados, lantejas los viernes, algún 
palomino de añadidura los domingos, consumían las tres partes 
de su hacienda"""
result = analyze_text(text)
print (result)