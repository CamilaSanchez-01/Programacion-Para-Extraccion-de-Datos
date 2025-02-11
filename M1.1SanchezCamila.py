
print(" Ejercicio 1")
# Alumna: Sanchez Parra Camila Grupo: 951
# Fecha de realizacion: 8 de febrero del 2025
# Descripcion del problema: En este ejercicio se busca crear una clase llamada estadistica la cual guardara funciones que nos ayudara a realizar acciones de estadistica.
# Funciones:
# Frecuencia. Es la cantidad de veces que aparece un numerO,
# Moda. Es el numero que mas veces aparece,
# Histograma. el cual nos ayudara a "crear" un grafico visible con simbolos basada en la recopilacion de datos de la frecuencia y la moda
# Esto demostrando la cantidad de veces que aparece cada numero dentro de la lista

class Estadistica:
    def __init__(self,lista):
        self.lista = lista

    def frecuencia_num(self):
        frecuencia = {}
        for num in self.lista:
            if num in frecuencia:
                frecuencia [num] += 1
            else:
                frecuencia [num] = 1

        return list(frecuencia.items())
    def moda(self):
        frecuencias = self.frecuencia_num()

        num_mas_rep, mayor_freq = frecuencias[0]
        for num, frecuencia in frecuencias:
            if frecuencia > mayor_freq:
                num_mas_rep, mayor_freq = num, frecuencia

        return num_mas_rep

    def histograma(self):
        for num, rep in self.frecuencia_num():
            print(f"{num} {'*' * rep}")

lista = Estadistica([2, 3, 1, 4, 2, 5, 2, 3, 1, 1, 4, 4, 2, 3, 5, 4, 4, 3, 5, 2, 1, 3, 4, 2, 3, 4])
lista.histograma()

print("\n Ejercicio 2")
# Alumna: Sanchez Parra Camila Grupo: 951
# Fecha de realizacion: 8 de febrero del 2025
# Descripcion del problema: Para este problema se creo una lista en la cual se almacenaran los cambios que se haran en una hoja de excel.
# Se crean dos defs los cuales guardan dos funciones diferentes, uno registra los cambios positivos y el otro elimina o deshace movimiento.
# al final se agregan cambios, y tambien se elimina uno para verificar los cambios

historial_cambios = []

def regis_cambios(historial, celda, valor_ant):
    historial.append((celda, valor_ant))

def deshacer_cambio(historial):
    historial.pop()

regis_cambios(historial_cambios, 'A1', 10)
regis_cambios(historial_cambios, 'B2', 20)

print(historial_cambios)
deshacer_cambio(historial_cambios)

print(historial_cambios)



print("\n Ejercicio 3")
# Alumna: Sanchez Parra Camila Grupo: 951
# Fecha de realizacion: 8 de febrero del 2025
# Descripcion del problema: En este ejercicios se busca que un robot recorra un almacen, considerando los movimientos y que haya obstaculos en el almacen.
# Para ello se le da valor al almacen, al robot se le da una posicion, se cuentan los poductos, las filas, las columnas y se crea un set para los productos encontrados.
# Se crea condiciones para los movimientos, sumando y restando movimiento, y se crea la condicion de si aun no se recogia ese producto entonces se suma a los productos recogidos.
# Al final se busca que el robot recorra el almacen sin pasar por obstaculos y recogiendo todos los productos encontrados dentro del almacen.

def verificar_recogida(almacen, movimientos):
    filas = len(almacen)
    columnas = len(almacen[0])

    #posicion incial robot
    x, y =0,0

    tot_produc = sum(fila.count('P') for fila in almacen)
    produc_recogidos = 0

    prod_visitados = set()

    for mov in movimientos:
        if mov ==  "R" and y + 1 < columnas and almacen [x][y + 1] != '#':
            y +=1
        elif mov == "D" and x + 1 < filas and almacen [x + 1][y] != '#':
            x +=1
        elif mov == "L" and y - 1 >= 0 and almacen [x][y - 1] != '#':
            y -= 1
        elif mov == "U" and x - 1 >= 0 and almacen [x - 1][y] != '#':
             x -=1
        if almacen[x][y] == 'P' and (x, y) not in prod_visitados:
            produc_recogidos +=1
            prod_visitados. add((x, y))

    return produc_recogidos == tot_produc and (x, y) == (0, 0)


almacen = [
    [".", ",", "#","P"],
    [".", "#", ".", "."],
    ["P", ",", "P", "."],
    ["#", ",", "#", "."]
]
movimientos_correctos = ['D', 'D', 'R', 'R', 'U', 'R', 'U', 'D', 'L', 'D', 'L', 'L', 'U', 'U']
print(verificar_recogida(almacen, movimientos_correctos))
