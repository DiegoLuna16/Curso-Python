from random import randint

nombre = input("Ingresa tu nombre: ")
vidas = 8

print(f"\nHola {nombre}!")
print(f"\nBienvenido al Adivina el numero")
print("\n- Tienes 8 intentos para adivinar un numero del 1 al 100")

numero = randint(1,100)

while vidas > 0:
    
    if vidas < 8 and vidas > 1:      
        print(f"\nTe quedan {vidas} vidas")
    elif vidas == 1:
        print("\nTe queda una sola vida...")
    
    vidas -= 1
    n = int(input("\nIngresa un numero: "))
    
    if n < numero:
        print(f"\nEl numero secreto es mayor que {n}")
        continue
    elif n > numero:
        print(f"\nEl numero secreto es menor que {n}")
        continue
    elif n == numero:
        print(f"\n¡Felicidades!\nEncontraste {numero} que era el numero secreto en {8 - vidas} intentos")
        break
    else:
        print("\nEl numero tiene que estar entre 1 a 100")
else:
    print(f"\nPerdiste :(\nEl numero secreto era {numero}")