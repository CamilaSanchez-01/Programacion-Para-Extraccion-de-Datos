from numpy.ma.core import append

print(" Ejercicio 1\n")
# Alumna: Sanchez Parra Camila Grupo: 951
# Fecha de realizacion: 8 de febrero del 2025
# Descripcion del problema: Para este ejercicio se creo un sistema de reservacion
# creamos un set de habitaciones disponibles y uno donde se guardaran las reservas
# se crean las funciones
# funcion reserva guarda las habitaciones reservadas en la variable adecuada, y la remueve de las habitaciones disponibles
# funcion liberar esta vuekve a guardar las habitaciones disponibles liberandolas de la reservacion
# funcion disponible esta muestra las habitaciones disponibles
# al final se muestra una prueba de las funciones

habitaciones_dis = {101, 201, 301, 401, 501, 601}
habitaciones_reservadas = set()

def reserva(habitacion):
        if habitacion in habitaciones_dis:
            habitaciones_dis.remove(habitacion)
            habitaciones_reservadas.add(habitacion)
            print(f"Habitacion reservada: {habitacion}")

        else:
            print(f"La habitacion {habitacion} no se encuentra disponible")

def liberar(habitacion):
    if habitacion in habitaciones_reservadas:
        habitaciones_reservadas.remove(habitacion)
        habitaciones_dis.add(habitacion)
        print(f"La habitacion {habitacion}, ha sido liberada, gracias")
    else:
        print(f"La habitacion {habitacion}, no se encuentra liberada, vuelva a comprobar")

def disponible():
    print(f"Habitaciones disponibles: \n{sorted(habitaciones_dis)}")

print("ESTADO:")
disponible()

reserva(101)
reserva(401)
reserva(103)
disponible()

liberar(101)
liberar(501)
disponible()

reserva(501)
disponible()

print(" \n\nEjercicio 2\n")
# Alumna: Sanchez Parra Camila Grupo: 951
# Fecha de realizacion: 8 de febrero del 2025
# Descripcion del problema: Para este problema se creo un diccionario unico con codigos, asimismo se creo un diccionario inverso
# y se creo un mensaje el cual se hizo un codigo mediante el diccionario y asimismo se realizo lo opuesto

d_encriptado = {
    'a': '$%3', 'b': '8@*', 'c': '2&9','d': '@1r', 'e': '^e1', 'f': 'd#4',
    'g': '^t2', 'h': 'd3!', 'i': '6J5','j': '1@3', 'k': '>7<', 'l': '4&4',
    'm': '3d^', 'n': '3d&', 'o': '5t7','p': '4%6', 'q': '-&5', 'r': '3%/',
    's': 'd#1', 't': 'd+3', 'u': '3?h','v': '^*9', 'w': '7$6', 'x': '46?',
    'y': 'e$2', 'z': 'v^7'
}
d_desencriptado = {v:k for k, v in d_encriptado.items()}

def encriptar(mensaje):
    mensaje_encriptado = []
    for letra in mensaje.lower():
        if letra in d_encriptado:
            mensaje_encriptado.append(d_encriptado[letra])
        else:
            mensaje_encriptado += letra
    return mensaje_encriptado

def desencriptar(mensaje_encriptado):
    dm_desencriptado = []
    i = 0
    while i <len(mensaje_encriptado):
        cod = mensaje_encriptado[i:i+3]
        if cod in d_desencriptado:
            dm_desencriptado.append(d_desencriptado[cod])
            i += 3

        else:
            dm_desencriptado,append(mensaje_encriptado[i])
            i +=1

    return dm_desencriptado


mensaje_original = "Un 100 por este programa"
mensaje_encriptado = encriptar(mensaje_original)
print("Mensaje original: ", mensaje_original)
print("Mensaje encriptado: ", mensaje_encriptado)

mensaje_desencriptado = desencriptar(mensaje_encriptado)
print("Mensaje desencriptado: ", mensaje_desencriptado)




print(" \n\nEjercicio 3\n")
# Alumna: Sanchez Parra Camila Grupo: 951
# Fecha de realizacion: 8 de febrero del 2025
# Descripcion del problema: En este ejercicio se crea un diccionario de inventario con productos, claves y valores
# Se crean funciones para editar, eliminar los productos al igual que para agregar y eliminar productos
# y se crea una funcion para poder ver el inventario, asi como para realizar ventas de productos

inventario = {
    "P001":{
        "nombre": "Laptop",
        "precio":869.48,
        "en stock": 14
    },
    "P002":{
            "nombre": "Cargador Iphone",
            "precio": 245.8,
            "en stock": 32
    },
    "P003": {
        "nombre": "Cable hdmi",
        "precio": 158.21,
        "en stock": 5
    },
    "P004": {
        "nombre": "Bocina",
        "precio": 4365.3,
        "en stock": 4
    },
    "P005": {
        "nombre": "Silla reclinable",
        "precio": 2869.32,
        "en stock": 12
    },
    "P006": {
        "nombre": "Usb",
        "precio": 123.23,
        "en stock": 24
    },
    "P007": {
        "nombre": "Camara ",
        "precio": 3846.43,
        "en stock": 3
    },
    "P008": {
        "nombre": "Mouse",
        "precio": 639.35,
        "en stock": 67
    },
    "P009": {
        "nombre": "Audifonos inalambricos",
        "precio": 566.88,
        "en stock": 13
    },
    "P010": {
        "nombre": "Monitor",
        "precio": 2365.58,
        "en stock": 7
    },
    "P011": {
        "nombre": "Telefono",
        "precio": 1466.28,
        "en stock": 23
    },
    "P012": {
        "nombre": "Teclado",
        "precio": 139.58,
        "en stock": 9
    }
}

def agregar(key, nombre, precio, cantidad):
    if key in inventario:
        print(f"Este producto de codigo {key}, ya existe" )
    else:
        inventario[key] ={
            "nombre" : nombre,
            "precio" : precio,
            "en stock" : cantidad
        }
        print(f"Producto {key} ha sido agregado al inventario")

def editar(key, nombre=None, precio=None, cantidad=None):
    if key in inventario:
        if nombre:
            inventario[key]["nombre"] = nombre
        if precio:
            inventario[key]["precio"] = precio
        if cantidad:
            inventario[key]["en stock"] = cantidad

        print(f"El producto {key} se ha editado")
    else:
        print(f"El producto con codigo {key} no existe")
        return

def eliminar_prod(key):
    if key in inventario:
        k = inventario.pop(key)
        print(f"El producto {k} ha sido eliminado\n")
    else:
        print(f"El producto de codigo {key}, no existe\n" )

def venta(key, cant_vendida):
    if key in inventario:
        p = inventario[key]
        if p["en stock"] < cant_vendida:
            print(f"ERROR\n LA CANTIDAD DESEADA NO ESTA DISPONIBLE EN EL STOCK\n\n")
            return
        p["en stock"] -= cant_vendida
        print(f"Cantidad de la venta: {cant_vendida} unidades\n")

        total = cant_vendida*p["precio"]
        print(f"El total de la ventas es: ${total}\n")

    else:
        print(f"ERROR\n ESTE PRODUCTO NO EXISTE\n\n")
        return



def imprimir_inventario():
    if len(inventario) == 0:
        print("El inventario esta vacio")
        return
    for key, value in inventario.items():
        print(f"Clave: {key} \n"
              f"Nombre:{value['nombre']}\n"
              f"Precio: ${value['precio']}\n"
              f"Cantidad en Stock: {value['en stock']}\n"
              )

print("inventario incial:\n")
imprimir_inventario()

venta("P004", 4)

venta("P003", 6)

venta("P012", 5)

imprimir_inventario()

agregar("P001", "Laptop",3856.98, 13)
agregar("P0014","Laptop",3856.98,24)

editar("P0015", cantidad=23)
editar("P001", cantidad=34)

eliminar_prod("P0014")

print(f"Inventario despues de modificaciones:\n")

imprimir_inventario()



