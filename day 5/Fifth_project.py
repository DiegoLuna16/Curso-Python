import random

lista_palabras = ['hola','adios','coma','ala','escuela']

vidas = 6

def escoger_palabra(lista):
    return random.choice(lista)

palabra_secreta = escoger_palabra(lista_palabras)

def esconder_palabra():
    palabra_codificada = []
    for char in palabra_secreta:
        palabra_codificada.append('-')
    return "".join(palabra_codificada)

palabra_codificada = esconder_palabra()

def validar_letra(letra):
    if str(letra).isalpha():
        return True
    else:
        return False
    
def pedir_letra():
    letra = input("\nIngresa una letra: \n").lower()
    if validar_letra(letra):
        return str(letra)
    else:
        return pedir_letra()
                
def validar_letra_en_palabra(letra):
    if letra in palabra_secreta:
        return letra
    return False

        
def procesar_letra(letra):
    resultado = validar_letra_en_palabra(letra)
    matches = []
    if type(resultado) == str:
        for index, char in enumerate(palabra_secreta):
            if resultado == char:
                matches.append(index)
    if len(matches) > 0:
        return matches
    else:
        return False
    
def restar_vidas():
    global vidas
    vidas -= 1
    print(f"Te quedan {vidas} vidas")  

def mostrar_resultado(letra_escogida):
    global palabra_codificada
    resultado = procesar_letra(letra_escogida)
    if type(resultado) != bool:
        palabra_codificada_list = list(palabra_codificada)
        for x in resultado:
            palabra_codificada_list[x] = letra_escogida
        palabra_codificada = "".join(palabra_codificada_list)
        print(palabra_codificada)
    else:
        restar_vidas()
        print(palabra_codificada)     
        
def ganador():
    global palabra_secreta
    print("\n¡Felicidades, eres un ganador 🏆!\n")   
    print(f"¡La palabra secreta era {palabra_secreta}!\n")   

def perdedor():
    global palabra_secreta
    print("\nPerdiste😭!\n")   
    print(f"¡La palabra secreta era {palabra_secreta}!\n")   
    
    
def jugar():
    global vidas, palabra_codificada
        
    while vidas > 0 and "-" in palabra_codificada:
        letra = pedir_letra()
        mostrar_resultado(letra)
        
    if "-" not in palabra_codificada:
        ganador()
    else:
        perdedor()
        
jugar()