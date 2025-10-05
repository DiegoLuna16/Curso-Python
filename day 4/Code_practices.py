# Práctica Operadores de Comparación 1

num1 = 36
num2 = 17
mi_bool = num1 >= num2
# Práctica Operadores de Comparación 2

num1 = 25**0.5
num2 = 5
mi_bool = num1 == num2
# Práctica Operadores de Comparación 3

num1 = 64*3
num2 = 24*8
mi_bool = num1 != num2

# Práctica Operadores Lógicos 1

num1 = 36
num2 = 72/2
num3 = 48
 
 
mi_bool = num1 > num2 and num1 < num3
# Práctica Operadores Lógicos 2

num1 = 36
num2 = 72/2
num3 = 48
 
 
mi_bool = num1 > num2 or num1 < num3
# Práctica Operadores Lógicos 3

num1 = 36
num2 = 72/2
num3 = 48
 
 
mi_bool = num1 > num2 or num1 < num3

# Práctica Control de Flujo 1

num1 = int(input("Ingresa un número:"))
num2 = int(input("Ingresa otro número:"))
 
if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num2 > num1:
    print(f"{num2} es mayor que {num1}")
else:
    print(f"{num1} y {num2} son iguales")
# Práctica Control de Flujo 2

edad = 16
tiene_licencia = False
 
if edad >= 18 and tiene_licencia:
    print("Puedes conducir")
elif edad < 18:
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")
else:
    print("No puedes conducir. Necesitas contar con una licencia")

frase = "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
palabra1 = "éxito"
palabra2 = "tecnología"
 
mi_bool = palabra1 not in frase and palabra2 not in frase

#Práctica Control de Flujo 3

habla_ingles = False
sabe_python = True

if habla_ingles and sabe_python:
    print("Cumples con los requisitos para postularte")
else:
    if not habla_ingles and not sabe_python:
        print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")
    else:
        if not habla_ingles:
            print("Para postularte, necesitas tener conocimientos de inglés")
        if not sabe_python:
            print("Para postularte, necesitas saber programar en Python")
