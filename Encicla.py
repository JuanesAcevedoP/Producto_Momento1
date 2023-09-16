class Usuario:
    def __init__(self, nombre, numero_tarjeta):
        self.nombre = nombre
        self.numero_tarjeta = numero_tarjeta

class Bicicleta:
    def __init__(self, numero):
        self.numero = numero

class Prestamo:
    def __init__(self, usuario, bicicleta, origen, destino):
        self.usuario = usuario
        self.bicicleta = bicicleta
        self.origen = origen
        self.destino = destino

usuarios = []
bicicletas_disponibles = [Bicicleta(numero) for numero in range(1, 11)]
bicicletas_en_uso = []
prestamos = []

def registrar_usuario():
    nombre = input("Ingrese su nombre: ")
    numero_tarjeta = input("Ingrese su número de tarjeta: ")

    usuario = Usuario(nombre, numero_tarjeta)
    usuarios.append(usuario)
    print("Usuario registrado con éxito.")

def iniciar_prestamo():
    numero_tarjeta = input("Ingrese su número de tarjeta: ")
    usuario = next((u for u in usuarios if u.numero_tarjeta == numero_tarjeta), None)
    
    if usuario:
        print("Bicicletas disponibles:")
        for bicicleta in bicicletas_disponibles:
            print(f"Bicicleta {bicicleta.numero}")
        
        bicicleta_numero = input("Seleccione una bicicleta por su número: ")
        bicicleta_seleccionada = next((b for b in bicicletas_disponibles if b.numero == int(bicicleta_numero)), None)
        
        if bicicleta_seleccionada:
            origen = input("Ingrese el origen del préstamo: ")
            destino = input("Ingrese el destino del préstamo: ")
            
            prestamo = Prestamo(usuario, bicicleta_seleccionada, origen, destino)
            prestamos.append(prestamo)
            bicicletas_disponibles.remove(bicicleta_seleccionada)
            bicicletas_en_uso.append(bicicleta_seleccionada)
            print("Préstamo registrado con éxito.")
        else:
            print("Bicicleta no válida.")
    else:
        print("Usuario no encontrado.")

def finalizar_prestamo():
    numero_tarjeta = input("Ingrese su número de tarjeta: ")
    usuario = next((u for u in usuarios if u.numero_tarjeta == numero_tarjeta), None)
    
    if usuario:
        bicicleta_en_uso = next((p for p in prestamos if p.usuario == usuario and p.bicicleta in bicicletas_en_uso), None)
        
        if bicicleta_en_uso:
            respuesta = input("¿Ha devuelto la bicicleta? (si/no): ").lower()
            
            if respuesta == "si":
                bicicletas_disponibles.append(bicicleta_en_uso.bicicleta)
                bicicletas_en_uso.remove(bicicleta_en_uso.bicicleta)
                prestamos.remove(bicicleta_en_uso)
                print("Bicicleta devuelta con éxito.")
            elif respuesta == "no":
                print("Por favor, devuelva la bicicleta lo antes posible.")
            else:
                print("Respuesta no válida.")
        else:
            print("No tiene una bicicleta en uso en este momento.")
    else:
        print("Usuario no encontrado.")

def listar_usuarios():
    print("Listado de usuarios:")
    for usuario in usuarios:
        print(f"Nombre: {usuario.nombre}, Número de tarjeta: {usuario.numero_tarjeta}")

def listar_prestamos():
    print("Listado de préstamos:")
    for prestamo in prestamos:
        print(f"Usuario: {prestamo.usuario.nombre}, Bicicleta: {prestamo.bicicleta.numero}, Origen: {prestamo.origen}, Destino: {prestamo.destino}")

while True:
    print("\nSistema de Préstamos de Bicicletas de la Ciudad")
    print("1. Registrar Usuario")
    print("2. Iniciar Préstamo")
    print("3. Finalizar Préstamo")
    print("4. Listar Usuarios")
    print("5. Listar Préstamos")
    print("6. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        registrar_usuario()
    elif opcion == "2":
        iniciar_prestamo()
    elif opcion == "3":
        finalizar_prestamo()
    elif opcion == "4":
        listar_usuarios()
    elif opcion == "5":
        listar_prestamos()
    elif opcion == "6":
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
