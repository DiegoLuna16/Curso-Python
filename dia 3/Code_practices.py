# Práctica Método Index() 1

palabra = "ordenador"
 
print(palabra[4])
# Práctica Método Index() 2

frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
 
print(frase.index("práctica"))
# Práctica Método Index() 3

frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
 
print(frase.rindex("práctica"))
# Práctica Sub-Strings 1

frase = "Controlar la complejidad es la esencia de la programación"
 
print(frase[:9])
# Práctica Sub-Strings 2

frase = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
 
print(frase[8::3])
# Práctica Sub-Strings 3

frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
 
print(frase[::-1])

frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."


# Práctica Métodos de String 1

frase = "Especialmente en las comunicaciones electrónicas, la escritura enteramente en mayúsculas equivale a gritar."
 
print(frase.upper())
# Práctica Métodos de String 2

lista_palabras = ["La","legibilidad","cuenta."]
 
frase = " ".join(lista_palabras)
 
print(frase)
# Práctica Métodos de String 3

frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
 
print(frase.replace("difícil", "fácil").replace("mala","buena"))

# Práctica Propiedades de Strings 1

palabra = "Repetición"
 
print(palabra * 15)
# Práctica Propiedades de Strings 2

haiku = '''
Tierra mojada
mis recuerdos de viaje,
entre las lluvias
'''
 
print("agua" not in haiku)
# Práctica Propiedades de Strings 3

palabra = "electroencefalografista"
 
print(len(palabra))

# Práctica Listas 1

mi_lista = ["uno", 2, 3.33, "four", True]
# Práctica Listas 2

medios_transporte = ["avión", "auto", "barco", "bicicleta"]
medios_transporte.append("motocicleta")
# Práctica Listas 3

frutas = ["manzana", "banana", "mango", "cereza", "sandía"]
 
eliminado = frutas.pop(2)

# Práctica Diccionarios 1

mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}
# Práctica Diccionarios 2

mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
print(mi_dict["puntos"]["points2"][1])
# Práctica Diccionarios 3

mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}
 
mi_dic["edad"] = 36
mi_dic["ocupacion"] = "Editora"
mi_dic["pais"] = "Colombia"