class Persona:
    
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido
        
class Cliente(Persona):
    
    def __init__(self, nombre, apellido,numero_cuenta,balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance
    
    def __str__(self):
        return f"Nombre: {self.nombre} {self.apellido}\nNumero de cuenta: {self.numero_cuenta}\nBalance: {self.balance}"
    
    def depositar(self):
        monto = int(input("Ingrese el monto a depositar: "))
        self.balance += monto
        print(f"Tu nuevo balance es {self.balance}")
    
    def retirar(self):
        monto = int(input("Ingrese el monto a depositar: "))
        if self.balance >= monto:
            self.balance -= monto
            print(f"Tu nuevo balance es {self.balance}")
        else:
            print("No cuentas con los suficientes fondos para realizar la operación")
            print(f"Tu saldo actual es {self.balance}")

def crear_cliente():
    print("\n--- Crear nuevo cliente ---")
    nombre = input("Nombre: ").strip()
    apellido = input("Apellido: ").strip()
    numero_cuenta = input("Número de cuenta: ").strip()

    while True:
        try:
            balance_inicial = float(input("Balance inicial: "))
            break
        except ValueError:
            print("❌ Ingresa un número válido.\n")

    cliente = Cliente(nombre, apellido, numero_cuenta, balance_inicial)
    print("\n✅ Cliente creado exitosamente.")
    print(cliente)
    return cliente

def mostrar_menu():
    print("""
        [1] - Realizar retiro
        [2] - Realizar deposito
        [3] - Salir del programa
          """)

def elegir_opcion():
    while True:
        mostrar_menu()
        eleccion = input("Ingresa una opción: ")

        if eleccion.isdigit():
            eleccion = int(eleccion)
            if eleccion in range(1,4):
                return eleccion
        
        print("❌ Opción inválida. Intenta nuevamente.\n")

def inicio(cliente):
    continuar = False
        
    while not continuar:
        eleccion = elegir_opcion()
        
        if eleccion == 1:
            cliente.retirar()
        elif eleccion == 2:
            cliente.depositar()
        elif eleccion == 3:
            continuar = True
 
diego = Cliente('Diego','Luna',1234,10000) 
        
inicio(diego)