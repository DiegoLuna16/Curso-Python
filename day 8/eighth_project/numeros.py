def generador_perfumeria():
    turno = 0
    while True:
        turno += 1
        yield f"P-{turno}"

def generador_farmacia():
    turno = 0
    while True:
        turno += 1
        yield f"F-{turno}"

def generador_cosmeticos():
    turno = 0
    while True:
        turno += 1
        yield f"C-{turno}"
        
def decorador(funcion):
    generador = funcion()
    
    def otra_funcion():
        print("Su turno es: ")
        print(next(generador))
        print("Favor de esperar a su turno")
    
    return otra_funcion