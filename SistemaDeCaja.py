# Definir el diccionario para almacenar los valores por usuario
usuarios = {}

# Definir datos de prueba
usuarios["Gustavo"] = 400.00
usuarios["Carlos"] = 200.00

def registrar_usuarios():
    nombre = input("Introduce el nombre del usuario: ")
    if nombre in usuarios:
        print("El usuario ya está registrado")
    else:
        usuarios[nombre] = 0.00
        print(f"Usuario {nombre} agregado correctamente")

def depositar():
    nombre = input("Introduce el nombre del usuario: ")
    if nombre in usuarios:
        monto = float(input("Introduce el monto a depositar: "))
        usuarios[nombre] += monto
        print(f"Se han depositado {monto} a la cuenta de {nombre}.")
    else:
        print(f"Usuario {nombre} no existe")

def retirar():
    nombre = input("Introduce el nombre del usuario: ")
    
    if nombre in usuarios:
        retiro = float(input("Introduce el monto a retirar: "))
        if retiro > usuarios[nombre]:
            print(f"Se han retirado {retiro} de la cuenta de {nombre}.")
        else:
            usuarios[nombre] -= retiro
    else:
        print("Usuario no existente en el registro")

print(usuarios)
retirar()
print(usuarios)