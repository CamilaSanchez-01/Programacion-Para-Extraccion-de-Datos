# Índices, funciones loc e iloc pandas.

#Libreria
import pandas as pd

#Ejercicios a
# Alumna: Sanchez Parra Camila Grupo: 951
# Fecha de realizacion: 17 de Mayo del 2025
# Descripcion del problema: Crear Dataframe
# Datos
def crear():
    datos = {
        "enero":[300,200,345],
        "febrero":[300,200,350],
        "marzo":[550,300,205]
    }
    ventas = pd.DataFrame(datos, index=["A","B","C"])

    return ventas

#Ejercicios a
# Alumna: Sanchez Parra Camila Grupo: 951
# Fecha de realizacion: 17 de Mayo del 2025
# Descripcion del problema: Seleccionar datos usando loc e indices
def seleccionar_loc(df, producto=None, mes=None):
    if producto and mes:
        return df.loc[producto,mes]
    elif producto:
        return df.loc[producto]
    elif mes:
        return df[mes]
    else:
        return df

#Ejercicios b
# Alumna: Sanchez Parra Camila Grupo: 951
# Fecha de realizacion: 17 de Mayo del 2025
# Descripcion del problema: Seleccionar datos usando iloc e indices
def seleccionar_iloc(df, filas=None, columnas=None):
    return df.iloc[filas, columnas]

#Ejercicios c
# Alumna: Sanchez Parra Camila Grupo: 951
# Fecha de realizacion: 17 de Mayo del 2025
# Descripcion del problema: Cambiar valor de ventas de un producto y mes especifico
def cambio(df, producto, mes, nuevo_valor):
    print(f"Antes:\n{df}"
          f"\n\nDespues:")
    df.loc[producto, mes] = nuevo_valor
    return df

# Menu
if __name__ == "__main__":
    ventas=crear()
    print(f"Ventas\n{ventas}")

    print("\nEjercicios a")
    print("Ventas del producto A en enero")
    print(seleccionar_loc(ventas,"A","enero"))

    print("\nVentas de todos los productos en febrero")
    print(seleccionar_loc(ventas, mes="febrero"))

    print("\nVentas de todos los productos en el primer y tercer mes")
    print(seleccionar_loc(ventas, mes=["enero","marzo"]))

    print("\nEjercicios b")
    print("Ventas del primer mes para todos los productos")
    print(seleccionar_iloc(ventas, [0,1,2],0))

    print("\nVentas del segundo producto en todos los meses")
    print(seleccionar_iloc(ventas, 1,[0,1,2]))

    print("\nVentas del segundo y tercer mes para el primer producto")
    print(seleccionar_iloc(ventas, 0,[1,2]))

    print("\nEjercicio c")
    print("Cambiar valor produco B en febrero")
    ventas = cambio(ventas, "B","febrero", 354)
    print(ventas)