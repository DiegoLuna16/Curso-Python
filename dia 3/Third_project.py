texto = input("Ingresa cualquier texto: ")

def counterLettersInText(text):
    for i in range(0,3):
        letra = input("Ingresa una letra a ser buscada en el texto: ")
        if(letra not in text):
            print(f"La letra {letra} no esta en el texto")
        else:
            print(f"La letra {letra} aparece en el texto {text.count(letra)} veces")
    
def totalWords(text):
    print(f"El total de palabras en el texto es de {len(text)}")
    
def firstAndLastLetter(text):
    print(f"La primera letra del texto es {text[0]}")
    print(f"La ultima letra del texto es {text[int(len((text))-1)]}")
    
def invertedText(text):
    lista_texto_invertido = text.split()
    lista_texto_invertido.reverse()
    texto_invertido = " ".join(lista_texto_invertido)
    print(f"Las palabras del texto en orden inverso seria: {texto_invertido}")
    
def isPythonInText(text):
    texto_comparativo = text.lower()
    print(f"Aparece la palabra Python en el texto: {"python" in texto_comparativo}")
    
counterLettersInText(texto)
totalWords(texto)
firstAndLastLetter(texto)
invertedText(texto)
isPythonInText(texto)
